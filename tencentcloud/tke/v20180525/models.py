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


class AcquireClusterAdminRoleRequest(AbstractModel):
    """AcquireClusterAdminRole request structure.

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
        


class AcquireClusterAdminRoleResponse(AbstractModel):
    """AcquireClusterAdminRole response structure.

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


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: Instance list. Spot instance is not supported.
        :type InstanceIds: list of str
        :param _InstanceAdvancedSettings: Detailed information of the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _EnhancedService: Enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitor and Cloud Security are enabled by default.
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param _LoginSettings: Node login information (currently only supports using Password or single KeyIds)
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param _HostName: When reinstalling the system, you can specify the HostName of the modified instance (when the cluster is in HostName mode, this parameter is required, and the rule name is the same as the [Create CVM Instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API HostName except for uppercase letters not being supported.
        :type HostName: str
        :param _SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the `sgId` field returned by DescribeSecurityGroups. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId)
        :type SecurityGroupIds: list of str
        :param _NodePool: Node pool options
        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePoolOption`
        :param _SkipValidateOptions: Skips the specified verification. Valid values: GlobalRouteCIDRCheck, VpcCniCIDRCheck
        :type SkipValidateOptions: list of str
        :param _InstanceAdvancedSettingsOverrides: This parameter is used to customize the configuration of an instance, which corresponds to the `InstanceIds` one-to-one in sequence. If this parameter is passed in, the default parameter `InstanceAdvancedSettings` will be overwritten and will not take effect. If this parameter is not passed in, the `InstanceAdvancedSettings` will take effect for each instance.

The array length of `InstanceAdvancedSettingsOverride` should be the same as the array length of `InstanceIds`. If its array length is greater than the `InstanceIds` array length, an error will be reported. If its array length is less than the `InstanceIds` array length, the instance without corresponding configuration will use the default configuration.
        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings
        :param _ImageId: Node image
        :type ImageId: str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._InstanceAdvancedSettings = None
        self._EnhancedService = None
        self._LoginSettings = None
        self._HostName = None
        self._SecurityGroupIds = None
        self._NodePool = None
        self._SkipValidateOptions = None
        self._InstanceAdvancedSettingsOverrides = None
        self._ImageId = None

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
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def NodePool(self):
        return self._NodePool

    @NodePool.setter
    def NodePool(self, NodePool):
        self._NodePool = NodePool

    @property
    def SkipValidateOptions(self):
        return self._SkipValidateOptions

    @SkipValidateOptions.setter
    def SkipValidateOptions(self, SkipValidateOptions):
        self._SkipValidateOptions = SkipValidateOptions

    @property
    def InstanceAdvancedSettingsOverrides(self):
        return self._InstanceAdvancedSettingsOverrides

    @InstanceAdvancedSettingsOverrides.setter
    def InstanceAdvancedSettingsOverrides(self, InstanceAdvancedSettingsOverrides):
        self._InstanceAdvancedSettingsOverrides = InstanceAdvancedSettingsOverrides

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._HostName = params.get("HostName")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("NodePool") is not None:
            self._NodePool = NodePoolOption()
            self._NodePool._deserialize(params.get("NodePool"))
        self._SkipValidateOptions = params.get("SkipValidateOptions")
        if params.get("InstanceAdvancedSettingsOverrides") is not None:
            self._InstanceAdvancedSettingsOverrides = []
            for item in params.get("InstanceAdvancedSettingsOverrides"):
                obj = InstanceAdvancedSettings()
                obj._deserialize(item)
                self._InstanceAdvancedSettingsOverrides.append(obj)
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances response structure.

    """

    def __init__(self):
        r"""
        :param _FailedInstanceIds: IDs of failed nodes
Note: This field may return null, indicating that no valid value was found.
        :type FailedInstanceIds: list of str
        :param _SuccInstanceIds: IDs of successful nodes
Note: This field may return null, indicating that no valid value was found.
        :type SuccInstanceIds: list of str
        :param _TimeoutInstanceIds: IDs of (successful or failed) nodes that timed out
Note: This field may return null, indicating that no valid value was found.
        :type TimeoutInstanceIds: list of str
        :param _FailedReasons: Causes of the failure to add a node to a cluster
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FailedReasons: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FailedInstanceIds = None
        self._SuccInstanceIds = None
        self._TimeoutInstanceIds = None
        self._FailedReasons = None
        self._RequestId = None

    @property
    def FailedInstanceIds(self):
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def SuccInstanceIds(self):
        return self._SuccInstanceIds

    @SuccInstanceIds.setter
    def SuccInstanceIds(self, SuccInstanceIds):
        self._SuccInstanceIds = SuccInstanceIds

    @property
    def TimeoutInstanceIds(self):
        return self._TimeoutInstanceIds

    @TimeoutInstanceIds.setter
    def TimeoutInstanceIds(self, TimeoutInstanceIds):
        self._TimeoutInstanceIds = TimeoutInstanceIds

    @property
    def FailedReasons(self):
        return self._FailedReasons

    @FailedReasons.setter
    def FailedReasons(self, FailedReasons):
        self._FailedReasons = FailedReasons

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._SuccInstanceIds = params.get("SuccInstanceIds")
        self._TimeoutInstanceIds = params.get("TimeoutInstanceIds")
        self._FailedReasons = params.get("FailedReasons")
        self._RequestId = params.get("RequestId")


class AddNodeToNodePoolRequest(AbstractModel):
    """AddNodeToNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _InstanceIds: Node ID
        :type InstanceIds: list of str
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._InstanceIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodeToNodePoolResponse(AbstractModel):
    """AddNodeToNodePool response structure.

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


class AddVpcCniSubnetsRequest(AbstractModel):
    """AddVpcCniSubnets request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SubnetIds: The subnets added for the cluster container network
        :type SubnetIds: list of str
        :param _VpcId: ID of the VPC where the cluster resides
        :type VpcId: str
        :param _SkipAddingNonMasqueradeCIDRs: Whether to skip adding the VPC IP range to `NonMasqueradeCIDRs` field of `ip-masq-agent-config`. Default value: `false`
        :type SkipAddingNonMasqueradeCIDRs: bool
        """
        self._ClusterId = None
        self._SubnetIds = None
        self._VpcId = None
        self._SkipAddingNonMasqueradeCIDRs = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SkipAddingNonMasqueradeCIDRs(self):
        return self._SkipAddingNonMasqueradeCIDRs

    @SkipAddingNonMasqueradeCIDRs.setter
    def SkipAddingNonMasqueradeCIDRs(self, SkipAddingNonMasqueradeCIDRs):
        self._SkipAddingNonMasqueradeCIDRs = SkipAddingNonMasqueradeCIDRs


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SubnetIds = params.get("SubnetIds")
        self._VpcId = params.get("VpcId")
        self._SkipAddingNonMasqueradeCIDRs = params.get("SkipAddingNonMasqueradeCIDRs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddVpcCniSubnetsResponse(AbstractModel):
    """AddVpcCniSubnets response structure.

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


class AutoScalingGroupRange(AbstractModel):
    """Maximum and minimum number of pods in cluster-associated scaling groups

    """

    def __init__(self):
        r"""
        :param _MinSize: Minimum number of pods in a scaling group
        :type MinSize: int
        :param _MaxSize: Maximum number of pods in a scaling group
        :type MaxSize: int
        """
        self._MinSize = None
        self._MaxSize = None

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
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoUpgradeClusterLevel(AbstractModel):
    """Auto-upgrades cluster specification

    """

    def __init__(self):
        r"""
        :param _IsAutoUpgrade: Whether to enable Auto Cluster Upgrade
        :type IsAutoUpgrade: bool
        """
        self._IsAutoUpgrade = None

    @property
    def IsAutoUpgrade(self):
        return self._IsAutoUpgrade

    @IsAutoUpgrade.setter
    def IsAutoUpgrade(self, IsAutoUpgrade):
        self._IsAutoUpgrade = IsAutoUpgrade


    def _deserialize(self, params):
        self._IsAutoUpgrade = params.get("IsAutoUpgrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoscalingAdded(AbstractModel):
    """Nodes that are added in scale-out

    """

    def __init__(self):
        r"""
        :param _Joining: Number of nodes that are being added
        :type Joining: int
        :param _Initializing: Number of nodes that are being initialized
        :type Initializing: int
        :param _Normal: Number of normal nodes
        :type Normal: int
        :param _Total: Total number of nodes
        :type Total: int
        """
        self._Joining = None
        self._Initializing = None
        self._Normal = None
        self._Total = None

    @property
    def Joining(self):
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Joining = params.get("Joining")
        self._Initializing = params.get("Initializing")
        self._Normal = params.get("Normal")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupStorageLocation(AbstractModel):
    """Storage repository information

    """

    def __init__(self):
        r"""
        :param _Name: Backup repository name	
        :type Name: str
        :param _StorageRegion: Repository region, such as `ap-guangzhou`	
        :type StorageRegion: str
        :param _Provider: The provider of storage service. It defaults to Tencent Cloud. 	
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type Provider: str
        :param _Bucket: COS bucket name. For COS storage type, it must start with the prefix `tke-backup`. 	
Note: This field may return null, indicating that no valid values can be obtained.
        :type Bucket: str
        :param _Path: COS bucket path 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _State: Storage repository status 
Note: This field may return null, indicating that no valid values can be obtained.
        :type State: str
        :param _Message: Status information 	
Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _LastValidationTime: Last checked time 	
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type LastValidationTime: str
        """
        self._Name = None
        self._StorageRegion = None
        self._Provider = None
        self._Bucket = None
        self._Path = None
        self._State = None
        self._Message = None
        self._LastValidationTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StorageRegion(self):
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def Provider(self):
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def LastValidationTime(self):
        return self._LastValidationTime

    @LastValidationTime.setter
    def LastValidationTime(self, LastValidationTime):
        self._LastValidationTime = LastValidationTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StorageRegion = params.get("StorageRegion")
        self._Provider = params.get("Provider")
        self._Bucket = params.get("Bucket")
        self._Path = params.get("Path")
        self._State = params.get("State")
        self._Message = params.get("Message")
        self._LastValidationTime = params.get("LastValidationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CUDNN(AbstractModel):
    """cuDNN version information

    """

    def __init__(self):
        r"""
        :param _Version: cuDNN version
        :type Version: str
        :param _Name: cuDNN name
        :type Name: str
        :param _DocName: Doc name of cuDNN
        :type DocName: str
        :param _DevName: Dev name of cuDNN
        :type DevName: str
        """
        self._Version = None
        self._Name = None
        self._DocName = None
        self._DevName = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DocName(self):
        return self._DocName

    @DocName.setter
    def DocName(self, DocName):
        self._DocName = DocName

    @property
    def DevName(self):
        return self._DevName

    @DevName.setter
    def DevName(self, DevName):
        self._DevName = DevName


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Name = params.get("Name")
        self._DocName = params.get("DocName")
        self._DevName = params.get("DevName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckEdgeClusterCIDRRequest(AbstractModel):
    """CheckEdgeClusterCIDR request structure.

    """

    def __init__(self):
        r"""
        :param _VpcId: Cluster VPC ID
        :type VpcId: str
        :param _PodCIDR: Cluster Pod CIDR block
        :type PodCIDR: str
        :param _ServiceCIDR: Cluster service CIDR block
        :type ServiceCIDR: str
        """
        self._VpcId = None
        self._PodCIDR = None
        self._ServiceCIDR = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def PodCIDR(self):
        return self._PodCIDR

    @PodCIDR.setter
    def PodCIDR(self, PodCIDR):
        self._PodCIDR = PodCIDR

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._PodCIDR = params.get("PodCIDR")
        self._ServiceCIDR = params.get("ServiceCIDR")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckEdgeClusterCIDRResponse(AbstractModel):
    """CheckEdgeClusterCIDR response structure.

    """

    def __init__(self):
        r"""
        :param _ConflictCode: Return code. Valid values:
-1: Internal error
0: No conflict
1: Conflict between VPC and serviceCIDR
2: Conflict between VPC and podCIDR
3: Conflict between serviceCIDR and podCIDR
        :type ConflictCode: int
        :param _ConflictMsg: CIDR block conflict description
        :type ConflictMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ConflictCode = None
        self._ConflictMsg = None
        self._RequestId = None

    @property
    def ConflictCode(self):
        return self._ConflictCode

    @ConflictCode.setter
    def ConflictCode(self, ConflictCode):
        self._ConflictCode = ConflictCode

    @property
    def ConflictMsg(self):
        return self._ConflictMsg

    @ConflictMsg.setter
    def ConflictMsg(self, ConflictMsg):
        self._ConflictMsg = ConflictMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConflictCode = params.get("ConflictCode")
        self._ConflictMsg = params.get("ConflictMsg")
        self._RequestId = params.get("RequestId")


class CheckInstancesUpgradeAbleRequest(AbstractModel):
    """CheckInstancesUpgradeAble request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: Specify the node list to check. If it’s not passed in, all nodes of the cluster will be checked.
        :type InstanceIds: list of str
        :param _UpgradeType: Upgrade type
        :type UpgradeType: str
        :param _Offset: Pagination offset
        :type Offset: int
        :param _Limit: Pagination limit
        :type Limit: int
        :param _Filter: Filtering
        :type Filter: list of Filter
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._UpgradeType = None
        self._Offset = None
        self._Limit = None
        self._Filter = None

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
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

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
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._UpgradeType = params.get("UpgradeType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstancesUpgradeAbleResponse(AbstractModel):
    """CheckInstancesUpgradeAble response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterVersion: The current minor version of cluster Master
        :type ClusterVersion: str
        :param _LatestVersion: The latest minor version of cluster Master corresponding major version
        :type LatestVersion: str
        :param _UpgradeAbleInstances: List of nodes that can be upgraded
Note: this field may return `null`, indicating that no valid value is obtained.
        :type UpgradeAbleInstances: list of UpgradeAbleInstancesItem
        :param _Total: Total number
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Total: int
        :param _UnavailableVersionReason: Reason why the upgrade is not available
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UnavailableVersionReason: list of UnavailableReason
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterVersion = None
        self._LatestVersion = None
        self._UpgradeAbleInstances = None
        self._Total = None
        self._UnavailableVersionReason = None
        self._RequestId = None

    @property
    def ClusterVersion(self):
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def LatestVersion(self):
        return self._LatestVersion

    @LatestVersion.setter
    def LatestVersion(self, LatestVersion):
        self._LatestVersion = LatestVersion

    @property
    def UpgradeAbleInstances(self):
        return self._UpgradeAbleInstances

    @UpgradeAbleInstances.setter
    def UpgradeAbleInstances(self, UpgradeAbleInstances):
        self._UpgradeAbleInstances = UpgradeAbleInstances

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UnavailableVersionReason(self):
        return self._UnavailableVersionReason

    @UnavailableVersionReason.setter
    def UnavailableVersionReason(self, UnavailableVersionReason):
        self._UnavailableVersionReason = UnavailableVersionReason

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterVersion = params.get("ClusterVersion")
        self._LatestVersion = params.get("LatestVersion")
        if params.get("UpgradeAbleInstances") is not None:
            self._UpgradeAbleInstances = []
            for item in params.get("UpgradeAbleInstances"):
                obj = UpgradeAbleInstancesItem()
                obj._deserialize(item)
                self._UpgradeAbleInstances.append(obj)
        self._Total = params.get("Total")
        if params.get("UnavailableVersionReason") is not None:
            self._UnavailableVersionReason = []
            for item in params.get("UnavailableVersionReason"):
                obj = UnavailableReason()
                obj._deserialize(item)
                self._UnavailableVersionReason.append(obj)
        self._RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """Cluster information struct

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _ClusterDescription: Cluster description
        :type ClusterDescription: str
        :param _ClusterVersion: Cluster version. The default value is 1.10.5.
        :type ClusterVersion: str
        :param _ClusterOs: Cluster operating system. centOS 7.2x86_64 or ubuntu 16.04.1 LTSx86_64. Default value: ubuntu 16.04.1 LTSx86_64
        :type ClusterOs: str
        :param _ClusterType: Cluster type. Managed cluster: MANAGED_CLUSTER; Self-deployed cluster: INDEPENDENT_CLUSTER.
        :type ClusterType: str
        :param _ClusterNetworkSettings: Cluster network-related parameters
        :type ClusterNetworkSettings: :class:`tencentcloud.tke.v20180525.models.ClusterNetworkSettings`
        :param _ClusterNodeNum: Current number of nodes in the cluster
        :type ClusterNodeNum: int
        :param _ProjectId: ID of the project to which the cluster belongs
        :type ProjectId: int
        :param _TagSpecification: Tag description list.
        :type TagSpecification: list of TagSpecification
        :param _ClusterStatus: Cluster status. Values: `Trading` (Preparing), `Creating`, `Running`, `Deleting`, `Idling` (Idle), `Recovering`, `Scaling`, `Upgrading` (Upgrading the cluster), `WaittingForConnect` (Pending registration), `Pause` (Cluster upgrade paused), `NodeUpgrading` (Upgrading the node), `RuntimeUpgrading` (Upgrading the node runtime), `MasterScaling` (Scaling Master), `ClusterLevelUpgrading` (Adjusting cluster specification level), `ResourceIsolate` (Isolating), `ResourceIsolated` (Isolated), `ResourceReverse` (Overdue payment made. Recovering the cluster), and `Abnormal`.
        :type ClusterStatus: str
        :param _Property: Cluster attributes (including a map of different cluster attributes, with attribute fields including NodeNameType (lan-ip mode and hostname mode, with lan-ip mode as default))
        :type Property: str
        :param _ClusterMaterNodeNum: Number of primary nodes currently in the cluster
        :type ClusterMaterNodeNum: int
        :param _ImageId: ID of the image used by the cluster
Note: this field may return null, indicating that no valid value is obtained.
        :type ImageId: str
        :param _OsCustomizeType: Container image tag
Note: This field may return null, indicating that no valid value was found.
        :type OsCustomizeType: str
        :param _ContainerRuntime: Runtime environment of the cluster. Values can be `docker` or `containerd`.
Note: this field may return null, indicating that no valid value is obtained.
        :type ContainerRuntime: str
        :param _CreatedTime: Creation time
Note: this field may return null, indicating that no valid value is obtained.
        :type CreatedTime: str
        :param _DeletionProtection: Whether Deletion Protection is enabled
Note: this field may return null, indicating that no valid value is obtained.
        :type DeletionProtection: bool
        :param _EnableExternalNode: Specifies whether the cluster supports external nodes.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type EnableExternalNode: bool
        :param _ClusterLevel: Cluster models. It’s valid for managed clusters.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterLevel: str
        :param _AutoUpgradeClusterLevel: The target cluster model for auto-upgrade
Note: this field may return null, indicating that no valid value is obtained.
        :type AutoUpgradeClusterLevel: bool
        :param _QGPUShareEnable: Whether to enable qGPU Sharing
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type QGPUShareEnable: bool
        :param _RuntimeVersion: Runtime version
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuntimeVersion: str
        :param _ClusterEtcdNodeNum: Number of current etcd in the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterEtcdNodeNum: int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._ClusterDescription = None
        self._ClusterVersion = None
        self._ClusterOs = None
        self._ClusterType = None
        self._ClusterNetworkSettings = None
        self._ClusterNodeNum = None
        self._ProjectId = None
        self._TagSpecification = None
        self._ClusterStatus = None
        self._Property = None
        self._ClusterMaterNodeNum = None
        self._ImageId = None
        self._OsCustomizeType = None
        self._ContainerRuntime = None
        self._CreatedTime = None
        self._DeletionProtection = None
        self._EnableExternalNode = None
        self._ClusterLevel = None
        self._AutoUpgradeClusterLevel = None
        self._QGPUShareEnable = None
        self._RuntimeVersion = None
        self._ClusterEtcdNodeNum = None

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
    def ClusterDescription(self):
        return self._ClusterDescription

    @ClusterDescription.setter
    def ClusterDescription(self, ClusterDescription):
        self._ClusterDescription = ClusterDescription

    @property
    def ClusterVersion(self):
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def ClusterOs(self):
        return self._ClusterOs

    @ClusterOs.setter
    def ClusterOs(self, ClusterOs):
        self._ClusterOs = ClusterOs

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def ClusterNetworkSettings(self):
        return self._ClusterNetworkSettings

    @ClusterNetworkSettings.setter
    def ClusterNetworkSettings(self, ClusterNetworkSettings):
        self._ClusterNetworkSettings = ClusterNetworkSettings

    @property
    def ClusterNodeNum(self):
        return self._ClusterNodeNum

    @ClusterNodeNum.setter
    def ClusterNodeNum(self, ClusterNodeNum):
        self._ClusterNodeNum = ClusterNodeNum

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

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def Property(self):
        return self._Property

    @Property.setter
    def Property(self, Property):
        self._Property = Property

    @property
    def ClusterMaterNodeNum(self):
        return self._ClusterMaterNodeNum

    @ClusterMaterNodeNum.setter
    def ClusterMaterNodeNum(self, ClusterMaterNodeNum):
        self._ClusterMaterNodeNum = ClusterMaterNodeNum

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def OsCustomizeType(self):
        return self._OsCustomizeType

    @OsCustomizeType.setter
    def OsCustomizeType(self, OsCustomizeType):
        self._OsCustomizeType = OsCustomizeType

    @property
    def ContainerRuntime(self):
        return self._ContainerRuntime

    @ContainerRuntime.setter
    def ContainerRuntime(self, ContainerRuntime):
        self._ContainerRuntime = ContainerRuntime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def EnableExternalNode(self):
        return self._EnableExternalNode

    @EnableExternalNode.setter
    def EnableExternalNode(self, EnableExternalNode):
        self._EnableExternalNode = EnableExternalNode

    @property
    def ClusterLevel(self):
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel

    @property
    def AutoUpgradeClusterLevel(self):
        return self._AutoUpgradeClusterLevel

    @AutoUpgradeClusterLevel.setter
    def AutoUpgradeClusterLevel(self, AutoUpgradeClusterLevel):
        self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel

    @property
    def QGPUShareEnable(self):
        return self._QGPUShareEnable

    @QGPUShareEnable.setter
    def QGPUShareEnable(self, QGPUShareEnable):
        self._QGPUShareEnable = QGPUShareEnable

    @property
    def RuntimeVersion(self):
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def ClusterEtcdNodeNum(self):
        return self._ClusterEtcdNodeNum

    @ClusterEtcdNodeNum.setter
    def ClusterEtcdNodeNum(self, ClusterEtcdNodeNum):
        self._ClusterEtcdNodeNum = ClusterEtcdNodeNum


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._ClusterDescription = params.get("ClusterDescription")
        self._ClusterVersion = params.get("ClusterVersion")
        self._ClusterOs = params.get("ClusterOs")
        self._ClusterType = params.get("ClusterType")
        if params.get("ClusterNetworkSettings") is not None:
            self._ClusterNetworkSettings = ClusterNetworkSettings()
            self._ClusterNetworkSettings._deserialize(params.get("ClusterNetworkSettings"))
        self._ClusterNodeNum = params.get("ClusterNodeNum")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._ClusterStatus = params.get("ClusterStatus")
        self._Property = params.get("Property")
        self._ClusterMaterNodeNum = params.get("ClusterMaterNodeNum")
        self._ImageId = params.get("ImageId")
        self._OsCustomizeType = params.get("OsCustomizeType")
        self._ContainerRuntime = params.get("ContainerRuntime")
        self._CreatedTime = params.get("CreatedTime")
        self._DeletionProtection = params.get("DeletionProtection")
        self._EnableExternalNode = params.get("EnableExternalNode")
        self._ClusterLevel = params.get("ClusterLevel")
        self._AutoUpgradeClusterLevel = params.get("AutoUpgradeClusterLevel")
        self._QGPUShareEnable = params.get("QGPUShareEnable")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._ClusterEtcdNodeNum = params.get("ClusterEtcdNodeNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAdvancedSettings(AbstractModel):
    """Cluster advanced configurations

    """

    def __init__(self):
        r"""
        :param _IPVS: Whether IPVS is enabled
        :type IPVS: bool
        :param _AsEnabled: Whether auto-scaling is enabled for nodes in the cluster (Enabling this function is not supported when you create a cluster)
        :type AsEnabled: bool
        :param _ContainerRuntime: Type of runtime component used by the cluster. The types include "docker" and "containerd". Default value: docker
        :type ContainerRuntime: str
        :param _NodeNameType: NodeName type for a node in a cluster (This includes the two forms of **hostname** and **lan-ip**, with the default as **lan-ip**. If **hostname** is used, you need to set the HostName parameter when creating a node, and the InstanceName needs to be the same as the HostName.)
        :type NodeNameType: str
        :param _ExtraArgs: Cluster custom parameter
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        :param _NetworkType: Cluster network type, which can be GR (Global Router) or VPC-CNI. The default value is GR.
        :type NetworkType: str
        :param _IsNonStaticIpMode: Whether a cluster in VPC-CNI mode uses dynamic IP addresses. The default value is FALSE, which indicates that static IP addresses are used.
        :type IsNonStaticIpMode: bool
        :param _DeletionProtection: Indicates whether to enable cluster deletion protection.
        :type DeletionProtection: bool
        :param _KubeProxyMode: Cluster network proxy model, which is only used when ipvs-bpf mode is used. At present, TKE cluster supports three network proxy modes including `iptables`, `ipvs` and `ipvs-bpf` and their parameter setting relationships are as follows:
`iptables`: do not set IPVS and KubeProxyMode.
`ipvs`: set IPVS to `true` and do not set KubeProxyMode.
`ipvs-bpf`: set KubeProxyMode to `kube-proxy-bpf`.
The following conditions are required to use ipvs-bpf network mode:
1. The cluster version must be v1.14 or later.
2. The system image must be Tencent Linux 2.4.
        :type KubeProxyMode: str
        :param _AuditEnabled: Indicates whether to enable auditing
        :type AuditEnabled: bool
        :param _AuditLogsetId: Specifies the ID of logset to which the audit logs are uploaded.
        :type AuditLogsetId: str
        :param _AuditLogTopicId: Specifies the ID of topic to which the audit logs are uploaded.
        :type AuditLogTopicId: str
        :param _VpcCniType: Specifies the ENI type. Values: `tke-route-eni` (multi-IP shared ENI); `tke-direct-eni` (independent ENI). It defaults to `tke-route-eni`.
        :type VpcCniType: str
        :param _RuntimeVersion: Runtime version
        :type RuntimeVersion: str
        :param _EnableCustomizedPodCIDR: Indicates whether to enable the custom mode for the node’s pod CIDR range
        :type EnableCustomizedPodCIDR: bool
        :param _BasePodNumber: The basic number of Pods in custom mode
        :type BasePodNumber: int
        :param _CiliumMode: Specifies whether to enable Cilium. If it’s left empty, Cilium is not enabled. If `clusterIP` is passed in, it means to enable Cilium to support the clusterIP service type.
        :type CiliumMode: str
        :param _IsDualStack: Whether it is a dual-stack cluster in VPC-CNI mode. Default value: `false`, which indicates it is not a dual-stack cluster.
        :type IsDualStack: bool
        :param _QGPUShareEnable: Whether to enable qGPU Sharing
        :type QGPUShareEnable: bool
        """
        self._IPVS = None
        self._AsEnabled = None
        self._ContainerRuntime = None
        self._NodeNameType = None
        self._ExtraArgs = None
        self._NetworkType = None
        self._IsNonStaticIpMode = None
        self._DeletionProtection = None
        self._KubeProxyMode = None
        self._AuditEnabled = None
        self._AuditLogsetId = None
        self._AuditLogTopicId = None
        self._VpcCniType = None
        self._RuntimeVersion = None
        self._EnableCustomizedPodCIDR = None
        self._BasePodNumber = None
        self._CiliumMode = None
        self._IsDualStack = None
        self._QGPUShareEnable = None

    @property
    def IPVS(self):
        return self._IPVS

    @IPVS.setter
    def IPVS(self, IPVS):
        self._IPVS = IPVS

    @property
    def AsEnabled(self):
        return self._AsEnabled

    @AsEnabled.setter
    def AsEnabled(self, AsEnabled):
        self._AsEnabled = AsEnabled

    @property
    def ContainerRuntime(self):
        return self._ContainerRuntime

    @ContainerRuntime.setter
    def ContainerRuntime(self, ContainerRuntime):
        self._ContainerRuntime = ContainerRuntime

    @property
    def NodeNameType(self):
        return self._NodeNameType

    @NodeNameType.setter
    def NodeNameType(self, NodeNameType):
        self._NodeNameType = NodeNameType

    @property
    def ExtraArgs(self):
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def IsNonStaticIpMode(self):
        return self._IsNonStaticIpMode

    @IsNonStaticIpMode.setter
    def IsNonStaticIpMode(self, IsNonStaticIpMode):
        self._IsNonStaticIpMode = IsNonStaticIpMode

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def KubeProxyMode(self):
        return self._KubeProxyMode

    @KubeProxyMode.setter
    def KubeProxyMode(self, KubeProxyMode):
        self._KubeProxyMode = KubeProxyMode

    @property
    def AuditEnabled(self):
        return self._AuditEnabled

    @AuditEnabled.setter
    def AuditEnabled(self, AuditEnabled):
        self._AuditEnabled = AuditEnabled

    @property
    def AuditLogsetId(self):
        return self._AuditLogsetId

    @AuditLogsetId.setter
    def AuditLogsetId(self, AuditLogsetId):
        self._AuditLogsetId = AuditLogsetId

    @property
    def AuditLogTopicId(self):
        return self._AuditLogTopicId

    @AuditLogTopicId.setter
    def AuditLogTopicId(self, AuditLogTopicId):
        self._AuditLogTopicId = AuditLogTopicId

    @property
    def VpcCniType(self):
        return self._VpcCniType

    @VpcCniType.setter
    def VpcCniType(self, VpcCniType):
        self._VpcCniType = VpcCniType

    @property
    def RuntimeVersion(self):
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def EnableCustomizedPodCIDR(self):
        return self._EnableCustomizedPodCIDR

    @EnableCustomizedPodCIDR.setter
    def EnableCustomizedPodCIDR(self, EnableCustomizedPodCIDR):
        self._EnableCustomizedPodCIDR = EnableCustomizedPodCIDR

    @property
    def BasePodNumber(self):
        return self._BasePodNumber

    @BasePodNumber.setter
    def BasePodNumber(self, BasePodNumber):
        self._BasePodNumber = BasePodNumber

    @property
    def CiliumMode(self):
        return self._CiliumMode

    @CiliumMode.setter
    def CiliumMode(self, CiliumMode):
        self._CiliumMode = CiliumMode

    @property
    def IsDualStack(self):
        return self._IsDualStack

    @IsDualStack.setter
    def IsDualStack(self, IsDualStack):
        self._IsDualStack = IsDualStack

    @property
    def QGPUShareEnable(self):
        return self._QGPUShareEnable

    @QGPUShareEnable.setter
    def QGPUShareEnable(self, QGPUShareEnable):
        self._QGPUShareEnable = QGPUShareEnable


    def _deserialize(self, params):
        self._IPVS = params.get("IPVS")
        self._AsEnabled = params.get("AsEnabled")
        self._ContainerRuntime = params.get("ContainerRuntime")
        self._NodeNameType = params.get("NodeNameType")
        if params.get("ExtraArgs") is not None:
            self._ExtraArgs = ClusterExtraArgs()
            self._ExtraArgs._deserialize(params.get("ExtraArgs"))
        self._NetworkType = params.get("NetworkType")
        self._IsNonStaticIpMode = params.get("IsNonStaticIpMode")
        self._DeletionProtection = params.get("DeletionProtection")
        self._KubeProxyMode = params.get("KubeProxyMode")
        self._AuditEnabled = params.get("AuditEnabled")
        self._AuditLogsetId = params.get("AuditLogsetId")
        self._AuditLogTopicId = params.get("AuditLogTopicId")
        self._VpcCniType = params.get("VpcCniType")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._EnableCustomizedPodCIDR = params.get("EnableCustomizedPodCIDR")
        self._BasePodNumber = params.get("BasePodNumber")
        self._CiliumMode = params.get("CiliumMode")
        self._IsDualStack = params.get("IsDualStack")
        self._QGPUShareEnable = params.get("QGPUShareEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroup(AbstractModel):
    """Cluster-associated scaling group information

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _Status: Scaling group status (`enabled`, `enabling`, `disabled`, `disabling`, `updating`, `deleting`, `scaleDownEnabling`, `scaleDownDisabling`)
        :type Status: str
        :param _IsUnschedulable: Whether the node is set to unschedulable
Note: this field may return null, indicating that no valid value was found.
        :type IsUnschedulable: bool
        :param _Labels: Scaling group label list
Note: this field may return null, indicating that no valid value was found.
        :type Labels: list of Label
        :param _CreatedTime: Creation time
        :type CreatedTime: str
        """
        self._AutoScalingGroupId = None
        self._Status = None
        self._IsUnschedulable = None
        self._Labels = None
        self._CreatedTime = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsUnschedulable(self):
        return self._IsUnschedulable

    @IsUnschedulable.setter
    def IsUnschedulable(self, IsUnschedulable):
        self._IsUnschedulable = IsUnschedulable

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._Status = params.get("Status")
        self._IsUnschedulable = params.get("IsUnschedulable")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupAttribute(AbstractModel):
    """Cluster scaling group attributes

    """

    def __init__(self):
        r"""
        :param _AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param _AutoScalingGroupEnabled: Whether it is enabled
        :type AutoScalingGroupEnabled: bool
        :param _AutoScalingGroupRange: Maximum and minimum number of pods in a scaling group
        :type AutoScalingGroupRange: :class:`tencentcloud.tke.v20180525.models.AutoScalingGroupRange`
        """
        self._AutoScalingGroupId = None
        self._AutoScalingGroupEnabled = None
        self._AutoScalingGroupRange = None

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def AutoScalingGroupEnabled(self):
        return self._AutoScalingGroupEnabled

    @AutoScalingGroupEnabled.setter
    def AutoScalingGroupEnabled(self, AutoScalingGroupEnabled):
        self._AutoScalingGroupEnabled = AutoScalingGroupEnabled

    @property
    def AutoScalingGroupRange(self):
        return self._AutoScalingGroupRange

    @AutoScalingGroupRange.setter
    def AutoScalingGroupRange(self, AutoScalingGroupRange):
        self._AutoScalingGroupRange = AutoScalingGroupRange


    def _deserialize(self, params):
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._AutoScalingGroupEnabled = params.get("AutoScalingGroupEnabled")
        if params.get("AutoScalingGroupRange") is not None:
            self._AutoScalingGroupRange = AutoScalingGroupRange()
            self._AutoScalingGroupRange._deserialize(params.get("AutoScalingGroupRange"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupOption(AbstractModel):
    """Cluster auto scaling configuration

    """

    def __init__(self):
        r"""
        :param _IsScaleDownEnabled: Whether to enable scale-in
Note: this field may return null, indicating that no valid value was found.
        :type IsScaleDownEnabled: bool
        :param _Expander: The scale-out method when there are multiple scaling groups. `random`: select a random scaling group. `most-pods`: choose the scaling group that can schedule the most pods. `least-waste`: select the scaling group that can ensure the fewest remaining resources after Pod scheduling.. The default value is `random`.)
Note: this field may return null, indicating that no valid value was found.
        :type Expander: str
        :param _MaxEmptyBulkDelete: Max concurrent scale-in volume
Note: this field may return null, indicating that no valid value was found.
        :type MaxEmptyBulkDelete: int
        :param _ScaleDownDelay: Number of minutes after cluster scale-out when the system starts judging whether to perform scale-in
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownDelay: int
        :param _ScaleDownUnneededTime: Number of consecutive minutes of idleness after which the node is subject to scale-in (default value: 10)
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownUnneededTime: int
        :param _ScaleDownUtilizationThreshold: Percentage of node resource usage below which the node is considered to be idle (default value: 50)
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownUtilizationThreshold: int
        :param _SkipNodesWithLocalStorage: During scale-in, ignore nodes with local storage pods (default value: False)
Note: this field may return null, indicating that no valid value was found.
        :type SkipNodesWithLocalStorage: bool
        :param _SkipNodesWithSystemPods: During scale-in, ignore nodes with pods in the kube-system namespace that are not managed by DaemonSet (default value: False)
Note: this field may return null, indicating that no valid value was found.
        :type SkipNodesWithSystemPods: bool
        :param _IgnoreDaemonSetsUtilization: Whether to ignore DaemonSet pods by default when calculating resource usage (default value: False: do not ignore)
Note: this field may return null, indicating that no valid value was found.
        :type IgnoreDaemonSetsUtilization: bool
        :param _OkTotalUnreadyCount: Number at which CA health detection is triggered (default value: 3). After the number specified in OkTotalUnreadyCount is exceeded, CA will perform health detection.
Note: this field may return null, indicating that no valid value was found.
        :type OkTotalUnreadyCount: int
        :param _MaxTotalUnreadyPercentage: Max percentage of unready nodes. After the max percentage is exceeded, CA will stop operation.
Note: this field may return null, indicating that no valid value was found.
        :type MaxTotalUnreadyPercentage: int
        :param _ScaleDownUnreadyTime: Amount of time before unready nodes become eligible for scale-in
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownUnreadyTime: int
        :param _UnregisteredNodeRemovalTime: Waiting time before CA deletes nodes that are not registered in Kubernetes
Note: this field may return null, indicating that no valid value was found.
        :type UnregisteredNodeRemovalTime: int
        """
        self._IsScaleDownEnabled = None
        self._Expander = None
        self._MaxEmptyBulkDelete = None
        self._ScaleDownDelay = None
        self._ScaleDownUnneededTime = None
        self._ScaleDownUtilizationThreshold = None
        self._SkipNodesWithLocalStorage = None
        self._SkipNodesWithSystemPods = None
        self._IgnoreDaemonSetsUtilization = None
        self._OkTotalUnreadyCount = None
        self._MaxTotalUnreadyPercentage = None
        self._ScaleDownUnreadyTime = None
        self._UnregisteredNodeRemovalTime = None

    @property
    def IsScaleDownEnabled(self):
        return self._IsScaleDownEnabled

    @IsScaleDownEnabled.setter
    def IsScaleDownEnabled(self, IsScaleDownEnabled):
        self._IsScaleDownEnabled = IsScaleDownEnabled

    @property
    def Expander(self):
        return self._Expander

    @Expander.setter
    def Expander(self, Expander):
        self._Expander = Expander

    @property
    def MaxEmptyBulkDelete(self):
        return self._MaxEmptyBulkDelete

    @MaxEmptyBulkDelete.setter
    def MaxEmptyBulkDelete(self, MaxEmptyBulkDelete):
        self._MaxEmptyBulkDelete = MaxEmptyBulkDelete

    @property
    def ScaleDownDelay(self):
        return self._ScaleDownDelay

    @ScaleDownDelay.setter
    def ScaleDownDelay(self, ScaleDownDelay):
        self._ScaleDownDelay = ScaleDownDelay

    @property
    def ScaleDownUnneededTime(self):
        return self._ScaleDownUnneededTime

    @ScaleDownUnneededTime.setter
    def ScaleDownUnneededTime(self, ScaleDownUnneededTime):
        self._ScaleDownUnneededTime = ScaleDownUnneededTime

    @property
    def ScaleDownUtilizationThreshold(self):
        return self._ScaleDownUtilizationThreshold

    @ScaleDownUtilizationThreshold.setter
    def ScaleDownUtilizationThreshold(self, ScaleDownUtilizationThreshold):
        self._ScaleDownUtilizationThreshold = ScaleDownUtilizationThreshold

    @property
    def SkipNodesWithLocalStorage(self):
        return self._SkipNodesWithLocalStorage

    @SkipNodesWithLocalStorage.setter
    def SkipNodesWithLocalStorage(self, SkipNodesWithLocalStorage):
        self._SkipNodesWithLocalStorage = SkipNodesWithLocalStorage

    @property
    def SkipNodesWithSystemPods(self):
        return self._SkipNodesWithSystemPods

    @SkipNodesWithSystemPods.setter
    def SkipNodesWithSystemPods(self, SkipNodesWithSystemPods):
        self._SkipNodesWithSystemPods = SkipNodesWithSystemPods

    @property
    def IgnoreDaemonSetsUtilization(self):
        return self._IgnoreDaemonSetsUtilization

    @IgnoreDaemonSetsUtilization.setter
    def IgnoreDaemonSetsUtilization(self, IgnoreDaemonSetsUtilization):
        self._IgnoreDaemonSetsUtilization = IgnoreDaemonSetsUtilization

    @property
    def OkTotalUnreadyCount(self):
        return self._OkTotalUnreadyCount

    @OkTotalUnreadyCount.setter
    def OkTotalUnreadyCount(self, OkTotalUnreadyCount):
        self._OkTotalUnreadyCount = OkTotalUnreadyCount

    @property
    def MaxTotalUnreadyPercentage(self):
        return self._MaxTotalUnreadyPercentage

    @MaxTotalUnreadyPercentage.setter
    def MaxTotalUnreadyPercentage(self, MaxTotalUnreadyPercentage):
        self._MaxTotalUnreadyPercentage = MaxTotalUnreadyPercentage

    @property
    def ScaleDownUnreadyTime(self):
        return self._ScaleDownUnreadyTime

    @ScaleDownUnreadyTime.setter
    def ScaleDownUnreadyTime(self, ScaleDownUnreadyTime):
        self._ScaleDownUnreadyTime = ScaleDownUnreadyTime

    @property
    def UnregisteredNodeRemovalTime(self):
        return self._UnregisteredNodeRemovalTime

    @UnregisteredNodeRemovalTime.setter
    def UnregisteredNodeRemovalTime(self, UnregisteredNodeRemovalTime):
        self._UnregisteredNodeRemovalTime = UnregisteredNodeRemovalTime


    def _deserialize(self, params):
        self._IsScaleDownEnabled = params.get("IsScaleDownEnabled")
        self._Expander = params.get("Expander")
        self._MaxEmptyBulkDelete = params.get("MaxEmptyBulkDelete")
        self._ScaleDownDelay = params.get("ScaleDownDelay")
        self._ScaleDownUnneededTime = params.get("ScaleDownUnneededTime")
        self._ScaleDownUtilizationThreshold = params.get("ScaleDownUtilizationThreshold")
        self._SkipNodesWithLocalStorage = params.get("SkipNodesWithLocalStorage")
        self._SkipNodesWithSystemPods = params.get("SkipNodesWithSystemPods")
        self._IgnoreDaemonSetsUtilization = params.get("IgnoreDaemonSetsUtilization")
        self._OkTotalUnreadyCount = params.get("OkTotalUnreadyCount")
        self._MaxTotalUnreadyPercentage = params.get("MaxTotalUnreadyPercentage")
        self._ScaleDownUnreadyTime = params.get("ScaleDownUnreadyTime")
        self._UnregisteredNodeRemovalTime = params.get("UnregisteredNodeRemovalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterBasicSettings(AbstractModel):
    """Describes the basic configuration information of a cluster

    """

    def __init__(self):
        r"""
        :param _ClusterOs: Cluster operating system. Public image (enter the image name) and custom image (enter the image ID) are supported. For details, see https://intl.cloud.tencent.com/document/product/457/68289?from_cn_redirect=1
        :type ClusterOs: str
        :param _ClusterVersion: Cluster version. The default value is 1.10.5.
        :type ClusterVersion: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _ClusterDescription: Cluster description
        :type ClusterDescription: str
        :param _VpcId: VPC ID, in the format of vpc-xxx, which is required when you create an empty managed cluster.
        :type VpcId: str
        :param _ProjectId: ID of the project to which the new resources in the cluster belong.
        :type ProjectId: int
        :param _TagSpecification: Tag description list. This parameter is used to bind a tag to a resource instance. Currently, a tag can only be bound to cluster instances.
        :type TagSpecification: list of TagSpecification
        :param _OsCustomizeType: Container image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
        :type OsCustomizeType: str
        :param _NeedWorkSecurityGroup: Whether to enable the node’s default security group (default: `No`, Alpha feature)
        :type NeedWorkSecurityGroup: bool
        :param _SubnetId: When the Cilium Overlay add-on is selected, TKE will take two IPs from the subnet to create the private network CLB.
        :type SubnetId: str
        :param _ClusterLevel: Cluster specifications available for managed clusters
        :type ClusterLevel: str
        :param _AutoUpgradeClusterLevel: Auto cluster upgrade for managed clusters
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
        """
        self._ClusterOs = None
        self._ClusterVersion = None
        self._ClusterName = None
        self._ClusterDescription = None
        self._VpcId = None
        self._ProjectId = None
        self._TagSpecification = None
        self._OsCustomizeType = None
        self._NeedWorkSecurityGroup = None
        self._SubnetId = None
        self._ClusterLevel = None
        self._AutoUpgradeClusterLevel = None

    @property
    def ClusterOs(self):
        return self._ClusterOs

    @ClusterOs.setter
    def ClusterOs(self, ClusterOs):
        self._ClusterOs = ClusterOs

    @property
    def ClusterVersion(self):
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterDescription(self):
        return self._ClusterDescription

    @ClusterDescription.setter
    def ClusterDescription(self, ClusterDescription):
        self._ClusterDescription = ClusterDescription

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

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

    @property
    def OsCustomizeType(self):
        return self._OsCustomizeType

    @OsCustomizeType.setter
    def OsCustomizeType(self, OsCustomizeType):
        self._OsCustomizeType = OsCustomizeType

    @property
    def NeedWorkSecurityGroup(self):
        return self._NeedWorkSecurityGroup

    @NeedWorkSecurityGroup.setter
    def NeedWorkSecurityGroup(self, NeedWorkSecurityGroup):
        self._NeedWorkSecurityGroup = NeedWorkSecurityGroup

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ClusterLevel(self):
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel

    @property
    def AutoUpgradeClusterLevel(self):
        return self._AutoUpgradeClusterLevel

    @AutoUpgradeClusterLevel.setter
    def AutoUpgradeClusterLevel(self, AutoUpgradeClusterLevel):
        self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel


    def _deserialize(self, params):
        self._ClusterOs = params.get("ClusterOs")
        self._ClusterVersion = params.get("ClusterVersion")
        self._ClusterName = params.get("ClusterName")
        self._ClusterDescription = params.get("ClusterDescription")
        self._VpcId = params.get("VpcId")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._OsCustomizeType = params.get("OsCustomizeType")
        self._NeedWorkSecurityGroup = params.get("NeedWorkSecurityGroup")
        self._SubnetId = params.get("SubnetId")
        self._ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self._AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCIDRSettings(AbstractModel):
    """Container networking parameters for the cluster

    """

    def __init__(self):
        r"""
        :param _ClusterCIDR: CIDR used to assign container and service IPs for the cluster. It cannot conflict with the VPC's CIDR or the CIDRs of other clusters in the same VPC
        :type ClusterCIDR: str
        :param _IgnoreClusterCIDRConflict: Whether to ignore ClusterCIDR conflict errors, which are not ignored by default
        :type IgnoreClusterCIDRConflict: bool
        :param _MaxNodePodNum: Maximum number of Pods on each node. Value range: 16 to 256. When its power is not 2, it will round upward to the closest power of 2.
        :type MaxNodePodNum: int
        :param _MaxClusterServiceNum: The maximum number of services in a cluster. The range is from 32 to 32768. When its power is not 2, it will round upward to the closest power of 2. Default value is 256.
        :type MaxClusterServiceNum: int
        :param _ServiceCIDR: The CIDR block used to assign cluster service IP addresses. It must conflict with neither the VPC CIDR block nor with CIDR blocks of other clusters in the same VPC instance. The IP range must be within the private network IP range, such as 10.1.0.0/14, 192.168.0.1/18, and 172.16.0.0/16.
        :type ServiceCIDR: str
        :param _EniSubnetIds: Subnet ID of the ENI in VPC-CNI network mode
        :type EniSubnetIds: list of str
        :param _ClaimExpiredSeconds: Repossession time of ENI IP addresses in VPC-CNI network mode, whose range is [300,15768000)
        :type ClaimExpiredSeconds: int
        :param _IgnoreServiceCIDRConflict: Whether to ignore ServiceCIDR conflict errors. It is only valid in VPC-CNI mode. Default value: `false`.
        :type IgnoreServiceCIDRConflict: bool
        """
        self._ClusterCIDR = None
        self._IgnoreClusterCIDRConflict = None
        self._MaxNodePodNum = None
        self._MaxClusterServiceNum = None
        self._ServiceCIDR = None
        self._EniSubnetIds = None
        self._ClaimExpiredSeconds = None
        self._IgnoreServiceCIDRConflict = None

    @property
    def ClusterCIDR(self):
        return self._ClusterCIDR

    @ClusterCIDR.setter
    def ClusterCIDR(self, ClusterCIDR):
        self._ClusterCIDR = ClusterCIDR

    @property
    def IgnoreClusterCIDRConflict(self):
        return self._IgnoreClusterCIDRConflict

    @IgnoreClusterCIDRConflict.setter
    def IgnoreClusterCIDRConflict(self, IgnoreClusterCIDRConflict):
        self._IgnoreClusterCIDRConflict = IgnoreClusterCIDRConflict

    @property
    def MaxNodePodNum(self):
        return self._MaxNodePodNum

    @MaxNodePodNum.setter
    def MaxNodePodNum(self, MaxNodePodNum):
        self._MaxNodePodNum = MaxNodePodNum

    @property
    def MaxClusterServiceNum(self):
        return self._MaxClusterServiceNum

    @MaxClusterServiceNum.setter
    def MaxClusterServiceNum(self, MaxClusterServiceNum):
        self._MaxClusterServiceNum = MaxClusterServiceNum

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR

    @property
    def EniSubnetIds(self):
        return self._EniSubnetIds

    @EniSubnetIds.setter
    def EniSubnetIds(self, EniSubnetIds):
        self._EniSubnetIds = EniSubnetIds

    @property
    def ClaimExpiredSeconds(self):
        return self._ClaimExpiredSeconds

    @ClaimExpiredSeconds.setter
    def ClaimExpiredSeconds(self, ClaimExpiredSeconds):
        self._ClaimExpiredSeconds = ClaimExpiredSeconds

    @property
    def IgnoreServiceCIDRConflict(self):
        return self._IgnoreServiceCIDRConflict

    @IgnoreServiceCIDRConflict.setter
    def IgnoreServiceCIDRConflict(self, IgnoreServiceCIDRConflict):
        self._IgnoreServiceCIDRConflict = IgnoreServiceCIDRConflict


    def _deserialize(self, params):
        self._ClusterCIDR = params.get("ClusterCIDR")
        self._IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self._MaxNodePodNum = params.get("MaxNodePodNum")
        self._MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self._ServiceCIDR = params.get("ServiceCIDR")
        self._EniSubnetIds = params.get("EniSubnetIds")
        self._ClaimExpiredSeconds = params.get("ClaimExpiredSeconds")
        self._IgnoreServiceCIDRConflict = params.get("IgnoreServiceCIDRConflict")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCondition(AbstractModel):
    """Cluster creation process

    """

    def __init__(self):
        r"""
        :param _Type: Process type
        :type Type: str
        :param _Status: Process status
        :type Status: str
        :param _LastProbeTime: Last time when the status is probed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastProbeTime: str
        :param _LastTransitionTime: Last time when transiting to the process
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastTransitionTime: str
        :param _Reason: Reasons for transiting to the process
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Reason: str
        :param _Message: More information on transition
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Message: str
        """
        self._Type = None
        self._Status = None
        self._LastProbeTime = None
        self._LastTransitionTime = None
        self._Reason = None
        self._Message = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastProbeTime(self):
        return self._LastProbeTime

    @LastProbeTime.setter
    def LastProbeTime(self, LastProbeTime):
        self._LastProbeTime = LastProbeTime

    @property
    def LastTransitionTime(self):
        return self._LastTransitionTime

    @LastTransitionTime.setter
    def LastTransitionTime(self, LastTransitionTime):
        self._LastTransitionTime = LastTransitionTime

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._LastProbeTime = params.get("LastProbeTime")
        self._LastTransitionTime = params.get("LastTransitionTime")
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCredential(AbstractModel):
    """Authentication information for accessing K8s

    """

    def __init__(self):
        r"""
        :param _CACert: CA root certificate
        :type CACert: str
        :param _Token: Token for authentication
        :type Token: str
        """
        self._CACert = None
        self._Token = None

    @property
    def CACert(self):
        return self._CACert

    @CACert.setter
    def CACert(self, CACert):
        self._CACert = CACert

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._CACert = params.get("CACert")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExtraArgs(AbstractModel):
    """Cluster master custom parameter

    """

    def __init__(self):
        r"""
        :param _KubeAPIServer: kube-apiserver custom parameter, in the format of ["k1=v1", "k1=v2"], for example: ["max-requests-inflight=500","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"].
Note: this field may return `null`, indicating that no valid value is obtained.
        :type KubeAPIServer: list of str
        :param _KubeControllerManager: kube-controller-manager custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type KubeControllerManager: list of str
        :param _KubeScheduler: kube-scheduler custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type KubeScheduler: list of str
        :param _Etcd: etcd custom parameter, which is only effective for self-deployed cluster.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Etcd: list of str
        """
        self._KubeAPIServer = None
        self._KubeControllerManager = None
        self._KubeScheduler = None
        self._Etcd = None

    @property
    def KubeAPIServer(self):
        return self._KubeAPIServer

    @KubeAPIServer.setter
    def KubeAPIServer(self, KubeAPIServer):
        self._KubeAPIServer = KubeAPIServer

    @property
    def KubeControllerManager(self):
        return self._KubeControllerManager

    @KubeControllerManager.setter
    def KubeControllerManager(self, KubeControllerManager):
        self._KubeControllerManager = KubeControllerManager

    @property
    def KubeScheduler(self):
        return self._KubeScheduler

    @KubeScheduler.setter
    def KubeScheduler(self, KubeScheduler):
        self._KubeScheduler = KubeScheduler

    @property
    def Etcd(self):
        return self._Etcd

    @Etcd.setter
    def Etcd(self, Etcd):
        self._Etcd = Etcd


    def _deserialize(self, params):
        self._KubeAPIServer = params.get("KubeAPIServer")
        self._KubeControllerManager = params.get("KubeControllerManager")
        self._KubeScheduler = params.get("KubeScheduler")
        self._Etcd = params.get("Etcd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterLevelAttribute(AbstractModel):
    """Information of the managed cluster model

    """

    def __init__(self):
        r"""
        :param _Name: Cluster model
        :type Name: str
        :param _Alias: Model name
        :type Alias: str
        :param _NodeCount: Number of nodes
        :type NodeCount: int
        :param _PodCount: Number of Pods
        :type PodCount: int
        :param _ConfigMapCount: Number of ConfigMap
        :type ConfigMapCount: int
        :param _CRDCount: Number of CRDs
        :type CRDCount: int
        :param _Enable: Whether it is enabled
        :type Enable: bool
        :param _OtherCount: Number of other resources
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OtherCount: int
        """
        self._Name = None
        self._Alias = None
        self._NodeCount = None
        self._PodCount = None
        self._ConfigMapCount = None
        self._CRDCount = None
        self._Enable = None
        self._OtherCount = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def PodCount(self):
        return self._PodCount

    @PodCount.setter
    def PodCount(self, PodCount):
        self._PodCount = PodCount

    @property
    def ConfigMapCount(self):
        return self._ConfigMapCount

    @ConfigMapCount.setter
    def ConfigMapCount(self, ConfigMapCount):
        self._ConfigMapCount = ConfigMapCount

    @property
    def CRDCount(self):
        return self._CRDCount

    @CRDCount.setter
    def CRDCount(self, CRDCount):
        self._CRDCount = CRDCount

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def OtherCount(self):
        return self._OtherCount

    @OtherCount.setter
    def OtherCount(self, OtherCount):
        self._OtherCount = OtherCount


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Alias = params.get("Alias")
        self._NodeCount = params.get("NodeCount")
        self._PodCount = params.get("PodCount")
        self._ConfigMapCount = params.get("ConfigMapCount")
        self._CRDCount = params.get("CRDCount")
        self._Enable = params.get("Enable")
        self._OtherCount = params.get("OtherCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterLevelChangeRecord(AbstractModel):
    """Cluster model adjustment history

    """

    def __init__(self):
        r"""
        :param _ID: Record ID
        :type ID: str
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _Status: Status (valid values: `trading`, `upgrading`, `success`, `failed`)
        :type Status: str
        :param _Message: Status description
        :type Message: str
        :param _OldLevel: Original model
        :type OldLevel: str
        :param _NewLevel: New model
        :type NewLevel: str
        :param _TriggerType: Trigger type (valid values: `manual`, `auto`)
        :type TriggerType: str
        :param _StartedAt: Start time
        :type StartedAt: str
        :param _EndedAt: End time
        :type EndedAt: str
        """
        self._ID = None
        self._ClusterID = None
        self._Status = None
        self._Message = None
        self._OldLevel = None
        self._NewLevel = None
        self._TriggerType = None
        self._StartedAt = None
        self._EndedAt = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def OldLevel(self):
        return self._OldLevel

    @OldLevel.setter
    def OldLevel(self, OldLevel):
        self._OldLevel = OldLevel

    @property
    def NewLevel(self):
        return self._NewLevel

    @NewLevel.setter
    def NewLevel(self, NewLevel):
        self._NewLevel = NewLevel

    @property
    def TriggerType(self):
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def StartedAt(self):
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def EndedAt(self):
        return self._EndedAt

    @EndedAt.setter
    def EndedAt(self, EndedAt):
        self._EndedAt = EndedAt


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ClusterID = params.get("ClusterID")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._OldLevel = params.get("OldLevel")
        self._NewLevel = params.get("NewLevel")
        self._TriggerType = params.get("TriggerType")
        self._StartedAt = params.get("StartedAt")
        self._EndedAt = params.get("EndedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterNetworkSettings(AbstractModel):
    """Cluster network-related parameters

    """

    def __init__(self):
        r"""
        :param _ClusterCIDR: CIDR used to assign container and service IPs for the cluster. It cannot conflict with the VPC's CIDR or the CIDRs of other clusters in the same VPC.
        :type ClusterCIDR: str
        :param _IgnoreClusterCIDRConflict: Whether to ignore ClusterCIDR conflict errors. It defaults to not ignore.
        :type IgnoreClusterCIDRConflict: bool
        :param _MaxNodePodNum: Maximum number of pods on each node in the cluster. Default value: 256
        :type MaxNodePodNum: int
        :param _MaxClusterServiceNum: Maximum number of cluster services. Default value: 256
        :type MaxClusterServiceNum: int
        :param _Ipvs: Whether IPVS is enabled. Default value: disabled
        :type Ipvs: bool
        :param _VpcId: Cluster VPC ID, which is required when you create an empty cluster; otherwise, it is automatically set to be consistent with that of the nodes in the cluster
        :type VpcId: str
        :param _Cni: Whether CNI is enabled for network plugin(s). Default value: enabled
        :type Cni: bool
        :param _KubeProxyMode: The network mode of service. This parameter is only applicable to ipvs+bpf mode.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type KubeProxyMode: str
        :param _ServiceCIDR: The IP range for service assignment. It cannot conflict with the VPC’s CIDR block nor the CIDR blocks of other clusters in the same VPC.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ServiceCIDR: str
        :param _Subnets: The container subnet associated with the cluster
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Subnets: list of str
        :param _IgnoreServiceCIDRConflict: Whether to ignore ServiceCIDR conflict errors. It is only valid in VPC-CNI mode. Default value: `false`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreServiceCIDRConflict: bool
        :param _IsDualStack: Whether it is a dual-stack cluster in VPC-CNI mode. Default value: `false`, which indicates it is not a dual-stack cluster.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IsDualStack: bool
        :param _Ipv6ServiceCIDR: It is used to automatically assign the IP ranges for the service.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ipv6ServiceCIDR: str
        :param _CiliumMode: Cluster Cilium Mode configuration
- clusterIP
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CiliumMode: str
        """
        self._ClusterCIDR = None
        self._IgnoreClusterCIDRConflict = None
        self._MaxNodePodNum = None
        self._MaxClusterServiceNum = None
        self._Ipvs = None
        self._VpcId = None
        self._Cni = None
        self._KubeProxyMode = None
        self._ServiceCIDR = None
        self._Subnets = None
        self._IgnoreServiceCIDRConflict = None
        self._IsDualStack = None
        self._Ipv6ServiceCIDR = None
        self._CiliumMode = None

    @property
    def ClusterCIDR(self):
        return self._ClusterCIDR

    @ClusterCIDR.setter
    def ClusterCIDR(self, ClusterCIDR):
        self._ClusterCIDR = ClusterCIDR

    @property
    def IgnoreClusterCIDRConflict(self):
        return self._IgnoreClusterCIDRConflict

    @IgnoreClusterCIDRConflict.setter
    def IgnoreClusterCIDRConflict(self, IgnoreClusterCIDRConflict):
        self._IgnoreClusterCIDRConflict = IgnoreClusterCIDRConflict

    @property
    def MaxNodePodNum(self):
        return self._MaxNodePodNum

    @MaxNodePodNum.setter
    def MaxNodePodNum(self, MaxNodePodNum):
        self._MaxNodePodNum = MaxNodePodNum

    @property
    def MaxClusterServiceNum(self):
        return self._MaxClusterServiceNum

    @MaxClusterServiceNum.setter
    def MaxClusterServiceNum(self, MaxClusterServiceNum):
        self._MaxClusterServiceNum = MaxClusterServiceNum

    @property
    def Ipvs(self):
        return self._Ipvs

    @Ipvs.setter
    def Ipvs(self, Ipvs):
        self._Ipvs = Ipvs

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Cni(self):
        return self._Cni

    @Cni.setter
    def Cni(self, Cni):
        self._Cni = Cni

    @property
    def KubeProxyMode(self):
        return self._KubeProxyMode

    @KubeProxyMode.setter
    def KubeProxyMode(self, KubeProxyMode):
        self._KubeProxyMode = KubeProxyMode

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR

    @property
    def Subnets(self):
        return self._Subnets

    @Subnets.setter
    def Subnets(self, Subnets):
        self._Subnets = Subnets

    @property
    def IgnoreServiceCIDRConflict(self):
        return self._IgnoreServiceCIDRConflict

    @IgnoreServiceCIDRConflict.setter
    def IgnoreServiceCIDRConflict(self, IgnoreServiceCIDRConflict):
        self._IgnoreServiceCIDRConflict = IgnoreServiceCIDRConflict

    @property
    def IsDualStack(self):
        return self._IsDualStack

    @IsDualStack.setter
    def IsDualStack(self, IsDualStack):
        self._IsDualStack = IsDualStack

    @property
    def Ipv6ServiceCIDR(self):
        return self._Ipv6ServiceCIDR

    @Ipv6ServiceCIDR.setter
    def Ipv6ServiceCIDR(self, Ipv6ServiceCIDR):
        self._Ipv6ServiceCIDR = Ipv6ServiceCIDR

    @property
    def CiliumMode(self):
        return self._CiliumMode

    @CiliumMode.setter
    def CiliumMode(self, CiliumMode):
        self._CiliumMode = CiliumMode


    def _deserialize(self, params):
        self._ClusterCIDR = params.get("ClusterCIDR")
        self._IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self._MaxNodePodNum = params.get("MaxNodePodNum")
        self._MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self._Ipvs = params.get("Ipvs")
        self._VpcId = params.get("VpcId")
        self._Cni = params.get("Cni")
        self._KubeProxyMode = params.get("KubeProxyMode")
        self._ServiceCIDR = params.get("ServiceCIDR")
        self._Subnets = params.get("Subnets")
        self._IgnoreServiceCIDRConflict = params.get("IgnoreServiceCIDRConflict")
        self._IsDualStack = params.get("IsDualStack")
        self._Ipv6ServiceCIDR = params.get("Ipv6ServiceCIDR")
        self._CiliumMode = params.get("CiliumMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterStatus(AbstractModel):
    """Cluster status information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterState: Cluster status
        :type ClusterState: str
        :param _ClusterInstanceState: Status of nodes in the cluster
        :type ClusterInstanceState: str
        :param _ClusterBMonitor: Indicates whether the monitoring service is enabled for the cluster
        :type ClusterBMonitor: bool
        :param _ClusterInitNodeNum: Number of cluster nodes being created. "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
        :type ClusterInitNodeNum: int
        :param _ClusterRunningNodeNum: Number of running nodes in the cluster. "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
        :type ClusterRunningNodeNum: int
        :param _ClusterFailedNodeNum: Number of abnormal nodes in the cluster.  "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
        :type ClusterFailedNodeNum: int
        :param _ClusterClosedNodeNum: Number of shutdown nodes in the cluster.  "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterClosedNodeNum: int
        :param _ClusterClosingNodeNum: Number of nodes being shut down in the cluster.  "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterClosingNodeNum: int
        :param _ClusterDeletionProtection: Indicates whether to enable cluster deletion protection
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterDeletionProtection: bool
        :param _ClusterAuditEnabled: Indicates whether the cluster is auditable
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterAuditEnabled: bool
        """
        self._ClusterId = None
        self._ClusterState = None
        self._ClusterInstanceState = None
        self._ClusterBMonitor = None
        self._ClusterInitNodeNum = None
        self._ClusterRunningNodeNum = None
        self._ClusterFailedNodeNum = None
        self._ClusterClosedNodeNum = None
        self._ClusterClosingNodeNum = None
        self._ClusterDeletionProtection = None
        self._ClusterAuditEnabled = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterState(self):
        return self._ClusterState

    @ClusterState.setter
    def ClusterState(self, ClusterState):
        self._ClusterState = ClusterState

    @property
    def ClusterInstanceState(self):
        return self._ClusterInstanceState

    @ClusterInstanceState.setter
    def ClusterInstanceState(self, ClusterInstanceState):
        self._ClusterInstanceState = ClusterInstanceState

    @property
    def ClusterBMonitor(self):
        return self._ClusterBMonitor

    @ClusterBMonitor.setter
    def ClusterBMonitor(self, ClusterBMonitor):
        self._ClusterBMonitor = ClusterBMonitor

    @property
    def ClusterInitNodeNum(self):
        return self._ClusterInitNodeNum

    @ClusterInitNodeNum.setter
    def ClusterInitNodeNum(self, ClusterInitNodeNum):
        self._ClusterInitNodeNum = ClusterInitNodeNum

    @property
    def ClusterRunningNodeNum(self):
        return self._ClusterRunningNodeNum

    @ClusterRunningNodeNum.setter
    def ClusterRunningNodeNum(self, ClusterRunningNodeNum):
        self._ClusterRunningNodeNum = ClusterRunningNodeNum

    @property
    def ClusterFailedNodeNum(self):
        return self._ClusterFailedNodeNum

    @ClusterFailedNodeNum.setter
    def ClusterFailedNodeNum(self, ClusterFailedNodeNum):
        self._ClusterFailedNodeNum = ClusterFailedNodeNum

    @property
    def ClusterClosedNodeNum(self):
        return self._ClusterClosedNodeNum

    @ClusterClosedNodeNum.setter
    def ClusterClosedNodeNum(self, ClusterClosedNodeNum):
        self._ClusterClosedNodeNum = ClusterClosedNodeNum

    @property
    def ClusterClosingNodeNum(self):
        return self._ClusterClosingNodeNum

    @ClusterClosingNodeNum.setter
    def ClusterClosingNodeNum(self, ClusterClosingNodeNum):
        self._ClusterClosingNodeNum = ClusterClosingNodeNum

    @property
    def ClusterDeletionProtection(self):
        return self._ClusterDeletionProtection

    @ClusterDeletionProtection.setter
    def ClusterDeletionProtection(self, ClusterDeletionProtection):
        self._ClusterDeletionProtection = ClusterDeletionProtection

    @property
    def ClusterAuditEnabled(self):
        return self._ClusterAuditEnabled

    @ClusterAuditEnabled.setter
    def ClusterAuditEnabled(self, ClusterAuditEnabled):
        self._ClusterAuditEnabled = ClusterAuditEnabled


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterState = params.get("ClusterState")
        self._ClusterInstanceState = params.get("ClusterInstanceState")
        self._ClusterBMonitor = params.get("ClusterBMonitor")
        self._ClusterInitNodeNum = params.get("ClusterInitNodeNum")
        self._ClusterRunningNodeNum = params.get("ClusterRunningNodeNum")
        self._ClusterFailedNodeNum = params.get("ClusterFailedNodeNum")
        self._ClusterClosedNodeNum = params.get("ClusterClosedNodeNum")
        self._ClusterClosingNodeNum = params.get("ClusterClosingNodeNum")
        self._ClusterDeletionProtection = params.get("ClusterDeletionProtection")
        self._ClusterAuditEnabled = params.get("ClusterAuditEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterVersion(AbstractModel):
    """Cluster version information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Versions: The list of cluster major version, such as 1.18.4
        :type Versions: list of str
        """
        self._ClusterId = None
        self._Versions = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Versions = params.get("Versions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonName(AbstractModel):
    """The CommonName in the certificate of the client corresponding to the user UIN

    """

    def __init__(self):
        r"""
        :param _SubaccountUin: User UIN
        :type SubaccountUin: str
        :param _CN: The CommonName in the certificate of the client corresponding to the sub-account
        :type CN: str
        """
        self._SubaccountUin = None
        self._CN = None

    @property
    def SubaccountUin(self):
        return self._SubaccountUin

    @SubaccountUin.setter
    def SubaccountUin(self, SubaccountUin):
        self._SubaccountUin = SubaccountUin

    @property
    def CN(self):
        return self._CN

    @CN.setter
    def CN(self, CN):
        self._CN = CN


    def _deserialize(self, params):
        self._SubaccountUin = params.get("SubaccountUin")
        self._CN = params.get("CN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupStorageLocationRequest(AbstractModel):
    """CreateBackupStorageLocation request structure.

    """

    def __init__(self):
        r"""
        :param _StorageRegion: Repository region, such as `ap-guangzhou`
        :type StorageRegion: str
        :param _Bucket: COS bucket name. For COS storage type, it must start with the prefix `tke-backup`.
        :type Bucket: str
        :param _Name: Backup repository name
        :type Name: str
        :param _Provider: The provider of storage service. It defaults to Tencent Cloud.
        :type Provider: str
        :param _Path: COS bucket path
        :type Path: str
        """
        self._StorageRegion = None
        self._Bucket = None
        self._Name = None
        self._Provider = None
        self._Path = None

    @property
    def StorageRegion(self):
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Provider(self):
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._StorageRegion = params.get("StorageRegion")
        self._Bucket = params.get("Bucket")
        self._Name = params.get("Name")
        self._Provider = params.get("Provider")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupStorageLocationResponse(AbstractModel):
    """CreateBackupStorageLocation response structure.

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


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SubnetId: The ID of the subnet where the cluster's port is located (only needs to be entered when the non-public network access is enabled, and must be within the subnet of the cluster's VPC). 
        :type SubnetId: str
        :param _IsExtranet: Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE).
        :type IsExtranet: bool
        :param _Domain: The domain name
        :type Domain: str
        :param _SecurityGroup: The security group in use, which must be passed in when public access is enabled.
        :type SecurityGroup: str
        :param _ExtensiveParameters: Parameters used to create a CLB in JSON format. It’s only required for public network access. Example: `{"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":"200"},"VipIsp":"","BandwidthPackageId":""}`. 
Parameters: 
`InternetAccessible.InternetChargeType`: `TRAFFIC_POSTPAID_BY_HOUR`, `BANDWIDTH_POSTPAID_BY_HOUR`, `InternetAccessible.BANDWIDTH_PACKAGE` (Bill by the bandwidth package) 
`InternetMaxBandwidthOut`: Outbound bandwidth cap in Mbps. Range: 0 - 2048. It defaults to 10. 
`VipIsp`: The VIP provider. Values: `CMCC` (China Mobile), `CTCC` (China Telecom), `CUCC` (China Unicom). If this parameter is not specified, BGP will be used by default. ISPs supported in a region can be queried with the `DescribeSingleIsp` API. If an ISP is specified, only bill-by-bandwidth-package (BANDWIDTH_PACKAGE) can be used as the network billing mode. 
`BandwidthPackageId`: Bandwidth package ID. If this parameter is specified, the network billing mode (`InternetAccessible.InternetChargeType`) will only support bill-by-bandwidth package (`BANDWIDTH_PACKAGE`).
        :type ExtensiveParameters: str
        """
        self._ClusterId = None
        self._SubnetId = None
        self._IsExtranet = None
        self._Domain = None
        self._SecurityGroup = None
        self._ExtensiveParameters = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def IsExtranet(self):
        return self._IsExtranet

    @IsExtranet.setter
    def IsExtranet(self, IsExtranet):
        self._IsExtranet = IsExtranet

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def ExtensiveParameters(self):
        return self._ExtensiveParameters

    @ExtensiveParameters.setter
    def ExtensiveParameters(self, ExtensiveParameters):
        self._ExtensiveParameters = ExtensiveParameters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SubnetId = params.get("SubnetId")
        self._IsExtranet = params.get("IsExtranet")
        self._Domain = params.get("Domain")
        self._SecurityGroup = params.get("SecurityGroup")
        self._ExtensiveParameters = params.get("ExtensiveParameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointResponse(AbstractModel):
    """CreateClusterEndpoint response structure.

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


class CreateClusterEndpointVipRequest(AbstractModel):
    """CreateClusterEndpointVip request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SecurityPolicies: Security policy opens single IP or CIDR to the Internet (for example: '192.168.1.0/24', with 'reject all' as the default).
        :type SecurityPolicies: list of str
        """
        self._ClusterId = None
        self._SecurityPolicies = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SecurityPolicies(self):
        return self._SecurityPolicies

    @SecurityPolicies.setter
    def SecurityPolicies(self, SecurityPolicies):
        self._SecurityPolicies = SecurityPolicies


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SecurityPolicies = params.get("SecurityPolicies")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip response structure.

    """

    def __init__(self):
        r"""
        :param _RequestFlowId: Request job's FlowId
        :type RequestFlowId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestFlowId = None
        self._RequestId = None

    @property
    def RequestFlowId(self):
        return self._RequestFlowId

    @RequestFlowId.setter
    def RequestFlowId(self, RequestFlowId):
        self._RequestFlowId = RequestFlowId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestFlowId = params.get("RequestFlowId")
        self._RequestId = params.get("RequestId")


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID. Enter the ClusterId field returned by the DescribeClusters API
        :type ClusterId: str
        :param _RunInstancePara: Pass-through parameter for CVM creation in the format of a JSON string. To ensure the idempotence of requests for adding cluster nodes, you need to add the ClientToken field in this parameter. For more information, see the documentation for [RunInstances](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API.
        :type RunInstancePara: str
        :param _InstanceAdvancedSettings: Additional parameter to be set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _SkipValidateOptions: Skips the specified verification. Valid values: GlobalRouteCIDRCheck, VpcCniCIDRCheck
        :type SkipValidateOptions: list of str
        """
        self._ClusterId = None
        self._RunInstancePara = None
        self._InstanceAdvancedSettings = None
        self._SkipValidateOptions = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RunInstancePara(self):
        return self._RunInstancePara

    @RunInstancePara.setter
    def RunInstancePara(self, RunInstancePara):
        self._RunInstancePara = RunInstancePara

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def SkipValidateOptions(self):
        return self._SkipValidateOptions

    @SkipValidateOptions.setter
    def SkipValidateOptions(self, SkipValidateOptions):
        self._SkipValidateOptions = SkipValidateOptions


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RunInstancePara = params.get("RunInstancePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self._SkipValidateOptions = params.get("SkipValidateOptions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: Instance ID
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


class CreateClusterNodePoolRequest(AbstractModel):
    """CreateClusterNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _AutoScalingGroupPara: AS group parameters. For details, see https://intl.cloud.tencent.com/document/product/377/20440?from_cn_redirect=1
        :type AutoScalingGroupPara: str
        :param _LaunchConfigurePara: Running parameters. For details, see https://intl.cloud.tencent.com/document/product/377/20447?from_cn_redirect=1
        :type LaunchConfigurePara: str
        :param _InstanceAdvancedSettings: Sample parameters
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _EnableAutoscale: Indicates whether to enable auto scaling
        :type EnableAutoscale: bool
        :param _Name: Node pool name
        :type Name: str
        :param _Labels: Labels
        :type Labels: list of Label
        :param _Taints: Taints
        :type Taints: list of Taint
        :param _ContainerRuntime: Node pool runtime type and version
        :type ContainerRuntime: str
        :param _RuntimeVersion: Runtime version
        :type RuntimeVersion: str
        :param _NodePoolOs: Node pool operating system (enter the image ID for a custom image, and enter the OS name for a public image)
        :type NodePoolOs: str
        :param _OsCustomizeType: Container image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
        :type OsCustomizeType: str
        :param _Tags: Resource tag
        :type Tags: list of Tag
        :param _DeletionProtection: Whether Deletion Protection is enabled
        :type DeletionProtection: bool
        """
        self._ClusterId = None
        self._AutoScalingGroupPara = None
        self._LaunchConfigurePara = None
        self._InstanceAdvancedSettings = None
        self._EnableAutoscale = None
        self._Name = None
        self._Labels = None
        self._Taints = None
        self._ContainerRuntime = None
        self._RuntimeVersion = None
        self._NodePoolOs = None
        self._OsCustomizeType = None
        self._Tags = None
        self._DeletionProtection = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AutoScalingGroupPara(self):
        return self._AutoScalingGroupPara

    @AutoScalingGroupPara.setter
    def AutoScalingGroupPara(self, AutoScalingGroupPara):
        self._AutoScalingGroupPara = AutoScalingGroupPara

    @property
    def LaunchConfigurePara(self):
        return self._LaunchConfigurePara

    @LaunchConfigurePara.setter
    def LaunchConfigurePara(self, LaunchConfigurePara):
        self._LaunchConfigurePara = LaunchConfigurePara

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def EnableAutoscale(self):
        return self._EnableAutoscale

    @EnableAutoscale.setter
    def EnableAutoscale(self, EnableAutoscale):
        self._EnableAutoscale = EnableAutoscale

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def ContainerRuntime(self):
        return self._ContainerRuntime

    @ContainerRuntime.setter
    def ContainerRuntime(self, ContainerRuntime):
        self._ContainerRuntime = ContainerRuntime

    @property
    def RuntimeVersion(self):
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def NodePoolOs(self):
        return self._NodePoolOs

    @NodePoolOs.setter
    def NodePoolOs(self, NodePoolOs):
        self._NodePoolOs = NodePoolOs

    @property
    def OsCustomizeType(self):
        return self._OsCustomizeType

    @OsCustomizeType.setter
    def OsCustomizeType(self, OsCustomizeType):
        self._OsCustomizeType = OsCustomizeType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AutoScalingGroupPara = params.get("AutoScalingGroupPara")
        self._LaunchConfigurePara = params.get("LaunchConfigurePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self._EnableAutoscale = params.get("EnableAutoscale")
        self._Name = params.get("Name")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        self._ContainerRuntime = params.get("ContainerRuntime")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._NodePoolOs = params.get("NodePoolOs")
        self._OsCustomizeType = params.get("OsCustomizeType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterNodePoolResponse(AbstractModel):
    """CreateClusterNodePool response structure.

    """

    def __init__(self):
        r"""
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodePoolId = None
        self._RequestId = None

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NodePoolId = params.get("NodePoolId")
        self._RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterCIDRSettings: Container networking configuration information for the cluster
        :type ClusterCIDRSettings: :class:`tencentcloud.tke.v20180525.models.ClusterCIDRSettings`
        :param _ClusterType: Cluster type. Managed cluster: MANAGED_CLUSTER; self-deployed cluster: INDEPENDENT_CLUSTER.
        :type ClusterType: str
        :param _RunInstancesForNode: Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the API for [creating a CVM instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1).
        :type RunInstancesForNode: list of RunInstancesForNode
        :param _ClusterBasicSettings: Basic configuration information of the cluster
        :type ClusterBasicSettings: :class:`tencentcloud.tke.v20180525.models.ClusterBasicSettings`
        :param _ClusterAdvancedSettings: Advanced configuration information of the cluster
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.ClusterAdvancedSettings`
        :param _InstanceAdvancedSettings: Advanced configuration information of the node
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _ExistedInstancesForNode: The configuration information for existing instances. All instances must be in the same VPC. Up to 100 instances are allowed in one VPC. Spot instances are not supported.
        :type ExistedInstancesForNode: list of ExistedInstancesForNode
        :param _InstanceDataDiskMountSettings: CVM type and the corresponding data disk mounting configuration information.
        :type InstanceDataDiskMountSettings: list of InstanceDataDiskMountSetting
        :param _ExtensionAddons: Information of the add-on to be installed
        :type ExtensionAddons: list of ExtensionAddon
        """
        self._ClusterCIDRSettings = None
        self._ClusterType = None
        self._RunInstancesForNode = None
        self._ClusterBasicSettings = None
        self._ClusterAdvancedSettings = None
        self._InstanceAdvancedSettings = None
        self._ExistedInstancesForNode = None
        self._InstanceDataDiskMountSettings = None
        self._ExtensionAddons = None

    @property
    def ClusterCIDRSettings(self):
        return self._ClusterCIDRSettings

    @ClusterCIDRSettings.setter
    def ClusterCIDRSettings(self, ClusterCIDRSettings):
        self._ClusterCIDRSettings = ClusterCIDRSettings

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType

    @property
    def RunInstancesForNode(self):
        return self._RunInstancesForNode

    @RunInstancesForNode.setter
    def RunInstancesForNode(self, RunInstancesForNode):
        self._RunInstancesForNode = RunInstancesForNode

    @property
    def ClusterBasicSettings(self):
        return self._ClusterBasicSettings

    @ClusterBasicSettings.setter
    def ClusterBasicSettings(self, ClusterBasicSettings):
        self._ClusterBasicSettings = ClusterBasicSettings

    @property
    def ClusterAdvancedSettings(self):
        return self._ClusterAdvancedSettings

    @ClusterAdvancedSettings.setter
    def ClusterAdvancedSettings(self, ClusterAdvancedSettings):
        self._ClusterAdvancedSettings = ClusterAdvancedSettings

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def ExistedInstancesForNode(self):
        return self._ExistedInstancesForNode

    @ExistedInstancesForNode.setter
    def ExistedInstancesForNode(self, ExistedInstancesForNode):
        self._ExistedInstancesForNode = ExistedInstancesForNode

    @property
    def InstanceDataDiskMountSettings(self):
        return self._InstanceDataDiskMountSettings

    @InstanceDataDiskMountSettings.setter
    def InstanceDataDiskMountSettings(self, InstanceDataDiskMountSettings):
        self._InstanceDataDiskMountSettings = InstanceDataDiskMountSettings

    @property
    def ExtensionAddons(self):
        return self._ExtensionAddons

    @ExtensionAddons.setter
    def ExtensionAddons(self, ExtensionAddons):
        self._ExtensionAddons = ExtensionAddons


    def _deserialize(self, params):
        if params.get("ClusterCIDRSettings") is not None:
            self._ClusterCIDRSettings = ClusterCIDRSettings()
            self._ClusterCIDRSettings._deserialize(params.get("ClusterCIDRSettings"))
        self._ClusterType = params.get("ClusterType")
        if params.get("RunInstancesForNode") is not None:
            self._RunInstancesForNode = []
            for item in params.get("RunInstancesForNode"):
                obj = RunInstancesForNode()
                obj._deserialize(item)
                self._RunInstancesForNode.append(obj)
        if params.get("ClusterBasicSettings") is not None:
            self._ClusterBasicSettings = ClusterBasicSettings()
            self._ClusterBasicSettings._deserialize(params.get("ClusterBasicSettings"))
        if params.get("ClusterAdvancedSettings") is not None:
            self._ClusterAdvancedSettings = ClusterAdvancedSettings()
            self._ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("ExistedInstancesForNode") is not None:
            self._ExistedInstancesForNode = []
            for item in params.get("ExistedInstancesForNode"):
                obj = ExistedInstancesForNode()
                obj._deserialize(item)
                self._ExistedInstancesForNode.append(obj)
        if params.get("InstanceDataDiskMountSettings") is not None:
            self._InstanceDataDiskMountSettings = []
            for item in params.get("InstanceDataDiskMountSettings"):
                obj = InstanceDataDiskMountSetting()
                obj._deserialize(item)
                self._InstanceDataDiskMountSettings.append(obj)
        if params.get("ExtensionAddons") is not None:
            self._ExtensionAddons = []
            for item in params.get("ExtensionAddons"):
                obj = ExtensionAddon()
                obj._deserialize(item)
                self._ExtensionAddons.append(obj)
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


class CreateClusterRouteTableRequest(AbstractModel):
    """CreateClusterRouteTable request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableName: Route table name
        :type RouteTableName: str
        :param _RouteTableCidrBlock: Route table CIDR
        :type RouteTableCidrBlock: str
        :param _VpcId: VPC bound to the route table
        :type VpcId: str
        :param _IgnoreClusterCidrConflict: Whether to ignore CIDR conflicts
        :type IgnoreClusterCidrConflict: int
        """
        self._RouteTableName = None
        self._RouteTableCidrBlock = None
        self._VpcId = None
        self._IgnoreClusterCidrConflict = None

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def RouteTableCidrBlock(self):
        return self._RouteTableCidrBlock

    @RouteTableCidrBlock.setter
    def RouteTableCidrBlock(self, RouteTableCidrBlock):
        self._RouteTableCidrBlock = RouteTableCidrBlock

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def IgnoreClusterCidrConflict(self):
        return self._IgnoreClusterCidrConflict

    @IgnoreClusterCidrConflict.setter
    def IgnoreClusterCidrConflict(self, IgnoreClusterCidrConflict):
        self._IgnoreClusterCidrConflict = IgnoreClusterCidrConflict


    def _deserialize(self, params):
        self._RouteTableName = params.get("RouteTableName")
        self._RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self._VpcId = params.get("VpcId")
        self._IgnoreClusterCidrConflict = params.get("IgnoreClusterCidrConflict")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRouteTableResponse(AbstractModel):
    """CreateClusterRouteTable response structure.

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


class CreateClusterVirtualNodePoolRequest(AbstractModel):
    """CreateClusterVirtualNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Name: Node pool name
        :type Name: str
        :param _SubnetIds: List of subnet IDs
        :type SubnetIds: list of str
        :param _SecurityGroupIds: List of security group IDs
        :type SecurityGroupIds: list of str
        :param _Labels: Virtual node labels
        :type Labels: list of Label
        :param _Taints: Virtual node taint
        :type Taints: list of Taint
        :param _VirtualNodes: List of nodes
        :type VirtualNodes: list of VirtualNodeSpec
        :param _DeletionProtection: Setting of deletion protection
        :type DeletionProtection: bool
        :param _OS: Node pool OS:
- `linux` (default value)
- `windows`
        :type OS: str
        """
        self._ClusterId = None
        self._Name = None
        self._SubnetIds = None
        self._SecurityGroupIds = None
        self._Labels = None
        self._Taints = None
        self._VirtualNodes = None
        self._DeletionProtection = None
        self._OS = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def VirtualNodes(self):
        return self._VirtualNodes

    @VirtualNodes.setter
    def VirtualNodes(self, VirtualNodes):
        self._VirtualNodes = VirtualNodes

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def OS(self):
        return self._OS

    @OS.setter
    def OS(self, OS):
        self._OS = OS


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Name = params.get("Name")
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        if params.get("VirtualNodes") is not None:
            self._VirtualNodes = []
            for item in params.get("VirtualNodes"):
                obj = VirtualNodeSpec()
                obj._deserialize(item)
                self._VirtualNodes.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._OS = params.get("OS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterVirtualNodePoolResponse(AbstractModel):
    """CreateClusterVirtualNodePool response structure.

    """

    def __init__(self):
        r"""
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodePoolId = None
        self._RequestId = None

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NodePoolId = params.get("NodePoolId")
        self._RequestId = params.get("RequestId")


class CreateClusterVirtualNodeRequest(AbstractModel):
    """CreateClusterVirtualNode request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool
        :type NodePoolId: str
        :param _SubnetId: Subnet
        :type SubnetId: str
        :param _SubnetIds: List of subnet IDs (this parameter and `SubnetId` are mutually exclusive)
        :type SubnetIds: list of str
        :param _VirtualNodes: List of virtual nodes
        :type VirtualNodes: list of VirtualNodeSpec
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._SubnetId = None
        self._SubnetIds = None
        self._VirtualNodes = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def VirtualNodes(self):
        return self._VirtualNodes

    @VirtualNodes.setter
    def VirtualNodes(self, VirtualNodes):
        self._VirtualNodes = VirtualNodes


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetIds = params.get("SubnetIds")
        if params.get("VirtualNodes") is not None:
            self._VirtualNodes = []
            for item in params.get("VirtualNodes"):
                obj = VirtualNodeSpec()
                obj._deserialize(item)
                self._VirtualNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterVirtualNodeResponse(AbstractModel):
    """CreateClusterVirtualNode response structure.

    """

    def __init__(self):
        r"""
        :param _NodeName: Virtual node name
        :type NodeName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodeName = None
        self._RequestId = None

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NodeName = params.get("NodeName")
        self._RequestId = params.get("RequestId")


class CreateECMInstancesRequest(AbstractModel):
    """CreateECMInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _ModuleId: Module ID
        :type ModuleId: str
        :param _ZoneInstanceCountISPSet: Instance AZ, number of instances and ISP
        :type ZoneInstanceCountISPSet: list of ECMZoneInstanceCountISP
        :param _Password: Password
        :type Password: str
        :param _InternetMaxBandwidthOut: Public network bandwidth
        :type InternetMaxBandwidthOut: int
        :param _ImageId: Image ID
        :type ImageId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _HostName: Host name
        :type HostName: str
        :param _EnhancedService: Enhanced service (including CWP and Cloud Monitoring)
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.ECMEnhancedService`
        :param _UserData: Custom script
        :type UserData: str
        :param _External: Instance extension information
        :type External: str
        :param _SecurityGroupIds: Security group of the instance
        :type SecurityGroupIds: list of str
        """
        self._ClusterID = None
        self._ModuleId = None
        self._ZoneInstanceCountISPSet = None
        self._Password = None
        self._InternetMaxBandwidthOut = None
        self._ImageId = None
        self._InstanceName = None
        self._HostName = None
        self._EnhancedService = None
        self._UserData = None
        self._External = None
        self._SecurityGroupIds = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def ModuleId(self):
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ZoneInstanceCountISPSet(self):
        return self._ZoneInstanceCountISPSet

    @ZoneInstanceCountISPSet.setter
    def ZoneInstanceCountISPSet(self, ZoneInstanceCountISPSet):
        self._ZoneInstanceCountISPSet = ZoneInstanceCountISPSet

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

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
    def External(self):
        return self._External

    @External.setter
    def External(self, External):
        self._External = External

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._ModuleId = params.get("ModuleId")
        if params.get("ZoneInstanceCountISPSet") is not None:
            self._ZoneInstanceCountISPSet = []
            for item in params.get("ZoneInstanceCountISPSet"):
                obj = ECMZoneInstanceCountISP()
                obj._deserialize(item)
                self._ZoneInstanceCountISPSet.append(obj)
        self._Password = params.get("Password")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._ImageId = params.get("ImageId")
        self._InstanceName = params.get("InstanceName")
        self._HostName = params.get("HostName")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = ECMEnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._UserData = params.get("UserData")
        self._External = params.get("External")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateECMInstancesResponse(AbstractModel):
    """CreateECMInstances response structure.

    """

    def __init__(self):
        r"""
        :param _EcmIdSet: ECM ID list
        :type EcmIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EcmIdSet = None
        self._RequestId = None

    @property
    def EcmIdSet(self):
        return self._EcmIdSet

    @EcmIdSet.setter
    def EcmIdSet(self, EcmIdSet):
        self._EcmIdSet = EcmIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EcmIdSet = params.get("EcmIdSet")
        self._RequestId = params.get("RequestId")


class CreateEdgeCVMInstancesRequest(AbstractModel):
    """CreateEdgeCVMInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _RunInstancePara: Pass-through parameter for CVM creation in the format of a JSON string. To ensure the idempotency of requests for adding cluster nodes, you need to add the `ClientToken` field in this parameter. For more information, see the documentation for [RunInstances](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API.
        :type RunInstancePara: str
        :param _CvmRegion: Region of the CVM instances to create
        :type CvmRegion: str
        :param _CvmCount: Quantity of CVM instances to create
        :type CvmCount: int
        :param _External: Instance extension information
        :type External: str
        :param _UserScript: Custom script
        :type UserScript: str
        :param _EnableEni: Whether to enable ENI
        :type EnableEni: bool
        """
        self._ClusterID = None
        self._RunInstancePara = None
        self._CvmRegion = None
        self._CvmCount = None
        self._External = None
        self._UserScript = None
        self._EnableEni = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def RunInstancePara(self):
        return self._RunInstancePara

    @RunInstancePara.setter
    def RunInstancePara(self, RunInstancePara):
        self._RunInstancePara = RunInstancePara

    @property
    def CvmRegion(self):
        return self._CvmRegion

    @CvmRegion.setter
    def CvmRegion(self, CvmRegion):
        self._CvmRegion = CvmRegion

    @property
    def CvmCount(self):
        return self._CvmCount

    @CvmCount.setter
    def CvmCount(self, CvmCount):
        self._CvmCount = CvmCount

    @property
    def External(self):
        return self._External

    @External.setter
    def External(self, External):
        self._External = External

    @property
    def UserScript(self):
        return self._UserScript

    @UserScript.setter
    def UserScript(self, UserScript):
        self._UserScript = UserScript

    @property
    def EnableEni(self):
        return self._EnableEni

    @EnableEni.setter
    def EnableEni(self, EnableEni):
        self._EnableEni = EnableEni


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._RunInstancePara = params.get("RunInstancePara")
        self._CvmRegion = params.get("CvmRegion")
        self._CvmCount = params.get("CvmCount")
        self._External = params.get("External")
        self._UserScript = params.get("UserScript")
        self._EnableEni = params.get("EnableEni")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeCVMInstancesResponse(AbstractModel):
    """CreateEdgeCVMInstances response structure.

    """

    def __init__(self):
        r"""
        :param _CvmIdSet: List of CVM IDs
        :type CvmIdSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CvmIdSet = None
        self._RequestId = None

    @property
    def CvmIdSet(self):
        return self._CvmIdSet

    @CvmIdSet.setter
    def CvmIdSet(self, CvmIdSet):
        self._CvmIdSet = CvmIdSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CvmIdSet = params.get("CvmIdSet")
        self._RequestId = params.get("RequestId")


class CreateEdgeLogConfigRequest(AbstractModel):
    """CreateEdgeLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _LogConfig: Log collection configuration in json form
        :type LogConfig: str
        :param _LogsetId: CLS logset ID
        :type LogsetId: str
        """
        self._ClusterId = None
        self._LogConfig = None
        self._LogsetId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def LogConfig(self):
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._LogConfig = params.get("LogConfig")
        self._LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeLogConfigResponse(AbstractModel):
    """CreateEdgeLogConfig response structure.

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


class CreatePrometheusAlertRuleRequest(AbstractModel):
    """CreatePrometheusAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AlertRule: Alarm configurations
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`
        """
        self._InstanceId = None
        self._AlertRule = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertRule(self):
        return self._AlertRule

    @AlertRule.setter
    def AlertRule(self, AlertRule):
        self._AlertRule = AlertRule


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self._AlertRule = PrometheusAlertRuleDetail()
            self._AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAlertRuleResponse(AbstractModel):
    """CreatePrometheusAlertRule response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Alarm ID
        :type Id: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateTKEEdgeClusterRequest(AbstractModel):
    """CreateTKEEdgeCluster request structure.

    """

    def __init__(self):
        r"""
        :param _K8SVersion: 
        :type K8SVersion: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _PodCIDR: Cluster Pod CIDR block
        :type PodCIDR: str
        :param _ServiceCIDR: Cluster service CIDR block
        :type ServiceCIDR: str
        :param _ClusterDesc: Cluster description
        :type ClusterDesc: str
        :param _ClusterAdvancedSettings: Cluster advanced settings
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.EdgeClusterAdvancedSettings`
        :param _MaxNodePodNum: Maximum number of Pods on the node
        :type MaxNodePodNum: int
        :param _PublicLB: Public LB of the TKE Edge cluster
        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.EdgeClusterPublicLB`
        :param _ClusterLevel: Cluster specification level
        :type ClusterLevel: str
        :param _AutoUpgradeClusterLevel: Whether auto upgrade is supported
        :type AutoUpgradeClusterLevel: bool
        :param _ChargeType: Cluster billing mode
        :type ChargeType: str
        :param _EdgeVersion: Edge cluster version. It is the set of versions of all cluster components.
        :type EdgeVersion: str
        :param _RegistryPrefix: Prefix of the image registry of an edge component
        :type RegistryPrefix: str
        """
        self._K8SVersion = None
        self._VpcId = None
        self._ClusterName = None
        self._PodCIDR = None
        self._ServiceCIDR = None
        self._ClusterDesc = None
        self._ClusterAdvancedSettings = None
        self._MaxNodePodNum = None
        self._PublicLB = None
        self._ClusterLevel = None
        self._AutoUpgradeClusterLevel = None
        self._ChargeType = None
        self._EdgeVersion = None
        self._RegistryPrefix = None

    @property
    def K8SVersion(self):
        return self._K8SVersion

    @K8SVersion.setter
    def K8SVersion(self, K8SVersion):
        self._K8SVersion = K8SVersion

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def PodCIDR(self):
        return self._PodCIDR

    @PodCIDR.setter
    def PodCIDR(self, PodCIDR):
        self._PodCIDR = PodCIDR

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR

    @property
    def ClusterDesc(self):
        return self._ClusterDesc

    @ClusterDesc.setter
    def ClusterDesc(self, ClusterDesc):
        self._ClusterDesc = ClusterDesc

    @property
    def ClusterAdvancedSettings(self):
        return self._ClusterAdvancedSettings

    @ClusterAdvancedSettings.setter
    def ClusterAdvancedSettings(self, ClusterAdvancedSettings):
        self._ClusterAdvancedSettings = ClusterAdvancedSettings

    @property
    def MaxNodePodNum(self):
        return self._MaxNodePodNum

    @MaxNodePodNum.setter
    def MaxNodePodNum(self, MaxNodePodNum):
        self._MaxNodePodNum = MaxNodePodNum

    @property
    def PublicLB(self):
        return self._PublicLB

    @PublicLB.setter
    def PublicLB(self, PublicLB):
        self._PublicLB = PublicLB

    @property
    def ClusterLevel(self):
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel

    @property
    def AutoUpgradeClusterLevel(self):
        return self._AutoUpgradeClusterLevel

    @AutoUpgradeClusterLevel.setter
    def AutoUpgradeClusterLevel(self, AutoUpgradeClusterLevel):
        self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def EdgeVersion(self):
        return self._EdgeVersion

    @EdgeVersion.setter
    def EdgeVersion(self, EdgeVersion):
        self._EdgeVersion = EdgeVersion

    @property
    def RegistryPrefix(self):
        return self._RegistryPrefix

    @RegistryPrefix.setter
    def RegistryPrefix(self, RegistryPrefix):
        self._RegistryPrefix = RegistryPrefix


    def _deserialize(self, params):
        self._K8SVersion = params.get("K8SVersion")
        self._VpcId = params.get("VpcId")
        self._ClusterName = params.get("ClusterName")
        self._PodCIDR = params.get("PodCIDR")
        self._ServiceCIDR = params.get("ServiceCIDR")
        self._ClusterDesc = params.get("ClusterDesc")
        if params.get("ClusterAdvancedSettings") is not None:
            self._ClusterAdvancedSettings = EdgeClusterAdvancedSettings()
            self._ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        self._MaxNodePodNum = params.get("MaxNodePodNum")
        if params.get("PublicLB") is not None:
            self._PublicLB = EdgeClusterPublicLB()
            self._PublicLB._deserialize(params.get("PublicLB"))
        self._ClusterLevel = params.get("ClusterLevel")
        self._AutoUpgradeClusterLevel = params.get("AutoUpgradeClusterLevel")
        self._ChargeType = params.get("ChargeType")
        self._EdgeVersion = params.get("EdgeVersion")
        self._RegistryPrefix = params.get("RegistryPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTKEEdgeClusterResponse(AbstractModel):
    """CreateTKEEdgeCluster response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: TKE Edge cluster ID
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


class CustomDriver(AbstractModel):
    """Custom driver information

    """

    def __init__(self):
        r"""
        :param _Address: URL of custom GPU driver address
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Address: str
        """
        self._Address = None

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address


    def _deserialize(self, params):
        self._Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataDisk(AbstractModel):
    """Described the configuration and information of k8s node data disk.

    """

    def __init__(self):
        r"""
        :param _DiskType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param _FileSystem: File system (ext3/ext4/xfs)
Note: This field may return null, indicating that no valid value was found.
        :type FileSystem: str
        :param _DiskSize: Disk size (G)
Note: This field may return null, indicating that no valid value was found.
        :type DiskSize: int
        :param _AutoFormatAndMount: Whether the disk is auto-formatted and mounted
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AutoFormatAndMount: bool
        :param _MountTarget: Mounting directory
Note: This field may return null, indicating that no valid value was found.
        :type MountTarget: str
        :param _DiskPartition: Mounted device name or partition name (only required when adding an existing node)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DiskPartition: str
        """
        self._DiskType = None
        self._FileSystem = None
        self._DiskSize = None
        self._AutoFormatAndMount = None
        self._MountTarget = None
        self._DiskPartition = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def AutoFormatAndMount(self):
        return self._AutoFormatAndMount

    @AutoFormatAndMount.setter
    def AutoFormatAndMount(self, AutoFormatAndMount):
        self._AutoFormatAndMount = AutoFormatAndMount

    @property
    def MountTarget(self):
        return self._MountTarget

    @MountTarget.setter
    def MountTarget(self, MountTarget):
        self._MountTarget = MountTarget

    @property
    def DiskPartition(self):
        return self._DiskPartition

    @DiskPartition.setter
    def DiskPartition(self, DiskPartition):
        self._DiskPartition = DiskPartition


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._FileSystem = params.get("FileSystem")
        self._DiskSize = params.get("DiskSize")
        self._AutoFormatAndMount = params.get("AutoFormatAndMount")
        self._MountTarget = params.get("MountTarget")
        self._DiskPartition = params.get("DiskPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupStorageLocationRequest(AbstractModel):
    """DeleteBackupStorageLocation request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Backup repository name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupStorageLocationResponse(AbstractModel):
    """DeleteBackupStorageLocation response structure.

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


class DeleteClusterAsGroupsRequest(AbstractModel):
    """DeleteClusterAsGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The cluster ID, obtained through the [DescribeClusters](https://intl.cloud.tencent.com/document/api/457/31862?from_cn_redirect=1) API.
        :type ClusterId: str
        :param _AutoScalingGroupIds: Cluster scaling group ID list
        :type AutoScalingGroupIds: list of str
        :param _KeepInstance: Whether to keep nodes in the scaling group. Default to **false** (not keep)
        :type KeepInstance: bool
        """
        self._ClusterId = None
        self._AutoScalingGroupIds = None
        self._KeepInstance = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds

    @property
    def KeepInstance(self):
        return self._KeepInstance

    @KeepInstance.setter
    def KeepInstance(self, KeepInstance):
        self._KeepInstance = KeepInstance


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self._KeepInstance = params.get("KeepInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterAsGroupsResponse(AbstractModel):
    """DeleteClusterAsGroups response structure.

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


class DeleteClusterEndpointRequest(AbstractModel):
    """DeleteClusterEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _IsExtranet: Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE).
        :type IsExtranet: bool
        """
        self._ClusterId = None
        self._IsExtranet = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IsExtranet(self):
        return self._IsExtranet

    @IsExtranet.setter
    def IsExtranet(self, IsExtranet):
        self._IsExtranet = IsExtranet


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._IsExtranet = params.get("IsExtranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterEndpointResponse(AbstractModel):
    """DeleteClusterEndpoint response structure.

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


class DeleteClusterEndpointVipRequest(AbstractModel):
    """DeleteClusterEndpointVip request structure.

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
        


class DeleteClusterEndpointVipResponse(AbstractModel):
    """DeleteClusterEndpointVip response structure.

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


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: List of Instance IDs
        :type InstanceIds: list of str
        :param _InstanceDeleteMode: Policy used to delete an instance in the cluster: `terminate` (terminates the instance. Only available for pay-as-you-go CVMs); `retain` (only removes it from the cluster. The instance will be retained.)
        :type InstanceDeleteMode: str
        :param _ForceDelete: Whether or not there is forced deletion (when a node is initialized, the parameters can be specified as TRUE)
        :type ForceDelete: bool
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._InstanceDeleteMode = None
        self._ForceDelete = None

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
    def InstanceDeleteMode(self):
        return self._InstanceDeleteMode

    @InstanceDeleteMode.setter
    def InstanceDeleteMode(self, InstanceDeleteMode):
        self._InstanceDeleteMode = InstanceDeleteMode

    @property
    def ForceDelete(self):
        return self._ForceDelete

    @ForceDelete.setter
    def ForceDelete(self, ForceDelete):
        self._ForceDelete = ForceDelete


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceDeleteMode = params.get("InstanceDeleteMode")
        self._ForceDelete = params.get("ForceDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances response structure.

    """

    def __init__(self):
        r"""
        :param _SuccInstanceIds: IDs of deleted instances
        :type SuccInstanceIds: list of str
        :param _FailedInstanceIds: IDs of instances failed to be deleted
        :type FailedInstanceIds: list of str
        :param _NotFoundInstanceIds: IDs of instances that cannot be found
        :type NotFoundInstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccInstanceIds = None
        self._FailedInstanceIds = None
        self._NotFoundInstanceIds = None
        self._RequestId = None

    @property
    def SuccInstanceIds(self):
        return self._SuccInstanceIds

    @SuccInstanceIds.setter
    def SuccInstanceIds(self, SuccInstanceIds):
        self._SuccInstanceIds = SuccInstanceIds

    @property
    def FailedInstanceIds(self):
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def NotFoundInstanceIds(self):
        return self._NotFoundInstanceIds

    @NotFoundInstanceIds.setter
    def NotFoundInstanceIds(self, NotFoundInstanceIds):
        self._NotFoundInstanceIds = NotFoundInstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccInstanceIds = params.get("SuccInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._NotFoundInstanceIds = params.get("NotFoundInstanceIds")
        self._RequestId = params.get("RequestId")


class DeleteClusterNodePoolRequest(AbstractModel):
    """DeleteClusterNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ClusterId of a node pool
        :type ClusterId: str
        :param _NodePoolIds: IDs of node pools to delete
        :type NodePoolIds: list of str
        :param _KeepInstance: Indicates whether nodes in a node pool are retained when the node pool is deleted. (The nodes are removed from the cluster. However, the corresponding instances will not be terminated.)
        :type KeepInstance: bool
        """
        self._ClusterId = None
        self._NodePoolIds = None
        self._KeepInstance = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolIds(self):
        return self._NodePoolIds

    @NodePoolIds.setter
    def NodePoolIds(self, NodePoolIds):
        self._NodePoolIds = NodePoolIds

    @property
    def KeepInstance(self):
        return self._KeepInstance

    @KeepInstance.setter
    def KeepInstance(self, KeepInstance):
        self._KeepInstance = KeepInstance


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolIds = params.get("NodePoolIds")
        self._KeepInstance = params.get("KeepInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterNodePoolResponse(AbstractModel):
    """DeleteClusterNodePool response structure.

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


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceDeleteMode: Policy used to delete an instance in the cluster: terminate (terminates the instance. Only available for instances on pay-as-you-go CVMs); retain (only removes it from the cluster. The instance will be retained.)
        :type InstanceDeleteMode: str
        :param _ResourceDeleteOptions: Specifies the policy to deal with resources in the cluster when the cluster is deleted. It only supports CBS now. The default policy is to retain CBS disks.
        :type ResourceDeleteOptions: list of ResourceDeleteOption
        """
        self._ClusterId = None
        self._InstanceDeleteMode = None
        self._ResourceDeleteOptions = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def InstanceDeleteMode(self):
        return self._InstanceDeleteMode

    @InstanceDeleteMode.setter
    def InstanceDeleteMode(self, InstanceDeleteMode):
        self._InstanceDeleteMode = InstanceDeleteMode

    @property
    def ResourceDeleteOptions(self):
        return self._ResourceDeleteOptions

    @ResourceDeleteOptions.setter
    def ResourceDeleteOptions(self, ResourceDeleteOptions):
        self._ResourceDeleteOptions = ResourceDeleteOptions


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceDeleteMode = params.get("InstanceDeleteMode")
        if params.get("ResourceDeleteOptions") is not None:
            self._ResourceDeleteOptions = []
            for item in params.get("ResourceDeleteOptions"):
                obj = ResourceDeleteOption()
                obj._deserialize(item)
                self._ResourceDeleteOptions.append(obj)
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


class DeleteClusterRouteRequest(AbstractModel):
    """DeleteClusterRoute request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableName: Route table name.
        :type RouteTableName: str
        :param _GatewayIp: Next hop address.
        :type GatewayIp: str
        :param _DestinationCidrBlock: Destination CIDR.
        :type DestinationCidrBlock: str
        """
        self._RouteTableName = None
        self._GatewayIp = None
        self._DestinationCidrBlock = None

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def GatewayIp(self):
        return self._GatewayIp

    @GatewayIp.setter
    def GatewayIp(self, GatewayIp):
        self._GatewayIp = GatewayIp

    @property
    def DestinationCidrBlock(self):
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock


    def _deserialize(self, params):
        self._RouteTableName = params.get("RouteTableName")
        self._GatewayIp = params.get("GatewayIp")
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteResponse(AbstractModel):
    """DeleteClusterRoute response structure.

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


class DeleteClusterRouteTableRequest(AbstractModel):
    """DeleteClusterRouteTable request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableName: Route table name
        :type RouteTableName: str
        """
        self._RouteTableName = None

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName


    def _deserialize(self, params):
        self._RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteTableResponse(AbstractModel):
    """DeleteClusterRouteTable response structure.

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


class DeleteClusterVirtualNodePoolRequest(AbstractModel):
    """DeleteClusterVirtualNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolIds: List of virtual node pool IDs
        :type NodePoolIds: list of str
        :param _Force: Whether to forcibly delete the nodes with pods. Values: `true`, `false`.
        :type Force: bool
        """
        self._ClusterId = None
        self._NodePoolIds = None
        self._Force = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolIds(self):
        return self._NodePoolIds

    @NodePoolIds.setter
    def NodePoolIds(self, NodePoolIds):
        self._NodePoolIds = NodePoolIds

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolIds = params.get("NodePoolIds")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterVirtualNodePoolResponse(AbstractModel):
    """DeleteClusterVirtualNodePool response structure.

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


class DeleteClusterVirtualNodeRequest(AbstractModel):
    """DeleteClusterVirtualNode request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodeNames: List of virtual nodes
        :type NodeNames: list of str
        :param _Force: Whether to forcibly delete running pods in the virtual node. Values: `true`, `false`.
        :type Force: bool
        """
        self._ClusterId = None
        self._NodeNames = None
        self._Force = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodeNames(self):
        return self._NodeNames

    @NodeNames.setter
    def NodeNames(self, NodeNames):
        self._NodeNames = NodeNames

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodeNames = params.get("NodeNames")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterVirtualNodeResponse(AbstractModel):
    """DeleteClusterVirtualNode response structure.

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


class DeleteECMInstancesRequest(AbstractModel):
    """DeleteECMInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _EcmIdSet: IDs of ECMs to be deleted
        :type EcmIdSet: list of str
        """
        self._ClusterID = None
        self._EcmIdSet = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def EcmIdSet(self):
        return self._EcmIdSet

    @EcmIdSet.setter
    def EcmIdSet(self, EcmIdSet):
        self._EcmIdSet = EcmIdSet


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._EcmIdSet = params.get("EcmIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteECMInstancesResponse(AbstractModel):
    """DeleteECMInstances response structure.

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


class DeleteEdgeCVMInstancesRequest(AbstractModel):
    """DeleteEdgeCVMInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _CvmIdSet: IDs of CVMs to be deleted
        :type CvmIdSet: list of str
        """
        self._ClusterID = None
        self._CvmIdSet = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def CvmIdSet(self):
        return self._CvmIdSet

    @CvmIdSet.setter
    def CvmIdSet(self, CvmIdSet):
        self._CvmIdSet = CvmIdSet


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._CvmIdSet = params.get("CvmIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeCVMInstancesResponse(AbstractModel):
    """DeleteEdgeCVMInstances response structure.

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


class DeleteEdgeClusterInstancesRequest(AbstractModel):
    """DeleteEdgeClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _InstanceIds: Array of instance IDs to be deleted
        :type InstanceIds: list of str
        """
        self._ClusterId = None
        self._InstanceIds = None

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeClusterInstancesResponse(AbstractModel):
    """DeleteEdgeClusterInstances response structure.

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


class DeletePrometheusAlertRuleRequest(AbstractModel):
    """DeletePrometheusAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AlertIds: The ID list of alarm rules
        :type AlertIds: list of str
        """
        self._InstanceId = None
        self._AlertIds = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertIds(self):
        return self._AlertIds

    @AlertIds.setter
    def AlertIds(self, AlertIds):
        self._AlertIds = AlertIds


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AlertIds = params.get("AlertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusAlertRuleResponse(AbstractModel):
    """DeletePrometheusAlertRule response structure.

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


class DeleteTKEEdgeClusterRequest(AbstractModel):
    """DeleteTKEEdgeCluster request structure.

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
        


class DeleteTKEEdgeClusterResponse(AbstractModel):
    """DeleteTKEEdgeCluster response structure.

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


class DescribeAvailableClusterVersionRequest(AbstractModel):
    """DescribeAvailableClusterVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterIds: List of cluster IDs
        :type ClusterIds: list of str
        """
        self._ClusterId = None
        self._ClusterIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableClusterVersionResponse(AbstractModel):
    """DescribeAvailableClusterVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Versions: Upgradable cluster version
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Versions: list of str
        :param _Clusters: Cluster information
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Clusters: list of ClusterVersion
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Versions = None
        self._Clusters = None
        self._RequestId = None

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

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
        self._Versions = params.get("Versions")
        if params.get("Clusters") is not None:
            self._Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterVersion()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAvailableTKEEdgeVersionRequest(AbstractModel):
    """DescribeAvailableTKEEdgeVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: You can enter the `ClusterId` to query the current and latest versions of all cluster components.
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
        


class DescribeAvailableTKEEdgeVersionResponse(AbstractModel):
    """DescribeAvailableTKEEdgeVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Versions: Version list
        :type Versions: list of str
        :param _EdgeVersionLatest: Latest version of the edge cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EdgeVersionLatest: str
        :param _EdgeVersionCurrent: Current version of the edge cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EdgeVersionCurrent: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Versions = None
        self._EdgeVersionLatest = None
        self._EdgeVersionCurrent = None
        self._RequestId = None

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def EdgeVersionLatest(self):
        return self._EdgeVersionLatest

    @EdgeVersionLatest.setter
    def EdgeVersionLatest(self, EdgeVersionLatest):
        self._EdgeVersionLatest = EdgeVersionLatest

    @property
    def EdgeVersionCurrent(self):
        return self._EdgeVersionCurrent

    @EdgeVersionCurrent.setter
    def EdgeVersionCurrent(self, EdgeVersionCurrent):
        self._EdgeVersionCurrent = EdgeVersionCurrent

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Versions = params.get("Versions")
        self._EdgeVersionLatest = params.get("EdgeVersionLatest")
        self._EdgeVersionCurrent = params.get("EdgeVersionCurrent")
        self._RequestId = params.get("RequestId")


class DescribeBackupStorageLocationsRequest(AbstractModel):
    """DescribeBackupStorageLocations request structure.

    """

    def __init__(self):
        r"""
        :param _Names: Names of repositories. If it’s not specified, all storage repository names in the current region are returned.
        :type Names: list of str
        """
        self._Names = None

    @property
    def Names(self):
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupStorageLocationsResponse(AbstractModel):
    """DescribeBackupStorageLocations response structure.

    """

    def __init__(self):
        r"""
        :param _BackupStorageLocationSet: Detailed information of the backup repository 
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type BackupStorageLocationSet: list of BackupStorageLocation
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BackupStorageLocationSet = None
        self._RequestId = None

    @property
    def BackupStorageLocationSet(self):
        return self._BackupStorageLocationSet

    @BackupStorageLocationSet.setter
    def BackupStorageLocationSet(self, BackupStorageLocationSet):
        self._BackupStorageLocationSet = BackupStorageLocationSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BackupStorageLocationSet") is not None:
            self._BackupStorageLocationSet = []
            for item in params.get("BackupStorageLocationSet"):
                obj = BackupStorageLocation()
                obj._deserialize(item)
                self._BackupStorageLocationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterAsGroupOptionRequest(AbstractModel):
    """DescribeClusterAsGroupOption request structure.

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
        


class DescribeClusterAsGroupOptionResponse(AbstractModel):
    """DescribeClusterAsGroupOption response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterAsGroupOption: Cluster auto scaling attributes
Note: this field may return null, indicating that no valid value was found.
        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterAsGroupOption = None
        self._RequestId = None

    @property
    def ClusterAsGroupOption(self):
        return self._ClusterAsGroupOption

    @ClusterAsGroupOption.setter
    def ClusterAsGroupOption(self, ClusterAsGroupOption):
        self._ClusterAsGroupOption = ClusterAsGroupOption

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterAsGroupOption") is not None:
            self._ClusterAsGroupOption = ClusterAsGroupOption()
            self._ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))
        self._RequestId = params.get("RequestId")


class DescribeClusterAsGroupsRequest(AbstractModel):
    """DescribeClusterAsGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _AutoScalingGroupIds: Scaling group ID list. If this value is null, it indicates that all cluster-associated scaling groups are pulled.
        :type AutoScalingGroupIds: list of str
        :param _Offset: Offset. This value defaults to 0. For more information on Offset, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. This value defaults to 20. The maximum is 100. For more information on Limit, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self._ClusterId = None
        self._AutoScalingGroupIds = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AutoScalingGroupIds(self):
        return self._AutoScalingGroupIds

    @AutoScalingGroupIds.setter
    def AutoScalingGroupIds(self, AutoScalingGroupIds):
        self._AutoScalingGroupIds = AutoScalingGroupIds

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
        self._AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAsGroupsResponse(AbstractModel):
    """DescribeClusterAsGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of scaling groups associated with the cluster
        :type TotalCount: int
        :param _ClusterAsGroupSet: Cluster-associated scaling group list
        :type ClusterAsGroupSet: list of ClusterAsGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterAsGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterAsGroupSet(self):
        return self._ClusterAsGroupSet

    @ClusterAsGroupSet.setter
    def ClusterAsGroupSet(self, ClusterAsGroupSet):
        self._ClusterAsGroupSet = ClusterAsGroupSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterAsGroupSet") is not None:
            self._ClusterAsGroupSet = []
            for item in params.get("ClusterAsGroupSet"):
                obj = ClusterAsGroup()
                obj._deserialize(item)
                self._ClusterAsGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterAuthenticationOptionsRequest(AbstractModel):
    """DescribeClusterAuthenticationOptions request structure.

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
        


class DescribeClusterAuthenticationOptionsResponse(AbstractModel):
    """DescribeClusterAuthenticationOptions response structure.

    """

    def __init__(self):
        r"""
        :param _ServiceAccounts: ServiceAccount authentication configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServiceAccounts: :class:`tencentcloud.tke.v20180525.models.ServiceAccountAuthenticationOptions`
        :param _LatestOperationState: Result of the last modification. Values: `Updating`, `Success`, `Failed` or `TimeOut`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LatestOperationState: str
        :param _OIDCConfig: OIDC authentication configurations
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OIDCConfig: :class:`tencentcloud.tke.v20180525.models.OIDCConfigAuthenticationOptions`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServiceAccounts = None
        self._LatestOperationState = None
        self._OIDCConfig = None
        self._RequestId = None

    @property
    def ServiceAccounts(self):
        return self._ServiceAccounts

    @ServiceAccounts.setter
    def ServiceAccounts(self, ServiceAccounts):
        self._ServiceAccounts = ServiceAccounts

    @property
    def LatestOperationState(self):
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def OIDCConfig(self):
        return self._OIDCConfig

    @OIDCConfig.setter
    def OIDCConfig(self, OIDCConfig):
        self._OIDCConfig = OIDCConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceAccounts") is not None:
            self._ServiceAccounts = ServiceAccountAuthenticationOptions()
            self._ServiceAccounts._deserialize(params.get("ServiceAccounts"))
        self._LatestOperationState = params.get("LatestOperationState")
        if params.get("OIDCConfig") is not None:
            self._OIDCConfig = OIDCConfigAuthenticationOptions()
            self._OIDCConfig._deserialize(params.get("OIDCConfig"))
        self._RequestId = params.get("RequestId")


class DescribeClusterCommonNamesRequest(AbstractModel):
    """DescribeClusterCommonNames request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SubaccountUins: Sub-account. Up to 50 sub-accounts can be passed in at a time.
        :type SubaccountUins: list of str
        :param _RoleIds: Role ID. Up to 50 role IDs can be passed in at a time.
        :type RoleIds: list of str
        """
        self._ClusterId = None
        self._SubaccountUins = None
        self._RoleIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SubaccountUins(self):
        return self._SubaccountUins

    @SubaccountUins.setter
    def SubaccountUins(self, SubaccountUins):
        self._SubaccountUins = SubaccountUins

    @property
    def RoleIds(self):
        return self._RoleIds

    @RoleIds.setter
    def RoleIds(self, RoleIds):
        self._RoleIds = RoleIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SubaccountUins = params.get("SubaccountUins")
        self._RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterCommonNamesResponse(AbstractModel):
    """DescribeClusterCommonNames response structure.

    """

    def __init__(self):
        r"""
        :param _CommonNames: The CommonName in the certificate of the client corresponding to the sub-account UIN
        :type CommonNames: list of CommonName
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CommonNames = None
        self._RequestId = None

    @property
    def CommonNames(self):
        return self._CommonNames

    @CommonNames.setter
    def CommonNames(self, CommonNames):
        self._CommonNames = CommonNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CommonNames") is not None:
            self._CommonNames = []
            for item in params.get("CommonNames"):
                obj = CommonName()
                obj._deserialize(item)
                self._CommonNames.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterEndpointStatusRequest(AbstractModel):
    """DescribeClusterEndpointStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _IsExtranet: Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE).
        :type IsExtranet: bool
        """
        self._ClusterId = None
        self._IsExtranet = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IsExtranet(self):
        return self._IsExtranet

    @IsExtranet.setter
    def IsExtranet(self, IsExtranet):
        self._IsExtranet = IsExtranet


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._IsExtranet = params.get("IsExtranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: The status of cluster access port. It can be `Created` (enabled); `Creating` (enabling) and `NotFound` (not enabled)
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Status: str
        :param _ErrorMsg: Details of the error occurred while opening the access port
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeClusterEndpointVipStatusRequest(AbstractModel):
    """DescribeClusterEndpointVipStatus request structure.

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
        


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Port operation status (Creating = in the process of creation; CreateFailed = creation has failed; Created = creation completed; Deleting = in the process of deletion; DeletedFailed = deletion has failed; Deleted = deletion completed; NotFound = operation not found)
        :type Status: str
        :param _ErrorMsg: Reason for operation failure
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class DescribeClusterEndpointsRequest(AbstractModel):
    """DescribeClusterEndpoints request structure.

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
        


class DescribeClusterEndpointsResponse(AbstractModel):
    """DescribeClusterEndpoints response structure.

    """

    def __init__(self):
        r"""
        :param _CertificationAuthority: CA certificate of cluster APIServer
        :type CertificationAuthority: str
        :param _ClusterExternalEndpoint: Public network access address of cluster APIServer
        :type ClusterExternalEndpoint: str
        :param _ClusterIntranetEndpoint: Private network access address of cluster APIServer
        :type ClusterIntranetEndpoint: str
        :param _ClusterDomain: Domain name of cluster APIServer
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterDomain: str
        :param _ClusterExternalACL: Public network access ACL of cluster APIServer
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterExternalACL: list of str
        :param _ClusterExternalDomain: Public network domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterExternalDomain: str
        :param _ClusterIntranetDomain: Private network domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterIntranetDomain: str
        :param _SecurityGroup: Public network security group
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroup: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CertificationAuthority = None
        self._ClusterExternalEndpoint = None
        self._ClusterIntranetEndpoint = None
        self._ClusterDomain = None
        self._ClusterExternalACL = None
        self._ClusterExternalDomain = None
        self._ClusterIntranetDomain = None
        self._SecurityGroup = None
        self._RequestId = None

    @property
    def CertificationAuthority(self):
        return self._CertificationAuthority

    @CertificationAuthority.setter
    def CertificationAuthority(self, CertificationAuthority):
        self._CertificationAuthority = CertificationAuthority

    @property
    def ClusterExternalEndpoint(self):
        return self._ClusterExternalEndpoint

    @ClusterExternalEndpoint.setter
    def ClusterExternalEndpoint(self, ClusterExternalEndpoint):
        self._ClusterExternalEndpoint = ClusterExternalEndpoint

    @property
    def ClusterIntranetEndpoint(self):
        return self._ClusterIntranetEndpoint

    @ClusterIntranetEndpoint.setter
    def ClusterIntranetEndpoint(self, ClusterIntranetEndpoint):
        self._ClusterIntranetEndpoint = ClusterIntranetEndpoint

    @property
    def ClusterDomain(self):
        return self._ClusterDomain

    @ClusterDomain.setter
    def ClusterDomain(self, ClusterDomain):
        self._ClusterDomain = ClusterDomain

    @property
    def ClusterExternalACL(self):
        return self._ClusterExternalACL

    @ClusterExternalACL.setter
    def ClusterExternalACL(self, ClusterExternalACL):
        self._ClusterExternalACL = ClusterExternalACL

    @property
    def ClusterExternalDomain(self):
        return self._ClusterExternalDomain

    @ClusterExternalDomain.setter
    def ClusterExternalDomain(self, ClusterExternalDomain):
        self._ClusterExternalDomain = ClusterExternalDomain

    @property
    def ClusterIntranetDomain(self):
        return self._ClusterIntranetDomain

    @ClusterIntranetDomain.setter
    def ClusterIntranetDomain(self, ClusterIntranetDomain):
        self._ClusterIntranetDomain = ClusterIntranetDomain

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificationAuthority = params.get("CertificationAuthority")
        self._ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self._ClusterIntranetEndpoint = params.get("ClusterIntranetEndpoint")
        self._ClusterDomain = params.get("ClusterDomain")
        self._ClusterExternalACL = params.get("ClusterExternalACL")
        self._ClusterExternalDomain = params.get("ClusterExternalDomain")
        self._ClusterIntranetDomain = params.get("ClusterIntranetDomain")
        self._SecurityGroup = params.get("SecurityGroup")
        self._RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: 20
        :type Limit: int
        :param _InstanceIds: List of instance IDs to be obtained. This parameter is empty by default, which indicates that all instances in the cluster will be pulled.
        :type InstanceIds: list of str
        :param _InstanceRole: Node role. Valid values are MASTER, WORKER, ETCD, MASTER_ETCD, and ALL. Default value: WORKER.
        :type InstanceRole: str
        :param _Filters: Filters include `nodepool-id` and `nodepool-instance-type` (how the instance is added to the pool). For `nodepool-instance-type`, the values can be `MANUALLY_ADDED`, `AUTOSCALING_ADDED` and `ALL`.
        :type Filters: list of Filter
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._InstanceIds = None
        self._InstanceRole = None
        self._Filters = None

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
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceIds = params.get("InstanceIds")
        self._InstanceRole = params.get("InstanceRole")
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
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of instances in the cluster
        :type TotalCount: int
        :param _InstanceSet: List of instances in the cluster
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


class DescribeClusterKubeconfigRequest(AbstractModel):
    """DescribeClusterKubeconfig request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _IsExtranet: Defaults to `false`, which means to obtain the kubeconfig of private network
        :type IsExtranet: bool
        """
        self._ClusterId = None
        self._IsExtranet = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def IsExtranet(self):
        return self._IsExtranet

    @IsExtranet.setter
    def IsExtranet(self, IsExtranet):
        self._IsExtranet = IsExtranet


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._IsExtranet = params.get("IsExtranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterKubeconfigResponse(AbstractModel):
    """DescribeClusterKubeconfig response structure.

    """

    def __init__(self):
        r"""
        :param _Kubeconfig: Sub-account kubeconfig file, used to access the cluster kube-apiserver directly
        :type Kubeconfig: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Kubeconfig = None
        self._RequestId = None

    @property
    def Kubeconfig(self):
        return self._Kubeconfig

    @Kubeconfig.setter
    def Kubeconfig(self, Kubeconfig):
        self._Kubeconfig = Kubeconfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Kubeconfig = params.get("Kubeconfig")
        self._RequestId = params.get("RequestId")


class DescribeClusterLevelAttributeRequest(AbstractModel):
    """DescribeClusterLevelAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID (available for cluster model adjustment)
        :type ClusterID: str
        """
        self._ClusterID = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterLevelAttributeResponse(AbstractModel):
    """DescribeClusterLevelAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _Items: Cluster model
        :type Items: list of ClusterLevelAttribute
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
                obj = ClusterLevelAttribute()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterLevelChangeRecordsRequest(AbstractModel):
    """DescribeClusterLevelChangeRecords request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _StartAt: Start time
        :type StartAt: str
        :param _EndAt: End time
        :type EndAt: str
        :param _Offset: Offset. Default value: `0`
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: `20`
        :type Limit: int
        """
        self._ClusterID = None
        self._StartAt = None
        self._EndAt = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

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
        self._ClusterID = params.get("ClusterID")
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterLevelChangeRecordsResponse(AbstractModel):
    """DescribeClusterLevelChangeRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _Items: Cluster model
        :type Items: list of ClusterLevelChangeRecord
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
                obj = ClusterLevelChangeRecord()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterNodePoolDetailRequest(AbstractModel):
    """DescribeClusterNodePoolDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        """
        self._ClusterId = None
        self._NodePoolId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodePoolDetailResponse(AbstractModel):
    """DescribeClusterNodePoolDetail response structure.

    """

    def __init__(self):
        r"""
        :param _NodePool: Node pool details
        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePool`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodePool = None
        self._RequestId = None

    @property
    def NodePool(self):
        return self._NodePool

    @NodePool.setter
    def NodePool(self, NodePool):
        self._NodePool = NodePool

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NodePool") is not None:
            self._NodePool = NodePool()
            self._NodePool._deserialize(params.get("NodePool"))
        self._RequestId = params.get("RequestId")


class DescribeClusterNodePoolsRequest(AbstractModel):
    """DescribeClusterNodePools request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ClusterId (cluster ID)
        :type ClusterId: str
        :param _Filters: ·  NodePoolsName
    Filters by the node pool name
    Type: String
    Required: No

·  NodePoolsId
    Filters by the node pool ID
    Type: String
    Required: No

·  tags
    Filters by key-value pairs of tags
    Type: String
    Required: No

·  tag:tag-key
    Filters by key-value pairs of tags
    Type: String
    Required: No
        :type Filters: list of Filter
        """
        self._ClusterId = None
        self._Filters = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
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
        


class DescribeClusterNodePoolsResponse(AbstractModel):
    """DescribeClusterNodePools response structure.

    """

    def __init__(self):
        r"""
        :param _NodePoolSet: NodePools (node pool list)
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NodePoolSet: list of NodePool
        :param _TotalCount: Total resources
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodePoolSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodePoolSet(self):
        return self._NodePoolSet

    @NodePoolSet.setter
    def NodePoolSet(self, NodePoolSet):
        self._NodePoolSet = NodePoolSet

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
        if params.get("NodePoolSet") is not None:
            self._NodePoolSet = []
            for item in params.get("NodePoolSet"):
                obj = NodePool()
                obj._deserialize(item)
                self._NodePoolSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterRouteTablesRequest(AbstractModel):
    """DescribeClusterRouteTables request structure.

    """


class DescribeClusterRouteTablesResponse(AbstractModel):
    """DescribeClusterRouteTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances that match the filter condition(s).
        :type TotalCount: int
        :param _RouteTableSet: Object of cluster route table.
        :type RouteTableSet: list of RouteTableInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RouteTableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RouteTableSet(self):
        return self._RouteTableSet

    @RouteTableSet.setter
    def RouteTableSet(self, RouteTableSet):
        self._RouteTableSet = RouteTableSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self._RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTableInfo()
                obj._deserialize(item)
                self._RouteTableSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterRoutesRequest(AbstractModel):
    """DescribeClusterRoutes request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableName: Route table name.
        :type RouteTableName: str
        :param _Filters: Filtering conditions, which are optional. Currently, only filtering by GatewayIP is supported.
        :type Filters: list of Filter
        """
        self._RouteTableName = None
        self._Filters = None

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._RouteTableName = params.get("RouteTableName")
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
        


class DescribeClusterRoutesResponse(AbstractModel):
    """DescribeClusterRoutes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances that match the filter condition(s).
        :type TotalCount: int
        :param _RouteSet: Object of cluster route.
        :type RouteSet: list of RouteInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RouteSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RouteSet(self):
        return self._RouteSet

    @RouteSet.setter
    def RouteSet(self, RouteSet):
        self._RouteSet = RouteSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self._RouteSet = []
            for item in params.get("RouteSet"):
                obj = RouteInfo()
                obj._deserialize(item)
                self._RouteSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterSecurityRequest(AbstractModel):
    """DescribeClusterSecurity request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID. Enter the ClusterId field returned by the DescribeClusters API
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
        


class DescribeClusterSecurityResponse(AbstractModel):
    """DescribeClusterSecurity response structure.

    """

    def __init__(self):
        r"""
        :param _UserName: Cluster's account name
        :type UserName: str
        :param _Password: Cluster's password
        :type Password: str
        :param _CertificationAuthority: Cluster's access CA certificate
        :type CertificationAuthority: str
        :param _ClusterExternalEndpoint: Cluster's access address
        :type ClusterExternalEndpoint: str
        :param _Domain: Domain name accessed by the cluster
        :type Domain: str
        :param _PgwEndpoint: Cluster's endpoint address
        :type PgwEndpoint: str
        :param _SecurityPolicy: Cluster's access policy group
Note: This field may return null, indicating that no valid value was found.
        :type SecurityPolicy: list of str
        :param _Kubeconfig: Cluster Kubeconfig file
Note: This field may return null, indicating that no valid value was found.
        :type Kubeconfig: str
        :param _JnsGwEndpoint: Access address of the cluster JnsGw
Note: This field may return null, indicating that no valid value was found.
        :type JnsGwEndpoint: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserName = None
        self._Password = None
        self._CertificationAuthority = None
        self._ClusterExternalEndpoint = None
        self._Domain = None
        self._PgwEndpoint = None
        self._SecurityPolicy = None
        self._Kubeconfig = None
        self._JnsGwEndpoint = None
        self._RequestId = None

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def CertificationAuthority(self):
        return self._CertificationAuthority

    @CertificationAuthority.setter
    def CertificationAuthority(self, CertificationAuthority):
        self._CertificationAuthority = CertificationAuthority

    @property
    def ClusterExternalEndpoint(self):
        return self._ClusterExternalEndpoint

    @ClusterExternalEndpoint.setter
    def ClusterExternalEndpoint(self, ClusterExternalEndpoint):
        self._ClusterExternalEndpoint = ClusterExternalEndpoint

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def PgwEndpoint(self):
        return self._PgwEndpoint

    @PgwEndpoint.setter
    def PgwEndpoint(self, PgwEndpoint):
        self._PgwEndpoint = PgwEndpoint

    @property
    def SecurityPolicy(self):
        return self._SecurityPolicy

    @SecurityPolicy.setter
    def SecurityPolicy(self, SecurityPolicy):
        self._SecurityPolicy = SecurityPolicy

    @property
    def Kubeconfig(self):
        return self._Kubeconfig

    @Kubeconfig.setter
    def Kubeconfig(self, Kubeconfig):
        self._Kubeconfig = Kubeconfig

    @property
    def JnsGwEndpoint(self):
        return self._JnsGwEndpoint

    @JnsGwEndpoint.setter
    def JnsGwEndpoint(self, JnsGwEndpoint):
        self._JnsGwEndpoint = JnsGwEndpoint

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        self._CertificationAuthority = params.get("CertificationAuthority")
        self._ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self._Domain = params.get("Domain")
        self._PgwEndpoint = params.get("PgwEndpoint")
        self._SecurityPolicy = params.get("SecurityPolicy")
        self._Kubeconfig = params.get("Kubeconfig")
        self._JnsGwEndpoint = params.get("JnsGwEndpoint")
        self._RequestId = params.get("RequestId")


class DescribeClusterStatusRequest(AbstractModel):
    """DescribeClusterStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: Cluster ID list. All clusters are pulled if it is left empty.
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
        


class DescribeClusterStatusResponse(AbstractModel):
    """DescribeClusterStatus response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterStatusSet: Cluster status list
        :type ClusterStatusSet: list of ClusterStatus
        :param _TotalCount: Number of clusters
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterStatusSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterStatusSet(self):
        return self._ClusterStatusSet

    @ClusterStatusSet.setter
    def ClusterStatusSet(self, ClusterStatusSet):
        self._ClusterStatusSet = ClusterStatusSet

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
        if params.get("ClusterStatusSet") is not None:
            self._ClusterStatusSet = []
            for item in params.get("ClusterStatusSet"):
                obj = ClusterStatus()
                obj._deserialize(item)
                self._ClusterStatusSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterVirtualNodePoolsRequest(AbstractModel):
    """DescribeClusterVirtualNodePools request structure.

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
        


class DescribeClusterVirtualNodePoolsResponse(AbstractModel):
    """DescribeClusterVirtualNodePools response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of node pools
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _NodePoolSet: List of virtual node pools
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodePoolSet: list of VirtualNodePool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodePoolSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodePoolSet(self):
        return self._NodePoolSet

    @NodePoolSet.setter
    def NodePoolSet(self, NodePoolSet):
        self._NodePoolSet = NodePoolSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodePoolSet") is not None:
            self._NodePoolSet = []
            for item in params.get("NodePoolSet"):
                obj = VirtualNodePool()
                obj._deserialize(item)
                self._NodePoolSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterVirtualNodeRequest(AbstractModel):
    """DescribeClusterVirtualNode request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _NodeNames: Node name
        :type NodeNames: list of str
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._NodeNames = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def NodeNames(self):
        return self._NodeNames

    @NodeNames.setter
    def NodeNames(self, NodeNames):
        self._NodeNames = NodeNames


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._NodeNames = params.get("NodeNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterVirtualNodeResponse(AbstractModel):
    """DescribeClusterVirtualNode response structure.

    """

    def __init__(self):
        r"""
        :param _Nodes: List of nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type Nodes: list of VirtualNode
        :param _TotalCount: Total number of nodes
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Nodes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

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
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = VirtualNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: Cluster ID list (When it is empty,
all clusters under the account will be obtained)
        :type ClusterIds: list of str
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: 20
        :type Limit: int
        :param _Filters: ·  ClusterName
    Filters by the cluster name
    Type: String
    Required: No

·  ClusterType
    Filters by the cluster type
    Type: String
    Required: No

·  ClusterStatus
    Filters by the cluster status
    Type: String
    Required: No

·  Tags
    Filters by key-value pairs of tags
    Type: String
    Required: No

·  vpc-id
    Filters by the VPC ID
    Type: String
    Required: No

·  tag-key
    Filters by the tag key
    Type: String
    Required: No

·  tag-value
    Filters by the tag value
    Type: String
    Required: No

·  tag:tag-key
    Filters by key-value pairs of tags
    Type: String
    Required: No
        :type Filters: list of Filter
        :param _ClusterType: Cluster type, such as `MANAGED_CLUSTER`
        :type ClusterType: str
        """
        self._ClusterIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ClusterType = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ClusterType(self):
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ClusterType = params.get("ClusterType")
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
        :param _TotalCount: Total number of clusters
        :type TotalCount: int
        :param _Clusters: Cluster information list
        :type Clusters: list of Cluster
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
                obj = Cluster()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeECMInstancesRequest(AbstractModel):
    """DescribeECMInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _Filters: Filter condition
Only filtering by an ECM ID is supported
        :type Filters: list of Filter
        """
        self._ClusterID = None
        self._Filters = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
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
        


class DescribeECMInstancesResponse(AbstractModel):
    """DescribeECMInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances matched the condition
        :type TotalCount: int
        :param _InstanceInfoSet: List of the returned instance information
        :type InstanceInfoSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceInfoSet(self):
        return self._InstanceInfoSet

    @InstanceInfoSet.setter
    def InstanceInfoSet(self, InstanceInfoSet):
        self._InstanceInfoSet = InstanceInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._InstanceInfoSet = params.get("InstanceInfoSet")
        self._RequestId = params.get("RequestId")


class DescribeEdgeAvailableExtraArgsRequest(AbstractModel):
    """DescribeEdgeAvailableExtraArgs request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterVersion: Cluster version
        :type ClusterVersion: str
        """
        self._ClusterVersion = None

    @property
    def ClusterVersion(self):
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion


    def _deserialize(self, params):
        self._ClusterVersion = params.get("ClusterVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeAvailableExtraArgsResponse(AbstractModel):
    """DescribeEdgeAvailableExtraArgs response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterVersion: Cluster version
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterVersion: str
        :param _AvailableExtraArgs: Available custom parameters
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AvailableExtraArgs: :class:`tencentcloud.tke.v20180525.models.EdgeAvailableExtraArgs`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterVersion = None
        self._AvailableExtraArgs = None
        self._RequestId = None

    @property
    def ClusterVersion(self):
        return self._ClusterVersion

    @ClusterVersion.setter
    def ClusterVersion(self, ClusterVersion):
        self._ClusterVersion = ClusterVersion

    @property
    def AvailableExtraArgs(self):
        return self._AvailableExtraArgs

    @AvailableExtraArgs.setter
    def AvailableExtraArgs(self, AvailableExtraArgs):
        self._AvailableExtraArgs = AvailableExtraArgs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterVersion = params.get("ClusterVersion")
        if params.get("AvailableExtraArgs") is not None:
            self._AvailableExtraArgs = EdgeAvailableExtraArgs()
            self._AvailableExtraArgs._deserialize(params.get("AvailableExtraArgs"))
        self._RequestId = params.get("RequestId")


class DescribeEdgeCVMInstancesRequest(AbstractModel):
    """DescribeEdgeCVMInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _Filters: Filter condition
Only `cvm-id` is supported.
        :type Filters: list of Filter
        """
        self._ClusterID = None
        self._Filters = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
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
        


class DescribeEdgeCVMInstancesResponse(AbstractModel):
    """DescribeEdgeCVMInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of instances matched the condition
        :type TotalCount: int
        :param _InstanceInfoSet: List of the returned instance information
        :type InstanceInfoSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceInfoSet(self):
        return self._InstanceInfoSet

    @InstanceInfoSet.setter
    def InstanceInfoSet(self, InstanceInfoSet):
        self._InstanceInfoSet = InstanceInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._InstanceInfoSet = params.get("InstanceInfoSet")
        self._RequestId = params.get("RequestId")


class DescribeEdgeClusterExtraArgsRequest(AbstractModel):
    """DescribeEdgeClusterExtraArgs request structure.

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
        


class DescribeEdgeClusterExtraArgsResponse(AbstractModel):
    """DescribeEdgeClusterExtraArgs response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterExtraArgs: Custom parameters of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterExtraArgs: :class:`tencentcloud.tke.v20180525.models.EdgeClusterExtraArgs`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterExtraArgs = None
        self._RequestId = None

    @property
    def ClusterExtraArgs(self):
        return self._ClusterExtraArgs

    @ClusterExtraArgs.setter
    def ClusterExtraArgs(self, ClusterExtraArgs):
        self._ClusterExtraArgs = ClusterExtraArgs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterExtraArgs") is not None:
            self._ClusterExtraArgs = EdgeClusterExtraArgs()
            self._ClusterExtraArgs._deserialize(params.get("ClusterExtraArgs"))
        self._RequestId = params.get("RequestId")


class DescribeEdgeClusterInstancesRequest(AbstractModel):
    """DescribeEdgeClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Cluster ID
        :type ClusterID: str
        :param _Limit: Max number of returned entries
        :type Limit: int
        :param _Offset: Offset
        :type Offset: int
        :param _Filters: Filter condition. Only `NodeName` is supported.
        :type Filters: list of Filter
        """
        self._ClusterID = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ClusterID(self):
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeEdgeClusterInstancesResponse(AbstractModel):
    """DescribeEdgeClusterInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of nodes in the cluster
        :type TotalCount: int
        :param _InstanceInfoSet: Array of node information
        :type InstanceInfoSet: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceInfoSet(self):
        return self._InstanceInfoSet

    @InstanceInfoSet.setter
    def InstanceInfoSet(self, InstanceInfoSet):
        self._InstanceInfoSet = InstanceInfoSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._InstanceInfoSet = params.get("InstanceInfoSet")
        self._RequestId = params.get("RequestId")


class DescribeEdgeClusterUpgradeInfoRequest(AbstractModel):
    """DescribeEdgeClusterUpgradeInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _EdgeVersion: Target TKEEdge version
        :type EdgeVersion: str
        """
        self._ClusterId = None
        self._EdgeVersion = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EdgeVersion(self):
        return self._EdgeVersion

    @EdgeVersion.setter
    def EdgeVersion(self, EdgeVersion):
        self._EdgeVersion = EdgeVersion


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EdgeVersion = params.get("EdgeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeClusterUpgradeInfoResponse(AbstractModel):
    """DescribeEdgeClusterUpgradeInfo response structure.

    """

    def __init__(self):
        r"""
        :param _ComponentVersion: Upgradeable cluster component
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ComponentVersion: str
        :param _EdgeVersionCurrent: Current version of the edge cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EdgeVersionCurrent: str
        :param _RegistryPrefix: Prefix of the image registry of an edge component (including domain name and namespace)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RegistryPrefix: str
        :param _ClusterUpgradeStatus: Cluster upgrade status. Valid values: `Running`, `Updating`, `Failed`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterUpgradeStatus: str
        :param _ClusterUpgradeStatusReason: Reason for `Updating` or `Failed`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClusterUpgradeStatusReason: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ComponentVersion = None
        self._EdgeVersionCurrent = None
        self._RegistryPrefix = None
        self._ClusterUpgradeStatus = None
        self._ClusterUpgradeStatusReason = None
        self._RequestId = None

    @property
    def ComponentVersion(self):
        return self._ComponentVersion

    @ComponentVersion.setter
    def ComponentVersion(self, ComponentVersion):
        self._ComponentVersion = ComponentVersion

    @property
    def EdgeVersionCurrent(self):
        return self._EdgeVersionCurrent

    @EdgeVersionCurrent.setter
    def EdgeVersionCurrent(self, EdgeVersionCurrent):
        self._EdgeVersionCurrent = EdgeVersionCurrent

    @property
    def RegistryPrefix(self):
        return self._RegistryPrefix

    @RegistryPrefix.setter
    def RegistryPrefix(self, RegistryPrefix):
        self._RegistryPrefix = RegistryPrefix

    @property
    def ClusterUpgradeStatus(self):
        return self._ClusterUpgradeStatus

    @ClusterUpgradeStatus.setter
    def ClusterUpgradeStatus(self, ClusterUpgradeStatus):
        self._ClusterUpgradeStatus = ClusterUpgradeStatus

    @property
    def ClusterUpgradeStatusReason(self):
        return self._ClusterUpgradeStatusReason

    @ClusterUpgradeStatusReason.setter
    def ClusterUpgradeStatusReason(self, ClusterUpgradeStatusReason):
        self._ClusterUpgradeStatusReason = ClusterUpgradeStatusReason

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ComponentVersion = params.get("ComponentVersion")
        self._EdgeVersionCurrent = params.get("EdgeVersionCurrent")
        self._RegistryPrefix = params.get("RegistryPrefix")
        self._ClusterUpgradeStatus = params.get("ClusterUpgradeStatus")
        self._ClusterUpgradeStatusReason = params.get("ClusterUpgradeStatusReason")
        self._RequestId = params.get("RequestId")


class DescribeEdgeLogSwitchesRequest(AbstractModel):
    """DescribeEdgeLogSwitches request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: List of cluster IDs
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
        


class DescribeEdgeLogSwitchesResponse(AbstractModel):
    """DescribeEdgeLogSwitches response structure.

    """

    def __init__(self):
        r"""
        :param _SwitchSet: Array of TKE Edge cluster log switches
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SwitchSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SwitchSet = None
        self._RequestId = None

    @property
    def SwitchSet(self):
        return self._SwitchSet

    @SwitchSet.setter
    def SwitchSet(self, SwitchSet):
        self._SwitchSet = SwitchSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SwitchSet = params.get("SwitchSet")
        self._RequestId = params.get("RequestId")


class DescribeEnableVpcCniProgressRequest(AbstractModel):
    """DescribeEnableVpcCniProgress request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster for which you want to enable the VPC-CNI mode
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
        


class DescribeEnableVpcCniProgressResponse(AbstractModel):
    """DescribeEnableVpcCniProgress response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status, which can be `Running`, `Succeed`, or `Failed`.
        :type Status: str
        :param _ErrorMessage: The description for the task status when the task status is “Failed”, for example, failed to install the IPAMD component.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMessage(self):
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID. Enter the `ClusterId` field returned when you call the DescribeClusters API (Only VPC ID obtained through `ClusterId` need filtering conditions. When comparing statuses, the nodes on all clusters in this region will be used for comparison. You cannot specify `InstanceIds` and `ClusterId` at the same time.)
        :type ClusterId: str
        :param _InstanceIds: Query by one or more instance ID(s). Instance ID format: ins-xxxxxxxx. (Refer to section ID.N of the API overview for this parameter's specific format.) Up to 100 instances are allowed for each request. You cannot specify InstanceIds and Filters at the same time.
        :type InstanceIds: list of str
        :param _Filters: Filter condition. For fields and other information, see [the DescribeInstances API](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1). If a ClusterId has been set, then the cluster's VPC ID will be attached as a query field. In this situation, if a "vpc-id" is specified in Filter, then the specified VPC ID must be consistent with the cluster's VPC ID.
        :type Filters: list of Filter
        :param _VagueIpAddress: Filter by instance IP (Supports both private and public IPs)
        :type VagueIpAddress: str
        :param _VagueInstanceName: Filter by instance name
        :type VagueInstanceName: str
        :param _Offset: Offset. Default value: 0. For more information on Offset, see the relevant section in the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on Limit, see the relevant section in the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _IpAddresses: Filter by multiple instance IPs
        :type IpAddresses: list of str
        """
        self._ClusterId = None
        self._InstanceIds = None
        self._Filters = None
        self._VagueIpAddress = None
        self._VagueInstanceName = None
        self._Offset = None
        self._Limit = None
        self._IpAddresses = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def VagueIpAddress(self):
        return self._VagueIpAddress

    @VagueIpAddress.setter
    def VagueIpAddress(self, VagueIpAddress):
        self._VagueIpAddress = VagueIpAddress

    @property
    def VagueInstanceName(self):
        return self._VagueInstanceName

    @VagueInstanceName.setter
    def VagueInstanceName(self, VagueInstanceName):
        self._VagueInstanceName = VagueInstanceName

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
    def IpAddresses(self):
        return self._IpAddresses

    @IpAddresses.setter
    def IpAddresses(self, IpAddresses):
        self._IpAddresses = IpAddresses


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._VagueIpAddress = params.get("VagueIpAddress")
        self._VagueInstanceName = params.get("VagueInstanceName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IpAddresses = params.get("IpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExistedInstancesResponse(AbstractModel):
    """DescribeExistedInstances response structure.

    """

    def __init__(self):
        r"""
        :param _ExistedInstanceSet: Array of existing instance information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExistedInstanceSet: list of ExistedInstance
        :param _TotalCount: Number of instances that match the filter condition(s).
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExistedInstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ExistedInstanceSet(self):
        return self._ExistedInstanceSet

    @ExistedInstanceSet.setter
    def ExistedInstanceSet(self, ExistedInstanceSet):
        self._ExistedInstanceSet = ExistedInstanceSet

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
        if params.get("ExistedInstanceSet") is not None:
            self._ExistedInstanceSet = []
            for item in params.get("ExistedInstanceSet"):
                obj = ExistedInstance()
                obj._deserialize(item)
                self._ExistedInstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages request structure.

    """


class DescribeImagesResponse(AbstractModel):
    """DescribeImages response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of images
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ImageInstanceSet: Image information list
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageInstanceSet: list of ImageInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ImageInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImageInstanceSet(self):
        return self._ImageInstanceSet

    @ImageInstanceSet.setter
    def ImageInstanceSet(self, ImageInstanceSet):
        self._ImageInstanceSet = ImageInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ImageInstanceSet") is not None:
            self._ImageInstanceSet = []
            for item in params.get("ImageInstanceSet"):
                obj = ImageInstance()
                obj._deserialize(item)
                self._ImageInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrometheusInstanceRequest(AbstractModel):
    """DescribePrometheusInstance request structure.

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
        


class DescribePrometheusInstanceResponse(AbstractModel):
    """DescribePrometheusInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _Name: Instance name
        :type Name: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _COSBucket: COS bucket name
        :type COSBucket: str
        :param _QueryAddress: Data query address
        :type QueryAddress: str
        :param _Grafana: The grafana related information in the instance
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Grafana: :class:`tencentcloud.tke.v20180525.models.PrometheusGrafanaInfo`
        :param _AlertManagerUrl: Custom alertmanager
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type AlertManagerUrl: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._Name = None
        self._VpcId = None
        self._SubnetId = None
        self._COSBucket = None
        self._QueryAddress = None
        self._Grafana = None
        self._AlertManagerUrl = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
    def COSBucket(self):
        return self._COSBucket

    @COSBucket.setter
    def COSBucket(self, COSBucket):
        self._COSBucket = COSBucket

    @property
    def QueryAddress(self):
        return self._QueryAddress

    @QueryAddress.setter
    def QueryAddress(self, QueryAddress):
        self._QueryAddress = QueryAddress

    @property
    def Grafana(self):
        return self._Grafana

    @Grafana.setter
    def Grafana(self, Grafana):
        self._Grafana = Grafana

    @property
    def AlertManagerUrl(self):
        return self._AlertManagerUrl

    @AlertManagerUrl.setter
    def AlertManagerUrl(self, AlertManagerUrl):
        self._AlertManagerUrl = AlertManagerUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._COSBucket = params.get("COSBucket")
        self._QueryAddress = params.get("QueryAddress")
        if params.get("Grafana") is not None:
            self._Grafana = PrometheusGrafanaInfo()
            self._Grafana._deserialize(params.get("Grafana"))
        self._AlertManagerUrl = params.get("AlertManagerUrl")
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
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RegionInstanceSet: ## Region List
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionInstanceSet: list of RegionInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionInstanceSet(self):
        return self._RegionInstanceSet

    @RegionInstanceSet.setter
    def RegionInstanceSet(self, RegionInstanceSet):
        self._RegionInstanceSet = RegionInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionInstanceSet") is not None:
            self._RegionInstanceSet = []
            for item in params.get("RegionInstanceSet"):
                obj = RegionInstance()
                obj._deserialize(item)
                self._RegionInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceUsageRequest(AbstractModel):
    """DescribeResourceUsage request structure.

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
        


class DescribeResourceUsageResponse(AbstractModel):
    """DescribeResourceUsage response structure.

    """

    def __init__(self):
        r"""
        :param _CRDUsage: CRD usage
        :type CRDUsage: :class:`tencentcloud.tke.v20180525.models.ResourceUsage`
        :param _PodUsage: Pod usage
        :type PodUsage: int
        :param _ConfigMapUsage: ConfigMap usage
        :type ConfigMapUsage: int
        :param _OtherUsage: Other resource usage
        :type OtherUsage: :class:`tencentcloud.tke.v20180525.models.ResourceUsage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CRDUsage = None
        self._PodUsage = None
        self._ConfigMapUsage = None
        self._OtherUsage = None
        self._RequestId = None

    @property
    def CRDUsage(self):
        return self._CRDUsage

    @CRDUsage.setter
    def CRDUsage(self, CRDUsage):
        self._CRDUsage = CRDUsage

    @property
    def PodUsage(self):
        return self._PodUsage

    @PodUsage.setter
    def PodUsage(self, PodUsage):
        self._PodUsage = PodUsage

    @property
    def ConfigMapUsage(self):
        return self._ConfigMapUsage

    @ConfigMapUsage.setter
    def ConfigMapUsage(self, ConfigMapUsage):
        self._ConfigMapUsage = ConfigMapUsage

    @property
    def OtherUsage(self):
        return self._OtherUsage

    @OtherUsage.setter
    def OtherUsage(self, OtherUsage):
        self._OtherUsage = OtherUsage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CRDUsage") is not None:
            self._CRDUsage = ResourceUsage()
            self._CRDUsage._deserialize(params.get("CRDUsage"))
        self._PodUsage = params.get("PodUsage")
        self._ConfigMapUsage = params.get("ConfigMapUsage")
        if params.get("OtherUsage") is not None:
            self._OtherUsage = ResourceUsage()
            self._OtherUsage._deserialize(params.get("OtherUsage"))
        self._RequestId = params.get("RequestId")


class DescribeRouteTableConflictsRequest(AbstractModel):
    """DescribeRouteTableConflicts request structure.

    """

    def __init__(self):
        r"""
        :param _RouteTableCidrBlock: Route table CIDR
        :type RouteTableCidrBlock: str
        :param _VpcId: VPC bound to the route table
        :type VpcId: str
        """
        self._RouteTableCidrBlock = None
        self._VpcId = None

    @property
    def RouteTableCidrBlock(self):
        return self._RouteTableCidrBlock

    @RouteTableCidrBlock.setter
    def RouteTableCidrBlock(self, RouteTableCidrBlock):
        self._RouteTableCidrBlock = RouteTableCidrBlock

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTableConflictsResponse(AbstractModel):
    """DescribeRouteTableConflicts response structure.

    """

    def __init__(self):
        r"""
        :param _HasConflict: Whether there is a conflict in the route table.
        :type HasConflict: bool
        :param _RouteTableConflictSet: Route table conflict list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableConflictSet: list of RouteTableConflict
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HasConflict = None
        self._RouteTableConflictSet = None
        self._RequestId = None

    @property
    def HasConflict(self):
        return self._HasConflict

    @HasConflict.setter
    def HasConflict(self, HasConflict):
        self._HasConflict = HasConflict

    @property
    def RouteTableConflictSet(self):
        return self._RouteTableConflictSet

    @RouteTableConflictSet.setter
    def RouteTableConflictSet(self, RouteTableConflictSet):
        self._RouteTableConflictSet = RouteTableConflictSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HasConflict = params.get("HasConflict")
        if params.get("RouteTableConflictSet") is not None:
            self._RouteTableConflictSet = []
            for item in params.get("RouteTableConflictSet"):
                obj = RouteTableConflict()
                obj._deserialize(item)
                self._RouteTableConflictSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTKEEdgeClusterCredentialRequest(AbstractModel):
    """DescribeTKEEdgeClusterCredential request structure.

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
        


class DescribeTKEEdgeClusterCredentialResponse(AbstractModel):
    """DescribeTKEEdgeClusterCredential response structure.

    """

    def __init__(self):
        r"""
        :param _Addresses: Access address of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Addresses: list of IPAddress
        :param _Credential: Cluster authentication information
        :type Credential: :class:`tencentcloud.tke.v20180525.models.ClusterCredential`
        :param _PublicLB: Public network access information of the cluster
        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.EdgeClusterPublicLB`
        :param _InternalLB: Private network access information of the cluster
        :type InternalLB: :class:`tencentcloud.tke.v20180525.models.EdgeClusterInternalLB`
        :param _CoreDns: CoreDns deployment information of the cluster
        :type CoreDns: str
        :param _HealthRegion: Multi-region health check deployment information of the cluster
        :type HealthRegion: str
        :param _Health: Health check deployment information of the cluster
        :type Health: str
        :param _GridDaemon: Whether to deploy GridDaemon to support headless service
        :type GridDaemon: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Addresses = None
        self._Credential = None
        self._PublicLB = None
        self._InternalLB = None
        self._CoreDns = None
        self._HealthRegion = None
        self._Health = None
        self._GridDaemon = None
        self._RequestId = None

    @property
    def Addresses(self):
        return self._Addresses

    @Addresses.setter
    def Addresses(self, Addresses):
        self._Addresses = Addresses

    @property
    def Credential(self):
        return self._Credential

    @Credential.setter
    def Credential(self, Credential):
        self._Credential = Credential

    @property
    def PublicLB(self):
        return self._PublicLB

    @PublicLB.setter
    def PublicLB(self, PublicLB):
        self._PublicLB = PublicLB

    @property
    def InternalLB(self):
        return self._InternalLB

    @InternalLB.setter
    def InternalLB(self, InternalLB):
        self._InternalLB = InternalLB

    @property
    def CoreDns(self):
        return self._CoreDns

    @CoreDns.setter
    def CoreDns(self, CoreDns):
        self._CoreDns = CoreDns

    @property
    def HealthRegion(self):
        return self._HealthRegion

    @HealthRegion.setter
    def HealthRegion(self, HealthRegion):
        self._HealthRegion = HealthRegion

    @property
    def Health(self):
        return self._Health

    @Health.setter
    def Health(self, Health):
        self._Health = Health

    @property
    def GridDaemon(self):
        return self._GridDaemon

    @GridDaemon.setter
    def GridDaemon(self, GridDaemon):
        self._GridDaemon = GridDaemon

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Addresses") is not None:
            self._Addresses = []
            for item in params.get("Addresses"):
                obj = IPAddress()
                obj._deserialize(item)
                self._Addresses.append(obj)
        if params.get("Credential") is not None:
            self._Credential = ClusterCredential()
            self._Credential._deserialize(params.get("Credential"))
        if params.get("PublicLB") is not None:
            self._PublicLB = EdgeClusterPublicLB()
            self._PublicLB._deserialize(params.get("PublicLB"))
        if params.get("InternalLB") is not None:
            self._InternalLB = EdgeClusterInternalLB()
            self._InternalLB._deserialize(params.get("InternalLB"))
        self._CoreDns = params.get("CoreDns")
        self._HealthRegion = params.get("HealthRegion")
        self._Health = params.get("Health")
        self._GridDaemon = params.get("GridDaemon")
        self._RequestId = params.get("RequestId")


class DescribeTKEEdgeClusterStatusRequest(AbstractModel):
    """DescribeTKEEdgeClusterStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Edge compute cluster ID
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
        


class DescribeTKEEdgeClusterStatusResponse(AbstractModel):
    """DescribeTKEEdgeClusterStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Phase: Current cluster status
        :type Phase: str
        :param _Conditions: Array of cluster processes
        :type Conditions: list of ClusterCondition
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Phase = None
        self._Conditions = None
        self._RequestId = None

    @property
    def Phase(self):
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def Conditions(self):
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Phase = params.get("Phase")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ClusterCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTKEEdgeClustersRequest(AbstractModel):
    """DescribeTKEEdgeClusters request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterIds: Cluster ID list (when it is empty,
all clusters under the account are obtained)
        :type ClusterIds: list of str
        :param _Offset: Offset. Default value: `0`
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: `20`
        :type Limit: int
        :param _Filters: Filter condition (only filtering by a single ClusterName is supported)
        :type Filters: list of Filter
        """
        self._ClusterIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ClusterIds = params.get("ClusterIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeTKEEdgeClustersResponse(AbstractModel):
    """DescribeTKEEdgeClusters response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of clusters
        :type TotalCount: int
        :param _Clusters: Cluster information list
        :type Clusters: list of EdgeCluster
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
                obj = EdgeCluster()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTKEEdgeExternalKubeconfigRequest(AbstractModel):
    """DescribeTKEEdgeExternalKubeconfig request structure.

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
        


class DescribeTKEEdgeExternalKubeconfigResponse(AbstractModel):
    """DescribeTKEEdgeExternalKubeconfig response structure.

    """

    def __init__(self):
        r"""
        :param _Kubeconfig: Kubeconfig file content
        :type Kubeconfig: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Kubeconfig = None
        self._RequestId = None

    @property
    def Kubeconfig(self):
        return self._Kubeconfig

    @Kubeconfig.setter
    def Kubeconfig(self, Kubeconfig):
        self._Kubeconfig = Kubeconfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Kubeconfig = params.get("Kubeconfig")
        self._RequestId = params.get("RequestId")


class DescribeTKEEdgeScriptRequest(AbstractModel):
    """DescribeTKEEdgeScript request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Interface: ENI
        :type Interface: str
        :param _NodeName: Name of the name
        :type NodeName: str
        :param _Config: Node configuration in JSON format 
        :type Config: str
        :param _ScriptVersion: A legacy version of edgectl script can be downloaded. The latest version is downloaded by default. The version information can be checked in the script.
        :type ScriptVersion: str
        """
        self._ClusterId = None
        self._Interface = None
        self._NodeName = None
        self._Config = None
        self._ScriptVersion = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Interface(self):
        return self._Interface

    @Interface.setter
    def Interface(self, Interface):
        self._Interface = Interface

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ScriptVersion(self):
        return self._ScriptVersion

    @ScriptVersion.setter
    def ScriptVersion(self, ScriptVersion):
        self._ScriptVersion = ScriptVersion


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Interface = params.get("Interface")
        self._NodeName = params.get("NodeName")
        self._Config = params.get("Config")
        self._ScriptVersion = params.get("ScriptVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTKEEdgeScriptResponse(AbstractModel):
    """DescribeTKEEdgeScript response structure.

    """

    def __init__(self):
        r"""
        :param _Link: Whether to download the link
        :type Link: str
        :param _Token: Whether to download the desired token
        :type Token: str
        :param _Command: Whether to download the command
        :type Command: str
        :param _ScriptVersion: Version of edgectl script. The latest version is obtained by default.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ScriptVersion: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Link = None
        self._Token = None
        self._Command = None
        self._ScriptVersion = None
        self._RequestId = None

    @property
    def Link(self):
        return self._Link

    @Link.setter
    def Link(self, Link):
        self._Link = Link

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Command(self):
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ScriptVersion(self):
        return self._ScriptVersion

    @ScriptVersion.setter
    def ScriptVersion(self, ScriptVersion):
        self._ScriptVersion = ScriptVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Link = params.get("Link")
        self._Token = params.get("Token")
        self._Command = params.get("Command")
        self._ScriptVersion = params.get("ScriptVersion")
        self._RequestId = params.get("RequestId")


class DescribeVersionsRequest(AbstractModel):
    """DescribeVersions request structure.

    """


class DescribeVersionsResponse(AbstractModel):
    """DescribeVersions response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of versions
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _VersionInstanceSet: Version list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VersionInstanceSet: list of VersionInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._VersionInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VersionInstanceSet(self):
        return self._VersionInstanceSet

    @VersionInstanceSet.setter
    def VersionInstanceSet(self, VersionInstanceSet):
        self._VersionInstanceSet = VersionInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VersionInstanceSet") is not None:
            self._VersionInstanceSet = []
            for item in params.get("VersionInstanceSet"):
                obj = VersionInstance()
                obj._deserialize(item)
                self._VersionInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcCniPodLimitsRequest(AbstractModel):
    """DescribeVpcCniPodLimits request structure.

    """

    def __init__(self):
        r"""
        :param _Zone: The availability zone of the model to query, for example, `ap-guangzhou-3`. This field is left empty by default, that is, do not filter by the availability zone.
        :type Zone: str
        :param _InstanceFamily: The instance family to query, for example, `S5`. This field is left empty by default, that is, do not filter by the instance family.
        :type InstanceFamily: str
        :param _InstanceType: The instance model to query, for example, `S5.LARGE8`. This field is empty by default, that is, do not filter by instance type.
        :type InstanceType: str
        """
        self._Zone = None
        self._InstanceFamily = None
        self._InstanceType = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceFamily = params.get("InstanceFamily")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcCniPodLimitsResponse(AbstractModel):
    """DescribeVpcCniPodLimits response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of the models
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _PodLimitsInstanceSet: The model information and the maximum supported number of Pods in the VPC-CNI mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PodLimitsInstanceSet: list of PodLimitsInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._PodLimitsInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PodLimitsInstanceSet(self):
        return self._PodLimitsInstanceSet

    @PodLimitsInstanceSet.setter
    def PodLimitsInstanceSet(self, PodLimitsInstanceSet):
        self._PodLimitsInstanceSet = PodLimitsInstanceSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PodLimitsInstanceSet") is not None:
            self._PodLimitsInstanceSet = []
            for item in params.get("PodLimitsInstanceSet"):
                obj = PodLimitsInstance()
                obj._deserialize(item)
                self._PodLimitsInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisableClusterDeletionProtectionRequest(AbstractModel):
    """DisableClusterDeletionProtection request structure.

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
        


class DisableClusterDeletionProtectionResponse(AbstractModel):
    """DisableClusterDeletionProtection response structure.

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


class DrainClusterVirtualNodeRequest(AbstractModel):
    """DrainClusterVirtualNode request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodeName: Node name
        :type NodeName: str
        """
        self._ClusterId = None
        self._NodeName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodeName = params.get("NodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrainClusterVirtualNodeResponse(AbstractModel):
    """DrainClusterVirtualNode response structure.

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


class DriverVersion(AbstractModel):
    """Version information of GPU driver and CUDA

    """

    def __init__(self):
        r"""
        :param _Version: Version of GPU driver or CUDA
        :type Version: str
        :param _Name: Name of GPU driver or CUDA
        :type Name: str
        """
        self._Version = None
        self._Name = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECMEnhancedService(AbstractModel):
    """ECM enhanced services

    """

    def __init__(self):
        r"""
        :param _SecurityService: Whether Cloud Monitoring is enabled
        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.ECMRunMonitorServiceEnabled`
        :param _MonitorService: Whether Cloud Workload Protection is enabled
        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.ECMRunSecurityServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None

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


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = ECMRunMonitorServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = ECMRunSecurityServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECMRunMonitorServiceEnabled(AbstractModel):
    """ECM Cloud Monitoring

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether it is enabled
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
        


class ECMRunSecurityServiceEnabled(AbstractModel):
    """ECM Cloud Workload Protection

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether it is enabled
        :type Enabled: bool
        :param _Version: CWP version. Valid values: `0` (CWP Pro), `1` (CWP Pro)
        :type Version: int
        """
        self._Enabled = None
        self._Version = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECMZoneInstanceCountISP(AbstractModel):
    """Combination of the ECM instance AZ, number of instances, and ISP

    """

    def __init__(self):
        r"""
        :param _Zone: Instance AZ
        :type Zone: str
        :param _InstanceCount: Number of instances to be created in the current AZ
        :type InstanceCount: int
        :param _ISP: ISP
        :type ISP: str
        """
        self._Zone = None
        self._InstanceCount = None
        self._ISP = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceCount(self):
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ISP(self):
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceCount = params.get("InstanceCount")
        self._ISP = params.get("ISP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeArgsFlag(AbstractModel):
    """Edge cluster parameters

    """

    def __init__(self):
        r"""
        :param _Name: Parameter name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param _Type: Parameter type
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        :param _Usage: Parameter description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Usage: str
        :param _Default: Default value of the parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Default: str
        :param _Constraint: Valid value or range. Options: `[]` (it indicates a range, for example, “[1, 5]” indicates the parameter must be equal or larger than 1, and be equal or smaller than 5), and `()` (it indicates a valid value, for example, “('aa', 'bb')” indicates the parameter must be “aa” or “bb”. If it is left empty, the verification can be skipped.)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Constraint: str
        """
        self._Name = None
        self._Type = None
        self._Usage = None
        self._Default = None
        self._Constraint = None

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
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Constraint(self):
        return self._Constraint

    @Constraint.setter
    def Constraint(self, Constraint):
        self._Constraint = Constraint


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Usage = params.get("Usage")
        self._Default = params.get("Default")
        self._Constraint = params.get("Constraint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeAvailableExtraArgs(AbstractModel):
    """Custom parameters available for the edge cluster

    """

    def __init__(self):
        r"""
        :param _KubeAPIServer: kube-apiserver custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeAPIServer: list of EdgeArgsFlag
        :param _KubeControllerManager: kube-controller-manager custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeControllerManager: list of EdgeArgsFlag
        :param _KubeScheduler: kube-scheduler custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeScheduler: list of EdgeArgsFlag
        :param _Kubelet: kubelet custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Kubelet: list of EdgeArgsFlag
        """
        self._KubeAPIServer = None
        self._KubeControllerManager = None
        self._KubeScheduler = None
        self._Kubelet = None

    @property
    def KubeAPIServer(self):
        return self._KubeAPIServer

    @KubeAPIServer.setter
    def KubeAPIServer(self, KubeAPIServer):
        self._KubeAPIServer = KubeAPIServer

    @property
    def KubeControllerManager(self):
        return self._KubeControllerManager

    @KubeControllerManager.setter
    def KubeControllerManager(self, KubeControllerManager):
        self._KubeControllerManager = KubeControllerManager

    @property
    def KubeScheduler(self):
        return self._KubeScheduler

    @KubeScheduler.setter
    def KubeScheduler(self, KubeScheduler):
        self._KubeScheduler = KubeScheduler

    @property
    def Kubelet(self):
        return self._Kubelet

    @Kubelet.setter
    def Kubelet(self, Kubelet):
        self._Kubelet = Kubelet


    def _deserialize(self, params):
        if params.get("KubeAPIServer") is not None:
            self._KubeAPIServer = []
            for item in params.get("KubeAPIServer"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self._KubeAPIServer.append(obj)
        if params.get("KubeControllerManager") is not None:
            self._KubeControllerManager = []
            for item in params.get("KubeControllerManager"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self._KubeControllerManager.append(obj)
        if params.get("KubeScheduler") is not None:
            self._KubeScheduler = []
            for item in params.get("KubeScheduler"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self._KubeScheduler.append(obj)
        if params.get("Kubelet") is not None:
            self._Kubelet = []
            for item in params.get("Kubelet"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self._Kubelet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeCluster(AbstractModel):
    """Edge compute cluster information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _PodCIDR: Cluster Pod CIDR block
        :type PodCIDR: str
        :param _ServiceCIDR: Cluster service CIDR block
        :type ServiceCIDR: str
        :param _K8SVersion: 
        :type K8SVersion: str
        :param _Status: Cluster status
        :type Status: str
        :param _ClusterDesc: Cluster description
        :type ClusterDesc: str
        :param _CreatedTime: Cluster creation time
        :type CreatedTime: str
        :param _EdgeClusterVersion: Edge cluster version
        :type EdgeClusterVersion: str
        :param _MaxNodePodNum: Maximum number of Pods on the node
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MaxNodePodNum: int
        :param _ClusterAdvancedSettings: Cluster advanced settings
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.EdgeClusterAdvancedSettings`
        :param _Level: TKE edge cluster level
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Level: str
        :param _AutoUpgradeClusterLevel: Whether to support auto upgrade of cluster spec level
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutoUpgradeClusterLevel: bool
        :param _ChargeType: Cluster billing mode. Valid values: `POSTPAID_BY_HOUR`, `PREPAID`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _EdgeVersion: Edge cluster component version 
Note: This field may return null, indicating that no valid values can be obtained.
        :type EdgeVersion: str
        :param _TagSpecification: 
        :type TagSpecification: :class:`tencentcloud.tke.v20180525.models.TagSpecification`
        """
        self._ClusterId = None
        self._ClusterName = None
        self._VpcId = None
        self._PodCIDR = None
        self._ServiceCIDR = None
        self._K8SVersion = None
        self._Status = None
        self._ClusterDesc = None
        self._CreatedTime = None
        self._EdgeClusterVersion = None
        self._MaxNodePodNum = None
        self._ClusterAdvancedSettings = None
        self._Level = None
        self._AutoUpgradeClusterLevel = None
        self._ChargeType = None
        self._EdgeVersion = None
        self._TagSpecification = None

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
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def PodCIDR(self):
        return self._PodCIDR

    @PodCIDR.setter
    def PodCIDR(self, PodCIDR):
        self._PodCIDR = PodCIDR

    @property
    def ServiceCIDR(self):
        return self._ServiceCIDR

    @ServiceCIDR.setter
    def ServiceCIDR(self, ServiceCIDR):
        self._ServiceCIDR = ServiceCIDR

    @property
    def K8SVersion(self):
        return self._K8SVersion

    @K8SVersion.setter
    def K8SVersion(self, K8SVersion):
        self._K8SVersion = K8SVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterDesc(self):
        return self._ClusterDesc

    @ClusterDesc.setter
    def ClusterDesc(self, ClusterDesc):
        self._ClusterDesc = ClusterDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def EdgeClusterVersion(self):
        return self._EdgeClusterVersion

    @EdgeClusterVersion.setter
    def EdgeClusterVersion(self, EdgeClusterVersion):
        self._EdgeClusterVersion = EdgeClusterVersion

    @property
    def MaxNodePodNum(self):
        return self._MaxNodePodNum

    @MaxNodePodNum.setter
    def MaxNodePodNum(self, MaxNodePodNum):
        self._MaxNodePodNum = MaxNodePodNum

    @property
    def ClusterAdvancedSettings(self):
        return self._ClusterAdvancedSettings

    @ClusterAdvancedSettings.setter
    def ClusterAdvancedSettings(self, ClusterAdvancedSettings):
        self._ClusterAdvancedSettings = ClusterAdvancedSettings

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def AutoUpgradeClusterLevel(self):
        return self._AutoUpgradeClusterLevel

    @AutoUpgradeClusterLevel.setter
    def AutoUpgradeClusterLevel(self, AutoUpgradeClusterLevel):
        self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def EdgeVersion(self):
        return self._EdgeVersion

    @EdgeVersion.setter
    def EdgeVersion(self, EdgeVersion):
        self._EdgeVersion = EdgeVersion

    @property
    def TagSpecification(self):
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._VpcId = params.get("VpcId")
        self._PodCIDR = params.get("PodCIDR")
        self._ServiceCIDR = params.get("ServiceCIDR")
        self._K8SVersion = params.get("K8SVersion")
        self._Status = params.get("Status")
        self._ClusterDesc = params.get("ClusterDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._EdgeClusterVersion = params.get("EdgeClusterVersion")
        self._MaxNodePodNum = params.get("MaxNodePodNum")
        if params.get("ClusterAdvancedSettings") is not None:
            self._ClusterAdvancedSettings = EdgeClusterAdvancedSettings()
            self._ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        self._Level = params.get("Level")
        self._AutoUpgradeClusterLevel = params.get("AutoUpgradeClusterLevel")
        self._ChargeType = params.get("ChargeType")
        self._EdgeVersion = params.get("EdgeVersion")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = TagSpecification()
            self._TagSpecification._deserialize(params.get("TagSpecification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterAdvancedSettings(AbstractModel):
    """Edge cluster advanced settings

    """

    def __init__(self):
        r"""
        :param _ExtraArgs: Custom parameters of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.EdgeClusterExtraArgs`
        :param _Runtime: Runtime type. Valid values: "docker" (default), "containerd".
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Runtime: str
        :param _ProxyMode: Forwarding mode of kube-proxy. Valid values: "iptables" (default), "ipvs".
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProxyMode: str
        """
        self._ExtraArgs = None
        self._Runtime = None
        self._ProxyMode = None

    @property
    def ExtraArgs(self):
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs

    @property
    def Runtime(self):
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def ProxyMode(self):
        return self._ProxyMode

    @ProxyMode.setter
    def ProxyMode(self, ProxyMode):
        self._ProxyMode = ProxyMode


    def _deserialize(self, params):
        if params.get("ExtraArgs") is not None:
            self._ExtraArgs = EdgeClusterExtraArgs()
            self._ExtraArgs._deserialize(params.get("ExtraArgs"))
        self._Runtime = params.get("Runtime")
        self._ProxyMode = params.get("ProxyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterExtraArgs(AbstractModel):
    """Edge cluster master custom parameters

    """

    def __init__(self):
        r"""
        :param _KubeAPIServer: kube-apiserver custom parameter, in the format of ["k1=v1", "k1=v2"], for example: ["max-requests-inflight=500","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeAPIServer: list of str
        :param _KubeControllerManager: kube-controller-manager custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeControllerManager: list of str
        :param _KubeScheduler: kube-scheduler custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeScheduler: list of str
        """
        self._KubeAPIServer = None
        self._KubeControllerManager = None
        self._KubeScheduler = None

    @property
    def KubeAPIServer(self):
        return self._KubeAPIServer

    @KubeAPIServer.setter
    def KubeAPIServer(self, KubeAPIServer):
        self._KubeAPIServer = KubeAPIServer

    @property
    def KubeControllerManager(self):
        return self._KubeControllerManager

    @KubeControllerManager.setter
    def KubeControllerManager(self, KubeControllerManager):
        self._KubeControllerManager = KubeControllerManager

    @property
    def KubeScheduler(self):
        return self._KubeScheduler

    @KubeScheduler.setter
    def KubeScheduler(self, KubeScheduler):
        self._KubeScheduler = KubeScheduler


    def _deserialize(self, params):
        self._KubeAPIServer = params.get("KubeAPIServer")
        self._KubeControllerManager = params.get("KubeControllerManager")
        self._KubeScheduler = params.get("KubeScheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterInternalLB(AbstractModel):
    """Edge compute cluster private LB information

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether the private LB is enabled
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Enabled: bool
        :param _SubnetId: ID of the subnet associated with the private LB
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: list of str
        """
        self._Enabled = None
        self._SubnetId = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterPublicLB(AbstractModel):
    """Edge compute cluster public LB information

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether the public LB is enabled
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Enabled: bool
        :param _AllowFromCidrs: Public network CIDR block allowed to access
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AllowFromCidrs: list of str
        """
        self._Enabled = None
        self._AllowFromCidrs = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def AllowFromCidrs(self):
        return self._AllowFromCidrs

    @AllowFromCidrs.setter
    def AllowFromCidrs(self, AllowFromCidrs):
        self._AllowFromCidrs = AllowFromCidrs


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._AllowFromCidrs = params.get("AllowFromCidrs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClusterDeletionProtectionRequest(AbstractModel):
    """EnableClusterDeletionProtection request structure.

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
        


class EnableClusterDeletionProtectionResponse(AbstractModel):
    """EnableClusterDeletionProtection response structure.

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


class EnableVpcCniNetworkTypeRequest(AbstractModel):
    """EnableVpcCniNetworkType request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _VpcCniType: The VPC-CNI mode. `tke-route-eni`: Multi-IP ENI, `tke-direct-eni`: Independent ENI
        :type VpcCniType: str
        :param _EnableStaticIp: Whether to enable static IP address
        :type EnableStaticIp: bool
        :param _Subnets: The container subnet being used
        :type Subnets: list of str
        :param _ExpiredSeconds: Specifies when to release the IP after the Pod termination in static IP mode. It must be longer than 300 seconds. If this parameter is left empty, the IP address will never be released.
        :type ExpiredSeconds: int
        :param _SkipAddingNonMasqueradeCIDRs: Whether to skip adding the VPC IP range to `NonMasqueradeCIDRs` field of `ip-masq-agent-config`. Default value: `false`
        :type SkipAddingNonMasqueradeCIDRs: bool
        """
        self._ClusterId = None
        self._VpcCniType = None
        self._EnableStaticIp = None
        self._Subnets = None
        self._ExpiredSeconds = None
        self._SkipAddingNonMasqueradeCIDRs = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def VpcCniType(self):
        return self._VpcCniType

    @VpcCniType.setter
    def VpcCniType(self, VpcCniType):
        self._VpcCniType = VpcCniType

    @property
    def EnableStaticIp(self):
        return self._EnableStaticIp

    @EnableStaticIp.setter
    def EnableStaticIp(self, EnableStaticIp):
        self._EnableStaticIp = EnableStaticIp

    @property
    def Subnets(self):
        return self._Subnets

    @Subnets.setter
    def Subnets(self, Subnets):
        self._Subnets = Subnets

    @property
    def ExpiredSeconds(self):
        return self._ExpiredSeconds

    @ExpiredSeconds.setter
    def ExpiredSeconds(self, ExpiredSeconds):
        self._ExpiredSeconds = ExpiredSeconds

    @property
    def SkipAddingNonMasqueradeCIDRs(self):
        return self._SkipAddingNonMasqueradeCIDRs

    @SkipAddingNonMasqueradeCIDRs.setter
    def SkipAddingNonMasqueradeCIDRs(self, SkipAddingNonMasqueradeCIDRs):
        self._SkipAddingNonMasqueradeCIDRs = SkipAddingNonMasqueradeCIDRs


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._VpcCniType = params.get("VpcCniType")
        self._EnableStaticIp = params.get("EnableStaticIp")
        self._Subnets = params.get("Subnets")
        self._ExpiredSeconds = params.get("ExpiredSeconds")
        self._SkipAddingNonMasqueradeCIDRs = params.get("SkipAddingNonMasqueradeCIDRs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableVpcCniNetworkTypeResponse(AbstractModel):
    """EnableVpcCniNetworkType response structure.

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


class EnhancedService(AbstractModel):
    """Describes the configuration of enhanced services, such as Cloud Security and Cloud Monitor.

    """

    def __init__(self):
        r"""
        :param _SecurityService: Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.RunSecurityServiceEnabled`
        :param _MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.RunMonitorServiceEnabled`
        :param _AutomationService: Whether to enable the TAT service. If this parameter is not specified, the TAT service is enabled for public images and disabled for other images by default.
        :type AutomationService: :class:`tencentcloud.tke.v20180525.models.RunAutomationServiceEnabled`
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
        


class ExistedInstance(AbstractModel):
    """Information of existing instances

    """

    def __init__(self):
        r"""
        :param _Usable: Whether the instance supports being added to the cluster (TRUE: support; FALSE: not support).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Usable: bool
        :param _UnusableReason: Reason that the instance does not support being added.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnusableReason: str
        :param _AlreadyInCluster: ID of the cluster in which the instance currently resides.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlreadyInCluster: str
        :param _InstanceId: Instance ID, in the format of ins-xxxxxxxx.
        :type InstanceId: str
        :param _InstanceName: Instance name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param _PrivateIpAddresses: List of private IPs of the instance's primary ENI.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param _PublicIpAddresses: List of public IPs of the instance's primary ENI.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param _CreatedTime: Creation time, which follows the ISO8601 standard and uses UTC time. Format: YYYY-MM-DDThh:mm:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _CPU: Instance's number of CPU cores. Unit: cores.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CPU: int
        :param _Memory: Instance's memory capacity. Unit: GB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Memory: int
        :param _OsName: Operating system name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OsName: str
        :param _InstanceType: Instance model.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _AutoscalingGroupId: Auto scaling group ID
Note: This field may return null, indicating that no valid value was found.
        :type AutoscalingGroupId: str
        :param _InstanceChargeType: Instance billing method. Valid values: POSTPAID_BY_HOUR (pay-as-you-go hourly); CDHPAID (billed based on CDH, i.e., only CDH is billed but not the instances on CDH)
Note: This field may return null, indicating that no valid value was found.
        :type InstanceChargeType: str
        :param _IPv6Addresses: IPv6 address of the instance
Note: This field may return `null`, indicating that no valid values can be obtained.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IPv6Addresses: list of str
        """
        self._Usable = None
        self._UnusableReason = None
        self._AlreadyInCluster = None
        self._InstanceId = None
        self._InstanceName = None
        self._PrivateIpAddresses = None
        self._PublicIpAddresses = None
        self._CreatedTime = None
        self._CPU = None
        self._Memory = None
        self._OsName = None
        self._InstanceType = None
        self._AutoscalingGroupId = None
        self._InstanceChargeType = None
        self._IPv6Addresses = None

    @property
    def Usable(self):
        return self._Usable

    @Usable.setter
    def Usable(self, Usable):
        self._Usable = Usable

    @property
    def UnusableReason(self):
        return self._UnusableReason

    @UnusableReason.setter
    def UnusableReason(self, UnusableReason):
        self._UnusableReason = UnusableReason

    @property
    def AlreadyInCluster(self):
        return self._AlreadyInCluster

    @AlreadyInCluster.setter
    def AlreadyInCluster(self, AlreadyInCluster):
        self._AlreadyInCluster = AlreadyInCluster

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
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

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
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def AutoscalingGroupId(self):
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def IPv6Addresses(self):
        return self._IPv6Addresses

    @IPv6Addresses.setter
    def IPv6Addresses(self, IPv6Addresses):
        self._IPv6Addresses = IPv6Addresses


    def _deserialize(self, params):
        self._Usable = params.get("Usable")
        self._UnusableReason = params.get("UnusableReason")
        self._AlreadyInCluster = params.get("AlreadyInCluster")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._CreatedTime = params.get("CreatedTime")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._OsName = params.get("OsName")
        self._InstanceType = params.get("InstanceType")
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._IPv6Addresses = params.get("IPv6Addresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesForNode(AbstractModel):
    """Configuration parameters of existing nodes in different roles

    """

    def __init__(self):
        r"""
        :param _NodeRole: Node role. Values: MASTER_ETCD, WORKER. You only need to specify MASTER_ETCD when creating a self-deployed cluster (INDEPENDENT_CLUSTER).
        :type NodeRole: str
        :param _ExistedInstancesPara: Reinstallation parameter of existing instances
        :type ExistedInstancesPara: :class:`tencentcloud.tke.v20180525.models.ExistedInstancesPara`
        :param _InstanceAdvancedSettingsOverride: Advanced node setting, which overrides the InstanceAdvancedSettings item set at the cluster level (currently valid for the ExtraArgs node custom parameter only)
        :type InstanceAdvancedSettingsOverride: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _DesiredPodNumbers: When the custom PodCIDR mode is enabled for the cluster, you can specify the maximum number of pods per node.
        :type DesiredPodNumbers: list of int
        """
        self._NodeRole = None
        self._ExistedInstancesPara = None
        self._InstanceAdvancedSettingsOverride = None
        self._DesiredPodNumbers = None

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def ExistedInstancesPara(self):
        return self._ExistedInstancesPara

    @ExistedInstancesPara.setter
    def ExistedInstancesPara(self, ExistedInstancesPara):
        self._ExistedInstancesPara = ExistedInstancesPara

    @property
    def InstanceAdvancedSettingsOverride(self):
        return self._InstanceAdvancedSettingsOverride

    @InstanceAdvancedSettingsOverride.setter
    def InstanceAdvancedSettingsOverride(self, InstanceAdvancedSettingsOverride):
        self._InstanceAdvancedSettingsOverride = InstanceAdvancedSettingsOverride

    @property
    def DesiredPodNumbers(self):
        return self._DesiredPodNumbers

    @DesiredPodNumbers.setter
    def DesiredPodNumbers(self, DesiredPodNumbers):
        self._DesiredPodNumbers = DesiredPodNumbers


    def _deserialize(self, params):
        self._NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self._ExistedInstancesPara = ExistedInstancesPara()
            self._ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))
        if params.get("InstanceAdvancedSettingsOverride") is not None:
            self._InstanceAdvancedSettingsOverride = InstanceAdvancedSettings()
            self._InstanceAdvancedSettingsOverride._deserialize(params.get("InstanceAdvancedSettingsOverride"))
        self._DesiredPodNumbers = params.get("DesiredPodNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesPara(AbstractModel):
    """Reinstallation parameter of existing instances

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Cluster ID
        :type InstanceIds: list of str
        :param _InstanceAdvancedSettings: Additional parameter to be set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _EnhancedService: Enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitor and other services. If this parameter is not specified, Cloud Monitor and Cloud Security are enabled by default.
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param _LoginSettings: Node login information (currently only supports using Password or single KeyIds)
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param _SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the sgId field in the returned values of DescribeSecurityGroups. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId)
        :type SecurityGroupIds: list of str
        :param _HostName: When reinstalling the system, you can specify the HostName of the modified instance (when the cluster is in HostName mode, this parameter is required, and the rule name is the same as the [Create CVM Instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API HostName except for uppercase letters not being supported.
        :type HostName: str
        """
        self._InstanceIds = None
        self._InstanceAdvancedSettings = None
        self._EnhancedService = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._HostName = None

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

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
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionAddon(AbstractModel):
    """Information of the add-on selected for installation during cluster creation

    """

    def __init__(self):
        r"""
        :param _AddonName: Add-on name
        :type AddonName: str
        :param _AddonParam: Add-on information (description of the add-on resource object in JSON string format)
        :type AddonParam: str
        """
        self._AddonName = None
        self._AddonParam = None

    @property
    def AddonName(self):
        return self._AddonName

    @AddonName.setter
    def AddonName(self, AddonName):
        self._AddonName = AddonName

    @property
    def AddonParam(self):
        return self._AddonParam

    @AddonParam.setter
    def AddonParam(self, AddonParam):
        self._AddonParam = AddonParam


    def _deserialize(self, params):
        self._AddonName = params.get("AddonName")
        self._AddonParam = params.get("AddonParam")
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
        


class ForwardTKEEdgeApplicationRequestV3Request(AbstractModel):
    """ForwardTKEEdgeApplicationRequestV3 request structure.

    """

    def __init__(self):
        r"""
        :param _Method: Access to request the cluster add-on
        :type Method: str
        :param _Path: Path to request the cluster add-on
        :type Path: str
        :param _Accept: Data format allowed to receive the requested cluster add-on
        :type Accept: str
        :param _ContentType: Data format for requesting the cluster add-on
        :type ContentType: str
        :param _RequestBody: Data sent to request the cluster add-on
        :type RequestBody: str
        :param _ClusterName: Cluster name (for example, `cls-1234abcd`)
        :type ClusterName: str
        :param _EncodedBody: Whether to encode the request content
        :type EncodedBody: str
        """
        self._Method = None
        self._Path = None
        self._Accept = None
        self._ContentType = None
        self._RequestBody = None
        self._ClusterName = None
        self._EncodedBody = None

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Accept(self):
        return self._Accept

    @Accept.setter
    def Accept(self, Accept):
        self._Accept = Accept

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def RequestBody(self):
        return self._RequestBody

    @RequestBody.setter
    def RequestBody(self, RequestBody):
        self._RequestBody = RequestBody

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def EncodedBody(self):
        return self._EncodedBody

    @EncodedBody.setter
    def EncodedBody(self, EncodedBody):
        self._EncodedBody = EncodedBody


    def _deserialize(self, params):
        self._Method = params.get("Method")
        self._Path = params.get("Path")
        self._Accept = params.get("Accept")
        self._ContentType = params.get("ContentType")
        self._RequestBody = params.get("RequestBody")
        self._ClusterName = params.get("ClusterName")
        self._EncodedBody = params.get("EncodedBody")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardTKEEdgeApplicationRequestV3Response(AbstractModel):
    """ForwardTKEEdgeApplicationRequestV3 response structure.

    """

    def __init__(self):
        r"""
        :param _ResponseBody: Data returned after requesting the cluster add-on
        :type ResponseBody: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ResponseBody = None
        self._RequestId = None

    @property
    def ResponseBody(self):
        return self._ResponseBody

    @ResponseBody.setter
    def ResponseBody(self, ResponseBody):
        self._ResponseBody = ResponseBody

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResponseBody = params.get("ResponseBody")
        self._RequestId = params.get("RequestId")


class GPUArgs(AbstractModel):
    """GPU parameters, including GPU driver version, CDUA version, cuDNN version and whether to enable MIG.

    """

    def __init__(self):
        r"""
        :param _MIGEnable: Whether to enable MIG
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MIGEnable: bool
        :param _Driver: GPU driver version
        :type Driver: :class:`tencentcloud.tke.v20180525.models.DriverVersion`
        :param _CUDA: CUDA version
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CUDA: :class:`tencentcloud.tke.v20180525.models.DriverVersion`
        :param _CUDNN: cuDNN version
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CUDNN: :class:`tencentcloud.tke.v20180525.models.CUDNN`
        :param _CustomDriver: Custom GPU driver
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CustomDriver: :class:`tencentcloud.tke.v20180525.models.CustomDriver`
        """
        self._MIGEnable = None
        self._Driver = None
        self._CUDA = None
        self._CUDNN = None
        self._CustomDriver = None

    @property
    def MIGEnable(self):
        return self._MIGEnable

    @MIGEnable.setter
    def MIGEnable(self, MIGEnable):
        self._MIGEnable = MIGEnable

    @property
    def Driver(self):
        return self._Driver

    @Driver.setter
    def Driver(self, Driver):
        self._Driver = Driver

    @property
    def CUDA(self):
        return self._CUDA

    @CUDA.setter
    def CUDA(self, CUDA):
        self._CUDA = CUDA

    @property
    def CUDNN(self):
        return self._CUDNN

    @CUDNN.setter
    def CUDNN(self, CUDNN):
        self._CUDNN = CUDNN

    @property
    def CustomDriver(self):
        return self._CustomDriver

    @CustomDriver.setter
    def CustomDriver(self, CustomDriver):
        self._CustomDriver = CustomDriver


    def _deserialize(self, params):
        self._MIGEnable = params.get("MIGEnable")
        if params.get("Driver") is not None:
            self._Driver = DriverVersion()
            self._Driver._deserialize(params.get("Driver"))
        if params.get("CUDA") is not None:
            self._CUDA = DriverVersion()
            self._CUDA._deserialize(params.get("CUDA"))
        if params.get("CUDNN") is not None:
            self._CUDNN = CUDNN()
            self._CUDNN._deserialize(params.get("CUDNN"))
        if params.get("CustomDriver") is not None:
            self._CustomDriver = CustomDriver()
            self._CustomDriver._deserialize(params.get("CustomDriver"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetClusterLevelPriceRequest(AbstractModel):
    """GetClusterLevelPrice request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterLevel: The cluster model. It’s used for price query.
        :type ClusterLevel: str
        """
        self._ClusterLevel = None

    @property
    def ClusterLevel(self):
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel


    def _deserialize(self, params):
        self._ClusterLevel = params.get("ClusterLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetClusterLevelPriceResponse(AbstractModel):
    """GetClusterLevelPrice response structure.

    """

    def __init__(self):
        r"""
        :param _Cost: Discount price (unit: US cent)
        :type Cost: int
        :param _TotalCost: Original price (unit: US cent)
        :type TotalCost: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Cost = None
        self._TotalCost = None
        self._RequestId = None

    @property
    def Cost(self):
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def TotalCost(self):
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Cost = params.get("Cost")
        self._TotalCost = params.get("TotalCost")
        self._RequestId = params.get("RequestId")


class GetUpgradeInstanceProgressRequest(AbstractModel):
    """GetUpgradeInstanceProgress request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Limit: Maximum number of nodes to be queried
        :type Limit: int
        :param _Offset: The starting node for the query
        :type Offset: int
        """
        self._ClusterId = None
        self._Limit = None
        self._Offset = None

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUpgradeInstanceProgressResponse(AbstractModel):
    """GetUpgradeInstanceProgress response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total nodes to upgrade
        :type Total: int
        :param _Done: Total upgraded nodes
        :type Done: int
        :param _LifeState: The lifecycle of the upgrade task
process: running
paused: stopped
pausing: stopping
done: completed
timeout: timed out
aborted: canceled
        :type LifeState: str
        :param _Instances: Details of upgrade progress of each node
        :type Instances: list of InstanceUpgradeProgressItem
        :param _ClusterStatus: Current cluster status
        :type ClusterStatus: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradeClusterStatus`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Done = None
        self._LifeState = None
        self._Instances = None
        self._ClusterStatus = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Done(self):
        return self._Done

    @Done.setter
    def Done(self, Done):
        self._Done = Done

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Done = params.get("Done")
        self._LifeState = params.get("LifeState")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = InstanceUpgradeProgressItem()
                obj._deserialize(item)
                self._Instances.append(obj)
        if params.get("ClusterStatus") is not None:
            self._ClusterStatus = InstanceUpgradeClusterStatus()
            self._ClusterStatus._deserialize(params.get("ClusterStatus"))
        self._RequestId = params.get("RequestId")


class IPAddress(AbstractModel):
    """IP Address

    """

    def __init__(self):
        r"""
        :param _Type: Type. Valid values: `advertise`, `public`, and others
        :type Type: str
        :param _Ip: IP Address
        :type Ip: str
        :param _Port: Network port
        :type Port: int
        """
        self._Type = None
        self._Ip = None
        self._Port = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInstance(AbstractModel):
    """Image details

    """

    def __init__(self):
        r"""
        :param _Alias: Image alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _OsName: Operating system name
Note: this field may return null, indicating that no valid values can be obtained.
        :type OsName: str
        :param _ImageId: Image ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageId: str
        :param _OsCustomizeType: Container image tag, **DOCKER_CUSTOMIZE** (container customized tag), **GENERAL** (general tag, default value)
Note: this field may return null, indicating that no valid values can be obtained.
        :type OsCustomizeType: str
        """
        self._Alias = None
        self._OsName = None
        self._ImageId = None
        self._OsCustomizeType = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def OsCustomizeType(self):
        return self._OsCustomizeType

    @OsCustomizeType.setter
    def OsCustomizeType(self, OsCustomizeType):
        self._OsCustomizeType = OsCustomizeType


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._OsName = params.get("OsName")
        self._ImageId = params.get("ImageId")
        self._OsCustomizeType = params.get("OsCustomizeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallEdgeLogAgentRequest(AbstractModel):
    """InstallEdgeLogAgent request structure.

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
        


class InstallEdgeLogAgentResponse(AbstractModel):
    """InstallEdgeLogAgent response structure.

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


class Instance(AbstractModel):
    """Cluster's instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceRole: Node role: MASTER, WORKER, ETCD, MASTER_ETCD, and ALL. Default value: WORKER
        :type InstanceRole: str
        :param _FailedReason: Reason for instance exception (or initialization)
        :type FailedReason: str
        :param _InstanceState: Instance status (running, initializing, or failed)
        :type InstanceState: str
        :param _DrainStatus: Whether the instance is drained
Note: this field may return null, indicating that no valid value is obtained.
        :type DrainStatus: str
        :param _InstanceAdvancedSettings: Node settings
Note: this field may return null, indicating that no valid value is obtained.
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _CreatedTime: Creation time
        :type CreatedTime: str
        :param _LanIP: Node private IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type LanIP: str
        :param _NodePoolId: Resource pool ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type NodePoolId: str
        :param _AutoscalingGroupId: ID of the auto-scaling group
Note: this field may return null, indicating that no valid value is obtained.
        :type AutoscalingGroupId: str
        """
        self._InstanceId = None
        self._InstanceRole = None
        self._FailedReason = None
        self._InstanceState = None
        self._DrainStatus = None
        self._InstanceAdvancedSettings = None
        self._CreatedTime = None
        self._LanIP = None
        self._NodePoolId = None
        self._AutoscalingGroupId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def FailedReason(self):
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def DrainStatus(self):
        return self._DrainStatus

    @DrainStatus.setter
    def DrainStatus(self, DrainStatus):
        self._DrainStatus = DrainStatus

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def LanIP(self):
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def AutoscalingGroupId(self):
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceRole = params.get("InstanceRole")
        self._FailedReason = params.get("FailedReason")
        self._InstanceState = params.get("InstanceState")
        self._DrainStatus = params.get("DrainStatus")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self._CreatedTime = params.get("CreatedTime")
        self._LanIP = params.get("LanIP")
        self._NodePoolId = params.get("NodePoolId")
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """Describes K8s cluster configuration and related information.

    """

    def __init__(self):
        r"""
        :param _DesiredPodNumber: When the custom PodCIDR mode is enabled for the cluster, you can specify the maximum number of pods per node.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DesiredPodNumber: int
        :param _GPUArgs: GPU driver parameters
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type GPUArgs: :class:`tencentcloud.tke.v20180525.models.GPUArgs`
        :param _PreStartUserScript: Specifies the base64-encoded custom script to be executed before initialization of the node. It’s only valid for adding existing nodes for now.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PreStartUserScript: str
        :param _Taints: Node taint
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Taints: list of Taint
        :param _MountTarget: Data disk mount point. By default, no data disk is mounted. Data disks in ext3, ext4, or XFS file system formats will be mounted directly, while data disks in other file systems and unformatted data disks will automatically be formatted as ext4 (xfs for tlinux system) and then mounted. Please back up your data in advance. This setting is only applicable to CVMs with a single data disk.
Note: in multi-disk scenarios, use the DataDisks data structure below to set the corresponding information, such as cloud disk type, cloud disk size, mount path, and whether to perform formatting.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MountTarget: str
        :param _DockerGraphPath: Specified value of dockerd --graph. Default value: /var/lib/docker
Note: This field may return null, indicating that no valid value was found.
        :type DockerGraphPath: str
        :param _UserScript: Base64-encoded user script, which will be executed after the K8s component starts running. You need to ensure the reentrant and retry logic of the script. The script and its log files can be viewed at the node path: /data/ccs_userscript/. If you want to initialize nodes before adding them to the scheduling list, you can use this parameter together with the unschedulable parameter. After the final initialization of userScript is completed, add the kubectl uncordon nodename --kubeconfig=/root/.kube/config command to enable the node for scheduling.
Note: This field may return null, indicating that no valid value was found.
        :type UserScript: str
        :param _Unschedulable: Sets whether the added node is schedulable. 0 (default): schedulable; other values: unschedulable. After node initialization is completed, you can run kubectl uncordon nodename to enable this node for scheduling.
        :type Unschedulable: int
        :param _Labels: Node label array
Note: This field may return null, indicating that no valid value was found.
        :type Labels: list of Label
        :param _DataDisks: Mounting information of multiple data disks. When you create a node, ensure that the CVM purchase parameter specifies the information required for the purchase of multiple data disks. For example, the `DataDisks` under `RunInstancesPara` of the `CreateClusterInstances` API should be configured accordingly (Referto document of CreateClusterInstances API). When you add an existing node, ensure that the specified partition exists in the node.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DataDisks: list of DataDisk
        :param _ExtraArgs: Information about node custom parameters
Note: This field may return null, indicating that no valid value was found.
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        """
        self._DesiredPodNumber = None
        self._GPUArgs = None
        self._PreStartUserScript = None
        self._Taints = None
        self._MountTarget = None
        self._DockerGraphPath = None
        self._UserScript = None
        self._Unschedulable = None
        self._Labels = None
        self._DataDisks = None
        self._ExtraArgs = None

    @property
    def DesiredPodNumber(self):
        return self._DesiredPodNumber

    @DesiredPodNumber.setter
    def DesiredPodNumber(self, DesiredPodNumber):
        self._DesiredPodNumber = DesiredPodNumber

    @property
    def GPUArgs(self):
        return self._GPUArgs

    @GPUArgs.setter
    def GPUArgs(self, GPUArgs):
        self._GPUArgs = GPUArgs

    @property
    def PreStartUserScript(self):
        return self._PreStartUserScript

    @PreStartUserScript.setter
    def PreStartUserScript(self, PreStartUserScript):
        self._PreStartUserScript = PreStartUserScript

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def MountTarget(self):
        return self._MountTarget

    @MountTarget.setter
    def MountTarget(self, MountTarget):
        self._MountTarget = MountTarget

    @property
    def DockerGraphPath(self):
        return self._DockerGraphPath

    @DockerGraphPath.setter
    def DockerGraphPath(self, DockerGraphPath):
        self._DockerGraphPath = DockerGraphPath

    @property
    def UserScript(self):
        return self._UserScript

    @UserScript.setter
    def UserScript(self, UserScript):
        self._UserScript = UserScript

    @property
    def Unschedulable(self):
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def ExtraArgs(self):
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs


    def _deserialize(self, params):
        self._DesiredPodNumber = params.get("DesiredPodNumber")
        if params.get("GPUArgs") is not None:
            self._GPUArgs = GPUArgs()
            self._GPUArgs._deserialize(params.get("GPUArgs"))
        self._PreStartUserScript = params.get("PreStartUserScript")
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        self._MountTarget = params.get("MountTarget")
        self._DockerGraphPath = params.get("DockerGraphPath")
        self._UserScript = params.get("UserScript")
        self._Unschedulable = params.get("Unschedulable")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("ExtraArgs") is not None:
            self._ExtraArgs = InstanceExtraArgs()
            self._ExtraArgs._deserialize(params.get("ExtraArgs"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDataDiskMountSetting(AbstractModel):
    """Mounting configuration of the CVM instance data disk

    """

    def __init__(self):
        r"""
        :param _InstanceType: CVM instance type
        :type InstanceType: str
        :param _DataDisks: Data disk mounting information
        :type DataDisks: list of DataDisk
        :param _Zone: Availability zone where the CVM instance is located
        :type Zone: str
        """
        self._InstanceType = None
        self._DataDisks = None
        self._Zone = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtraArgs(AbstractModel):
    """Node custom parameter

    """

    def __init__(self):
        r"""
        :param _Kubelet: Kubelet custom parameter, in the format of ["k1=v1", "k1=v2"], for example: ["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"].
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Kubelet: list of str
        """
        self._Kubelet = None

    @property
    def Kubelet(self):
        return self._Kubelet

    @Kubelet.setter
    def Kubelet(self, Kubelet):
        self._Kubelet = Kubelet


    def _deserialize(self, params):
        self._Kubelet = params.get("Kubelet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeClusterStatus(AbstractModel):
    """Current status of the cluster during node upgrade

    """

    def __init__(self):
        r"""
        :param _PodTotal: Total Pods
        :type PodTotal: int
        :param _NotReadyPod: Total number of NotReady Pods
        :type NotReadyPod: int
        """
        self._PodTotal = None
        self._NotReadyPod = None

    @property
    def PodTotal(self):
        return self._PodTotal

    @PodTotal.setter
    def PodTotal(self, PodTotal):
        self._PodTotal = PodTotal

    @property
    def NotReadyPod(self):
        return self._NotReadyPod

    @NotReadyPod.setter
    def NotReadyPod(self, NotReadyPod):
        self._NotReadyPod = NotReadyPod


    def _deserialize(self, params):
        self._PodTotal = params.get("PodTotal")
        self._NotReadyPod = params.get("NotReadyPod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResult(AbstractModel):
    """Pre-upgrade check result of a node

    """

    def __init__(self):
        r"""
        :param _CheckPass: Whether the check is passed
        :type CheckPass: bool
        :param _Items: Array of check items
        :type Items: list of InstanceUpgradePreCheckResultItem
        :param _SinglePods: List of independent pods on this node
        :type SinglePods: list of str
        """
        self._CheckPass = None
        self._Items = None
        self._SinglePods = None

    @property
    def CheckPass(self):
        return self._CheckPass

    @CheckPass.setter
    def CheckPass(self, CheckPass):
        self._CheckPass = CheckPass

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def SinglePods(self):
        return self._SinglePods

    @SinglePods.setter
    def SinglePods(self, SinglePods):
        self._SinglePods = SinglePods


    def _deserialize(self, params):
        self._CheckPass = params.get("CheckPass")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = InstanceUpgradePreCheckResultItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._SinglePods = params.get("SinglePods")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResultItem(AbstractModel):
    """Check result for node upgrade

    """

    def __init__(self):
        r"""
        :param _Namespace: The namespace of the workload
        :type Namespace: str
        :param _WorkLoadKind: Workload type
        :type WorkLoadKind: str
        :param _WorkLoadName: Workload name
        :type WorkLoadName: str
        :param _Before: The number of running pods in the workload before draining the node
        :type Before: int
        :param _After: The number of running pods in the workload after draining the node
        :type After: int
        :param _Pods: The pod list of the workload on this node
        :type Pods: list of str
        """
        self._Namespace = None
        self._WorkLoadKind = None
        self._WorkLoadName = None
        self._Before = None
        self._After = None
        self._Pods = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def WorkLoadKind(self):
        return self._WorkLoadKind

    @WorkLoadKind.setter
    def WorkLoadKind(self, WorkLoadKind):
        self._WorkLoadKind = WorkLoadKind

    @property
    def WorkLoadName(self):
        return self._WorkLoadName

    @WorkLoadName.setter
    def WorkLoadName(self, WorkLoadName):
        self._WorkLoadName = WorkLoadName

    @property
    def Before(self):
        return self._Before

    @Before.setter
    def Before(self, Before):
        self._Before = Before

    @property
    def After(self):
        return self._After

    @After.setter
    def After(self, After):
        self._After = After

    @property
    def Pods(self):
        return self._Pods

    @Pods.setter
    def Pods(self, Pods):
        self._Pods = Pods


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._WorkLoadKind = params.get("WorkLoadKind")
        self._WorkLoadName = params.get("WorkLoadName")
        self._Before = params.get("Before")
        self._After = params.get("After")
        self._Pods = params.get("Pods")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeProgressItem(AbstractModel):
    """Upgrade progress of a node

    """

    def __init__(self):
        r"""
        :param _InstanceID: Node instance ID
        :type InstanceID: str
        :param _LifeState: Task lifecycle
process: running
paused: stopped
pausing: stopping
done: completed
timeout: timed out
aborted: canceled
pending: not started
        :type LifeState: str
        :param _StartAt: Upgrade start time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StartAt: str
        :param _EndAt: Upgrade end time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EndAt: str
        :param _CheckResult: Check result before upgrading
        :type CheckResult: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradePreCheckResult`
        :param _Detail: Upgrade steps details
        :type Detail: list of TaskStepInfo
        """
        self._InstanceID = None
        self._LifeState = None
        self._StartAt = None
        self._EndAt = None
        self._CheckResult = None
        self._Detail = None

    @property
    def InstanceID(self):
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def CheckResult(self):
        return self._CheckResult

    @CheckResult.setter
    def CheckResult(self, CheckResult):
        self._CheckResult = CheckResult

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._LifeState = params.get("LifeState")
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        if params.get("CheckResult") is not None:
            self._CheckResult = InstanceUpgradePreCheckResult()
            self._CheckResult._deserialize(params.get("CheckResult"))
        if params.get("Detail") is not None:
            self._Detail = []
            for item in params.get("Detail"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self._Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """k8s tags, generally exist as an array

    """

    def __init__(self):
        r"""
        :param _Name: Name in map list
        :type Name: str
        :param _Value: Value in map list
        :type Value: str
        """
        self._Name = None
        self._Value = None

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


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
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
        


class ManuallyAdded(AbstractModel):
    """Nodes that are manually added

    """

    def __init__(self):
        r"""
        :param _Joining: Number of nodes that are being added
        :type Joining: int
        :param _Initializing: Number of nodes that are being initialized
        :type Initializing: int
        :param _Normal: Number of normal nodes
        :type Normal: int
        :param _Total: Total number of nodes
        :type Total: int
        """
        self._Joining = None
        self._Initializing = None
        self._Normal = None
        self._Total = None

    @property
    def Joining(self):
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Joining = params.get("Joining")
        self._Initializing = params.get("Initializing")
        self._Normal = params.get("Normal")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterAsGroupAttribute: Cluster-associated scaling group attributes
        :type ClusterAsGroupAttribute: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupAttribute`
        """
        self._ClusterId = None
        self._ClusterAsGroupAttribute = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterAsGroupAttribute(self):
        return self._ClusterAsGroupAttribute

    @ClusterAsGroupAttribute.setter
    def ClusterAsGroupAttribute(self, ClusterAsGroupAttribute):
        self._ClusterAsGroupAttribute = ClusterAsGroupAttribute


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ClusterAsGroupAttribute") is not None:
            self._ClusterAsGroupAttribute = ClusterAsGroupAttribute()
            self._ClusterAsGroupAttribute._deserialize(params.get("ClusterAsGroupAttribute"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupAttribute response structure.

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


class ModifyClusterAsGroupOptionAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterAsGroupOption: Cluster auto scaling attributes
        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`
        """
        self._ClusterId = None
        self._ClusterAsGroupOption = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterAsGroupOption(self):
        return self._ClusterAsGroupOption

    @ClusterAsGroupOption.setter
    def ClusterAsGroupOption(self, ClusterAsGroupOption):
        self._ClusterAsGroupOption = ClusterAsGroupOption


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ClusterAsGroupOption") is not None:
            self._ClusterAsGroupOption = ClusterAsGroupOption()
            self._ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupOptionAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute response structure.

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


class ModifyClusterAttributeRequest(AbstractModel):
    """ModifyClusterAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ProjectId: Project of the Cluster
        :type ProjectId: int
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _ClusterDesc: Cluster description
        :type ClusterDesc: str
        :param _ClusterLevel: Cluster specification
        :type ClusterLevel: str
        :param _AutoUpgradeClusterLevel: Auto-upgrades cluster specification
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
        :param _QGPUShareEnable: Whether to enable qGPU Sharing
        :type QGPUShareEnable: bool
        """
        self._ClusterId = None
        self._ProjectId = None
        self._ClusterName = None
        self._ClusterDesc = None
        self._ClusterLevel = None
        self._AutoUpgradeClusterLevel = None
        self._QGPUShareEnable = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterDesc(self):
        return self._ClusterDesc

    @ClusterDesc.setter
    def ClusterDesc(self, ClusterDesc):
        self._ClusterDesc = ClusterDesc

    @property
    def ClusterLevel(self):
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel

    @property
    def AutoUpgradeClusterLevel(self):
        return self._AutoUpgradeClusterLevel

    @AutoUpgradeClusterLevel.setter
    def AutoUpgradeClusterLevel(self, AutoUpgradeClusterLevel):
        self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel

    @property
    def QGPUShareEnable(self):
        return self._QGPUShareEnable

    @QGPUShareEnable.setter
    def QGPUShareEnable(self, QGPUShareEnable):
        self._QGPUShareEnable = QGPUShareEnable


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ProjectId = params.get("ProjectId")
        self._ClusterName = params.get("ClusterName")
        self._ClusterDesc = params.get("ClusterDesc")
        self._ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self._AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
        self._QGPUShareEnable = params.get("QGPUShareEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAttributeResponse(AbstractModel):
    """ModifyClusterAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project of the Cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param _ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param _ClusterDesc: Cluster description
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterDesc: str
        :param _ClusterLevel: Cluster specification
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterLevel: str
        :param _AutoUpgradeClusterLevel: Auto-upgrades cluster specification
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
        :param _QGPUShareEnable: Whether to enable qGPU Sharing
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QGPUShareEnable: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProjectId = None
        self._ClusterName = None
        self._ClusterDesc = None
        self._ClusterLevel = None
        self._AutoUpgradeClusterLevel = None
        self._QGPUShareEnable = None
        self._RequestId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def ClusterDesc(self):
        return self._ClusterDesc

    @ClusterDesc.setter
    def ClusterDesc(self, ClusterDesc):
        self._ClusterDesc = ClusterDesc

    @property
    def ClusterLevel(self):
        return self._ClusterLevel

    @ClusterLevel.setter
    def ClusterLevel(self, ClusterLevel):
        self._ClusterLevel = ClusterLevel

    @property
    def AutoUpgradeClusterLevel(self):
        return self._AutoUpgradeClusterLevel

    @AutoUpgradeClusterLevel.setter
    def AutoUpgradeClusterLevel(self, AutoUpgradeClusterLevel):
        self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel

    @property
    def QGPUShareEnable(self):
        return self._QGPUShareEnable

    @QGPUShareEnable.setter
    def QGPUShareEnable(self, QGPUShareEnable):
        self._QGPUShareEnable = QGPUShareEnable

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ClusterName = params.get("ClusterName")
        self._ClusterDesc = params.get("ClusterDesc")
        self._ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self._AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self._AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
        self._QGPUShareEnable = params.get("QGPUShareEnable")
        self._RequestId = params.get("RequestId")


class ModifyClusterAuthenticationOptionsRequest(AbstractModel):
    """ModifyClusterAuthenticationOptions request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ServiceAccounts: ServiceAccount authentication configuration
        :type ServiceAccounts: :class:`tencentcloud.tke.v20180525.models.ServiceAccountAuthenticationOptions`
        :param _OIDCConfig: OIDC authentication configurations
        :type OIDCConfig: :class:`tencentcloud.tke.v20180525.models.OIDCConfigAuthenticationOptions`
        """
        self._ClusterId = None
        self._ServiceAccounts = None
        self._OIDCConfig = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ServiceAccounts(self):
        return self._ServiceAccounts

    @ServiceAccounts.setter
    def ServiceAccounts(self, ServiceAccounts):
        self._ServiceAccounts = ServiceAccounts

    @property
    def OIDCConfig(self):
        return self._OIDCConfig

    @OIDCConfig.setter
    def OIDCConfig(self, OIDCConfig):
        self._OIDCConfig = OIDCConfig


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("ServiceAccounts") is not None:
            self._ServiceAccounts = ServiceAccountAuthenticationOptions()
            self._ServiceAccounts._deserialize(params.get("ServiceAccounts"))
        if params.get("OIDCConfig") is not None:
            self._OIDCConfig = OIDCConfigAuthenticationOptions()
            self._OIDCConfig._deserialize(params.get("OIDCConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAuthenticationOptionsResponse(AbstractModel):
    """ModifyClusterAuthenticationOptions response structure.

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


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _SecurityPolicies: Security policy opens single IP or CIDR block to the Internet (for example: '192.168.1.0/24', with 'reject all' as the default).
        :type SecurityPolicies: list of str
        :param _SecurityGroup: Modify public network security group
        :type SecurityGroup: str
        """
        self._ClusterId = None
        self._SecurityPolicies = None
        self._SecurityGroup = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SecurityPolicies(self):
        return self._SecurityPolicies

    @SecurityPolicies.setter
    def SecurityPolicies(self, SecurityPolicies):
        self._SecurityPolicies = SecurityPolicies

    @property
    def SecurityGroup(self):
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SecurityPolicies = params.get("SecurityPolicies")
        self._SecurityGroup = params.get("SecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterEndpointSPResponse(AbstractModel):
    """ModifyClusterEndpointSP response structure.

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


class ModifyClusterNodePoolRequest(AbstractModel):
    """ModifyClusterNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _Name: Name
        :type Name: str
        :param _MaxNodesNum: Maximum number of nodes
        :type MaxNodesNum: int
        :param _MinNodesNum: Minimum number of nodes
        :type MinNodesNum: int
        :param _Labels: Labels
        :type Labels: list of Label
        :param _Taints: Taints
        :type Taints: list of Taint
        :param _EnableAutoscale: Indicates whether auto scaling is enabled.
        :type EnableAutoscale: bool
        :param _OsName: Operating system name
        :type OsName: str
        :param _OsCustomizeType: Image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
        :type OsCustomizeType: str
        :param _GPUArgs: GPU driver version, CUDA version, cuDNN version and wether to enable MIG
        :type GPUArgs: :class:`tencentcloud.tke.v20180525.models.GPUArgs`
        :param _UserScript: Base64-encoded custom script
        :type UserScript: str
        :param _IgnoreExistedNode: Ignore existing nodes when update `Label` and `Taint`
        :type IgnoreExistedNode: bool
        :param _ExtraArgs: Node custom parameter
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        :param _Tags: Resource tag
        :type Tags: list of Tag
        :param _Unschedulable: Sets whether the added node is schedulable. 0 (default): schedulable; other values: unschedulable. After node initialization is completed, you can run `kubectl uncordon nodename` to enable this node for scheduling.
        :type Unschedulable: int
        :param _DeletionProtection: Whether Deletion Protection is enabled
        :type DeletionProtection: bool
        :param _DockerGraphPath: Specified value of dockerd --graph. Default value: /var/lib/docker
        :type DockerGraphPath: str
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._Name = None
        self._MaxNodesNum = None
        self._MinNodesNum = None
        self._Labels = None
        self._Taints = None
        self._EnableAutoscale = None
        self._OsName = None
        self._OsCustomizeType = None
        self._GPUArgs = None
        self._UserScript = None
        self._IgnoreExistedNode = None
        self._ExtraArgs = None
        self._Tags = None
        self._Unschedulable = None
        self._DeletionProtection = None
        self._DockerGraphPath = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MaxNodesNum(self):
        return self._MaxNodesNum

    @MaxNodesNum.setter
    def MaxNodesNum(self, MaxNodesNum):
        self._MaxNodesNum = MaxNodesNum

    @property
    def MinNodesNum(self):
        return self._MinNodesNum

    @MinNodesNum.setter
    def MinNodesNum(self, MinNodesNum):
        self._MinNodesNum = MinNodesNum

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def EnableAutoscale(self):
        return self._EnableAutoscale

    @EnableAutoscale.setter
    def EnableAutoscale(self, EnableAutoscale):
        self._EnableAutoscale = EnableAutoscale

    @property
    def OsName(self):
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def OsCustomizeType(self):
        return self._OsCustomizeType

    @OsCustomizeType.setter
    def OsCustomizeType(self, OsCustomizeType):
        self._OsCustomizeType = OsCustomizeType

    @property
    def GPUArgs(self):
        return self._GPUArgs

    @GPUArgs.setter
    def GPUArgs(self, GPUArgs):
        self._GPUArgs = GPUArgs

    @property
    def UserScript(self):
        return self._UserScript

    @UserScript.setter
    def UserScript(self, UserScript):
        self._UserScript = UserScript

    @property
    def IgnoreExistedNode(self):
        return self._IgnoreExistedNode

    @IgnoreExistedNode.setter
    def IgnoreExistedNode(self, IgnoreExistedNode):
        self._IgnoreExistedNode = IgnoreExistedNode

    @property
    def ExtraArgs(self):
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Unschedulable(self):
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def DockerGraphPath(self):
        return self._DockerGraphPath

    @DockerGraphPath.setter
    def DockerGraphPath(self, DockerGraphPath):
        self._DockerGraphPath = DockerGraphPath


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._Name = params.get("Name")
        self._MaxNodesNum = params.get("MaxNodesNum")
        self._MinNodesNum = params.get("MinNodesNum")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        self._EnableAutoscale = params.get("EnableAutoscale")
        self._OsName = params.get("OsName")
        self._OsCustomizeType = params.get("OsCustomizeType")
        if params.get("GPUArgs") is not None:
            self._GPUArgs = GPUArgs()
            self._GPUArgs._deserialize(params.get("GPUArgs"))
        self._UserScript = params.get("UserScript")
        self._IgnoreExistedNode = params.get("IgnoreExistedNode")
        if params.get("ExtraArgs") is not None:
            self._ExtraArgs = InstanceExtraArgs()
            self._ExtraArgs._deserialize(params.get("ExtraArgs"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Unschedulable = params.get("Unschedulable")
        self._DeletionProtection = params.get("DeletionProtection")
        self._DockerGraphPath = params.get("DockerGraphPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNodePoolResponse(AbstractModel):
    """ModifyClusterNodePool response structure.

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


class ModifyClusterVirtualNodePoolRequest(AbstractModel):
    """ModifyClusterVirtualNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _Name: Node pool name
        :type Name: str
        :param _Labels: Virtual node labels
        :type Labels: list of Label
        :param _Taints: Virtual node taint
        :type Taints: list of Taint
        :param _DeletionProtection: Setting of deletion protection
        :type DeletionProtection: bool
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._Name = None
        self._Labels = None
        self._Taints = None
        self._DeletionProtection = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._Name = params.get("Name")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterVirtualNodePoolResponse(AbstractModel):
    """ModifyClusterVirtualNodePool response structure.

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


class ModifyNodePoolInstanceTypesRequest(AbstractModel):
    """ModifyNodePoolInstanceTypes request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _InstanceTypes: List of instance types
        :type InstanceTypes: list of str
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._InstanceTypes = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._InstanceTypes = params.get("InstanceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodePoolInstanceTypesResponse(AbstractModel):
    """ModifyNodePoolInstanceTypes response structure.

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


class ModifyPrometheusAlertRuleRequest(AbstractModel):
    """ModifyPrometheusAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _AlertRule: Alarm configurations
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`
        """
        self._InstanceId = None
        self._AlertRule = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AlertRule(self):
        return self._AlertRule

    @AlertRule.setter
    def AlertRule(self, AlertRule):
        self._AlertRule = AlertRule


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self._AlertRule = PrometheusAlertRuleDetail()
            self._AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAlertRuleResponse(AbstractModel):
    """ModifyPrometheusAlertRule response structure.

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


class NodeCountSummary(AbstractModel):
    """Node statistics list

    """

    def __init__(self):
        r"""
        :param _ManuallyAdded: Nodes that are manually managed
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ManuallyAdded: :class:`tencentcloud.tke.v20180525.models.ManuallyAdded`
        :param _AutoscalingAdded: Nodes that are automatically managed
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AutoscalingAdded: :class:`tencentcloud.tke.v20180525.models.AutoscalingAdded`
        """
        self._ManuallyAdded = None
        self._AutoscalingAdded = None

    @property
    def ManuallyAdded(self):
        return self._ManuallyAdded

    @ManuallyAdded.setter
    def ManuallyAdded(self, ManuallyAdded):
        self._ManuallyAdded = ManuallyAdded

    @property
    def AutoscalingAdded(self):
        return self._AutoscalingAdded

    @AutoscalingAdded.setter
    def AutoscalingAdded(self, AutoscalingAdded):
        self._AutoscalingAdded = AutoscalingAdded


    def _deserialize(self, params):
        if params.get("ManuallyAdded") is not None:
            self._ManuallyAdded = ManuallyAdded()
            self._ManuallyAdded._deserialize(params.get("ManuallyAdded"))
        if params.get("AutoscalingAdded") is not None:
            self._AutoscalingAdded = AutoscalingAdded()
            self._AutoscalingAdded._deserialize(params.get("AutoscalingAdded"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePool(AbstractModel):
    """Node pool description

    """

    def __init__(self):
        r"""
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _Name: Node pool name
        :type Name: str
        :param _ClusterInstanceId: Cluster instance ID
        :type ClusterInstanceId: str
        :param _LifeState: The lifecycle state of the current node pool. Valid values: `creating`, `normal`, `updating`, `deleting`, and `deleted`.
        :type LifeState: str
        :param _LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param _AutoscalingGroupId: Auto-scaling group ID
        :type AutoscalingGroupId: str
        :param _Labels: Labels
        :type Labels: list of Label
        :param _Taints: Array of taint
        :type Taints: list of Taint
        :param _NodeCountSummary: Node list
        :type NodeCountSummary: :class:`tencentcloud.tke.v20180525.models.NodeCountSummary`
        :param _AutoscalingGroupStatus: 
        :type AutoscalingGroupStatus: str
        :param _MaxNodesNum: Maximum number of nodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MaxNodesNum: int
        :param _MinNodesNum: Minimum number of nodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MinNodesNum: int
        :param _DesiredNodesNum: Desired number of nodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type DesiredNodesNum: int
        :param _NodePoolOs: The operating system of the node pool
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NodePoolOs: str
        :param _OsCustomizeType: Container image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
Note: this field may return `null`, indicating that no valid value is obtained.
        :type OsCustomizeType: str
        :param _ImageId: Image ID
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ImageId: str
        :param _DesiredPodNum: This parameter is required when the custom PodCIDR mode is enabled for the cluster.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type DesiredPodNum: int
        :param _UserScript: Custom script
Note: this field may return `null`, indicating that no valid value is obtained.
        :type UserScript: str
        :param _Tags: Resource tag
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _DeletionProtection: Whether Deletion Protection is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeletionProtection: bool
        """
        self._NodePoolId = None
        self._Name = None
        self._ClusterInstanceId = None
        self._LifeState = None
        self._LaunchConfigurationId = None
        self._AutoscalingGroupId = None
        self._Labels = None
        self._Taints = None
        self._NodeCountSummary = None
        self._AutoscalingGroupStatus = None
        self._MaxNodesNum = None
        self._MinNodesNum = None
        self._DesiredNodesNum = None
        self._NodePoolOs = None
        self._OsCustomizeType = None
        self._ImageId = None
        self._DesiredPodNum = None
        self._UserScript = None
        self._Tags = None
        self._DeletionProtection = None

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ClusterInstanceId(self):
        return self._ClusterInstanceId

    @ClusterInstanceId.setter
    def ClusterInstanceId(self, ClusterInstanceId):
        self._ClusterInstanceId = ClusterInstanceId

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def AutoscalingGroupId(self):
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def NodeCountSummary(self):
        return self._NodeCountSummary

    @NodeCountSummary.setter
    def NodeCountSummary(self, NodeCountSummary):
        self._NodeCountSummary = NodeCountSummary

    @property
    def AutoscalingGroupStatus(self):
        return self._AutoscalingGroupStatus

    @AutoscalingGroupStatus.setter
    def AutoscalingGroupStatus(self, AutoscalingGroupStatus):
        self._AutoscalingGroupStatus = AutoscalingGroupStatus

    @property
    def MaxNodesNum(self):
        return self._MaxNodesNum

    @MaxNodesNum.setter
    def MaxNodesNum(self, MaxNodesNum):
        self._MaxNodesNum = MaxNodesNum

    @property
    def MinNodesNum(self):
        return self._MinNodesNum

    @MinNodesNum.setter
    def MinNodesNum(self, MinNodesNum):
        self._MinNodesNum = MinNodesNum

    @property
    def DesiredNodesNum(self):
        return self._DesiredNodesNum

    @DesiredNodesNum.setter
    def DesiredNodesNum(self, DesiredNodesNum):
        self._DesiredNodesNum = DesiredNodesNum

    @property
    def NodePoolOs(self):
        return self._NodePoolOs

    @NodePoolOs.setter
    def NodePoolOs(self, NodePoolOs):
        self._NodePoolOs = NodePoolOs

    @property
    def OsCustomizeType(self):
        return self._OsCustomizeType

    @OsCustomizeType.setter
    def OsCustomizeType(self, OsCustomizeType):
        self._OsCustomizeType = OsCustomizeType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def DesiredPodNum(self):
        return self._DesiredPodNum

    @DesiredPodNum.setter
    def DesiredPodNum(self, DesiredPodNum):
        self._DesiredPodNum = DesiredPodNum

    @property
    def UserScript(self):
        return self._UserScript

    @UserScript.setter
    def UserScript(self, UserScript):
        self._UserScript = UserScript

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection


    def _deserialize(self, params):
        self._NodePoolId = params.get("NodePoolId")
        self._Name = params.get("Name")
        self._ClusterInstanceId = params.get("ClusterInstanceId")
        self._LifeState = params.get("LifeState")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        if params.get("NodeCountSummary") is not None:
            self._NodeCountSummary = NodeCountSummary()
            self._NodeCountSummary._deserialize(params.get("NodeCountSummary"))
        self._AutoscalingGroupStatus = params.get("AutoscalingGroupStatus")
        self._MaxNodesNum = params.get("MaxNodesNum")
        self._MinNodesNum = params.get("MinNodesNum")
        self._DesiredNodesNum = params.get("DesiredNodesNum")
        self._NodePoolOs = params.get("NodePoolOs")
        self._OsCustomizeType = params.get("OsCustomizeType")
        self._ImageId = params.get("ImageId")
        self._DesiredPodNum = params.get("DesiredPodNum")
        self._UserScript = params.get("UserScript")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePoolOption(AbstractModel):
    """The options for adding the existing node to the node pool

    """

    def __init__(self):
        r"""
        :param _AddToNodePool: Whether to add to the node pool.
        :type AddToNodePool: bool
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _InheritConfigurationFromNodePool: Whether to inherit the node pool configuration.
        :type InheritConfigurationFromNodePool: bool
        """
        self._AddToNodePool = None
        self._NodePoolId = None
        self._InheritConfigurationFromNodePool = None

    @property
    def AddToNodePool(self):
        return self._AddToNodePool

    @AddToNodePool.setter
    def AddToNodePool(self, AddToNodePool):
        self._AddToNodePool = AddToNodePool

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def InheritConfigurationFromNodePool(self):
        return self._InheritConfigurationFromNodePool

    @InheritConfigurationFromNodePool.setter
    def InheritConfigurationFromNodePool(self, InheritConfigurationFromNodePool):
        self._InheritConfigurationFromNodePool = InheritConfigurationFromNodePool


    def _deserialize(self, params):
        self._AddToNodePool = params.get("AddToNodePool")
        self._NodePoolId = params.get("NodePoolId")
        self._InheritConfigurationFromNodePool = params.get("InheritConfigurationFromNodePool")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OIDCConfigAuthenticationOptions(AbstractModel):
    """OIDC authentication related configurations

    """

    def __init__(self):
        r"""
        :param _AutoCreateOIDCConfig: Creating an identity provider
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AutoCreateOIDCConfig: bool
        :param _AutoCreateClientId: Creating ClientId of the identity provider
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AutoCreateClientId: list of str
        :param _AutoInstallPodIdentityWebhookAddon: Creating the PodIdentityWebhook component
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AutoInstallPodIdentityWebhookAddon: bool
        """
        self._AutoCreateOIDCConfig = None
        self._AutoCreateClientId = None
        self._AutoInstallPodIdentityWebhookAddon = None

    @property
    def AutoCreateOIDCConfig(self):
        return self._AutoCreateOIDCConfig

    @AutoCreateOIDCConfig.setter
    def AutoCreateOIDCConfig(self, AutoCreateOIDCConfig):
        self._AutoCreateOIDCConfig = AutoCreateOIDCConfig

    @property
    def AutoCreateClientId(self):
        return self._AutoCreateClientId

    @AutoCreateClientId.setter
    def AutoCreateClientId(self, AutoCreateClientId):
        self._AutoCreateClientId = AutoCreateClientId

    @property
    def AutoInstallPodIdentityWebhookAddon(self):
        return self._AutoInstallPodIdentityWebhookAddon

    @AutoInstallPodIdentityWebhookAddon.setter
    def AutoInstallPodIdentityWebhookAddon(self, AutoInstallPodIdentityWebhookAddon):
        self._AutoInstallPodIdentityWebhookAddon = AutoInstallPodIdentityWebhookAddon


    def _deserialize(self, params):
        self._AutoCreateOIDCConfig = params.get("AutoCreateOIDCConfig")
        self._AutoCreateClientId = params.get("AutoCreateClientId")
        self._AutoInstallPodIdentityWebhookAddon = params.get("AutoInstallPodIdentityWebhookAddon")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodLimitsByType(AbstractModel):
    """The maximum number of Pods in VPC-CNI mode supported by a model

    """

    def __init__(self):
        r"""
        :param _TKERouteENINonStaticIP: The number of Pods supported by a TKE shared ENI in non-static IP address mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TKERouteENINonStaticIP: int
        :param _TKERouteENIStaticIP: The number of Pods supported by a TKE shared ENI in static IP address mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TKERouteENIStaticIP: int
        :param _TKEDirectENI: The number of Pods supported by TKE independent ENI mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TKEDirectENI: int
        """
        self._TKERouteENINonStaticIP = None
        self._TKERouteENIStaticIP = None
        self._TKEDirectENI = None

    @property
    def TKERouteENINonStaticIP(self):
        return self._TKERouteENINonStaticIP

    @TKERouteENINonStaticIP.setter
    def TKERouteENINonStaticIP(self, TKERouteENINonStaticIP):
        self._TKERouteENINonStaticIP = TKERouteENINonStaticIP

    @property
    def TKERouteENIStaticIP(self):
        return self._TKERouteENIStaticIP

    @TKERouteENIStaticIP.setter
    def TKERouteENIStaticIP(self, TKERouteENIStaticIP):
        self._TKERouteENIStaticIP = TKERouteENIStaticIP

    @property
    def TKEDirectENI(self):
        return self._TKEDirectENI

    @TKEDirectENI.setter
    def TKEDirectENI(self, TKEDirectENI):
        self._TKEDirectENI = TKEDirectENI


    def _deserialize(self, params):
        self._TKERouteENINonStaticIP = params.get("TKERouteENINonStaticIP")
        self._TKERouteENIStaticIP = params.get("TKERouteENIStaticIP")
        self._TKEDirectENI = params.get("TKEDirectENI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodLimitsInstance(AbstractModel):
    """The model information and the maximum supported number of Pods in the VPC-CNI mode

    """

    def __init__(self):
        r"""
        :param _Zone: The availability zone where the model is located
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param _InstanceFamily: The instance family to which the model belongs
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type InstanceFamily: str
        :param _InstanceType: Instance type
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type InstanceType: str
        :param _PodLimits: The maximum number of Pods in the VPC-CNI mode supported by the model
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PodLimits: :class:`tencentcloud.tke.v20180525.models.PodLimitsByType`
        """
        self._Zone = None
        self._InstanceFamily = None
        self._InstanceType = None
        self._PodLimits = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PodLimits(self):
        return self._PodLimits

    @PodLimits.setter
    def PodLimits(self, PodLimits):
        self._PodLimits = PodLimits


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceFamily = params.get("InstanceFamily")
        self._InstanceType = params.get("InstanceType")
        if params.get("PodLimits") is not None:
            self._PodLimits = PodLimitsByType()
            self._PodLimits._deserialize(params.get("PodLimits"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRule(AbstractModel):
    """PROM instance alarm rule

    """

    def __init__(self):
        r"""
        :param _Name: Rule name
        :type Name: str
        :param _Rule: PromQL contents
        :type Rule: str
        :param _Labels: Additional labels
        :type Labels: list of Label
        :param _Template: Alarm delivery template
        :type Template: str
        :param _For: Duration
        :type For: str
        :param _Describe: Rule description
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Describe: str
        :param _Annotations: Refer to annotations in prometheus rule
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Annotations: list of Label
        :param _RuleState: Alarm rule status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RuleState: int
        """
        self._Name = None
        self._Rule = None
        self._Labels = None
        self._Template = None
        self._For = None
        self._Describe = None
        self._Annotations = None
        self._RuleState = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rule(self):
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Template(self):
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def For(self):
        return self._For

    @For.setter
    def For(self, For):
        self._For = For

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def RuleState(self):
        return self._RuleState

    @RuleState.setter
    def RuleState(self, RuleState):
        self._RuleState = RuleState


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Rule = params.get("Rule")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._Template = params.get("Template")
        self._For = params.get("For")
        self._Describe = params.get("Describe")
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Label()
                obj._deserialize(item)
                self._Annotations.append(obj)
        self._RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRuleDetail(AbstractModel):
    """The alarm configuration

    """

    def __init__(self):
        r"""
        :param _Name: Rule name
        :type Name: str
        :param _Rules: Rule list
        :type Rules: list of PrometheusAlertRule
        :param _UpdatedAt: Last modification time
        :type UpdatedAt: str
        :param _Notification: Alarm delivery methods
        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotification`
        :param _Id: Alarm rule ID
        :type Id: str
        :param _TemplateId: If the alarm is delivered via a template, the TemplateId is the template ID.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TemplateId: str
        :param _Interval: Alarm interval
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Interval: str
        """
        self._Name = None
        self._Rules = None
        self._UpdatedAt = None
        self._Notification = None
        self._Id = None
        self._TemplateId = None
        self._Interval = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Notification(self):
        return self._Notification

    @Notification.setter
    def Notification(self, Notification):
        self._Notification = Notification

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("Notification") is not None:
            self._Notification = PrometheusNotification()
            self._Notification._deserialize(params.get("Notification"))
        self._Id = params.get("Id")
        self._TemplateId = params.get("TemplateId")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusGrafanaInfo(AbstractModel):
    """The grafana information in the managed PROM instance

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether it is enabled
        :type Enabled: bool
        :param _Domain: Domain name. It will be effective only when the public network access is enabled.
        :type Domain: str
        :param _Address: The private network or public network address
        :type Address: str
        :param _Internet: Whether the public network access is enabled.
`close`: the public network access is not enabled
`opening`: the public network access is being enabled
`open`: the public network access is enabled
        :type Internet: str
        :param _AdminUser: The user name of the grafana admin
        :type AdminUser: str
        """
        self._Enabled = None
        self._Domain = None
        self._Address = None
        self._Internet = None
        self._AdminUser = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Internet(self):
        return self._Internet

    @Internet.setter
    def Internet(self, Internet):
        self._Internet = Internet

    @property
    def AdminUser(self):
        return self._AdminUser

    @AdminUser.setter
    def AdminUser(self, AdminUser):
        self._AdminUser = AdminUser


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Domain = params.get("Domain")
        self._Address = params.get("Address")
        self._Internet = params.get("Internet")
        self._AdminUser = params.get("AdminUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusNotification(AbstractModel):
    """amp alarm channel configuration

    """

    def __init__(self):
        r"""
        :param _Enabled: Whether it is enabled
        :type Enabled: bool
        :param _RepeatInterval: Convergence time
        :type RepeatInterval: str
        :param _TimeRangeStart: Start time
        :type TimeRangeStart: str
        :param _TimeRangeEnd: End time
        :type TimeRangeEnd: str
        :param _NotifyWay: Alarm delivery method. Valid values: `SMS`, `EMAIL`, `CALL`, and `WECHAT`
It respectively represents SMS, email, phone calls, and WeChat.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type NotifyWay: list of str
        :param _ReceiverGroups: The alarm recipient group (user group)
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ReceiverGroups: list of int non-negative
        :param _PhoneNotifyOrder: The alarm sequence of phone calls
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneNotifyOrder: list of int non-negative
        :param _PhoneCircleTimes: The number of phone call alarms
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneCircleTimes: int
        :param _PhoneInnerInterval: Dialing interval in seconds within one polling
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneInnerInterval: int
        :param _PhoneCircleInterval: Polling interval in seconds
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneCircleInterval: int
        :param _PhoneArriveNotice: Phone call alarm arrival notification
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneArriveNotice: bool
        :param _Type: Channel type. Default value: `amp`. The following channels are supported:
amp
webhook
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param _WebHook: This parameter is required if `Type` is `webhook`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type WebHook: str
        """
        self._Enabled = None
        self._RepeatInterval = None
        self._TimeRangeStart = None
        self._TimeRangeEnd = None
        self._NotifyWay = None
        self._ReceiverGroups = None
        self._PhoneNotifyOrder = None
        self._PhoneCircleTimes = None
        self._PhoneInnerInterval = None
        self._PhoneCircleInterval = None
        self._PhoneArriveNotice = None
        self._Type = None
        self._WebHook = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def RepeatInterval(self):
        return self._RepeatInterval

    @RepeatInterval.setter
    def RepeatInterval(self, RepeatInterval):
        self._RepeatInterval = RepeatInterval

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
    def NotifyWay(self):
        return self._NotifyWay

    @NotifyWay.setter
    def NotifyWay(self, NotifyWay):
        self._NotifyWay = NotifyWay

    @property
    def ReceiverGroups(self):
        return self._ReceiverGroups

    @ReceiverGroups.setter
    def ReceiverGroups(self, ReceiverGroups):
        self._ReceiverGroups = ReceiverGroups

    @property
    def PhoneNotifyOrder(self):
        return self._PhoneNotifyOrder

    @PhoneNotifyOrder.setter
    def PhoneNotifyOrder(self, PhoneNotifyOrder):
        self._PhoneNotifyOrder = PhoneNotifyOrder

    @property
    def PhoneCircleTimes(self):
        return self._PhoneCircleTimes

    @PhoneCircleTimes.setter
    def PhoneCircleTimes(self, PhoneCircleTimes):
        self._PhoneCircleTimes = PhoneCircleTimes

    @property
    def PhoneInnerInterval(self):
        return self._PhoneInnerInterval

    @PhoneInnerInterval.setter
    def PhoneInnerInterval(self, PhoneInnerInterval):
        self._PhoneInnerInterval = PhoneInnerInterval

    @property
    def PhoneCircleInterval(self):
        return self._PhoneCircleInterval

    @PhoneCircleInterval.setter
    def PhoneCircleInterval(self, PhoneCircleInterval):
        self._PhoneCircleInterval = PhoneCircleInterval

    @property
    def PhoneArriveNotice(self):
        return self._PhoneArriveNotice

    @PhoneArriveNotice.setter
    def PhoneArriveNotice(self, PhoneArriveNotice):
        self._PhoneArriveNotice = PhoneArriveNotice

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WebHook(self):
        return self._WebHook

    @WebHook.setter
    def WebHook(self, WebHook):
        self._WebHook = WebHook


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._RepeatInterval = params.get("RepeatInterval")
        self._TimeRangeStart = params.get("TimeRangeStart")
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        self._NotifyWay = params.get("NotifyWay")
        self._ReceiverGroups = params.get("ReceiverGroups")
        self._PhoneNotifyOrder = params.get("PhoneNotifyOrder")
        self._PhoneCircleTimes = params.get("PhoneCircleTimes")
        self._PhoneInnerInterval = params.get("PhoneInnerInterval")
        self._PhoneCircleInterval = params.get("PhoneCircleInterval")
        self._PhoneArriveNotice = params.get("PhoneArriveNotice")
        self._Type = params.get("Type")
        self._WebHook = params.get("WebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstance(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _RegionName: Region name
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionName: str
        :param _RegionId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param _Status: Region status
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _FeatureGates: Status of region-related features (return all attributes in JSON format)
Note: this field may return null, indicating that no valid values can be obtained.
        :type FeatureGates: str
        :param _Alias: Region abbreviation
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param _Remark: Whitelisted location
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self._RegionName = None
        self._RegionId = None
        self._Status = None
        self._FeatureGates = None
        self._Alias = None
        self._Remark = None

    @property
    def RegionName(self):
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FeatureGates(self):
        return self._FeatureGates

    @FeatureGates.setter
    def FeatureGates(self, FeatureGates):
        self._FeatureGates = FeatureGates

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        self._Status = params.get("Status")
        self._FeatureGates = params.get("FeatureGates")
        self._Alias = params.get("Alias")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolRequest(AbstractModel):
    """RemoveNodeFromNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _InstanceIds: The node ID list. Up to 100 nodes can be removed at a time.
        :type InstanceIds: list of str
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._InstanceIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolResponse(AbstractModel):
    """RemoveNodeFromNodePool response structure.

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


class ResourceDeleteOption(AbstractModel):
    """The policy to deal with resources in the cluster when the cluster is deleted.

    """

    def __init__(self):
        r"""
        :param _ResourceType: Resource type, for example `CBS`
        :type ResourceType: str
        :param _DeleteMode: Specifies the policy to deal with resources in the cluster when the cluster is deleted. It can be `terminate` or `retain`.
        :type DeleteMode: str
        """
        self._ResourceType = None
        self._DeleteMode = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def DeleteMode(self):
        return self._DeleteMode

    @DeleteMode.setter
    def DeleteMode(self, DeleteMode):
        self._DeleteMode = DeleteMode


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._DeleteMode = params.get("DeleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsage(AbstractModel):
    """Cluster resource usage

    """

    def __init__(self):
        r"""
        :param _Name: Resource type
        :type Name: str
        :param _Usage: Resource usage
        :type Usage: int
        :param _Details: Resource usage details
        :type Details: list of ResourceUsageDetail
        """
        self._Name = None
        self._Usage = None
        self._Details = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Details(self):
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Usage = params.get("Usage")
        if params.get("Details") is not None:
            self._Details = []
            for item in params.get("Details"):
                obj = ResourceUsageDetail()
                obj._deserialize(item)
                self._Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsageDetail(AbstractModel):
    """Resource usage details

    """

    def __init__(self):
        r"""
        :param _Name: Resource name
        :type Name: str
        :param _Usage: Resource usage
        :type Usage: int
        """
        self._Name = None
        self._Usage = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Usage = params.get("Usage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteInfo(AbstractModel):
    """Object of cluster route

    """

    def __init__(self):
        r"""
        :param _RouteTableName: Route table name.
        :type RouteTableName: str
        :param _DestinationCidrBlock: Destination CIDR.
        :type DestinationCidrBlock: str
        :param _GatewayIp: Next hop address.
        :type GatewayIp: str
        """
        self._RouteTableName = None
        self._DestinationCidrBlock = None
        self._GatewayIp = None

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def DestinationCidrBlock(self):
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock

    @property
    def GatewayIp(self):
        return self._GatewayIp

    @GatewayIp.setter
    def GatewayIp(self, GatewayIp):
        self._GatewayIp = GatewayIp


    def _deserialize(self, params):
        self._RouteTableName = params.get("RouteTableName")
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        self._GatewayIp = params.get("GatewayIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableConflict(AbstractModel):
    """Object of route table conflict

    """

    def __init__(self):
        r"""
        :param _RouteTableType: Route table type.
        :type RouteTableType: str
        :param _RouteTableCidrBlock: Route table CIDR.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableCidrBlock: str
        :param _RouteTableName: Route table name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableName: str
        :param _RouteTableId: Route table ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableId: str
        """
        self._RouteTableType = None
        self._RouteTableCidrBlock = None
        self._RouteTableName = None
        self._RouteTableId = None

    @property
    def RouteTableType(self):
        return self._RouteTableType

    @RouteTableType.setter
    def RouteTableType(self, RouteTableType):
        self._RouteTableType = RouteTableType

    @property
    def RouteTableCidrBlock(self):
        return self._RouteTableCidrBlock

    @RouteTableCidrBlock.setter
    def RouteTableCidrBlock(self, RouteTableCidrBlock):
        self._RouteTableCidrBlock = RouteTableCidrBlock

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def RouteTableId(self):
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId


    def _deserialize(self, params):
        self._RouteTableType = params.get("RouteTableType")
        self._RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self._RouteTableName = params.get("RouteTableName")
        self._RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableInfo(AbstractModel):
    """Object of cluster route table

    """

    def __init__(self):
        r"""
        :param _RouteTableName: Route table name.
        :type RouteTableName: str
        :param _RouteTableCidrBlock: Route table CIDR.
        :type RouteTableCidrBlock: str
        :param _VpcId: VPC instance ID.
        :type VpcId: str
        """
        self._RouteTableName = None
        self._RouteTableCidrBlock = None
        self._VpcId = None

    @property
    def RouteTableName(self):
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def RouteTableCidrBlock(self):
        return self._RouteTableCidrBlock

    @RouteTableCidrBlock.setter
    def RouteTableCidrBlock(self, RouteTableCidrBlock):
        self._RouteTableCidrBlock = RouteTableCidrBlock

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._RouteTableName = params.get("RouteTableName")
        self._RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class RunInstancesForNode(AbstractModel):
    """Node configuration parameters of different roles

    """

    def __init__(self):
        r"""
        :param _NodeRole: Node role. Values: MASTER_ETCD, WORKER. You only need to specify MASTER_ETCD when creating a self-deployed cluster (INDEPENDENT_CLUSTER).
        :type NodeRole: str
        :param _RunInstancesPara: Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the API for [creating a CVM instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1). Pass any parameter other than common parameters. ImageId will be replaced with the image corresponding to the TKE cluster operating system.
        :type RunInstancesPara: list of str
        :param _InstanceAdvancedSettingsOverrides: An advanced node setting. This parameter overrides the InstanceAdvancedSettings item set at the cluster level and corresponds to RunInstancesPara in a one-to-one sequential manner (currently valid for the ExtraArgs node custom parameter only).
        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings
        """
        self._NodeRole = None
        self._RunInstancesPara = None
        self._InstanceAdvancedSettingsOverrides = None

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def RunInstancesPara(self):
        return self._RunInstancesPara

    @RunInstancesPara.setter
    def RunInstancesPara(self, RunInstancesPara):
        self._RunInstancesPara = RunInstancesPara

    @property
    def InstanceAdvancedSettingsOverrides(self):
        return self._InstanceAdvancedSettingsOverrides

    @InstanceAdvancedSettingsOverrides.setter
    def InstanceAdvancedSettingsOverrides(self, InstanceAdvancedSettingsOverrides):
        self._InstanceAdvancedSettingsOverrides = InstanceAdvancedSettingsOverrides


    def _deserialize(self, params):
        self._NodeRole = params.get("NodeRole")
        self._RunInstancesPara = params.get("RunInstancesPara")
        if params.get("InstanceAdvancedSettingsOverrides") is not None:
            self._InstanceAdvancedSettingsOverrides = []
            for item in params.get("InstanceAdvancedSettingsOverrides"):
                obj = InstanceAdvancedSettings()
                obj._deserialize(item)
                self._InstanceAdvancedSettingsOverrides.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class ServiceAccountAuthenticationOptions(AbstractModel):
    """ServiceAccount authentication configuration

    """

    def __init__(self):
        r"""
        :param _UseTKEDefault: Use TKE default issuer and jwksuri
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UseTKEDefault: bool
        :param _Issuer: service-account-issuer
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Issuer: str
        :param _JWKSURI: service-account-jwks-uri
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type JWKSURI: str
        :param _AutoCreateDiscoveryAnonymousAuth: If it is set to `true`, a RABC rule is automatically created to allow anonymous users to access `/.well-known/openid-configuration` and `/openid/v1/jwks`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoCreateDiscoveryAnonymousAuth: bool
        """
        self._UseTKEDefault = None
        self._Issuer = None
        self._JWKSURI = None
        self._AutoCreateDiscoveryAnonymousAuth = None

    @property
    def UseTKEDefault(self):
        return self._UseTKEDefault

    @UseTKEDefault.setter
    def UseTKEDefault(self, UseTKEDefault):
        self._UseTKEDefault = UseTKEDefault

    @property
    def Issuer(self):
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def JWKSURI(self):
        return self._JWKSURI

    @JWKSURI.setter
    def JWKSURI(self, JWKSURI):
        self._JWKSURI = JWKSURI

    @property
    def AutoCreateDiscoveryAnonymousAuth(self):
        return self._AutoCreateDiscoveryAnonymousAuth

    @AutoCreateDiscoveryAnonymousAuth.setter
    def AutoCreateDiscoveryAnonymousAuth(self, AutoCreateDiscoveryAnonymousAuth):
        self._AutoCreateDiscoveryAnonymousAuth = AutoCreateDiscoveryAnonymousAuth


    def _deserialize(self, params):
        self._UseTKEDefault = params.get("UseTKEDefault")
        self._Issuer = params.get("Issuer")
        self._JWKSURI = params.get("JWKSURI")
        self._AutoCreateDiscoveryAnonymousAuth = params.get("AutoCreateDiscoveryAnonymousAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNodePoolNodeProtectionRequest(AbstractModel):
    """SetNodePoolNodeProtection request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _InstanceIds: Node ID
        :type InstanceIds: list of str
        :param _ProtectedFromScaleIn: Whether the node needs removal protection
        :type ProtectedFromScaleIn: bool
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._InstanceIds = None
        self._ProtectedFromScaleIn = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProtectedFromScaleIn(self):
        return self._ProtectedFromScaleIn

    @ProtectedFromScaleIn.setter
    def ProtectedFromScaleIn(self, ProtectedFromScaleIn):
        self._ProtectedFromScaleIn = ProtectedFromScaleIn


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._InstanceIds = params.get("InstanceIds")
        self._ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNodePoolNodeProtectionResponse(AbstractModel):
    """SetNodePoolNodeProtection response structure.

    """

    def __init__(self):
        r"""
        :param _SucceedInstanceIds: ID of the node that has successfully set the removal protection
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SucceedInstanceIds: list of str
        :param _FailedInstanceIds: ID of the node that fails to set the removal protection
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FailedInstanceIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SucceedInstanceIds = None
        self._FailedInstanceIds = None
        self._RequestId = None

    @property
    def SucceedInstanceIds(self):
        return self._SucceedInstanceIds

    @SucceedInstanceIds.setter
    def SucceedInstanceIds(self, SucceedInstanceIds):
        self._SucceedInstanceIds = SucceedInstanceIds

    @property
    def FailedInstanceIds(self):
        return self._FailedInstanceIds

    @FailedInstanceIds.setter
    def FailedInstanceIds(self, FailedInstanceIds):
        self._FailedInstanceIds = FailedInstanceIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SucceedInstanceIds = params.get("SucceedInstanceIds")
        self._FailedInstanceIds = params.get("FailedInstanceIds")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """The type of resource the label is bound to. Type currently supported is **cluster**.

    """

    def __init__(self):
        r"""
        :param _Key: Tag key.
        :type Key: str
        :param _Value: Tag value.
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
    """List of tag descriptions. By specifying this parameter, you can bind tags to corresponding resource instances at the same time. Currently, only tags are bound to cloud host instances.

    """

    def __init__(self):
        r"""
        :param _ResourceType: The type of resource that the tag is bound to. The type currently supported is `cluster`.
        :type ResourceType: str
        :param _Tags: List of tag pairs
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
        


class Taint(AbstractModel):
    """Kubernetes Taint

    """

    def __init__(self):
        r"""
        :param _Key: Key of the taint
        :type Key: str
        :param _Value: Value of the taint
        :type Value: str
        :param _Effect: Effect of the taint
        :type Effect: str
        """
        self._Key = None
        self._Value = None
        self._Effect = None

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

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Effect = params.get("Effect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStepInfo(AbstractModel):
    """Task step information

    """

    def __init__(self):
        r"""
        :param _Step: Step name
        :type Step: str
        :param _LifeState: Lifecycle
pending: the step is not started
running: the step is in progress
success: the step is completed
failed: the step failed
        :type LifeState: str
        :param _StartAt: Step start time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StartAt: str
        :param _EndAt: Step end time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EndAt: str
        :param _FailedMsg: If the lifecycle of the step is failed, this field will display the error information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FailedMsg: str
        """
        self._Step = None
        self._LifeState = None
        self._StartAt = None
        self._EndAt = None
        self._FailedMsg = None

    @property
    def Step(self):
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def EndAt(self):
        return self._EndAt

    @EndAt.setter
    def EndAt(self, EndAt):
        self._EndAt = EndAt

    @property
    def FailedMsg(self):
        return self._FailedMsg

    @FailedMsg.setter
    def FailedMsg(self, FailedMsg):
        self._FailedMsg = FailedMsg


    def _deserialize(self, params):
        self._Step = params.get("Step")
        self._LifeState = params.get("LifeState")
        self._StartAt = params.get("StartAt")
        self._EndAt = params.get("EndAt")
        self._FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnavailableReason(AbstractModel):
    """Reason for unavailability

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _Reason: Reason
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Reason: str
        """
        self._InstanceId = None
        self._Reason = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallEdgeLogAgentRequest(AbstractModel):
    """UninstallEdgeLogAgent request structure.

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
        


class UninstallEdgeLogAgentResponse(AbstractModel):
    """UninstallEdgeLogAgent response structure.

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


class UpdateClusterKubeconfigRequest(AbstractModel):
    """UpdateClusterKubeconfig request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: The cluster ID.
        :type ClusterId: str
        :param _SubAccounts: List of sub-account UINs. If it’s not specified, the SubUin used to invoke this API is used.
        :type SubAccounts: list of str
        """
        self._ClusterId = None
        self._SubAccounts = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def SubAccounts(self):
        return self._SubAccounts

    @SubAccounts.setter
    def SubAccounts(self, SubAccounts):
        self._SubAccounts = SubAccounts


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._SubAccounts = params.get("SubAccounts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClusterKubeconfigResponse(AbstractModel):
    """UpdateClusterKubeconfig response structure.

    """

    def __init__(self):
        r"""
        :param _UpdatedSubAccounts: List of updated sub-account UINs 
Note: This parameter may return null, indicating that no valid values can be obtained.
        :type UpdatedSubAccounts: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UpdatedSubAccounts = None
        self._RequestId = None

    @property
    def UpdatedSubAccounts(self):
        return self._UpdatedSubAccounts

    @UpdatedSubAccounts.setter
    def UpdatedSubAccounts(self, UpdatedSubAccounts):
        self._UpdatedSubAccounts = UpdatedSubAccounts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UpdatedSubAccounts = params.get("UpdatedSubAccounts")
        self._RequestId = params.get("RequestId")


class UpdateClusterVersionRequest(AbstractModel):
    """UpdateClusterVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _DstVersion: The version that needs to upgrade to
        :type DstVersion: str
        :param _ExtraArgs: Cluster custom parameter
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        :param _MaxNotReadyPercent: The maximum tolerable number of unavailable pods
        :type MaxNotReadyPercent: float
        :param _SkipPreCheck: Whether to skip the precheck
        :type SkipPreCheck: bool
        """
        self._ClusterId = None
        self._DstVersion = None
        self._ExtraArgs = None
        self._MaxNotReadyPercent = None
        self._SkipPreCheck = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DstVersion(self):
        return self._DstVersion

    @DstVersion.setter
    def DstVersion(self, DstVersion):
        self._DstVersion = DstVersion

    @property
    def ExtraArgs(self):
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs

    @property
    def MaxNotReadyPercent(self):
        return self._MaxNotReadyPercent

    @MaxNotReadyPercent.setter
    def MaxNotReadyPercent(self, MaxNotReadyPercent):
        self._MaxNotReadyPercent = MaxNotReadyPercent

    @property
    def SkipPreCheck(self):
        return self._SkipPreCheck

    @SkipPreCheck.setter
    def SkipPreCheck(self, SkipPreCheck):
        self._SkipPreCheck = SkipPreCheck


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DstVersion = params.get("DstVersion")
        if params.get("ExtraArgs") is not None:
            self._ExtraArgs = ClusterExtraArgs()
            self._ExtraArgs._deserialize(params.get("ExtraArgs"))
        self._MaxNotReadyPercent = params.get("MaxNotReadyPercent")
        self._SkipPreCheck = params.get("SkipPreCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClusterVersionResponse(AbstractModel):
    """UpdateClusterVersion response structure.

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


class UpdateEdgeClusterVersionRequest(AbstractModel):
    """UpdateEdgeClusterVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _EdgeVersion: Target version
        :type EdgeVersion: str
        :param _RegistryPrefix: Prefix of the image repository of a custom edge component
        :type RegistryPrefix: str
        :param _SkipPreCheck: Whether to skip precheck
        :type SkipPreCheck: bool
        """
        self._ClusterId = None
        self._EdgeVersion = None
        self._RegistryPrefix = None
        self._SkipPreCheck = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EdgeVersion(self):
        return self._EdgeVersion

    @EdgeVersion.setter
    def EdgeVersion(self, EdgeVersion):
        self._EdgeVersion = EdgeVersion

    @property
    def RegistryPrefix(self):
        return self._RegistryPrefix

    @RegistryPrefix.setter
    def RegistryPrefix(self, RegistryPrefix):
        self._RegistryPrefix = RegistryPrefix

    @property
    def SkipPreCheck(self):
        return self._SkipPreCheck

    @SkipPreCheck.setter
    def SkipPreCheck(self, SkipPreCheck):
        self._SkipPreCheck = SkipPreCheck


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._EdgeVersion = params.get("EdgeVersion")
        self._RegistryPrefix = params.get("RegistryPrefix")
        self._SkipPreCheck = params.get("SkipPreCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEdgeClusterVersionResponse(AbstractModel):
    """UpdateEdgeClusterVersion response structure.

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


class UpgradeAbleInstancesItem(AbstractModel):
    """Upgradeable node information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Node ID
        :type InstanceId: str
        :param _Version: The current version of the node
        :type Version: str
        :param _LatestVersion: The latest minor version of the current version
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LatestVersion: str
        :param _RuntimeVersion: RuntimeVersion
        :type RuntimeVersion: str
        :param _RuntimeLatestVersion: RuntimeLatestVersion
        :type RuntimeLatestVersion: str
        """
        self._InstanceId = None
        self._Version = None
        self._LatestVersion = None
        self._RuntimeVersion = None
        self._RuntimeLatestVersion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LatestVersion(self):
        return self._LatestVersion

    @LatestVersion.setter
    def LatestVersion(self, LatestVersion):
        self._LatestVersion = LatestVersion

    @property
    def RuntimeVersion(self):
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def RuntimeLatestVersion(self):
        return self._RuntimeLatestVersion

    @RuntimeLatestVersion.setter
    def RuntimeLatestVersion(self, RuntimeLatestVersion):
        self._RuntimeLatestVersion = RuntimeLatestVersion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Version = params.get("Version")
        self._LatestVersion = params.get("LatestVersion")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._RuntimeLatestVersion = params.get("RuntimeLatestVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesRequest(AbstractModel):
    """UpgradeClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Operation: create: starting an upgrade task
pause: pausing the task
resume: continuing the task
abort: stopping the task
        :type Operation: str
        :param _UpgradeType: Upgrade type. It’s only required when `Operation` is set as `create`.
reset: the reinstallation and upgrade of major version
hot: the hot upgrade of minor version
major: in-place upgrade of major version
        :type UpgradeType: str
        :param _InstanceIds: List of nodes that need to upgrade
        :type InstanceIds: list of str
        :param _ResetParam: This parameter is used when the node joins the cluster again. Refer to the API of creating one or more cluster nodes.
        :type ResetParam: :class:`tencentcloud.tke.v20180525.models.UpgradeNodeResetParam`
        :param _SkipPreCheck: Whether to skip the pre-upgrade check of the node
        :type SkipPreCheck: bool
        :param _MaxNotReadyPercent: The maximum tolerable proportion of unavailable pods
        :type MaxNotReadyPercent: float
        :param _UpgradeRunTime: Whether to upgrade node runtime. Values: `true`, `false` (default).
        :type UpgradeRunTime: bool
        """
        self._ClusterId = None
        self._Operation = None
        self._UpgradeType = None
        self._InstanceIds = None
        self._ResetParam = None
        self._SkipPreCheck = None
        self._MaxNotReadyPercent = None
        self._UpgradeRunTime = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Operation(self):
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def UpgradeType(self):
        return self._UpgradeType

    @UpgradeType.setter
    def UpgradeType(self, UpgradeType):
        self._UpgradeType = UpgradeType

    @property
    def InstanceIds(self):
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ResetParam(self):
        return self._ResetParam

    @ResetParam.setter
    def ResetParam(self, ResetParam):
        self._ResetParam = ResetParam

    @property
    def SkipPreCheck(self):
        return self._SkipPreCheck

    @SkipPreCheck.setter
    def SkipPreCheck(self, SkipPreCheck):
        self._SkipPreCheck = SkipPreCheck

    @property
    def MaxNotReadyPercent(self):
        return self._MaxNotReadyPercent

    @MaxNotReadyPercent.setter
    def MaxNotReadyPercent(self, MaxNotReadyPercent):
        self._MaxNotReadyPercent = MaxNotReadyPercent

    @property
    def UpgradeRunTime(self):
        return self._UpgradeRunTime

    @UpgradeRunTime.setter
    def UpgradeRunTime(self, UpgradeRunTime):
        self._UpgradeRunTime = UpgradeRunTime


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Operation = params.get("Operation")
        self._UpgradeType = params.get("UpgradeType")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ResetParam") is not None:
            self._ResetParam = UpgradeNodeResetParam()
            self._ResetParam._deserialize(params.get("ResetParam"))
        self._SkipPreCheck = params.get("SkipPreCheck")
        self._MaxNotReadyPercent = params.get("MaxNotReadyPercent")
        self._UpgradeRunTime = params.get("UpgradeRunTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesResponse(AbstractModel):
    """UpgradeClusterInstances response structure.

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


class UpgradeNodeResetParam(AbstractModel):
    """Node upgrade and reinstallation parameters

    """

    def __init__(self):
        r"""
        :param _InstanceAdvancedSettings: Additional parameters set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param _EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param _LoginSettings: Node login information. For now, it only supports Password or a single KeyIds
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param _SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the `sgId` field in the response of `DescribeSecurityGroups`. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId.)
        :type SecurityGroupIds: list of str
        """
        self._InstanceAdvancedSettings = None
        self._EnhancedService = None
        self._LoginSettings = None
        self._SecurityGroupIds = None

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def EnhancedService(self):
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

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


    def _deserialize(self, params):
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionInstance(AbstractModel):
    """Version Info

    """

    def __init__(self):
        r"""
        :param _Name: Version name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param _Version: Version Info
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Version: str
        :param _Remark: Remark
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self._Name = None
        self._Version = None
        self._Remark = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Version = params.get("Version")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualNode(AbstractModel):
    """Virtual node

    """

    def __init__(self):
        r"""
        :param _Name: Virtual node name
        :type Name: str
        :param _SubnetId: Subnet of the virtual node
        :type SubnetId: str
        :param _Phase: Virtual node status
        :type Phase: str
        :param _CreatedTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        """
        self._Name = None
        self._SubnetId = None
        self._Phase = None
        self._CreatedTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Phase(self):
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SubnetId = params.get("SubnetId")
        self._Phase = params.get("Phase")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualNodePool(AbstractModel):
    """Virtual node pool

    """

    def __init__(self):
        r"""
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _SubnetIds: List of subnets
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetIds: list of str
        :param _Name: Node pool name
        :type Name: str
        :param _LifeState: Node pool lifecycle status
        :type LifeState: str
        :param _Labels: Virtual node labels
Note: This field may return null, indicating that no valid values can be obtained.
        :type Labels: list of Label
        :param _Taints: Virtual node taint
Note: This field may return null, indicating that no valid values can be obtained.
        :type Taints: list of Taint
        """
        self._NodePoolId = None
        self._SubnetIds = None
        self._Name = None
        self._LifeState = None
        self._Labels = None
        self._Taints = None

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints


    def _deserialize(self, params):
        self._NodePoolId = params.get("NodePoolId")
        self._SubnetIds = params.get("SubnetIds")
        self._Name = params.get("Name")
        self._LifeState = params.get("LifeState")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VirtualNodeSpec(AbstractModel):
    """Virtual node

    """

    def __init__(self):
        r"""
        :param _DisplayName: Node display name
        :type DisplayName: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        :param _Tags: Tencent Cloud tags
        :type Tags: list of Tag
        """
        self._DisplayName = None
        self._SubnetId = None
        self._Tags = None

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DisplayName = params.get("DisplayName")
        self._SubnetId = params.get("SubnetId")
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
        