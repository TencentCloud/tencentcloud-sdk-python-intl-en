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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class ActionTimer(AbstractModel):
    """Scheduled tasks.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AllocateHostsRequest(AbstractModel):
    """AllocateHosts request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AllocateHostsResponse(AbstractModel):
    """AllocateHosts response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AssociateInstancesKeyPairsResponse(AbstractModel):
    """AssociateInstancesKeyPairs response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChargePrepaid(AbstractModel):
    """Parameters related to the prepaid billing method, including the subscription period, the auto renewal logic, etc.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDisasterRecoverGroupRequest(AbstractModel):
    """CreateDisasterRecoverGroup request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDisasterRecoverGroupResponse(AbstractModel):
    """CreateDisasterRecoverGroup response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateImageRequest(AbstractModel):
    """CreateImage request structure.

    """

    def __init__(self):
        """
        :param ImageName: Image name
        :type ImageName: str
        :param InstanceId: Instance ID used to create an image.
        :type InstanceId: str
        :param ImageDescription: Image description
        :type ImageDescription: str
        :param ForcePoweroff: Whether to force shut down an instance to create an image when a soft shutdown fails
        :type ForcePoweroff: str
        :param Sysprep: Whether to enable Sysprep when creating a Windows image. Click [here](https://intl.cloud.tencent.com/document/product/213/43498?from_cn_redirect=1) to learn more about Sysprep.
        :type Sysprep: str
        :param DataDiskIds: Specified data disk ID included in the full image created from the instance.
        :type DataDiskIds: list of str
        :param SnapshotIds: Specified snapshot ID used to create an image. A system disk snapshot must be included. It cannot be passed together with `InstanceId`.
        :type SnapshotIds: list of str
        :param DryRun: Success status of this request, without affecting the resources involved
        :type DryRun: bool
        """
        self.ImageName = None
        self.InstanceId = None
        self.ImageDescription = None
        self.ForcePoweroff = None
        self.Sysprep = None
        self.DataDiskIds = None
        self.SnapshotIds = None
        self.DryRun = None


    def _deserialize(self, params):
        self.ImageName = params.get("ImageName")
        self.InstanceId = params.get("InstanceId")
        self.ImageDescription = params.get("ImageDescription")
        self.ForcePoweroff = params.get("ForcePoweroff")
        self.Sysprep = params.get("Sysprep")
        self.DataDiskIds = params.get("DataDiskIds")
        self.SnapshotIds = params.get("SnapshotIds")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateImageResponse(AbstractModel):
    """CreateImage response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair request structure.

    """

    def __init__(self):
        """
        :param KeyName: Name of the key pair, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param ProjectId: The ID of the project to which the new key pair belongs.
You can query the project IDs in two ways:
<li>Query the project IDs in the project list.
<li>Call `DescribeProject` and look for `projectId` in the response.
        :type ProjectId: int
        """
        self.KeyName = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DataDisk(AbstractModel):
    """Describes data disk information.

    """

    def __init__(self):
        """
        :param DiskSize: Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.
        :type DiskSize: int
        :param DiskType: Data disk type. For more information about limits on different data disk types, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values: <br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>LOCAL_NVME: local NVME disk, specified in the `InstanceType`<br><li>LOCAL_PRO: local HDD disk, specified in the `InstanceType`<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: Tremendous SSD<br><br>Default value: LOCAL_BASIC.<br><br>This parameter is invalid for the `ResizeInstanceDisk` API.
        :type DiskType: str
        :param DiskId: Data disk ID. Data disks of the type `LOCAL_BASIC` or `LOCAL_SSD` do not have IDs and do not support this parameter.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteDisasterRecoverGroupsRequest(AbstractModel):
    """DeleteDisasterRecoverGroups request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteDisasterRecoverGroupsResponse(AbstractModel):
    """DeleteDisasterRecoverGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteImagesRequest(AbstractModel):
    """DeleteImages request structure.

    """

    def __init__(self):
        """
        :param ImageIds: List of the IDs of the instances to be deleted.
        :type ImageIds: list of str
        """
        self.ImageIds = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteImagesResponse(AbstractModel):
    """DeleteImages response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteKeyPairsRequest(AbstractModel):
    """DeleteKeyPairs request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteKeyPairsResponse(AbstractModel):
    """DeleteKeyPairs response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDisasterRecoverGroupQuotaRequest(AbstractModel):
    """DescribeDisasterRecoverGroupQuota request structure.

    """


class DescribeDisasterRecoverGroupQuotaResponse(AbstractModel):
    """DescribeDisasterRecoverGroupQuota response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDisasterRecoverGroupsRequest(AbstractModel):
    """DescribeDisasterRecoverGroups request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDisasterRecoverGroupsResponse(AbstractModel):
    """DescribeDisasterRecoverGroups response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeHostsRequest(AbstractModel):
    """DescribeHosts request structure.

    """

    def __init__(self):
        """
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">Filter results by **<strong>availability zones</strong>**. For example, availability zone: ap-guangzhou-1;</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">list of availability zones</a></p>
<li><strong>project-id</strong></li>
<p style="padding-left: 30px;">Filter results by **<strong>project ID</strong>**. You can query the existing project list through the [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) API or [CVM console](https://console.cloud.tencent.com/cvm/index), or create a project by calling the [AddProject](https://intl.cloud.tencent.com/document/api/378/4398?from_cn_redirect=1) API. For example, project ID: 1002189;</p><p style="padding-left: 30px;">Type: Integer</p><p style="padding-left: 30px;">Required: no</p>
<li><strong>host-id</strong></li>
<p style="padding-left: 30px;">Filter results by **<strong>[CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) ID</strong>**. For example, [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) ID: host-xxxxxxxx;</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p>
<li><strong>state</strong></li>
<p style="padding-left: 30px;">Filter results by **<strong>CDH instance name</strong>**. </p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p>
<li><strong>state</strong></li>
<p style="padding-left: 30px;">Filter results by **<strong>CDH instance status </strong>**. (PENDING: creating | LAUNCH_FAILURE: creation failed | RUNNING: running | EXPIRED: expired)</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p>
Each request can have up to 10 `Filters` and 5 `Filters.Values`.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeHostsResponse(AbstractModel):
    """DescribeHosts response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageQuotaRequest(AbstractModel):
    """DescribeImageQuota request structure.

    """


class DescribeImageQuotaResponse(AbstractModel):
    """DescribeImageQuota response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageSharePermissionRequest(AbstractModel):
    """DescribeImageSharePermission request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageSharePermissionResponse(AbstractModel):
    """DescribeImageSharePermission response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImagesRequest(AbstractModel):
    """DescribeImages request structure.

    """

    def __init__(self):
        """
        :param ImageIds: List of image IDs, such as `img-gvbnzy6f`. For the format of array-type parameters, see [API Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>View the image IDs in the [Image Console](https://console.cloud.tencent.com/cvm/image).
        :type ImageIds: list of str
        :param Filters: Filters. Each request can have up to 10 `Filters` and 5 `Filters.Values`. You cannot specify `ImageIds` and `Filters` at the same time. Specific filters:
<li>`image-id` - String - Optional - Filter results by image ID</li>
<li>`image-type` - String - Optional - Filter results by image type. Valid values:
    PRIVATE_IMAGE: private image created by the current account 
    PUBLIC_IMAGE: public image created by Tencent Cloud
   SHARED_IMAGE: image shared with the current account by another account.</li>
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImagesResponse(AbstractModel):
    """DescribeImages response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs request structure.

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstanceFamilyConfigsRequest(AbstractModel):
    """DescribeInstanceFamilyConfigs request structure.

    """


class DescribeInstanceFamilyConfigsResponse(AbstractModel):
    """DescribeInstanceFamilyConfigs response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstanceTypeConfigsRequest(AbstractModel):
    """DescribeInstanceTypeConfigs request structure.

    """

    def __init__(self):
        """
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">Filter results by **<strong>availability zones</strong>**. For example, availability zone: ap-guangzhou-1.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">list of availability zones</a></p>
<li><strong>instance-family</strong></li>
<p style="padding-left: 30px;">Filter results by **<strong>instance models</strong>**. For example, instance models: S1, I1 and M1.</p><p style="padding-left: 30px;">Type: Integer</p><p style="padding-left: 30px;">Required: no</p>
Each request can have up to 10 `Filters` and 1 `Filters.Values`.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstanceTypeConfigsResponse(AbstractModel):
    """DescribeInstanceTypeConfigs response structure.

    """

    def __init__(self):
        """
        :param InstanceTypeConfigSet: List of instance model families
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl response structure.

    """

    def __init__(self):
        """
        :param InstanceVncUrl: Instance VNC URL.
        :type InstanceVncUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceVncUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceVncUrl = params.get("InstanceVncUrl")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesOperationLimitRequest(AbstractModel):
    """DescribeInstancesOperationLimit request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesOperationLimitResponse(AbstractModel):
    """DescribeInstancesOperationLimit response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Query by instance ID(s). For example, instance ID: `ins-xxxxxxxx`. For the specific format, refer to section `Ids.N` of the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You can query up to 100 instances in each request. However, `InstanceIds` and `Filters` cannot be specified at the same time.
        :type InstanceIds: list of str
        :param Filters: Filters.
<li> `zone` - String - Optional - Filter results by availability zone.</li>
<li> `project-id` - Integer - Optional - Filter results by project ID. You can call [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) or log in to the [console](https://console.cloud.tencent.com/cvm/index) to view the list of existing projects. You can also create a new project by calling [AddProject](https://intl.cloud.tencent.com/document/api/378/4398?from_cn_redirect=1).</li>
<li> `host-id` - String - Optional - Filter results by [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) ID. [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) ID format: `host-xxxxxxxx`.</li>
</li>`vpc-id` - String - Optional - Filter results by VPC ID. VPC ID format: `vpc-xxxxxxxx`.</li>
<li> `subnet-id` - String - Optional - Filter results by subnet ID. Subnet ID format: `subnet-xxxxxxxx`.</li>
</li>`instance-id` - String - Optional - Filter results by instance ID. Instance ID format: `ins-xxxxxxxx`.</li>
</li>`security-group-id` - String - Optional - Filter results by security group ID. Security group ID format: `sg-8jlk3f3r`.</li>
</li>`instance-name` - String - Optional - Filter results by instance name.</li>
</li>`instance-charge-type` - String - Optional - Filter results by instance billing method. `POSTPAID_BY_HOUR`: pay-as-you-go | `CDHPAID`: you are only billed for [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances, not the CVMs running on the [CDH](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) instances.</li>
</li>`private-ip-address` - String - Optional - Filter results by the private IP address of the instance's primary ENI.</li>
</li>`public-ip-address` - String - Optional - Filter results by the public IP address of the instance's primary ENI, including the IP addresses automatically assigned during the instance creation and the EIPs manually associated after the instance creation.</li>
<li> `tag-key` - String - Optional - Filter results by tag key.</li>
</li>`tag-value` - String - Optional - Filter results by tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter results by tag key-value pair. Replace `tag-key` with specific tag keys, as shown in example 2.</li>
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesStatusRequest(AbstractModel):
    """DescribeInstancesStatus request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInstancesStatusResponse(AbstractModel):
    """DescribeInstancesStatus response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeInternetChargeTypeConfigsRequest(AbstractModel):
    """DescribeInternetChargeTypeConfigs request structure.

    """


class DescribeInternetChargeTypeConfigsResponse(AbstractModel):
    """DescribeInternetChargeTypeConfigs response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs request structure.

    """

    def __init__(self):
        """
        :param KeyIds: Key pair ID(s) in the format of `skey-11112222`. This API supports using multiple IDs as filters at the same time. For more information on the format of this parameter, see the `id.N` section in [API Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1). You cannot specify `KeyIds` and `Filters` at the same time. You can log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the key pair IDs.
        :type KeyIds: list of str
        :param Filters: Filters.
<li> `project-id` - Integer - Optional - Filter results by project ID. To view the list of project IDs, you can go to [Project Management](https://console.cloud.tencent.com/project), or call [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) and look for `projectId` in the response. </li>
<li> `key-name` - String - Optional - Filter results by key pair name. </li> You cannot specify `KeyIds` and `Filters` at the same time.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeKeyPairsResponse(AbstractModel):
    """DescribeKeyPairs response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReservedInstancesConfigInfosRequest(AbstractModel):
    """DescribeReservedInstancesConfigInfos request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReservedInstancesConfigInfosResponse(AbstractModel):
    """DescribeReservedInstancesConfigInfos response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReservedInstancesOfferingsRequest(AbstractModel):
    """DescribeReservedInstancesOfferings request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReservedInstancesOfferingsResponse(AbstractModel):
    """DescribeReservedInstancesOfferings response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReservedInstancesRequest(AbstractModel):
    """DescribeReservedInstances request structure.

    """

    def __init__(self):
        """
        :param DryRun: Dry run. The default is false.
        :type DryRun: bool
        :param Offset: Offset. The default value is 0. For more information on `Offset`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param Limit: Number of returned results. The default value is 20. The maximum is 100. For more information on `Limit`, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param Filters: <li><strong>zone</strong></li>
<p style="padding-left: 30px;">Filters by <strong>availability zone</strong> in which reserved instances can be purchased, such as `ap-guangzhou-1`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">Availability Zones</a></p>
<li><strong>duration</strong></li>
<p style="padding-left: 30px;">Filters by <strong>validity period</strong> of the reserved instance, such as `31536000`.</p><p style="padding-left: 30px;">Type: Integer</p><p style="padding-left: 30px;">Unit: second</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid value: 31536000 (1 year)</p>
<li><strong>instance-type</strong></li>
<p style="padding-left: 30px;">Filters by <strong>specification of the reserved instance</strong>, such as `S3.MEDIUM4`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1">Reserved Instance Types</a></p>
<li><strong>instance-family</strong></li>
<p style="padding-left: 30px;">Filters by <strong>type of the reserved instance</strong>, such as `S3`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1">Reserved Instance Types</a></p>
<li><strong>offering-type</strong></li>
<li><strong>offering-type</strong></li>
<p style="padding-left: 30px;">Filters by <strong>payment method</strong>, such as `All Upfront`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: All Upfront | Partial Upfront | No Upfront</p>
<li><strong>product-description</strong></li>
<p style="padding-left: 30px;">Filters by <strong>platform description</strong> (operating system) of the reserved instance, such as `linux`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid value: linux</p>
<li><strong>reserved-instances-id</strong></li>
<p style="padding-left: 30px;">Filters by <strong>reserved instance ID</strong> in the form of 650c138f-ae7e-4750-952a-96841d6e9fc1.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p>
<li><strong>state</strong></li>
<p style="padding-left: 30px;">Filters by <strong>reserved instance status</strong>, such as `active`.</p><p style="padding-left: 30px;">Type: String</p><p style="padding-left: 30px;">Required: no</p><p style="padding-left: 30px;">Valid values: active (created) | pending (waiting to be created) | retired (expired)</p>
Each request can have up to 10 `Filters` and 5 `Filter.Values`.
        :type Filters: list of Filter
        """
        self.DryRun = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.DryRun = params.get("DryRun")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReservedInstancesResponse(AbstractModel):
    """DescribeReservedInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: The number of eligible reserved instances.
        :type TotalCount: int
        :param ReservedInstancesSet: List of eligible reserved instances.
        :type ReservedInstancesSet: list of ReservedInstances
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ReservedInstancesSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ReservedInstancesSet") is not None:
            self.ReservedInstancesSet = []
            for item in params.get("ReservedInstancesSet"):
                obj = ReservedInstances()
                obj._deserialize(item)
                self.ReservedInstancesSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeZoneInstanceConfigInfos request structure.

    """

    def __init__(self):
        """
        :param Filters: Filters.

<li> `zone` - String - Optional - Filter results by availability zone.</li>

<li>`instance-family` - String - Optional - Filter results by instance model family, such as `S1`, `I1`, and `M1`.</li>

<li>`instance-type` - String - Optional - Filter results by model. Different instance models have different configurations. You can call `DescribeInstanceTypeConfigs` to query the latest configuration list or refer to the documentation on instance types. If this parameter is not specified, `S1.SMALL1` will be used by default.</li>

<li>`instance-charge-type` - String - Optional - Filter results by instance billing method. `POSTPAID_BY_HOUR`: pay-as-you-go | `CDHPAID`: you are only billed for CDH instances, not the CVMs running on the CDH instances.</li>
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeZoneInstanceConfigInfos response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeZonesRequest(AbstractModel):
    """DescribeZones request structure.

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisasterRecoverGroup(AbstractModel):
    """Information on disaster recovery groups

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnhancedService(AbstractModel):
    """Describes the configuration of enhanced services, such as Cloud Security and Cloud Monitor.

    """

    def __init__(self):
        """
        :param SecurityService: Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.cvm.v20170312.models.RunSecurityServiceEnabled`
        :param MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.cvm.v20170312.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Externals(AbstractModel):
    """Additional data

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HostItem(AbstractModel):
    """Details about a CDH instance

    """

    def __init__(self):
        """
        :param Placement: Location of the CDH instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param HostId: CDH instance ID
        :type HostId: str
        :param HostType: CDH instance type
        :type HostType: str
        :param HostName: CDH instance name
        :type HostName: str
        :param HostChargeType: Billing method of the CDH instance
        :type HostChargeType: str
        :param RenewFlag: Auto renewal flag of the CDH instance
        :type RenewFlag: str
        :param CreatedTime: Creation time of the CDH instance
        :type CreatedTime: str
        :param ExpiredTime: Expiration time of the CDH instance
        :type ExpiredTime: str
        :param InstanceIds: List of IDs of CVM instances created on the CDH
        :type InstanceIds: list of str
        :param HostState: CDH instance state
        :type HostState: str
        :param HostIp: CDH instance IP
        :type HostIp: str
        :param HostResource: Resource information of the CDH instance
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HostResource(AbstractModel):
    """Resource information of a CDH instance

    """

    def __init__(self):
        """
        :param CpuTotal: Total number of CPU cores in the CDH instance
        :type CpuTotal: int
        :param CpuAvailable: Number of available CPU cores in the CDH instance
        :type CpuAvailable: int
        :param MemTotal: Total memory of the CDH instance; unit: GiB
        :type MemTotal: float
        :param MemAvailable: Available memory of the CDH instance; unit: GiB
        :type MemAvailable: float
        :param DiskTotal: Total disk size of the CDH instance; unit: GiB
        :type DiskTotal: int
        :param DiskAvailable: Avilable disk size of the CDH instance; unit: GiB
        :type DiskAvailable: int
        :param DiskType: CDH instance disk type.
        :type DiskType: str
        """
        self.CpuTotal = None
        self.CpuAvailable = None
        self.MemTotal = None
        self.MemAvailable = None
        self.DiskTotal = None
        self.DiskAvailable = None
        self.DiskType = None


    def _deserialize(self, params):
        self.CpuTotal = params.get("CpuTotal")
        self.CpuAvailable = params.get("CpuAvailable")
        self.MemTotal = params.get("MemTotal")
        self.MemAvailable = params.get("MemAvailable")
        self.DiskTotal = params.get("DiskTotal")
        self.DiskAvailable = params.get("DiskAvailable")
        self.DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Image(AbstractModel):
    """Details about an image, including its state and attributes.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImageOsList(AbstractModel):
    """Supported operating systems are divided into two categories, Windows and Linux.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportImageRequest(AbstractModel):
    """ImportImage request structure.

    """

    def __init__(self):
        """
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
        """
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.ImageUrl = None
        self.ImageName = None
        self.ImageDescription = None
        self.DryRun = None
        self.Force = None


    def _deserialize(self, params):
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        self.DryRun = params.get("DryRun")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportImageResponse(AbstractModel):
    """ImportImage response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair request structure.

    """

    def __init__(self):
        """
        :param KeyName: Key pair name, which can contain numbers, letters, and underscores, with a maximum length of 25 characters.
        :type KeyName: str
        :param ProjectId: The ID of the [project](https://intl.cloud.tencent.com/document/product/378/10861?from_cn_redirect=1) to which the created key pair belongs.<br><br>You can retrieve the project ID in two ways:<br><li>Query the project ID in [Project Management](https://console.cloud.tencent.com/project).<br><li>Call [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) and search for `projectId` in the response.

If you want to use the default project, specify 0 for the parameter.
        :type ProjectId: int
        :param PublicKey: Content of the public key in the key pair in the `OpenSSH RSA` format.
        :type PublicKey: str
        """
        self.KeyName = None
        self.ProjectId = None
        self.PublicKey = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.PublicKey = params.get("PublicKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImportKeyPairResponse(AbstractModel):
    """ImportKeyPair response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquirePricePurchaseReservedInstancesOfferingRequest(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquirePricePurchaseReservedInstancesOfferingResponse(AbstractModel):
    """InquirePricePurchaseReservedInstancesOffering response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResetInstanceRequest(AbstractModel):
    """InquiryPriceResetInstance request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResetInstanceResponse(AbstractModel):
    """InquiryPriceResetInstance response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResetInstancesTypeRequest(AbstractModel):
    """InquiryPriceResetInstancesType request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResetInstancesTypeResponse(AbstractModel):
    """InquiryPriceResetInstancesType response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResizeInstanceDisksRequest(AbstractModel):
    """InquiryPriceResizeInstanceDisks request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceResizeInstanceDisksResponse(AbstractModel):
    """InquiryPriceResizeInstanceDisks response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceRunInstancesRequest(AbstractModel):
    """InquiryPriceRunInstances request structure.

    """

    def __init__(self):
        """
        :param Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone and project.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param ImageId: [Image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images: <br/><li>Public images </li><li>Custom images </li><li>Shared images </li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways: <br/><li>For IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information; for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
        :type ImageId: str
        :param InstanceChargeType: The instance [billing method](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1).<br><li>POSTPAID_BY_HOUR: hourly, pay-as-you-go<br>Default value: POSTPAID_BY_HOUR.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Configuration of prepaid instances. You can use the parameter to specify the attributes of prepaid instances, such as the subscription period and the auto-renewal plan. This parameter is required for prepaid instances.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param InstanceType: The instance model. Different resource specifications are specified for different models. For specific values, call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) to retrieve the latest specification list or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If the parameter is not specified, `S1.SMALL1` will be used by default.
        :type InstanceType: str
        :param SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: The configuration information of the instance data disk. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC data disk or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC data disks, CLOUD_PREMIUM data disks, or CLOUD_SSD data disks.
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: VPC configurations. You can use this parameter to specify the VPC ID, subnet ID, etc. If this parameter is not specified, the basic network will be used by default. If a VPC IP is specified in this parameter, the `InstanceCount` parameter can only be 1. 
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: Number of instances to be purchased. Value range: [1, 100]; default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on quota, see [CVM instance purchase limit](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param InstanceName: Instance name to be displayed.<br><li>If this parameter is not specified, "Unnamed" will be displayed by default.</li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`.</li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and name them as `server_`, the instance names will be displayed as `server_1` and `server_2`.</li><li>The instance name contains up to 60 characters (including pattern strings).
        :type InstanceName: str
        :param LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will not be associated with any security group by default.
        :type SecurityGroupIds: list of str
        :param EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Monitor and Cloud Security. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. <br>For more information, see 'How to ensure idempotency'.
        :type ClientToken: str
        :param HostName: Host name of the CVM. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>For Windows instances, the host name must be 2-15 characters long and can contain uppercase and lowercase letters, numbers, and hyphens (-). It cannot contain periods (.) or contain only numbers. <br><li>For other instances, such as Linux instances, the host name must be 2-30 characters long. It supports multiple periods (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two periods (.).
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InquiryPriceRunInstancesResponse(AbstractModel):
    """InquiryPriceRunInstances response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Instance(AbstractModel):
    """Describes information on an instance

    """

    def __init__(self):
        """
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
        :param DataDisks: Information on the data disks of the instance, which only covers the data disks purchased together with the instance. 
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceChargePrepaid(AbstractModel):
    """Describes the billing method of an instance.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceFamilyConfig(AbstractModel):
    """Describes the model family of the instance.
    Examples: {'InstanceFamilyName': 'Standard S1', 'InstanceFamily': 'S1'}, {'InstanceFamilyName': 'Network-optimized N1', 'InstanceFamily': 'N1'}, {'InstanceFamilyName': 'High IO I1', 'InstanceFamily': 'I1'}, etc.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceMarketOptionsRequest(AbstractModel):
    """Options related to bidding requests

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceStatus(AbstractModel):
    """Describes instance states. For state types, see [here](https://intl.cloud.tencent.com/document/api/213/15753?from_cn_redirect=1#InstanceStatus).

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceTypeConfig(AbstractModel):
    """Describes the configurations of an instance model.

    """

    def __init__(self):
        """
        :param Zone: Availability zone.
        :type Zone: str
        :param InstanceType: Instance model.
        :type InstanceType: str
        :param InstanceFamily: Instance model family.
        :type InstanceFamily: str
        :param GPU: Number of GPU cores.
        :type GPU: int
        :param CPU: Number of CPU cores.
        :type CPU: int
        :param Memory: Memory capacity; unit: `GB`.
        :type Memory: int
        :param FPGA: Number of FPGA cores; unit: core.
        :type FPGA: int
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceFamily = None
        self.GPU = None
        self.CPU = None
        self.Memory = None
        self.FPGA = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceFamily = params.get("InstanceFamily")
        self.GPU = params.get("GPU")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.FPGA = params.get("FPGA")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceTypeQuotaItem(AbstractModel):
    """Describes instance model quota.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InternetAccessible(AbstractModel):
    """Describes the accessibility of an instance in the public network, including its network billing method, maximum bandwidth, etc.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InternetChargeTypeConfig(AbstractModel):
    """Describes network billing.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ItemPrice(AbstractModel):
    """Describes pricing information.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class KeyPair(AbstractModel):
    """Describes key pair information.

    """

    def __init__(self):
        """
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
        """
        self.KeyId = None
        self.KeyName = None
        self.ProjectId = None
        self.Description = None
        self.PublicKey = None
        self.PrivateKey = None
        self.AssociatedInstanceIds = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.Description = params.get("Description")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LocalDiskType(AbstractModel):
    """Describes local disk specifications.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        """
        :param Password: Login password of the instance. The password requirements vary among different operating systems: <br><li>For Linux instances, the password must be 8-30 characters long and contain at least two of the following types: [a-z], [A-Z], [0-9] and [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]. <br><li>For Windows instances, the password must be 12-30 characters long and contain at least three of the following categories: [a-z], [A-Z], [0-9] and [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]. <br><br>If this parameter is not specified, a random password will be generated and sent to you via the Message Center.
Note: this field may return null, indicating that no valid value is obtained.
        :type Password: str
        :param KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call [`DescribeKeyPairs`](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) to obtain `KeyId`. A key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
Note: this field may return null, indicating that no valid value is obtained.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDisasterRecoverGroupAttributeRequest(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyDisasterRecoverGroupAttributeResponse(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyHostsAttributeRequest(AbstractModel):
    """ModifyHostsAttribute request structure.

    """

    def __init__(self):
        """
        :param HostIds: CDH instance ID(s).
        :type HostIds: list of str
        :param HostName: CDH instance name to be displayed. You can specify any name you like, but its length cannot exceed 60 characters.
        :type HostName: str
        :param RenewFlag: Auto renewal flag. Valid values: <br><li>NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically <br><li>NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically <br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify upon expiration nor renew automatically <br><br>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis if the account balance is sufficient.
        :type RenewFlag: str
        :param ProjectId: Project ID. You can create a project by using the [AddProject](https://intl.cloud.tencent.com/doc/api/403/4398?from_cn_redirect=1) API and obtain its ID from the response parameter `projectId` of the [`DescribeProject`](https://intl.cloud.tencent.com/document/product/378/4400?from_cn_redirect=1) API. Subsequently, the project ID can be used to filter results when you query instances by calling the [DescribeHosts](https://intl.cloud.tencent.com/document/api/213/16474?from_cn_redirect=1) API.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyHostsAttributeResponse(AbstractModel):
    """ModifyHostsAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyImageSharePermissionRequest(AbstractModel):
    """ModifyImageSharePermission request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyImageSharePermissionResponse(AbstractModel):
    """ModifyImageSharePermission response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param InstanceName: Instance name. You can specify any name you like, but its length cannot exceed 60 characters.
        :type InstanceName: str
        :param SecurityGroups: ID list of security groups of the instance. The instance will be associated with the specified security groups and will be disassociated from the original security groups.
        :type SecurityGroups: list of str
        """
        self.InstanceIds = None
        self.InstanceName = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyInstancesProjectRequest(AbstractModel):
    """ModifyInstancesProject request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance IDs. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. You can operate up to 100 instances in each request.
        :type InstanceIds: list of str
        :param ProjectId: Project ID. You can create a project by using the [AddProject](https://intl.cloud.tencent.com/doc/api/403/4398?from_cn_redirect=1) API and obtain its ID from the response parameter `projectId` of the [`DescribeProject`](https://intl.cloud.tencent.com/document/product/378/4400?from_cn_redirect=1) API. Subsequently, the project ID can be used to filter results when you query instances by calling the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyInstancesProjectResponse(AbstractModel):
    """ModifyInstancesProject response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyInstancesVpcAttributeRequest(AbstractModel):
    """ModifyInstancesVpcAttribute request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyInstancesVpcAttributeResponse(AbstractModel):
    """ModifyInstancesVpcAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyKeyPairAttributeRequest(AbstractModel):
    """ModifyKeyPairAttribute request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyKeyPairAttributeResponse(AbstractModel):
    """ModifyKeyPairAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OperationCountLimit(AbstractModel):
    """Describes the maximum number of times you can perform an operation on a single instance.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OsVersion(AbstractModel):
    """Supported operating system types.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Placement(AbstractModel):
    """Describes the location of an instance, including its availability zone, project, host (for CDH products only), primary host IP, etc.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Price(AbstractModel):
    """Price.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurchaseReservedInstancesOfferingRequest(AbstractModel):
    """PurchaseReservedInstancesOffering request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurchaseReservedInstancesOfferingResponse(AbstractModel):
    """PurchaseReservedInstancesOffering response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RebootInstancesRequest(AbstractModel):
    """RebootInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance IDs. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. You can operate up to 100 instances in each request.
        :type InstanceIds: list of str
        :param ForceReboot: Whether to force restart an instance after a normal restart fails. Valid values: <br><li>TRUE: force restart an instance after a normal restart fails <br><li>FALSE: do not force restart an instance after a normal restart fails <br><br>Default value: FALSE.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegionInfo(AbstractModel):
    """Region information.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReservedInstanceConfigInfoItem(AbstractModel):
    """Static configurations of the reserved instance. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReservedInstanceFamilyItem(AbstractModel):
    """RI-related instance family. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReservedInstancePrice(AbstractModel):
    """Price of the reserved instance. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReservedInstancePriceItem(AbstractModel):
    """Price information of the reserved instance based on the payment method. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReservedInstanceTypeItem(AbstractModel):
    """Reserved instance specification. Currently, RIs are only offered to beta users.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReservedInstances(AbstractModel):
    """Describes the information of the reserved instances the user has purchased

    """

    def __init__(self):
        """
        :param ReservedInstancesId: The ID of the purchased reserved instance, taking the form 650c138f-ae7e-4750-952a-96841d6e9fc1.
        :type ReservedInstancesId: str
        :param InstanceType: Reserved instance specification, such as `S3.MEDIUM4`.
Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1">Reserved Instance Specifications</a>
        :type InstanceType: str
        :param Zone: Availability zones in which the reserved instance can be purchased. For example, "ap-guangzhou-1".
Returned values: <a href="https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1">list of availability zones</a>
        :type Zone: str
        :param StartTime: Start time of the reserved instance billing, taking the form of 2019-10-23 00:00:00.
        :type StartTime: str
        :param EndTime: End time of the reserved instance, taking the form of 2019-10-23 00:00:00
        :type EndTime: str
        :param Duration: The **validity** of the reserved instance in seconds, which is the purchased usage period. For example, 31536000.
Measurement unit: second.
        :type Duration: int
        :param InstanceCount: The number of reserved instances that have been purchased. For example, 10.
        :type InstanceCount: int
        :param ProductDescription: The operating system of the reserved instance. For example, "linux".
Returned value: linux.
        :type ProductDescription: str
        :param State: The status of the reserved instance. For example, "active".
Returned value: "active" (created) | "pending" (waiting to be created) | "retired" (expired).
        :type State: str
        :param CurrencyCode: The currency in which the reserved instance is billed. The ISO 4217 standard currency codes are used. For example, USD.
Returned value: USD.
        :type CurrencyCode: str
        :param OfferingType: The payment method of the reserved instance. For example, "All Upfront".
Returned value: All Upfront.
        :type OfferingType: str
        :param InstanceFamily: Reserved instance type, such as `S3`.
Valid values: please see <a href="https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1">Reserved Instance Types</a>
        :type InstanceFamily: str
        """
        self.ReservedInstancesId = None
        self.InstanceType = None
        self.Zone = None
        self.StartTime = None
        self.EndTime = None
        self.Duration = None
        self.InstanceCount = None
        self.ProductDescription = None
        self.State = None
        self.CurrencyCode = None
        self.OfferingType = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.ReservedInstancesId = params.get("ReservedInstancesId")
        self.InstanceType = params.get("InstanceType")
        self.Zone = params.get("Zone")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Duration = params.get("Duration")
        self.InstanceCount = params.get("InstanceCount")
        self.ProductDescription = params.get("ProductDescription")
        self.State = params.get("State")
        self.CurrencyCode = params.get("CurrencyCode")
        self.OfferingType = params.get("OfferingType")
        self.InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReservedInstancesOffering(AbstractModel):
    """The information of the Reserved Instance offering.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstanceRequest(AbstractModel):
    """ResetInstance request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param ImageId: Specified effective [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><li>Marketplace images </li><br/>You can obtain the available image IDs in the following ways:<br/><li>for IDs of `public images`, `custom images`, and `shared images`, log in to the [CVM console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE); for IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list).</li><li>Call the API [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response.</li>
<br>Default value: current image.
        :type ImageId: str
        :param SystemDisk: System disk configurations in the instance. For instances with a cloud disk as the system disk, you can expand the capacity of the system disk to the specified value after re-installation by using this parameter. If the parameter is not specified, lower system disk capacity will be automatically expanded to the image size, and extra disk costs are generated. You can only expand but cannot reduce the system disk capacity. By re-installing the system, you only modify the system disk capacity, but not the type.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstanceResponse(AbstractModel):
    """ResetInstance response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """ResetInstancesInternetMaxBandwidth request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """ResetInstancesInternetMaxBandwidth response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param Password: Login password of the instance. The rule of password complexity varies with operating systems:
For a Linux instance, the password must be 8 to 30 characters in length; password with more than 12 characters is recommended. It cannot begin with "/", and must contain at least three types of the following:<br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\`~!@#$%^&\*-+=\_|{}[]:;'<>,.?/
For a Windows CVM, the password must be 12 to 30 characters in length. It cannot begin with "/" or contain your username. It must contain at least three types of the following:<br><li>Lowercase letters: [a-z]<br><li>Uppercase letters: [A-Z]<br><li>Numbers: 0-9<br><li>Special characters: ()\`~!@#$%^&\*-+=\_|{}[]:;' <>,.?/<li>If the specified instances include both `Linux` and `Windows` instances, you need to follow the password requirements for `Windows` instances.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstancesTypeRequest(AbstractModel):
    """ResetInstancesType request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResetInstancesTypeResponse(AbstractModel):
    """ResetInstancesType response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResizeInstanceDisksRequest(AbstractModel):
    """ResizeInstanceDisks request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID. To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response.
        :type InstanceId: str
        :param DataDisks: Configuration of data disks to be expanded. Currently you can only use the API to expand non-elastic data disks whose [disk type](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#block_device) is `CLOUD_BASIC`, `CLOUD_PREMIUM`, or `CLOUD_SSD`. You can use [`DescribeDisks`](https://intl.cloud.tencent.com/document/api/362/16315?from_cn_redirect=1) to check whether a disk is elastic. If the `Portable` field in the response is `false`, it means that the disk is not elastic. Data disk capacity unit: GB; minimum increment: 10 GB. For more information on selecting the data disk type, see the [product overview on cloud disks](https://intl.cloud.tencent.com/document/product/362/2353?from_cn_redirect=1). Available data disk types are subject to the instance type (`InstanceType`). In addition, the maximum capacity allowed for expansion varies by data disk type.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResizeInstanceDisksResponse(AbstractModel):
    """ResizeInstanceDisks response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunInstancesRequest(AbstractModel):
    """RunInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceChargeType: The instance [billing method](https://intl.cloud.tencent.com/document/product/213/2180?from_cn_redirect=1). Valid values: <br><li>`POSTPAID_BY_HOUR`: hourly, pay-as-you-go<br><li>`CDHPAID`: you are only billed for CDH instances, not the CVMs running on the CDH instances.<br>Default value: POSTPAID_BY_HOUR.
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: Configuration of prepaid instances. You can use the parameter to specify the attributes of prepaid instances, such as the subscription period and the auto-renewal plan. This parameter is required for prepaid instances.
        :type InstanceChargePrepaid: :class:`tencentcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param Placement: Location of the instance. You can use this parameter to specify the attributes of the instance, such as its availability zone, project, and CDH. You can specify a CDH for a CVM by creating the CVM on the CDH.
        :type Placement: :class:`tencentcloud.cvm.v20170312.models.Placement`
        :param InstanceType: The instance model. Different resource specifications are specified for different instance models.
<br><li>To view specific values for `POSTPAID_BY_HOUR` instances, you can call [DescribeInstanceTypeConfigs](https://intl.cloud.tencent.com/document/api/213/15749?from_cn_redirect=1) or refer to [Instance Types](https://intl.cloud.tencent.com/document/product/213/11518?from_cn_redirect=1). If this parameter is not specified, `S1.SMALL1` will be used by default.<br><li>For `CDHPAID` instances, the value of this parameter is in the format of `CDH_XCXG` based on the number of CPU cores and memory capacity. For example, if you want to create a CDH instance with a single-core CPU and 1 GB memory, specify this parameter as `CDH_1C1G`.
        :type InstanceType: str
        :param ImageId: The [image](https://intl.cloud.tencent.com/document/product/213/4940?from_cn_redirect=1) ID in the format of `img-xxx`. There are four types of images:<br/><li>Public images</li><li>Custom images</li><li>Shared images</li><li>Marketplace images</li><br/>You can retrieve available image IDs in the following ways:<br/><li>For the IDs of `public images`, `custom images`, and `shared images`, log in to the [console](https://console.cloud.tencent.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE) to query the information. For the IDs of `marketplace images`, go to [Cloud Marketplace](https://market.cloud.tencent.com/list). </li><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1), pass in `InstanceType` to retrieve the list of images supported by the current model, and then find the `ImageId` in the response.</li>
        :type ImageId: str
        :param SystemDisk: System disk configuration of the instance. If this parameter is not specified, the default value will be used.
        :type SystemDisk: :class:`tencentcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: The configuration information of instance data disks. If this parameter is not specified, no data disk will be purchased by default. When purchasing, you can specify 21 data disks, which can contain at most 1 LOCAL_BASIC data disk or LOCAL_SSD data disk, and at most 20 CLOUD_BASIC data disks, CLOUD_PREMIUM data disks, or CLOUD_SSD data disks.
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: Configuration information of VPC. This parameter is used to specify VPC ID and subnet ID, etc. If this parameter is not specified, the classic network is used by default. If a VPC IP is specified in this parameter, it indicates the primary ENI IP of each instance. The value of parameter InstanceCount must be same as the number of VPC IPs, which cannot be greater than 20.
        :type VirtualPrivateCloud: :class:`tencentcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: Configuration of public network bandwidth. If this parameter is not specified, 0 Mbps will be used by default.
        :type InternetAccessible: :class:`tencentcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: The number of instances to be purchased. Value range: [1, 100]; default value: 1. The specified number of instances to be purchased cannot exceed the remaining quota allowed for the user. For more information on the quota, see [CVM instance purchase limit](https://intl.cloud.tencent.com/document/product/213/2664).
        :type InstanceCount: int
        :param InstanceName: Instance name to be displayed.<br><li>If this parameter is not specified, "Unnamed" will be displayed by default.</li><li>If you purchase multiple instances at the same time and specify a pattern string `{R:x}`, numbers `[x, x+n-1]` will be generated, where `n` represents the number of instances purchased. For example, you specify a pattern string, `server_{R:3}`. If you only purchase 1 instance, the instance will be named `server_3`; if you purchase 2, they will be named `server_3` and `server_4`. You can specify multiple pattern strings in the format of `{R:x}`.</li><li>If you purchase multiple instances at the same time and do not specify a pattern string, the instance names will be suffixed by `1, 2...n`, where `n` represents the number of instances purchased. For example, if you purchase 2 instances and name them as `server_`, the instance names will be displayed as `server_1` and `server_2`.</li><li>The instance name contains up to 60 characters (including pattern strings).
        :type InstanceName: str
        :param LoginSettings: Login settings of the instance. You can use this parameter to set the login method, password, and key of the instance or keep the login settings of the original image. By default, a random password will be generated and sent to you via the Message Center.
        :type LoginSettings: :class:`tencentcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: Security groups to which the instance belongs. To obtain the security group IDs, you can call [DescribeSecurityGroups](https://intl.cloud.tencent.com/document/api/215/15808) and look for the `sgld` fields in the response. If this parameter is not specified, the instance will be associated with default security groups.
        :type SecurityGroupIds: list of str
        :param EnhancedService: Specifies whether to enable services such as Anti-DDoS and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Anti-DDoS are enabled for public images by default. However, for custom images and images from the marketplace, Anti-DDoS and Cloud Monitor are not enabled by default. The original services in the image will be retained.
        :type EnhancedService: :class:`tencentcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: A string used to ensure the idempotency of the request, which is generated by the user and must be unique to each request. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed. <br>For more information, see 'How to ensure idempotency'.
        :type ClientToken: str
        :param HostName: Host name of the CVM. <br><li>Periods (.) or hyphens (-) cannot be the start or end of a host name or appear consecutively in a host name.<br><li>For Windows instances, the host name must be 2-15 characters long and can contain uppercase and lowercase letters, numbers, and hyphens (-). It cannot contain periods (.) or contain only numbers. <br><li>For other instances, such as Linux instances, the host name must be 2-60 characters long. It supports multiple periods (.) and allows uppercase and lowercase letters, numbers, and hyphens (-) between any two periods (.).
        :type HostName: str
        :param ActionTimer: Scheduled tasks. You can use this parameter to specify scheduled tasks for the instance. Only scheduled termination is supported.
        :type ActionTimer: :class:`tencentcloud.cvm.v20170312.models.ActionTimer`
        :param DisasterRecoverGroupIds: Placement group ID. You can only specify one.
        :type DisasterRecoverGroupIds: list of str
        :param TagSpecification: The tag description list. This parameter is used to bind a tag to a resource instance. A tag can only be bound to CVM instances.
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: The market options of the instance.
        :type InstanceMarketOptions: :class:`tencentcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param UserData: User data provided to the instance, which needs to be encoded in base64 format with the maximum size of 16KB. For more information on how to get the value of this parameter, see the commands you need to execute on startup for [Windows](https://intl.cloud.tencent.com/document/product/213/17526) or [Linux](https://intl.cloud.tencent.com/document/product/213/17525).
        :type UserData: str
        :param DryRun: Whether the request is a dry run only.
true: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available.
If the dry run fails, the corresponding error code will be returned.
If the dry run succeeds, the RequestId will be returned.
false (default value): send a normal request and create instance(s) if all the requirements are met.
        :type DryRun: bool
        :param CamRoleName: CAM role name, which can be obtained from the `roleName` field in the response of the [`DescribeRoleList`](https://intl.cloud.tencent.com/document/product/598/13887?from_cn_redirect=1) API.
        :type CamRoleName: str
        :param HpcClusterId: HPC cluster ID. The HPC cluster must and can only be specified for a high-performance computing instance.
        :type HpcClusterId: str
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunInstancesResponse(AbstractModel):
    """RunInstances response structure.

    """

    def __init__(self):
        """
        :param InstanceIdSet: If you use this API to create instance(s), this parameter will be returned, representing one or more instance `ID`s. Retuning the instance `ID` list does not necessarily mean that the instance(s) were created successfully. To check whether the instance(s) were created successfully, you can call [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and check the states of the instances in `InstancesSet` in the response. If the state of an instance changes from "pending" to "running", it means that the instance has been created successfully.
        :type InstanceIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunMonitorServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Monitor service.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunSecurityServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Security service.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SharePermission(AbstractModel):
    """Describes image sharing information.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Snapshot(AbstractModel):
    """Describes information on the snapshot associated with an image.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SpotMarketOptions(AbstractModel):
    """Options related to bidding.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartInstancesRequest(AbstractModel):
    """StartInstances request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartInstancesResponse(AbstractModel):
    """StartInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopInstancesRequest(AbstractModel):
    """StopInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceIds: Instance ID(s). To obtain the instance IDs, you can call [`DescribeInstances`](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) and look for `InstanceId` in the response. The maximum number of instances in each request is 100.
        :type InstanceIds: list of str
        :param ForceStop: Whether to force shut down an instance after a normal shutdown fails. Valid values: <br><li>TRUE: force shut down an instance after a normal shutdown fails <br><li>FALSE: do not force shut down an instance after a normal shutdown fails <br><br>Default value: FALSE.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopInstancesResponse(AbstractModel):
    """StopInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StorageBlock(AbstractModel):
    """Information on local HDD storage.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SyncImagesRequest(AbstractModel):
    """SyncImages request structure.

    """

    def __init__(self):
        """
        :param ImageIds: List of image IDs. You can obtain the image IDs in two ways: <br><li>Call [DescribeImages](https://intl.cloud.tencent.com/document/api/213/15715?from_cn_redirect=1) and look for `ImageId` in the response. <br><li>Look for the information in the [Image Console](https://console.cloud.tencent.com/cvm/image). <br>The specified images must meet the following requirements: <br><li>The images must be in the `NORMAL` state. <br><li>The image size must be smaller than 50 GB. <br>For more information on image states, see [here](https://intl.cloud.tencent.com/document/api/213/9452?from_cn_redirect=1#image_state).
        :type ImageIds: list of str
        :param DestinationRegions: List of destination regions for synchronization. A destination region must meet the following requirements: <br><li>It cannot be the source region. <br><li>It must be valid. <br><li>Currently some regions do not support image synchronization. <br>For specific regions, see [Region](https://intl.cloud.tencent.com/document/product/213/6091?from_cn_redirect=1).
        :type DestinationRegions: list of str
        """
        self.ImageIds = None
        self.DestinationRegions = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        self.DestinationRegions = params.get("DestinationRegions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SyncImagesResponse(AbstractModel):
    """SyncImages response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SystemDisk(AbstractModel):
    """Describes information on the block device where the operating system is stored, i.e., the system disk.

    """

    def __init__(self):
        """
        :param DiskType: System disk type. For more information on limits of system disk types, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values:<br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_SSD: SSD<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><br>The disk type currently in stock will be used by default. 
        :type DiskType: str
        :param DiskId: System disk ID. System disks whose type is `LOCAL_BASIC` or `LOCAL_SSD` do not have an ID and do not support this parameter currently.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Tag(AbstractModel):
    """Key-value pair of a tag.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagSpecification(AbstractModel):
    """Description of tags associated with resource instances during instance creation.

    """

    def __init__(self):
        """
        :param ResourceType: The type of resource that bound with the tag. Valid values: `instance` (for CVM) and `host` (for CDH).
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances request structure.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VirtualPrivateCloud(AbstractModel):
    """Describes information on VPC, including subnets, IP addresses, etc.

    """

    def __init__(self):
        """
        :param VpcId: VPC ID in the format of `vpc-xxx`. To obtain valid VPC IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or call the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API and look for the `unVpcId` fields in the response. If you specify `DEFAULT` for both `VpcId` and `SubnetId` when creating an instance, the default VPC will be used.
        :type VpcId: str
        :param SubnetId: VPC subnet ID in the format `subnet-xxx`. To obtain valid subnet IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/subnet?rid=1) or call [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) and look for the `unSubnetId` fields in the response. If you specify `DEFAULT` for both `SubnetId` and `VpcId` when creating an instance, the default VPC will be used.
        :type SubnetId: str
        :param AsVpcGateway: Whether to use an instance as a public gateway. An instance can be used as a public gateway only when it has a public IP and resides in a VPC. Valid values: <br><li>TRUE: use the instance as a public gateway <br><li>FALSE: do not use the instance as a public gateway <br><br>Default value: FALSE.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ZoneInfo(AbstractModel):
    """Information on availability zones.

    """

    def __init__(self):
        """
        :param Zone: Availability zone name, such as `ap-guangzhou-3`.
Check below for the list of all availability zones:
<li> ap-chongqing-1 </li>
<li> ap-seoul-1 </li>
<li> ap-seoul-2 </li>
<li> ap-chengdu-1 </li>
<li> ap-chengdu-2 </li>
<li> ap-hongkong-1 </li>
<li> ap-hongkong-2 </li>
<li> ap-shenzhen-fsi-1 </li>
<li> ap-shenzhen-fsi-2 </li>
<li> ap-shenzhen-fsi-3 </li>
<li> ap-guangzhou-1 (sold out)</li>
<li> ap-guangzhou-2 (sold out)</li>
<li> ap-guangzhou-3 </li>
<li> ap-guangzhou-4 </li>
<li> ap-guangzhou-6 </li>
<li> ap-tokyo-1 </li>
<li> ap-singapore-1 </li>
<li> ap-singapore-2 </li>
<li> ap-shanghai-fsi-1 </li>
<li> ap-shanghai-fsi-2 </li>
<li> ap-shanghai-fsi-3 </li>
<li> ap-bangkok-1 </li>
<li> ap-shanghai-1 (sold out) </li>
<li> ap-shanghai-2 </li>
<li> ap-shanghai-3 </li>
<li> ap-shanghai-4 </li>
<li> ap-shanghai-5 </li>
<li> ap-mumbai-1 </li>
<li> ap-mumbai-2 </li>
<li> eu-moscow-1 </li>
<li> ap-beijing-1 </li>
<li> ap-beijing-2 </li>
<li> ap-beijing-3 </li>
<li> ap-beijing-4 </li>
<li> ap-beijing-5 </li>
<li> ap-beijing-6 </li>
<li> ap-beijing-7 </li>
<li> na-siliconvalley-1 </li>
<li> na-siliconvalley-2 </li>
<li> eu-frankfurt-1 </li>
<li> na-toronto-1 </li>
<li> na-ashburn-1 </li>
<li> na-ashburn-2 </li>
<li> ap-nanjing-1 </li>
<li> ap-nanjing-2 </li>
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        