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


class Activity(AbstractModel):
    """Compute environment creation or termination activities

    """

    def __init__(self):
        r"""
        :param ActivityId: Activity ID
        :type ActivityId: str
        :param ComputeNodeId: Compute node ID
        :type ComputeNodeId: str
        :param ComputeNodeActivityType: Compute node activity type: creation or termination
        :type ComputeNodeActivityType: str
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param Cause: Cause
        :type Cause: str
        :param ActivityState: Active status
        :type ActivityState: str
        :param StateReason: State reason
        :type StateReason: str
        :param StartTime: Activity start time
        :type StartTime: str
        :param EndTime: Activity end time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param InstanceId: CVM instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        """
        self.ActivityId = None
        self.ComputeNodeId = None
        self.ComputeNodeActivityType = None
        self.EnvId = None
        self.Cause = None
        self.ActivityState = None
        self.StateReason = None
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.ComputeNodeId = params.get("ComputeNodeId")
        self.ComputeNodeActivityType = params.get("ComputeNodeActivityType")
        self.EnvId = params.get("EnvId")
        self.Cause = params.get("Cause")
        self.ActivityState = params.get("ActivityState")
        self.StateReason = params.get("StateReason")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentRunningMode(AbstractModel):
    """Agent running mode

    """

    def __init__(self):
        r"""
        :param Scene: Scenario type. Windows is supported
        :type Scene: str
        :param User: The user that runs the Agent
        :type User: str
        :param Session: The session that runs the Agent
        :type Session: str
        """
        self.Scene = None
        self.User = None
        self.Session = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.User = params.get("User")
        self.Session = params.get("Session")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnonymousComputeEnv(AbstractModel):
    """Compute environment

    """

    def __init__(self):
        r"""
        :param EnvType: Compute environment management type
        :type EnvType: str
        :param EnvData: Compute environment's specific parameters
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: Data disk mounting option
        :type MountDataDisks: list of MountDataDisk
        :param AgentRunningMode: Agent running mode; applicable for Windows
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        """
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.AgentRunningMode = None


    def _deserialize(self, params):
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("AgentRunningMode") is not None:
            self.AgentRunningMode = AgentRunningMode()
            self.AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Application(AbstractModel):
    """Application information

    """

    def __init__(self):
        r"""
        :param Command: Task execution command
        :type Command: str
        :param DeliveryForm: Delivery form of the application. Value range: PACKAGE, LOCAL, which refer to remotely stored software package and local compute environment, respectively.
        :type DeliveryForm: str
        :param PackagePath: Remote storage path of the application package
        :type PackagePath: str
        :param Docker: Relevant configuration of the Docker used by the application. In case that the Docker configuration is used, "LOCAL" DeliveryForm means that the application software inside the Docker image is used directly and run in Docker mode; "PACKAGE" DeliveryForm means that the remote application package is run in Docker mode after being injected into the Docker image. To avoid compatibility issues with different versions of Docker, the Docker installation package and relevant dependencies are taken care of by BatchCompute. For custom images where Docker has already been installed, uninstall Docker first and then use the Docker feature.
        :type Docker: :class:`tencentcloud.batch.v20170312.models.Docker`
        """
        self.Command = None
        self.DeliveryForm = None
        self.PackagePath = None
        self.Docker = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.DeliveryForm = params.get("DeliveryForm")
        self.PackagePath = params.get("PackagePath")
        if params.get("Docker") is not None:
            self.Docker = Docker()
            self.Docker._deserialize(params.get("Docker"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesRequest(AbstractModel):
    """AttachInstances request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param Instances: List of instances that added to the compute environment
        :type Instances: list of Instance
        """
        self.EnvId = None
        self.Instances = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesResponse(AbstractModel):
    """AttachInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Authentication(AbstractModel):
    """Authentication information

    """

    def __init__(self):
        r"""
        :param Scene: Authentication scenario such as COS
        :type Scene: str
        :param SecretId: SecretId
        :type SecretId: str
        :param SecretKey: SecretKey
        :type SecretKey: str
        """
        self.Scene = None
        self.SecretId = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeEnvCreateInfo(AbstractModel):
    """Compute environment creation information

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param EnvName: Compute environment name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvName: str
        :param EnvDescription: Compute environment description
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvDescription: str
        :param EnvType: Compute environment type. Only "MANAGED" type is supported
        :type EnvType: str
        :param EnvData: Compute environment parameter
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: Data disk mounting option
Note: This field may return null, indicating that no valid values can be obtained.
        :type MountDataDisks: list of MountDataDisk
        :param InputMappings: Input mapping
Note: This field may return null, indicating that no valid values can be obtained.
        :type InputMappings: list of InputMapping
        :param Authentications: Authorization information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Authentications: list of Authentication
        :param Notifications: Notification information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Notifications: list of Notification
        :param DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param Tags: Tag list of the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self.EnvId = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.InputMappings = None
        self.Authentications = None
        self.Notifications = None
        self.DesiredComputeNodeCount = None
        self.Tags = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
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
        


class ComputeEnvData(AbstractModel):
    """Compute environment attributes

    """

    def __init__(self):
        r"""
        :param InstanceTypes: List of CVM instance types
        :type InstanceTypes: list of str
        """
        self.InstanceTypes = None


    def _deserialize(self, params):
        self.InstanceTypes = params.get("InstanceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeEnvView(AbstractModel):
    """Compute environment information

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param EnvName: Compute environment name
        :type EnvName: str
        :param Placement: Location information
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param CreateTime: Creation time
        :type CreateTime: str
        :param ComputeNodeMetrics: Compute node statistical metrics
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param EnvType: Compute environment type
        :type EnvType: str
        :param DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param ResourceType: Compute environment resource type. Valid values: `CVM`, `CPM` (Bare Metal)
        :type ResourceType: str
        :param NextAction: Next action
        :type NextAction: str
        :param AttachedComputeNodeCount: Number of compute nodes added to the compute environment by the user
        :type AttachedComputeNodeCount: int
        :param Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self.EnvId = None
        self.EnvName = None
        self.Placement = None
        self.CreateTime = None
        self.ComputeNodeMetrics = None
        self.EnvType = None
        self.DesiredComputeNodeCount = None
        self.ResourceType = None
        self.NextAction = None
        self.AttachedComputeNodeCount = None
        self.Tags = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeMetrics") is not None:
            self.ComputeNodeMetrics = ComputeNodeMetrics()
            self.ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self.EnvType = params.get("EnvType")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.ResourceType = params.get("ResourceType")
        self.NextAction = params.get("NextAction")
        self.AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")
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
        


class ComputeNode(AbstractModel):
    """Compute node

    """

    def __init__(self):
        r"""
        :param ComputeNodeId: Compute node ID
        :type ComputeNodeId: str
        :param ComputeNodeInstanceId: Compute node instance ID. In a CVM scenario, this parameter is the CVM InstanceId
        :type ComputeNodeInstanceId: str
        :param ComputeNodeState: Compute node state
        :type ComputeNodeState: str
        :param Cpu: Number of CPU cores
        :type Cpu: int
        :param Mem: Memory size in GiB
        :type Mem: int
        :param ResourceCreatedTime: Resource creation time
        :type ResourceCreatedTime: str
        :param TaskInstanceNumAvailable: Available capacity of the compute node when running TaskInstance. 0 means that the compute node is busy.
        :type TaskInstanceNumAvailable: int
        :param AgentVersion: BatchCompute Agent version
        :type AgentVersion: str
        :param PrivateIpAddresses: Private IP of the instance
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: Public IP of the instance
        :type PublicIpAddresses: list of str
        :param ResourceType: Compute environment resource type. Valid values: `CVM`, `CPM` (Bare Metal)
        :type ResourceType: str
        :param ResourceOrigin: Source of compute environment resources. <br>BATCH_CREATED: instance resources created by BatchCompute.<br>
USER_ATTACHED: instance resources added by users to the compute environment.
        :type ResourceOrigin: str
        """
        self.ComputeNodeId = None
        self.ComputeNodeInstanceId = None
        self.ComputeNodeState = None
        self.Cpu = None
        self.Mem = None
        self.ResourceCreatedTime = None
        self.TaskInstanceNumAvailable = None
        self.AgentVersion = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.ResourceType = None
        self.ResourceOrigin = None


    def _deserialize(self, params):
        self.ComputeNodeId = params.get("ComputeNodeId")
        self.ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self.ComputeNodeState = params.get("ComputeNodeState")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.ResourceCreatedTime = params.get("ResourceCreatedTime")
        self.TaskInstanceNumAvailable = params.get("TaskInstanceNumAvailable")
        self.AgentVersion = params.get("AgentVersion")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.ResourceType = params.get("ResourceType")
        self.ResourceOrigin = params.get("ResourceOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNodeMetrics(AbstractModel):
    """Compute node statistical metrics

    """

    def __init__(self):
        r"""
        :param SubmittedCount: Number of compute nodes that have been submitted
        :type SubmittedCount: int
        :param CreatingCount: Number of compute nodes that are being created
        :type CreatingCount: int
        :param CreationFailedCount: Number of compute nodes that failed to be created
        :type CreationFailedCount: int
        :param CreatedCount: Number of compute nodes that have been created
        :type CreatedCount: int
        :param RunningCount: Number of running compute nodes
        :type RunningCount: int
        :param DeletingCount: Number of compute nodes that are being terminated
        :type DeletingCount: int
        :param AbnormalCount: Number of exceptional compute nodes
        :type AbnormalCount: int
        """
        self.SubmittedCount = None
        self.CreatingCount = None
        self.CreationFailedCount = None
        self.CreatedCount = None
        self.RunningCount = None
        self.DeletingCount = None
        self.AbnormalCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.CreatingCount = params.get("CreatingCount")
        self.CreationFailedCount = params.get("CreationFailedCount")
        self.CreatedCount = params.get("CreatedCount")
        self.RunningCount = params.get("RunningCount")
        self.DeletingCount = params.get("DeletingCount")
        self.AbnormalCount = params.get("AbnormalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateComputeEnvRequest(AbstractModel):
    """CreateComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param ComputeEnv: Compute environment information
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.NamedComputeEnv`
        :param Placement: Location information
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param ClientToken: The string used to guarantee the idempotency of the request, which is generated by the user and must be unique for different requests. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        """
        self.ComputeEnv = None
        self.Placement = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("ComputeEnv") is not None:
            self.ComputeEnv = NamedComputeEnv()
            self.ComputeEnv._deserialize(params.get("ComputeEnv"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateComputeEnvResponse(AbstractModel):
    """CreateComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateTaskTemplateRequest(AbstractModel):
    """CreateTaskTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TaskTemplateName: Task template name
        :type TaskTemplateName: str
        :param TaskTemplateInfo: Task template content with the same parameter requirements as the task
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param TaskTemplateDescription: Task template description
        :type TaskTemplateDescription: str
        :param Tags: Tag list. By setting this parameter, you can bind tags to a task template. Each task template supports up to 10 tags.
        :type Tags: list of Tag
        """
        self.TaskTemplateName = None
        self.TaskTemplateInfo = None
        self.TaskTemplateDescription = None
        self.Tags = None


    def _deserialize(self, params):
        self.TaskTemplateName = params.get("TaskTemplateName")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")
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
        


class CreateTaskTemplateResponse(AbstractModel):
    """CreateTaskTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TaskTemplateId: Task template ID
        :type TaskTemplateId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskTemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Describes data disk information.

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteComputeEnvRequest(AbstractModel):
    """DeleteComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteComputeEnvResponse(AbstractModel):
    """DeleteComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Job ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobResponse(AbstractModel):
    """DeleteJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTaskTemplatesRequest(AbstractModel):
    """DeleteTaskTemplates request structure.

    """

    def __init__(self):
        r"""
        :param TaskTemplateIds: This API is used to delete task template information.
        :type TaskTemplateIds: list of str
        """
        self.TaskTemplateIds = None


    def _deserialize(self, params):
        self.TaskTemplateIds = params.get("TaskTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskTemplatesResponse(AbstractModel):
    """DeleteTaskTemplates response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Dependence(AbstractModel):
    """Dependency

    """

    def __init__(self):
        r"""
        :param StartTask: Dependency start task name |
        :type StartTask: str
        :param EndTask: Dependency end task name |
        :type EndTask: str
        """
        self.StartTask = None
        self.EndTask = None


    def _deserialize(self, params):
        self.StartTask = params.get("StartTask")
        self.EndTask = params.get("EndTask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableCvmInstanceTypesRequest(AbstractModel):
    """DescribeAvailableCvmInstanceTypes request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>
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
        


class DescribeAvailableCvmInstanceTypesResponse(AbstractModel):
    """DescribeAvailableCvmInstanceTypes response structure.

    """

    def __init__(self):
        r"""
        :param InstanceTypeConfigSet: Array of model configurations
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


class DescribeComputeEnvActivitiesRequest(AbstractModel):
    """DescribeComputeEnvActivities request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of returned results
        :type Limit: int
        :param Filters: Filter
<li> compute-node-id - String - Required: No - (Filter) Filter by compute node ID.</li>
        :type Filters: :class:`tencentcloud.batch.v20170312.models.Filter`
        """
        self.EnvId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvActivitiesResponse(AbstractModel):
    """DescribeComputeEnvActivities response structure.

    """

    def __init__(self):
        r"""
        :param ActivitySet: List of activities in the compute environment
        :type ActivitySet: list of Activity
        :param TotalCount: Number of activities
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ActivitySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfoRequest(AbstractModel):
    """DescribeComputeEnvCreateInfo request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvCreateInfoResponse(AbstractModel):
    """DescribeComputeEnvCreateInfo response structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param EnvName: Compute environment name
        :type EnvName: str
        :param EnvDescription: Compute environment description
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvDescription: str
        :param EnvType: Compute environment type. Only "MANAGED" type is supported
        :type EnvType: str
        :param EnvData: Compute environment parameter
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: Data disk mounting option
        :type MountDataDisks: list of MountDataDisk
        :param InputMappings: Input mapping
        :type InputMappings: list of InputMapping
        :param Authentications: Authorization information
        :type Authentications: list of Authentication
        :param Notifications: Notification information
        :type Notifications: list of Notification
        :param DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnvId = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.InputMappings = None
        self.Authentications = None
        self.Notifications = None
        self.DesiredComputeNodeCount = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfosRequest(AbstractModel):
    """DescribeComputeEnvCreateInfos request structure.

    """

    def __init__(self):
        r"""
        :param EnvIds: Compute environment ID
        :type EnvIds: list of str
        :param Filters: Filter
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> env-id - String - Required: No - (Filter) Filter by compute environment ID.</li>
<li> env-name - String - Required: No - (Filter) Filter by compute environment name.</li>
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of returned results
        :type Limit: int
        """
        self.EnvIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvIds = params.get("EnvIds")
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
        


class DescribeComputeEnvCreateInfosResponse(AbstractModel):
    """DescribeComputeEnvCreateInfos response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of compute environments
        :type TotalCount: int
        :param ComputeEnvCreateInfoSet: List of compute environment creation information
        :type ComputeEnvCreateInfoSet: list of ComputeEnvCreateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComputeEnvCreateInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComputeEnvCreateInfoSet") is not None:
            self.ComputeEnvCreateInfoSet = []
            for item in params.get("ComputeEnvCreateInfoSet"):
                obj = ComputeEnvCreateInfo()
                obj._deserialize(item)
                self.ComputeEnvCreateInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvRequest(AbstractModel):
    """DescribeComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvResponse(AbstractModel):
    """DescribeComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param EnvName: Compute environment name
        :type EnvName: str
        :param Placement: Location information
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param CreateTime: Compute environment creation time
        :type CreateTime: str
        :param ComputeNodeSet: List of compute nodes
        :type ComputeNodeSet: list of ComputeNode
        :param ComputeNodeMetrics: Compute node statistical metrics
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param EnvType: Compute environment type
        :type EnvType: str
        :param ResourceType: Compute environment resource type. Valid values: CVM, CPM (Bare Metal)
        :type ResourceType: str
        :param NextAction: Next action
        :type NextAction: str
        :param AttachedComputeNodeCount: Number of compute nodes added to the compute environment by the user
        :type AttachedComputeNodeCount: int
        :param Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnvId = None
        self.EnvName = None
        self.Placement = None
        self.CreateTime = None
        self.ComputeNodeSet = None
        self.ComputeNodeMetrics = None
        self.DesiredComputeNodeCount = None
        self.EnvType = None
        self.ResourceType = None
        self.NextAction = None
        self.AttachedComputeNodeCount = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeSet") is not None:
            self.ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNode()
                obj._deserialize(item)
                self.ComputeNodeSet.append(obj)
        if params.get("ComputeNodeMetrics") is not None:
            self.ComputeNodeMetrics = ComputeNodeMetrics()
            self.ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvType = params.get("EnvType")
        self.ResourceType = params.get("ResourceType")
        self.NextAction = params.get("NextAction")
        self.AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvsRequest(AbstractModel):
    """DescribeComputeEnvs request structure.

    """

    def __init__(self):
        r"""
        :param EnvIds: Compute environment ID
        :type EnvIds: list of str
        :param Filters: Filter.
<li> `zone` - String - Optional - Filter by availability zone.</li>
<li> `env-id` - String - Optional - Filter by compute environment ID.</li>
<li> `env-name` - String - Optional - Filter by compute environment name.</li>
<li> `resource-type` - String - Optional - Filter by compute resource type, which can be CVM or CPM (BM).</li>
<li> `tag-key` - String - Optional - Filter by tag key.</li>
</li>`tag-value` - String - Optional - Filter by tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with the `EnvIds` parameter.
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of returned results
        :type Limit: int
        """
        self.EnvIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvIds = params.get("EnvIds")
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
        


class DescribeComputeEnvsResponse(AbstractModel):
    """DescribeComputeEnvs response structure.

    """

    def __init__(self):
        r"""
        :param ComputeEnvSet: List of compute environments
        :type ComputeEnvSet: list of ComputeEnvView
        :param TotalCount: Number of compute environments
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ComputeEnvSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ComputeEnvSet") is not None:
            self.ComputeEnvSet = []
            for item in params.get("ComputeEnvSet"):
                obj = ComputeEnvView()
                obj._deserialize(item)
                self.ComputeEnvSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCvmZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos request structure.

    """

    def __init__(self):
        r"""
        :param Filters: Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>
<li> instance-type - String - Required: No - (Filter) Filter by model.</li>
<li> instance-charge-type - String - Required: No - (Filter) Filter by instance billing method. ( POSTPAID_BY_HOUR: pay-as-you-go | SPOTPAID: bidding.)  </li>
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
        


class DescribeCvmZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos response structure.

    """

    def __init__(self):
        r"""
        :param InstanceTypeQuotaSet: List of model configurations in the availability zone.
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


class DescribeInstanceCategoriesRequest(AbstractModel):
    """DescribeInstanceCategories request structure.

    """


class DescribeInstanceCategoriesResponse(AbstractModel):
    """DescribeInstanceCategories response structure.

    """

    def __init__(self):
        r"""
        :param InstanceCategorySet: List of CVM instance categories
        :type InstanceCategorySet: list of InstanceCategoryItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceCategorySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceCategorySet") is not None:
            self.InstanceCategorySet = []
            for item in params.get("InstanceCategorySet"):
                obj = InstanceCategoryItem()
                obj._deserialize(item)
                self.InstanceCategorySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobResponse(AbstractModel):
    """DescribeJob response structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        :param JobName: Instance name
        :type JobName: str
        :param Zone: Information of availability zone
        :type Zone: str
        :param Priority: Instance priority
        :type Priority: int
        :param JobState: Instance state
        :type JobState: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param EndTime: End time
        :type EndTime: str
        :param TaskSet: Task view information
        :type TaskSet: list of TaskView
        :param DependenceSet: Information of the dependency among tasks
        :type DependenceSet: list of Dependence
        :param TaskMetrics: Task statistical metrics
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        :param TaskInstanceMetrics: Task instance statistical metrics
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param StateReason: Instance failure reason
        :type StateReason: str
        :param Tags: Tag list bound to the job.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param NextAction: Next action
Note: This field may return `null`, indicating that no valid value was found.
        :type NextAction: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.Zone = None
        self.Priority = None
        self.JobState = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskSet = None
        self.DependenceSet = None
        self.TaskMetrics = None
        self.TaskInstanceMetrics = None
        self.StateReason = None
        self.Tags = None
        self.NextAction = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Zone = params.get("Zone")
        self.Priority = params.get("Priority")
        self.JobState = params.get("JobState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskView()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        if params.get("DependenceSet") is not None:
            self.DependenceSet = []
            for item in params.get("DependenceSet"):
                obj = Dependence()
                obj._deserialize(item)
                self.DependenceSet.append(obj)
        if params.get("TaskMetrics") is not None:
            self.TaskMetrics = TaskMetrics()
            self.TaskMetrics._deserialize(params.get("TaskMetrics"))
        if params.get("TaskInstanceMetrics") is not None:
            self.TaskInstanceMetrics = TaskInstanceMetrics()
            self.TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self.StateReason = params.get("StateReason")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.NextAction = params.get("NextAction")
        self.RequestId = params.get("RequestId")


class DescribeJobSubmitInfoRequest(AbstractModel):
    """DescribeJobSubmitInfo request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobSubmitInfoResponse(AbstractModel):
    """DescribeJobSubmitInfo response structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        :param JobName: Instance name
        :type JobName: str
        :param JobDescription: Instance description
        :type JobDescription: str
        :param Priority: Job priority. Tasks (Task) and task instances (TaskInstance) inherit the priority of the job
        :type Priority: int
        :param Tasks: Task information
        :type Tasks: list of Task
        :param Dependences: Dependency information
        :type Dependences: list of Dependence
        :param Tags: Tag list bound to the job.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.JobDescription = None
        self.Priority = None
        self.Tasks = None
        self.Dependences = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobDescription = params.get("JobDescription")
        self.Priority = params.get("Priority")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        if params.get("Dependences") is not None:
            self.Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self.Dependences.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs request structure.

    """

    def __init__(self):
        r"""
        :param JobIds: Instance ID
        :type JobIds: list of str
        :param Filters: Filter.
<li> `job-id` - String - Optional - Filter by job ID.</li>
<li> `job-name` - String - Optional - Filter by job name.</li>
<li> `job-state` - String - Optional - Filter by job state.</li>
<li> `zone` - String - Optional - Filter by availability zone.</li>
<li> `tag-key` - String - Optional - Filter by tag key.</li>
<li> `tag-value` - String - Optional - Filter by tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with the `JobIds` parameter.
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of returned results
        :type Limit: int
        """
        self.JobIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
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
        


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs response structure.

    """

    def __init__(self):
        r"""
        :param JobSet: List of instances
        :type JobSet: list of JobView
        :param TotalCount: Number of eligible instances
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self.JobSet = []
            for item in params.get("JobSet"):
                obj = JobView()
                obj._deserialize(item)
                self.JobSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskLogsRequest(AbstractModel):
    """DescribeTaskLogs request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        :param TaskName: Job name
        :type TaskName: str
        :param TaskInstanceIndexes: Set of task instances
        :type TaskInstanceIndexes: list of int non-negative
        :param Offset: Starting task instance
        :type Offset: int
        :param Limit: Maximum number of task instances
        :type Limit: int
        """
        self.JobId = None
        self.TaskName = None
        self.TaskInstanceIndexes = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskInstanceIndexes = params.get("TaskInstanceIndexes")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogsResponse(AbstractModel):
    """DescribeTaskLogs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of task instances
        :type TotalCount: int
        :param TaskInstanceLogSet: Set of task instance log details
        :type TaskInstanceLogSet: list of TaskInstanceLog
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInstanceLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInstanceLogSet") is not None:
            self.TaskInstanceLogSet = []
            for item in params.get("TaskInstanceLogSet"):
                obj = TaskInstanceLog()
                obj._deserialize(item)
                self.TaskInstanceLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        :param TaskName: Task name
        :type TaskName: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of returned results. Default value: 100. Maximum value: 1,000.
        :type Limit: int
        :param Filters: Filter as detailed below:
<li> task-instance-type - String - Required: No - (Filter) Filter by task instance state. (SUBMITTED: submitted; PENDING: pending; RUNNABLE: runnable; STARTING: starting; RUNNING: running; SUCCEED: succeeded; FAILED: failed; FAILED_INTERRUPTED: instance retained after failure).</li>
        :type Filters: list of Filter
        """
        self.JobId = None
        self.TaskName = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask response structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        :param TaskName: Job name
        :type TaskName: str
        :param TaskState: Job state
        :type TaskState: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param EndTime: End time
        :type EndTime: str
        :param TaskInstanceTotalCount: Total number of task instances
        :type TaskInstanceTotalCount: int
        :param TaskInstanceSet: Task instance information
        :type TaskInstanceSet: list of TaskInstanceView
        :param TaskInstanceMetrics: Task instance statistical metrics
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.JobId = None
        self.TaskName = None
        self.TaskState = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskInstanceTotalCount = None
        self.TaskInstanceSet = None
        self.TaskInstanceMetrics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskState = params.get("TaskState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        self.TaskInstanceTotalCount = params.get("TaskInstanceTotalCount")
        if params.get("TaskInstanceSet") is not None:
            self.TaskInstanceSet = []
            for item in params.get("TaskInstanceSet"):
                obj = TaskInstanceView()
                obj._deserialize(item)
                self.TaskInstanceSet.append(obj)
        if params.get("TaskInstanceMetrics") is not None:
            self.TaskInstanceMetrics = TaskInstanceMetrics()
            self.TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self.RequestId = params.get("RequestId")


class DescribeTaskTemplatesRequest(AbstractModel):
    """DescribeTaskTemplates request structure.

    """

    def __init__(self):
        r"""
        :param TaskTemplateIds: Job template ID
        :type TaskTemplateIds: list of str
        :param Filters: Filter.
<li> `task-template-name` - String - Optional - Filter by task template name.</li>
<li> `tag-key` - String - Optional - Filter by tag key.</li>
<li> `tag-value` - String - Optional - Filter by tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with the `TaskTemplateIds` parameter.
        :type Filters: list of Filter
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of returned results
        :type Limit: int
        """
        self.TaskTemplateIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TaskTemplateIds = params.get("TaskTemplateIds")
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
        


class DescribeTaskTemplatesResponse(AbstractModel):
    """DescribeTaskTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TaskTemplateSet: List of job templates
        :type TaskTemplateSet: list of TaskTemplateView
        :param TotalCount: Number of job templates
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskTemplateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskTemplateSet") is not None:
            self.TaskTemplateSet = []
            for item in params.get("TaskTemplateSet"):
                obj = TaskTemplateView()
                obj._deserialize(item)
                self.TaskTemplateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param InstanceIds: Instance ID list
        :type InstanceIds: list of str
        """
        self.EnvId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachInstancesResponse(AbstractModel):
    """DetachInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Docker(AbstractModel):
    """Docker container information

    """

    def __init__(self):
        r"""
        :param User: Docker Hub username or Tencent Registry username
        :type User: str
        :param Password: Docker Hub password or Tencent Registry password
        :type Password: str
        :param Image: For Docker Hub, enter "[user/repo]:[tag]"; for Tencent Registry, enter "ccr.ccs.tencentyun.com/[namespace/repo]:[tag]"
        :type Image: str
        :param Server: For Docker Hub, this can be left blank, but please ensure public network access is present. For Tencent Registry, the server address is "ccr.ccs.tencentyun.com"
        :type Server: str
        """
        self.User = None
        self.Password = None
        self.Image = None
        self.Server = None


    def _deserialize(self, params):
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.Image = params.get("Image")
        self.Server = params.get("Server")
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
        :type SecurityService: :class:`tencentcloud.batch.v20170312.models.RunSecurityServiceEnabled`
        :param MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.batch.v20170312.models.RunMonitorServiceEnabled`
        :param AutomationService: Enables the TAT service. If this parameter is not specified, the TAT service will not be enabled.
        :type AutomationService: :class:`tencentcloud.batch.v20170312.models.RunAutomationServiceEnabled`
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
        


class EnvData(AbstractModel):
    """Compute environment information

    """

    def __init__(self):
        r"""
        :param InstanceType: CVM instance type, which cannot be present together with InstanceTypes or InstanceTypeOptions at the same time.
        :type InstanceType: str
        :param ImageId: CVM image ID
        :type ImageId: str
        :param SystemDisk: Information of the instance's system disk configuration
        :type SystemDisk: :class:`tencentcloud.batch.v20170312.models.SystemDisk`
        :param DataDisks: Information of the instance's data disk configuration
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: Information of the VPC configuration, which cannot be specified together with Zones and VirtualPrivateClouds.
        :type VirtualPrivateCloud: :class:`tencentcloud.batch.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: Information of the public network bandwidth configuration
        :type InternetAccessible: :class:`tencentcloud.batch.v20170312.models.InternetAccessible`
        :param InstanceName: CVM instance display name
        :type InstanceName: str
        :param LoginSettings: Instance login settings
        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        :param SecurityGroupIds: Security group of the instance
        :type SecurityGroupIds: list of str
        :param EnhancedService: Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitoring and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.batch.v20170312.models.EnhancedService`
        :param InstanceChargeType: CVM instance billing method <br><li>POSTPAID_BY_HOUR: pay-as-you-go by the hour <br><li>SPOTPAID: bidding <br>Default value: POSTPAID_BY_HOUR.
        :type InstanceChargeType: str
        :param InstanceMarketOptions: Market-related options of the instance, such as parameters related to spot instance
        :type InstanceMarketOptions: :class:`tencentcloud.batch.v20170312.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: List of CVM instance types, which cannot be present together with InstanceType or InstanceTypeOptions at the same time. After the field is specified, the system will try creating compute nodes in the order of the models until successful creation and then stop the traversal process. Up to 10 models are supported.
        :type InstanceTypes: list of str
        :param InstanceTypeOptions: CVM instance model configuration, which cannot be present together with InstanceType or InstanceTypes at the same time.
        :type InstanceTypeOptions: :class:`tencentcloud.batch.v20170312.models.InstanceTypeOptions`
        :param Zones: List of availability zones (creation of CVM instances across availability zones is supported), which cannot be specified together with VirtualPrivateCloud or VirtualPrivateClouds at the same time.
        :type Zones: list of str
        :param VirtualPrivateClouds: List of VPCs (creation of CVM instances across VPCs is supported), which cannot be specified together with VirtualPrivateCloud or Zones at the same time.
        :type VirtualPrivateClouds: list of VirtualPrivateCloud
        """
        self.InstanceType = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None
        self.InstanceTypeOptions = None
        self.Zones = None
        self.VirtualPrivateClouds = None


    def _deserialize(self, params):
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
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTypeOptions") is not None:
            self.InstanceTypeOptions = InstanceTypeOptions()
            self.InstanceTypeOptions._deserialize(params.get("InstanceTypeOptions"))
        self.Zones = params.get("Zones")
        if params.get("VirtualPrivateClouds") is not None:
            self.VirtualPrivateClouds = []
            for item in params.get("VirtualPrivateClouds"):
                obj = VirtualPrivateCloud()
                obj._deserialize(item)
                self.VirtualPrivateClouds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    """Environment variable

    """

    def __init__(self):
        r"""
        :param Name: Environment variable name
        :type Name: str
        :param Value: Environment variable value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventConfig(AbstractModel):
    """Event configuration

    """

    def __init__(self):
        r"""
        :param EventName: Event type. Value range: <br/><li>"JOB_RUNNING": the job is running, applicable to "SubmitJob". </li><li>"JOB_SUCCEED: the job succeeded, applicable to "SubmitJob". </li><li>"JOB_FAILED": the job failed, applicable to "SubmitJob". </li><li>"JOB_FAILED_INTERRUPTED": the job failed and the instance is retained, applicable to "SubmitJob". </li><li>"TASK_RUNNING": the task is running, applicable to "SubmitJob". </li><li>"TASK_SUCCEED": the task succeeded, applicable to "SubmitJob". </li><li>"TASK_FAILED": the task failed, applicable to "SubmitJob". </li><li>"TASK_FAILED_INTERRUPTED": the task failed and the instance is retained, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_RUNNING": the task instance is running, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_SUCCEED": the task instance succeeded, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_FAILED": the task instance failed, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_FAILED_INTERRUPTED": the task instance failed and the instance is retained, applicable to "SubmitJob". </li><li>"COMPUTE_ENV_CREATED": the compute environment has been created, applicable to "CreateComputeEnv". </li><li>"COMPUTE_ENV_DELETED": the compute environment has been deleted, applicable to "CreateComputeEnv". </li><li>"COMPUTE_NODE_CREATED": the compute node has been created, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_CREATION_FAILED": the compute node creation failed, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_RUNNING": the compute node is running, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_ABNORMAL": the compute node is exceptional, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_DELETING": the compute node has been deleted, applicable to "CreateComputeEnv" and "SubmitJob". </li>
        :type EventName: str
        :param EventVars: Custom key-value pair
        :type EventVars: list of EventVar
        """
        self.EventName = None
        self.EventVars = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        if params.get("EventVars") is not None:
            self.EventVars = []
            for item in params.get("EventVars"):
                obj = EventVar()
                obj._deserialize(item)
                self.EventVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventVar(AbstractModel):
    """Custom key-value pair

    """

    def __init__(self):
        r"""
        :param Name: Custom key
        :type Name: str
        :param Value: Custom value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :type StorageBlockAttr: :class:`tencentcloud.batch.v20170312.models.StorageBlock`
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
        


class InputMapping(AbstractModel):
    """Input mapping

    """

    def __init__(self):
        r"""
        :param SourcePath: Source path
        :type SourcePath: str
        :param DestinationPath: Destination path
        :type DestinationPath: str
        :param MountOptionParameter: Mounting configuration item parameter
        :type MountOptionParameter: str
        """
        self.SourcePath = None
        self.DestinationPath = None
        self.MountOptionParameter = None


    def _deserialize(self, params):
        self.SourcePath = params.get("SourcePath")
        self.DestinationPath = params.get("DestinationPath")
        self.MountOptionParameter = params.get("MountOptionParameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """Describes information on an instance

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param ImageId: Image ID.
        :type ImageId: str
        :param LoginSettings: Instance login settings.
        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        """
        self.InstanceId = None
        self.ImageId = None
        self.LoginSettings = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceCategoryItem(AbstractModel):
    """List of instance categories

    """

    def __init__(self):
        r"""
        :param InstanceCategory: Instance type name
        :type InstanceCategory: str
        :param InstanceFamilySet: List of instance families
        :type InstanceFamilySet: list of str
        """
        self.InstanceCategory = None
        self.InstanceFamilySet = None


    def _deserialize(self, params):
        self.InstanceCategory = params.get("InstanceCategory")
        self.InstanceFamilySet = params.get("InstanceFamilySet")
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
        :type SpotOptions: :class:`tencentcloud.batch.v20170312.models.SpotMarketOptions`
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
        


class InstanceTypeConfig(AbstractModel):
    """Information of InstanceTypeConfig available to BatchCompute

    """

    def __init__(self):
        r"""
        :param Mem: Memory size in GB.
        :type Mem: int
        :param Cpu: Number of CPU cores.
        :type Cpu: int
        :param InstanceType: Instance model.
        :type InstanceType: str
        :param Zone: Availability zone.
        :type Zone: str
        :param InstanceFamily: Instance model family.
        :type InstanceFamily: str
        """
        self.Mem = None
        self.Cpu = None
        self.InstanceType = None
        self.Zone = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.Mem = params.get("Mem")
        self.Cpu = params.get("Cpu")
        self.InstanceType = params.get("InstanceType")
        self.Zone = params.get("Zone")
        self.InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeOptions(AbstractModel):
    """Instance model configuration.

    """

    def __init__(self):
        r"""
        :param CPU: Number of CPU cores.
        :type CPU: int
        :param Memory: Memory size in GB.
        :type Memory: int
        :param InstanceCategories: Instance model category. Value range: "ALL", "GENERAL", "GENERAL_2", "GENERAL_3", "COMPUTE", "COMPUTE_2", and "COMPUTE_3". Default value: "ALL".
        :type InstanceCategories: list of str
        """
        self.CPU = None
        self.Memory = None
        self.InstanceCategories = None


    def _deserialize(self, params):
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.InstanceCategories = params.get("InstanceCategories")
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
        :type Externals: :class:`tencentcloud.batch.v20170312.models.Externals`
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
        :type Price: :class:`tencentcloud.batch.v20170312.models.ItemPrice`
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
        


class JobView(AbstractModel):
    """Instance information

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        :param JobName: Instance name
        :type JobName: str
        :param JobState: Instance state
        :type JobState: str
        :param Priority: Instance priority
        :type Priority: int
        :param Placement: Location information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param CreateTime: Creation time
        :type CreateTime: str
        :param EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param TaskMetrics: Task statistical metrics
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        :param Tags: Tag list bound to the job.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self.JobId = None
        self.JobName = None
        self.JobState = None
        self.Priority = None
        self.Placement = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskMetrics = None
        self.Tags = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobState = params.get("JobState")
        self.Priority = params.get("Priority")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        if params.get("TaskMetrics") is not None:
            self.TaskMetrics = TaskMetrics()
            self.TaskMetrics._deserialize(params.get("TaskMetrics"))
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
    """Describes the configuration and information related to instance login.

    """

    def __init__(self):
        r"""
        :param Password: Login password of the instance. The password requirements vary among different operating systems: <br><li>For Linux instances, the password must be 8-16 characters long and contain at least one character from two of the following categories: [a-z, A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]. <br><li>For Windows instances, the password must be 12-16 characters long and contain at least one character from three of the following categories: [a-z], [A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. <br><br>If this parameter is not specified, a random password will be generated and sent to you via the Message Center.
        :type Password: str
        :param KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
        :type KeyIds: list of str
        :param KeepImageLogin: Whether to keep the original settings of an image. You cannot specify this parameter and `Password` or `KeyIds.N` at the same time. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. Valid values: <br><li>TRUE: keep the login settings of the image <br><li>FALSE: do not keep the login settings of the image <br><br>Default value: FALSE.
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
        


class ModifyComputeEnvRequest(AbstractModel):
    """ModifyComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param EnvName: Compute environment name
        :type EnvName: str
        :param EnvDescription: Compute environment description
        :type EnvDescription: str
        :param EnvData: Compute environment attributes
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.ComputeEnvData`
        """
        self.EnvId = None
        self.DesiredComputeNodeCount = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvData = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        if params.get("EnvData") is not None:
            self.EnvData = ComputeEnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyComputeEnvResponse(AbstractModel):
    """ModifyComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskTemplateRequest(AbstractModel):
    """ModifyTaskTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TaskTemplateId: Job template ID
        :type TaskTemplateId: str
        :param TaskTemplateName: Job template name
        :type TaskTemplateName: str
        :param TaskTemplateDescription: Job template description
        :type TaskTemplateDescription: str
        :param TaskTemplateInfo: Job template information
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        """
        self.TaskTemplateId = None
        self.TaskTemplateName = None
        self.TaskTemplateDescription = None
        self.TaskTemplateInfo = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.TaskTemplateName = params.get("TaskTemplateName")
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskTemplateResponse(AbstractModel):
    """ModifyTaskTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MountDataDisk(AbstractModel):
    """Data disk mounting option

    """

    def __init__(self):
        r"""
        :param LocalPath: Mounting point. For Linux, this parameter should be a valid path. For Windows, this parameter should be a system disk letter such as "H:\\"
        :type LocalPath: str
        :param FileSystemType: File system type. For Linux, "EXT3" and "EXT4" are supported and the default value is "EXT3". For Windows, only "NTFS" is supported
        :type FileSystemType: str
        """
        self.LocalPath = None
        self.FileSystemType = None


    def _deserialize(self, params):
        self.LocalPath = params.get("LocalPath")
        self.FileSystemType = params.get("FileSystemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamedComputeEnv(AbstractModel):
    """Compute environment

    """

    def __init__(self):
        r"""
        :param EnvName: Compute environment name
        :type EnvName: str
        :param DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param EnvDescription: Compute environment description
        :type EnvDescription: str
        :param EnvType: Compute environment management type
        :type EnvType: str
        :param EnvData: Compute environment's specific parameters
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: Data disk mounting option
        :type MountDataDisks: list of MountDataDisk
        :param Authentications: Authorization information
        :type Authentications: list of Authentication
        :param InputMappings: Input mapping information
        :type InputMappings: list of InputMapping
        :param AgentRunningMode: Agent running mode; applicable for Windows
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        :param Notifications: Notification information
        :type Notifications: :class:`tencentcloud.batch.v20170312.models.Notification`
        :param ActionIfComputeNodeInactive: Inactive node processing policy. Default value: RECREATE, which means that instance resources will be re-created periodically for compute nodes where instance creation fails or is abnormally returned.
        :type ActionIfComputeNodeInactive: str
        :param ResourceMaxRetryCount: When the instances are failed to be created or returned because of exceptions, the related compute node will retry to create instances periodically. This parameter specifies the maximum retry attempts. The max value is 11 and the default value is 7.
        :type ResourceMaxRetryCount: int
        :param Tags: Tag list. By setting this parameter, you can bind tags to a compute environment. Each compute environment supports up to 10 tags.
        :type Tags: list of Tag
        """
        self.EnvName = None
        self.DesiredComputeNodeCount = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.Authentications = None
        self.InputMappings = None
        self.AgentRunningMode = None
        self.Notifications = None
        self.ActionIfComputeNodeInactive = None
        self.ResourceMaxRetryCount = None
        self.Tags = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("AgentRunningMode") is not None:
            self.AgentRunningMode = AgentRunningMode()
            self.AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        if params.get("Notifications") is not None:
            self.Notifications = Notification()
            self.Notifications._deserialize(params.get("Notifications"))
        self.ActionIfComputeNodeInactive = params.get("ActionIfComputeNodeInactive")
        self.ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")
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
        


class Notification(AbstractModel):
    """Notification information

    """

    def __init__(self):
        r"""
        :param TopicName: CMQ topic name which should be valid and associated with a subscription
        :type TopicName: str
        :param EventConfigs: Event configuration
        :type EventConfigs: list of EventConfig
        """
        self.TopicName = None
        self.EventConfigs = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        if params.get("EventConfigs") is not None:
            self.EventConfigs = []
            for item in params.get("EventConfigs"):
                obj = EventConfig()
                obj._deserialize(item)
                self.EventConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMapping(AbstractModel):
    """Output mapping

    """

    def __init__(self):
        r"""
        :param SourcePath: Source path
        :type SourcePath: str
        :param DestinationPath: Destination path
        :type DestinationPath: str
        """
        self.SourcePath = None
        self.DestinationPath = None


    def _deserialize(self, params):
        self.SourcePath = params.get("SourcePath")
        self.DestinationPath = params.get("DestinationPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMappingConfig(AbstractModel):
    """Output mapping configuration

    """

    def __init__(self):
        r"""
        :param Scene: Storage type. Only COS is supported
        :type Scene: str
        :param WorkerNum: Number of parallel workers
        :type WorkerNum: int
        :param WorkerPartSize: Size of a worker part, in MB.
        :type WorkerPartSize: int
        """
        self.Scene = None
        self.WorkerNum = None
        self.WorkerPartSize = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.WorkerNum = params.get("WorkerNum")
        self.WorkerPartSize = params.get("WorkerPartSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """Describes the location of an instance, including its availability zone, project, host (for CDH products only), primary host IP, etc.

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
        


class RedirectInfo(AbstractModel):
    """Redirection information

    """

    def __init__(self):
        r"""
        :param StdoutRedirectPath: Standard output redirection path
        :type StdoutRedirectPath: str
        :param StderrRedirectPath: Standard error redirection path
        :type StderrRedirectPath: str
        :param StdoutRedirectFileName: Standard output redirection file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutRedirectFileName: str
        :param StderrRedirectFileName: Standard error redirection file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}
        :type StderrRedirectFileName: str
        """
        self.StdoutRedirectPath = None
        self.StderrRedirectPath = None
        self.StdoutRedirectFileName = None
        self.StderrRedirectFileName = None


    def _deserialize(self, params):
        self.StdoutRedirectPath = params.get("StdoutRedirectPath")
        self.StderrRedirectPath = params.get("StderrRedirectPath")
        self.StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self.StderrRedirectFileName = params.get("StderrRedirectFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedirectLocalInfo(AbstractModel):
    """Local redirection information

    """

    def __init__(self):
        r"""
        :param StdoutLocalPath: Standard output redirection local path
        :type StdoutLocalPath: str
        :param StderrLocalPath: Standard error redirection local path
        :type StderrLocalPath: str
        :param StdoutLocalFileName: Standard output redirection local file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutLocalFileName: str
        :param StderrLocalFileName: Standard error redirection local file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}
        :type StderrLocalFileName: str
        """
        self.StdoutLocalPath = None
        self.StderrLocalPath = None
        self.StdoutLocalFileName = None
        self.StderrLocalFileName = None


    def _deserialize(self, params):
        self.StdoutLocalPath = params.get("StdoutLocalPath")
        self.StderrLocalPath = params.get("StderrLocalPath")
        self.StdoutLocalFileName = params.get("StdoutLocalFileName")
        self.StderrLocalFileName = params.get("StderrLocalFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryJobsRequest(AbstractModel):
    """RetryJobs request structure.

    """

    def __init__(self):
        r"""
        :param JobIds: List of instance IDs.
        :type JobIds: list of str
        """
        self.JobIds = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryJobsResponse(AbstractModel):
    """RetryJobs response structure.

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
        


class SystemDisk(AbstractModel):
    """Describes information on the block device where the operating system is stored, i.e., the system disk.

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Information on tags

    """

    def __init__(self):
        r"""
        :param Key: Tag key.
Note: This field may return `null`, indicating that no valid value was found.
        :type Key: str
        :param Value: Tag value.
Note: This field may return `null`, indicating that no valid value was found.
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
        


class Task(AbstractModel):
    """Task

    """

    def __init__(self):
        r"""
        :param Application: Application information
        :type Application: :class:`tencentcloud.batch.v20170312.models.Application`
        :param TaskName: Job name, which should be unique within instance
        :type TaskName: str
        :param TaskInstanceNum: Number of running task instances
        :type TaskInstanceNum: int
        :param ComputeEnv: Compute environment information. One (and only one) parameter must be specified for ComputeEnv and EnvId.
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.AnonymousComputeEnv`
        :param EnvId: Compute environment ID. One (and only one) parameter must be specified for ComputeEnv and EnvId.
        :type EnvId: str
        :param RedirectInfo: Redirection information
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param RedirectLocalInfo: Local redirection information
        :type RedirectLocalInfo: :class:`tencentcloud.batch.v20170312.models.RedirectLocalInfo`
        :param InputMappings: Input mapping
        :type InputMappings: list of InputMapping
        :param OutputMappings: Output mapping
        :type OutputMappings: list of OutputMapping
        :param OutputMappingConfigs: Output mapping configuration
        :type OutputMappingConfigs: list of OutputMappingConfig
        :param EnvVars: Custom environment variable
        :type EnvVars: list of EnvVar
        :param Authentications: Authorization information
        :type Authentications: list of Authentication
        :param FailedAction: The processing method after the TaskInstance fails; Value range: TERMINATE (default), INTERRUPT, FAST_INTERRUPT.
        :type FailedAction: str
        :param MaxRetryCount: The maximum number of retries after the task fails. Default value: 0
        :type MaxRetryCount: int
        :param Timeout: Timeout period in seconds after the task starts. Defaults value: 86,400
        :type Timeout: int
        :param MaxConcurrentNum: The maximum number of concurrent tasks. There is no limit by default.
        :type MaxConcurrentNum: int
        :param RestartComputeNode: Restarts the compute node after the task is completed. This is suitable for specifying the compute environment for task execution.
        :type RestartComputeNode: bool
        :param ResourceMaxRetryCount: Maximum number of retry attempts after failing to create computing resources such as the CVM in the task launch process. Default value: 0.
        :type ResourceMaxRetryCount: int
        """
        self.Application = None
        self.TaskName = None
        self.TaskInstanceNum = None
        self.ComputeEnv = None
        self.EnvId = None
        self.RedirectInfo = None
        self.RedirectLocalInfo = None
        self.InputMappings = None
        self.OutputMappings = None
        self.OutputMappingConfigs = None
        self.EnvVars = None
        self.Authentications = None
        self.FailedAction = None
        self.MaxRetryCount = None
        self.Timeout = None
        self.MaxConcurrentNum = None
        self.RestartComputeNode = None
        self.ResourceMaxRetryCount = None


    def _deserialize(self, params):
        if params.get("Application") is not None:
            self.Application = Application()
            self.Application._deserialize(params.get("Application"))
        self.TaskName = params.get("TaskName")
        self.TaskInstanceNum = params.get("TaskInstanceNum")
        if params.get("ComputeEnv") is not None:
            self.ComputeEnv = AnonymousComputeEnv()
            self.ComputeEnv._deserialize(params.get("ComputeEnv"))
        self.EnvId = params.get("EnvId")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = RedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        if params.get("RedirectLocalInfo") is not None:
            self.RedirectLocalInfo = RedirectLocalInfo()
            self.RedirectLocalInfo._deserialize(params.get("RedirectLocalInfo"))
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("OutputMappings") is not None:
            self.OutputMappings = []
            for item in params.get("OutputMappings"):
                obj = OutputMapping()
                obj._deserialize(item)
                self.OutputMappings.append(obj)
        if params.get("OutputMappingConfigs") is not None:
            self.OutputMappingConfigs = []
            for item in params.get("OutputMappingConfigs"):
                obj = OutputMappingConfig()
                obj._deserialize(item)
                self.OutputMappingConfigs.append(obj)
        if params.get("EnvVars") is not None:
            self.EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self.EnvVars.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        self.FailedAction = params.get("FailedAction")
        self.MaxRetryCount = params.get("MaxRetryCount")
        self.Timeout = params.get("Timeout")
        self.MaxConcurrentNum = params.get("MaxConcurrentNum")
        self.RestartComputeNode = params.get("RestartComputeNode")
        self.ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceLog(AbstractModel):
    """Task instance log details.

    """

    def __init__(self):
        r"""
        :param TaskInstanceIndex: Task instance
        :type TaskInstanceIndex: int
        :param StdoutLog: Standard output log (Base64-encoded)
Note: This field may return null, indicating that no valid values can be obtained.
        :type StdoutLog: str
        :param StderrLog: Standard error log (Base64-encoded)
Note: This field may return null, indicating that no valid values can be obtained.
        :type StderrLog: str
        :param StdoutRedirectPath: Standard output redirection path
Note: This field may return null, indicating that no valid values can be obtained.
        :type StdoutRedirectPath: str
        :param StderrRedirectPath: Standard error redirection path
Note: This field may return null, indicating that no valid values can be obtained.
        :type StderrRedirectPath: str
        :param StdoutRedirectFileName: Standard output redirection file name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StdoutRedirectFileName: str
        :param StderrRedirectFileName: Standard error redirection file name
Note: This field may return null, indicating that no valid values can be obtained.
        :type StderrRedirectFileName: str
        """
        self.TaskInstanceIndex = None
        self.StdoutLog = None
        self.StderrLog = None
        self.StdoutRedirectPath = None
        self.StderrRedirectPath = None
        self.StdoutRedirectFileName = None
        self.StderrRedirectFileName = None


    def _deserialize(self, params):
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")
        self.StdoutLog = params.get("StdoutLog")
        self.StderrLog = params.get("StderrLog")
        self.StdoutRedirectPath = params.get("StdoutRedirectPath")
        self.StderrRedirectPath = params.get("StderrRedirectPath")
        self.StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self.StderrRedirectFileName = params.get("StderrRedirectFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceMetrics(AbstractModel):
    """Task instance statistical metrics

    """

    def __init__(self):
        r"""
        :param SubmittedCount: Submitted count
        :type SubmittedCount: int
        :param PendingCount: Pending count
        :type PendingCount: int
        :param RunnableCount: Runnable count
        :type RunnableCount: int
        :param StartingCount: Starting count
        :type StartingCount: int
        :param RunningCount: Running count
        :type RunningCount: int
        :param SucceedCount: Succeed count
        :type SucceedCount: int
        :param FailedInterruptedCount: FailedInterrupted count
        :type FailedInterruptedCount: int
        :param FailedCount: Failed count
        :type FailedCount: int
        """
        self.SubmittedCount = None
        self.PendingCount = None
        self.RunnableCount = None
        self.StartingCount = None
        self.RunningCount = None
        self.SucceedCount = None
        self.FailedInterruptedCount = None
        self.FailedCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.PendingCount = params.get("PendingCount")
        self.RunnableCount = params.get("RunnableCount")
        self.StartingCount = params.get("StartingCount")
        self.RunningCount = params.get("RunningCount")
        self.SucceedCount = params.get("SucceedCount")
        self.FailedInterruptedCount = params.get("FailedInterruptedCount")
        self.FailedCount = params.get("FailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceView(AbstractModel):
    """Task instance view information

    """

    def __init__(self):
        r"""
        :param TaskInstanceIndex: Task instance index
        :type TaskInstanceIndex: int
        :param TaskInstanceState: Task instance state
        :type TaskInstanceState: str
        :param ExitCode: Exit code after application execution is completed
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExitCode: int
        :param StateReason: Task instance state reason. If the task instance fails, the reason for the failure will be logged.
        :type StateReason: str
        :param ComputeNodeInstanceId: The InstanceId of the compute node (e.g., CVM instance) where the task instance is running. This field is empty if the task instance is not running or has already been completed and will change when the task instance is retried
Note: This field may return null, indicating that no valid values can be obtained.
        :type ComputeNodeInstanceId: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param LaunchTime: Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type LaunchTime: str
        :param RunningTime: Running start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunningTime: str
        :param EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param RedirectInfo: Redirection information
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param StateDetailedReason: Task instance state reason details. If the task instance fails, the reason for the failure will be logged
        :type StateDetailedReason: str
        """
        self.TaskInstanceIndex = None
        self.TaskInstanceState = None
        self.ExitCode = None
        self.StateReason = None
        self.ComputeNodeInstanceId = None
        self.CreateTime = None
        self.LaunchTime = None
        self.RunningTime = None
        self.EndTime = None
        self.RedirectInfo = None
        self.StateDetailedReason = None


    def _deserialize(self, params):
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")
        self.TaskInstanceState = params.get("TaskInstanceState")
        self.ExitCode = params.get("ExitCode")
        self.StateReason = params.get("StateReason")
        self.ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self.CreateTime = params.get("CreateTime")
        self.LaunchTime = params.get("LaunchTime")
        self.RunningTime = params.get("RunningTime")
        self.EndTime = params.get("EndTime")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = RedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        self.StateDetailedReason = params.get("StateDetailedReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskMetrics(AbstractModel):
    """Task statistical metrics

    """

    def __init__(self):
        r"""
        :param SubmittedCount: Submitted count
        :type SubmittedCount: int
        :param PendingCount: Pending count
        :type PendingCount: int
        :param RunnableCount: Runnable count
        :type RunnableCount: int
        :param StartingCount: Starting count
        :type StartingCount: int
        :param RunningCount: Running count
        :type RunningCount: int
        :param SucceedCount: Succeed count
        :type SucceedCount: int
        :param FailedInterruptedCount: FailedInterrupted count
        :type FailedInterruptedCount: int
        :param FailedCount: Failed count
        :type FailedCount: int
        """
        self.SubmittedCount = None
        self.PendingCount = None
        self.RunnableCount = None
        self.StartingCount = None
        self.RunningCount = None
        self.SucceedCount = None
        self.FailedInterruptedCount = None
        self.FailedCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.PendingCount = params.get("PendingCount")
        self.RunnableCount = params.get("RunnableCount")
        self.StartingCount = params.get("StartingCount")
        self.RunningCount = params.get("RunningCount")
        self.SucceedCount = params.get("SucceedCount")
        self.FailedInterruptedCount = params.get("FailedInterruptedCount")
        self.FailedCount = params.get("FailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskTemplateView(AbstractModel):
    """Task template information

    """

    def __init__(self):
        r"""
        :param TaskTemplateId: Task template ID
        :type TaskTemplateId: str
        :param TaskTemplateName: Task template name
        :type TaskTemplateName: str
        :param TaskTemplateDescription: Task template description
        :type TaskTemplateDescription: str
        :param TaskTemplateInfo: Task template information
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Tags: Tag list bound to the task template.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self.TaskTemplateId = None
        self.TaskTemplateName = None
        self.TaskTemplateDescription = None
        self.TaskTemplateInfo = None
        self.CreateTime = None
        self.Tags = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.TaskTemplateName = params.get("TaskTemplateName")
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self.CreateTime = params.get("CreateTime")
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
        


class TaskView(AbstractModel):
    """Task view information

    """

    def __init__(self):
        r"""
        :param TaskName: Task name
        :type TaskName: str
        :param TaskState: Task state
        :type TaskState: str
        :param CreateTime: Create time
        :type CreateTime: str
        :param EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self.TaskName = None
        self.TaskState = None
        self.CreateTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskState = params.get("TaskState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodeRequest(AbstractModel):
    """TerminateComputeNode request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param ComputeNodeId: Compute node ID
        :type ComputeNodeId: str
        """
        self.EnvId = None
        self.ComputeNodeId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ComputeNodeId = params.get("ComputeNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodeResponse(AbstractModel):
    """TerminateComputeNode response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateComputeNodesRequest(AbstractModel):
    """TerminateComputeNodes request structure.

    """

    def __init__(self):
        r"""
        :param EnvId: Compute environment ID
        :type EnvId: str
        :param ComputeNodeIds: List of compute node IDs
        :type ComputeNodeIds: list of str
        """
        self.EnvId = None
        self.ComputeNodeIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ComputeNodeIds = params.get("ComputeNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodesResponse(AbstractModel):
    """TerminateComputeNodes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateJobRequest(AbstractModel):
    """TerminateJob request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateJobResponse(AbstractModel):
    """TerminateJob response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTaskInstanceRequest(AbstractModel):
    """TerminateTaskInstance request structure.

    """

    def __init__(self):
        r"""
        :param JobId: Instance ID
        :type JobId: str
        :param TaskName: Task name
        :type TaskName: str
        :param TaskInstanceIndex: Task instance index
        :type TaskInstanceIndex: int
        """
        self.JobId = None
        self.TaskName = None
        self.TaskInstanceIndex = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTaskInstanceResponse(AbstractModel):
    """TerminateTaskInstance response structure.

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
        