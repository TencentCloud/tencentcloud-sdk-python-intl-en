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
        :param Externals: Additional data
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param TimerAction: Timer name. Currently `TerminateInstances` is the only supported value.
        :type TimerAction: str
        :param ActionTime: Execution time, which must be at least 5 minutes later than the current time. For example, 2018-5-29 11:26:40.
        :type ActionTime: str
        """
        self.Externals = None
        self.TimerAction = None
        self.ActionTime = None


    def _deserialize(self, params):
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.TimerAction = params.get("TimerAction")
        self.ActionTime = params.get("ActionTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsRequest(AbstractModel):
    """AllocateHosts request structure.

    """

    def __init__(self):
        r"""
        :param Placement: Instance location. This parameter is used to specify the attributes of an instance, such as its availability zone and project.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param ClientToken: A string used to ensure the idempotency of the request.
        :type ClientToken: str
        :param HostChargePrepaid: Configuration of prepaid instances. You can use the parameter to specify the attributes of prepaid instances, such as the subscription period and the auto-renewal plan. This parameter is required for prepaid instances.
        :type HostChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.ChargePrepaid`
        :param HostChargeType: Instance billing model, only monthly or yearly subscription supported. Default value: `PREPAID'.
        :type HostChargeType: str
        :param HostType: CDH instance model. Default value: `HS1`.
        :type HostType: str
        :param HostCount: Quantity of CDH instances purchased. Default value: 1.
        :type HostCount: int
        :param TagSpecification: Tag description. You can specify the parameter to associate a tag with an instance.
        :type TagSpecification: list of TagSpecification
        """
        self.Placement = None
        self.ClientToken = None
        self.HostChargePrepaid = None
        self.HostChargeType = None
        self.HostType = None
        self.HostCount = None
        self.TagSpecification = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClientToken = params.get("ClientToken")
        if params.get("HostChargePrepaid") is not None:
            self.HostChargePrepaid = ChargePrepaid()
            self.HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        self.HostChargeType = params.get("HostChargeType")
        self.HostType = params.get("HostType")
        self.HostCount = params.get("HostCount")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateHostsResponse(AbstractModel):
    """AllocateHosts response structure.

    """

    def __init__(self):
        r"""
        :param HostIdSet: The ID list of the CVM instances newly created on the CDH.
        :type HostIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HostIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HostIdSet = params.get("HostIdSet")
        self.RequestId = params.get("RequestId")


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). The maximum number of instances in each request is 100. <br>You can obtain the available instance IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance IDs. <br><li>Call [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceIds: list of str
        :param KeyIds: Key ID(s). The maximum number of key pairs in each request is 100. The key pair ID is in the format of `skey-3glfot13`. <br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyIds: list of str
        :param ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before associating a key pair with it. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE.
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.KeyIds = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.KeyIds = params.get("KeyIds")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateInstancesKeyPairsResponse(AbstractModel):
    """AssociateInstancesKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupIds: ID of the security group to be associated, such as `sg-efil73jd`. Only one security group can be associated.
        :type SecurityGroupIds: list of str
        :param InstanceIds: ID of the instance bound in the format of ins-lesecurk. You can specify up to 100 instances in each request.
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChargePrepaid(AbstractModel):
    """Parameters related to the prepaid billing method, including the subscription period, the auto renewal logic, etc.

    """

    def __init__(self):
        r"""
        :param Period: Purchased usage period, in month. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36
        :type Period: int
        :param RenewFlag: Auto renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>Default value: NOTIFY_AND_AUTO_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param ChcId: CHC host ID
        :type ChcId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param SerialNumber: Server serial number
        :type SerialNumber: str
        :param InstanceState: CHC host status<br/>
<ul>
<li>REGISTERED: The CHC host is registered, but the out-of-band network and deployment network are not configured.</li>
<li>VPC_READY: The out-of-band network and deployment network are configured.</li>
<li>PREPARED: It’s ready and can be associated with a CVM.</li>
<li>ONLINE: It’s already associated with a CVM.</li>
</ul>
        :type InstanceState: str
        :param DeviceType: Device type
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeviceType: str
        :param Placement: Availability zone
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param BmcVirtualPrivateCloud: Out-of-band network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param BmcIp: Out-of-band network IP
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcIp: str
        :param BmcSecurityGroupIds: Out-of-band network security group ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcSecurityGroupIds: list of str
        :param DeployVirtualPrivateCloud: Deployment network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param DeployIp: Deployment network IP
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployIp: str
        :param DeploySecurityGroupIds: Deployment network security group ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeploySecurityGroupIds: list of str
        :param CvmInstanceId: ID of the associated CVM
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CvmInstanceId: str
        :param CreatedTime: Server creation time
        :type CreatedTime: str
        :param HardwareDescription: Instance hardware description, including CPU cores, memory capacity and disk capacity.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HardwareDescription: str
        :param CPU: CPU cores of the CHC host
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CPU: int
        :param Memory: Memory capacity of the CHC host (unit: GB)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Memory: int
        :param Disk: Disk capacity of the CHC host
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Disk: str
        :param BmcMAC: MAC address assigned under the out-of-band network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BmcMAC: str
        :param DeployMAC: MAC address assigned under the deployment network
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployMAC: str
        :param TenantType: Management type
HOSTING: Hosting
TENANT: Leasing
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TenantType: str
        :param DeployExtraConfig: CHC DHCP option, which is used for MiniOS debugging.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployExtraConfig: :class:`tencentcloud.cvm.v20170312.models.ChcDeployExtraConfig`
        """
        self.ChcId = None
        self.InstanceName = None
        self.SerialNumber = None
        self.InstanceState = None
        self.DeviceType = None
        self.Placement = None
        self.BmcVirtualPrivateCloud = None
        self.BmcIp = None
        self.BmcSecurityGroupIds = None
        self.DeployVirtualPrivateCloud = None
        self.DeployIp = None
        self.DeploySecurityGroupIds = None
        self.CvmInstanceId = None
        self.CreatedTime = None
        self.HardwareDescription = None
        self.CPU = None
        self.Memory = None
        self.Disk = None
        self.BmcMAC = None
        self.DeployMAC = None
        self.TenantType = None
        self.DeployExtraConfig = None


    def _deserialize(self, params):
        self.ChcId = params.get("ChcId")
        self.InstanceName = params.get("InstanceName")
        self.SerialNumber = params.get("SerialNumber")
        self.InstanceState = params.get("InstanceState")
        self.DeviceType = params.get("DeviceType")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("BmcVirtualPrivateCloud") is not None:
            self.BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self.BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self.BmcIp = params.get("BmcIp")
        self.BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self.DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self.DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self.DeployIp = params.get("DeployIp")
        self.DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.CreatedTime = params.get("CreatedTime")
        self.HardwareDescription = params.get("HardwareDescription")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.Disk = params.get("Disk")
        self.BmcMAC = params.get("BmcMAC")
        self.DeployMAC = params.get("DeployMAC")
        self.TenantType = params.get("TenantType")
        if params.get("DeployExtraConfig") is not None:
            self.DeployExtraConfig = ChcDeployExtraConfig()
            self.DeployExtraConfig._deserialize(params.get("DeployExtraConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChcHostDeniedActions(AbstractModel):
    """Describe details of actions not allowed for a CHC instance

    """

    def __init__(self):
        r"""
        :param ChcId: CHC instance ID
        :type ChcId: str
        :param State: CHC instance status
        :type State: str
        :param DenyActions: Actions not allowed for the current CHC instance
        :type DenyActions: list of str
        """
        self.ChcId = None
        self.State = None
        self.DenyActions = None


    def _deserialize(self, params):
        self.ChcId = params.get("ChcId")
        self.State = params.get("State")
        self.DenyActions = params.get("DenyActions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcRequest(AbstractModel):
    """ConfigureChcAssistVpc request structure.

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC host IDs
        :type ChcIds: list of str
        :param BmcVirtualPrivateCloud: Out-of-band network information
        :type BmcVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param BmcSecurityGroupIds: Out-of-band network security group list
        :type BmcSecurityGroupIds: list of str
        :param DeployVirtualPrivateCloud: Deployment network information
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param DeploySecurityGroupIds: Deployment network security group list
        :type DeploySecurityGroupIds: list of str
        """
        self.ChcIds = None
        self.BmcVirtualPrivateCloud = None
        self.BmcSecurityGroupIds = None
        self.DeployVirtualPrivateCloud = None
        self.DeploySecurityGroupIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        if params.get("BmcVirtualPrivateCloud") is not None:
            self.BmcVirtualPrivateCloud = VirtualPrivateCloud()
            self.BmcVirtualPrivateCloud._deserialize(params.get("BmcVirtualPrivateCloud"))
        self.BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self.DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self.DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self.DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcAssistVpcResponse(AbstractModel):
    """ConfigureChcAssistVpc response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConfigureChcDeployVpcRequest(AbstractModel):
    """ConfigureChcDeployVpc request structure.

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC instance ID
        :type ChcIds: list of str
        :param DeployVirtualPrivateCloud: Deployment network information
        :type DeployVirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param DeploySecurityGroupIds: Deployment network security group list
        :type DeploySecurityGroupIds: list of str
        """
        self.ChcIds = None
        self.DeployVirtualPrivateCloud = None
        self.DeploySecurityGroupIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        if params.get("DeployVirtualPrivateCloud") is not None:
            self.DeployVirtualPrivateCloud = VirtualPrivateCloud()
            self.DeployVirtualPrivateCloud._deserialize(params.get("DeployVirtualPrivateCloud"))
        self.DeploySecurityGroupIds = params.get("DeploySecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigureChcDeployVpcResponse(AbstractModel):
    """ConfigureChcDeployVpc response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDisasterRecoverGroupRequest(AbstractModel):
    """CreateDisasterRecoverGroup request structure.

    """

    def __init__(self):
        r"""
        :param Name: Name of the spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters.
        :type Name: str
        :param Type: Type of the spread placement group. Valid values: <br><li>HOST: physical machine <br><li>SW: switch <br><li>RACK: rack
        :type Type: str
        :param ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. <br>For more information, see 'How to ensure idempotency'.
        :type ClientToken: str
        """
        self.Name = None
        self.Type = None
        self.ClientToken = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisasterRecoverGroupResponse(AbstractModel):
    """CreateDisasterRecoverGroup response structure.

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupId: List of spread placement group IDs.
        :type DisasterRecoverGroupId: str
        :param Type: Type of the spread placement group. Valid values: <br><li>HOST: physical machine <br><li>SW: switch <br><li>RACK: rack.
        :type Type: str
        :param Name: Name of the spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters.
        :type Name: str
        :param CvmQuotaTotal: The maximum number of CVMs in a placement group.
        :type CvmQuotaTotal: int
        :param CurrentNum: The current number of CVMs in a placement group.
        :type CurrentNum: int
        :param CreateTime: Creation time of the placement group.
        :type CreateTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DisasterRecoverGroupId = None
        self.Type = None
        self.Name = None
        self.CvmQuotaTotal = None
        self.CurrentNum = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.CvmQuotaTotal = params.get("CvmQuotaTotal")
        self.CurrentNum = params.get("CurrentNum")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage request structure.

    """

    def __init__(self):
        r"""
        :param ImageName: Image name
        :type ImageName: str
        :param InstanceId: ID of the instance from which an image will be created. This parameter is required when using instance to create an image.
        :type InstanceId: str
        :param ImageDescription: Image description
        :type ImageDescription: str
        :param ForcePoweroff: Whether to force shut down an instance to create an image when a soft shutdown fails
        :type ForcePoweroff: str
        :param Sysprep: Whether to enable Sysprep when creating a Windows image.
Valid values: `TRUE` and `FALSE`; default value: `FALSE`.

Click [here](https://intl.cloud.tencent.com/document/product/213/43498?from_cn_redirect=1) to learn more about Sysprep.
        :type Sysprep: str
        :param DataDiskIds: Specified data disk ID included in the full image created from the instance.
        :type DataDiskIds: list of str
        :param SnapshotIds: Specified snapshot ID used to create an image. A system disk snapshot must be included. It cannot be passed together with `InstanceId`.
        :type SnapshotIds: list of str
        :param DryRun: Success status of this request, without affecting the resources involved
        :type DryRun: bool
        :param TagSpecification: Tag description list. This parameter is used to bind a tag to a custom image.
        :type TagSpecification: list of TagSpecification
        """
        self.ImageName = None
        self.InstanceId = None
        self.ImageDescription = None
        self.ForcePoweroff = None
        self.Sysprep = None
        self.DataDiskIds = None
        self.SnapshotIds = None
        self.DryRun = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.ImageName = params.get("ImageName")
        self.InstanceId = params.get("InstanceId")
        self.ImageDescription = params.get("ImageDescription")
        self.ForcePoweroff = params.get("ForcePoweroff")
        self.Sysprep = params.get("Sysprep")
        self.DataDiskIds = params.get("DataDiskIds")
        self.SnapshotIds = params.get("SnapshotIds")
        self.DryRun = params.get("DryRun")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage response structure.

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID.
Note: This field may return null, indicating that no valid value was found.
        :type ImageId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param KeyName: Name of the key pair, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param ProjectId: The ID of the project to which the new key pair belongs.
You can query the project IDs in two ways:
<li>Query the project IDs in the project list.
<li>Call `DescribeProject` and look for `projectId` in the response.
        :type ProjectId: int
        :param TagSpecification: Tag description list. This parameter is used to bind a tag to a key pair.
        :type TagSpecification: list of TagSpecification
        """
        self.KeyName = None
        self.ProjectId = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param KeyPair: Key pair information.
        :type KeyPair: :class:`tencentcloud.cvm.v20170312.models.KeyPair`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyPair = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self.KeyPair = KeyPair()
            self.KeyPair._deserialize(params.get("KeyPair"))
        self.RequestId = params.get("RequestId")


class CreateLaunchTemplateVersionRequest(AbstractModel):
    """CreateLaunchTemplateVersion request structure.

    """

    def __init__(self):
        r"""
        :param Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone, project, and CDH (for dedicated CVMs)
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param LaunchTemplateId: Instance launch template ID. This parameter is used as a basis for creating new template versions.
        :type LaunchTemplateId: str
        :param LaunchTemplateVersion: This parameter, when specified, is used to create instance launch templates. If this parameter is not specified, the default version will be used.
        :type LaunchTemplateVersion: int
        :param LaunchTemplateVersionDescription: Description of instance launch template versions. This parameter can contain 2-256 characters.
        :type LaunchTemplateVersionDescription: str
        :param InstanceType: The instance model. Different resource specifications are specified for different instance models.
<br><li>To view specific values for `PREPAID` or `POSTPAID_BY_HOUR` instances, you can call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If this parameter is not specified, the system will specify the default model according to the dynamic resource sales in the current region. <br><li>For `CDHPAID` instances, the value of this parameter is in the format of `CDH_XCXG` based on the number of CPU cores and memory capacity. For example, if you want to create a CDH instance with a single-core CPU and 1 GB memory, you need to specify this parameter as `CDH_1C1G`.
        :type InstanceType: str
        :param ImageId: The [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><li>Marketplace images (for Chinese mainland only)</li><br/>To check the image ID:<br/><li>For public images, custom images, and shared images, go to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE). For marketplace images, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1), pass in `InstanceType` to retrieve the list of images supported by the current model, and then find the `ImageId` in the response.</li>
        :type ImageId: str
        :param SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: The configuration information of instance data disks. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC, CLOUD_PREMIUM, or CLOUD_SSD data disks.
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: Configuration information of VPC. This parameter is used to specify VPC ID and subnet ID, etc. If this parameter is not specified, the classic network is used by default. If a VPC IP is specified in this parameter, it indicates the primary ENI IP of each instance. The value of parameter InstanceCount must be same as the number of VPC IPs, which cannot be greater than 20.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: Number of instances to be purchased. Value range for monthly-subscribed instances: [1, 300]. Value range for pay-as-you-go instances: [1, 100]. Default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on quota, see CVM instance [Purchase Limits](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param InstanceName: Instance name to be displayed. <br><li>If this parameter is not specified, "Unnamed" will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`. </li><li>This parameter can contain up to 60 characters, including the pattern string.
        :type InstanceName: str
        :param LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will be associated with default security groups.
        :type SecurityGroupIds: list of str
        :param EnhancedService: Enhanced service. You can use this parameter to specify whether to enable services such as Anti-DDoS and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Anti-DDoS are enabled for public images by default. However, for custom images and images from the marketplace, Anti-DDoS and Cloud Monitor are not enabled by default. The original services in the image will be retained.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        :param HostName: Host name of the CVM. <br><li>Dots (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name. <br><li>For Windows instances, the host name must be 2-15 characters long and can contain uppercase and lowercase letters, numbers, and hyphens (-). It cannot contain dots (.) or contain only numbers. <br><li>For other instances, such as Linux instances, the host name must be 2-60 characters long. It supports multiple dots (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two dots (.).
        :type HostName: str
        :param ActionTimer: Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported.
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param DisasterRecoverGroupIds: Placement group ID. You can only specify one.
        :type DisasterRecoverGroupIds: list of str
        :param TagSpecification: The tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances.
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param UserData: User data provided to the instance. This parameter needs to be encoded in base64 format with the maximum size of 16KB. For more information on how to get the value of this parameter, see the commands you need to execute on startup for [Windows](https://intl.cloud.tencent.com/document/product/213/17526) or [Linux](https://intl.cloud.tencent.com/document/product/213/17525).
        :type UserData: str
        :param DryRun: Whether the request is a dry run only.
`true`: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available.
If the dry run fails, the corresponding error code will be returned.
If the dry run succeeds, the RequestId will be returned.
`false` (default value): send a normal request and create instance(s) if all the requirements are met.
        :type DryRun: bool
        :param CamRoleName: CAM role name, which can be obtained from the `roleName` field in the response of the [`DescribeRoleList`](https://intl.cloud.tencent.com/document/product/598/36223?from_cn_redirect=1) API.
        :type CamRoleName: str
        :param HpcClusterId: HPC cluster ID. The HPC cluster must and can only be specified for a high-performance computing instance.
        :type HpcClusterId: str
        :param InstanceChargeType: Instance [billing mode](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1). Valid values: <br><li>`PREPAID`: monthly subscription <br><li>`POSTPAID_BY_HOUR`: pay-as-you-go on an hourly basis <br><li>`CDHPAID`: billed on the associated CDH instance. <br><li>`SPOTPAID`: spot instances. <br>Default value: `POSTPAID_BY_HOUR`.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: Enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: Do not enable the instance protection.<br><br>Default value: `FALSE`.
        :type DisableApiTermination: bool
        """
        self.Placement = None
        self.LaunchTemplateId = None
        self.LaunchTemplateVersion = None
        self.LaunchTemplateVersionDescription = None
        self.InstanceType = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.ActionTimer = None
        self.DisasterRecoverGroupIds = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.UserData = None
        self.DryRun = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.DisableApiTermination = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        self.LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self.InstanceType = params.get("InstanceType")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.UserData = params.get("UserData")
        self.DryRun = params.get("DryRun")
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLaunchTemplateVersionResponse(AbstractModel):
    """CreateLaunchTemplateVersion response structure.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateVersionNumber: Version number of the new instance launch template.
        :type LaunchTemplateVersionNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LaunchTemplateVersionNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchTemplateVersionNumber = params.get("LaunchTemplateVersionNumber")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Describes data disk information.

    """

    def __init__(self):
        r"""
        :param DiskSize: Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.
        :type DiskSize: int
        :param DiskType: Data disk type. For more information about limits on different data disk types, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values: <br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>LOCAL_NVME: local NVME disk, specified in the `InstanceType`<br><li>LOCAL_PRO: local HDD disk, specified in the `InstanceType`<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: Tremendous SSD<br><li>CLOUD_BSSD: Balanced SSD<br><br>Default value: LOCAL_BASIC.<br><br>This parameter is invalid for the `ResizeInstanceDisk` API.
        :type DiskType: str
        :param DiskId: Data disk ID. Note that it’s not available for `LOCAL_BASIC` and `LOCAL_SSD` disks.
It is only used as a response parameter for APIs such as `DescribeInstances`, and cannot be used as a request parameter for APIs such as `RunInstances`.
        :type DiskId: str
        :param DeleteWithInstance: Whether to terminate the data disk when its CVM is terminated. Valid values:
<li>TRUE: terminate the data disk when its CVM is terminated. This value only supports pay-as-you-go cloud disks billed on an hourly basis.
<li>FALSE: retain the data disk when its CVM is terminated.<br>
Default value: TRUE<br>
Currently this parameter is only used in the `RunInstances` API.
Note: This field may return null, indicating that no valid value is found.
        :type DeleteWithInstance: bool
        :param SnapshotId: Data disk snapshot ID. The size of the selected data disk snapshot must be smaller than that of the data disk.
Note: This field may return null, indicating that no valid value is found.
        :type SnapshotId: str
        :param Encrypt: Specifies whether the data disk is encrypted. Valid values: 
<li>TRUE: encrypted
<li>FALSE: not encrypted<br>
Default value: FALSE<br>
This parameter is only used with `RunInstances`.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Encrypt: bool
        :param KmsKeyId: ID of the custom CMK in the format of UUID or “kms-abcd1234”. This parameter is used to encrypt cloud disks.

Currently, this parameter is only used in the `RunInstances` API.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KmsKeyId: str
        :param ThroughputPerformance: Cloud disk performance, in MB/s
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ThroughputPerformance: int
        :param CdcId: ID of the dedicated cluster to which the instance belongs.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CdcId: str
        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskId = None
        self.DeleteWithInstance = None
        self.SnapshotId = None
        self.Encrypt = None
        self.KmsKeyId = None
        self.ThroughputPerformance = None
        self.CdcId = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.SnapshotId = params.get("SnapshotId")
        self.Encrypt = params.get("Encrypt")
        self.KmsKeyId = params.get("KmsKeyId")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsRequest(AbstractModel):
    """DeleteDisasterRecoverGroups request structure.

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupIds: ID list of spread placement groups, obtainable via the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/api/213/17810?from_cn_redirect=1) API. You can operate up to 100 spread placement groups in each request.
        :type DisasterRecoverGroupIds: list of str
        """
        self.DisasterRecoverGroupIds = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDisasterRecoverGroupsResponse(AbstractModel):
    """DeleteDisasterRecoverGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImagesRequest(AbstractModel):
    """DeleteImages request structure.

    """

    def __init__(self):
        r"""
        :param ImageIds: List of the IDs of the instances to be deleted.
        :type ImageIds: list of str
        :param DeleteBindedSnap: Whether to delete the snapshot associated with the image
        :type DeleteBindedSnap: bool
        :param DryRun: Check whether deleting an image is supported
        :type DryRun: bool
        """
        self.ImageIds = None
        self.DeleteBindedSnap = None
        self.DryRun = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        self.DeleteBindedSnap = params.get("DeleteBindedSnap")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImagesResponse(AbstractModel):
    """DeleteImages response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteKeyPairsRequest(AbstractModel):
    """DeleteKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param KeyIds: Key ID(s). The maximum number of key pairs in each request is 100. <br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKeyPairsResponse(AbstractModel):
    """DeleteKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLaunchTemplateRequest(AbstractModel):
    """DeleteLaunchTemplate request structure.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        """
        self.LaunchTemplateId = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateResponse(AbstractModel):
    """DeleteLaunchTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLaunchTemplateVersionsRequest(AbstractModel):
    """DeleteLaunchTemplateVersions request structure.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        :param LaunchTemplateVersions: List of instance launch template versions.
        :type LaunchTemplateVersions: list of int
        """
        self.LaunchTemplateId = None
        self.LaunchTemplateVersions = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLaunchTemplateVersionsResponse(AbstractModel):
    """DeleteLaunchTemplateVersions response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeChcDeniedActionsRequest(AbstractModel):
    """DescribeChcDeniedActions request structure.

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC instance ID
        :type ChcIds: list of str
        """
        self.ChcIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeChcDeniedActionsResponse(AbstractModel):
    """DescribeChcDeniedActions response structure.

    """

    def __init__(self):
        r"""
        :param ChcHostDeniedActionSet: Actions not allowed for the CHC instance
        :type ChcHostDeniedActionSet: list of ChcHostDeniedActions
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ChcHostDeniedActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ChcHostDeniedActionSet") is not None:
            self.ChcHostDeniedActionSet = []
            for item in params.get("ChcHostDeniedActionSet"):
                obj = ChcHostDeniedActions()
                obj._deserialize(item)
                self.ChcHostDeniedActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeChcHostsRequest(AbstractModel):
    """DescribeChcHosts request structure.

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC host ID. Up to 100 instances per request is allowed. `ChcIds` and `Filters` cannot be specified at the same time.
        :type ChcIds: list of str
        :param Filters: <li><strong>zone</strong></li>
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
        :param Offset: The offset. Default value: `0`. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param Limit: The number of returned results. Default value: `20`. Maximum value: `100`. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self.ChcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
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
        


class DescribeChcHostsResponse(AbstractModel):
    """DescribeChcHosts response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible instances
        :type TotalCount: int
        :param ChcHostSet: List of returned instances
        :type ChcHostSet: list of ChcHost
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ChcHostSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ChcHostSet") is not None:
            self.ChcHostSet = []
            for item in params.get("ChcHostSet"):
                obj = ChcHost()
                obj._deserialize(item)
                self.ChcHostSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupQuotaRequest(AbstractModel):
    """DescribeDisasterRecoverGroupQuota request structure.

    """


class DescribeDisasterRecoverGroupQuotaResponse(AbstractModel):
    """DescribeDisasterRecoverGroupQuota response structure.

    """

    def __init__(self):
        r"""
        :param GroupQuota: The maximum number of placement groups that can be created.
        :type GroupQuota: int
        :param CurrentNum: The number of placement groups that have been created by the current user.
        :type CurrentNum: int
        :param CvmInHostGroupQuota: Quota on instances in a physical-machine-type disaster recovery group.
        :type CvmInHostGroupQuota: int
        :param CvmInSwGroupQuota: Quota on instances in a switch-type disaster recovery group.
        :type CvmInSwGroupQuota: int
        :param CvmInRackGroupQuota: Quota on instances in a rack-type disaster recovery group.
        :type CvmInRackGroupQuota: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.GroupQuota = None
        self.CurrentNum = None
        self.CvmInHostGroupQuota = None
        self.CvmInSwGroupQuota = None
        self.CvmInRackGroupQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupQuota = params.get("GroupQuota")
        self.CurrentNum = params.get("CurrentNum")
        self.CvmInHostGroupQuota = params.get("CvmInHostGroupQuota")
        self.CvmInSwGroupQuota = params.get("CvmInSwGroupQuota")
        self.CvmInRackGroupQuota = params.get("CvmInRackGroupQuota")
        self.RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupsRequest(AbstractModel):
    """DescribeDisasterRecoverGroups request structure.

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupIds: ID list of spread placement groups. You can operate up to 100 spread placement groups in each request.
        :type DisasterRecoverGroupIds: list of str
        :param Name: Name of a spread placement group. Fuzzy match is supported.
        :type Name: str
        :param Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Offset: int
        :param Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Limit: int
        """
        self.DisasterRecoverGroupIds = None
        self.Name = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisasterRecoverGroupsResponse(AbstractModel):
    """DescribeDisasterRecoverGroups response structure.

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupSet: Information on spread placement groups.
        :type DisasterRecoverGroupSet: list of DisasterRecoverGroup
        :param TotalCount: Total number of placement groups of the user.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DisasterRecoverGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DisasterRecoverGroupSet") is not None:
            self.DisasterRecoverGroupSet = []
            for item in params.get("DisasterRecoverGroupSet"):
                obj = DisasterRecoverGroup()
                obj._deserialize(item)
                self.DisasterRecoverGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostsRequest(AbstractModel):
    """DescribeHosts request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <li><strong>zone</strong></li>
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
        :param Offset: Offset; default value: 0.
        :type Offset: int
        :param Limit: Number of results returned; default value: 20; maximum: 100.
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
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
        


class DescribeHostsResponse(AbstractModel):
    """DescribeHosts response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of CDH instances meeting the query conditions
        :type TotalCount: int
        :param HostSet: Information on CDH instances
        :type HostSet: list of HostItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.HostSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HostSet") is not None:
            self.HostSet = []
            for item in params.get("HostSet"):
                obj = HostItem()
                obj._deserialize(item)
                self.HostSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageQuotaRequest(AbstractModel):
    """DescribeImageQuota request structure.

    """


class DescribeImageQuotaResponse(AbstractModel):
    """DescribeImageQuota response structure.

    """

    def __init__(self):
        r"""
        :param ImageNumQuota: The image quota of an account
        :type ImageNumQuota: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageNumQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageNumQuota = params.get("ImageNumQuota")
        self.RequestId = params.get("RequestId")


class DescribeImageSharePermissionRequest(AbstractModel):
    """DescribeImageSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param ImageId: The ID of the image to be shared
        :type ImageId: str
        """
        self.ImageId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSharePermissionResponse(AbstractModel):
    """DescribeImageSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param SharePermissionSet: Information on image sharing.
        :type SharePermissionSet: list of SharePermission
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SharePermissionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self.SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self.SharePermissionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages request structure.

    """

    def __init__(self):
        r"""
        :param ImageIds: List of image IDs, such as `img-gvbnzy6f`. For the format of array-type parameters, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>View the image IDs in the [Image Console](https://console.cloud.tencent.com/cvm/image).
        :type ImageIds: list of str
        :param Filters: Filters. Each request can have up to 10 `Filters`, and 5 `Filters.Values` for each filter. `ImageIds` and `Filters` cannot be specified at the same time. See details:

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
        :param Offset: Offset; default value: 0. For more information on `Offset`, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).
        :type Offset: int
        :param Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).
        :type Limit: int
        :param InstanceType: Instance type, e.g. `S1.SMALL1`
        :type InstanceType: str
        """
        self.ImageIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages response structure.

    """

    def __init__(self):
        r"""
        :param ImageSet: Information on an image, including its state and attributes.
        :type ImageSet: list of Image
        :param TotalCount: Number of images meeting the filtering conditions.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImageSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageSet") is not None:
            self.ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self.ImageSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs request structure.

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs response structure.

    """

    def __init__(self):
        r"""
        :param ImportImageOsListSupported: Supported operating system types of imported images.
        :type ImportImageOsListSupported: :class:`tencentcloud.cvm.v20170312.models.ImageOsList`
        :param ImportImageOsVersionSet: Supported operating system versions of imported images. 
        :type ImportImageOsVersionSet: list of OsVersion
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ImportImageOsListSupported = None
        self.ImportImageOsVersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self.ImportImageOsListSupported = ImageOsList()
            self.ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self.ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self.ImportImageOsVersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceFamilyConfigsRequest(AbstractModel):
    """DescribeInstanceFamilyConfigs request structure.

    """


class DescribeInstanceFamilyConfigsResponse(AbstractModel):
    """DescribeInstanceFamilyConfigs response structure.

    """

    def __init__(self):
        r"""
        :param InstanceFamilyConfigSet: List of instance model families
        :type InstanceFamilyConfigSet: list of InstanceFamilyConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceFamilyConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfigSet") is not None:
            self.InstanceFamilyConfigSet = []
            for item in params.get("InstanceFamilyConfigSet"):
                obj = InstanceFamilyConfig()
                obj._deserialize(item)
                self.InstanceFamilyConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesOperationLimitRequest(AbstractModel):
    """DescribeInstancesOperationLimit request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Query by instance ID(s). You can obtain the instance IDs from the value of `InstanceId` returned by the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API. For example, instance ID: ins-xxxxxxxx. (For the specific format, refer to section `ids.N` of the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).) You can query up to 100 instances in each request.
        :type InstanceIds: list of str
        :param Operation: Operation on the instance(s).
<li> INSTANCE_DEGRADE: downgrade the instance configurations</li>
        :type Operation: str
        """
        self.InstanceIds = None
        self.Operation = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesOperationLimitResponse(AbstractModel):
    """DescribeInstancesOperationLimit response structure.

    """

    def __init__(self):
        r"""
        :param InstanceOperationLimitSet: The maximum number of times you can modify the instance configurations (degrading the configurations)
        :type InstanceOperationLimitSet: list of OperationCountLimit
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceOperationLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceOperationLimitSet") is not None:
            self.InstanceOperationLimitSet = []
            for item in params.get("InstanceOperationLimitSet"):
                obj = OperationCountLimit()
                obj._deserialize(item)
                self.InstanceOperationLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Query by instance ID(s). For example, instance ID: `ins-xxxxxxxx`. For the specific format, refer to section `Ids.N` of the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can query up to 100 instances in each request. However, `InstanceIds` and `Filters` cannot be specified at the same time.
        :type InstanceIds: list of str
        :param Filters: Filters
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
        :param Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Offset: int
        :param Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Limit: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
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
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of instances meeting the filtering conditions.
        :type TotalCount: int
        :param InstanceSet: Detailed instance information.
        :type InstanceSet: list of Instance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesStatusRequest(AbstractModel):
    """DescribeInstancesStatus request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Query by instance ID(s). For example, instance ID: `ins-xxxxxxxx`. For the specific format, refer to section `Ids.N` of the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can query up to 100 instances in each request.
        :type InstanceIds: list of str
        :param Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Offset: int
        :param Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377).
        :type Limit: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesStatusResponse(AbstractModel):
    """DescribeInstancesStatus response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of instance states meeting the filtering conditions.
        :type TotalCount: int
        :param InstanceStatusSet: [Instance status](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) list.
        :type InstanceStatusSet: list of InstanceStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceStatusSet") is not None:
            self.InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = InstanceStatus()
                obj._deserialize(item)
                self.InstanceStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternetChargeTypeConfigsRequest(AbstractModel):
    """DescribeInternetChargeTypeConfigs request structure.

    """


class DescribeInternetChargeTypeConfigsResponse(AbstractModel):
    """DescribeInternetChargeTypeConfigs response structure.

    """

    def __init__(self):
        r"""
        :param InternetChargeTypeConfigSet: List of network billing methods.
        :type InternetChargeTypeConfigSet: list of InternetChargeTypeConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InternetChargeTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InternetChargeTypeConfigSet") is not None:
            self.InternetChargeTypeConfigSet = []
            for item in params.get("InternetChargeTypeConfigSet"):
                obj = InternetChargeTypeConfig()
                obj._deserialize(item)
                self.InternetChargeTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param KeyIds: Key pair ID(s) in the format of `skey-11112222`. This API supports using multiple IDs as filters at the same time. For more information on the format of this parameter, see the `id.N` section in [API Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You cannot specify `KeyIds` and `Filters` at the same time. You can log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the key pair IDs.
        :type KeyIds: list of str
        :param Filters: Filters
<li> `project-id` - Integer - Optional - Filter by project ID. To view the list of project IDs, you can go to [Project Management](https://console.cloud.tencent.com/project), or call the `DescribeProject` API and look for `projectId` in the response.</li>
<li> `key-name` - String - Optional - Filter by key pair name.</li>You cannot specify `KeyIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Offset: Offset; default value: 0. For more information on `Offset`, see the corresponding sections in API [Introduction](https://intl.cloud.tencent.com/document/product/377). Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Offset: int
        :param Limit: Number of results returned; default value: 20; maximum: 100. For more information on `Limit`, see the corresponding section in API [Introduction](https://intl.cloud.tencent.com/document/product/377). 
        :type Limit: int
        """
        self.KeyIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
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
        


class DescribeKeyPairsResponse(AbstractModel):
    """DescribeKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of key pairs meeting the filtering conditions.
        :type TotalCount: int
        :param KeyPairSet: Detailed information on key pairs.
        :type KeyPairSet: list of KeyPair
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.KeyPairSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyPairSet") is not None:
            self.KeyPairSet = []
            for item in params.get("KeyPairSet"):
                obj = KeyPair()
                obj._deserialize(item)
                self.KeyPairSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLaunchTemplateVersionsRequest(AbstractModel):
    """DescribeLaunchTemplateVersions request structure.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        :param LaunchTemplateVersions: List of instance launch templates.
        :type LaunchTemplateVersions: list of int non-negative
        :param MinVersion: The minimum version number specified, which defaults to 0.
        :type MinVersion: int
        :param MaxVersion: The maximum version number specified, which defaults to 30.
        :type MaxVersion: int
        :param Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param DefaultVersion: Specify whether to query the default version. This parameter and `LaunchTemplateVersions` cannot be specified at the same time.
        :type DefaultVersion: bool
        """
        self.LaunchTemplateId = None
        self.LaunchTemplateVersions = None
        self.MinVersion = None
        self.MaxVersion = None
        self.Offset = None
        self.Limit = None
        self.DefaultVersion = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersions = params.get("LaunchTemplateVersions")
        self.MinVersion = params.get("MinVersion")
        self.MaxVersion = params.get("MaxVersion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLaunchTemplateVersionsResponse(AbstractModel):
    """DescribeLaunchTemplateVersions response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of instance launch templates.
        :type TotalCount: int
        :param LaunchTemplateVersionSet: Set of instance launch template versions.
        :type LaunchTemplateVersionSet: list of LaunchTemplateVersionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.LaunchTemplateVersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateVersionSet") is not None:
            self.LaunchTemplateVersionSet = []
            for item in params.get("LaunchTemplateVersionSet"):
                obj = LaunchTemplateVersionInfo()
                obj._deserialize(item)
                self.LaunchTemplateVersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLaunchTemplatesRequest(AbstractModel):
    """DescribeLaunchTemplates request structure.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateIds: Instance launch template ID. ID of one or more instance launch templates. If not specified, all templates of the user will be displayed.
        :type LaunchTemplateIds: list of str
        :param Filters: <p style="padding-left: 30px;">Filter by [<strong>LaunchTemplateName</strong>].</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Optional</p>
The maximum number of `Filters` in each request is 10. The upper limit for `Filter.Values` is 5. This parameter cannot specify `LaunchTemplateIds` and `Filters` at the same time.
        :type Filters: list of Filter
        :param Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self.LaunchTemplateIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.LaunchTemplateIds = params.get("LaunchTemplateIds")
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
        


class DescribeLaunchTemplatesResponse(AbstractModel):
    """DescribeLaunchTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible instance templates.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param LaunchTemplateSet: List of instance details
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateSet: list of LaunchTemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.LaunchTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LaunchTemplateSet") is not None:
            self.LaunchTemplateSet = []
            for item in params.get("LaunchTemplateSet"):
                obj = LaunchTemplateInfo()
                obj._deserialize(item)
                self.LaunchTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of regions
        :type TotalCount: int
        :param RegionSet: List of regions
        :type RegionSet: list of RegionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReservedInstancesConfigInfosRequest(AbstractModel):
    """DescribeReservedInstancesConfigInfos request structure.

    """

    def __init__(self):
        r"""
        :param Filters: zone
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
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesConfigInfosResponse(AbstractModel):
    """DescribeReservedInstancesConfigInfos response structure.

    """

    def __init__(self):
        r"""
        :param ReservedInstanceConfigInfos: Static configurations of the reserved instance.
        :type ReservedInstanceConfigInfos: list of ReservedInstanceConfigInfoItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReservedInstanceConfigInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReservedInstanceConfigInfos") is not None:
            self.ReservedInstanceConfigInfos = []
            for item in params.get("ReservedInstanceConfigInfos"):
                obj = ReservedInstanceConfigInfoItem()
                obj._deserialize(item)
                self.ReservedInstanceConfigInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReservedInstancesOfferingsRequest(AbstractModel):
    """DescribeReservedInstancesOfferings request structure.

    """

    def __init__(self):
        r"""
        :param DryRun: Dry run. Default value: false.
        :type DryRun: bool
        :param Offset: The offset. Default value: 0. For more information on `Offset`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param Limit: The number of returned results. Default value: 20. Maximum value: 100. For more information on `Limit`, see the relevant sections in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param MaxDuration: The maximum duration as a filter, 
in seconds.
Default value: 94608000.
        :type MaxDuration: int
        :param MinDuration: The minimum duration as a filter, 
in seconds.
Default value: 2592000.
        :type MinDuration: int
        :param Filters: <li><strong>zone</strong></li>
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
        self.DryRun = None
        self.Offset = None
        self.Limit = None
        self.MaxDuration = None
        self.MinDuration = None
        self.Filters = None


    def _deserialize(self, params):
        self.DryRun = params.get("DryRun")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MaxDuration = params.get("MaxDuration")
        self.MinDuration = params.get("MinDuration")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReservedInstancesOfferingsResponse(AbstractModel):
    """DescribeReservedInstancesOfferings response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of Reserved Instances that meet the condition.
        :type TotalCount: int
        :param ReservedInstancesOfferingsSet: The list of Reserved Instances that meet the condition.
        :type ReservedInstancesOfferingsSet: list of ReservedInstancesOffering
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReservedInstancesOfferingsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReservedInstancesOfferingsSet") is not None:
            self.ReservedInstancesOfferingsSet = []
            for item in params.get("ReservedInstancesOfferingsSet"):
                obj = ReservedInstancesOffering()
                obj._deserialize(item)
                self.ReservedInstancesOfferingsSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeZoneInstanceConfigInfos request structure.

    """

    def __init__(self):
        r"""
        :param Filters: <li> instance-charge-type-String-required: no-(filter) billing mode of instances. (POSTPAID_BY_HOUR: pay-as-you-go billing by hour | SPOTPAID: spot billing, which is suitable for a [spot instance] (https://intl.cloud.Tencent.com/document/product/213/17817) | CDHPAID: CDH billing, that is, billing only for CDH, but not for the instances on CDH. )  </li>
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeZoneInstanceConfigInfos response structure.

    """

    def __init__(self):
        r"""
        :param InstanceTypeQuotaSet: List of model configurations for the availability zone.
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceTypeQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self.InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self.InstanceTypeQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of availability zones.
        :type TotalCount: int
        :param ZoneSet: List of availability zones.
        :type ZoneSet: list of ZoneInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). The maximum number of instances in each request is 100. <br><br>You can obtain the available instance IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance IDs. <br><li>Call [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceIds: list of str
        :param KeyIds: List of key pair IDs. The maximum number of key pairs in each request is 100. The key pair ID is in the format of `skey-11112222`. <br><br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyIds: list of str
        :param ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before disassociating a key pair from it. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE.
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.KeyIds = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.KeyIds = params.get("KeyIds")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        r"""
        :param SecurityGroupIds: ID of the security group to be disassociated, such as `sg-efil73jd`. Only one security group can be disassociated.
        :type SecurityGroupIds: list of str
        :param InstanceIds: ID(s) of the instance(s) to be disassociated,such as `ins-lesecurk`. You can specify multiple instances.
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisasterRecoverGroup(AbstractModel):
    """Information on disaster recovery groups

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupId: ID of a spread placement group.
        :type DisasterRecoverGroupId: str
        :param Name: Name of a spread placement group, which must be 1-60 characters long.
        :type Name: str
        :param Type: Type of a spread placement group. Valid values: <br><li>HOST: physical machine <br><li>SW: switch <br><li>RACK: rack.
        :type Type: str
        :param CvmQuotaTotal: The maximum number of CVMs that can be hosted in a spread placement group.
        :type CvmQuotaTotal: int
        :param CurrentNum: The current number of CVMs in a spread placement group.
        :type CurrentNum: int
        :param InstanceIds: The list of CVM IDs in a spread placement group.
Note: This field may return null, indicating that no valid value was found.
        :type InstanceIds: list of str
        :param CreateTime: Creation time of a spread placement group.
Note: This field may return null, indicating that no valid value is found.
        :type CreateTime: str
        """
        self.DisasterRecoverGroupId = None
        self.Name = None
        self.Type = None
        self.CvmQuotaTotal = None
        self.CurrentNum = None
        self.InstanceIds = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.CvmQuotaTotal = params.get("CvmQuotaTotal")
        self.CurrentNum = params.get("CurrentNum")
        self.InstanceIds = params.get("InstanceIds")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnhancedService(AbstractModel):
    """Describes the configuration of enhanced services, such as Cloud Security and Cloud Monitor.

    """

    def __init__(self):
        r"""
        :param SecurityService: Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.cvm.v20170312.models.RunSecurityServiceEnabled`
        :param MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.cvm.v20170312.models.RunMonitorServiceEnabled`
        :param AutomationService: Enables the TAT service. If this parameter is not specified, the TAT service will not be enabled.
        :type AutomationService: :class:`tencentcloud.cvm.v20170312.models.RunAutomationServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None
        self.AutomationService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self.AutomationService = RunAutomationServiceEnabled()
            self.AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportImagesRequest(AbstractModel):
    """ExportImages request structure.

    """

    def __init__(self):
        r"""
        :param BucketName: COS bucket name
        :type BucketName: str
        :param ImageIds: List of image IDs
        :type ImageIds: list of str
        :param ExportFormat: Format of the exported image file. Valid values: `RAW`, `QCOW2`, `VHD` and `VMDK`. Default value: `RAW`.
        :type ExportFormat: str
        :param FileNamePrefixList: Prefix list of the name of exported files
        :type FileNamePrefixList: list of str
        :param OnlyExportRootDisk: Whether to export only the system disk
        :type OnlyExportRootDisk: bool
        :param DryRun: Check whether the image can be exported
        :type DryRun: bool
        :param RoleName: Role name (Default: `CVM_QcsRole`). Before exporting the images, make sure the role exists, and it has write permission to COS.
        :type RoleName: str
        """
        self.BucketName = None
        self.ImageIds = None
        self.ExportFormat = None
        self.FileNamePrefixList = None
        self.OnlyExportRootDisk = None
        self.DryRun = None
        self.RoleName = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ImageIds = params.get("ImageIds")
        self.ExportFormat = params.get("ExportFormat")
        self.FileNamePrefixList = params.get("FileNamePrefixList")
        self.OnlyExportRootDisk = params.get("OnlyExportRootDisk")
        self.DryRun = params.get("DryRun")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportImagesResponse(AbstractModel):
    """ExportImages response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the image export task
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Externals(AbstractModel):
    """Additional data

    """

    def __init__(self):
        r"""
        :param ReleaseAddress: Release address
Note: This field may return null, indicating that no valid value is found.
        :type ReleaseAddress: bool
        :param UnsupportNetworks: Not supported network. Value: <br><li>BASIC: classic network<br><li>VPC1.0: VPC1.0
Note: This field may return null, indicating that no valid value was found.
        :type UnsupportNetworks: list of str
        :param StorageBlockAttr: Attributes of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :type StorageBlockAttr: :class:`tencentcloud.cvm.v20170312.models.StorageBlock`
        """
        self.ReleaseAddress = None
        self.UnsupportNetworks = None
        self.StorageBlockAttr = None


    def _deserialize(self, params):
        self.ReleaseAddress = params.get("ReleaseAddress")
        self.UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self.StorageBlockAttr = StorageBlock()
            self.StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param Name: Filters.
        :type Name: str
        :param Values: Filter values.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GPUInfo(AbstractModel):
    """GPU information of the instance

    """

    def __init__(self):
        r"""
        :param GPUCount: Number of GPUs. 
Note: this field may return `null`, indicating that no valid value can be found.
        :type GPUCount: float
        :param GPUId: GPU address
Note: this field may return `null`, indicating that no valid value can be found.
        :type GPUId: list of str
        :param GPUType: GPU type of the instance.
Note: this field may return `null`, indicating that no valid value can be found.
        :type GPUType: str
        """
        self.GPUCount = None
        self.GPUId = None
        self.GPUType = None


    def _deserialize(self, params):
        self.GPUCount = params.get("GPUCount")
        self.GPUId = params.get("GPUId")
        self.GPUType = params.get("GPUType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostItem(AbstractModel):
    """CDH instance details

    """

    def __init__(self):
        r"""
        :param Placement: CDH instance location. This parameter is used to specify the AZ, project, and other attributes of the instance.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param HostId: CDH instance ID
        :type HostId: str
        :param HostType: CDH instance type
        :type HostType: str
        :param HostName: CDH instance name
        :type HostName: str
        :param HostChargeType: CDH instance billing mode
        :type HostChargeType: str
        :param RenewFlag: CDH instance renewal flag
        :type RenewFlag: str
        :param CreatedTime: CDH instance creation time
        :type CreatedTime: str
        :param ExpiredTime: CDH instance expiry time
        :type ExpiredTime: str
        :param InstanceIds: List of IDs of CVMs created on a CDH instance
        :type InstanceIds: list of str
        :param HostState: CDH instance status
        :type HostState: str
        :param HostIp: CDH instance IP
        :type HostIp: str
        :param HostResource: CDH instance resource information
        :type HostResource: :class:`tencentcloud.cvm.v20170312.models.HostResource`
        :param CageId: Cage ID of the CDH instance. This parameter is only valid for CDH instances in the cages of finance availability zones.
Note: This field may return null, indicating that no valid value is found.
        :type CageId: str
        """
        self.Placement = None
        self.HostId = None
        self.HostType = None
        self.HostName = None
        self.HostChargeType = None
        self.RenewFlag = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.InstanceIds = None
        self.HostState = None
        self.HostIp = None
        self.HostResource = None
        self.CageId = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.HostId = params.get("HostId")
        self.HostType = params.get("HostType")
        self.HostName = params.get("HostName")
        self.HostChargeType = params.get("HostChargeType")
        self.RenewFlag = params.get("RenewFlag")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.InstanceIds = params.get("InstanceIds")
        self.HostState = params.get("HostState")
        self.HostIp = params.get("HostIp")
        if params.get("HostResource") is not None:
            self.HostResource = HostResource()
            self.HostResource._deserialize(params.get("HostResource"))
        self.CageId = params.get("CageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostResource(AbstractModel):
    """Resource information of the CDH instance

    """

    def __init__(self):
        r"""
        :param CpuTotal: Total number of CPU cores in the CDH instance
        :type CpuTotal: int
        :param CpuAvailable: Number of available CPU cores in the CDH instance
        :type CpuAvailable: int
        :param MemTotal: Total memory size of the CDH instance (unit: GiB)
        :type MemTotal: float
        :param MemAvailable: Available memory size of the CDH instance (unit: GiB)
        :type MemAvailable: float
        :param DiskTotal: Total disk size of the CDH instance (unit: GiB)
        :type DiskTotal: int
        :param DiskAvailable: Available disk size of the CDH instance (unit: GiB)
        :type DiskAvailable: int
        :param DiskType: Disk type of the CDH instance
        :type DiskType: str
        :param GpuTotal: Total number of GPU cards in the CDH instance
        :type GpuTotal: int
        :param GpuAvailable: Number of available GPU cards in the CDH instance
        :type GpuAvailable: int
        """
        self.CpuTotal = None
        self.CpuAvailable = None
        self.MemTotal = None
        self.MemAvailable = None
        self.DiskTotal = None
        self.DiskAvailable = None
        self.DiskType = None
        self.GpuTotal = None
        self.GpuAvailable = None


    def _deserialize(self, params):
        self.CpuTotal = params.get("CpuTotal")
        self.CpuAvailable = params.get("CpuAvailable")
        self.MemTotal = params.get("MemTotal")
        self.MemAvailable = params.get("MemAvailable")
        self.DiskTotal = params.get("DiskTotal")
        self.DiskAvailable = params.get("DiskAvailable")
        self.DiskType = params.get("DiskType")
        self.GpuTotal = params.get("GpuTotal")
        self.GpuAvailable = params.get("GpuAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """Details about an image, including its state and attributes.

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID
        :type ImageId: str
        :param OsName: Operating system of the image
        :type OsName: str
        :param ImageType: Image type
        :type ImageType: str
        :param CreatedTime: Creation time of the image
        :type CreatedTime: str
        :param ImageName: Image name
        :type ImageName: str
        :param ImageDescription: Image description
        :type ImageDescription: str
        :param ImageSize: Image size
        :type ImageSize: int
        :param Architecture: Image architecture
        :type Architecture: str
        :param ImageState: Image state
        :type ImageState: str
        :param Platform: Source platform of the image
        :type Platform: str
        :param ImageCreator: Image creator
        :type ImageCreator: str
        :param ImageSource: Image source
        :type ImageSource: str
        :param SyncPercent: Synchronization percentage
Note: This field may return null, indicating that no valid value is found.
        :type SyncPercent: int
        :param IsSupportCloudinit: Whether the image supports cloud-init
Note: This field may return null, indicating that no valid value is found.
        :type IsSupportCloudinit: bool
        :param SnapshotSet: Information on the snapshots associated with the image
Note: This field may return null, indicating that no valid value is found.
        :type SnapshotSet: list of Snapshot
        :param Tags: The list of tags bound to the image.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param LicenseType: Image license type
        :type LicenseType: str
        """
        self.ImageId = None
        self.OsName = None
        self.ImageType = None
        self.CreatedTime = None
        self.ImageName = None
        self.ImageDescription = None
        self.ImageSize = None
        self.Architecture = None
        self.ImageState = None
        self.Platform = None
        self.ImageCreator = None
        self.ImageSource = None
        self.SyncPercent = None
        self.IsSupportCloudinit = None
        self.SnapshotSet = None
        self.Tags = None
        self.LicenseType = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.OsName = params.get("OsName")
        self.ImageType = params.get("ImageType")
        self.CreatedTime = params.get("CreatedTime")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        self.ImageSize = params.get("ImageSize")
        self.Architecture = params.get("Architecture")
        self.ImageState = params.get("ImageState")
        self.Platform = params.get("Platform")
        self.ImageCreator = params.get("ImageCreator")
        self.ImageSource = params.get("ImageSource")
        self.SyncPercent = params.get("SyncPercent")
        self.IsSupportCloudinit = params.get("IsSupportCloudinit")
        if params.get("SnapshotSet") is not None:
            self.SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self.SnapshotSet.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """Supported operating systems are divided into two categories, Windows and Linux.

    """

    def __init__(self):
        r"""
        :param Windows: Supported Windows OS
Note: This field may return null, indicating that no valid value is found.
        :type Windows: list of str
        :param Linux: Supported Linux OS
Note: This field may return null, indicating that no valid value is found.
        :type Linux: list of str
        """
        self.Windows = None
        self.Linux = None


    def _deserialize(self, params):
        self.Windows = params.get("Windows")
        self.Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageRequest(AbstractModel):
    """ImportImage request structure.

    """

    def __init__(self):
        r"""
        :param Architecture: OS architecture of the image to be imported, `x86_64` or `i386`.
        :type Architecture: str
        :param OsType: OS type of the image to be imported. You can call `DescribeImportImageOs` to obtain the list of supported operating systems.
        :type OsType: str
        :param OsVersion: OS version of the image to be imported. You can call `DescribeImportImageOs` to obtain the list of supported operating systems.
        :type OsVersion: str
        :param ImageUrl: Address on COS where the image to be imported is stored.
        :type ImageUrl: str
        :param ImageName: Image name
        :type ImageName: str
        :param ImageDescription: Image description
        :type ImageDescription: str
        :param DryRun: Dry run to check the parameters without performing the operation
        :type DryRun: bool
        :param Force: Whether to force import the image. For more information, see [Forcibly Import Image](https://intl.cloud.tencent.com/document/product/213/12849).
        :type Force: bool
        :param TagSpecification: Tag description list. This parameter is used to bind a tag to a custom image.
        :type TagSpecification: list of TagSpecification
        :param LicenseType: The license type used to activate the OS after importing an image.
Valid values:
`TencentCloud`: Tencent Cloud official license
`BYOL`: Bring Your Own License
        :type LicenseType: str
        """
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.ImageUrl = None
        self.ImageName = None
        self.ImageDescription = None
        self.DryRun = None
        self.Force = None
        self.TagSpecification = None
        self.LicenseType = None


    def _deserialize(self, params):
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        self.DryRun = params.get("DryRun")
        self.Force = params.get("Force")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.LicenseType = params.get("LicenseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair request structure.

    """

    def __init__(self):
        r"""
        :param KeyName: Key pair name, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param ProjectId: The project ID to which the key pair belongs after it is created. <br><br>You can obtain the project ID in the following ways: <br><li>Check the project list in the [Project management](https://console.cloud.tencent.com/project) page.<br><li>Call the `DescribeProject` API and view the `projectId` in the response.

If you want to use the default project, specify 0 for the parameter.
        :type ProjectId: int
        :param PublicKey: Content of the public key in the key pair in the `OpenSSH RSA` format.
        :type PublicKey: str
        :param TagSpecification: Tag description list. This parameter is used to bind a tag to a key pair.
        :type TagSpecification: list of TagSpecification
        """
        self.KeyName = None
        self.ProjectId = None
        self.PublicKey = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.PublicKey = params.get("PublicKey")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyPairResponse(AbstractModel):
    """ImportKeyPair response structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Key pair ID
        :type KeyId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class InquirePricePurchaseReservedInstancesOfferingRequest(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering request structure.

    """

    def __init__(self):
        r"""
        :param InstanceCount: The number of the reserved instances you are purchasing.
        :type InstanceCount: int
        :param ReservedInstancesOfferingId: The ID of the reserved instance offering.
        :type ReservedInstancesOfferingId: str
        :param DryRun: Dry run.
        :type DryRun: bool
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.<br>For more information, see Ensuring Idempotency.
        :type ClientToken: str
        :param ReservedInstanceName: Reserved instance name.<br><li>The RI name defaults to “unnamed” if this parameter is left empty.</li><li>You can enter any name within 60 characters (including the pattern string).</li>
        :type ReservedInstanceName: str
        """
        self.InstanceCount = None
        self.ReservedInstancesOfferingId = None
        self.DryRun = None
        self.ClientToken = None
        self.ReservedInstanceName = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.DryRun = params.get("DryRun")
        self.ClientToken = params.get("ClientToken")
        self.ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePricePurchaseReservedInstancesOfferingResponse(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price of the reserved instance with specified configuration.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ReservedInstancePrice`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = ReservedInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstanceRequest(AbstractModel):
    """InquiryPriceResetInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information; for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :type ImageId: str
        :param SystemDisk: Configuration of the system disk of the instance. For instances with a cloud disk as the system disk, you can expand the system disk by using this parameter to specify the new capacity after reinstallation. If the parameter is not specified, the system disk capacity remains unchanged by default. You can only expand the capacity of the system disk; reducing its capacity is not supported. When reinstalling the system, you can only modify the capacity of the system disk, not the type.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        """
        self.InstanceId = None
        self.ImageId = None
        self.SystemDisk = None
        self.LoginSettings = None
        self.EnhancedService = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstanceResponse(AbstractModel):
    """InquiryPriceResetInstance response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price of reinstalling the instance with the specified configuration.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100. When changing the bandwidth of instances with `BANDWIDTH_PREPAID` or `BANDWIDTH_POSTPAID_BY_HOUR` as the network billing method, you can only specify one instance at a time.
        :type InstanceIds: list of str
        :param InternetAccessible: Configuration of public network egress bandwidth. The maximum bandwidth varies among different models. For more information, see the documentation on bandwidth limits. Currently only the `InternetMaxBandwidthOut` parameter is supported.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param StartTime: Date from which the new bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The starting date cannot be earlier than the current date. If the starting date is the current date, the new bandwidth takes effect immediately. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type StartTime: str
        :param EndTime: Date until which the new bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the new bandwidth covers the end date. The end date cannot be later than the expiration date of a prepaid instance. You can query the expiration time of an instance by calling [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728) and looking for `ExpiredTime` in the response. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type EndTime: str
        """
        self.InstanceIds = None
        self.InternetAccessible = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price of the new bandwidth
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstancesTypeRequest(AbstractModel):
    """InquiryPriceResetInstancesType request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). You can obtain the instance IDs from the value of `InstanceId` returned by the [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API. The maximum number of instances in each request is 1.
        :type InstanceIds: list of str
        :param InstanceType: Instance model. Resources vary with the instance model. Specific values can be found in the tables of [Instance Types] (https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1) or in the latest specifications via the [DescribeInstanceTypeConfigs] (https://intl.cloud.tencent.com/document/product/213/15749?from_cn_redirect=1) API.
        :type InstanceType: str
        """
        self.InstanceIds = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetInstancesTypeResponse(AbstractModel):
    """InquiryPriceResetInstancesType response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price of the instance using the specified model
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResizeInstanceDisksRequest(AbstractModel):
    """InquiryPriceResizeInstanceDisks request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param DataDisks: The configuration of data disks to be expanded. Currently, you can only use the API to expand non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#DataDisk) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is non-elastic. Data disk capacity unit: GB; minimum increment: 10 GB. For more information about selecting a data disk type, see the product overview on cloud disks. Available data disk types are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies by data disk type.
        :type DataDisks: list of DataDisk
        :param ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally.
        :type ForceStop: bool
        """
        self.InstanceId = None
        self.DataDisks = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResizeInstanceDisksResponse(AbstractModel):
    """InquiryPriceResizeInstanceDisks response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price of the disks after being expanded to the specified configurations
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRunInstancesRequest(AbstractModel):
    """InquiryPriceRunInstances request structure.

    """

    def __init__(self):
        r"""
        :param Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project.
 <b>Note: `Placement` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `Placement` prevails.</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images: <br/><li>Public images</li><li>Custom images</li><li>Shared images</li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information. </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
 <b>Note: `ImageId` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `ImageId` prevails.</b>
        :type ImageId: str
        :param InstanceChargeType: The instance [billing method](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1).<br><li>POSTPAID_BY_HOUR: Pay-as-you-go on an hourly basis<br>Default value: POSTPAID_BY_HOUR.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`. 
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param InstanceType: The instance model. Different resource specifications are specified for different models. For specific values, call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) to retrieve the latest specification list or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If the parameter is not specified, `S1.SMALL1` will be used by default.
        :type InstanceType: str
        :param SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: Data disk configuration of the instance. If the parameter is not specified, no data disk will be purchased by default. If you want to purchase data disks, you can specify 21 data disks, including up to 1 `LOCAL_BASIC` data disk or `LOCAL_SSD` data disk and up to 20 `CLOUD_BASIC` data disks, `CLOUD_PREMIUM` data disks, or `CLOUD_SSD` data disks.
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: VPC configurations (VPC ID, subnet ID, etc). If it’s not specified, the classic network will be used by default. If a VPC IP is specified in this parameter, the `InstanceCount` can only be 1.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: Configuration of public network bandwidth. If it’s not specified, 0 Mbps is used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: Number of instances to purchase. Value range: 1 (default) to 100. It cannot exceed the remaining CVM quota of the user. For more information on quota, see [Restrictions on CVM Instance Purchase](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param InstanceName: Instance name (up to 60 characters)<br><li>If this parameter is not specified, **Unnamed** will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`. </li>
        :type InstanceName: str
        :param LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance, or keep the original login settings of the image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will not be associated with any security group by default.
        :type SecurityGroupIds: list of str
        :param EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.<br>For more information, see Ensuring Idempotency.
        :type ClientToken: str
        :param HostName: Host name of the CVM. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>Windows: 2-15 characters, containing [a-z], [A-Z], [0-9] and hyphens (-). Digit-only strings are not allowed.<br><li>For other instances, such as Linux instances, the host name must be 2-30 characters long. It supports multiple periods (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two periods (.).
        :type HostName: str
        :param TagSpecification: The tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances.
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: The market options of the instance.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param HpcClusterId: HPC cluster ID.
        :type HpcClusterId: str
        """
        self.Placement = None
        self.ImageId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.HpcClusterId = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ImageId = params.get("ImageId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.HpcClusterId = params.get("HpcClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRunInstancesResponse(AbstractModel):
    """InquiryPriceRunInstances response structure.

    """

    def __init__(self):
        r"""
        :param Price: Price of the instance with the specified configurations.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.Price`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Describes information on an instance

    """

    def __init__(self):
        r"""
        :param Placement: Location of the instance
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param InstanceId: Instance `ID`
        :type InstanceId: str
        :param InstanceType: Instance model
        :type InstanceType: str
        :param CPU: Number of CPU cores of the instance; unit: core
        :type CPU: int
        :param Memory: Memory capacity; unit: `GB`.
        :type Memory: int
        :param RestrictState: Instance status. Valid values: <br><li>NORMAL: instance is normal. <br><li>EXPIRED: instance expired. <br><li>PROTECTIVELY_ISOLATED: instance is protectively isolated.
        :type RestrictState: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param InstanceChargeType: Instance billing plan. Valid values:<br><li>`POSTPAID_BY_HOUR`: pay after use. You are billed by the hour, by traffic.<br><li>`CDHPAID`: `CDH` billing plan. Applicable to `CDH` only, not the instances on the host.<br>
        :type InstanceChargeType: str
        :param SystemDisk: Information on the system disk of the instance
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: Information of the instance data disks.
        :type DataDisks: list of DataDisk
        :param PrivateIpAddresses: List of private IPs of the instance's primary ENI.
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: List of public IPs of the instance's primary ENI.
Note: This field may return null, indicating that no valid value is found.
        :type PublicIpAddresses: list of str
        :param InternetAccessible: Information on instance bandwidth.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param VirtualPrivateCloud: Information on the VPC where the instance resides.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ImageId: `ID` of the image used to create the instance.
        :type ImageId: str
        :param RenewFlag: Auto renewal flag. Valid values: <br><li>`NOTIFY_AND_MANUAL_RENEW`: notify upon expiration, but do not renew automatically <br><li>`NOTIFY_AND_AUTO_RENEW`: notify upon expiration and renew automatically <br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`: do not notify upon expiration and do not renew automatically.
<br><li>Note: this parameter is `null` for postpaid instances.
        :type RenewFlag: str
        :param CreatedTime: Creation time following the `ISO8601` standard and using `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.
        :type CreatedTime: str
        :param ExpiredTime: Expiration time in UTC format following the `ISO8601` standard: `YYYY-MM-DDThh:mm:ssZ`. Note: this parameter is `null` for postpaid instances.
        :type ExpiredTime: str
        :param OsName: Operating system name.
        :type OsName: str
        :param SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response.
        :type SecurityGroupIds: list of str
        :param LoginSettings: Login settings of the instance. Currently only the key associated with the instance is returned.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param InstanceState: Instance state. Valid values: <br><li>PENDING: creating <br></li><li>LAUNCH_FAILED: creation failed <br></li><li>RUNNING: running <br></li><li>STOPPED: shut down <br></li><li>STARTING: starting <br></li><li>STOPPING: shutting down <br></li><li>REBOOTING: rebooting <br></li><li>SHUTDOWN: shut down and to be terminated <br></li><li>TERMINATING: terminating. <br></li>
        :type InstanceState: str
        :param Tags: List of tags associated with the instance.
        :type Tags: list of Tag
        :param StopChargingMode: Instance billing method after shutdown.
Valid values: <br><li>KEEP_CHARGING: billing continues after shutdown <br><li>STOP_CHARGING: billing stops after shutdown <li>NOT_APPLICABLE: the instance is not shut down or stopping billing after shutdown is not applicable to the instance. <br>
        :type StopChargingMode: str
        :param Uuid: Globally unique ID of the instance.
        :type Uuid: str
        :param LatestOperation: Last operation of the instance, such as StopInstances or ResetInstance.
        :type LatestOperation: str
        :param LatestOperationState: The latest operation status of the instance. Valid values:<br><li>SUCCESS: operation succeeded<br><li>OPERATING: operation in progress<br><li>FAILED: operation failed
        :type LatestOperationState: str
        :param LatestOperationRequestId: Unique request ID for the last operation of the instance.
        :type LatestOperationRequestId: str
        :param DisasterRecoverGroupId: ID of a spread placement group.
Note: this field may return null, indicating that no valid value is obtained.
        :type DisasterRecoverGroupId: str
        :param IPv6Addresses: IPv6 address of the instance.
Note: this field may return null, indicating that no valid value is obtained.
        :type IPv6Addresses: list of str
        :param CamRoleName: CAM role name.
Note: this field may return null, indicating that no valid value is obtained.
        :type CamRoleName: str
        :param HpcClusterId: HPC cluster ID.
Note: this field may return null, indicating that no valid value was found.
        :type HpcClusterId: str
        :param RdmaIpAddresses: IP list of HPC cluster.
Note: this field may return null, indicating that no valid value was found.
        :type RdmaIpAddresses: list of str
        :param IsolatedSource: The isolation status of the instance. Valid values:<br><li>`ARREAR`: isolated due to overdue payment;<br></li><li>`EXPIRE`: isolated upon expiration;<br></li><li>`MANMADE`: isolated after manual returning;<br></li><li>`NOTISOLATED`: not isolated<br></li>
Note: this field may return null, indicating that no valid value was found.
        :type IsolatedSource: str
        :param GPUInfo: GPU information. This field is only returned for GPU instances.
Note: this field may return null, indicating that no valid value was found.
        :type GPUInfo: :class:`tencentcloud.cvm.v20170312.models.GPUInfo`
        :param LicenseType: Instance OS license type. Default value: `TencentCloud`
        :type LicenseType: str
        :param DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: Enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: Do not enable the instance protection.<br><br>Default value: `FALSE`.
        :type DisableApiTermination: bool
        """
        self.Placement = None
        self.InstanceId = None
        self.InstanceType = None
        self.CPU = None
        self.Memory = None
        self.RestrictState = None
        self.InstanceName = None
        self.InstanceChargeType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.InternetAccessible = None
        self.VirtualPrivateCloud = None
        self.ImageId = None
        self.RenewFlag = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.OsName = None
        self.SecurityGroupIds = None
        self.LoginSettings = None
        self.InstanceState = None
        self.Tags = None
        self.StopChargingMode = None
        self.Uuid = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.LatestOperationRequestId = None
        self.DisasterRecoverGroupId = None
        self.IPv6Addresses = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.RdmaIpAddresses = None
        self.IsolatedSource = None
        self.GPUInfo = None
        self.LicenseType = None
        self.DisableApiTermination = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceId = params.get("InstanceId")
        self.InstanceType = params.get("InstanceType")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.RestrictState = params.get("RestrictState")
        self.InstanceName = params.get("InstanceName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ImageId = params.get("ImageId")
        self.RenewFlag = params.get("RenewFlag")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.OsName = params.get("OsName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.InstanceState = params.get("InstanceState")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.StopChargingMode = params.get("StopChargingMode")
        self.Uuid = params.get("Uuid")
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.LatestOperationRequestId = params.get("LatestOperationRequestId")
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.IPv6Addresses = params.get("IPv6Addresses")
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        self.RdmaIpAddresses = params.get("RdmaIpAddresses")
        self.IsolatedSource = params.get("IsolatedSource")
        if params.get("GPUInfo") is not None:
            self.GPUInfo = GPUInfo()
            self.GPUInfo._deserialize(params.get("GPUInfo"))
        self.LicenseType = params.get("LicenseType")
        self.DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """Describes the billing method of an instance.

    """

    def __init__(self):
        r"""
        :param Period: Subscription period; unit: month; valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36.
        :type Period: int
        :param RenewFlag: Auto renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>Default value: NOTIFY_AND_MANUAL_RENEW. If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyConfig(AbstractModel):
    """Describes the model family of the instance.
    Examples: {'InstanceFamilyName': 'Standard S1', 'InstanceFamily': 'S1'}, {'InstanceFamilyName': 'Network-optimized N1', 'InstanceFamily': 'N1'}, {'InstanceFamilyName': 'High IO I1', 'InstanceFamily': 'I1'}, etc.

    """

    def __init__(self):
        r"""
        :param InstanceFamilyName: Full name of the model family.
        :type InstanceFamilyName: str
        :param InstanceFamily: Acronym of the model family.
        :type InstanceFamily: str
        """
        self.InstanceFamilyName = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.InstanceFamilyName = params.get("InstanceFamilyName")
        self.InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceMarketOptionsRequest(AbstractModel):
    """Options related to bidding requests

    """

    def __init__(self):
        r"""
        :param SpotOptions: Options related to bidding
        :type SpotOptions: :class:`tencentcloud.cvm.v20170312.models.SpotMarketOptions`
        :param MarketType: Market option type. Currently `spot` is the only supported value.
        :type MarketType: str
        """
        self.SpotOptions = None
        self.MarketType = None


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))
        self.MarketType = params.get("MarketType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatus(AbstractModel):
    """Describes instance states. For state types, see [here](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#InstanceStatus).

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance `ID`.
        :type InstanceId: str
        :param InstanceState: The instance state. Valid values: <br><li>PENDING: creating<br></li><li>LAUNCH_FAILED: creation failed<br></li><li>RUNNING: running<br></li><li>STOPPED: shut down<br></li><li>STARTING: starting<br></li><li>STOPPING: shutting down<br></li><li>REBOOTING: rebooting<br></li><li>SHUTDOWN: shut down and to be terminated<br></li><li>TERMINATING: terminating.<br></li>
        :type InstanceState: str
        """
        self.InstanceId = None
        self.InstanceState = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceState = params.get("InstanceState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeQuotaItem(AbstractModel):
    """Describes instance model quota.

    """

    def __init__(self):
        r"""
        :param Zone: Availability zone.
        :type Zone: str
        :param InstanceType: Instance model.
        :type InstanceType: str
        :param InstanceChargeType: Instance billing plan. Valid values: <br><li>POSTPAID_BY_HOUR: pay after use. You are billed for your traffic by the hour.<br><li>`CDHPAID`: [`CDH`](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) billing plan. Applicable to `CDH` only, not the instances on the host.
        :type InstanceChargeType: str
        :param NetworkCard: ENI type. For example, 25 represents an ENI of 25 GB.
        :type NetworkCard: int
        :param Externals: Additional data.
Note: This field may return null, indicating that no valid value is found.
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param Cpu: Number of CPU cores of an instance model.
        :type Cpu: int
        :param Memory: Instance memory capacity; unit: `GB`.
        :type Memory: int
        :param InstanceFamily: Instance model family.
        :type InstanceFamily: str
        :param TypeName: Model name.
        :type TypeName: str
        :param LocalDiskTypeList: List of local disk specifications. If the parameter returns null, it means that local disks cannot be created.
        :type LocalDiskTypeList: list of LocalDiskType
        :param Status: Whether an instance model is available. Valid values: <br><li>SELL: available <br><li>SOLD_OUT: sold out
        :type Status: str
        :param Price: Price of an instance model.
        :type Price: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param SoldOutReason: Details of out-of-stock items
Note: this field may return null, indicating that no valid value is obtained.
        :type SoldOutReason: str
        :param InstanceBandwidth: Private network bandwidth, in Gbps.
        :type InstanceBandwidth: float
        :param InstancePps: The max packet sending and receiving capability (in 10k PPS).
        :type InstancePps: int
        :param StorageBlockAmount: Number of local storage blocks.
        :type StorageBlockAmount: int
        :param CpuType: CPU type.
        :type CpuType: str
        :param Gpu: Number of GPUs of the instance.
        :type Gpu: int
        :param Fpga: Number of FPGAs of the instance.
        :type Fpga: int
        :param Remark: Descriptive information of the instance.
        :type Remark: str
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceChargeType = None
        self.NetworkCard = None
        self.Externals = None
        self.Cpu = None
        self.Memory = None
        self.InstanceFamily = None
        self.TypeName = None
        self.LocalDiskTypeList = None
        self.Status = None
        self.Price = None
        self.SoldOutReason = None
        self.InstanceBandwidth = None
        self.InstancePps = None
        self.StorageBlockAmount = None
        self.CpuType = None
        self.Gpu = None
        self.Fpga = None
        self.Remark = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.InstanceFamily = params.get("InstanceFamily")
        self.TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self.LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self.LocalDiskTypeList.append(obj)
        self.Status = params.get("Status")
        if params.get("Price") is not None:
            self.Price = ItemPrice()
            self.Price._deserialize(params.get("Price"))
        self.SoldOutReason = params.get("SoldOutReason")
        self.InstanceBandwidth = params.get("InstanceBandwidth")
        self.InstancePps = params.get("InstancePps")
        self.StorageBlockAmount = params.get("StorageBlockAmount")
        self.CpuType = params.get("CpuType")
        self.Gpu = params.get("Gpu")
        self.Fpga = params.get("Fpga")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """Describes the accessibility of an instance in the public network, including its network billing method, maximum bandwidth, etc.

    """

    def __init__(self):
        r"""
        :param InternetChargeType: Network connection billing plan. Valid value: <br><li>TRAFFIC_POSTPAID_BY_HOUR: pay after use. You are billed for your traffic, by the hour.
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the public network, in Mbps. The default value is 0 Mbps. The upper limit of bandwidth varies for different models. For more information, see [Purchase Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/12523?from_cn_redirect=1).
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: Whether to assign a public IP. Valid values: <br><li>TRUE: Assign a public IP <br><li>FALSE: Do not assign a public IP <br><br>If the public network bandwidth is greater than 0 Mbps, you can choose whether to assign a public IP; by default a public IP will be assigned. If the public network bandwidth is 0 Mbps, you will not be able to assign a public IP.
        :type PublicIpAssigned: bool
        :param BandwidthPackageId: Bandwidth package ID. To obatin the IDs, you can call [`DescribeBandwidthPackages`](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) and look for the `BandwidthPackageId` fields in the response.
        :type BandwidthPackageId: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetChargeTypeConfig(AbstractModel):
    """Describes network billing.

    """

    def __init__(self):
        r"""
        :param InternetChargeType: Network billing method.
        :type InternetChargeType: str
        :param Description: Description of the network billing method.
        :type Description: str
        """
        self.InternetChargeType = None
        self.Description = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """Describes pricing information.

    """

    def __init__(self):
        r"""
        :param UnitPrice: The original unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPrice: float
        :param ChargeUnit: Billing unit for pay-as-you-go mode. Valid values: <br><li>HOUR: billed on an hourly basis. It's used for hourly postpaid instances (`POSTPAID_BY_HOUR`). <br><li>GB: bill by traffic in GB. It's used for postpaid products that are billed by the hourly traffic (`TRAFFIC_POSTPAID_BY_HOUR`).
Note: this field may return null, indicating that no valid value is obtained.
        :type ChargeUnit: str
        :param OriginalPrice: The original price of a pay-in-advance instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.
        :type OriginalPrice: float
        :param DiscountPrice: Discount price of a prepaid instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.
        :type DiscountPrice: float
        :param Discount: Percentage of the original price. For example, if you enter "20.0", the discounted price will be 20% of the original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Discount: float
        :param UnitPriceDiscount: The discounted unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceDiscount: float
        :param UnitPriceSecondStep: Original unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceSecondStep: float
        :param UnitPriceDiscountSecondStep: Discounted unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceDiscountSecondStep: float
        :param UnitPriceThirdStep: Original unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceThirdStep: float
        :param UnitPriceDiscountThirdStep: Discounted unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :type UnitPriceDiscountThirdStep: float
        :param OriginalPriceThreeYear: Original 3-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type OriginalPriceThreeYear: float
        :param DiscountPriceThreeYear: Discounted 3-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountPriceThreeYear: float
        :param DiscountThreeYear: Discount for 3-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountThreeYear: float
        :param OriginalPriceFiveYear: Original 5-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type OriginalPriceFiveYear: float
        :param DiscountPriceFiveYear: Discounted 5-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountPriceFiveYear: float
        :param DiscountFiveYear: Discount for 5-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountFiveYear: float
        :param OriginalPriceOneYear: Original 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type OriginalPriceOneYear: float
        :param DiscountPriceOneYear: Discounted 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountPriceOneYear: float
        :param DiscountOneYear: Discount for 1-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :type DiscountOneYear: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.Discount = None
        self.UnitPriceDiscount = None
        self.UnitPriceSecondStep = None
        self.UnitPriceDiscountSecondStep = None
        self.UnitPriceThirdStep = None
        self.UnitPriceDiscountThirdStep = None
        self.OriginalPriceThreeYear = None
        self.DiscountPriceThreeYear = None
        self.DiscountThreeYear = None
        self.OriginalPriceFiveYear = None
        self.DiscountPriceFiveYear = None
        self.DiscountFiveYear = None
        self.OriginalPriceOneYear = None
        self.DiscountPriceOneYear = None
        self.DiscountOneYear = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.Discount = params.get("Discount")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")
        self.UnitPriceSecondStep = params.get("UnitPriceSecondStep")
        self.UnitPriceDiscountSecondStep = params.get("UnitPriceDiscountSecondStep")
        self.UnitPriceThirdStep = params.get("UnitPriceThirdStep")
        self.UnitPriceDiscountThirdStep = params.get("UnitPriceDiscountThirdStep")
        self.OriginalPriceThreeYear = params.get("OriginalPriceThreeYear")
        self.DiscountPriceThreeYear = params.get("DiscountPriceThreeYear")
        self.DiscountThreeYear = params.get("DiscountThreeYear")
        self.OriginalPriceFiveYear = params.get("OriginalPriceFiveYear")
        self.DiscountPriceFiveYear = params.get("DiscountPriceFiveYear")
        self.DiscountFiveYear = params.get("DiscountFiveYear")
        self.OriginalPriceOneYear = params.get("OriginalPriceOneYear")
        self.DiscountPriceOneYear = params.get("DiscountPriceOneYear")
        self.DiscountOneYear = params.get("DiscountOneYear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """Describes key pair information.

    """

    def __init__(self):
        r"""
        :param KeyId: Key pair `ID`, the unique identifier of a key pair.
        :type KeyId: str
        :param KeyName: Key pair name.
        :type KeyName: str
        :param ProjectId: `ID` of the project to which a key pair belongs.
        :type ProjectId: int
        :param Description: Key pair description.
        :type Description: str
        :param PublicKey: Content of public key in a key pair.
        :type PublicKey: str
        :param PrivateKey: Content of private key in a key pair. Tencent Cloud do not keep private keys. Please keep it properly.
        :type PrivateKey: str
        :param AssociatedInstanceIds: `ID` list of instances associated with a key.
        :type AssociatedInstanceIds: list of str
        :param CreatedTime: Creation time, which follows the `ISO8601` standard and uses `UTC` time in the format of `YYYY-MM-DDThh:mm:ssZ`.
        :type CreatedTime: str
        :param Tags: The list of tags bound to the key.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tags: list of Tag
        """
        self.KeyId = None
        self.KeyName = None
        self.ProjectId = None
        self.Description = None
        self.PublicKey = None
        self.PrivateKey = None
        self.AssociatedInstanceIds = None
        self.CreatedTime = None
        self.Tags = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.Description = params.get("Description")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplate(AbstractModel):
    """Instance launch template. This parameter enables you to create an instance using the preset parameters in the template.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: Instance launch template ID. This parameter enables you to create an instance using the preset parameters in the template.
        :type LaunchTemplateId: str
        :param LaunchTemplateVersion: Instance launch template version number. If specified, this parameter will be used to create a new instance launch template.
        :type LaunchTemplateVersion: int
        """
        self.LaunchTemplateId = None
        self.LaunchTemplateVersion = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateInfo(AbstractModel):
    """Information of instance launch template.

    """

    def __init__(self):
        r"""
        :param LatestVersionNumber: Instance launch template version number.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LatestVersionNumber: int
        :param LaunchTemplateId: Instance launch template ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateId: str
        :param LaunchTemplateName: Instance launch template name.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateName: str
        :param DefaultVersionNumber: Default instance launch template version number.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DefaultVersionNumber: int
        :param LaunchTemplateVersionCount: Total number of versions that the instance launch template contains.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateVersionCount: int
        :param CreatedBy: UIN of the user who created the template.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreatedBy: str
        :param CreationTime: Creation time of the template.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreationTime: str
        """
        self.LatestVersionNumber = None
        self.LaunchTemplateId = None
        self.LaunchTemplateName = None
        self.DefaultVersionNumber = None
        self.LaunchTemplateVersionCount = None
        self.CreatedBy = None
        self.CreationTime = None


    def _deserialize(self, params):
        self.LatestVersionNumber = params.get("LatestVersionNumber")
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.LaunchTemplateName = params.get("LaunchTemplateName")
        self.DefaultVersionNumber = params.get("DefaultVersionNumber")
        self.LaunchTemplateVersionCount = params.get("LaunchTemplateVersionCount")
        self.CreatedBy = params.get("CreatedBy")
        self.CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionData(AbstractModel):
    """Information of instance launch template versions

    """

    def __init__(self):
        r"""
        :param Placement: Location of the instance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param InstanceType: Instance model.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param InstanceName: Instance name.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param InstanceChargeType: Instance billing mode. Valid values: <br><li>`POSTPAID_BY_HOUR`: postpaid for pay-as-you-go instances <br><li>`CDHPAID`: billed for CDH instances, not the CVMs running on the CDHs.<br>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceChargeType: str
        :param SystemDisk: Instance system disk information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: Instance data disk information. This parameter only covers the data disks purchased together with the instance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DataDisks: list of DataDisk
        :param InternetAccessible: Instance bandwidth information.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param VirtualPrivateCloud: Information of the VPC where the instance resides.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ImageId: `ID` of the image used to create the instance.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageId: str
        :param SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroupIds: list of str
        :param LoginSettings: Login settings of the instance. Currently, only the key associated with the instance is returned.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param CamRoleName: CAM role name.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CamRoleName: str
        :param HpcClusterId: HPC cluster `ID`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HpcClusterId: str
        :param InstanceCount: Number of instances purchased.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceCount: int
        :param EnhancedService: Enhanced service.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param UserData: User data provided to the instance. This parameter needs to be encoded in base64 format with the maximum size of 16KB.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UserData: str
        :param DisasterRecoverGroupIds: Placement group ID. You can only specify one.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DisasterRecoverGroupIds: list of str
        :param ActionTimer: Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param InstanceMarketOptions: Market options of the instance, such as parameters related to spot instances. This parameter is required for spot instances.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param HostName: Hostname of a CVM.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HostName: str
        :param ClientToken: A string used to ensure the idempotency of the request.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClientToken: str
        :param InstanceChargePrepaid: Prepaid mode. This parameter indicates relevant parameter settings for monthly-subscribed instances.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param TagSpecification: List of tag description. By specifying this parameter, the tag can be bound to the corresponding CVM and CBS instances at the same time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TagSpecification: list of TagSpecification
        """
        self.Placement = None
        self.InstanceType = None
        self.InstanceName = None
        self.InstanceChargeType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.VirtualPrivateCloud = None
        self.ImageId = None
        self.SecurityGroupIds = None
        self.LoginSettings = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.InstanceCount = None
        self.EnhancedService = None
        self.UserData = None
        self.DisasterRecoverGroupIds = None
        self.ActionTimer = None
        self.InstanceMarketOptions = None
        self.HostName = None
        self.ClientToken = None
        self.InstanceChargePrepaid = None
        self.TagSpecification = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceType = params.get("InstanceType")
        self.InstanceName = params.get("InstanceName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ImageId = params.get("ImageId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        self.InstanceCount = params.get("InstanceCount")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.UserData = params.get("UserData")
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.HostName = params.get("HostName")
        self.ClientToken = params.get("ClientToken")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LaunchTemplateVersionInfo(AbstractModel):
    """Set of instance launch template versions.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateVersion: Instance launch template version number.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateVersion: int
        :param LaunchTemplateVersionData: Details of instance launch template versions.
        :type LaunchTemplateVersionData: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplateVersionData`
        :param CreationTime: Creation time of the instance launch template version.
        :type CreationTime: str
        :param LaunchTemplateId: Instance launch template ID.
        :type LaunchTemplateId: str
        :param IsDefaultVersion: Specifies whether it’s the default launch template version.
        :type IsDefaultVersion: bool
        :param LaunchTemplateVersionDescription: Information of instance launch template version description.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LaunchTemplateVersionDescription: str
        :param CreatedBy: Creator account
        :type CreatedBy: str
        """
        self.LaunchTemplateVersion = None
        self.LaunchTemplateVersionData = None
        self.CreationTime = None
        self.LaunchTemplateId = None
        self.IsDefaultVersion = None
        self.LaunchTemplateVersionDescription = None
        self.CreatedBy = None


    def _deserialize(self, params):
        self.LaunchTemplateVersion = params.get("LaunchTemplateVersion")
        if params.get("LaunchTemplateVersionData") is not None:
            self.LaunchTemplateVersionData = LaunchTemplateVersionData()
            self.LaunchTemplateVersionData._deserialize(params.get("LaunchTemplateVersionData"))
        self.CreationTime = params.get("CreationTime")
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        self.LaunchTemplateVersionDescription = params.get("LaunchTemplateVersionDescription")
        self.CreatedBy = params.get("CreatedBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDiskType(AbstractModel):
    """Describes local disk specifications.

    """

    def __init__(self):
        r"""
        :param Type: Type of a local disk.
        :type Type: str
        :param PartitionType: Attributes of a local disk.
        :type PartitionType: str
        :param MinSize: Minimum size of a local disk.
        :type MinSize: int
        :param MaxSize: Maximum size of a local disk.
        :type MaxSize: int
        :param Required: Whether a local disk is required during purchase. Valid values:<br><li>REQUIRED: required<br><li>OPTIONAL: optional
        :type Required: str
        """
        self.Type = None
        self.PartitionType = None
        self.MinSize = None
        self.MaxSize = None
        self.Required = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PartitionType = params.get("PartitionType")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        r"""
        :param Password: Login password of the instance. <br><li>For Linux instances, the password must include 8-30 characters, and contain at least two of the following character sets: [a-z], [A-Z], [0-9] and [()\`~!@#$%^&*-+=|{}[]:;',.?/]. <br><li>For Windows instances, the password must include 12-30 characters, and contain at least three of the following character sets: [a-z], [A-Z], [0-9] and [()\`~!@#$%^&*-+=|{}[]:;',.?/]. <br><br>If it's not specified, the user needs to set the login password using the **Reset password** option in the CVM console or calling the API `ResetInstancesPassword` to complete the creation of the CVM instance(s).
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Password: str
        :param KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call [`DescribeKeyPairs`](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) to obtain `KeyId`. You cannot specify a key and a password at the same time. Windows instances do not support keys.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KeyIds: list of str
        :param KeepImageLogin: Whether to keep the original settings of an image. You cannot specify this parameter and `Password` or `KeyIds.N` at the same time. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. Valid values: <br><li>TRUE: keep the login settings of the image <br><li>FALSE: do not keep the login settings of the image <br><br>Default value: FALSE.
Note: This field may return null, indicating that no valid value is found.
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeRequest(AbstractModel):
    """ModifyChcAttribute request structure.

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC host IDs
        :type ChcIds: list of str
        :param InstanceName: CHC host name
        :type InstanceName: str
        :param DeviceType: Server type
        :type DeviceType: str
        :param BmcUser: Valid characters: Letters, numbers, hyphens and underscores
        :type BmcUser: str
        :param Password: The password can contain 8 to 16 characters, including letters, numbers and special symbols (()`~!@#$%^&*-+=_|{}).
        :type Password: str
        :param BmcSecurityGroupIds: BMC network security group list
        :type BmcSecurityGroupIds: list of str
        """
        self.ChcIds = None
        self.InstanceName = None
        self.DeviceType = None
        self.BmcUser = None
        self.Password = None
        self.BmcSecurityGroupIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        self.InstanceName = params.get("InstanceName")
        self.DeviceType = params.get("DeviceType")
        self.BmcUser = params.get("BmcUser")
        self.Password = params.get("Password")
        self.BmcSecurityGroupIds = params.get("BmcSecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyChcAttributeResponse(AbstractModel):
    """ModifyChcAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDisasterRecoverGroupAttributeRequest(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute request structure.

    """

    def __init__(self):
        r"""
        :param DisasterRecoverGroupId: Spread placement group ID, which can be obtained by calling the [DescribeDisasterRecoverGroups](https://intl.cloud.tencent.com/document/api/213/17810?from_cn_redirect=1) API.
        :type DisasterRecoverGroupId: str
        :param Name: Name of a spread placement group. The name must be 1-60 characters long and can contain both Chinese characters and English letters.
        :type Name: str
        """
        self.DisasterRecoverGroupId = None
        self.Name = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDisasterRecoverGroupAttributeResponse(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHostsAttributeRequest(AbstractModel):
    """ModifyHostsAttribute request structure.

    """

    def __init__(self):
        r"""
        :param HostIds: CDH instance ID(s).
        :type HostIds: list of str
        :param HostName: CDH instance name to be displayed. You can specify any name you like, but its length cannot exceed 60 characters.
        :type HostName: str
        :param RenewFlag: Auto renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        :param ProjectId: Project ID. You can use the `AddProject` API to create projects, and obtain the `projectId` field in the response of the `DescribeProject` API. When using the [DescribeHosts](https://intl.cloud.tencent.com/document/api/213/16474?from_cn_redirect=1) API to query instances later, you can filter the results by the project ID.
        :type ProjectId: int
        """
        self.HostIds = None
        self.HostName = None
        self.RenewFlag = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.HostIds = params.get("HostIds")
        self.HostName = params.get("HostName")
        self.RenewFlag = params.get("RenewFlag")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHostsAttributeResponse(AbstractModel):
    """ModifyHostsAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute request structure.

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID such as `img-gvbnzy6f`. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image).
        :type ImageId: str
        :param ImageName: New image name, which must meet the following requirements: <br> <li>No more than 20 characters. <br> <li>Must be unique.
        :type ImageName: str
        :param ImageDescription: New image description, which must meet the following requirement: <br> <li> No more than 60 characters.
        :type ImageDescription: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSharePermissionRequest(AbstractModel):
    """ModifyImageSharePermission request structure.

    """

    def __init__(self):
        r"""
        :param ImageId: Image ID such as `img-gvbnzy6f`. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image). <br>You can only specify an image in the `NORMAL` state. For more information on image states, see [here](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#image_state).
        :type ImageId: str
        :param AccountIds: List of account IDs with which an image is shared. For the format of array-type parameters, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/568?from_cn_redirect=1). The account ID is different from the QQ number. You can find the account ID in [Account Information](https://console.cloud.tencent.com/developer). 
        :type AccountIds: list of str
        :param Permission: Operations. Valid values: `SHARE`, sharing an image; `CANCEL`, cancelling an image sharing. 
        :type Permission: str
        """
        self.ImageId = None
        self.AccountIds = None
        self.Permission = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.AccountIds = params.get("AccountIds")
        self.Permission = params.get("Permission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSharePermissionResponse(AbstractModel):
    """ModifyImageSharePermission response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param InstanceName: The instance name, which can not exceed 60 characters
<dx-alert infotype="explain" title="">Either `InstanceName` or `SecurityGroups` must be specified, but they can not be both specified.</dx-alert>
        :type InstanceName: str
        :param SecurityGroups: IDs of security groups associated with the specified instance. You can associate with a security group by adding its ID, or cancel the association with a security group by removing its ID. <dx-alert infotype="explain" title="">Either `InstanceName` or `SecurityGroups` must be specified, but they cannot be both set.</dx-alert>
        :type SecurityGroups: list of str
        :param CamRoleName: The role bound with the instance. If it is not specified, it indicates to unbind the current role of the CVM.
        :type CamRoleName: str
        :param HostName: Host name of the instance. <br><li>Hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name. <br><li>Windows: 2-15 characters, including [a-z], [A-Z], [0-9] and hyphens (-). Digit-only strings are not allowed. <br><li>Other OS: 2-60 characters, including [a-z], [A-Z], [0-9] and [.-]. Separate characters with dots. 
        :type HostName: str
        :param DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: do not enable the instance protection.<br><br>Default Value: `FALSE`.
        :type DisableApiTermination: bool
        :param CamRoleType: The role type, which is used in conjunction with `CamRoleName`. The value is obtained in `RoleType` field, returning by `CAM DescribeRoleList` and `GetRole` APIs. Valid value: `user`, `system` and `service_linked`.
For example, when `LinkedRoleIn` is contained in `CamRoleName` (such as `TKE_QCSLinkedRoleInPrometheusService`), the returned `RoleType` of `DescribeRoleList` and `GetRoleis` is `service_linked`, and the `CamRoleType` `service_linked`.
When the value obtained in `RoleType` is `user` (default) or `system`, `CamRoleType` can be left empty.
        :type CamRoleType: str
        """
        self.InstanceIds = None
        self.InstanceName = None
        self.SecurityGroups = None
        self.CamRoleName = None
        self.HostName = None
        self.DisableApiTermination = None
        self.CamRoleType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroups = params.get("SecurityGroups")
        self.CamRoleName = params.get("CamRoleName")
        self.HostName = params.get("HostName")
        self.DisableApiTermination = params.get("DisableApiTermination")
        self.CamRoleType = params.get("CamRoleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesProjectRequest(AbstractModel):
    """ModifyInstancesProject request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance IDs. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. You can operate up to 100 instances in each request.
        :type InstanceIds: list of str
        :param ProjectId: Project ID. You can use the API `AddProject` to create projects, and obtain the `projectId` field in the response of the `DescribeProject` API. When using the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API to query instances later, you can filter the results by the project ID.
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesProjectResponse(AbstractModel):
    """ModifyInstancesProject response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesVpcAttributeRequest(AbstractModel):
    """ModifyInstancesVpcAttribute request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceIds: list of str
        :param VirtualPrivateCloud: VPC configurations. You can use this parameter to specify the VPC ID, subnet ID, VPC IP, etc. If the specified VPC ID and subnet ID (the subnet must be in the same availability zone as the instance) are different from the VPC where the specified instance resides, the instance will be migrated to a subnet of the specified VPC. You can use `PrivateIpAddresses` to specify the VPC subnet IP. If you want to specify the subnet IP, you will need to specify a subnet IP for each of the specified instances, and each `InstanceIds` will match a `PrivateIpAddresses`. If `PrivateIpAddresses` is not specified, the VPC subnet IP will be assigned randomly.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ForceStop: Whether to force shut down a running instances. Default value: TRUE.
        :type ForceStop: bool
        :param ReserveHostName: Whether to keep the host name. Default value: FALSE.
        :type ReserveHostName: bool
        """
        self.InstanceIds = None
        self.VirtualPrivateCloud = None
        self.ForceStop = None
        self.ReserveHostName = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ForceStop = params.get("ForceStop")
        self.ReserveHostName = params.get("ReserveHostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesVpcAttributeResponse(AbstractModel):
    """ModifyInstancesVpcAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyKeyPairAttributeRequest(AbstractModel):
    """ModifyKeyPairAttribute request structure.

    """

    def __init__(self):
        r"""
        :param KeyId: Key pair ID in the format of `skey-xxxxxxxx`. <br><br>You can obtain the available key pair IDs in two ways: <br><li>Log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair IDs. <br><li>Call [DescribeKeyPairs](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) and look for `KeyId` in the response.
        :type KeyId: str
        :param KeyName: New key pair name, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param Description: New key pair description. You can specify any name you like, but its length cannot exceed 60 characters.
        :type Description: str
        """
        self.KeyId = None
        self.KeyName = None
        self.Description = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyKeyPairAttributeResponse(AbstractModel):
    """ModifyKeyPairAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLaunchTemplateDefaultVersionRequest(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion request structure.

    """

    def __init__(self):
        r"""
        :param LaunchTemplateId: The launch template ID
        :type LaunchTemplateId: str
        :param DefaultVersion: The number of the version that you want to set as the default version
        :type DefaultVersion: int
        """
        self.LaunchTemplateId = None
        self.DefaultVersion = None


    def _deserialize(self, params):
        self.LaunchTemplateId = params.get("LaunchTemplateId")
        self.DefaultVersion = params.get("DefaultVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLaunchTemplateDefaultVersionResponse(AbstractModel):
    """ModifyLaunchTemplateDefaultVersion response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OperationCountLimit(AbstractModel):
    """Describes the maximum number of times you can perform an operation on a single instance.

    """

    def __init__(self):
        r"""
        :param Operation: Instance operation. Valid values: <br><li>`INSTANCE_DEGRADE`: downgrade an instance<br><li>`INTERNET_CHARGE_TYPE_CHANGE`: modify the billing plan of the network connection
        :type Operation: str
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param CurrentCount: Number of operations already performed. If it returns `-1`, it means there is no limit on the times of the operation.
        :type CurrentCount: int
        :param LimitCount: Maximum number of times you can perform an operation. If it returns `-1`, it means there is no limit on the times of the operation. If it returns `0`, it means that configuration modification is not supported.
        :type LimitCount: int
        """
        self.Operation = None
        self.InstanceId = None
        self.CurrentCount = None
        self.LimitCount = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.InstanceId = params.get("InstanceId")
        self.CurrentCount = params.get("CurrentCount")
        self.LimitCount = params.get("LimitCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """Supported operating system types.

    """

    def __init__(self):
        r"""
        :param OsName: Operating system type
        :type OsName: str
        :param OsVersions: Supported operating system versions
        :type OsVersions: list of str
        :param Architecture: Supported operating system architecture
        :type Architecture: list of str
        """
        self.OsName = None
        self.OsVersions = None
        self.Architecture = None


    def _deserialize(self, params):
        self.OsName = params.get("OsName")
        self.OsVersions = params.get("OsVersions")
        self.Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """Placement of an instance, including its availability zone, project, host (for CDH products only), master host IP, etc.

    """

    def __init__(self):
        r"""
        :param Zone: ID of the availability zone where the instance resides. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/35071) API and obtain the ID in the returned `Zone` field.
        :type Zone: str
        :param ProjectId: ID of the project to which the instance belongs. To obtain the project IDs, you can call [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) and look for the `projectId` fields in the response. If this parameter is not specified, the default project will be used.
        :type ProjectId: int
        :param HostIds: ID list of CDHs from which the instance can be created. If you have purchased CDHs and specify this parameter, the instances you purchase will be randomly deployed on the CDHs.
        :type HostIds: list of str
        :param HostIps: Master host IP used to create the CVM
        :type HostIps: list of str
        :param HostId: The ID of the CDH to which the instance belongs, only used as an output parameter.
        :type HostId: str
        """
        self.Zone = None
        self.ProjectId = None
        self.HostIds = None
        self.HostIps = None
        self.HostId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.HostIds = params.get("HostIds")
        self.HostIps = params.get("HostIps")
        self.HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Price.

    """

    def __init__(self):
        r"""
        :param InstancePrice: Instance price.
        :type InstancePrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        :param BandwidthPrice: Network price.
        :type BandwidthPrice: :class:`tencentcloud.cvm.v20170312.models.ItemPrice`
        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurchaseReservedInstancesOfferingRequest(AbstractModel):
    """PurchaseReservedInstancesOffering request structure.

    """

    def __init__(self):
        r"""
        :param InstanceCount: The number of the Reserved Instance you are purchasing.
        :type InstanceCount: int
        :param ReservedInstancesOfferingId: The ID of the Reserved Instance.
        :type ReservedInstancesOfferingId: str
        :param DryRun: Dry run
        :type DryRun: bool
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.<br>For more information, see Ensuring Idempotency.
        :type ClientToken: str
        :param ReservedInstanceName: Reserved instance name.<br><li>The RI name defaults to “unnamed” if this parameter is left empty.</li><li>You can enter any name within 60 characters (including the pattern string).</li>
        :type ReservedInstanceName: str
        """
        self.InstanceCount = None
        self.ReservedInstancesOfferingId = None
        self.DryRun = None
        self.ClientToken = None
        self.ReservedInstanceName = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.DryRun = params.get("DryRun")
        self.ClientToken = params.get("ClientToken")
        self.ReservedInstanceName = params.get("ReservedInstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurchaseReservedInstancesOfferingResponse(AbstractModel):
    """PurchaseReservedInstancesOffering response structure.

    """

    def __init__(self):
        r"""
        :param ReservedInstanceId: The ID of the Reserved Instance purchased.
        :type ReservedInstanceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReservedInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedInstanceId = params.get("ReservedInstanceId")
        self.RequestId = params.get("RequestId")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance IDs. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. You can operate up to 100 instances in each request.
        :type InstanceIds: list of str
        :param ForceReboot: Whether to forcibly restart an instance after a normal restart fails. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default value: `FALSE`. This parameter has been disused. We recommend using `StopType` instead. Note that `ForceReboot` and `StopType` parameters cannot be specified at the same time.
        :type ForceReboot: bool
        :param StopType: Shutdown type. Valid values: <br><li>SOFT: soft shutdown<br><li>HARD: hard shutdown<br><li>SOFT_FIRST: perform a soft shutdown first, and perform a hard shutdown if the soft shutdown fails<br><br>Default value: SOFT.
        :type StopType: str
        """
        self.InstanceIds = None
        self.ForceReboot = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ForceReboot = params.get("ForceReboot")
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region information.

    """

    def __init__(self):
        r"""
        :param Region: Region name, such as `ap-guangzhou`
        :type Region: str
        :param RegionName: Region description, such as South China (Guangzhou)
        :type RegionName: str
        :param RegionState: Whether the region is available
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcRequest(AbstractModel):
    """RemoveChcAssistVpc request structure.

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC ID
        :type ChcIds: list of str
        """
        self.ChcIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcAssistVpcResponse(AbstractModel):
    """RemoveChcAssistVpc response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveChcDeployVpcRequest(AbstractModel):
    """RemoveChcDeployVpc request structure.

    """

    def __init__(self):
        r"""
        :param ChcIds: CHC ID
        :type ChcIds: list of str
        """
        self.ChcIds = None


    def _deserialize(self, params):
        self.ChcIds = params.get("ChcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveChcDeployVpcResponse(AbstractModel):
    """RemoveChcDeployVpc response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReservedInstanceConfigInfoItem(AbstractModel):
    """Static configurations of the reserved instance. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param Type: Abbreviation name of the instance type.
        :type Type: str
        :param TypeName: Full name of the instance type.
        :type TypeName: str
        :param Order: Priority.
        :type Order: int
        :param InstanceFamilies: List of instance families.
        :type InstanceFamilies: list of ReservedInstanceFamilyItem
        """
        self.Type = None
        self.TypeName = None
        self.Order = None
        self.InstanceFamilies = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        self.Order = params.get("Order")
        if params.get("InstanceFamilies") is not None:
            self.InstanceFamilies = []
            for item in params.get("InstanceFamilies"):
                obj = ReservedInstanceFamilyItem()
                obj._deserialize(item)
                self.InstanceFamilies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceFamilyItem(AbstractModel):
    """RI-related instance family. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param InstanceFamily: Instance family.
        :type InstanceFamily: str
        :param Order: Priority.
        :type Order: int
        :param InstanceTypes: List of instance types.
        :type InstanceTypes: list of ReservedInstanceTypeItem
        """
        self.InstanceFamily = None
        self.Order = None
        self.InstanceTypes = None


    def _deserialize(self, params):
        self.InstanceFamily = params.get("InstanceFamily")
        self.Order = params.get("Order")
        if params.get("InstanceTypes") is not None:
            self.InstanceTypes = []
            for item in params.get("InstanceTypes"):
                obj = ReservedInstanceTypeItem()
                obj._deserialize(item)
                self.InstanceTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePrice(AbstractModel):
    """Price of the reserved instance. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param OriginalFixedPrice: Original upfront payment, in USD.
        :type OriginalFixedPrice: float
        :param DiscountFixedPrice: Discounted upfront payment, in USD.
        :type DiscountFixedPrice: float
        :param OriginalUsagePrice: Original subsequent unit price, in USD/hr.
        :type OriginalUsagePrice: float
        :param DiscountUsagePrice: Discounted subsequent unit price, in USD/hr.
        :type DiscountUsagePrice: float
        """
        self.OriginalFixedPrice = None
        self.DiscountFixedPrice = None
        self.OriginalUsagePrice = None
        self.DiscountUsagePrice = None


    def _deserialize(self, params):
        self.OriginalFixedPrice = params.get("OriginalFixedPrice")
        self.DiscountFixedPrice = params.get("DiscountFixedPrice")
        self.OriginalUsagePrice = params.get("OriginalUsagePrice")
        self.DiscountUsagePrice = params.get("DiscountUsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancePriceItem(AbstractModel):
    """Price information of the reserved instance based on the payment method. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param OfferingType: Payment method. Valid values: All Upfront, Partial Upfront, and No Upfront.
        :type OfferingType: str
        :param FixedPrice: Upfront payment, in USD.
        :type FixedPrice: float
        :param UsagePrice: Subsequent unit price, in USD/hr.
        :type UsagePrice: float
        :param ReservedInstancesOfferingId: The ID of the reserved instance offering.
        :type ReservedInstancesOfferingId: str
        :param Zone: The availability zone in which the reserved instance can be purchased.
        :type Zone: str
        :param Duration: The **validity** of the reserved instance in seconds, which is the purchased usage period. For example, `31536000`.
Unit: second
        :type Duration: int
        :param ProductDescription: The operating system of the reserved instance, such as `linux`.
Valid value: linux.
        :type ProductDescription: str
        """
        self.OfferingType = None
        self.FixedPrice = None
        self.UsagePrice = None
        self.ReservedInstancesOfferingId = None
        self.Zone = None
        self.Duration = None
        self.ProductDescription = None


    def _deserialize(self, params):
        self.OfferingType = params.get("OfferingType")
        self.FixedPrice = params.get("FixedPrice")
        self.UsagePrice = params.get("UsagePrice")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.Zone = params.get("Zone")
        self.Duration = params.get("Duration")
        self.ProductDescription = params.get("ProductDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstanceTypeItem(AbstractModel):
    """Reserved instance specification. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        r"""
        :param InstanceType: Instance type.
        :type InstanceType: str
        :param Cpu: Number of CPU cores.
        :type Cpu: int
        :param Memory: Memory size.
        :type Memory: int
        :param Gpu: Number of GPUs.
        :type Gpu: int
        :param Fpga: Number of FPGAs.
        :type Fpga: int
        :param StorageBlock: Number of local storage blocks.
        :type StorageBlock: int
        :param NetworkCard: Number of NICs.
        :type NetworkCard: int
        :param MaxBandwidth: Maximum bandwidth.
        :type MaxBandwidth: float
        :param Frequency: CPU frequency.
        :type Frequency: str
        :param CpuModelName: CPU type.
        :type CpuModelName: str
        :param Pps: Packet forwarding rate.
        :type Pps: int
        :param Externals: Other information.
        :type Externals: :class:`tencentcloud.cvm.v20170312.models.Externals`
        :param Remark: Remarks.
        :type Remark: str
        :param Prices: Price information about the reserved instance.
        :type Prices: list of ReservedInstancePriceItem
        """
        self.InstanceType = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.Fpga = None
        self.StorageBlock = None
        self.NetworkCard = None
        self.MaxBandwidth = None
        self.Frequency = None
        self.CpuModelName = None
        self.Pps = None
        self.Externals = None
        self.Remark = None
        self.Prices = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.Fpga = params.get("Fpga")
        self.StorageBlock = params.get("StorageBlock")
        self.NetworkCard = params.get("NetworkCard")
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.Frequency = params.get("Frequency")
        self.CpuModelName = params.get("CpuModelName")
        self.Pps = params.get("Pps")
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.Remark = params.get("Remark")
        if params.get("Prices") is not None:
            self.Prices = []
            for item in params.get("Prices"):
                obj = ReservedInstancePriceItem()
                obj._deserialize(item)
                self.Prices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReservedInstancesOffering(AbstractModel):
    """The information of the Reserved Instance offering.

    """

    def __init__(self):
        r"""
        :param Zone: The availability zones in which the Reserved Instance can be purchased, such as ap-guangzhou-1.
Valid value: <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">Availability Zones</a>
        :type Zone: str
        :param CurrencyCode: The billing currency of the Reserved Instance you are purchasing. It's specified using ISO 4217 standard currency.
Value: USD.
        :type CurrencyCode: str
        :param Duration: The **validity** of the Reserved Instance in seconds, which is the purchased usage period. For example, 31536000.
Unit: second
        :type Duration: int
        :param FixedPrice: The purchase price of the Reserved Instance, such as 4000.0.
Unit: this field uses the currency code specified in `currencyCode`, and only supports “USD” at this time.
        :type FixedPrice: float
        :param InstanceType: The instance model of the Reserved Instance, such as S3.MEDIUM4.
Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/11518">Reserved Instance Types</a>
        :type InstanceType: str
        :param OfferingType: The payment term of the Reserved Instance, such as **All Upfront**.
Valid value: All Upfront.
        :type OfferingType: str
        :param ReservedInstancesOfferingId: The ID of the Reserved Instance offering, such as 650c138f-ae7e-4750-952a-96841d6e9fc1.
        :type ReservedInstancesOfferingId: str
        :param ProductDescription: The operating system of the Reserved Instance, such as **linux**.
Valid value: linux.
        :type ProductDescription: str
        :param UsagePrice: The hourly usage price of the Reserved Instance, such as 0.0.
Currently, the only supported payment mode is **All Upfront**, so the default value of `UsagePrice` is 0 USD/hr.
Unit: USD/hr. This field uses the currency code specified in `currencyCode`, and only supports “USD” at this time.
        :type UsagePrice: float
        """
        self.Zone = None
        self.CurrencyCode = None
        self.Duration = None
        self.FixedPrice = None
        self.InstanceType = None
        self.OfferingType = None
        self.ReservedInstancesOfferingId = None
        self.ProductDescription = None
        self.UsagePrice = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.CurrencyCode = params.get("CurrencyCode")
        self.Duration = params.get("Duration")
        self.FixedPrice = params.get("FixedPrice")
        self.InstanceType = params.get("InstanceType")
        self.OfferingType = params.get("OfferingType")
        self.ReservedInstancesOfferingId = params.get("ReservedInstancesOfferingId")
        self.ProductDescription = params.get("ProductDescription")
        self.UsagePrice = params.get("UsagePrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceRequest(AbstractModel):
    """ResetInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param ImageId: Specified effective [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways:<br/><li>for IDs of `public images`, `custom images`, and `shared images`, log in to the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE); for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>Call the API [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
<br>Default value: current image.
        :type ImageId: str
        :param SystemDisk: Configurations of the system disk. For an instance whose system disk is a cloud disk, this parameter can be used to expand the system disk by specifying a new capacity after reinstallation. The system disk capacity can only be expanded but not shrunk. Reinstalling the system can only resize rather than changing the type of the system disk.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param HostName: Host name of the CVM, editable during the system reinstallation. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>For Windows instances, the host name must consist of 2-15 characters , including uppercase and lowercase letters, numbers, or hyphens (-). It cannot contain periods (.) or contain only numbers.<br><li>For other instances, such as Linux instances, the host name must consist of 2-60 characters, including multiple periods (.), and allows uppercase and lowercase letters, numbers, or hyphens (-) between any two periods (.).
        :type HostName: str
        """
        self.InstanceId = None
        self.ImageId = None
        self.SystemDisk = None
        self.LoginSettings = None
        self.EnhancedService = None
        self.HostName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstanceResponse(AbstractModel):
    """ResetInstance response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """ResetInstancesInternetMaxBandwidth request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100. When changing the bandwidth of instances with `BANDWIDTH_PREPAID` or `BANDWIDTH_POSTPAID_BY_HOUR` as the network billing method, you can only specify one instance at a time.
        :type InstanceIds: list of str
        :param InternetAccessible: Configuration of public network egress bandwidth. The maximum bandwidth varies among different models. For more information, see the documentation on bandwidth limits. Currently only the `InternetMaxBandwidthOut` parameter is supported.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param StartTime: Date from which the new bandwidth takes effect. Format: `YYYY-MM-DD`, such as `2016-10-30`. The starting date cannot be earlier than the current date. If the starting date is the current date, the new bandwidth takes effect immediately. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type StartTime: str
        :param EndTime: Date until which the new bandwidth is effective. Format: `YYYY-MM-DD`, such as `2016-10-30`. The validity period of the new bandwidth covers the end date. The end date cannot be later than the expiration date of a prepaid instance. You can query the expiration time of an instance by calling [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728) and looking for `ExpiredTime` in the response. This parameter is only valid for prepaid bandwidth. If you specify the parameter for bandwidth with other network billing methods, an error code will be returned.
        :type EndTime: str
        """
        self.InstanceIds = None
        self.InternetAccessible = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """ResetInstancesInternetMaxBandwidth response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param Password: Login password of the instance. The password requirements vary among different operating systems:
For a Linux instance, the password must be 8 to 30 characters in length; password with more than 12 characters is recommended. It cannot begin with "/", and must contain at least one character from three of the following categories: <br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\`\~!@#$%^&\*-+=\_|{}[]:;'<>,.?/
For a Windows CVM, the password must be 12 to 30 characters in length. It cannot begin with "/" or contain a username. It must contain at least one character from three of the following categories: <br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\`\~!@#$%^&\*-+=\_|{}[]:;' <>,.?/<br><li>If the specified instances include both `Linux` and `Windows` instances, you will need to follow the password requirements for `Windows` instances.
        :type Password: str
        :param UserName: Username of the instance operating system for which the password needs to be reset. This parameter is limited to 64 characters.
        :type UserName: str
        :param ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally.
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.Password = None
        self.UserName = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Password = params.get("Password")
        self.UserName = params.get("UserName")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesTypeRequest(AbstractModel):
    """ResetInstancesType request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call the [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API and find the value `InstanceId` in the response. The maximum number of instances in each request is 1.
        :type InstanceIds: list of str
        :param InstanceType: Instance model. Different resource specifications are specified for different models. For specific values, call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) to get the latest specification list or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1).
        :type InstanceType: str
        :param ForceStop: Forced shutdown of a running instances. We recommend you firstly try to shut down a running instance manually. Valid values: <br><li>TRUE: forced shutdown of an instance after a normal shutdown fails.<br><li>FALSE: no forced shutdown of an instance after a normal shutdown fails.<br><br>Default value: FALSE.<br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force a CVM to shut off if the normal shutdown fails.
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesTypeResponse(AbstractModel):
    """ResetInstancesType response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeInstanceDisksRequest(AbstractModel):
    """ResizeInstanceDisks request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param DataDisks: Configuration of data disks to be expanded. Currently you can only use the API to expand non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is not elastic. Data disk capacity unit: GB; minimum increment: 10 GB. For more information on selecting the data disk type, see the [product overview on cloud disks](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1). Available data disk types are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies by data disk type.
        :type DataDisks: list of DataDisk
        :param ForceStop: Whether to force shut down a running instances. It is recommended to manually shut down a running instance before resetting the user password. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails. <br><li>FALSE: do not force shut down an instance after a normal shutdown fails. <br><br>Default value: FALSE. <br><br>A forced shutdown is similar to switching off the power of a physical computer. It may cause data loss or file system corruption. Be sure to only force shut down a CVM when it cannot be shut down normally.
        :type ForceStop: bool
        :param SystemDisk: Configuration of the system disk to be expanded. Only cloud disks are supported.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param ResizeOnline: Whether the cloud disk is expanded online.
        :type ResizeOnline: bool
        """
        self.InstanceId = None
        self.DataDisks = None
        self.ForceStop = None
        self.SystemDisk = None
        self.ResizeOnline = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.ForceStop = params.get("ForceStop")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        self.ResizeOnline = params.get("ResizeOnline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeInstanceDisksResponse(AbstractModel):
    """ResizeInstanceDisks response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunAutomationServiceEnabled(AbstractModel):
    """Describes the TAT service information.

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable the TAT service. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default: `FALSE`.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceChargeType: Instance [billing type](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1). <br><li>`POSTPAID_BY_HOUR`: Hourly-based pay-as-you-go <br><li>`CDHPAID`: Dedicated CVM (associated with a dedicated host. Resource usage of the dedicated host is free of charge.) <br><li>`SPOTPAID`: [Spot instance](https://intl.cloud.tencent.com/document/product/213/17817)<br>Default value: `POSTPAID_BY_HOUR`.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Details of the monthly subscription, including the purchase period, auto-renewal. It is required if the `InstanceChargeType` is `PREPAID`.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param Placement: Location of the instance. You can use this parameter to specify the availability zone, project, and CDH (for dedicated CVMs).
 <b>Note: `Placement` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `Placement` prevails.</b>
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param InstanceType: The instance model. 
<br><li>To view specific values for `POSTPAID_BY_HOUR` instances, you can call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If this parameter is not specified, `S1.SMALL1` will be used by default.<br><li>For `CDHPAID` instances, the value of this parameter is in the format of `CDH_XCXG` based on the number of CPU cores and memory capacity. For example, if you want to create a CDH instance with a single-core CPU and 1 GB memory, specify this parameter as `CDH_1C1G`.
        :type InstanceType: str
        :param ImageId: The [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are three types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><br/>To check the image ID:<br/><li>For public images, custom images, and shared images, go to the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1), pass in `InstanceType` to retrieve the list of images supported by the current model, and then find the `ImageId` in the response.</li>
 <b>Note: `ImageId` is required when `LaunchTemplate` is not specified. If both the parameters are passed in, `ImageId` prevails.</b>
        :type ImageId: str
        :param SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: The configuration information of instance data disks. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC, CLOUD_PREMIUM, or CLOUD_SSD data disks.
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: Configuration information of VPC. This parameter is used to specify VPC ID and subnet ID, etc. If a VPC IP is specified in this parameter, it indicates the primary ENI IP of each instance. The value of parameter InstanceCount must be the same as the number of VPC IPs, which cannot be greater than 20.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: The number of instances to be purchased. Value range for pay-as-you-go instances: [1, 100]. Default value: `1`. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on the quota, see [Quota for CVM Instances](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param InstanceName: Instance name to be displayed. <br><li>If this parameter is not specified, "Unnamed" will be displayed by default. </li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`. </li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and the instance name body is `server_`, the instance names will be `server_1` and `server_2`. </li><li>This parameter can contain up to 60 characters, including the pattern string.
        :type InstanceName: str
        :param LoginSettings: Instance login settings. You can use this parameter to set the login method, password and key of the instance, or keep the original login settings of the image. If it's not specified, the user needs to set the login password using the "Reset password" option in the CVM console or calling the API `ResetInstancesPassword` to complete the creation of the CVM instance(s).
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will be associated with default security groups.
        :type SecurityGroupIds: list of str
        :param EnhancedService: Enhanced service. You can use this parameter to specify whether to enable services such as Anti-DDoS and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Anti-DDoS are enabled for public images by default. However, for custom images and images from the marketplace, Anti-DDoS and Cloud Monitor are not enabled by default. The original services in the image will be retained.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
        :type ClientToken: str
        :param HostName: Instance hostname. <br><li>Dots (.) and dashes (-) can not be used as the first or last character of HostName nor used consecutively. <br<li>Windows instances: 2 to 15 characters, including English letters (case-insensitive), numbers and dashes (-). Dots and numeric-only names are not allowed. <br><li>Other instances (Linux, etc.): 2 to 60 characters, including English letters (case-insensitive), numbers, dashes (-) and dots. Note that consecutive dots are not allowed.<br><li>Batch naming: use `{R:x}` for batch naming if multiple instances are purchased. `x` is the serial number of the instance. It’s generated by [x, x+n-1], where `n` refers to the number of instances purchased. For example, if `server{R:3}` is input, if you purchase one instance, the hostname is `server3`. If you purchase two instances, the hostnames are `server3` and `server4` respectively. You can specify multiple pattern strings `{R:x}`. </li><br><li>Purchasing multiple instances: If no pattern string is specified, you shall add suffixes `1, 2...n` to the instance hostname. `n` represents the number of purchased instances. For example, if the instance hostname is `server`,  when two instances are purchased, the hostnames of instances purchased are respectively `server1` and `server2`.
        :type HostName: str
        :param ActionTimer: Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported.
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param DisasterRecoverGroupIds: Placement group ID. You can only specify one.
        :type DisasterRecoverGroupIds: list of str
        :param TagSpecification: List of tag description. By specifying this parameter, the tag can be bound to the corresponding CVM and CBS instances at the same time.
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: The market options of the instance.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param UserData: User data provided to the instance. This parameter needs to be encoded in base64 format with the maximum size of 16 KB. For more information on how to get the value of this parameter, see the commands you need to execute on startup for [Windows](https://intl.cloud.tencent.com/document/product/213/17526) or [Linux](https://intl.cloud.tencent.com/document/product/213/17525).
        :type UserData: str
        :param DryRun: Whether the request is a dry run only.
`true`: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available.
If the dry run fails, the corresponding error code will be returned.
If the dry run succeeds, the RequestId will be returned.
`false` (default value): Send a normal request and create instance(s) if all the requirements are met.
        :type DryRun: bool
        :param CamRoleName: CAM role name, which can be obtained from the `roleName` field in the response of the [`DescribeRoleList`](https://intl.cloud.tencent.com/document/product/598/36223?from_cn_redirect=1) API.
        :type CamRoleName: str
        :param HpcClusterId: HPC cluster ID. The HPC cluster must and can only be specified for a high-performance computing instance.
        :type HpcClusterId: str
        :param LaunchTemplate: Instance launch template.
        :type LaunchTemplate: :class:`tencentcloud.cvm.v20170312.models.LaunchTemplate`
        :param DedicatedClusterId: Specify the ID of the dedicated cluster where the CVM is created.
        :type DedicatedClusterId: str
        :param ChcIds: Specify the CHC physical server that used to create the CHC CVM.
        :type ChcIds: list of str
        :param DisableApiTermination: Whether the termination protection is enabled. Values: <br><li>`TRUE`: Enable instance protection, which means that this instance can not be deleted by an API action.<br><li>`FALSE`: Do not enable the instance protection.<br><br>Default value: `FALSE`.
        :type DisableApiTermination: bool
        """
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.Placement = None
        self.InstanceType = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.ActionTimer = None
        self.DisasterRecoverGroupIds = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.UserData = None
        self.DryRun = None
        self.CamRoleName = None
        self.HpcClusterId = None
        self.LaunchTemplate = None
        self.DedicatedClusterId = None
        self.ChcIds = None
        self.DisableApiTermination = None


    def _deserialize(self, params):
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceType = params.get("InstanceType")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.UserData = params.get("UserData")
        self.DryRun = params.get("DryRun")
        self.CamRoleName = params.get("CamRoleName")
        self.HpcClusterId = params.get("HpcClusterId")
        if params.get("LaunchTemplate") is not None:
            self.LaunchTemplate = LaunchTemplate()
            self.LaunchTemplate._deserialize(params.get("LaunchTemplate"))
        self.DedicatedClusterId = params.get("DedicatedClusterId")
        self.ChcIds = params.get("ChcIds")
        self.DisableApiTermination = params.get("DisableApiTermination")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances response structure.

    """

    def __init__(self):
        r"""
        :param InstanceIdSet: If you use this API to create instance(s), this parameter will be returned, representing one or more instance IDs. Retuning the instance ID list does not necessarily mean that the instance(s) were created successfully. To check whether the instance(s) were created successfully, you can call [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and check the status of the instances in `InstancesSet` in the response. If the status of an instance changes from "PENDING" to "RUNNING", it means that the instance has been created successfully.
        :type InstanceIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Monitor service.

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable [Cloud Monitor](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Monitor <br><li>FALSE: do not enable Cloud Monitor <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Security service.

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable [Cloud Security](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Security <br><li>FALSE: do not enable Cloud Security <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SharePermission(AbstractModel):
    """Describes image sharing information.

    """

    def __init__(self):
        r"""
        :param CreatedTime: Time when an image was shared.
        :type CreatedTime: str
        :param AccountId: ID of the account with which the image is shared.
        :type AccountId: str
        """
        self.CreatedTime = None
        self.AccountId = None


    def _deserialize(self, params):
        self.CreatedTime = params.get("CreatedTime")
        self.AccountId = params.get("AccountId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """Describes information on the snapshot associated with an image.

    """

    def __init__(self):
        r"""
        :param SnapshotId: Snapshot ID.
        :type SnapshotId: str
        :param DiskUsage: Type of the cloud disk used to create the snapshot. Valid values:
SYSTEM_DISK: system disk
DATA_DISK: data disk
        :type DiskUsage: str
        :param DiskSize: Size of the cloud disk used to create the snapshot; unit: GB.
        :type DiskSize: int
        """
        self.SnapshotId = None
        self.DiskUsage = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpotMarketOptions(AbstractModel):
    """Options related to bidding.

    """

    def __init__(self):
        r"""
        :param MaxPrice: Bidding price
        :type MaxPrice: str
        :param SpotInstanceType: Bidding request type. Currently only "one-time" is supported.
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    """StopInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param ForceStop: (Disused. Please use `StopType` instead.) Whether to forcibly shut down an instance after a normal shutdown fails. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default value: `FALSE`. 
        :type ForceStop: bool
        :param StopType: Instance shutdown mode. Valid values: <br><li>SOFT_FIRST: perform a soft shutdown first, and force shut down the instance if the soft shutdown fails <br><li>HARD: force shut down the instance directly <br><li>SOFT: soft shutdown only <br>Default value: SOFT.
        :type StopType: str
        :param StoppedMode: Billing method of a pay-as-you-go instance after shutdown.
Valid values: <br><li>KEEP_CHARGING: billing continues after shutdown <br><li>STOP_CHARGING: billing stops after shutdown <br>Default value: KEEP_CHARGING.
This parameter is only valid for some pay-as-you-go instances using cloud disks. For more information, see [No charges when shut down for pay-as-you-go instances](https://intl.cloud.tencent.com/document/product/213/19918).
        :type StoppedMode: str
        """
        self.InstanceIds = None
        self.ForceStop = None
        self.StopType = None
        self.StoppedMode = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ForceStop = params.get("ForceStop")
        self.StopType = params.get("StopType")
        self.StoppedMode = params.get("StoppedMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StorageBlock(AbstractModel):
    """Information on local HDD storage.

    """

    def __init__(self):
        r"""
        :param Type: Local HDD storage type. Value: LOCAL_PRO.
Note: This field may return null, indicating that no valid value is found.
        :type Type: str
        :param MinSize: Minimum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :type MinSize: int
        :param MaxSize: Maximum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :type MaxSize: int
        """
        self.Type = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesRequest(AbstractModel):
    """SyncImages request structure.

    """

    def __init__(self):
        r"""
        :param ImageIds: List of image IDs. You can obtain the image IDs in two ways: <br><li>Call the [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) API and find the value of `ImageId` in the response. <br><li>Find the image IDs in the [Image Console](https://console.cloud.tencent.com/cvm/image). <br>The specified images must meet the following requirement: <br><li>the images must be in the `NORMAL` state. <br>For more information on image status, see [Image Data Table](https://intl.cloud.tencent.com/document/product/213/15753?from_cn_redirect=1#Image).
        :type ImageIds: list of str
        :param DestinationRegions: List of destination regions for synchronization. Limits:<br><li>It must be a valid region.<br><li>For a custom image, the destination region cannot be the source region.<br><li>For a shared image, the destination region must be the source region, which indicates to create a copy of the image as a custom image in the same region.<br><li>Image synchronization is only available in limited regions.<br>See [Region](https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1).
        :type DestinationRegions: list of str
        :param DryRun: Checks whether image synchronization can be initiated.
        :type DryRun: bool
        :param ImageName: Destination image name.
        :type ImageName: str
        """
        self.ImageIds = None
        self.DestinationRegions = None
        self.DryRun = None
        self.ImageName = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        self.DestinationRegions = params.get("DestinationRegions")
        self.DryRun = params.get("DryRun")
        self.ImageName = params.get("ImageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncImagesResponse(AbstractModel):
    """SyncImages response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """Describes information on the block device where the operating system is stored, i.e., the system disk.

    """

    def __init__(self):
        r"""
        :param DiskType: System disk type. For more information about the limits of system disk types, please see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values:<br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_SSD: SSD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud storage<br><li>CLOUD_BSSD: Balanced SSD<br><br>The disk currently in stock will be used by default.
        :type DiskType: str
        :param DiskId: System disk ID. System disks whose type is `LOCAL_BASIC` or `LOCAL_SSD` do not have an ID and do not support this parameter.
It is only used as a response parameter for APIs such as `DescribeInstances`, and cannot be used as a request parameter for APIs such as `RunInstances`.
        :type DiskId: str
        :param DiskSize: System disk size; unit: GB; default value: 50 GB.
        :type DiskSize: int
        :param CdcId: ID of the dedicated cluster to which the instance belongs.
        :type CdcId: str
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None
        self.CdcId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Key-value pair of a tag.

    """

    def __init__(self):
        r"""
        :param Key: Tag key
        :type Key: str
        :param Value: Tag value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """Description of tags associated with resource instances during instance creation.

    """

    def __init__(self):
        r"""
        :param ResourceType: The type of resource that the tag is bound to. Valid values: `instance` (for CVM), `host` (for CDH), `image` (for image), and `keypair` (for key).
        :type ResourceType: str
        :param Tags: List of tags
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """Describes information on VPC, including subnets, IP addresses, etc.

    """

    def __init__(self):
        r"""
        :param VpcId: VPC ID in the format of `vpc-xxx`. To obtain valid VPC IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or call the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API and look for the `unVpcId` fields in the response. If you specify `DEFAULT` for both `VpcId` and `SubnetId` when creating an instance, the default VPC will be used.
        :type VpcId: str
        :param SubnetId: VPC subnet ID in the format `subnet-xxx`. To obtain valid subnet IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/subnet?rid=1) or call [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) and look for the `unSubnetId` fields in the response. If you specify `DEFAULT` for both `SubnetId` and `VpcId` when creating an instance, the default VPC will be used.
        :type SubnetId: str
        :param AsVpcGateway: Whether to use a CVM instance as a public gateway. The public gateway is only available when the instance has a public IP and resides in a VPC. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default: `FALSE`.
        :type AsVpcGateway: bool
        :param PrivateIpAddresses: Array of VPC subnet IPs. You can use this parameter when creating instances or modifying VPC attributes of instances. Currently you can specify multiple IPs in one subnet only when creating multiple instances at the same time.
        :type PrivateIpAddresses: list of str
        :param Ipv6AddressCount: Number of IPv6 addresses randomly generated for the ENI.
        :type Ipv6AddressCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.AsVpcGateway = None
        self.PrivateIpAddresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AsVpcGateway = params.get("AsVpcGateway")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Information on availability zones.

    """

    def __init__(self):
        r"""
        :param Zone: Availability zone name, such as `ap-guangzhou-3`.
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
        :param ZoneName: Availability zone description, such as Guangzhou Zone 3.
        :type ZoneName: str
        :param ZoneId: Availability zone ID.
        :type ZoneId: str
        :param ZoneState: Availability zone status. Valid values: `AVAILABLE`: available; `UNAVAILABLE`: unavailable.
        :type ZoneState: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        