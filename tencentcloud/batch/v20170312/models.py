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
        """
        :param ActivityId: Activity ID\n        :type ActivityId: str\n        :param ComputeNodeId: Compute node ID\n        :type ComputeNodeId: str\n        :param ComputeNodeActivityType: Compute node activity type: creation or termination\n        :type ComputeNodeActivityType: str\n        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param Cause: Cause\n        :type Cause: str\n        :param ActivityState: Active status\n        :type ActivityState: str\n        :param StateReason: State reason\n        :type StateReason: str\n        :param StartTime: Activity start time\n        :type StartTime: str\n        :param EndTime: Activity end time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EndTime: str\n        :param InstanceId: CVM instance ID
Note: This field may return null, indicating that no valid values can be obtained.\n        :type InstanceId: str\n        """
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
        """
        :param Scene: Scenario type. Windows is supported\n        :type Scene: str\n        :param User: The user that runs the Agent\n        :type User: str\n        :param Session: The session that runs the Agent\n        :type Session: str\n        """
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
        """
        :param EnvType: Compute environment management type\n        :type EnvType: str\n        :param EnvData: Compute environment's specific parameters\n        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`\n        :param MountDataDisks: Data disk mounting option\n        :type MountDataDisks: list of MountDataDisk\n        :param AgentRunningMode: Agent running mode; applicable for Windows\n        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`\n        """
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
        """
        :param Command: Task execution command\n        :type Command: str\n        :param DeliveryForm: Delivery form of the application. Value range: PACKAGE, LOCAL, which refer to remotely stored software package and local compute environment, respectively.\n        :type DeliveryForm: str\n        :param PackagePath: Remote storage path of the application package\n        :type PackagePath: str\n        :param Docker: Relevant configuration of the Docker used by the application. In case that the Docker configuration is used, "LOCAL" DeliveryForm means that the application software inside the Docker image is used directly and run in Docker mode; "PACKAGE" DeliveryForm means that the remote application package is run in Docker mode after being injected into the Docker image. To avoid compatibility issues with different versions of Docker, the Docker installation package and relevant dependencies are taken care of by BatchCompute. For custom images where Docker has already been installed, uninstall Docker first and then use the Docker feature.\n        :type Docker: :class:`tencentcloud.batch.v20170312.models.Docker`\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param Instances: List of instances that added to the compute environment\n        :type Instances: list of Instance\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Authentication(AbstractModel):
    """Authentication information

    """

    def __init__(self):
        """
        :param Scene: Authentication scenario such as COS\n        :type Scene: str\n        :param SecretId: SecretId\n        :type SecretId: str\n        :param SecretKey: SecretKey\n        :type SecretKey: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param EnvName: Compute environment name
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EnvName: str\n        :param EnvDescription: Compute environment description
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EnvDescription: str\n        :param EnvType: Compute environment type. Only "MANAGED" type is supported\n        :type EnvType: str\n        :param EnvData: Compute environment parameter\n        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`\n        :param MountDataDisks: Data disk mounting option
Note: This field may return null, indicating that no valid values can be obtained.\n        :type MountDataDisks: list of MountDataDisk\n        :param InputMappings: Input mapping
Note: This field may return null, indicating that no valid values can be obtained.\n        :type InputMappings: list of InputMapping\n        :param Authentications: Authorization information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Authentications: list of Authentication\n        :param Notifications: Notification information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Notifications: list of Notification\n        :param DesiredComputeNodeCount: Number of desired compute nodes\n        :type DesiredComputeNodeCount: int\n        :param Tags: Tag list of the compute environment.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        """
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
        """
        :param InstanceTypes: List of CVM instance types\n        :type InstanceTypes: list of str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param EnvName: Compute environment name\n        :type EnvName: str\n        :param Placement: Location information\n        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param ComputeNodeMetrics: Compute node statistical metrics\n        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`\n        :param EnvType: Compute environment type\n        :type EnvType: str\n        :param DesiredComputeNodeCount: Number of desired compute nodes\n        :type DesiredComputeNodeCount: int\n        :param ResourceType: Compute environment resource type. Valid values: `CVM`, `CPM` (Bare Metal)\n        :type ResourceType: str\n        :param NextAction: Next action\n        :type NextAction: str\n        :param AttachedComputeNodeCount: Number of compute nodes added to the compute environment by the user\n        :type AttachedComputeNodeCount: int\n        :param Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        """
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
        """
        :param ComputeNodeId: Compute node ID\n        :type ComputeNodeId: str\n        :param ComputeNodeInstanceId: Compute node instance ID. In a CVM scenario, this parameter is the CVM InstanceId\n        :type ComputeNodeInstanceId: str\n        :param ComputeNodeState: Compute node state\n        :type ComputeNodeState: str\n        :param Cpu: Number of CPU cores\n        :type Cpu: int\n        :param Mem: Memory size in GiB\n        :type Mem: int\n        :param ResourceCreatedTime: Resource creation time\n        :type ResourceCreatedTime: str\n        :param TaskInstanceNumAvailable: Available capacity of the compute node when running TaskInstance. 0 means that the compute node is busy.\n        :type TaskInstanceNumAvailable: int\n        :param AgentVersion: BatchCompute Agent version\n        :type AgentVersion: str\n        :param PrivateIpAddresses: Private IP of the instance\n        :type PrivateIpAddresses: list of str\n        :param PublicIpAddresses: Public IP of the instance\n        :type PublicIpAddresses: list of str\n        :param ResourceType: Compute environment resource type. Valid values: `CVM`, `CPM` (Bare Metal)\n        :type ResourceType: str\n        :param ResourceOrigin: Source of compute environment resources. <br>BATCH_CREATED: instance resources created by BatchCompute.<br>
USER_ATTACHED: instance resources added by users to the compute environment.\n        :type ResourceOrigin: str\n        """
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
        """
        :param SubmittedCount: Number of compute nodes that have been submitted\n        :type SubmittedCount: int\n        :param CreatingCount: Number of compute nodes that are being created\n        :type CreatingCount: int\n        :param CreationFailedCount: Number of compute nodes that failed to be created\n        :type CreationFailedCount: int\n        :param CreatedCount: Number of compute nodes that have been created\n        :type CreatedCount: int\n        :param RunningCount: Number of running compute nodes\n        :type RunningCount: int\n        :param DeletingCount: Number of compute nodes that are being terminated\n        :type DeletingCount: int\n        :param AbnormalCount: Number of exceptional compute nodes\n        :type AbnormalCount: int\n        """
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
        """
        :param ComputeEnv: Compute environment information\n        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.NamedComputeEnv`\n        :param Placement: Location information\n        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`\n        :param ClientToken: The string used to guarantee the idempotency of the request, which is generated by the user and must be unique for different requests. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\n        :type ClientToken: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateTaskTemplateRequest(AbstractModel):
    """CreateTaskTemplate request structure.

    """

    def __init__(self):
        """
        :param TaskTemplateName: Task template name\n        :type TaskTemplateName: str\n        :param TaskTemplateInfo: Task template content with the same parameter requirements as the task\n        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`\n        :param TaskTemplateDescription: Task template description\n        :type TaskTemplateDescription: str\n        :param Tags: Tag list. By setting this parameter, you can bind tags to a task template. Each task template supports up to 10 tags.\n        :type Tags: list of Tag\n        """
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
        """
        :param TaskTemplateId: Task template ID\n        :type TaskTemplateId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskTemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Describes data disk information.

    """

    def __init__(self):
        """
        :param DiskSize: Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.\n        :type DiskSize: int\n        :param DiskType: Data disk type. For more information about limits on different data disk types, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values: <br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>LOCAL_NVME: local NVME disk, specified in the `InstanceType`<br><li>LOCAL_PRO: local HDD disk, specified in the `InstanceType`<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><li>CLOUD_SSD: SSD<br><li>CLOUD_HSSD: Enhanced SSD<br><li>CLOUD_TSSD: Tremendous SSD<br><br>Default value: LOCAL_BASIC.<br><br>This parameter is invalid for the `ResizeInstanceDisk` API.\n        :type DiskType: str\n        :param DiskId: Data disk ID. Data disks of the type `LOCAL_BASIC` or `LOCAL_SSD` do not have IDs and do not support this parameter.\n        :type DiskId: str\n        :param DeleteWithInstance: Whether to terminate the data disk when its CVM is terminated. Valid values:
<li>TRUE: terminate the data disk when its CVM is terminated. This value only supports pay-as-you-go cloud disks billed on an hourly basis.
<li>FALSE: retain the data disk when its CVM is terminated.<br>
Default value: TRUE<br>
Currently this parameter is only used in the `RunInstances` API.
Note: This field may return null, indicating that no valid value is found.\n        :type DeleteWithInstance: bool\n        :param SnapshotId: Data disk snapshot ID. The size of the selected data disk snapshot must be smaller than that of the data disk.
Note: This field may return null, indicating that no valid value is found.\n        :type SnapshotId: str\n        :param Encrypt: Specifies whether the data disk is encrypted. Valid values: 
<li>TRUE: encrypted
<li>FALSE: not encrypted<br>
Default value: FALSE<br>
This parameter is only used with `RunInstances`.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Encrypt: bool\n        :param KmsKeyId: ID of the custom CMK in the format of UUID or “kms-abcd1234”. This parameter is used to encrypt cloud disks.

Currently, this parameter is only used in the `RunInstances` API.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KmsKeyId: str\n        :param ThroughputPerformance: Cloud disk performance, in MB/s
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type ThroughputPerformance: int\n        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskId = None
        self.DeleteWithInstance = None
        self.SnapshotId = None
        self.Encrypt = None
        self.KmsKeyId = None
        self.ThroughputPerformance = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.SnapshotId = params.get("SnapshotId")
        self.Encrypt = params.get("Encrypt")
        self.KmsKeyId = params.get("KmsKeyId")
        self.ThroughputPerformance = params.get("ThroughputPerformance")
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Job ID\n        :type JobId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTaskTemplatesRequest(AbstractModel):
    """DeleteTaskTemplates request structure.

    """

    def __init__(self):
        """
        :param TaskTemplateIds: This API is used to delete task template information.\n        :type TaskTemplateIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Dependence(AbstractModel):
    """Dependency

    """

    def __init__(self):
        """
        :param StartTask: Dependency start task name |\n        :type StartTask: str\n        :param EndTask: Dependency end task name |\n        :type EndTask: str\n        """
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
        """
        :param Filters: Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>\n        :type Filters: list of Filter\n        """
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
        """
        :param InstanceTypeConfigSet: Array of model configurations\n        :type InstanceTypeConfigSet: list of InstanceTypeConfig\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Number of returned results\n        :type Limit: int\n        :param Filters: Filter
<li> compute-node-id - String - Required: No - (Filter) Filter by compute node ID.</li>\n        :type Filters: :class:`tencentcloud.batch.v20170312.models.Filter`\n        """
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
        """
        :param ActivitySet: List of activities in the compute environment\n        :type ActivitySet: list of Activity\n        :param TotalCount: Number of activities\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param EnvName: Compute environment name\n        :type EnvName: str\n        :param EnvDescription: Compute environment description
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EnvDescription: str\n        :param EnvType: Compute environment type. Only "MANAGED" type is supported\n        :type EnvType: str\n        :param EnvData: Compute environment parameter\n        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`\n        :param MountDataDisks: Data disk mounting option\n        :type MountDataDisks: list of MountDataDisk\n        :param InputMappings: Input mapping\n        :type InputMappings: list of InputMapping\n        :param Authentications: Authorization information\n        :type Authentications: list of Authentication\n        :param Notifications: Notification information\n        :type Notifications: list of Notification\n        :param DesiredComputeNodeCount: Number of desired compute nodes\n        :type DesiredComputeNodeCount: int\n        :param Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param EnvIds: Compute environment ID\n        :type EnvIds: list of str\n        :param Filters: Filter
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> env-id - String - Required: No - (Filter) Filter by compute environment ID.</li>
<li> env-name - String - Required: No - (Filter) Filter by compute environment name.</li>\n        :type Filters: list of Filter\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Number of returned results\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Number of compute environments\n        :type TotalCount: int\n        :param ComputeEnvCreateInfoSet: List of compute environment creation information\n        :type ComputeEnvCreateInfoSet: list of ComputeEnvCreateInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param EnvName: Compute environment name\n        :type EnvName: str\n        :param Placement: Location information\n        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`\n        :param CreateTime: Compute environment creation time\n        :type CreateTime: str\n        :param ComputeNodeSet: List of compute nodes\n        :type ComputeNodeSet: list of ComputeNode\n        :param ComputeNodeMetrics: Compute node statistical metrics\n        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`\n        :param DesiredComputeNodeCount: Number of desired compute nodes\n        :type DesiredComputeNodeCount: int\n        :param EnvType: Compute environment type\n        :type EnvType: str\n        :param ResourceType: Compute environment resource type. Valid values: CVM, CPM (Bare Metal)\n        :type ResourceType: str\n        :param NextAction: Next action\n        :type NextAction: str\n        :param AttachedComputeNodeCount: Number of compute nodes added to the compute environment by the user\n        :type AttachedComputeNodeCount: int\n        :param Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param EnvIds: Compute environment ID\n        :type EnvIds: list of str\n        :param Filters: Filter.
<li> `zone` - String - Optional - Filter by availability zone.</li>
<li> `env-id` - String - Optional - Filter by compute environment ID.</li>
<li> `env-name` - String - Optional - Filter by compute environment name.</li>
<li> `resource-type` - String - Optional - Filter by compute resource type, which can be CVM or CPM (BM).</li>
<li> `tag-key` - String - Optional - Filter by tag key.</li>
</li>`tag-value` - String - Optional - Filter by tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with the `EnvIds` parameter.\n        :type Filters: list of Filter\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Number of returned results\n        :type Limit: int\n        """
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
        """
        :param ComputeEnvSet: List of compute environments\n        :type ComputeEnvSet: list of ComputeEnvView\n        :param TotalCount: Number of compute environments\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Filters: Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>
<li> instance-type - String - Required: No - (Filter) Filter by model.</li>
<li> instance-charge-type - String - Required: No - (Filter) Filter by instance billing method. ( POSTPAID_BY_HOUR: pay-as-you-go | SPOTPAID: bidding.)  </li>\n        :type Filters: list of Filter\n        """
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
        """
        :param InstanceTypeQuotaSet: List of model configurations in the availability zone.\n        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param InstanceCategorySet: List of CVM instance categories\n        :type InstanceCategorySet: list of InstanceCategoryItem\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param JobId: Instance ID\n        :type JobId: str\n        """
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
        """
        :param JobId: Instance ID\n        :type JobId: str\n        :param JobName: Instance name\n        :type JobName: str\n        :param Zone: Information of availability zone\n        :type Zone: str\n        :param Priority: Instance priority\n        :type Priority: int\n        :param JobState: Instance state\n        :type JobState: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param TaskSet: Task view information\n        :type TaskSet: list of TaskView\n        :param DependenceSet: Information of the dependency among tasks\n        :type DependenceSet: list of Dependence\n        :param TaskMetrics: Task statistical metrics\n        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`\n        :param TaskInstanceMetrics: Task instance statistical metrics\n        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`\n        :param StateReason: Instance failure reason\n        :type StateReason: str\n        :param Tags: Tag list bound to the job.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        :param NextAction: Next action
Note: This field may return `null`, indicating that no valid value was found.\n        :type NextAction: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param JobId: Instance ID\n        :type JobId: str\n        """
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
        """
        :param JobId: Instance ID\n        :type JobId: str\n        :param JobName: Instance name\n        :type JobName: str\n        :param JobDescription: Instance description\n        :type JobDescription: str\n        :param Priority: Job priority. Tasks (Task) and task instances (TaskInstance) inherit the priority of the job\n        :type Priority: int\n        :param Tasks: Task information\n        :type Tasks: list of Task\n        :param Dependences: Dependency information\n        :type Dependences: list of Dependence\n        :param Tags: Tag list bound to the job.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param JobIds: Instance ID\n        :type JobIds: list of str\n        :param Filters: Filter.
<li> `job-id` - String - Optional - Filter by job ID.</li>
<li> `job-name` - String - Optional - Filter by job name.</li>
<li> `job-state` - String - Optional - Filter by job state.</li>
<li> `zone` - String - Optional - Filter by availability zone.</li>
<li> `tag-key` - String - Optional - Filter by tag key.</li>
<li> `tag-value` - String - Optional - Filter by tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with the `JobIds` parameter.\n        :type Filters: list of Filter\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Number of returned results\n        :type Limit: int\n        """
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
        """
        :param JobSet: List of instances\n        :type JobSet: list of JobView\n        :param TotalCount: Number of eligible instances\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param JobId: Instance ID\n        :type JobId: str\n        :param TaskName: Job name\n        :type TaskName: str\n        :param TaskInstanceIndexes: Set of task instances\n        :type TaskInstanceIndexes: list of int non-negative\n        :param Offset: Starting task instance\n        :type Offset: int\n        :param Limit: Maximum number of task instances\n        :type Limit: int\n        """
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
        """
        :param TotalCount: Total number of task instances\n        :type TotalCount: int\n        :param TaskInstanceLogSet: Set of task instance log details\n        :type TaskInstanceLogSet: list of TaskInstanceLog\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param JobId: Instance ID\n        :type JobId: str\n        :param TaskName: Task name\n        :type TaskName: str\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Number of returned results. Default value: 100. Maximum value: 1,000.\n        :type Limit: int\n        :param Filters: Filter as detailed below:
<li> task-instance-type - String - Required: No - (Filter) Filter by task instance state. (SUBMITTED: submitted; PENDING: pending; RUNNABLE: runnable; STARTING: starting; RUNNING: running; SUCCEED: succeeded; FAILED: failed; FAILED_INTERRUPTED: instance retained after failure).</li>\n        :type Filters: list of Filter\n        """
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
        """
        :param JobId: Instance ID\n        :type JobId: str\n        :param TaskName: Job name\n        :type TaskName: str\n        :param TaskState: Job state\n        :type TaskState: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param EndTime: End time\n        :type EndTime: str\n        :param TaskInstanceTotalCount: Total number of task instances\n        :type TaskInstanceTotalCount: int\n        :param TaskInstanceSet: Task instance information\n        :type TaskInstanceSet: list of TaskInstanceView\n        :param TaskInstanceMetrics: Task instance statistical metrics\n        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TaskTemplateIds: Job template ID\n        :type TaskTemplateIds: list of str\n        :param Filters: Filter.
<li> `task-template-name` - String - Optional - Filter by task template name.</li>
<li> `tag-key` - String - Optional - Filter by tag key.</li>
<li> `tag-value` - String - Optional - Filter by tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with the `TaskTemplateIds` parameter.\n        :type Filters: list of Filter\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Number of returned results\n        :type Limit: int\n        """
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
        """
        :param TaskTemplateSet: List of job templates\n        :type TaskTemplateSet: list of TaskTemplateView\n        :param TotalCount: Number of job templates\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param InstanceIds: Instance ID list\n        :type InstanceIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Docker(AbstractModel):
    """Docker container information

    """

    def __init__(self):
        """
        :param User: Docker Hub username or Tencent Registry username\n        :type User: str\n        :param Password: Docker Hub password or Tencent Registry password\n        :type Password: str\n        :param Image: For Docker Hub, enter "[user/repo]:[tag]"; for Tencent Registry, enter "ccr.ccs.tencentyun.com/[namespace/repo]:[tag]"\n        :type Image: str\n        :param Server: For Docker Hub, this can be left blank, but please ensure public network access is present. For Tencent Registry, the server address is "ccr.ccs.tencentyun.com"\n        :type Server: str\n        """
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
        """
        :param SecurityService: Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.\n        :type SecurityService: :class:`tencentcloud.batch.v20170312.models.RunSecurityServiceEnabled`\n        :param MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.\n        :type MonitorService: :class:`tencentcloud.batch.v20170312.models.RunMonitorServiceEnabled`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvData(AbstractModel):
    """Compute environment information

    """

    def __init__(self):
        """
        :param InstanceType: CVM instance type, which cannot be present together with InstanceTypes or InstanceTypeOptions at the same time.\n        :type InstanceType: str\n        :param ImageId: CVM image ID\n        :type ImageId: str\n        :param SystemDisk: Information of the instance's system disk configuration\n        :type SystemDisk: :class:`tencentcloud.batch.v20170312.models.SystemDisk`\n        :param DataDisks: Information of the instance's data disk configuration\n        :type DataDisks: list of DataDisk\n        :param VirtualPrivateCloud: Information of the VPC configuration, which cannot be specified together with Zones and VirtualPrivateClouds.\n        :type VirtualPrivateCloud: :class:`tencentcloud.batch.v20170312.models.VirtualPrivateCloud`\n        :param InternetAccessible: Information of the public network bandwidth configuration\n        :type InternetAccessible: :class:`tencentcloud.batch.v20170312.models.InternetAccessible`\n        :param InstanceName: CVM instance display name\n        :type InstanceName: str\n        :param LoginSettings: Instance login settings\n        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`\n        :param SecurityGroupIds: Security group of the instance\n        :type SecurityGroupIds: list of str\n        :param EnhancedService: Enhanced service. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitoring and Cloud Security will be enabled by default.\n        :type EnhancedService: :class:`tencentcloud.batch.v20170312.models.EnhancedService`\n        :param InstanceChargeType: CVM instance billing method <br><li>POSTPAID_BY_HOUR: pay-as-you-go by the hour <br><li>SPOTPAID: bidding <br>Default value: POSTPAID_BY_HOUR.\n        :type InstanceChargeType: str\n        :param InstanceMarketOptions: Market-related options of the instance, such as parameters related to spot instance\n        :type InstanceMarketOptions: :class:`tencentcloud.batch.v20170312.models.InstanceMarketOptionsRequest`\n        :param InstanceTypes: List of CVM instance types, which cannot be present together with InstanceType or InstanceTypeOptions at the same time. After the field is specified, the system will try creating compute nodes in the order of the models until successful creation and then stop the traversal process. Up to 10 models are supported.\n        :type InstanceTypes: list of str\n        :param InstanceTypeOptions: CVM instance model configuration, which cannot be present together with InstanceType or InstanceTypes at the same time.\n        :type InstanceTypeOptions: :class:`tencentcloud.batch.v20170312.models.InstanceTypeOptions`\n        :param Zones: List of availability zones (creation of CVM instances across availability zones is supported), which cannot be specified together with VirtualPrivateCloud or VirtualPrivateClouds at the same time.\n        :type Zones: list of str\n        :param VirtualPrivateClouds: List of VPCs (creation of CVM instances across VPCs is supported), which cannot be specified together with VirtualPrivateCloud or Zones at the same time.\n        :type VirtualPrivateClouds: list of VirtualPrivateCloud\n        """
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
        """
        :param Name: Environment variable name\n        :type Name: str\n        :param Value: Environment variable value\n        :type Value: str\n        """
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
        """
        :param EventName: Event type. Value range: <br/><li>"JOB_RUNNING": the job is running, applicable to "SubmitJob". </li><li>"JOB_SUCCEED: the job succeeded, applicable to "SubmitJob". </li><li>"JOB_FAILED": the job failed, applicable to "SubmitJob". </li><li>"JOB_FAILED_INTERRUPTED": the job failed and the instance is retained, applicable to "SubmitJob". </li><li>"TASK_RUNNING": the task is running, applicable to "SubmitJob". </li><li>"TASK_SUCCEED": the task succeeded, applicable to "SubmitJob". </li><li>"TASK_FAILED": the task failed, applicable to "SubmitJob". </li><li>"TASK_FAILED_INTERRUPTED": the task failed and the instance is retained, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_RUNNING": the task instance is running, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_SUCCEED": the task instance succeeded, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_FAILED": the task instance failed, applicable to "SubmitJob". </li><li>"TASK_INSTANCE_FAILED_INTERRUPTED": the task instance failed and the instance is retained, applicable to "SubmitJob". </li><li>"COMPUTE_ENV_CREATED": the compute environment has been created, applicable to "CreateComputeEnv". </li><li>"COMPUTE_ENV_DELETED": the compute environment has been deleted, applicable to "CreateComputeEnv". </li><li>"COMPUTE_NODE_CREATED": the compute node has been created, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_CREATION_FAILED": the compute node creation failed, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_RUNNING": the compute node is running, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_ABNORMAL": the compute node is exceptional, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>"COMPUTE_NODE_DELETING": the compute node has been deleted, applicable to "CreateComputeEnv" and "SubmitJob". </li>\n        :type EventName: str\n        :param EventVars: Custom key-value pair\n        :type EventVars: list of EventVar\n        """
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
        """
        :param Name: Custom key\n        :type Name: str\n        :param Value: Custom value\n        :type Value: str\n        """
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
        """
        :param ReleaseAddress: Release address
Note: This field may return null, indicating that no valid value is found.\n        :type ReleaseAddress: bool\n        :param UnsupportNetworks: Not supported network. Value: <br><li>BASIC: classic network<br><li>VPC1.0: VPC1.0
Note: This field may return null, indicating that no valid value was found.\n        :type UnsupportNetworks: list of str\n        :param StorageBlockAttr: Attributes of local HDD storage
Note: This field may return null, indicating that no valid value is found.\n        :type StorageBlockAttr: :class:`tencentcloud.batch.v20170312.models.StorageBlock`\n        """
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
        """
        :param Name: Filters.\n        :type Name: str\n        :param Values: Filter values.\n        :type Values: list of str\n        """
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
        """
        :param SourcePath: Source path\n        :type SourcePath: str\n        :param DestinationPath: Destination path\n        :type DestinationPath: str\n        :param MountOptionParameter: Mounting configuration item parameter\n        :type MountOptionParameter: str\n        """
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
        """
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param ImageId: Image ID.\n        :type ImageId: str\n        :param LoginSettings: Instance login settings.\n        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`\n        """
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
        """
        :param InstanceCategory: Instance type name\n        :type InstanceCategory: str\n        :param InstanceFamilySet: List of instance families\n        :type InstanceFamilySet: list of str\n        """
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
        """
        :param SpotOptions: Options related to bidding\n        :type SpotOptions: :class:`tencentcloud.batch.v20170312.models.SpotMarketOptions`\n        :param MarketType: Market option type. Currently `spot` is the only supported value.\n        :type MarketType: str\n        """
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
        """
        :param Mem: Memory size in GB.\n        :type Mem: int\n        :param Cpu: Number of CPU cores.\n        :type Cpu: int\n        :param InstanceType: Instance model.\n        :type InstanceType: str\n        :param Zone: Availability zone.\n        :type Zone: str\n        :param InstanceFamily: Instance model family.\n        :type InstanceFamily: str\n        """
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
        """
        :param CPU: Number of CPU cores.\n        :type CPU: int\n        :param Memory: Memory size in GB.\n        :type Memory: int\n        :param InstanceCategories: Instance model category. Value range: "ALL", "GENERAL", "GENERAL_2", "GENERAL_3", "COMPUTE", "COMPUTE_2", and "COMPUTE_3". Default value: "ALL".\n        :type InstanceCategories: list of str\n        """
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
        """
        :param Zone: Availability zone.\n        :type Zone: str\n        :param InstanceType: Instance model.\n        :type InstanceType: str\n        :param InstanceChargeType: Instance billing plan. Valid values: <br><li>POSTPAID_BY_HOUR: pay after use. You are billed for your traffic by the hour.<br><li>`CDHPAID`: [`CDH`](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) billing plan. Applicable to `CDH` only, not the instances on the host.\n        :type InstanceChargeType: str\n        :param NetworkCard: ENI type. For example, 25 represents an ENI of 25 GB.\n        :type NetworkCard: int\n        :param Externals: Additional data.
Note: This field may return null, indicating that no valid value is found.\n        :type Externals: :class:`tencentcloud.batch.v20170312.models.Externals`\n        :param Cpu: Number of CPU cores of an instance model.\n        :type Cpu: int\n        :param Memory: Instance memory capacity; unit: `GB`.\n        :type Memory: int\n        :param InstanceFamily: Instance model family.\n        :type InstanceFamily: str\n        :param TypeName: Model name.\n        :type TypeName: str\n        :param LocalDiskTypeList: List of local disk specifications. If the parameter returns null, it means that local disks cannot be created.\n        :type LocalDiskTypeList: list of LocalDiskType\n        :param Status: Whether an instance model is available. Valid values: <br><li>SELL: available <br><li>SOLD_OUT: sold out\n        :type Status: str\n        :param Price: Price of an instance model.\n        :type Price: :class:`tencentcloud.batch.v20170312.models.ItemPrice`\n        :param SoldOutReason: Details of out-of-stock items
Note: this field may return null, indicating that no valid value is obtained.\n        :type SoldOutReason: str\n        :param InstanceBandwidth: Private network bandwidth, in Gbps.\n        :type InstanceBandwidth: float\n        :param InstancePps: The max packet sending and receiving capability (in 10k PPS).\n        :type InstancePps: int\n        :param StorageBlockAmount: Number of local storage blocks.\n        :type StorageBlockAmount: int\n        :param CpuType: CPU type.\n        :type CpuType: str\n        :param Gpu: Number of GPUs of the instance.\n        :type Gpu: int\n        :param Fpga: Number of FPGAs of the instance.\n        :type Fpga: int\n        :param Remark: Descriptive information of the instance.\n        :type Remark: str\n        """
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
        """
        :param InternetChargeType: Network connection billing plan. Valid value: <br><li>TRAFFIC_POSTPAID_BY_HOUR: pay after use. You are billed for your traffic, by the hour.\n        :type InternetChargeType: str\n        :param InternetMaxBandwidthOut: The maximum outbound bandwidth of the public network, in Mbps. The default value is 0 Mbps. The upper limit of bandwidth varies for different models. For more information, see [Purchase Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/12523?from_cn_redirect=1).\n        :type InternetMaxBandwidthOut: int\n        :param PublicIpAssigned: Whether to assign a public IP. Valid values: <br><li>TRUE: Assign a public IP <br><li>FALSE: Do not assign a public IP <br><br>If the public network bandwidth is greater than 0 Mbps, you can choose whether to assign a public IP; by default a public IP will be assigned. If the public network bandwidth is 0 Mbps, you will not be able to assign a public IP.\n        :type PublicIpAssigned: bool\n        :param BandwidthPackageId: Bandwidth package ID. To obatin the IDs, you can call [`DescribeBandwidthPackages`](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) and look for the `BandwidthPackageId` fields in the response.\n        :type BandwidthPackageId: str\n        """
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
        """
        :param UnitPrice: The original unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.\n        :type UnitPrice: float\n        :param ChargeUnit: Billing unit for pay-as-you-go mode. Valid values: <br><li>HOUR: billed on an hourly basis. It's used for hourly postpaid instances (`POSTPAID_BY_HOUR`). <br><li>GB: bill by traffic in GB. It's used for postpaid products that are billed by the hourly traffic (`TRAFFIC_POSTPAID_BY_HOUR`).
Note: this field may return null, indicating that no valid value is obtained.\n        :type ChargeUnit: str\n        :param OriginalPrice: The original price of a pay-in-advance instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.\n        :type OriginalPrice: float\n        :param DiscountPrice: Discount price of a prepaid instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.\n        :type DiscountPrice: float\n        :param Discount: Percentage of the original price. For example, if you enter "20.0", the discounted price will be 20% of the original price.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Discount: float\n        :param UnitPriceDiscount: The discounted unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.\n        :type UnitPriceDiscount: float\n        :param UnitPriceSecondStep: Original unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.\n        :type UnitPriceSecondStep: float\n        :param UnitPriceDiscountSecondStep: Discounted unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.\n        :type UnitPriceDiscountSecondStep: float\n        :param UnitPriceThirdStep: Original unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.\n        :type UnitPriceThirdStep: float\n        :param UnitPriceDiscountThirdStep: Discounted unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.\n        :type UnitPriceDiscountThirdStep: float\n        :param OriginalPriceThreeYear: Original 3-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type OriginalPriceThreeYear: float\n        :param DiscountPriceThreeYear: Discounted 3-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type DiscountPriceThreeYear: float\n        :param DiscountThreeYear: Discount for 3-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type DiscountThreeYear: float\n        :param OriginalPriceFiveYear: Original 5-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type OriginalPriceFiveYear: float\n        :param DiscountPriceFiveYear: Discounted 5-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type DiscountPriceFiveYear: float\n        :param DiscountFiveYear: Discount for 5-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type DiscountFiveYear: float\n        :param OriginalPriceOneYear: Original 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type OriginalPriceOneYear: float\n        :param DiscountPriceOneYear: Discounted 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type DiscountPriceOneYear: float\n        :param DiscountOneYear: Discount for 1-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.\n        :type DiscountOneYear: float\n        """
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
        


class Job(AbstractModel):
    """Instance

    """

    def __init__(self):
        """
        :param Tasks: Job information\n        :type Tasks: list of Task\n        :param JobName: Instance name\n        :type JobName: str\n        :param JobDescription: Instance description\n        :type JobDescription: str\n        :param Priority: Instance priority. Tasks (Task) and task instances (TaskInstance) inherit the priority of the instance\n        :type Priority: int\n        :param Dependences: Dependency information\n        :type Dependences: list of Dependence\n        :param Notifications: Notification information\n        :type Notifications: list of Notification\n        :param TaskExecutionDependOn: This is the dependency of the subsequent task on the previous task if there is a dependent relationship between them. Value range: PRE_TASK_SUCCEED, PRE_TASK_AT_LEAST_PARTLY_SUCCEED, PRE_TASK_FINISHED. Default value: PRE_TASK_SUCCEED.\n        :type TaskExecutionDependOn: str\n        :param StateIfCreateCvmFailed: Indicates which policy will be used in case that CVM instance creation fails. Value range: FAILED, RUNNABLE. FAILED indicates that the CVM instance creation failure will be processed as an execution failure, while RUNNABLE indicates that the failure will be processed as "keep waiting". Default value: FAILED. StateIfCreateCvmFailed is not valid for submitted jobs for which a compute environment is specified.\n        :type StateIfCreateCvmFailed: str\n        :param Tags: Tag list. By setting this parameter, you can bind tags to a job. Each job supports up to 10 tags.\n        :type Tags: list of Tag\n        """
        self.Tasks = None
        self.JobName = None
        self.JobDescription = None
        self.Priority = None
        self.Dependences = None
        self.Notifications = None
        self.TaskExecutionDependOn = None
        self.StateIfCreateCvmFailed = None
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.JobName = params.get("JobName")
        self.JobDescription = params.get("JobDescription")
        self.Priority = params.get("Priority")
        if params.get("Dependences") is not None:
            self.Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self.Dependences.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.TaskExecutionDependOn = params.get("TaskExecutionDependOn")
        self.StateIfCreateCvmFailed = params.get("StateIfCreateCvmFailed")
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
        


class JobView(AbstractModel):
    """Instance information

    """

    def __init__(self):
        """
        :param JobId: Instance ID\n        :type JobId: str\n        :param JobName: Instance name\n        :type JobName: str\n        :param JobState: Instance state\n        :type JobState: str\n        :param Priority: Instance priority\n        :type Priority: int\n        :param Placement: Location information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EndTime: str\n        :param TaskMetrics: Task statistical metrics\n        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`\n        :param Tags: Tag list bound to the job.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        """
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
        """
        :param Type: Type of a local disk.\n        :type Type: str\n        :param PartitionType: Attributes of a local disk.\n        :type PartitionType: str\n        :param MinSize: Minimum size of a local disk.\n        :type MinSize: int\n        :param MaxSize: Maximum size of a local disk.\n        :type MaxSize: int\n        :param Required: Whether a local disk is required during purchase. Valid values:<br><li>REQUIRED: required<br><li>OPTIONAL: optional\n        :type Required: str\n        """
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
        """
        :param Password: Login password of the instance. The password requirements vary among different operating systems: <br><li>For Linux instances, the password must be 8-16 characters long and contain at least one character from two of the following categories: [a-z, A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]. <br><li>For Windows instances, the password must be 12-16 characters long and contain at least one character from three of the following categories: [a-z], [A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. <br><br>If this parameter is not specified, a random password will be generated and sent to you via the Message Center.\n        :type Password: str\n        :param KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.\n        :type KeyIds: list of str\n        :param KeepImageLogin: Whether to keep the original settings of an image. You cannot specify this parameter and `Password` or `KeyIds.N` at the same time. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. Valid values: <br><li>TRUE: keep the login settings of the image <br><li>FALSE: do not keep the login settings of the image <br><br>Default value: FALSE.\n        :type KeepImageLogin: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param DesiredComputeNodeCount: Number of desired compute nodes\n        :type DesiredComputeNodeCount: int\n        :param EnvName: Compute environment name\n        :type EnvName: str\n        :param EnvDescription: Compute environment description\n        :type EnvDescription: str\n        :param EnvData: Compute environment attributes\n        :type EnvData: :class:`tencentcloud.batch.v20170312.models.ComputeEnvData`\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskTemplateRequest(AbstractModel):
    """ModifyTaskTemplate request structure.

    """

    def __init__(self):
        """
        :param TaskTemplateId: Job template ID\n        :type TaskTemplateId: str\n        :param TaskTemplateName: Job template name\n        :type TaskTemplateName: str\n        :param TaskTemplateDescription: Job template description\n        :type TaskTemplateDescription: str\n        :param TaskTemplateInfo: Job template information\n        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MountDataDisk(AbstractModel):
    """Data disk mounting option

    """

    def __init__(self):
        """
        :param LocalPath: Mounting point. For Linux, this parameter should be a valid path. For Windows, this parameter should be a system disk letter such as "H:\\"\n        :type LocalPath: str\n        :param FileSystemType: File system type. For Linux, "EXT3" and "EXT4" are supported and the default value is "EXT3". For Windows, only "NTFS" is supported\n        :type FileSystemType: str\n        """
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
        """
        :param EnvName: Compute environment name\n        :type EnvName: str\n        :param DesiredComputeNodeCount: Number of desired compute nodes\n        :type DesiredComputeNodeCount: int\n        :param EnvDescription: Compute environment description\n        :type EnvDescription: str\n        :param EnvType: Compute environment management type\n        :type EnvType: str\n        :param EnvData: Compute environment's specific parameters\n        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`\n        :param MountDataDisks: Data disk mounting option\n        :type MountDataDisks: list of MountDataDisk\n        :param Authentications: Authorization information\n        :type Authentications: list of Authentication\n        :param InputMappings: Input mapping information\n        :type InputMappings: list of InputMapping\n        :param AgentRunningMode: Agent running mode; applicable for Windows\n        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`\n        :param Notifications: Notification information\n        :type Notifications: :class:`tencentcloud.batch.v20170312.models.Notification`\n        :param ActionIfComputeNodeInactive: Inactive node processing policy. Default value: RECREATE, which means that instance resources will be re-created periodically for compute nodes where instance creation fails or is abnormally returned.\n        :type ActionIfComputeNodeInactive: str\n        :param ResourceMaxRetryCount: When the instances are failed to be created or returned because of exceptions, the related compute node will retry to create instances periodically. This parameter specifies the maximum retry attempts. The max value is 11 and the default value is 7.\n        :type ResourceMaxRetryCount: int\n        :param Tags: Tag list. By setting this parameter, you can bind tags to a compute environment. Each compute environment supports up to 10 tags.\n        :type Tags: list of Tag\n        """
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
        """
        :param TopicName: CMQ topic name which should be valid and associated with a subscription\n        :type TopicName: str\n        :param EventConfigs: Event configuration\n        :type EventConfigs: list of EventConfig\n        """
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
        """
        :param SourcePath: Source path\n        :type SourcePath: str\n        :param DestinationPath: Destination path\n        :type DestinationPath: str\n        """
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
        """
        :param Scene: Storage type. Only COS is supported\n        :type Scene: str\n        :param WorkerNum: Number of parallel workers\n        :type WorkerNum: int\n        :param WorkerPartSize: Size of a worker part, in MB.\n        :type WorkerPartSize: int\n        """
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
        """
        :param Zone: ID of the availability zone where the instance resides. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/15707?from_cn_redirect=1) API and obtain the ID in the returned `Zone` field.\n        :type Zone: str\n        :param ProjectId: ID of the project to which the instance belongs. To obtain the project IDs, you can call [DescribeProject](https://intl.cloud.tencent.com/document/api/378/4400?from_cn_redirect=1) and look for the `projectId` fields in the response. If this parameter is not specified, the default project will be used.\n        :type ProjectId: int\n        :param HostIds: ID list of CDHs from which the instance can be created. If you have purchased CDHs and specify this parameter, the instances you purchase will be randomly deployed on the CDHs.\n        :type HostIds: list of str\n        :param HostIps: Master host IP used to create the CVM\n        :type HostIps: list of str\n        :param HostId: The ID of the CDH to which the instance belongs, only used as an output parameter.\n        :type HostId: str\n        """
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
        """
        :param StdoutRedirectPath: Standard output redirection path\n        :type StdoutRedirectPath: str\n        :param StderrRedirectPath: Standard error redirection path\n        :type StderrRedirectPath: str\n        :param StdoutRedirectFileName: Standard output redirection file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}\n        :type StdoutRedirectFileName: str\n        :param StderrRedirectFileName: Standard error redirection file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}\n        :type StderrRedirectFileName: str\n        """
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
        """
        :param StdoutLocalPath: Standard output redirection local path\n        :type StdoutLocalPath: str\n        :param StderrLocalPath: Standard error redirection local path\n        :type StderrLocalPath: str\n        :param StdoutLocalFileName: Standard output redirection local file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}\n        :type StdoutLocalFileName: str\n        :param StderrLocalFileName: Standard error redirection local file name, which supports three placeholders: ${BATCH_JOB_ID}, ${BATCH_TASK_NAME}, and ${BATCH_TASK_INSTANCE_INDEX}\n        :type StderrLocalFileName: str\n        """
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
        """
        :param JobIds: List of instance IDs.\n        :type JobIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Monitor service.

    """

    def __init__(self):
        """
        :param Enabled: Whether to enable [Cloud Monitor](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Monitor <br><li>FALSE: do not enable Cloud Monitor <br><br>Default value: TRUE.\n        :type Enabled: bool\n        """
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
        """
        :param Enabled: Whether to enable [Cloud Security](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Security <br><li>FALSE: do not enable Cloud Security <br><br>Default value: TRUE.\n        :type Enabled: bool\n        """
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
        """
        :param MaxPrice: Bidding price\n        :type MaxPrice: str\n        :param SpotInstanceType: Bidding request type. Currently only "one-time" is supported.\n        :type SpotInstanceType: str\n        """
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
        """
        :param Type: Local HDD storage type. Value: LOCAL_PRO.
Note: This field may return null, indicating that no valid value is found.\n        :type Type: str\n        :param MinSize: Minimum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.\n        :type MinSize: int\n        :param MaxSize: Maximum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.\n        :type MaxSize: int\n        """
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
        


class SubmitJobRequest(AbstractModel):
    """SubmitJob request structure.

    """

    def __init__(self):
        """
        :param Placement: Location information of the submitted job. This parameter allows you to specify information such as the availability zone of the CVM instance with which the job is associated.\n        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`\n        :param Job: Job information\n        :type Job: :class:`tencentcloud.batch.v20170312.models.Job`\n        :param ClientToken: The string used to guarantee the idempotency of the request, which is generated by the user and must be unique for different requests. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.\n        :type ClientToken: str\n        """
        self.Placement = None
        self.Job = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitJobResponse(AbstractModel):
    """SubmitJob response structure.

    """

    def __init__(self):
        """
        :param JobId: When a job is submitted through this API, this parameter is returned and indicates the job ID. Returning the list of job IDs does not mean that the job is parsed/executed successfully. The job state can be queried using the DescribeJob API.\n        :type JobId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """Describes information on the block device where the operating system is stored, i.e., the system disk.

    """

    def __init__(self):
        """
        :param DiskType: System disk type. For more information on limits of system disk types, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values:<br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_SSD: SSD<br><li>CLOUD_PREMIUM: Premium Cloud Storage<br><br>The disk type currently in stock will be used by default. \n        :type DiskType: str\n        :param DiskId: System disk ID. System disks whose type is `LOCAL_BASIC` or `LOCAL_SSD` do not have an ID and do not support this parameter currently.\n        :type DiskId: str\n        :param DiskSize: System disk size; unit: GB; default value: 50 GB.\n        :type DiskSize: int\n        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
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
        """
        :param Key: Tag key.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Key: str\n        :param Value: Tag value.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Value: str\n        """
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
        """
        :param Application: Application information\n        :type Application: :class:`tencentcloud.batch.v20170312.models.Application`\n        :param TaskName: Job name, which should be unique within instance\n        :type TaskName: str\n        :param TaskInstanceNum: Number of running task instances\n        :type TaskInstanceNum: int\n        :param ComputeEnv: Compute environment information. One (and only one) parameter must be specified for ComputeEnv and EnvId.\n        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.AnonymousComputeEnv`\n        :param EnvId: Compute environment ID. One (and only one) parameter must be specified for ComputeEnv and EnvId.\n        :type EnvId: str\n        :param RedirectInfo: Redirection information\n        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`\n        :param RedirectLocalInfo: Local redirection information\n        :type RedirectLocalInfo: :class:`tencentcloud.batch.v20170312.models.RedirectLocalInfo`\n        :param InputMappings: Input mapping\n        :type InputMappings: list of InputMapping\n        :param OutputMappings: Output mapping\n        :type OutputMappings: list of OutputMapping\n        :param OutputMappingConfigs: Output mapping configuration\n        :type OutputMappingConfigs: list of OutputMappingConfig\n        :param EnvVars: Custom environment variable\n        :type EnvVars: list of EnvVar\n        :param Authentications: Authorization information\n        :type Authentications: list of Authentication\n        :param FailedAction: The processing method after the TaskInstance fails; Value range: TERMINATE (default), INTERRUPT, FAST_INTERRUPT.\n        :type FailedAction: str\n        :param MaxRetryCount: The maximum number of retries after the task fails. Default value: 0\n        :type MaxRetryCount: int\n        :param Timeout: Timeout period in seconds after the task starts. Defaults value: 86,400\n        :type Timeout: int\n        :param MaxConcurrentNum: The maximum number of concurrent tasks. There is no limit by default.\n        :type MaxConcurrentNum: int\n        :param RestartComputeNode: Restarts the compute node after the task is completed. This is suitable for specifying the compute environment for task execution.\n        :type RestartComputeNode: bool\n        :param ResourceMaxRetryCount: Maximum number of retry attempts after failing to create computing resources such as the CVM in the task launch process. Default value: 0.\n        :type ResourceMaxRetryCount: int\n        """
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
        """
        :param TaskInstanceIndex: Task instance\n        :type TaskInstanceIndex: int\n        :param StdoutLog: Standard output log (Base64-encoded)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type StdoutLog: str\n        :param StderrLog: Standard error log (Base64-encoded)
Note: This field may return null, indicating that no valid values can be obtained.\n        :type StderrLog: str\n        :param StdoutRedirectPath: Standard output redirection path
Note: This field may return null, indicating that no valid values can be obtained.\n        :type StdoutRedirectPath: str\n        :param StderrRedirectPath: Standard error redirection path
Note: This field may return null, indicating that no valid values can be obtained.\n        :type StderrRedirectPath: str\n        :param StdoutRedirectFileName: Standard output redirection file name
Note: This field may return null, indicating that no valid values can be obtained.\n        :type StdoutRedirectFileName: str\n        :param StderrRedirectFileName: Standard error redirection file name
Note: This field may return null, indicating that no valid values can be obtained.\n        :type StderrRedirectFileName: str\n        """
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
        """
        :param SubmittedCount: Submitted count\n        :type SubmittedCount: int\n        :param PendingCount: Pending count\n        :type PendingCount: int\n        :param RunnableCount: Runnable count\n        :type RunnableCount: int\n        :param StartingCount: Starting count\n        :type StartingCount: int\n        :param RunningCount: Running count\n        :type RunningCount: int\n        :param SucceedCount: Succeed count\n        :type SucceedCount: int\n        :param FailedInterruptedCount: FailedInterrupted count\n        :type FailedInterruptedCount: int\n        :param FailedCount: Failed count\n        :type FailedCount: int\n        """
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
        """
        :param TaskInstanceIndex: Task instance index\n        :type TaskInstanceIndex: int\n        :param TaskInstanceState: Task instance state\n        :type TaskInstanceState: str\n        :param ExitCode: Exit code after application execution is completed
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ExitCode: int\n        :param StateReason: Task instance state reason. If the task instance fails, the reason for the failure will be logged.\n        :type StateReason: str\n        :param ComputeNodeInstanceId: The InstanceId of the compute node (e.g., CVM instance) where the task instance is running. This field is empty if the task instance is not running or has already been completed and will change when the task instance is retried
Note: This field may return null, indicating that no valid values can be obtained.\n        :type ComputeNodeInstanceId: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param LaunchTime: Start time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type LaunchTime: str\n        :param RunningTime: Running start time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type RunningTime: str\n        :param EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EndTime: str\n        :param RedirectInfo: Redirection information\n        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`\n        :param StateDetailedReason: Task instance state reason details. If the task instance fails, the reason for the failure will be logged\n        :type StateDetailedReason: str\n        """
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
        """
        :param SubmittedCount: Submitted count\n        :type SubmittedCount: int\n        :param PendingCount: Pending count\n        :type PendingCount: int\n        :param RunnableCount: Runnable count\n        :type RunnableCount: int\n        :param StartingCount: Starting count\n        :type StartingCount: int\n        :param RunningCount: Running count\n        :type RunningCount: int\n        :param SucceedCount: Succeed count\n        :type SucceedCount: int\n        :param FailedInterruptedCount: FailedInterrupted count\n        :type FailedInterruptedCount: int\n        :param FailedCount: Failed count\n        :type FailedCount: int\n        """
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
        """
        :param TaskTemplateId: Task template ID\n        :type TaskTemplateId: str\n        :param TaskTemplateName: Task template name\n        :type TaskTemplateName: str\n        :param TaskTemplateDescription: Task template description\n        :type TaskTemplateDescription: str\n        :param TaskTemplateInfo: Task template information\n        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param Tags: Tag list bound to the task template.
Note: This field may return `null`, indicating that no valid value was found.\n        :type Tags: list of Tag\n        """
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
        """
        :param TaskName: Task name\n        :type TaskName: str\n        :param TaskState: Task state\n        :type TaskState: str\n        :param CreateTime: Create time\n        :type CreateTime: str\n        :param EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EndTime: str\n        """
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
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param ComputeNodeId: Compute node ID\n        :type ComputeNodeId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateComputeNodesRequest(AbstractModel):
    """TerminateComputeNodes request structure.

    """

    def __init__(self):
        """
        :param EnvId: Compute environment ID\n        :type EnvId: str\n        :param ComputeNodeIds: List of compute node IDs\n        :type ComputeNodeIds: list of str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateJobRequest(AbstractModel):
    """TerminateJob request structure.

    """

    def __init__(self):
        """
        :param JobId: Instance ID\n        :type JobId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTaskInstanceRequest(AbstractModel):
    """TerminateTaskInstance request structure.

    """

    def __init__(self):
        """
        :param JobId: Instance ID\n        :type JobId: str\n        :param TaskName: Task name\n        :type TaskName: str\n        :param TaskInstanceIndex: Task instance index\n        :type TaskInstanceIndex: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """Describes information on VPC, including subnets, IP addresses, etc.

    """

    def __init__(self):
        """
        :param VpcId: VPC ID in the format of `vpc-xxx`. To obtain valid VPC IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or call the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API and look for the `unVpcId` fields in the response. If you specify `DEFAULT` for both `VpcId` and `SubnetId` when creating an instance, the default VPC will be used.\n        :type VpcId: str\n        :param SubnetId: VPC subnet ID in the format `subnet-xxx`. To obtain valid subnet IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/subnet?rid=1) or call [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) and look for the `unSubnetId` fields in the response. If you specify `DEFAULT` for both `SubnetId` and `VpcId` when creating an instance, the default VPC will be used.\n        :type SubnetId: str\n        :param AsVpcGateway: Whether to use an instance as a public gateway. An instance can be used as a public gateway only when it has a public IP and resides in a VPC. Valid values: <br><li>TRUE: use the instance as a public gateway <br><li>FALSE: do not use the instance as a public gateway <br><br>Default value: FALSE.\n        :type AsVpcGateway: bool\n        :param PrivateIpAddresses: Array of VPC subnet IPs. You can use this parameter when creating instances or modifying VPC attributes of instances. Currently you can specify multiple IPs in one subnet only when creating multiple instances at the same time.\n        :type PrivateIpAddresses: list of str\n        :param Ipv6AddressCount: Number of IPv6 addresses randomly generated for the ENI.\n        :type Ipv6AddressCount: int\n        """
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
        