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


class Annotation(AbstractModel):
    """Annotations in k8s, generally existing as an array

    """

    def __init__(self):
        r"""
        :param _Name: Name in the map list
        :type Name: str
        :param _Value: Value in the map list
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Name in the map list
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Value in the map list
        :rtype: str
        """
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
        


class AutoUpgradeOptions(AbstractModel):
    """Ops window settings of managed node pools

    """

    def __init__(self):
        r"""
        :param _AutoUpgradeStartTime: Automatic upgrade start time
Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoUpgradeStartTime: str
        :param _Duration: Automatic upgrade duration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Duration: str
        :param _WeeklyPeriod: Ops date
Note: This field may return "null", indicating that no valid value can be obtained.
        :type WeeklyPeriod: list of str
        """
        self._AutoUpgradeStartTime = None
        self._Duration = None
        self._WeeklyPeriod = None

    @property
    def AutoUpgradeStartTime(self):
        """Automatic upgrade start time
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._AutoUpgradeStartTime

    @AutoUpgradeStartTime.setter
    def AutoUpgradeStartTime(self, AutoUpgradeStartTime):
        self._AutoUpgradeStartTime = AutoUpgradeStartTime

    @property
    def Duration(self):
        """Automatic upgrade duration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def WeeklyPeriod(self):
        """Ops date
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._WeeklyPeriod

    @WeeklyPeriod.setter
    def WeeklyPeriod(self, WeeklyPeriod):
        self._WeeklyPeriod = WeeklyPeriod


    def _deserialize(self, params):
        self._AutoUpgradeStartTime = params.get("AutoUpgradeStartTime")
        self._Duration = params.get("Duration")
        self._WeeklyPeriod = params.get("WeeklyPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoscalingAdded(AbstractModel):
    """Nodes for automatic scaling

    """

    def __init__(self):
        r"""
        :param _Joining: Number of nodes being added
        :type Joining: int
        :param _Initializing: Number of nodes being initialized
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
        """Number of nodes being added
        :rtype: int
        """
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        """Number of nodes being initialized
        :rtype: int
        """
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        """Number of normal nodes
        :rtype: int
        """
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        """Total number of nodes
        :rtype: int
        """
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
        


class CreateHealthCheckPolicyRequest(AbstractModel):
    """CreateHealthCheckPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _HealthCheckPolicy: Health check policy
        :type HealthCheckPolicy: :class:`tencentcloud.tke.v20220501.models.HealthCheckPolicy`
        """
        self._ClusterId = None
        self._HealthCheckPolicy = None

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
    def HealthCheckPolicy(self):
        """Health check policy
        :rtype: :class:`tencentcloud.tke.v20220501.models.HealthCheckPolicy`
        """
        return self._HealthCheckPolicy

    @HealthCheckPolicy.setter
    def HealthCheckPolicy(self, HealthCheckPolicy):
        self._HealthCheckPolicy = HealthCheckPolicy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("HealthCheckPolicy") is not None:
            self._HealthCheckPolicy = HealthCheckPolicy()
            self._HealthCheckPolicy._deserialize(params.get("HealthCheckPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHealthCheckPolicyResponse(AbstractModel):
    """CreateHealthCheckPolicy response structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckPolicyName: Health check policy name
        :type HealthCheckPolicyName: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthCheckPolicyName = None
        self._RequestId = None

    @property
    def HealthCheckPolicyName(self):
        """Health check policy name
        :rtype: str
        """
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

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
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._RequestId = params.get("RequestId")


class CreateNativeNodePoolParam(AbstractModel):
    """Native node pool creation parameters

    """

    def __init__(self):
        r"""
        :param _Scaling: Node pool scaling configuration
        :type Scaling: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        :param _SubnetIds: Subnet list
        :type SubnetIds: list of str
        :param _InstanceChargeType: Node billing type. PREPAID: Monthly subscription; POSTPAID_BY_HOUR: Pay-as-you-go (default);
        :type InstanceChargeType: str
        :param _SystemDisk: System disk configuration
        :type SystemDisk: :class:`tencentcloud.tke.v20220501.models.Disk`
        :param _InstanceTypes: List of models
        :type InstanceTypes: list of str
        :param _SecurityGroupIds: Security group list
        :type SecurityGroupIds: list of str
        :param _UpgradeSettings: Automatic upgrade configuration
        :type UpgradeSettings: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        :param _AutoRepair: Whether to enable self-healing capability
        :type AutoRepair: bool
        :param _InstanceChargePrepaid: Billing configuration of monthly subscription models
        :type InstanceChargePrepaid: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        :param _Management: Management parameter configuration of node pools
        :type Management: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        :param _HealthCheckPolicyName: Fault self-healing rule name
        :type HealthCheckPolicyName: str
        :param _HostNamePattern: hostname pattern string of native node pools
        :type HostNamePattern: str
        :param _KubeletArgs: kubelet custom parameters
        :type KubeletArgs: list of str
        :param _Lifecycle: Predefined script
        :type Lifecycle: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        :param _RuntimeRootDir: Runtime root directory
        :type RuntimeRootDir: str
        :param _EnableAutoscaling: Whether to enable Auto Scaling (AS)
        :type EnableAutoscaling: bool
        :param _Replicas: Desired node count
        :type Replicas: int
        :param _InternetAccessible: Public network bandwidth configuration
        :type InternetAccessible: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        :param _DataDisks: Data disk list of native node pools
        :type DataDisks: list of DataDisk
        :param _KeyIds: Node pool ssh public key ID array
        :type KeyIds: list of str
        :param _MachineType: Node pool type
        :type MachineType: str
        """
        self._Scaling = None
        self._SubnetIds = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._InstanceTypes = None
        self._SecurityGroupIds = None
        self._UpgradeSettings = None
        self._AutoRepair = None
        self._InstanceChargePrepaid = None
        self._Management = None
        self._HealthCheckPolicyName = None
        self._HostNamePattern = None
        self._KubeletArgs = None
        self._Lifecycle = None
        self._RuntimeRootDir = None
        self._EnableAutoscaling = None
        self._Replicas = None
        self._InternetAccessible = None
        self._DataDisks = None
        self._KeyIds = None
        self._MachineType = None

    @property
    def Scaling(self):
        """Node pool scaling configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        """
        return self._Scaling

    @Scaling.setter
    def Scaling(self, Scaling):
        self._Scaling = Scaling

    @property
    def SubnetIds(self):
        """Subnet list
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def InstanceChargeType(self):
        """Node billing type. PREPAID: Monthly subscription; POSTPAID_BY_HOUR: Pay-as-you-go (default);
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        """System disk configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.Disk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceTypes(self):
        """List of models
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def SecurityGroupIds(self):
        """Security group list
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UpgradeSettings(self):
        """Automatic upgrade configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        """
        return self._UpgradeSettings

    @UpgradeSettings.setter
    def UpgradeSettings(self, UpgradeSettings):
        self._UpgradeSettings = UpgradeSettings

    @property
    def AutoRepair(self):
        """Whether to enable self-healing capability
        :rtype: bool
        """
        return self._AutoRepair

    @AutoRepair.setter
    def AutoRepair(self, AutoRepair):
        self._AutoRepair = AutoRepair

    @property
    def InstanceChargePrepaid(self):
        """Billing configuration of monthly subscription models
        :rtype: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def Management(self):
        """Management parameter configuration of node pools
        :rtype: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        """
        return self._Management

    @Management.setter
    def Management(self, Management):
        self._Management = Management

    @property
    def HealthCheckPolicyName(self):
        """Fault self-healing rule name
        :rtype: str
        """
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

    @property
    def HostNamePattern(self):
        """hostname pattern string of native node pools
        :rtype: str
        """
        return self._HostNamePattern

    @HostNamePattern.setter
    def HostNamePattern(self, HostNamePattern):
        self._HostNamePattern = HostNamePattern

    @property
    def KubeletArgs(self):
        """kubelet custom parameters
        :rtype: list of str
        """
        return self._KubeletArgs

    @KubeletArgs.setter
    def KubeletArgs(self, KubeletArgs):
        self._KubeletArgs = KubeletArgs

    @property
    def Lifecycle(self):
        """Predefined script
        :rtype: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        """
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def RuntimeRootDir(self):
        """Runtime root directory
        :rtype: str
        """
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir

    @property
    def EnableAutoscaling(self):
        """Whether to enable Auto Scaling (AS)
        :rtype: bool
        """
        return self._EnableAutoscaling

    @EnableAutoscaling.setter
    def EnableAutoscaling(self, EnableAutoscaling):
        self._EnableAutoscaling = EnableAutoscaling

    @property
    def Replicas(self):
        """Desired node count
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def InternetAccessible(self):
        """Public network bandwidth configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def DataDisks(self):
        """Data disk list of native node pools
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def KeyIds(self):
        """Node pool ssh public key ID array
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def MachineType(self):
        """Node pool type
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        if params.get("Scaling") is not None:
            self._Scaling = MachineSetScaling()
            self._Scaling._deserialize(params.get("Scaling"))
        self._SubnetIds = params.get("SubnetIds")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = Disk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceTypes = params.get("InstanceTypes")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("UpgradeSettings") is not None:
            self._UpgradeSettings = MachineUpgradeSettings()
            self._UpgradeSettings._deserialize(params.get("UpgradeSettings"))
        self._AutoRepair = params.get("AutoRepair")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("Management") is not None:
            self._Management = ManagementConfig()
            self._Management._deserialize(params.get("Management"))
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._HostNamePattern = params.get("HostNamePattern")
        self._KubeletArgs = params.get("KubeletArgs")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifecycleConfig()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        self._EnableAutoscaling = params.get("EnableAutoscaling")
        self._Replicas = params.get("Replicas")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._KeyIds = params.get("KeyIds")
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNodePoolRequest(AbstractModel):
    """CreateNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Name: Node pool name
        :type Name: str
        :param _Type: Node pool type
        :type Type: str
        :param _Labels: Node Labels
        :type Labels: list of Label
        :param _Taints: Node taint
        :type Taints: list of Taint
        :param _Tags: Node tags
        :type Tags: list of TagSpecification
        :param _DeletionProtection: Whether to enable deletion protection
        :type DeletionProtection: bool
        :param _Unschedulable: Whether the node is unschedulable by default
        :type Unschedulable: bool
        :param _Native: Native node pool creation parameters
        :type Native: :class:`tencentcloud.tke.v20220501.models.CreateNativeNodePoolParam`
        :param _Annotations: Node Annotation List
        :type Annotations: list of Annotation
        """
        self._ClusterId = None
        self._Name = None
        self._Type = None
        self._Labels = None
        self._Taints = None
        self._Tags = None
        self._DeletionProtection = None
        self._Unschedulable = None
        self._Native = None
        self._Annotations = None

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
    def Name(self):
        """Node pool name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Node pool type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Labels(self):
        """Node Labels
        :rtype: list of Label
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        """Node taint
        :rtype: list of Taint
        """
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def Tags(self):
        """Node tags
        :rtype: list of TagSpecification
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeletionProtection(self):
        """Whether to enable deletion protection
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Unschedulable(self):
        """Whether the node is unschedulable by default
        :rtype: bool
        """
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def Native(self):
        """Native node pool creation parameters
        :rtype: :class:`tencentcloud.tke.v20220501.models.CreateNativeNodePoolParam`
        """
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Annotations(self):
        """Node Annotation List
        :rtype: list of Annotation
        """
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._Unschedulable = params.get("Unschedulable")
        if params.get("Native") is not None:
            self._Native = CreateNativeNodePoolParam()
            self._Native._deserialize(params.get("Native"))
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Annotation()
                obj._deserialize(item)
                self._Annotations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNodePoolResponse(AbstractModel):
    """CreateNodePool response structure.

    """

    def __init__(self):
        r"""
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodePoolId = None
        self._RequestId = None

    @property
    def NodePoolId(self):
        """Node pool ID
        :rtype: str
        """
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

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
        self._NodePoolId = params.get("NodePoolId")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Describes the configuration and related information of k8s node data disk.

    """

    def __init__(self):
        r"""
        :param _DiskType: Cloud disk type
Note: This field may return "null", indicating that no valid value can be obtained.
        :type DiskType: str
        :param _FileSystem: File system (ext3/ext4/xfs).

Note: This field may return "null", indicating that no valid value can be obtained.
        :type FileSystem: str
        :param _DiskSize: Cloud disk size (GB)

Note: This field may return "null", indicating that no valid value can be obtained.
        :type DiskSize: int
        :param _AutoFormatAndMount: Whether to automatically format and mount disks.

Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoFormatAndMount: bool
        :param _DiskPartition: Mount device name or partition name
Note: This field may return "null", indicating that no valid value can be obtained.
        :type DiskPartition: str
        :param _MountTarget: Mounting directory

Note: This field may return "null", indicating that no valid value can be obtained.
        :type MountTarget: str
        :param _Encrypt: This parameter is used to create an encrypted cloud disk, with the value fixed as ENCRYPT.
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Encrypt: str
        :param _KmsKeyId: Custom key for purchasing encrypted disks. When this parameter is input, the Encrypt input parameter cannot be left empty.
Note: This field may return "null", indicating that no valid value can be obtained.
        :type KmsKeyId: str
        :param _SnapshotId: Snapshot ID. If it is input, a cloud disk will be created based on this snapshot. The snapshot must be a data disk snapshot.
Note: This field may return "null", indicating that no valid value can be obtained.
        :type SnapshotId: str
        :param _ThroughputPerformance: Cloud disk performance (unit: MB/s), which can be used to purchase additional performance for cloud disks.
Note: This field may return "null", indicating that no valid value can be obtained.
        :type ThroughputPerformance: int
        """
        self._DiskType = None
        self._FileSystem = None
        self._DiskSize = None
        self._AutoFormatAndMount = None
        self._DiskPartition = None
        self._MountTarget = None
        self._Encrypt = None
        self._KmsKeyId = None
        self._SnapshotId = None
        self._ThroughputPerformance = None

    @property
    def DiskType(self):
        """Cloud disk type
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def FileSystem(self):
        """File system (ext3/ext4/xfs).

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def DiskSize(self):
        """Cloud disk size (GB)

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def AutoFormatAndMount(self):
        """Whether to automatically format and mount disks.

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._AutoFormatAndMount

    @AutoFormatAndMount.setter
    def AutoFormatAndMount(self, AutoFormatAndMount):
        self._AutoFormatAndMount = AutoFormatAndMount

    @property
    def DiskPartition(self):
        """Mount device name or partition name
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._DiskPartition

    @DiskPartition.setter
    def DiskPartition(self, DiskPartition):
        self._DiskPartition = DiskPartition

    @property
    def MountTarget(self):
        """Mounting directory

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._MountTarget

    @MountTarget.setter
    def MountTarget(self, MountTarget):
        self._MountTarget = MountTarget

    @property
    def Encrypt(self):
        """This parameter is used to create an encrypted cloud disk, with the value fixed as ENCRYPT.
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def KmsKeyId(self):
        """Custom key for purchasing encrypted disks. When this parameter is input, the Encrypt input parameter cannot be left empty.
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def SnapshotId(self):
        """Snapshot ID. If it is input, a cloud disk will be created based on this snapshot. The snapshot must be a data disk snapshot.
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def ThroughputPerformance(self):
        """Cloud disk performance (unit: MB/s), which can be used to purchase additional performance for cloud disks.
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._FileSystem = params.get("FileSystem")
        self._DiskSize = params.get("DiskSize")
        self._AutoFormatAndMount = params.get("AutoFormatAndMount")
        self._DiskPartition = params.get("DiskPartition")
        self._MountTarget = params.get("MountTarget")
        self._Encrypt = params.get("Encrypt")
        self._KmsKeyId = params.get("KmsKeyId")
        self._SnapshotId = params.get("SnapshotId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckPolicyRequest(AbstractModel):
    """DeleteHealthCheckPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _HealthCheckPolicyName: Health check policy name
        :type HealthCheckPolicyName: str
        """
        self._ClusterId = None
        self._HealthCheckPolicyName = None

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
    def HealthCheckPolicyName(self):
        """Health check policy name
        :rtype: str
        """
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckPolicyResponse(AbstractModel):
    """DeleteHealthCheckPolicy response structure.

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


class DeleteNodePoolRequest(AbstractModel):
    """DeleteNodePool request structure.

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
        """Cluster ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        """Node pool ID
        :rtype: str
        """
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
        


class DeleteNodePoolResponse(AbstractModel):
    """DeleteNodePool response structure.

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


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Offset: Offset. Default value: 0. For more information on Offset, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 20, maximum value: 100. For more information on Limit, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Filters: Filter criteria list:
InstanceIds (Instance ID), InstanceType (Instance type: Regular, Native, Virtual, External), VagueIpAddress (Fuzzy matching IP), Labels (k8s node label), NodePoolNames (Node pool name), VagueInstanceName (Fuzzy matching node name), InstanceStates (Node status), Unschedulable (Cordoning status), NodePoolIds (Node pool ID)
        :type Filters: list of Filter
        :param _SortBy: Sorting information
        :type SortBy: :class:`tencentcloud.tke.v20220501.models.SortBy`
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortBy = None

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
        """Offset. Default value: 0. For more information on Offset, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of returned results. Default value: 20, maximum value: 100. For more information on Limit, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Filter criteria list:
InstanceIds (Instance ID), InstanceType (Instance type: Regular, Native, Virtual, External), VagueIpAddress (Fuzzy matching IP), Labels (k8s node label), NodePoolNames (Node pool name), VagueInstanceName (Fuzzy matching node name), InstanceStates (Node status), Unschedulable (Cordoning status), NodePoolIds (Node pool ID)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        """Sorting information
        :rtype: :class:`tencentcloud.tke.v20220501.models.SortBy`
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
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
        :param _Errors: Error information collection
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Errors: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._Errors = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of instances in the cluster
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        """List of instances in the cluster
        :rtype: list of Instance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def Errors(self):
        """Error information collection
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

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
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._Errors = params.get("Errors")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckPoliciesRequest(AbstractModel):
    """DescribeHealthCheckPolicies request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Filters: ·  HealthCheckPolicyName
    Filter by [Health Check Policy Name].
    Type: String
        Required: No
        :type Filters: list of Filter
        :param _Limit: Maximum number of output entries. Default value: 20; maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        """
        self._ClusterId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

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
    def Filters(self):
        """·  HealthCheckPolicyName
    Filter by [Health Check Policy Name].
    Type: String
        Required: No
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Maximum number of output entries. Default value: 20; maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthCheckPoliciesResponse(AbstractModel):
    """DescribeHealthCheckPolicies response structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckPolicies: Health check policy array
Note: This field may return "null", indicating that no valid value can be obtained.
        :type HealthCheckPolicies: list of HealthCheckPolicy
        :param _TotalCount: Total number of arrays
Note: This field may return "null", indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthCheckPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HealthCheckPolicies(self):
        """Health check policy array
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of HealthCheckPolicy
        """
        return self._HealthCheckPolicies

    @HealthCheckPolicies.setter
    def HealthCheckPolicies(self, HealthCheckPolicies):
        self._HealthCheckPolicies = HealthCheckPolicies

    @property
    def TotalCount(self):
        """Total number of arrays
Note: This field may return "null", indicating that no valid value can be obtained.
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
        if params.get("HealthCheckPolicies") is not None:
            self._HealthCheckPolicies = []
            for item in params.get("HealthCheckPolicies"):
                obj = HealthCheckPolicy()
                obj._deserialize(item)
                self._HealthCheckPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckPolicyBindingsRequest(AbstractModel):
    """DescribeHealthCheckPolicyBindings request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Filter: ·  HealthCheckPolicyName
    Filter by [Health Check Rule Name].
    Type: String
        Required: No
        :type Filter: list of Filter
        :param _Limit: Maximum number of output entries. Default value: 20; maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        """
        self._ClusterId = None
        self._Filter = None
        self._Limit = None
        self._Offset = None

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
    def Filter(self):
        """·  HealthCheckPolicyName
    Filter by [Health Check Rule Name].
    Type: String
        Required: No
        :rtype: list of Filter
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Limit(self):
        """Maximum number of output entries. Default value: 20; maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthCheckPolicyBindingsResponse(AbstractModel):
    """DescribeHealthCheckPolicyBindings response structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckPolicyBindings: Health check rule array
Note: This field may return "null", indicating that no valid value can be obtained.
        :type HealthCheckPolicyBindings: list of HealthCheckPolicyBinding
        :param _TotalCount: Number of health check rules
Note: This field may return "null", indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthCheckPolicyBindings = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HealthCheckPolicyBindings(self):
        """Health check rule array
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of HealthCheckPolicyBinding
        """
        return self._HealthCheckPolicyBindings

    @HealthCheckPolicyBindings.setter
    def HealthCheckPolicyBindings(self, HealthCheckPolicyBindings):
        self._HealthCheckPolicyBindings = HealthCheckPolicyBindings

    @property
    def TotalCount(self):
        """Number of health check rules
Note: This field may return "null", indicating that no valid value can be obtained.
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
        if params.get("HealthCheckPolicyBindings") is not None:
            self._HealthCheckPolicyBindings = []
            for item in params.get("HealthCheckPolicyBindings"):
                obj = HealthCheckPolicyBinding()
                obj._deserialize(item)
                self._HealthCheckPolicyBindings.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckTemplateRequest(AbstractModel):
    """DescribeHealthCheckTemplate request structure.

    """


class DescribeHealthCheckTemplateResponse(AbstractModel):
    """DescribeHealthCheckTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplate: Health check policy template
        :type HealthCheckTemplate: :class:`tencentcloud.tke.v20220501.models.HealthCheckTemplate`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._HealthCheckTemplate = None
        self._RequestId = None

    @property
    def HealthCheckTemplate(self):
        """Health check policy template
        :rtype: :class:`tencentcloud.tke.v20220501.models.HealthCheckTemplate`
        """
        return self._HealthCheckTemplate

    @HealthCheckTemplate.setter
    def HealthCheckTemplate(self, HealthCheckTemplate):
        self._HealthCheckTemplate = HealthCheckTemplate

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
        if params.get("HealthCheckTemplate") is not None:
            self._HealthCheckTemplate = HealthCheckTemplate()
            self._HealthCheckTemplate._deserialize(params.get("HealthCheckTemplate"))
        self._RequestId = params.get("RequestId")


class DescribeNodePoolsRequest(AbstractModel):
    """DescribeNodePools request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Filters: Query filter criteria:
·  NodePoolsName
    Filter by [Node Pool Name].
    Type: String
        Required: No



·  NodePoolsId
    Filter by [Node Pool id].
    Type: String
        Required: No



·  tags
    Filter by [Tag Key-value Pairs].
    Type: String
        Required: No



·  tag:tag-key
    Filter by [Tag Key-value Pairs].
    Type: String
        Required: No
        :type Filters: list of Filter
        :param _Offset: Offset. Default value: 0
        :type Offset: int
        :param _Limit: Maximum number of output entries. Default value: 20; maximum value: 100.
        :type Limit: int
        """
        self._ClusterId = None
        self._Filters = None
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
    def Filters(self):
        """Query filter criteria:
·  NodePoolsName
    Filter by [Node Pool Name].
    Type: String
        Required: No



·  NodePoolsId
    Filter by [Node Pool id].
    Type: String
        Required: No



·  tags
    Filter by [Tag Key-value Pairs].
    Type: String
        Required: No



·  tag:tag-key
    Filter by [Tag Key-value Pairs].
    Type: String
        Required: No
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """Offset. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of output entries. Default value: 20; maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
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
        


class DescribeNodePoolsResponse(AbstractModel):
    """DescribeNodePools response structure.

    """

    def __init__(self):
        r"""
        :param _NodePools: Node pool list
Note: This field may return "null", indicating that no valid value can be obtained.
        :type NodePools: list of NodePool
        :param _TotalCount: Total resources
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._NodePools = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodePools(self):
        """Node pool list
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of NodePool
        """
        return self._NodePools

    @NodePools.setter
    def NodePools(self, NodePools):
        self._NodePools = NodePools

    @property
    def TotalCount(self):
        """Total resources
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
        if params.get("NodePools") is not None:
            self._NodePools = []
            for item in params.get("NodePools"):
                obj = NodePool()
                obj._deserialize(item)
                self._NodePools.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Disk(AbstractModel):
    """Node system disk and data disk configuration

    """

    def __init__(self):
        r"""
        :param _DiskType: Cloud disk type
        :type DiskType: str
        :param _DiskSize: Cloud disk size (GB)
        :type DiskSize: int
        :param _AutoFormatAndMount: Whether to automatically format and mount disks.
        :type AutoFormatAndMount: bool
        :param _FileSystem: File system
        :type FileSystem: str
        :param _MountTarget: Mounting directory
        :type MountTarget: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._AutoFormatAndMount = None
        self._FileSystem = None
        self._MountTarget = None

    @property
    def DiskType(self):
        """Cloud disk type
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        """Cloud disk size (GB)
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def AutoFormatAndMount(self):
        """Whether to automatically format and mount disks.
        :rtype: bool
        """
        return self._AutoFormatAndMount

    @AutoFormatAndMount.setter
    def AutoFormatAndMount(self, AutoFormatAndMount):
        self._AutoFormatAndMount = AutoFormatAndMount

    @property
    def FileSystem(self):
        """File system
        :rtype: str
        """
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def MountTarget(self):
        """Mounting directory
        :rtype: str
        """
        return self._MountTarget

    @MountTarget.setter
    def MountTarget(self, MountTarget):
        self._MountTarget = MountTarget


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._AutoFormatAndMount = params.get("AutoFormatAndMount")
        self._FileSystem = params.get("FileSystem")
        self._MountTarget = params.get("MountTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalNodeInfo(AbstractModel):
    """Third-party node

    """

    def __init__(self):
        r"""
        :param _Name: Third-party node name
        :type Name: str
        :param _CPU: Number of CPU cores (unit: cores)
Note: This field may return "null", indicating that no valid value can be obtained.
        :type CPU: int
        :param _Memory: Node memory capacity (unit: `GB`)
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Memory: int
        :param _K8SVersion: kubelet version information of third-party nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type K8SVersion: str
        """
        self._Name = None
        self._CPU = None
        self._Memory = None
        self._K8SVersion = None

    @property
    def Name(self):
        """Third-party node name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CPU(self):
        """Number of CPU cores (unit: cores)
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        """Node memory capacity (unit: `GB`)
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def K8SVersion(self):
        """kubelet version information of third-party nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._K8SVersion

    @K8SVersion.setter
    def K8SVersion(self, K8SVersion):
        self._K8SVersion = K8SVersion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._K8SVersion = params.get("K8SVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalNodePoolInfo(AbstractModel):
    """Third-party node pool information

    """

    def __init__(self):
        r"""
        :param _RuntimeConfig: Third-party node runtime configuration
        :type RuntimeConfig: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        :param _NodesNum: Number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type NodesNum: int
        """
        self._RuntimeConfig = None
        self._NodesNum = None

    @property
    def RuntimeConfig(self):
        """Third-party node runtime configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        """
        return self._RuntimeConfig

    @RuntimeConfig.setter
    def RuntimeConfig(self, RuntimeConfig):
        self._RuntimeConfig = RuntimeConfig

    @property
    def NodesNum(self):
        """Number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._NodesNum

    @NodesNum.setter
    def NodesNum(self, NodesNum):
        self._NodesNum = NodesNum


    def _deserialize(self, params):
        if params.get("RuntimeConfig") is not None:
            self._RuntimeConfig = RuntimeConfig()
            self._RuntimeConfig._deserialize(params.get("RuntimeConfig"))
        self._NodesNum = params.get("NodesNum")
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
        :param _Name: Attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.
        :type Name: str
        :param _Values: Attribute value. If multiple values exist in one filter, the logical relationship between these values is `OR`.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Attribute name. If more than one Filter exists, the logical relation between these Filters is `AND`.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Attribute value. If multiple values exist in one filter, the logical relationship between these values is `OR`.
        :rtype: list of str
        """
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
        


class HealthCheckPolicy(AbstractModel):
    """Health check rules

    """

    def __init__(self):
        r"""
        :param _Name: Health check policy name
        :type Name: str
        :param _Rules: List of health check policy rules
        :type Rules: list of HealthCheckPolicyRule
        """
        self._Name = None
        self._Rules = None

    @property
    def Name(self):
        """Health check policy name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rules(self):
        """List of health check policy rules
        :rtype: list of HealthCheckPolicyRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = HealthCheckPolicyRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckPolicyBinding(AbstractModel):
    """Binding relationship between health check policy and node pool

    """

    def __init__(self):
        r"""
        :param _Name: Health check policy name
        :type Name: str
        :param _CreatedAt: Rule creation time
        :type CreatedAt: str
        :param _NodePools: Associated node pool array
        :type NodePools: list of str
        """
        self._Name = None
        self._CreatedAt = None
        self._NodePools = None

    @property
    def Name(self):
        """Health check policy name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreatedAt(self):
        """Rule creation time
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def NodePools(self):
        """Associated node pool array
        :rtype: list of str
        """
        return self._NodePools

    @NodePools.setter
    def NodePools(self, NodePools):
        self._NodePools = NodePools


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreatedAt = params.get("CreatedAt")
        self._NodePools = params.get("NodePools")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckPolicyRule(AbstractModel):
    """Health check rules

    """

    def __init__(self):
        r"""
        :param _Name: Health check rules
        :type Name: str
        :param _Enabled: Whether to check this item
        :type Enabled: bool
        :param _AutoRepairEnabled: Whether to enable repair
        :type AutoRepairEnabled: bool
        """
        self._Name = None
        self._Enabled = None
        self._AutoRepairEnabled = None

    @property
    def Name(self):
        """Health check rules
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enabled(self):
        """Whether to check this item
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def AutoRepairEnabled(self):
        """Whether to enable repair
        :rtype: bool
        """
        return self._AutoRepairEnabled

    @AutoRepairEnabled.setter
    def AutoRepairEnabled(self, AutoRepairEnabled):
        self._AutoRepairEnabled = AutoRepairEnabled


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Enabled = params.get("Enabled")
        self._AutoRepairEnabled = params.get("AutoRepairEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckTemplate(AbstractModel):
    """Health check template

    """

    def __init__(self):
        r"""
        :param _Rules: Health check item
        :type Rules: list of HealthCheckTemplateRule
        """
        self._Rules = None

    @property
    def Rules(self):
        """Health check item
        :rtype: list of HealthCheckTemplateRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = HealthCheckTemplateRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckTemplateRule(AbstractModel):
    """Health check template rules

    """

    def __init__(self):
        r"""
        :param _Name: Health check item name
        :type Name: str
        :param _Description: Description of health check rules
        :type Description: str
        :param _RepairAction: Fix action
        :type RepairAction: str
        :param _RepairEffect: Fix impact
        :type RepairEffect: str
        :param _ShouldEnable: Whether it is recommended to enable check
        :type ShouldEnable: bool
        :param _ShouldRepair: Whether repair is suggested.
        :type ShouldRepair: bool
        :param _Severity: Severity
        :type Severity: str
        """
        self._Name = None
        self._Description = None
        self._RepairAction = None
        self._RepairEffect = None
        self._ShouldEnable = None
        self._ShouldRepair = None
        self._Severity = None

    @property
    def Name(self):
        """Health check item name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Description of health check rules
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RepairAction(self):
        """Fix action
        :rtype: str
        """
        return self._RepairAction

    @RepairAction.setter
    def RepairAction(self, RepairAction):
        self._RepairAction = RepairAction

    @property
    def RepairEffect(self):
        """Fix impact
        :rtype: str
        """
        return self._RepairEffect

    @RepairEffect.setter
    def RepairEffect(self, RepairEffect):
        self._RepairEffect = RepairEffect

    @property
    def ShouldEnable(self):
        """Whether it is recommended to enable check
        :rtype: bool
        """
        return self._ShouldEnable

    @ShouldEnable.setter
    def ShouldEnable(self, ShouldEnable):
        self._ShouldEnable = ShouldEnable

    @property
    def ShouldRepair(self):
        """Whether repair is suggested.
        :rtype: bool
        """
        return self._ShouldRepair

    @ShouldRepair.setter
    def ShouldRepair(self, ShouldRepair):
        self._ShouldRepair = ShouldRepair

    @property
    def Severity(self):
        """Severity
        :rtype: str
        """
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._RepairAction = params.get("RepairAction")
        self._RepairEffect = params.get("RepairEffect")
        self._ShouldEnable = params.get("ShouldEnable")
        self._ShouldRepair = params.get("ShouldRepair")
        self._Severity = params.get("Severity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """Cluster's instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceRole: Node role: MASTER, WORKER, ETCD, MASTER_ETCD, and ALL. Default value: WORKER
        :type InstanceRole: str
        :param _FailedReason: Cause of instance exception (or initialization)
Note: This field may return "null", indicating that no valid value can be obtained.
        :type FailedReason: str
        :param _InstanceState: Instance status

- initializing
- running
- failed
        :type InstanceState: str
        :param _Unschedulable: Whether it is unschedulable
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Unschedulable: bool
        :param _CreatedTime: Adding time
        :type CreatedTime: str
        :param _LanIP: Node private network IP
Note: This field may return "null", indicating that no valid value can be obtained.
        :type LanIP: str
        :param _NodePoolId: Resource pool ID

Note: This field may return "null", indicating that no valid value can be obtained.
        :type NodePoolId: str
        :param _Native: Native node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Native: :class:`tencentcloud.tke.v20220501.models.NativeNodeInfo`
        :param _Regular: General node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Regular: :class:`tencentcloud.tke.v20220501.models.RegularNodeInfo`
        :param _Super: Super node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Super: :class:`tencentcloud.tke.v20220501.models.SuperNodeInfo`
        :param _External: Third-party node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :type External: :class:`tencentcloud.tke.v20220501.models.ExternalNodeInfo`
        :param _NodeType: Node type

Note: This field may return "null", indicating that no valid value can be obtained.
        :type NodeType: str
        """
        self._InstanceId = None
        self._InstanceRole = None
        self._FailedReason = None
        self._InstanceState = None
        self._Unschedulable = None
        self._CreatedTime = None
        self._LanIP = None
        self._NodePoolId = None
        self._Native = None
        self._Regular = None
        self._Super = None
        self._External = None
        self._NodeType = None

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
    def InstanceRole(self):
        """Node role: MASTER, WORKER, ETCD, MASTER_ETCD, and ALL. Default value: WORKER
        :rtype: str
        """
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def FailedReason(self):
        """Cause of instance exception (or initialization)
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def InstanceState(self):
        """Instance status

- initializing
- running
- failed
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Unschedulable(self):
        """Whether it is unschedulable
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def CreatedTime(self):
        """Adding time
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def LanIP(self):
        """Node private network IP
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def NodePoolId(self):
        """Resource pool ID

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Native(self):
        """Native node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.NativeNodeInfo`
        """
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Regular(self):
        """General node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.RegularNodeInfo`
        """
        return self._Regular

    @Regular.setter
    def Regular(self, Regular):
        self._Regular = Regular

    @property
    def Super(self):
        """Super node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.SuperNodeInfo`
        """
        return self._Super

    @Super.setter
    def Super(self, Super):
        self._Super = Super

    @property
    def External(self):
        """Third-party node parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.ExternalNodeInfo`
        """
        return self._External

    @External.setter
    def External(self, External):
        self._External = External

    @property
    def NodeType(self):
        """Node type

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceRole = params.get("InstanceRole")
        self._FailedReason = params.get("FailedReason")
        self._InstanceState = params.get("InstanceState")
        self._Unschedulable = params.get("Unschedulable")
        self._CreatedTime = params.get("CreatedTime")
        self._LanIP = params.get("LanIP")
        self._NodePoolId = params.get("NodePoolId")
        if params.get("Native") is not None:
            self._Native = NativeNodeInfo()
            self._Native._deserialize(params.get("Native"))
        if params.get("Regular") is not None:
            self._Regular = RegularNodeInfo()
            self._Regular._deserialize(params.get("Regular"))
        if params.get("Super") is not None:
            self._Super = SuperNodeInfo()
            self._Super._deserialize(params.get("Super"))
        if params.get("External") is not None:
            self._External = ExternalNodeInfo()
            self._External._deserialize(params.get("External"))
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """Describes the configuration and related information of K8s cluster.

    """

    def __init__(self):
        r"""
        :param _DesiredPodNumber: When the node is in the podCIDR size customization mode, you can specify the upper limit of the number of pods running on the node.
Note: This field may return "null", indicating that no valid value can be obtained.
        :type DesiredPodNumber: int
        :param _PreStartUserScript: base64 encoded user script, executed before initializing the node and currently effective only for adding existing nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type PreStartUserScript: str
        :param _RuntimeConfig: Runtime description
Note: This field may return "null", indicating that no valid value can be obtained.
        :type RuntimeConfig: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        :param _UserScript: Base64-encoded user script. This script is executed after the k8s components start running. Users must ensure the reenterable and retry logic of the script. The script and the log files generated by it can be viewed at the /data/ccs_userscript/ path of the node. If a node must be initialized before joining the scheduling, it can be used in conjunction with the unschedulable parameter. After initializing with userScript, add the command `kubectl uncordon nodename --kubeconfig=/root/.kube/config` to add the node to scheduling.

Note: This field may return "null", indicating that no valid value can be obtained.
        :type UserScript: str
        :param _ExtraArgs: Node-related custom parameter information.

Note: This field may return "null", indicating that no valid value can be obtained.
        :type ExtraArgs: :class:`tencentcloud.tke.v20220501.models.InstanceExtraArgs`
        """
        self._DesiredPodNumber = None
        self._PreStartUserScript = None
        self._RuntimeConfig = None
        self._UserScript = None
        self._ExtraArgs = None

    @property
    def DesiredPodNumber(self):
        """When the node is in the podCIDR size customization mode, you can specify the upper limit of the number of pods running on the node.
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._DesiredPodNumber

    @DesiredPodNumber.setter
    def DesiredPodNumber(self, DesiredPodNumber):
        self._DesiredPodNumber = DesiredPodNumber

    @property
    def PreStartUserScript(self):
        """base64 encoded user script, executed before initializing the node and currently effective only for adding existing nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._PreStartUserScript

    @PreStartUserScript.setter
    def PreStartUserScript(self, PreStartUserScript):
        self._PreStartUserScript = PreStartUserScript

    @property
    def RuntimeConfig(self):
        """Runtime description
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        """
        return self._RuntimeConfig

    @RuntimeConfig.setter
    def RuntimeConfig(self, RuntimeConfig):
        self._RuntimeConfig = RuntimeConfig

    @property
    def UserScript(self):
        """Base64-encoded user script. This script is executed after the k8s components start running. Users must ensure the reenterable and retry logic of the script. The script and the log files generated by it can be viewed at the /data/ccs_userscript/ path of the node. If a node must be initialized before joining the scheduling, it can be used in conjunction with the unschedulable parameter. After initializing with userScript, add the command `kubectl uncordon nodename --kubeconfig=/root/.kube/config` to add the node to scheduling.

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._UserScript

    @UserScript.setter
    def UserScript(self, UserScript):
        self._UserScript = UserScript

    @property
    def ExtraArgs(self):
        """Node-related custom parameter information.

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.InstanceExtraArgs`
        """
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs


    def _deserialize(self, params):
        self._DesiredPodNumber = params.get("DesiredPodNumber")
        self._PreStartUserScript = params.get("PreStartUserScript")
        if params.get("RuntimeConfig") is not None:
            self._RuntimeConfig = RuntimeConfig()
            self._RuntimeConfig._deserialize(params.get("RuntimeConfig"))
        self._UserScript = params.get("UserScript")
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
        


class InstanceChargePrepaid(AbstractModel):
    """Monthly subscription configuration

    """

    def __init__(self):
        r"""
        :param _Period: Billing cycle of the pay-as-you-go mode (unit: month):
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60
        :type Period: int
        :param _RenewFlag: Renewal method of the prepayment mode:
- NOTIFY_AND_AUTO_RENEW: Notify the user of expiration and auto-renew (default)
- NOTIFY_AND_MANUAL_RENEW: Notify the user of expiration but do not auto-renew
- DISABLE_NOTIFY_AND_MANUAL_RENEW: Do not notify the user of expiration and do not auto-renew

        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        """Billing cycle of the pay-as-you-go mode (unit: month):
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        """Renewal method of the prepayment mode:
- NOTIFY_AND_AUTO_RENEW: Notify the user of expiration and auto-renew (default)
- NOTIFY_AND_MANUAL_RENEW: Notify the user of expiration but do not auto-renew
- DISABLE_NOTIFY_AND_MANUAL_RENEW: Do not notify the user of expiration and do not auto-renew

        :rtype: str
        """
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
        


class InstanceExtraArgs(AbstractModel):
    """Node custom parameters

    """

    def __init__(self):
        r"""
        :param _Kubelet: kubelet custom parameters, whose format is ["k1=v1", "k1=v2"], for example ["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Kubelet: list of str
        """
        self._Kubelet = None

    @property
    def Kubelet(self):
        """kubelet custom parameters, whose format is ["k1=v1", "k1=v2"], for example ["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
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
        


class IntOrString(AbstractModel):
    """Numerical structure

    """

    def __init__(self):
        r"""
        :param _Type: Numerical type, 0: int, 1: string
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Type: int
        :param _IntVal: Integer
Note: This field may return "null", indicating that no valid value can be obtained.
        :type IntVal: int
        :param _StrVal: String
Note: This field may return "null", indicating that no valid value can be obtained.
        :type StrVal: str
        """
        self._Type = None
        self._IntVal = None
        self._StrVal = None

    @property
    def Type(self):
        """Numerical type, 0: int, 1: string
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IntVal(self):
        """Integer
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._IntVal

    @IntVal.setter
    def IntVal(self, IntVal):
        self._IntVal = IntVal

    @property
    def StrVal(self):
        """String
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._StrVal

    @StrVal.setter
    def StrVal(self, StrVal):
        self._StrVal = StrVal


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._IntVal = params.get("IntVal")
        self._StrVal = params.get("StrVal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """Public network bandwidth

    """

    def __init__(self):
        r"""
        :param _MaxBandwidthOut: Bandwidth
        :type MaxBandwidthOut: int
        :param _ChargeType: Network billing method
        :type ChargeType: str
        :param _BandwidthPackageId: Bandwidth package ID
        :type BandwidthPackageId: str
        """
        self._MaxBandwidthOut = None
        self._ChargeType = None
        self._BandwidthPackageId = None

    @property
    def MaxBandwidthOut(self):
        """Bandwidth
        :rtype: int
        """
        return self._MaxBandwidthOut

    @MaxBandwidthOut.setter
    def MaxBandwidthOut(self, MaxBandwidthOut):
        self._MaxBandwidthOut = MaxBandwidthOut

    @property
    def ChargeType(self):
        """Network billing method
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def BandwidthPackageId(self):
        """Bandwidth package ID
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._MaxBandwidthOut = params.get("MaxBandwidthOut")
        self._ChargeType = params.get("ChargeType")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """Tags in k8s, generally existing as an array

    """

    def __init__(self):
        r"""
        :param _Name: Name in the map list
        :type Name: str
        :param _Value: Value in the map list
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Name in the map list
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Value in the map list
        :rtype: str
        """
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
        


class LifecycleConfig(AbstractModel):
    """Custom script for node pools

    """

    def __init__(self):
        r"""
        :param _PreInit: Custom script before node initialization
Note: This field may return "null", indicating that no valid value can be obtained.
        :type PreInit: str
        :param _PostInit: Custom script after node initialization
Note: This field may return "null", indicating that no valid value can be obtained.
        :type PostInit: str
        """
        self._PreInit = None
        self._PostInit = None

    @property
    def PreInit(self):
        """Custom script before node initialization
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._PreInit

    @PreInit.setter
    def PreInit(self, PreInit):
        self._PreInit = PreInit

    @property
    def PostInit(self):
        """Custom script after node initialization
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._PostInit

    @PostInit.setter
    def PostInit(self, PostInit):
        self._PostInit = PostInit


    def _deserialize(self, params):
        self._PreInit = params.get("PreInit")
        self._PostInit = params.get("PostInit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineSetScaling(AbstractModel):
    """Node pool AS configuration

    """

    def __init__(self):
        r"""
        :param _MinReplicas: Node pool minimum replica count
Note: This field may return "null", indicating that no valid value can be obtained.
        :type MinReplicas: int
        :param _MaxReplicas: Node pool maximum replica count
Note: This field may return "null", indicating that no valid value can be obtained.
        :type MaxReplicas: int
        :param _CreatePolicy: Node pool scaling policy. ZoneEquality: Scatter across multiple availability zones; ZonePriority: Prioritize preferred availability zones;
Note: This field may return "null", indicating that no valid value can be obtained.
        :type CreatePolicy: str
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._CreatePolicy = None

    @property
    def MinReplicas(self):
        """Node pool minimum replica count
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        """Node pool maximum replica count
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def CreatePolicy(self):
        """Node pool scaling policy. ZoneEquality: Scatter across multiple availability zones; ZonePriority: Prioritize preferred availability zones;
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CreatePolicy

    @CreatePolicy.setter
    def CreatePolicy(self, CreatePolicy):
        self._CreatePolicy = CreatePolicy


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._CreatePolicy = params.get("CreatePolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineUpgradeSettings(AbstractModel):
    """Managed node pool automatic upgrade configuration

    """

    def __init__(self):
        r"""
        :param _AutoUpgrade: Whether to enable automatic upgrade
Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoUpgrade: bool
        :param _UpgradeOptions: Ops window
Note: This field may return "null", indicating that no valid value can be obtained.
        :type UpgradeOptions: :class:`tencentcloud.tke.v20220501.models.AutoUpgradeOptions`
        :param _Components: Upgrade item
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Components: list of str
        :param _MaxUnavailable: Maximum number of nodes that cannot be upgraded during upgrade
Note: This field may return "null", indicating that no valid value can be obtained.
        :type MaxUnavailable: :class:`tencentcloud.tke.v20220501.models.IntOrString`
        """
        self._AutoUpgrade = None
        self._UpgradeOptions = None
        self._Components = None
        self._MaxUnavailable = None

    @property
    def AutoUpgrade(self):
        """Whether to enable automatic upgrade
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._AutoUpgrade

    @AutoUpgrade.setter
    def AutoUpgrade(self, AutoUpgrade):
        self._AutoUpgrade = AutoUpgrade

    @property
    def UpgradeOptions(self):
        """Ops window
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.AutoUpgradeOptions`
        """
        return self._UpgradeOptions

    @UpgradeOptions.setter
    def UpgradeOptions(self, UpgradeOptions):
        self._UpgradeOptions = UpgradeOptions

    @property
    def Components(self):
        """Upgrade item
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def MaxUnavailable(self):
        """Maximum number of nodes that cannot be upgraded during upgrade
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.IntOrString`
        """
        return self._MaxUnavailable

    @MaxUnavailable.setter
    def MaxUnavailable(self, MaxUnavailable):
        self._MaxUnavailable = MaxUnavailable


    def _deserialize(self, params):
        self._AutoUpgrade = params.get("AutoUpgrade")
        if params.get("UpgradeOptions") is not None:
            self._UpgradeOptions = AutoUpgradeOptions()
            self._UpgradeOptions._deserialize(params.get("UpgradeOptions"))
        self._Components = params.get("Components")
        if params.get("MaxUnavailable") is not None:
            self._MaxUnavailable = IntOrString()
            self._MaxUnavailable._deserialize(params.get("MaxUnavailable"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagementConfig(AbstractModel):
    """Management configuration of managed node pools

    """

    def __init__(self):
        r"""
        :param _Nameservers: dns configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Nameservers: list of str
        :param _Hosts: hosts configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Hosts: list of str
        :param _KernelArgs: Kernel parameter configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type KernelArgs: list of str
        """
        self._Nameservers = None
        self._Hosts = None
        self._KernelArgs = None

    @property
    def Nameservers(self):
        """dns configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._Nameservers

    @Nameservers.setter
    def Nameservers(self, Nameservers):
        self._Nameservers = Nameservers

    @property
    def Hosts(self):
        """hosts configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def KernelArgs(self):
        """Kernel parameter configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._KernelArgs

    @KernelArgs.setter
    def KernelArgs(self, KernelArgs):
        self._KernelArgs = KernelArgs


    def _deserialize(self, params):
        self._Nameservers = params.get("Nameservers")
        self._Hosts = params.get("Hosts")
        self._KernelArgs = params.get("KernelArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManuallyAdded(AbstractModel):
    """Nodes manually added

    """

    def __init__(self):
        r"""
        :param _Joining: Number of nodes being added
        :type Joining: int
        :param _Initializing: Number of nodes being initialized
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
        """Number of nodes being added
        :rtype: int
        """
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        """Number of nodes being initialized
        :rtype: int
        """
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        """Number of normal nodes
        :rtype: int
        """
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        """Total number of nodes
        :rtype: int
        """
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
        


class ModifyHealthCheckPolicyRequest(AbstractModel):
    """ModifyHealthCheckPolicy request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _HealthCheckPolicy: Health check policy
        :type HealthCheckPolicy: :class:`tencentcloud.tke.v20220501.models.HealthCheckPolicy`
        """
        self._ClusterId = None
        self._HealthCheckPolicy = None

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
    def HealthCheckPolicy(self):
        """Health check policy
        :rtype: :class:`tencentcloud.tke.v20220501.models.HealthCheckPolicy`
        """
        return self._HealthCheckPolicy

    @HealthCheckPolicy.setter
    def HealthCheckPolicy(self, HealthCheckPolicy):
        self._HealthCheckPolicy = HealthCheckPolicy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("HealthCheckPolicy") is not None:
            self._HealthCheckPolicy = HealthCheckPolicy()
            self._HealthCheckPolicy._deserialize(params.get("HealthCheckPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHealthCheckPolicyResponse(AbstractModel):
    """ModifyHealthCheckPolicy response structure.

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


class ModifyNodePoolRequest(AbstractModel):
    """ModifyNodePool request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _Name: Node pool name
        :type Name: str
        :param _Labels: Node Labels
        :type Labels: list of Label
        :param _Taints: Node taint
        :type Taints: list of Taint
        :param _Tags: Node tags
        :type Tags: list of TagSpecification
        :param _DeletionProtection: Whether to enable deletion protection
        :type DeletionProtection: bool
        :param _Unschedulable: Whether the node is unschedulable
        :type Unschedulable: bool
        :param _Native: Native node pool update parameters
        :type Native: :class:`tencentcloud.tke.v20220501.models.UpdateNativeNodePoolParam`
        :param _Annotations: Node annotation list
        :type Annotations: list of Annotation
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._Name = None
        self._Labels = None
        self._Taints = None
        self._Tags = None
        self._DeletionProtection = None
        self._Unschedulable = None
        self._Native = None
        self._Annotations = None

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
    def NodePoolId(self):
        """Node pool ID
        :rtype: str
        """
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Name(self):
        """Node pool name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Labels(self):
        """Node Labels
        :rtype: list of Label
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        """Node taint
        :rtype: list of Taint
        """
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def Tags(self):
        """Node tags
        :rtype: list of TagSpecification
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeletionProtection(self):
        """Whether to enable deletion protection
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Unschedulable(self):
        """Whether the node is unschedulable
        :rtype: bool
        """
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def Native(self):
        """Native node pool update parameters
        :rtype: :class:`tencentcloud.tke.v20220501.models.UpdateNativeNodePoolParam`
        """
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Annotations(self):
        """Node annotation list
        :rtype: list of Annotation
        """
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations


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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._Unschedulable = params.get("Unschedulable")
        if params.get("Native") is not None:
            self._Native = UpdateNativeNodePoolParam()
            self._Native._deserialize(params.get("Native"))
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Annotation()
                obj._deserialize(item)
                self._Annotations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodePoolResponse(AbstractModel):
    """ModifyNodePool response structure.

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


class NativeNodeInfo(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param _MachineName: Node name
        :type MachineName: str
        :param _MachineState: Machine status
        :type MachineState: str
        :param _Zone: Machine availability zone
        :type Zone: str
        :param _InstanceChargeType: Node billing type. PREPAID: Monthly subscription; POSTPAID_BY_HOUR: Pay-as-you-go (default);
        :type InstanceChargeType: str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _LoginStatus: Machine login status
Note: This field may return "null", indicating that no valid value can be obtained.
        :type LoginStatus: str
        :param _IsProtectedFromScaleIn: Whether to enable scale-in protection
Note: This field may return "null", indicating that no valid value can be obtained.
        :type IsProtectedFromScaleIn: bool
        :param _DisplayName: Machine name
Note: This field may return "null", indicating that no valid value can be obtained.
        :type DisplayName: str
        :param _CPU: Number of CPU cores (unit: cores)
        :type CPU: int
        :param _GPU: Number of GPU cores (unit: cores)
Note: This field may return "null", indicating that no valid value can be obtained.
        :type GPU: int
        :param _RenewFlag: Auto-renewal label
        :type RenewFlag: str
        :param _PayMode: Node billing mode (deprecated)
        :type PayMode: str
        :param _Memory: Node memory capacity (unit: `GB`)
        :type Memory: int
        :param _InternetAccessible: Public network bandwidth configuration
        :type InternetAccessible: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        :param _InstanceFamily: Model family
        :type InstanceFamily: str
        :param _LanIp: Node private network IP
        :type LanIp: str
        :param _InstanceType: Model
        :type InstanceType: str
        :param _ExpiredTime: Billing expiration time of monthly subscription nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type ExpiredTime: str
        :param _SecurityGroupIDs: Security group list
Note: This field may return "null", indicating that no valid value can be obtained.
        :type SecurityGroupIDs: list of str
        :param _VpcId: VPC unique ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet unique ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :type SubnetId: str
        :param _OsImage: OS name
Note: This field may return "null", indicating that no valid value can be obtained.
        :type OsImage: str
        :param _InstanceId: 
        :type InstanceId: str
        """
        self._MachineName = None
        self._MachineState = None
        self._Zone = None
        self._InstanceChargeType = None
        self._CreatedAt = None
        self._LoginStatus = None
        self._IsProtectedFromScaleIn = None
        self._DisplayName = None
        self._CPU = None
        self._GPU = None
        self._RenewFlag = None
        self._PayMode = None
        self._Memory = None
        self._InternetAccessible = None
        self._InstanceFamily = None
        self._LanIp = None
        self._InstanceType = None
        self._ExpiredTime = None
        self._SecurityGroupIDs = None
        self._VpcId = None
        self._SubnetId = None
        self._OsImage = None
        self._InstanceId = None

    @property
    def MachineName(self):
        """Node name
        :rtype: str
        """
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineState(self):
        """Machine status
        :rtype: str
        """
        return self._MachineState

    @MachineState.setter
    def MachineState(self, MachineState):
        self._MachineState = MachineState

    @property
    def Zone(self):
        """Machine availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceChargeType(self):
        """Node billing type. PREPAID: Monthly subscription; POSTPAID_BY_HOUR: Pay-as-you-go (default);
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def CreatedAt(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def LoginStatus(self):
        """Machine login status
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._LoginStatus

    @LoginStatus.setter
    def LoginStatus(self, LoginStatus):
        self._LoginStatus = LoginStatus

    @property
    def IsProtectedFromScaleIn(self):
        """Whether to enable scale-in protection
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._IsProtectedFromScaleIn

    @IsProtectedFromScaleIn.setter
    def IsProtectedFromScaleIn(self, IsProtectedFromScaleIn):
        self._IsProtectedFromScaleIn = IsProtectedFromScaleIn

    @property
    def DisplayName(self):
        """Machine name
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def CPU(self):
        """Number of CPU cores (unit: cores)
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def GPU(self):
        """Number of GPU cores (unit: cores)
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._GPU

    @GPU.setter
    def GPU(self, GPU):
        self._GPU = GPU

    @property
    def RenewFlag(self):
        """Auto-renewal label
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        """Node billing mode (deprecated)
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Memory(self):
        """Node memory capacity (unit: `GB`)
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InternetAccessible(self):
        """Public network bandwidth configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceFamily(self):
        """Model family
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def LanIp(self):
        """Node private network IP
        :rtype: str
        """
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def InstanceType(self):
        """Model
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ExpiredTime(self):
        """Billing expiration time of monthly subscription nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SecurityGroupIDs(self):
        """Security group list
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SecurityGroupIDs

    @SecurityGroupIDs.setter
    def SecurityGroupIDs(self, SecurityGroupIDs):
        self._SecurityGroupIDs = SecurityGroupIDs

    @property
    def VpcId(self):
        """VPC unique ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet unique ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def OsImage(self):
        """OS name
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._OsImage

    @OsImage.setter
    def OsImage(self, OsImage):
        self._OsImage = OsImage

    @property
    def InstanceId(self):
        """
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._MachineName = params.get("MachineName")
        self._MachineState = params.get("MachineState")
        self._Zone = params.get("Zone")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._CreatedAt = params.get("CreatedAt")
        self._LoginStatus = params.get("LoginStatus")
        self._IsProtectedFromScaleIn = params.get("IsProtectedFromScaleIn")
        self._DisplayName = params.get("DisplayName")
        self._CPU = params.get("CPU")
        self._GPU = params.get("GPU")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._Memory = params.get("Memory")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceFamily = params.get("InstanceFamily")
        self._LanIp = params.get("LanIp")
        self._InstanceType = params.get("InstanceType")
        self._ExpiredTime = params.get("ExpiredTime")
        self._SecurityGroupIDs = params.get("SecurityGroupIDs")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._OsImage = params.get("OsImage")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeNodePoolInfo(AbstractModel):
    """Native node pool information

    """

    def __init__(self):
        r"""
        :param _Scaling: Scaling configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Scaling: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        :param _SubnetIds: Subnet list
        :type SubnetIds: list of str
        :param _SecurityGroupIds: Security group list
Note: This field may return "null", indicating that no valid value can be obtained.
        :type SecurityGroupIds: list of str
        :param _UpgradeSettings: Automatic upgrade configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type UpgradeSettings: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        :param _AutoRepair: Whether to enable self-healing capability
Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoRepair: bool
        :param _InstanceChargeType: Node billing type
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: Billing configuration of monthly subscription models
Note: This field may return "null", indicating that no valid value can be obtained.
        :type InstanceChargePrepaid: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        :param _SystemDisk: System disk configuration
        :type SystemDisk: :class:`tencentcloud.tke.v20220501.models.Disk`
        :param _KeyIds: Key ID list
Note: This field may return "null", indicating that no valid value can be obtained.
        :type KeyIds: list of str
        :param _Management: Machine system configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Management: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        :param _HealthCheckPolicyName: Fault self-healing rule name
Note: This field may return "null", indicating that no valid value can be obtained.
        :type HealthCheckPolicyName: str
        :param _HostNamePattern: hostname pattern string of native node pools
Note: This field may return "null", indicating that no valid value can be obtained.
        :type HostNamePattern: str
        :param _KubeletArgs: kubelet custom parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :type KubeletArgs: list of str
        :param _Lifecycle: Predefined script
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Lifecycle: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        :param _RuntimeRootDir: Runtime root directory
Note: This field may return "null", indicating that no valid value can be obtained.
        :type RuntimeRootDir: str
        :param _EnableAutoscaling: Whether to enable Auto Scaling (AS)
Note: This field may return "null", indicating that no valid value can be obtained.
        :type EnableAutoscaling: bool
        :param _InstanceTypes: List of models
        :type InstanceTypes: list of str
        :param _Replicas: Desired node count
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Replicas: int
        :param _ReadyReplicas: Number of ready machines
        :type ReadyReplicas: int
        :param _InternetAccessible: Public network bandwidth configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type InternetAccessible: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        :param _DataDisks: Data disk of native node pools
Note: This field may return "null", indicating that no valid value can be obtained.
        :type DataDisks: list of DataDisk
        :param _MachineType: Native node models: Native, NativeCVM
Note: This field may return "null", indicating that no valid value can be obtained.
        :type MachineType: str
        """
        self._Scaling = None
        self._SubnetIds = None
        self._SecurityGroupIds = None
        self._UpgradeSettings = None
        self._AutoRepair = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._SystemDisk = None
        self._KeyIds = None
        self._Management = None
        self._HealthCheckPolicyName = None
        self._HostNamePattern = None
        self._KubeletArgs = None
        self._Lifecycle = None
        self._RuntimeRootDir = None
        self._EnableAutoscaling = None
        self._InstanceTypes = None
        self._Replicas = None
        self._ReadyReplicas = None
        self._InternetAccessible = None
        self._DataDisks = None
        self._MachineType = None

    @property
    def Scaling(self):
        """Scaling configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        """
        return self._Scaling

    @Scaling.setter
    def Scaling(self, Scaling):
        self._Scaling = Scaling

    @property
    def SubnetIds(self):
        """Subnet list
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        """Security group list
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UpgradeSettings(self):
        """Automatic upgrade configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        """
        return self._UpgradeSettings

    @UpgradeSettings.setter
    def UpgradeSettings(self, UpgradeSettings):
        self._UpgradeSettings = UpgradeSettings

    @property
    def AutoRepair(self):
        """Whether to enable self-healing capability
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._AutoRepair

    @AutoRepair.setter
    def AutoRepair(self, AutoRepair):
        self._AutoRepair = AutoRepair

    @property
    def InstanceChargeType(self):
        """Node billing type
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """Billing configuration of monthly subscription models
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def SystemDisk(self):
        """System disk configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.Disk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def KeyIds(self):
        """Key ID list
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def Management(self):
        """Machine system configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        """
        return self._Management

    @Management.setter
    def Management(self, Management):
        self._Management = Management

    @property
    def HealthCheckPolicyName(self):
        """Fault self-healing rule name
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

    @property
    def HostNamePattern(self):
        """hostname pattern string of native node pools
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._HostNamePattern

    @HostNamePattern.setter
    def HostNamePattern(self, HostNamePattern):
        self._HostNamePattern = HostNamePattern

    @property
    def KubeletArgs(self):
        """kubelet custom parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._KubeletArgs

    @KubeletArgs.setter
    def KubeletArgs(self, KubeletArgs):
        self._KubeletArgs = KubeletArgs

    @property
    def Lifecycle(self):
        """Predefined script
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        """
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def RuntimeRootDir(self):
        """Runtime root directory
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir

    @property
    def EnableAutoscaling(self):
        """Whether to enable Auto Scaling (AS)
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._EnableAutoscaling

    @EnableAutoscaling.setter
    def EnableAutoscaling(self, EnableAutoscaling):
        self._EnableAutoscaling = EnableAutoscaling

    @property
    def InstanceTypes(self):
        """List of models
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Replicas(self):
        """Desired node count
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def ReadyReplicas(self):
        """Number of ready machines
        :rtype: int
        """
        return self._ReadyReplicas

    @ReadyReplicas.setter
    def ReadyReplicas(self, ReadyReplicas):
        self._ReadyReplicas = ReadyReplicas

    @property
    def InternetAccessible(self):
        """Public network bandwidth configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def DataDisks(self):
        """Data disk of native node pools
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def MachineType(self):
        """Native node models: Native, NativeCVM
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._MachineType

    @MachineType.setter
    def MachineType(self, MachineType):
        self._MachineType = MachineType


    def _deserialize(self, params):
        if params.get("Scaling") is not None:
            self._Scaling = MachineSetScaling()
            self._Scaling._deserialize(params.get("Scaling"))
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("UpgradeSettings") is not None:
            self._UpgradeSettings = MachineUpgradeSettings()
            self._UpgradeSettings._deserialize(params.get("UpgradeSettings"))
        self._AutoRepair = params.get("AutoRepair")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("SystemDisk") is not None:
            self._SystemDisk = Disk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._KeyIds = params.get("KeyIds")
        if params.get("Management") is not None:
            self._Management = ManagementConfig()
            self._Management._deserialize(params.get("Management"))
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._HostNamePattern = params.get("HostNamePattern")
        self._KubeletArgs = params.get("KubeletArgs")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifecycleConfig()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        self._EnableAutoscaling = params.get("EnableAutoscaling")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Replicas = params.get("Replicas")
        self._ReadyReplicas = params.get("ReadyReplicas")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeCountSummary(AbstractModel):
    """Node statistics list

    """

    def __init__(self):
        r"""
        :param _ManuallyAdded: Manually managed nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type ManuallyAdded: :class:`tencentcloud.tke.v20220501.models.ManuallyAdded`
        :param _AutoscalingAdded: Automatically managed nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoscalingAdded: :class:`tencentcloud.tke.v20220501.models.AutoscalingAdded`
        """
        self._ManuallyAdded = None
        self._AutoscalingAdded = None

    @property
    def ManuallyAdded(self):
        """Manually managed nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.ManuallyAdded`
        """
        return self._ManuallyAdded

    @ManuallyAdded.setter
    def ManuallyAdded(self, ManuallyAdded):
        self._ManuallyAdded = ManuallyAdded

    @property
    def AutoscalingAdded(self):
        """Automatically managed nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.AutoscalingAdded`
        """
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
    """Node pool information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NodePoolId: Node pool ID
        :type NodePoolId: str
        :param _Tags: Node tags
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Tags: list of TagSpecification
        :param _Taints: Node taint

Note: This field may return "null", indicating that no valid value can be obtained.
        :type Taints: list of Taint
        :param _DeletionProtection: Whether to enable deletion protection
Note: This field may return "null", indicating that no valid value can be obtained.
        :type DeletionProtection: bool
        :param _Unschedulable: Whether the node is unschedulable
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Unschedulable: bool
        :param _Type: Node pool type
        :type Type: str
        :param _Labels: Node Labels
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Labels: list of Label
        :param _LifeState: Node pool status
        :type LifeState: str
        :param _CreatedAt: Creation time
        :type CreatedAt: str
        :param _Name: Node pool name
        :type Name: str
        :param _Native: Native node pool parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Native: :class:`tencentcloud.tke.v20220501.models.NativeNodePoolInfo`
        :param _Annotations: Node annotation list

Note: This field may return "null", indicating that no valid value can be obtained.
        :type Annotations: list of Annotation
        :param _Super: Super node pool parameter, which has a value only when Type equals Super
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Super: :class:`tencentcloud.tke.v20220501.models.SuperNodePoolInfo`
        :param _Regular: General node pool parameter, which has a value only when Type equals Regular
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Regular: :class:`tencentcloud.tke.v20220501.models.RegularNodePoolInfo`
        :param _External: Third-party node pool parameter, which has a value only when Type equals External
Note: This field may return "null", indicating that no valid value can be obtained.
        :type External: :class:`tencentcloud.tke.v20220501.models.ExternalNodePoolInfo`
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._Tags = None
        self._Taints = None
        self._DeletionProtection = None
        self._Unschedulable = None
        self._Type = None
        self._Labels = None
        self._LifeState = None
        self._CreatedAt = None
        self._Name = None
        self._Native = None
        self._Annotations = None
        self._Super = None
        self._Regular = None
        self._External = None

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
    def NodePoolId(self):
        """Node pool ID
        :rtype: str
        """
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Tags(self):
        """Node tags
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of TagSpecification
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Taints(self):
        """Node taint

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of Taint
        """
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def DeletionProtection(self):
        """Whether to enable deletion protection
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Unschedulable(self):
        """Whether the node is unschedulable
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def Type(self):
        """Node pool type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Labels(self):
        """Node Labels
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of Label
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def LifeState(self):
        """Node pool status
        :rtype: str
        """
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def CreatedAt(self):
        """Creation time
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Name(self):
        """Node pool name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Native(self):
        """Native node pool parameters
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.NativeNodePoolInfo`
        """
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Annotations(self):
        """Node annotation list

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of Annotation
        """
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Super(self):
        """Super node pool parameter, which has a value only when Type equals Super
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.SuperNodePoolInfo`
        """
        return self._Super

    @Super.setter
    def Super(self, Super):
        self._Super = Super

    @property
    def Regular(self):
        """General node pool parameter, which has a value only when Type equals Regular
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.RegularNodePoolInfo`
        """
        return self._Regular

    @Regular.setter
    def Regular(self, Regular):
        self._Regular = Regular

    @property
    def External(self):
        """Third-party node pool parameter, which has a value only when Type equals External
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.ExternalNodePoolInfo`
        """
        return self._External

    @External.setter
    def External(self, External):
        self._External = External


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._Unschedulable = params.get("Unschedulable")
        self._Type = params.get("Type")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._LifeState = params.get("LifeState")
        self._CreatedAt = params.get("CreatedAt")
        self._Name = params.get("Name")
        if params.get("Native") is not None:
            self._Native = NativeNodePoolInfo()
            self._Native._deserialize(params.get("Native"))
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Annotation()
                obj._deserialize(item)
                self._Annotations.append(obj)
        if params.get("Super") is not None:
            self._Super = SuperNodePoolInfo()
            self._Super._deserialize(params.get("Super"))
        if params.get("Regular") is not None:
            self._Regular = RegularNodePoolInfo()
            self._Regular._deserialize(params.get("Regular"))
        if params.get("External") is not None:
            self._External = ExternalNodePoolInfo()
            self._External._deserialize(params.get("External"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegularNodeInfo(AbstractModel):
    """General node information

    """

    def __init__(self):
        r"""
        :param _InstanceAdvancedSettings: Node configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        :param _AutoscalingGroupId: Auto scaling group ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoscalingGroupId: str
        """
        self._InstanceAdvancedSettings = None
        self._AutoscalingGroupId = None

    @property
    def InstanceAdvancedSettings(self):
        """Node configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        """
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def AutoscalingGroupId(self):
        """Auto scaling group ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId


    def _deserialize(self, params):
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegularNodePoolInfo(AbstractModel):
    """General node pool information

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: LaunchConfigurationId configuration
        :type LaunchConfigurationId: str
        :param _AutoscalingGroupId: Auto-scaling group ID
        :type AutoscalingGroupId: str
        :param _NodeCountSummary: NodeCountSummary node list
        :type NodeCountSummary: :class:`tencentcloud.tke.v20220501.models.NodeCountSummary`
        :param _AutoscalingGroupStatus: Status information
Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoscalingGroupStatus: str
        :param _MaxNodesNum: Maximum number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type MaxNodesNum: int
        :param _MinNodesNum: Minimum number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type MinNodesNum: int
        :param _DesiredNodesNum: Desired number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type DesiredNodesNum: int
        :param _NodePoolOs: Node pool osName
Note: This field may return "null", indicating that no valid value can be obtained.
        :type NodePoolOs: str
        :param _InstanceAdvancedSettings: Node configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        """
        self._LaunchConfigurationId = None
        self._AutoscalingGroupId = None
        self._NodeCountSummary = None
        self._AutoscalingGroupStatus = None
        self._MaxNodesNum = None
        self._MinNodesNum = None
        self._DesiredNodesNum = None
        self._NodePoolOs = None
        self._InstanceAdvancedSettings = None

    @property
    def LaunchConfigurationId(self):
        """LaunchConfigurationId configuration
        :rtype: str
        """
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def AutoscalingGroupId(self):
        """Auto-scaling group ID
        :rtype: str
        """
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId

    @property
    def NodeCountSummary(self):
        """NodeCountSummary node list
        :rtype: :class:`tencentcloud.tke.v20220501.models.NodeCountSummary`
        """
        return self._NodeCountSummary

    @NodeCountSummary.setter
    def NodeCountSummary(self, NodeCountSummary):
        self._NodeCountSummary = NodeCountSummary

    @property
    def AutoscalingGroupStatus(self):
        """Status information
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._AutoscalingGroupStatus

    @AutoscalingGroupStatus.setter
    def AutoscalingGroupStatus(self, AutoscalingGroupStatus):
        self._AutoscalingGroupStatus = AutoscalingGroupStatus

    @property
    def MaxNodesNum(self):
        """Maximum number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MaxNodesNum

    @MaxNodesNum.setter
    def MaxNodesNum(self, MaxNodesNum):
        self._MaxNodesNum = MaxNodesNum

    @property
    def MinNodesNum(self):
        """Minimum number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MinNodesNum

    @MinNodesNum.setter
    def MinNodesNum(self, MinNodesNum):
        self._MinNodesNum = MinNodesNum

    @property
    def DesiredNodesNum(self):
        """Desired number of nodes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._DesiredNodesNum

    @DesiredNodesNum.setter
    def DesiredNodesNum(self, DesiredNodesNum):
        self._DesiredNodesNum = DesiredNodesNum

    @property
    def NodePoolOs(self):
        """Node pool osName
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._NodePoolOs

    @NodePoolOs.setter
    def NodePoolOs(self, NodePoolOs):
        self._NodePoolOs = NodePoolOs

    @property
    def InstanceAdvancedSettings(self):
        """Node configuration
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        """
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        if params.get("NodeCountSummary") is not None:
            self._NodeCountSummary = NodeCountSummary()
            self._NodeCountSummary._deserialize(params.get("NodeCountSummary"))
        self._AutoscalingGroupStatus = params.get("AutoscalingGroupStatus")
        self._MaxNodesNum = params.get("MaxNodesNum")
        self._MinNodesNum = params.get("MinNodesNum")
        self._DesiredNodesNum = params.get("DesiredNodesNum")
        self._NodePoolOs = params.get("NodePoolOs")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeConfig(AbstractModel):
    """Runtime configuration

    """

    def __init__(self):
        r"""
        :param _RuntimeType: Runtime type
Note: This field may return "null", indicating that no valid value can be obtained.
        :type RuntimeType: str
        :param _RuntimeVersion: Runtime version
Note: This field may return "null", indicating that no valid value can be obtained.
        :type RuntimeVersion: str
        :param _RuntimeRootDir: Runtime root directory
Note: This field may return "null", indicating that no valid value can be obtained.
        :type RuntimeRootDir: str
        """
        self._RuntimeType = None
        self._RuntimeVersion = None
        self._RuntimeRootDir = None

    @property
    def RuntimeType(self):
        """Runtime type
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RuntimeType

    @RuntimeType.setter
    def RuntimeType(self, RuntimeType):
        self._RuntimeType = RuntimeType

    @property
    def RuntimeVersion(self):
        """Runtime version
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def RuntimeRootDir(self):
        """Runtime root directory
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir


    def _deserialize(self, params):
        self._RuntimeType = params.get("RuntimeType")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    """Sorting information

    """

    def __init__(self):
        r"""
        :param _FieldName: Sorting metrics
        :type FieldName: str
        :param _OrderType: Sorting method
        :type OrderType: str
        """
        self._FieldName = None
        self._OrderType = None

    @property
    def FieldName(self):
        """Sorting metrics
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def OrderType(self):
        """Sorting method
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuperNodeInfo(AbstractModel):
    """Super Node Information

    """

    def __init__(self):
        r"""
        :param _Name: Instance name
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Name: str
        :param _AutoRenewFlag: Auto-renewal label
Note: This field may return "null", indicating that no valid value can be obtained.
        :type AutoRenewFlag: int
        :param _ResourceType: Resource type
Note: This field may return "null", indicating that no valid value can be obtained.
        :type ResourceType: str
        :param _CPU: CPU specification of nodes (unit: cores).
Note: This field may return "null", indicating that no valid value can be obtained.
        :type CPU: float
        :param _UsedCPU: Total number of CPUs of Pods on nodes (unit: cores).
Note: This field may return "null", indicating that no valid value can be obtained.
        :type UsedCPU: float
        :param _Memory: Memory specification of nodes (unit: Gi).
Note: This field may return "null", indicating that no valid value can be obtained.
        :type Memory: float
        :param _UsedMemory: Total memory of Pods on nodes (unit: Gi).
Note: This field may return "null", indicating that no valid value can be obtained.
        :type UsedMemory: float
        :param _Zone: Availability zone

Note: This field may return "null", indicating that no valid value can be obtained.
        :type Zone: str
        :param _VpcId: Unique VPC ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet unique ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :type SubnetId: str
        :param _ActiveAt: Effective time
Note: This field may return "null", indicating that no valid value can be obtained.
        :type ActiveAt: str
        :param _ExpireAt: Expiration time

Note: This field may return "null", indicating that no valid value can be obtained.
        :type ExpireAt: str
        :param _MaxCPUScheduledPod: Maximum schedulable CPU specification for a single Pod
Note: This field may return "null", indicating that no valid value can be obtained.
        :type MaxCPUScheduledPod: int
        :param _InstanceAttribute: Instance attributes
Note: This field may return "null", indicating that no valid value can be obtained.
        :type InstanceAttribute: str
        """
        self._Name = None
        self._AutoRenewFlag = None
        self._ResourceType = None
        self._CPU = None
        self._UsedCPU = None
        self._Memory = None
        self._UsedMemory = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._ActiveAt = None
        self._ExpireAt = None
        self._MaxCPUScheduledPod = None
        self._InstanceAttribute = None

    @property
    def Name(self):
        """Instance name
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AutoRenewFlag(self):
        """Auto-renewal label
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ResourceType(self):
        """Resource type
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def CPU(self):
        """CPU specification of nodes (unit: cores).
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: float
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def UsedCPU(self):
        """Total number of CPUs of Pods on nodes (unit: cores).
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: float
        """
        return self._UsedCPU

    @UsedCPU.setter
    def UsedCPU(self, UsedCPU):
        self._UsedCPU = UsedCPU

    @property
    def Memory(self):
        """Memory specification of nodes (unit: Gi).
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: float
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UsedMemory(self):
        """Total memory of Pods on nodes (unit: Gi).
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: float
        """
        return self._UsedMemory

    @UsedMemory.setter
    def UsedMemory(self, UsedMemory):
        self._UsedMemory = UsedMemory

    @property
    def Zone(self):
        """Availability zone

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """Unique VPC ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """Subnet unique ID
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ActiveAt(self):
        """Effective time
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ActiveAt

    @ActiveAt.setter
    def ActiveAt(self, ActiveAt):
        self._ActiveAt = ActiveAt

    @property
    def ExpireAt(self):
        """Expiration time

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ExpireAt

    @ExpireAt.setter
    def ExpireAt(self, ExpireAt):
        self._ExpireAt = ExpireAt

    @property
    def MaxCPUScheduledPod(self):
        """Maximum schedulable CPU specification for a single Pod
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._MaxCPUScheduledPod

    @MaxCPUScheduledPod.setter
    def MaxCPUScheduledPod(self, MaxCPUScheduledPod):
        self._MaxCPUScheduledPod = MaxCPUScheduledPod

    @property
    def InstanceAttribute(self):
        """Instance attributes
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._InstanceAttribute

    @InstanceAttribute.setter
    def InstanceAttribute(self, InstanceAttribute):
        self._InstanceAttribute = InstanceAttribute


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ResourceType = params.get("ResourceType")
        self._CPU = params.get("CPU")
        self._UsedCPU = params.get("UsedCPU")
        self._Memory = params.get("Memory")
        self._UsedMemory = params.get("UsedMemory")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ActiveAt = params.get("ActiveAt")
        self._ExpireAt = params.get("ExpireAt")
        self._MaxCPUScheduledPod = params.get("MaxCPUScheduledPod")
        self._InstanceAttribute = params.get("InstanceAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuperNodePoolInfo(AbstractModel):
    """Virtual node pool information.

    """

    def __init__(self):
        r"""
        :param _SubnetIds: Subnet list
Note: This field may return "null", indicating that no valid value can be obtained.
        :type SubnetIds: list of str
        :param _SecurityGroupIds: Security group list
Note: This field may return "null", indicating that no valid value can be obtained.
        :type SecurityGroupIds: list of str
        """
        self._SubnetIds = None
        self._SecurityGroupIds = None

    @property
    def SubnetIds(self):
        """Subnet list
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        """Security group list
Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """The type of resources the label is bound to. Type currently supported: "cluster".

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
        """Tag key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value
        :rtype: str
        """
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
    """List of tag descriptions. By specifying this parameter, you can bind tags to corresponding resource instances at the same time. Currently, only tags can be bound to cloud host instances.

    """

    def __init__(self):
        r"""
        :param _ResourceType: The type of resources the label is bound to. Type currently supported: "cluster".

Note: This field may return "null", indicating that no valid value can be obtained.
        :type ResourceType: str
        :param _Tags: Tag pair list

Note: This field may return "null", indicating that no valid value can be obtained.
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        """The type of resources the label is bound to. Type currently supported: "cluster".

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        """Tag pair list

Note: This field may return "null", indicating that no valid value can be obtained.
        :rtype: list of Tag
        """
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
    """kubernetes Taint

    """

    def __init__(self):
        r"""
        :param _Key: Key of Taint
        :type Key: str
        :param _Value: Value of Taint
        :type Value: str
        :param _Effect: Effect of Taint
        :type Effect: str
        """
        self._Key = None
        self._Value = None
        self._Effect = None

    @property
    def Key(self):
        """Key of Taint
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Value of Taint
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Effect(self):
        """Effect of Taint
        :rtype: str
        """
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
        


class UpdateNativeNodePoolParam(AbstractModel):
    """Modify native node pool parameters

    """

    def __init__(self):
        r"""
        :param _Scaling: Scaling configuration
        :type Scaling: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        :param _SubnetIds: Subnet list
        :type SubnetIds: list of str
        :param _SecurityGroupIds: Security group list
        :type SecurityGroupIds: list of str
        :param _UpgradeSettings: Automatic upgrade configuration
        :type UpgradeSettings: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        :param _AutoRepair: Whether to enable self-healing capability
        :type AutoRepair: bool
        :param _InstanceChargeType: Change the node billing type
Currently, only pay-as-you-go to monthly subscription is supported:
- PREPAID

        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: Billing configuration of monthly subscription models
        :type InstanceChargePrepaid: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        :param _SystemDisk: System disk configuration
        :type SystemDisk: :class:`tencentcloud.tke.v20220501.models.Disk`
        :param _Management: Machine system configuration
        :type Management: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        :param _HealthCheckPolicyName: Fault self-healing rule name
        :type HealthCheckPolicyName: str
        :param _HostNamePattern: hostname pattern string of native node pools
        :type HostNamePattern: str
        :param _KubeletArgs: kubelet custom parameters
        :type KubeletArgs: list of str
        :param _Lifecycle: Predefined script
        :type Lifecycle: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        :param _RuntimeRootDir: Runtime root directory
        :type RuntimeRootDir: str
        :param _EnableAutoscaling: Whether to enable Auto Scaling (AS)
        :type EnableAutoscaling: bool
        :param _InstanceTypes: List of models
        :type InstanceTypes: list of str
        :param _Replicas: Desired node count
        :type Replicas: int
        :param _DataDisks: Data disk list
        :type DataDisks: list of DataDisk
        :param _KeyIds: ssh public key ID array
        :type KeyIds: list of str
        """
        self._Scaling = None
        self._SubnetIds = None
        self._SecurityGroupIds = None
        self._UpgradeSettings = None
        self._AutoRepair = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._SystemDisk = None
        self._Management = None
        self._HealthCheckPolicyName = None
        self._HostNamePattern = None
        self._KubeletArgs = None
        self._Lifecycle = None
        self._RuntimeRootDir = None
        self._EnableAutoscaling = None
        self._InstanceTypes = None
        self._Replicas = None
        self._DataDisks = None
        self._KeyIds = None

    @property
    def Scaling(self):
        """Scaling configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        """
        return self._Scaling

    @Scaling.setter
    def Scaling(self, Scaling):
        self._Scaling = Scaling

    @property
    def SubnetIds(self):
        """Subnet list
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        """Security group list
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UpgradeSettings(self):
        """Automatic upgrade configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        """
        return self._UpgradeSettings

    @UpgradeSettings.setter
    def UpgradeSettings(self, UpgradeSettings):
        self._UpgradeSettings = UpgradeSettings

    @property
    def AutoRepair(self):
        """Whether to enable self-healing capability
        :rtype: bool
        """
        return self._AutoRepair

    @AutoRepair.setter
    def AutoRepair(self, AutoRepair):
        self._AutoRepair = AutoRepair

    @property
    def InstanceChargeType(self):
        """Change the node billing type
Currently, only pay-as-you-go to monthly subscription is supported:
- PREPAID

        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        """Billing configuration of monthly subscription models
        :rtype: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def SystemDisk(self):
        """System disk configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.Disk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def Management(self):
        """Machine system configuration
        :rtype: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        """
        return self._Management

    @Management.setter
    def Management(self, Management):
        self._Management = Management

    @property
    def HealthCheckPolicyName(self):
        """Fault self-healing rule name
        :rtype: str
        """
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

    @property
    def HostNamePattern(self):
        """hostname pattern string of native node pools
        :rtype: str
        """
        return self._HostNamePattern

    @HostNamePattern.setter
    def HostNamePattern(self, HostNamePattern):
        self._HostNamePattern = HostNamePattern

    @property
    def KubeletArgs(self):
        """kubelet custom parameters
        :rtype: list of str
        """
        return self._KubeletArgs

    @KubeletArgs.setter
    def KubeletArgs(self, KubeletArgs):
        self._KubeletArgs = KubeletArgs

    @property
    def Lifecycle(self):
        """Predefined script
        :rtype: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        """
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def RuntimeRootDir(self):
        """Runtime root directory
        :rtype: str
        """
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir

    @property
    def EnableAutoscaling(self):
        """Whether to enable Auto Scaling (AS)
        :rtype: bool
        """
        return self._EnableAutoscaling

    @EnableAutoscaling.setter
    def EnableAutoscaling(self, EnableAutoscaling):
        self._EnableAutoscaling = EnableAutoscaling

    @property
    def InstanceTypes(self):
        """List of models
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Replicas(self):
        """Desired node count
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def DataDisks(self):
        """Data disk list
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def KeyIds(self):
        """ssh public key ID array
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        if params.get("Scaling") is not None:
            self._Scaling = MachineSetScaling()
            self._Scaling._deserialize(params.get("Scaling"))
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("UpgradeSettings") is not None:
            self._UpgradeSettings = MachineUpgradeSettings()
            self._UpgradeSettings._deserialize(params.get("UpgradeSettings"))
        self._AutoRepair = params.get("AutoRepair")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("SystemDisk") is not None:
            self._SystemDisk = Disk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("Management") is not None:
            self._Management = ManagementConfig()
            self._Management._deserialize(params.get("Management"))
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._HostNamePattern = params.get("HostNamePattern")
        self._KubeletArgs = params.get("KubeletArgs")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifecycleConfig()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        self._EnableAutoscaling = params.get("EnableAutoscaling")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Replicas = params.get("Replicas")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        