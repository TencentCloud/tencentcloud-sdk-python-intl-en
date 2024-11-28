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
    """Information of the creation/termination activity of a compute node

    """

    def __init__(self):
        r"""
        :param _ActivityId: Activity ID
        :type ActivityId: str
        :param _ComputeNodeId: Compute node ID
        :type ComputeNodeId: str
        :param _ComputeNodeActivityType: Activity type. Values: `CREATE_COMPUTE_NODE`, `TERMINATE_COMPUTE_NODE`
        :type ComputeNodeActivityType: str
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _Cause: Cause of the activity
        :type Cause: str
        :param _ActivityState: Activity state
        :type ActivityState: str
        :param _StateReason: Reason of going to this state
        :type StateReason: str
        :param _StartTime: Activity start time
        :type StartTime: str
        :param _EndTime: Activity end time
Note: This field may return `null`, indicating that no valid value was found.
        :type EndTime: str
        :param _InstanceId: CVM instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :type InstanceId: str
        """
        self._ActivityId = None
        self._ComputeNodeId = None
        self._ComputeNodeActivityType = None
        self._EnvId = None
        self._Cause = None
        self._ActivityState = None
        self._StateReason = None
        self._StartTime = None
        self._EndTime = None
        self._InstanceId = None

    @property
    def ActivityId(self):
        """Activity ID
        :rtype: str
        """
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ComputeNodeId(self):
        """Compute node ID
        :rtype: str
        """
        return self._ComputeNodeId

    @ComputeNodeId.setter
    def ComputeNodeId(self, ComputeNodeId):
        self._ComputeNodeId = ComputeNodeId

    @property
    def ComputeNodeActivityType(self):
        """Activity type. Values: `CREATE_COMPUTE_NODE`, `TERMINATE_COMPUTE_NODE`
        :rtype: str
        """
        return self._ComputeNodeActivityType

    @ComputeNodeActivityType.setter
    def ComputeNodeActivityType(self, ComputeNodeActivityType):
        self._ComputeNodeActivityType = ComputeNodeActivityType

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Cause(self):
        """Cause of the activity
        :rtype: str
        """
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def ActivityState(self):
        """Activity state
        :rtype: str
        """
        return self._ActivityState

    @ActivityState.setter
    def ActivityState(self, ActivityState):
        self._ActivityState = ActivityState

    @property
    def StateReason(self):
        """Reason of going to this state
        :rtype: str
        """
        return self._StateReason

    @StateReason.setter
    def StateReason(self, StateReason):
        self._StateReason = StateReason

    @property
    def StartTime(self):
        """Activity start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Activity end time
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def InstanceId(self):
        """CVM instance ID
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._ActivityId = params.get("ActivityId")
        self._ComputeNodeId = params.get("ComputeNodeId")
        self._ComputeNodeActivityType = params.get("ComputeNodeActivityType")
        self._EnvId = params.get("EnvId")
        self._Cause = params.get("Cause")
        self._ActivityState = params.get("ActivityState")
        self._StateReason = params.get("StateReason")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentRunningMode(AbstractModel):
    """Agent running mode

    """

    def __init__(self):
        r"""
        :param _Scene: Scenario type. Windows is supported
        :type Scene: str
        :param _User: The user that runs the Agent
        :type User: str
        :param _Session: The session that runs the Agent
        :type Session: str
        """
        self._Scene = None
        self._User = None
        self._Session = None

    @property
    def Scene(self):
        """Scenario type. Windows is supported
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def User(self):
        """The user that runs the Agent
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Session(self):
        """The session that runs the Agent
        :rtype: str
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._User = params.get("User")
        self._Session = params.get("Session")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnonymousComputeEnv(AbstractModel):
    """Compute environment

    """

    def __init__(self):
        r"""
        :param _EnvType: Compute environment management type
        :type EnvType: str
        :param _EnvData: Compute environment's parameters
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: Data disk mounting option
        :type MountDataDisks: list of MountDataDisk
        :param _AgentRunningMode: Agent running mode; applicable for Windows
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        """
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._AgentRunningMode = None

    @property
    def EnvType(self):
        """Compute environment management type
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        """Compute environment's parameters
        :rtype: :class:`tencentcloud.batch.v20170312.models.EnvData`
        """
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        """Data disk mounting option
        :rtype: list of MountDataDisk
        """
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def AgentRunningMode(self):
        """Agent running mode; applicable for Windows
        :rtype: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        """
        return self._AgentRunningMode

    @AgentRunningMode.setter
    def AgentRunningMode(self, AgentRunningMode):
        self._AgentRunningMode = AgentRunningMode


    def _deserialize(self, params):
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("AgentRunningMode") is not None:
            self._AgentRunningMode = AgentRunningMode()
            self._AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Application(AbstractModel):
    """Application information

    """

    def __init__(self):
        r"""
        :param _Command: Task execution command
        :type Command: str
        :param _DeliveryForm: Delivery form of the application. Values: `PACKAGE` (package stored in a remote location), `LOCAL` (local computer).
        :type DeliveryForm: str
        :param _PackagePath: Remote storage path of the application package
        :type PackagePath: str
        :param _Docker: Relevant configuration of the Docker used by the application. In case that the Docker configuration is used, "LOCAL" DeliveryForm means that the application software inside the Docker image is used directly and run in Docker mode; "PACKAGE" DeliveryForm means that the remote application package is run in Docker mode after being injected into the Docker image. To avoid compatibility issues with different versions of Docker, the Docker installation package and relevant dependencies are taken care of by BatchCompute. For custom images where Docker has already been installed, uninstall Docker first and then use the Docker feature.
        :type Docker: :class:`tencentcloud.batch.v20170312.models.Docker`
        """
        self._Command = None
        self._DeliveryForm = None
        self._PackagePath = None
        self._Docker = None

    @property
    def Command(self):
        """Task execution command
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def DeliveryForm(self):
        """Delivery form of the application. Values: `PACKAGE` (package stored in a remote location), `LOCAL` (local computer).
        :rtype: str
        """
        return self._DeliveryForm

    @DeliveryForm.setter
    def DeliveryForm(self, DeliveryForm):
        self._DeliveryForm = DeliveryForm

    @property
    def PackagePath(self):
        """Remote storage path of the application package
        :rtype: str
        """
        return self._PackagePath

    @PackagePath.setter
    def PackagePath(self, PackagePath):
        self._PackagePath = PackagePath

    @property
    def Docker(self):
        """Relevant configuration of the Docker used by the application. In case that the Docker configuration is used, "LOCAL" DeliveryForm means that the application software inside the Docker image is used directly and run in Docker mode; "PACKAGE" DeliveryForm means that the remote application package is run in Docker mode after being injected into the Docker image. To avoid compatibility issues with different versions of Docker, the Docker installation package and relevant dependencies are taken care of by BatchCompute. For custom images where Docker has already been installed, uninstall Docker first and then use the Docker feature.
        :rtype: :class:`tencentcloud.batch.v20170312.models.Docker`
        """
        return self._Docker

    @Docker.setter
    def Docker(self, Docker):
        self._Docker = Docker


    def _deserialize(self, params):
        self._Command = params.get("Command")
        self._DeliveryForm = params.get("DeliveryForm")
        self._PackagePath = params.get("PackagePath")
        if params.get("Docker") is not None:
            self._Docker = Docker()
            self._Docker._deserialize(params.get("Docker"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesRequest(AbstractModel):
    """AttachInstances request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _Instances: List of instances that added to the compute environment
        :type Instances: list of Instance
        """
        self._EnvId = None
        self._Instances = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Instances(self):
        """List of instances that added to the compute environment
        :rtype: list of Instance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachInstancesResponse(AbstractModel):
    """AttachInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Authentication(AbstractModel):
    """Authentication information

    """

    def __init__(self):
        r"""
        :param _Scene: Authentication scenario such as COS
        :type Scene: str
        :param _SecretId: SecretId
        :type SecretId: str
        :param _SecretKey: SecretKey
        :type SecretKey: str
        """
        self._Scene = None
        self._SecretId = None
        self._SecretKey = None

    @property
    def Scene(self):
        """Authentication scenario such as COS
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def SecretId(self):
        """SecretId
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        """SecretKey
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeEnvCreateInfo(AbstractModel):
    """Compute environment creation information

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _EnvName: Compute environment name
Note: This field may return `null`, indicating that no valid value was found.
        :type EnvName: str
        :param _EnvDescription: Compute environment description
Note: This field may return `null`, indicating that no valid value was found.
        :type EnvDescription: str
        :param _EnvType: Compute environment type. Only "MANAGED" type is supported
        :type EnvType: str
        :param _EnvData: Compute environment parameter
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: Data disk mounting option
Note: This field may return `null`, indicating that no valid value was found.
        :type MountDataDisks: list of MountDataDisk
        :param _InputMappings: Input mapping
Note: This field may return `null`, indicating that no valid value was found.
        :type InputMappings: list of InputMapping
        :param _Authentications: Authorization information
Note: This field may return `null`, indicating that no valid value was found.
        :type Authentications: list of Authentication
        :param _Notifications: Notification information
Note: This field may return `null`, indicating that no valid value was found.
        :type Notifications: list of Notification
        :param _DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param _Tags: Tag list of the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self._EnvId = None
        self._EnvName = None
        self._EnvDescription = None
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._InputMappings = None
        self._Authentications = None
        self._Notifications = None
        self._DesiredComputeNodeCount = None
        self._Tags = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        """Compute environment name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnvDescription(self):
        """Compute environment description
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvType(self):
        """Compute environment type. Only "MANAGED" type is supported
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        """Compute environment parameter
        :rtype: :class:`tencentcloud.batch.v20170312.models.EnvData`
        """
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        """Data disk mounting option
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of MountDataDisk
        """
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def InputMappings(self):
        """Input mapping
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of InputMapping
        """
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def Authentications(self):
        """Authorization information
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Authentication
        """
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def Notifications(self):
        """Notification information
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Notification
        """
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def DesiredComputeNodeCount(self):
        """Number of desired compute nodes
        :rtype: int
        """
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def Tags(self):
        """Tag list of the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        self._EnvDescription = params.get("EnvDescription")
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        if params.get("Notifications") is not None:
            self._Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self._Notifications.append(obj)
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
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
        


class ComputeEnvData(AbstractModel):
    """Compute environment attributes

    """

    def __init__(self):
        r"""
        :param _InstanceTypes: List of CVM instance types
        :type InstanceTypes: list of str
        """
        self._InstanceTypes = None

    @property
    def InstanceTypes(self):
        """List of CVM instance types
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes


    def _deserialize(self, params):
        self._InstanceTypes = params.get("InstanceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeEnvView(AbstractModel):
    """Compute environment information

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _EnvName: Compute environment name
        :type EnvName: str
        :param _Placement: Location information
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _ComputeNodeMetrics: Compute node statistical metrics
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param _EnvType: Compute environment type
        :type EnvType: str
        :param _DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param _ResourceType: Compute environment resource type. Values: `CVM`, `CPM` (Bare Metal)
        :type ResourceType: str
        :param _NextAction: Next action
        :type NextAction: str
        :param _AttachedComputeNodeCount: Number of compute nodes added to the compute environment
        :type AttachedComputeNodeCount: int
        :param _Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self._EnvId = None
        self._EnvName = None
        self._Placement = None
        self._CreateTime = None
        self._ComputeNodeMetrics = None
        self._EnvType = None
        self._DesiredComputeNodeCount = None
        self._ResourceType = None
        self._NextAction = None
        self._AttachedComputeNodeCount = None
        self._Tags = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        """Compute environment name
        :rtype: str
        """
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def Placement(self):
        """Location information
        :rtype: :class:`tencentcloud.batch.v20170312.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

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
    def ComputeNodeMetrics(self):
        """Compute node statistical metrics
        :rtype: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        """
        return self._ComputeNodeMetrics

    @ComputeNodeMetrics.setter
    def ComputeNodeMetrics(self, ComputeNodeMetrics):
        self._ComputeNodeMetrics = ComputeNodeMetrics

    @property
    def EnvType(self):
        """Compute environment type
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def DesiredComputeNodeCount(self):
        """Number of desired compute nodes
        :rtype: int
        """
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def ResourceType(self):
        """Compute environment resource type. Values: `CVM`, `CPM` (Bare Metal)
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def NextAction(self):
        """Next action
        :rtype: str
        """
        return self._NextAction

    @NextAction.setter
    def NextAction(self, NextAction):
        self._NextAction = NextAction

    @property
    def AttachedComputeNodeCount(self):
        """Number of compute nodes added to the compute environment
        :rtype: int
        """
        return self._AttachedComputeNodeCount

    @AttachedComputeNodeCount.setter
    def AttachedComputeNodeCount(self, AttachedComputeNodeCount):
        self._AttachedComputeNodeCount = AttachedComputeNodeCount

    @property
    def Tags(self):
        """Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeMetrics") is not None:
            self._ComputeNodeMetrics = ComputeNodeMetrics()
            self._ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self._EnvType = params.get("EnvType")
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._ResourceType = params.get("ResourceType")
        self._NextAction = params.get("NextAction")
        self._AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")
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
        


class ComputeNode(AbstractModel):
    """Compute node

    """

    def __init__(self):
        r"""
        :param _ComputeNodeId: Compute node ID
        :type ComputeNodeId: str
        :param _ComputeNodeInstanceId: Compute node instance ID. In a CVM scenario, this parameter is the CVM InstanceId
        :type ComputeNodeInstanceId: str
        :param _ComputeNodeState: Compute node state
        :type ComputeNodeState: str
        :param _Cpu: Number of CPU cores
        :type Cpu: int
        :param _Mem: Memory size in GiB
        :type Mem: int
        :param _ResourceCreatedTime: Resource creation time
        :type ResourceCreatedTime: str
        :param _TaskInstanceNumAvailable: Available capacity of the compute node when running TaskInstance. 0 means that the compute node is busy.
        :type TaskInstanceNumAvailable: int
        :param _AgentVersion: BatchCompute Agent version
        :type AgentVersion: str
        :param _PrivateIpAddresses: Private IP of the instance
        :type PrivateIpAddresses: list of str
        :param _PublicIpAddresses: Public IP of the instance
        :type PublicIpAddresses: list of str
        :param _ResourceType: Compute environment resource type. Values: `CVM`, `CPM` (Bare Metal)
        :type ResourceType: str
        :param _ResourceOrigin: Source of compute environment resources. <br>`BATCH_CREATED`: Instances created by BatchCompute.<br>
`USER_ATTACHED`: Instances added to the compute environment by the user.
        :type ResourceOrigin: str
        """
        self._ComputeNodeId = None
        self._ComputeNodeInstanceId = None
        self._ComputeNodeState = None
        self._Cpu = None
        self._Mem = None
        self._ResourceCreatedTime = None
        self._TaskInstanceNumAvailable = None
        self._AgentVersion = None
        self._PrivateIpAddresses = None
        self._PublicIpAddresses = None
        self._ResourceType = None
        self._ResourceOrigin = None

    @property
    def ComputeNodeId(self):
        """Compute node ID
        :rtype: str
        """
        return self._ComputeNodeId

    @ComputeNodeId.setter
    def ComputeNodeId(self, ComputeNodeId):
        self._ComputeNodeId = ComputeNodeId

    @property
    def ComputeNodeInstanceId(self):
        """Compute node instance ID. In a CVM scenario, this parameter is the CVM InstanceId
        :rtype: str
        """
        return self._ComputeNodeInstanceId

    @ComputeNodeInstanceId.setter
    def ComputeNodeInstanceId(self, ComputeNodeInstanceId):
        self._ComputeNodeInstanceId = ComputeNodeInstanceId

    @property
    def ComputeNodeState(self):
        """Compute node state
        :rtype: str
        """
        return self._ComputeNodeState

    @ComputeNodeState.setter
    def ComputeNodeState(self, ComputeNodeState):
        self._ComputeNodeState = ComputeNodeState

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
        """Memory size in GiB
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def ResourceCreatedTime(self):
        """Resource creation time
        :rtype: str
        """
        return self._ResourceCreatedTime

    @ResourceCreatedTime.setter
    def ResourceCreatedTime(self, ResourceCreatedTime):
        self._ResourceCreatedTime = ResourceCreatedTime

    @property
    def TaskInstanceNumAvailable(self):
        """Available capacity of the compute node when running TaskInstance. 0 means that the compute node is busy.
        :rtype: int
        """
        return self._TaskInstanceNumAvailable

    @TaskInstanceNumAvailable.setter
    def TaskInstanceNumAvailable(self, TaskInstanceNumAvailable):
        self._TaskInstanceNumAvailable = TaskInstanceNumAvailable

    @property
    def AgentVersion(self):
        """BatchCompute Agent version
        :rtype: str
        """
        return self._AgentVersion

    @AgentVersion.setter
    def AgentVersion(self, AgentVersion):
        self._AgentVersion = AgentVersion

    @property
    def PrivateIpAddresses(self):
        """Private IP of the instance
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def PublicIpAddresses(self):
        """Public IP of the instance
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def ResourceType(self):
        """Compute environment resource type. Values: `CVM`, `CPM` (Bare Metal)
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceOrigin(self):
        """Source of compute environment resources. <br>`BATCH_CREATED`: Instances created by BatchCompute.<br>
`USER_ATTACHED`: Instances added to the compute environment by the user.
        :rtype: str
        """
        return self._ResourceOrigin

    @ResourceOrigin.setter
    def ResourceOrigin(self, ResourceOrigin):
        self._ResourceOrigin = ResourceOrigin


    def _deserialize(self, params):
        self._ComputeNodeId = params.get("ComputeNodeId")
        self._ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self._ComputeNodeState = params.get("ComputeNodeState")
        self._Cpu = params.get("Cpu")
        self._Mem = params.get("Mem")
        self._ResourceCreatedTime = params.get("ResourceCreatedTime")
        self._TaskInstanceNumAvailable = params.get("TaskInstanceNumAvailable")
        self._AgentVersion = params.get("AgentVersion")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._ResourceType = params.get("ResourceType")
        self._ResourceOrigin = params.get("ResourceOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNodeMetrics(AbstractModel):
    """Compute node statistical metrics

    """

    def __init__(self):
        r"""
        :param _SubmittedCount: Number of compute nodes that have been submitted
        :type SubmittedCount: int
        :param _CreatingCount: Number of compute nodes that are being created
        :type CreatingCount: int
        :param _CreationFailedCount: Number of compute nodes that failed to be created
        :type CreationFailedCount: int
        :param _CreatedCount: Number of compute nodes that have been created
        :type CreatedCount: int
        :param _RunningCount: Number of running compute nodes
        :type RunningCount: int
        :param _DeletingCount: Number of compute nodes that are being terminated
        :type DeletingCount: int
        :param _AbnormalCount: Number of exceptional compute nodes
        :type AbnormalCount: int
        """
        self._SubmittedCount = None
        self._CreatingCount = None
        self._CreationFailedCount = None
        self._CreatedCount = None
        self._RunningCount = None
        self._DeletingCount = None
        self._AbnormalCount = None

    @property
    def SubmittedCount(self):
        """Number of compute nodes that have been submitted
        :rtype: int
        """
        return self._SubmittedCount

    @SubmittedCount.setter
    def SubmittedCount(self, SubmittedCount):
        self._SubmittedCount = SubmittedCount

    @property
    def CreatingCount(self):
        """Number of compute nodes that are being created
        :rtype: int
        """
        return self._CreatingCount

    @CreatingCount.setter
    def CreatingCount(self, CreatingCount):
        self._CreatingCount = CreatingCount

    @property
    def CreationFailedCount(self):
        """Number of compute nodes that failed to be created
        :rtype: int
        """
        return self._CreationFailedCount

    @CreationFailedCount.setter
    def CreationFailedCount(self, CreationFailedCount):
        self._CreationFailedCount = CreationFailedCount

    @property
    def CreatedCount(self):
        """Number of compute nodes that have been created
        :rtype: int
        """
        return self._CreatedCount

    @CreatedCount.setter
    def CreatedCount(self, CreatedCount):
        self._CreatedCount = CreatedCount

    @property
    def RunningCount(self):
        """Number of running compute nodes
        :rtype: int
        """
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def DeletingCount(self):
        """Number of compute nodes that are being terminated
        :rtype: int
        """
        return self._DeletingCount

    @DeletingCount.setter
    def DeletingCount(self, DeletingCount):
        self._DeletingCount = DeletingCount

    @property
    def AbnormalCount(self):
        """Number of exceptional compute nodes
        :rtype: int
        """
        return self._AbnormalCount

    @AbnormalCount.setter
    def AbnormalCount(self, AbnormalCount):
        self._AbnormalCount = AbnormalCount


    def _deserialize(self, params):
        self._SubmittedCount = params.get("SubmittedCount")
        self._CreatingCount = params.get("CreatingCount")
        self._CreationFailedCount = params.get("CreationFailedCount")
        self._CreatedCount = params.get("CreatedCount")
        self._RunningCount = params.get("RunningCount")
        self._DeletingCount = params.get("DeletingCount")
        self._AbnormalCount = params.get("AbnormalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateComputeEnvRequest(AbstractModel):
    """CreateComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param _ComputeEnv: Compute environment information
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.NamedComputeEnv`
        :param _Placement: Location information
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _ClientToken: The string used to guarantee the idempotency of the request, which is generated by the user and must be unique for different requests. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :type ClientToken: str
        """
        self._ComputeEnv = None
        self._Placement = None
        self._ClientToken = None

    @property
    def ComputeEnv(self):
        """Compute environment information
        :rtype: :class:`tencentcloud.batch.v20170312.models.NamedComputeEnv`
        """
        return self._ComputeEnv

    @ComputeEnv.setter
    def ComputeEnv(self, ComputeEnv):
        self._ComputeEnv = ComputeEnv

    @property
    def Placement(self):
        """Location information
        :rtype: :class:`tencentcloud.batch.v20170312.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ClientToken(self):
        """The string used to guarantee the idempotency of the request, which is generated by the user and must be unique for different requests. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed.
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        if params.get("ComputeEnv") is not None:
            self._ComputeEnv = NamedComputeEnv()
            self._ComputeEnv._deserialize(params.get("ComputeEnv"))
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateComputeEnvResponse(AbstractModel):
    """CreateComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvId = None
        self._RequestId = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

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
        self._EnvId = params.get("EnvId")
        self._RequestId = params.get("RequestId")


class CreateTaskTemplateRequest(AbstractModel):
    """CreateTaskTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TaskTemplateName: Task template name
        :type TaskTemplateName: str
        :param _TaskTemplateInfo: Task template content with the same parameter requirements as the task
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param _TaskTemplateDescription: Task template description
        :type TaskTemplateDescription: str
        :param _Tags: Specifies the tags you want to bind to a task template. Each task template supports up to 10 tags.
        :type Tags: list of Tag
        """
        self._TaskTemplateName = None
        self._TaskTemplateInfo = None
        self._TaskTemplateDescription = None
        self._Tags = None

    @property
    def TaskTemplateName(self):
        """Task template name
        :rtype: str
        """
        return self._TaskTemplateName

    @TaskTemplateName.setter
    def TaskTemplateName(self, TaskTemplateName):
        self._TaskTemplateName = TaskTemplateName

    @property
    def TaskTemplateInfo(self):
        """Task template content with the same parameter requirements as the task
        :rtype: :class:`tencentcloud.batch.v20170312.models.Task`
        """
        return self._TaskTemplateInfo

    @TaskTemplateInfo.setter
    def TaskTemplateInfo(self, TaskTemplateInfo):
        self._TaskTemplateInfo = TaskTemplateInfo

    @property
    def TaskTemplateDescription(self):
        """Task template description
        :rtype: str
        """
        return self._TaskTemplateDescription

    @TaskTemplateDescription.setter
    def TaskTemplateDescription(self, TaskTemplateDescription):
        self._TaskTemplateDescription = TaskTemplateDescription

    @property
    def Tags(self):
        """Specifies the tags you want to bind to a task template. Each task template supports up to 10 tags.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TaskTemplateName = params.get("TaskTemplateName")
        if params.get("TaskTemplateInfo") is not None:
            self._TaskTemplateInfo = Task()
            self._TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self._TaskTemplateDescription = params.get("TaskTemplateDescription")
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
        


class CreateTaskTemplateResponse(AbstractModel):
    """CreateTaskTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TaskTemplateId: Task template ID
        :type TaskTemplateId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskTemplateId = None
        self._RequestId = None

    @property
    def TaskTemplateId(self):
        """Task template ID
        :rtype: str
        """
        return self._TaskTemplateId

    @TaskTemplateId.setter
    def TaskTemplateId(self, TaskTemplateId):
        self._TaskTemplateId = TaskTemplateId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskTemplateId = params.get("TaskTemplateId")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Describes data disk information.

    """

    def __init__(self):
        r"""
        :param _DiskSize: Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.
        :type DiskSize: int
        :param _DiskType: Data disk type. For restrictions on data disk types, refer to [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values:<br/>
<li>
  LOCAL_BASIC: local disk.<br/>
  <li>
    LOCAL_SSD: local SSD.<br/>
    <li>
      LOCAL_NVME: local NVMe disk, which is closely related to InstanceType, and cannot be specified.<br/>
      <li>
        LOCAL_PRO: local HDD, which is closely related to InstanceType, and cannot be specified.<br/>
        <li>
          CLOUD_BASIC: basic cloud disk.<br/>
          <li>
            CLOUD_PREMIUM: premium cloud disk.<br/>
            <li>
              CLOUD_SSD: cloud SSD.<br />
              <li>
                CLOUD_HSSD: enhanced SSD.<br/>
                <li>
                  CLOUD_TSSD: tremendous SSD.<br/>
                  <li>
                    CLOUD_BSSD: balanced SSD.<br/><br/>Default value: LOCAL_BASIC.<br/><br/>This parameter is invalid for the `ResizeInstanceDisk` API.
                  </li>
                </li>
              </li>
            </li>
          </li>
        </li>
      </li>
    </li>
  </li>
</li>
        :type DiskType: str
        :param _DiskId: Data disk ID. Note that it’s not available for `LOCAL_BASIC` and `LOCAL_SSD` disks.
It is only used as a response parameter for APIs such as `DescribeInstances`, and cannot be used as a request parameter for APIs such as `RunInstances`.
        :type DiskId: str
        :param _DeleteWithInstance: Whether a data disk is terminated when the associated CVM instance is terminated. Valid values:
<li>TRUE: The data disk is terminated when the associated CVM instance is terminated. This only supports pay-as-you-go cloud disks that are billed by hour.</li>
<li>
  FALSE: The data disk is retained when the associated CVM instance is terminated.<br/>
  Default value: TRUE.<br/>
  This parameter is currently used only in the `RunInstances` API.
</li>
Note: This field may return null, indicating that no valid value is found.
        :type DeleteWithInstance: bool
        :param _SnapshotId: Data disk snapshot ID. The size of the selected data disk snapshot must be smaller than that of the data disk.
Note: This field may return null, indicating that no valid value is found.
        :type SnapshotId: str
        :param _Encrypt: Whether a data disk is encrypted. Valid values:
<li>true: encrypted.</li>
<li>
  false: not encrypted.<br/>
  Default value: false.<br/>
  This parameter is currently used only in the `RunInstances` API.
</li>
Note: This field may return null, indicating that no valid value is found.
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
        :param _BurstPerformance: Burst performance.

 <b>Note: This field is in beta test.</b>
Note: This field may return null, indicating that no valid value is found.
        :type BurstPerformance: bool
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
        self._BurstPerformance = None

    @property
    def DiskSize(self):
        """Data disk size (in GB). The minimum adjustment increment is 10 GB. The value range varies by data disk type. For more information on limits, see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). The default value is 0, indicating that no data disk is purchased. For more information, see the product documentation.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        """Data disk type. For restrictions on data disk types, refer to [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values:<br/>
<li>
  LOCAL_BASIC: local disk.<br/>
  <li>
    LOCAL_SSD: local SSD.<br/>
    <li>
      LOCAL_NVME: local NVMe disk, which is closely related to InstanceType, and cannot be specified.<br/>
      <li>
        LOCAL_PRO: local HDD, which is closely related to InstanceType, and cannot be specified.<br/>
        <li>
          CLOUD_BASIC: basic cloud disk.<br/>
          <li>
            CLOUD_PREMIUM: premium cloud disk.<br/>
            <li>
              CLOUD_SSD: cloud SSD.<br />
              <li>
                CLOUD_HSSD: enhanced SSD.<br/>
                <li>
                  CLOUD_TSSD: tremendous SSD.<br/>
                  <li>
                    CLOUD_BSSD: balanced SSD.<br/><br/>Default value: LOCAL_BASIC.<br/><br/>This parameter is invalid for the `ResizeInstanceDisk` API.
                  </li>
                </li>
              </li>
            </li>
          </li>
        </li>
      </li>
    </li>
  </li>
</li>
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        """Data disk ID. Note that it’s not available for `LOCAL_BASIC` and `LOCAL_SSD` disks.
It is only used as a response parameter for APIs such as `DescribeInstances`, and cannot be used as a request parameter for APIs such as `RunInstances`.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DeleteWithInstance(self):
        """Whether a data disk is terminated when the associated CVM instance is terminated. Valid values:
<li>TRUE: The data disk is terminated when the associated CVM instance is terminated. This only supports pay-as-you-go cloud disks that are billed by hour.</li>
<li>
  FALSE: The data disk is retained when the associated CVM instance is terminated.<br/>
  Default value: TRUE.<br/>
  This parameter is currently used only in the `RunInstances` API.
</li>
Note: This field may return null, indicating that no valid value is found.
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def SnapshotId(self):
        """Data disk snapshot ID. The size of the selected data disk snapshot must be smaller than that of the data disk.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def Encrypt(self):
        """Whether a data disk is encrypted. Valid values:
<li>true: encrypted.</li>
<li>
  false: not encrypted.<br/>
  Default value: false.<br/>
  This parameter is currently used only in the `RunInstances` API.
</li>
Note: This field may return null, indicating that no valid value is found.
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def KmsKeyId(self):
        """ID of the custom CMK in the format of UUID or “kms-abcd1234”. This parameter is used to encrypt cloud disks.

Currently, this parameter is only used in the `RunInstances` API.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def ThroughputPerformance(self):
        """Cloud disk performance, in MB/s
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def CdcId(self):
        """ID of the dedicated cluster to which the instance belongs.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId

    @property
    def BurstPerformance(self):
        """Burst performance.

 <b>Note: This field is in beta test.</b>
Note: This field may return null, indicating that no valid value is found.
        :rtype: bool
        """
        return self._BurstPerformance

    @BurstPerformance.setter
    def BurstPerformance(self, BurstPerformance):
        self._BurstPerformance = BurstPerformance


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
        self._BurstPerformance = params.get("BurstPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteComputeEnvRequest(AbstractModel):
    """DeleteComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteComputeEnvResponse(AbstractModel):
    """DeleteComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobResponse(AbstractModel):
    """DeleteJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTaskTemplatesRequest(AbstractModel):
    """DeleteTaskTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _TaskTemplateIds: This API is used to delete task template information.
        :type TaskTemplateIds: list of str
        """
        self._TaskTemplateIds = None

    @property
    def TaskTemplateIds(self):
        """This API is used to delete task template information.
        :rtype: list of str
        """
        return self._TaskTemplateIds

    @TaskTemplateIds.setter
    def TaskTemplateIds(self, TaskTemplateIds):
        self._TaskTemplateIds = TaskTemplateIds


    def _deserialize(self, params):
        self._TaskTemplateIds = params.get("TaskTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskTemplatesResponse(AbstractModel):
    """DeleteTaskTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Dependence(AbstractModel):
    """Dependency

    """

    def __init__(self):
        r"""
        :param _StartTask: Dependency start task name 
        :type StartTask: str
        :param _EndTask: Dependency end task name 
        :type EndTask: str
        """
        self._StartTask = None
        self._EndTask = None

    @property
    def StartTask(self):
        """Dependency start task name 
        :rtype: str
        """
        return self._StartTask

    @StartTask.setter
    def StartTask(self, StartTask):
        self._StartTask = StartTask

    @property
    def EndTask(self):
        """Dependency end task name 
        :rtype: str
        """
        return self._EndTask

    @EndTask.setter
    def EndTask(self, EndTask):
        self._EndTask = EndTask


    def _deserialize(self, params):
        self._StartTask = params.get("StartTask")
        self._EndTask = params.get("EndTask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableCvmInstanceTypesRequest(AbstractModel):
    """DescribeAvailableCvmInstanceTypes request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>
        :rtype: list of Filter
        """
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
        


class DescribeAvailableCvmInstanceTypesResponse(AbstractModel):
    """DescribeAvailableCvmInstanceTypes response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceTypeConfigSet: Array of model configurations
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceTypeConfigSet = None
        self._RequestId = None

    @property
    def InstanceTypeConfigSet(self):
        """Array of model configurations
        :rtype: list of InstanceTypeConfig
        """
        return self._InstanceTypeConfigSet

    @InstanceTypeConfigSet.setter
    def InstanceTypeConfigSet(self, InstanceTypeConfigSet):
        self._InstanceTypeConfigSet = InstanceTypeConfigSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self._InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self._InstanceTypeConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvActivitiesRequest(AbstractModel):
    """DescribeComputeEnvActivities request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number of returned items
        :type Limit: int
        :param _Filters: Filter
<li> `compute-node-id` - String - Optional - Filter by the compute node ID.</li>
        :type Filters: :class:`tencentcloud.batch.v20170312.models.Filter`
        """
        self._EnvId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

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
        """Maximum number of returned items
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Filter
<li> `compute-node-id` - String - Optional - Filter by the compute node ID.</li>
        :rtype: :class:`tencentcloud.batch.v20170312.models.Filter`
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = Filter()
            self._Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvActivitiesResponse(AbstractModel):
    """DescribeComputeEnvActivities response structure.

    """

    def __init__(self):
        r"""
        :param _ActivitySet: List of activities in the compute environment
        :type ActivitySet: list of Activity
        :param _TotalCount: Number of activities
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ActivitySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ActivitySet(self):
        """List of activities in the compute environment
        :rtype: list of Activity
        """
        return self._ActivitySet

    @ActivitySet.setter
    def ActivitySet(self, ActivitySet):
        self._ActivitySet = ActivitySet

    @property
    def TotalCount(self):
        """Number of activities
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self._ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self._ActivitySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfoRequest(AbstractModel):
    """DescribeComputeEnvCreateInfo request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvCreateInfoResponse(AbstractModel):
    """DescribeComputeEnvCreateInfo response structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _EnvName: Compute environment name
        :type EnvName: str
        :param _EnvDescription: Compute environment description
Note: This field may return `null`, indicating that no valid value was found.
        :type EnvDescription: str
        :param _EnvType: Compute environment type. Only `MANAGED` is supported
        :type EnvType: str
        :param _EnvData: Compute environment parameter
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: Data disk mounting option
        :type MountDataDisks: list of MountDataDisk
        :param _InputMappings: Input mapping
        :type InputMappings: list of InputMapping
        :param _Authentications: Authorization information
        :type Authentications: list of Authentication
        :param _Notifications: Notification information
        :type Notifications: list of Notification
        :param _DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param _Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvId = None
        self._EnvName = None
        self._EnvDescription = None
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._InputMappings = None
        self._Authentications = None
        self._Notifications = None
        self._DesiredComputeNodeCount = None
        self._Tags = None
        self._RequestId = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        """Compute environment name
        :rtype: str
        """
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnvDescription(self):
        """Compute environment description
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvType(self):
        """Compute environment type. Only `MANAGED` is supported
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        """Compute environment parameter
        :rtype: :class:`tencentcloud.batch.v20170312.models.EnvData`
        """
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        """Data disk mounting option
        :rtype: list of MountDataDisk
        """
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def InputMappings(self):
        """Input mapping
        :rtype: list of InputMapping
        """
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def Authentications(self):
        """Authorization information
        :rtype: list of Authentication
        """
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def Notifications(self):
        """Notification information
        :rtype: list of Notification
        """
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def DesiredComputeNodeCount(self):
        """Number of desired compute nodes
        :rtype: int
        """
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def Tags(self):
        """Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        self._EnvDescription = params.get("EnvDescription")
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        if params.get("Notifications") is not None:
            self._Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self._Notifications.append(obj)
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfosRequest(AbstractModel):
    """DescribeComputeEnvCreateInfos request structure.

    """

    def __init__(self):
        r"""
        :param _EnvIds: List of compute environment IDs, which cannot be specified together with the `Filters` parameter.
        :type EnvIds: list of str
        :param _Filters: Filter conditions
<li> `zone` - String - Optional - Filter by the availability zone.</li>
<li> `env-id` - String - Optional - Filter by the compute environment ID.</li>
<li> `env-name` - String - Optional - Filter by the compute environment name.</li>
It cannot be specified together with `EnvIds`.
        :type Filters: list of Filter
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number of returned items
        :type Limit: int
        """
        self._EnvIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EnvIds(self):
        """List of compute environment IDs, which cannot be specified together with the `Filters` parameter.
        :rtype: list of str
        """
        return self._EnvIds

    @EnvIds.setter
    def EnvIds(self, EnvIds):
        self._EnvIds = EnvIds

    @property
    def Filters(self):
        """Filter conditions
<li> `zone` - String - Optional - Filter by the availability zone.</li>
<li> `env-id` - String - Optional - Filter by the compute environment ID.</li>
<li> `env-name` - String - Optional - Filter by the compute environment name.</li>
It cannot be specified together with `EnvIds`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        """Maximum number of returned items
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EnvIds = params.get("EnvIds")
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
        


class DescribeComputeEnvCreateInfosResponse(AbstractModel):
    """DescribeComputeEnvCreateInfos response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of compute environments
        :type TotalCount: int
        :param _ComputeEnvCreateInfoSet: List of compute environment creation information
        :type ComputeEnvCreateInfoSet: list of ComputeEnvCreateInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ComputeEnvCreateInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of compute environments
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ComputeEnvCreateInfoSet(self):
        """List of compute environment creation information
        :rtype: list of ComputeEnvCreateInfo
        """
        return self._ComputeEnvCreateInfoSet

    @ComputeEnvCreateInfoSet.setter
    def ComputeEnvCreateInfoSet(self, ComputeEnvCreateInfoSet):
        self._ComputeEnvCreateInfoSet = ComputeEnvCreateInfoSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ComputeEnvCreateInfoSet") is not None:
            self._ComputeEnvCreateInfoSet = []
            for item in params.get("ComputeEnvCreateInfoSet"):
                obj = ComputeEnvCreateInfo()
                obj._deserialize(item)
                self._ComputeEnvCreateInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvRequest(AbstractModel):
    """DescribeComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        """
        self._EnvId = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComputeEnvResponse(AbstractModel):
    """DescribeComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _EnvName: Compute environment name
        :type EnvName: str
        :param _Placement: Location information
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _CreateTime: Compute environment creation time
        :type CreateTime: str
        :param _ComputeNodeSet: List of compute nodes
        :type ComputeNodeSet: list of ComputeNode
        :param _ComputeNodeMetrics: Compute node statistical metrics
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param _DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param _EnvType: Compute environment type
        :type EnvType: str
        :param _ResourceType: Compute environment resource type. Values: `CVM`, `CPM` (Bare Metal)
        :type ResourceType: str
        :param _NextAction: Next action
        :type NextAction: str
        :param _AttachedComputeNodeCount: Number of compute nodes added to the compute environment
        :type AttachedComputeNodeCount: int
        :param _Tags: Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvId = None
        self._EnvName = None
        self._Placement = None
        self._CreateTime = None
        self._ComputeNodeSet = None
        self._ComputeNodeMetrics = None
        self._DesiredComputeNodeCount = None
        self._EnvType = None
        self._ResourceType = None
        self._NextAction = None
        self._AttachedComputeNodeCount = None
        self._Tags = None
        self._RequestId = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvName(self):
        """Compute environment name
        :rtype: str
        """
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def Placement(self):
        """Location information
        :rtype: :class:`tencentcloud.batch.v20170312.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CreateTime(self):
        """Compute environment creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ComputeNodeSet(self):
        """List of compute nodes
        :rtype: list of ComputeNode
        """
        return self._ComputeNodeSet

    @ComputeNodeSet.setter
    def ComputeNodeSet(self, ComputeNodeSet):
        self._ComputeNodeSet = ComputeNodeSet

    @property
    def ComputeNodeMetrics(self):
        """Compute node statistical metrics
        :rtype: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        """
        return self._ComputeNodeMetrics

    @ComputeNodeMetrics.setter
    def ComputeNodeMetrics(self, ComputeNodeMetrics):
        self._ComputeNodeMetrics = ComputeNodeMetrics

    @property
    def DesiredComputeNodeCount(self):
        """Number of desired compute nodes
        :rtype: int
        """
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def EnvType(self):
        """Compute environment type
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def ResourceType(self):
        """Compute environment resource type. Values: `CVM`, `CPM` (Bare Metal)
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def NextAction(self):
        """Next action
        :rtype: str
        """
        return self._NextAction

    @NextAction.setter
    def NextAction(self, NextAction):
        self._NextAction = NextAction

    @property
    def AttachedComputeNodeCount(self):
        """Number of compute nodes added to the compute environment
        :rtype: int
        """
        return self._AttachedComputeNodeCount

    @AttachedComputeNodeCount.setter
    def AttachedComputeNodeCount(self, AttachedComputeNodeCount):
        self._AttachedComputeNodeCount = AttachedComputeNodeCount

    @property
    def Tags(self):
        """Tag list bound to the compute environment.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeSet") is not None:
            self._ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNode()
                obj._deserialize(item)
                self._ComputeNodeSet.append(obj)
        if params.get("ComputeNodeMetrics") is not None:
            self._ComputeNodeMetrics = ComputeNodeMetrics()
            self._ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._EnvType = params.get("EnvType")
        self._ResourceType = params.get("ResourceType")
        self._NextAction = params.get("NextAction")
        self._AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeComputeEnvsRequest(AbstractModel):
    """DescribeComputeEnvs request structure.

    """

    def __init__(self):
        r"""
        :param _EnvIds: List of compute environment IDs, which cannot be specified together with the `Filters` parameter.
        :type EnvIds: list of str
        :param _Filters: Filters
<li> `zone` - String - Optional - Availability zone.</li>
<li> `env-id` - String - Optional - Compute environment ID.</li>
<li> `env-name` - String - Optional - Compute environment name.</li>
<li> `resource-type` - String - Optional - Compute resource type (`CVM` or `CPM`).</li>
<li> `tag-key` - String - Optional - Tag key.</li>
</li>`tag-value` - String - Optional - Tag value.</li>
<li> `tag:tag-key` - String - Optional - Tag key-value pair. Replace `tag-key` with the actual tag key.</li>
It cannot be specified together with `EnvIds`.
        :type Filters: list of Filter
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number of returned items
        :type Limit: int
        """
        self._EnvIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EnvIds(self):
        """List of compute environment IDs, which cannot be specified together with the `Filters` parameter.
        :rtype: list of str
        """
        return self._EnvIds

    @EnvIds.setter
    def EnvIds(self, EnvIds):
        self._EnvIds = EnvIds

    @property
    def Filters(self):
        """Filters
<li> `zone` - String - Optional - Availability zone.</li>
<li> `env-id` - String - Optional - Compute environment ID.</li>
<li> `env-name` - String - Optional - Compute environment name.</li>
<li> `resource-type` - String - Optional - Compute resource type (`CVM` or `CPM`).</li>
<li> `tag-key` - String - Optional - Tag key.</li>
</li>`tag-value` - String - Optional - Tag value.</li>
<li> `tag:tag-key` - String - Optional - Tag key-value pair. Replace `tag-key` with the actual tag key.</li>
It cannot be specified together with `EnvIds`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        """Maximum number of returned items
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EnvIds = params.get("EnvIds")
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
        


class DescribeComputeEnvsResponse(AbstractModel):
    """DescribeComputeEnvs response structure.

    """

    def __init__(self):
        r"""
        :param _ComputeEnvSet: List of compute environments
        :type ComputeEnvSet: list of ComputeEnvView
        :param _TotalCount: Number of compute environments
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ComputeEnvSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ComputeEnvSet(self):
        """List of compute environments
        :rtype: list of ComputeEnvView
        """
        return self._ComputeEnvSet

    @ComputeEnvSet.setter
    def ComputeEnvSet(self, ComputeEnvSet):
        self._ComputeEnvSet = ComputeEnvSet

    @property
    def TotalCount(self):
        """Number of compute environments
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ComputeEnvSet") is not None:
            self._ComputeEnvSet = []
            for item in params.get("ComputeEnvSet"):
                obj = ComputeEnvView()
                obj._deserialize(item)
                self._ComputeEnvSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCvmZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>
<li> instance-type - String - Required: No - (Filter) Filter by model.</li>
<li> instance-charge-type - String - Required: No - (Filter) Filter by instance billing method. ( POSTPAID_BY_HOUR: pay-as-you-go | SPOTPAID: bidding.)  </li>
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """Filter.
<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>
<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>
<li> instance-type - String - Required: No - (Filter) Filter by model.</li>
<li> instance-charge-type - String - Required: No - (Filter) Filter by instance billing method. ( POSTPAID_BY_HOUR: pay-as-you-go | SPOTPAID: bidding.)  </li>
        :rtype: list of Filter
        """
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
        


class DescribeCvmZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceTypeQuotaSet: List of model configurations in the availability zone.
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceTypeQuotaSet = None
        self._RequestId = None

    @property
    def InstanceTypeQuotaSet(self):
        """List of model configurations in the availability zone.
        :rtype: list of InstanceTypeQuotaItem
        """
        return self._InstanceTypeQuotaSet

    @InstanceTypeQuotaSet.setter
    def InstanceTypeQuotaSet(self, InstanceTypeQuotaSet):
        self._InstanceTypeQuotaSet = InstanceTypeQuotaSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribeInstanceCategoriesRequest(AbstractModel):
    """DescribeInstanceCategories request structure.

    """


class DescribeInstanceCategoriesResponse(AbstractModel):
    """DescribeInstanceCategories response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceCategorySet: List of CVM instance categories
        :type InstanceCategorySet: list of InstanceCategoryItem
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceCategorySet = None
        self._RequestId = None

    @property
    def InstanceCategorySet(self):
        """List of CVM instance categories
        :rtype: list of InstanceCategoryItem
        """
        return self._InstanceCategorySet

    @InstanceCategorySet.setter
    def InstanceCategorySet(self, InstanceCategorySet):
        self._InstanceCategorySet = InstanceCategorySet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceCategorySet") is not None:
            self._InstanceCategorySet = []
            for item in params.get("InstanceCategorySet"):
                obj = InstanceCategoryItem()
                obj._deserialize(item)
                self._InstanceCategorySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobResponse(AbstractModel):
    """DescribeJob response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        :param _JobName: Job name
        :type JobName: str
        :param _Zone: Availability zone information
        :type Zone: str
        :param _Priority: Job priority
        :type Priority: int
        :param _JobState: Job state
        :type JobState: str
        :param _CreateTime: Creation Date
        :type CreateTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _TaskSet: Task view information
        :type TaskSet: list of TaskView
        :param _DependenceSet: Information of the dependency among tasks
        :type DependenceSet: list of Dependence
        :param _TaskMetrics: Task statistical metrics
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        :param _TaskInstanceMetrics: Task instance statistical metrics
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param _StateReason: Job failure reason
        :type StateReason: str
        :param _Tags: List of tags bound with the job.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _NextAction: Next action
Note: This field may return `null`, indicating that no valid value was found.
        :type NextAction: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._Zone = None
        self._Priority = None
        self._JobState = None
        self._CreateTime = None
        self._EndTime = None
        self._TaskSet = None
        self._DependenceSet = None
        self._TaskMetrics = None
        self._TaskInstanceMetrics = None
        self._StateReason = None
        self._Tags = None
        self._NextAction = None
        self._RequestId = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Job name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def Zone(self):
        """Availability zone information
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Priority(self):
        """Job priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def JobState(self):
        """Job state
        :rtype: str
        """
        return self._JobState

    @JobState.setter
    def JobState(self, JobState):
        self._JobState = JobState

    @property
    def CreateTime(self):
        """Creation Date
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def TaskSet(self):
        """Task view information
        :rtype: list of TaskView
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

    @property
    def DependenceSet(self):
        """Information of the dependency among tasks
        :rtype: list of Dependence
        """
        return self._DependenceSet

    @DependenceSet.setter
    def DependenceSet(self, DependenceSet):
        self._DependenceSet = DependenceSet

    @property
    def TaskMetrics(self):
        """Task statistical metrics
        :rtype: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        """
        return self._TaskMetrics

    @TaskMetrics.setter
    def TaskMetrics(self, TaskMetrics):
        self._TaskMetrics = TaskMetrics

    @property
    def TaskInstanceMetrics(self):
        """Task instance statistical metrics
        :rtype: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        """
        return self._TaskInstanceMetrics

    @TaskInstanceMetrics.setter
    def TaskInstanceMetrics(self, TaskInstanceMetrics):
        self._TaskInstanceMetrics = TaskInstanceMetrics

    @property
    def StateReason(self):
        """Job failure reason
        :rtype: str
        """
        return self._StateReason

    @StateReason.setter
    def StateReason(self, StateReason):
        self._StateReason = StateReason

    @property
    def Tags(self):
        """List of tags bound with the job.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextAction(self):
        """Next action
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._NextAction

    @NextAction.setter
    def NextAction(self, NextAction):
        self._NextAction = NextAction

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._Zone = params.get("Zone")
        self._Priority = params.get("Priority")
        self._JobState = params.get("JobState")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskView()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        if params.get("DependenceSet") is not None:
            self._DependenceSet = []
            for item in params.get("DependenceSet"):
                obj = Dependence()
                obj._deserialize(item)
                self._DependenceSet.append(obj)
        if params.get("TaskMetrics") is not None:
            self._TaskMetrics = TaskMetrics()
            self._TaskMetrics._deserialize(params.get("TaskMetrics"))
        if params.get("TaskInstanceMetrics") is not None:
            self._TaskInstanceMetrics = TaskInstanceMetrics()
            self._TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self._StateReason = params.get("StateReason")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NextAction = params.get("NextAction")
        self._RequestId = params.get("RequestId")


class DescribeJobSubmitInfoRequest(AbstractModel):
    """DescribeJobSubmitInfo request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeJobSubmitInfoResponse(AbstractModel):
    """DescribeJobSubmitInfo response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        :param _JobName: Job name
        :type JobName: str
        :param _JobDescription: Job description
        :type JobDescription: str
        :param _Priority: Job priority. Tasks (Task) and task instances (TaskInstance) inherit the job priority
        :type Priority: int
        :param _Tasks: Information of tasks in the job
        :type Tasks: list of Task
        :param _Dependences: Dependency information
        :type Dependences: list of Dependence
        :param _Tags: List of tags bound with the job.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._JobName = None
        self._JobDescription = None
        self._Priority = None
        self._Tasks = None
        self._Dependences = None
        self._Tags = None
        self._RequestId = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Job name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobDescription(self):
        """Job description
        :rtype: str
        """
        return self._JobDescription

    @JobDescription.setter
    def JobDescription(self, JobDescription):
        self._JobDescription = JobDescription

    @property
    def Priority(self):
        """Job priority. Tasks (Task) and task instances (TaskInstance) inherit the job priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Tasks(self):
        """Information of tasks in the job
        :rtype: list of Task
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def Dependences(self):
        """Dependency information
        :rtype: list of Dependence
        """
        return self._Dependences

    @Dependences.setter
    def Dependences(self, Dependences):
        self._Dependences = Dependences

    @property
    def Tags(self):
        """List of tags bound with the job.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobDescription = params.get("JobDescription")
        self._Priority = params.get("Priority")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self._Tasks.append(obj)
        if params.get("Dependences") is not None:
            self._Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self._Dependences.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs request structure.

    """

    def __init__(self):
        r"""
        :param _JobIds: List of job IDs. It cannot be specified together with `Filters`.
        :type JobIds: list of str
        :param _Filters: Filter
<li> `job-id` - String - Optional - Filter by the job ID.</li>
<li> `job-name` - String - Optional - Filter by the job name.</li>
<li> `job-state` - String - Optional - Filter by the job state.</li>
<li> `zone` - String - Optional - Filter by the availability zone.</li>
<li> `tag-key` - String - Optional - Tag key.</li>
<li> `tag-value` - String - Optional - Tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by the tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with `JobIds`.
        :type Filters: list of Filter
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number of returned items
        :type Limit: int
        """
        self._JobIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def JobIds(self):
        """List of job IDs. It cannot be specified together with `Filters`.
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds

    @property
    def Filters(self):
        """Filter
<li> `job-id` - String - Optional - Filter by the job ID.</li>
<li> `job-name` - String - Optional - Filter by the job name.</li>
<li> `job-state` - String - Optional - Filter by the job state.</li>
<li> `zone` - String - Optional - Filter by the availability zone.</li>
<li> `tag-key` - String - Optional - Tag key.</li>
<li> `tag-value` - String - Optional - Tag value.</li>
<li> `tag:tag-key` - String - Optional - Filter by the tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with `JobIds`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        """Maximum number of returned items
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
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
        


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs response structure.

    """

    def __init__(self):
        r"""
        :param _JobSet: List of jobs
        :type JobSet: list of JobView
        :param _TotalCount: Number of matched jobs
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def JobSet(self):
        """List of jobs
        :rtype: list of JobView
        """
        return self._JobSet

    @JobSet.setter
    def JobSet(self, JobSet):
        self._JobSet = JobSet

    @property
    def TotalCount(self):
        """Number of matched jobs
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self._JobSet = []
            for item in params.get("JobSet"):
                obj = JobView()
                obj._deserialize(item)
                self._JobSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTaskLogsRequest(AbstractModel):
    """DescribeTaskLogs request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        :param _TaskName: Task name
        :type TaskName: str
        :param _TaskInstanceIndexes: Set of task instances
        :type TaskInstanceIndexes: list of int non-negative
        :param _Offset: The start point of query
        :type Offset: int
        :param _Limit: Maximum number of task instances returned
        :type Limit: int
        """
        self._JobId = None
        self._TaskName = None
        self._TaskInstanceIndexes = None
        self._Offset = None
        self._Limit = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        """Task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskInstanceIndexes(self):
        """Set of task instances
        :rtype: list of int non-negative
        """
        return self._TaskInstanceIndexes

    @TaskInstanceIndexes.setter
    def TaskInstanceIndexes(self, TaskInstanceIndexes):
        self._TaskInstanceIndexes = TaskInstanceIndexes

    @property
    def Offset(self):
        """The start point of query
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of task instances returned
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._TaskInstanceIndexes = params.get("TaskInstanceIndexes")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskLogsResponse(AbstractModel):
    """DescribeTaskLogs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of task instances
        :type TotalCount: int
        :param _TaskInstanceLogSet: Set of task instance log details
        :type TaskInstanceLogSet: list of TaskInstanceLog
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TaskInstanceLogSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of task instances
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TaskInstanceLogSet(self):
        """Set of task instance log details
        :rtype: list of TaskInstanceLog
        """
        return self._TaskInstanceLogSet

    @TaskInstanceLogSet.setter
    def TaskInstanceLogSet(self, TaskInstanceLogSet):
        self._TaskInstanceLogSet = TaskInstanceLogSet

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TaskInstanceLogSet") is not None:
            self._TaskInstanceLogSet = []
            for item in params.get("TaskInstanceLogSet"):
                obj = TaskInstanceLog()
                obj._deserialize(item)
                self._TaskInstanceLogSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        :param _TaskName: Task name
        :type TaskName: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Number of returned results. Default value: 100. Maximum value: 1,000.
        :type Limit: int
        :param _Filters: Filter as detailed below:
<li> `task-instance-type` - String - Optional - Filter by the task instance state. (`SUBMITTED`, `PENDING`, `RUNNABLE`, `STARTING`, `RUNNING`, `SUCCEED`, `FAILED`, `FAILED_INTERRUPTED`).</li>
        :type Filters: list of Filter
        """
        self._JobId = None
        self._TaskName = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        """Task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

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
        """Number of returned results. Default value: 100. Maximum value: 1,000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Filter as detailed below:
<li> `task-instance-type` - String - Optional - Filter by the task instance state. (`SUBMITTED`, `PENDING`, `RUNNABLE`, `STARTING`, `RUNNING`, `SUCCEED`, `FAILED`, `FAILED_INTERRUPTED`).</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
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
        


class DescribeTaskResponse(AbstractModel):
    """DescribeTask response structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        :param _TaskName: Task name
        :type TaskName: str
        :param _TaskState: Task status
        :type TaskState: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _EndTime: End time
        :type EndTime: str
        :param _TaskInstanceTotalCount: Total number of task instances
        :type TaskInstanceTotalCount: int
        :param _TaskInstanceSet: Task instance information
        :type TaskInstanceSet: list of TaskInstanceView
        :param _TaskInstanceMetrics: Task instance statistical metrics
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._JobId = None
        self._TaskName = None
        self._TaskState = None
        self._CreateTime = None
        self._EndTime = None
        self._TaskInstanceTotalCount = None
        self._TaskInstanceSet = None
        self._TaskInstanceMetrics = None
        self._RequestId = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        """Task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskState(self):
        """Task status
        :rtype: str
        """
        return self._TaskState

    @TaskState.setter
    def TaskState(self, TaskState):
        self._TaskState = TaskState

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
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskInstanceTotalCount(self):
        """Total number of task instances
        :rtype: int
        """
        return self._TaskInstanceTotalCount

    @TaskInstanceTotalCount.setter
    def TaskInstanceTotalCount(self, TaskInstanceTotalCount):
        self._TaskInstanceTotalCount = TaskInstanceTotalCount

    @property
    def TaskInstanceSet(self):
        """Task instance information
        :rtype: list of TaskInstanceView
        """
        return self._TaskInstanceSet

    @TaskInstanceSet.setter
    def TaskInstanceSet(self, TaskInstanceSet):
        self._TaskInstanceSet = TaskInstanceSet

    @property
    def TaskInstanceMetrics(self):
        """Task instance statistical metrics
        :rtype: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        """
        return self._TaskInstanceMetrics

    @TaskInstanceMetrics.setter
    def TaskInstanceMetrics(self, TaskInstanceMetrics):
        self._TaskInstanceMetrics = TaskInstanceMetrics

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._TaskState = params.get("TaskState")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        self._TaskInstanceTotalCount = params.get("TaskInstanceTotalCount")
        if params.get("TaskInstanceSet") is not None:
            self._TaskInstanceSet = []
            for item in params.get("TaskInstanceSet"):
                obj = TaskInstanceView()
                obj._deserialize(item)
                self._TaskInstanceSet.append(obj)
        if params.get("TaskInstanceMetrics") is not None:
            self._TaskInstanceMetrics = TaskInstanceMetrics()
            self._TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self._RequestId = params.get("RequestId")


class DescribeTaskTemplatesRequest(AbstractModel):
    """DescribeTaskTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _TaskTemplateIds: List of task template IDs. It cannot be specified together with `Filters`.
        :type TaskTemplateIds: list of str
        :param _Filters: Filter
<li> `task-template-name` - String - Optional - Task template name.</li>
<li> `tag-key` - String - Optional - Tag key.</li>
<li> `tag-value` - String - Optional - Tag value.</li>
<li> `tag:tag-key` - String - Optional - Tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with `TaskTemplateIds`.
        :type Filters: list of Filter
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: Maximum number of returned items
        :type Limit: int
        """
        self._TaskTemplateIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def TaskTemplateIds(self):
        """List of task template IDs. It cannot be specified together with `Filters`.
        :rtype: list of str
        """
        return self._TaskTemplateIds

    @TaskTemplateIds.setter
    def TaskTemplateIds(self, TaskTemplateIds):
        self._TaskTemplateIds = TaskTemplateIds

    @property
    def Filters(self):
        """Filter
<li> `task-template-name` - String - Optional - Task template name.</li>
<li> `tag-key` - String - Optional - Tag key.</li>
<li> `tag-value` - String - Optional - Tag value.</li>
<li> `tag:tag-key` - String - Optional - Tag key-value pair. The tag-key should be replaced by a specified tag key.</li>
It cannot be specified together with `TaskTemplateIds`.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        """Maximum number of returned items
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TaskTemplateIds = params.get("TaskTemplateIds")
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
        


class DescribeTaskTemplatesResponse(AbstractModel):
    """DescribeTaskTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TaskTemplateSet: List of task templates
        :type TaskTemplateSet: list of TaskTemplateView
        :param _TotalCount: Number of task templates
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskTemplateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TaskTemplateSet(self):
        """List of task templates
        :rtype: list of TaskTemplateView
        """
        return self._TaskTemplateSet

    @TaskTemplateSet.setter
    def TaskTemplateSet(self, TaskTemplateSet):
        self._TaskTemplateSet = TaskTemplateSet

    @property
    def TotalCount(self):
        """Number of task templates
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskTemplateSet") is not None:
            self._TaskTemplateSet = []
            for item in params.get("TaskTemplateSet"):
                obj = TaskTemplateView()
                obj._deserialize(item)
                self._TaskTemplateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _InstanceIds: List of instance IDs
        :type InstanceIds: list of str
        """
        self._EnvId = None
        self._InstanceIds = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def InstanceIds(self):
        """List of instance IDs
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachInstancesResponse(AbstractModel):
    """DetachInstances response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Docker(AbstractModel):
    """Docker container information

    """

    def __init__(self):
        r"""
        :param _User: Docker Hub username or Tencent Registry username
        :type User: str
        :param _Password: Docker Hub password or Tencent Registry password
        :type Password: str
        :param _Image: For Docker Hub, enter "[user/repo]:[tag]"; for Tencent Registry, enter "ccr.ccs.tencentyun.com/[namespace/repo]:[tag]"
        :type Image: str
        :param _Server: For Docker Hub, this can be left blank, but please ensure public network access is present. For Tencent Registry, the server address is "ccr.ccs.tencentyun.com"
        :type Server: str
        :param _MaxRetryCount: Maximum retry attempts to load docket images. Range: 0 - 10. Default: `0`
        :type MaxRetryCount: int
        :param _DelayOnRetry: Docker image loading timeout period (in seconds). Range: 1 - 360
        :type DelayOnRetry: int
        :param _DockerRunOption: Docker command execution parameter
Note: This field may return `null`, indicating that no valid value was found.
        :type DockerRunOption: str
        """
        self._User = None
        self._Password = None
        self._Image = None
        self._Server = None
        self._MaxRetryCount = None
        self._DelayOnRetry = None
        self._DockerRunOption = None

    @property
    def User(self):
        """Docker Hub username or Tencent Registry username
        :rtype: str
        """
        return self._User

    @User.setter
    def User(self, User):
        self._User = User

    @property
    def Password(self):
        """Docker Hub password or Tencent Registry password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Image(self):
        """For Docker Hub, enter "[user/repo]:[tag]"; for Tencent Registry, enter "ccr.ccs.tencentyun.com/[namespace/repo]:[tag]"
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Server(self):
        """For Docker Hub, this can be left blank, but please ensure public network access is present. For Tencent Registry, the server address is "ccr.ccs.tencentyun.com"
        :rtype: str
        """
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def MaxRetryCount(self):
        """Maximum retry attempts to load docket images. Range: 0 - 10. Default: `0`
        :rtype: int
        """
        return self._MaxRetryCount

    @MaxRetryCount.setter
    def MaxRetryCount(self, MaxRetryCount):
        self._MaxRetryCount = MaxRetryCount

    @property
    def DelayOnRetry(self):
        """Docker image loading timeout period (in seconds). Range: 1 - 360
        :rtype: int
        """
        return self._DelayOnRetry

    @DelayOnRetry.setter
    def DelayOnRetry(self, DelayOnRetry):
        self._DelayOnRetry = DelayOnRetry

    @property
    def DockerRunOption(self):
        """Docker command execution parameter
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._DockerRunOption

    @DockerRunOption.setter
    def DockerRunOption(self, DockerRunOption):
        self._DockerRunOption = DockerRunOption


    def _deserialize(self, params):
        self._User = params.get("User")
        self._Password = params.get("Password")
        self._Image = params.get("Image")
        self._Server = params.get("Server")
        self._MaxRetryCount = params.get("MaxRetryCount")
        self._DelayOnRetry = params.get("DelayOnRetry")
        self._DockerRunOption = params.get("DockerRunOption")
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
        :type SecurityService: :class:`tencentcloud.batch.v20170312.models.RunSecurityServiceEnabled`
        :param _MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.batch.v20170312.models.RunMonitorServiceEnabled`
        :param _AutomationService: Whether to enable the TAT service. If this parameter is not specified, the TAT service is enabled for public images and disabled for other images by default.
        :type AutomationService: :class:`tencentcloud.batch.v20170312.models.RunAutomationServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._AutomationService = None

    @property
    def SecurityService(self):
        """Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.
        :rtype: :class:`tencentcloud.batch.v20170312.models.RunSecurityServiceEnabled`
        """
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        """Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :rtype: :class:`tencentcloud.batch.v20170312.models.RunMonitorServiceEnabled`
        """
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def AutomationService(self):
        """Whether to enable the TAT service. If this parameter is not specified, the TAT service is enabled for public images and disabled for other images by default.
        :rtype: :class:`tencentcloud.batch.v20170312.models.RunAutomationServiceEnabled`
        """
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
        


class EnvData(AbstractModel):
    """Compute environment information

    """

    def __init__(self):
        r"""
        :param _InstanceType: CVM instance type. It cannot be specified together with `InstanceTypes` or `InstanceTypeOptions`.
        :type InstanceType: str
        :param _ImageId: CVM image ID
        :type ImageId: str
        :param _SystemDisk: System disk configuration of the instance
        :type SystemDisk: :class:`tencentcloud.batch.v20170312.models.SystemDisk`
        :param _DataDisks: Data disk configuration of the instance
        :type DataDisks: list of DataDisk
        :param _VirtualPrivateCloud: Information of the VPC configuration. It cannot be specified together with `Zones` and `VirtualPrivateClouds`.
        :type VirtualPrivateCloud: :class:`tencentcloud.batch.v20170312.models.VirtualPrivateCloud`
        :param _InternetAccessible: Public network bandwidth configuration
        :type InternetAccessible: :class:`tencentcloud.batch.v20170312.models.InternetAccessible`
        :param _InstanceName: CVM instance display name
        :type InstanceName: str
        :param _LoginSettings: Instance login settings
        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        :param _SecurityGroupIds: Security groups associated with the instance
        :type SecurityGroupIds: list of str
        :param _EnhancedService: Whether to activate CWPP agent and Cloud Monitor. CWPP agent and Cloud Monitor are activated by default.
        :type EnhancedService: :class:`tencentcloud.batch.v20170312.models.EnhancedService`
        :param _InstanceChargeType: CVM instance billing method <br><li>`POSTPAID_BY_HOUR` (default): Hourly-billed pay-as-you-go <br><li>`SPOTPAID`: Spot instance <br>
        :type InstanceChargeType: str
        :param _InstanceMarketOptions: Market-related options for instances, such as parameters related to spot instances.
        :type InstanceMarketOptions: :class:`tencentcloud.batch.v20170312.models.InstanceMarketOptionsRequest`
        :param _InstanceTypes: Types of CVM instances to create (up to 10). The system creates compute nodes of types specified in this list from top to down till the creation is successful. It cannot be specified together with `InstanceType` or `InstanceTypeOptions`. 
        :type InstanceTypes: list of str
        :param _InstanceTypeOptions: CVM instance model configuration. It cannot be specified together with `InstanceType` or `InstanceTypes`.
        :type InstanceTypeOptions: :class:`tencentcloud.batch.v20170312.models.InstanceTypeOptions`
        :param _Zones: List of availability zones. You can create CVM cross AZs in the same region. It cannot be specified together with `VirtualPrivateCloud` or `VirtualPrivateClouds`.
        :type Zones: list of str
        :param _VirtualPrivateClouds: List of VPCs (creation of CVM instances across VPCs is supported). It cannot be specified together with `VirtualPrivateCloud` or `Zones`.
        :type VirtualPrivateClouds: list of VirtualPrivateCloud
        """
        self._InstanceType = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._VirtualPrivateCloud = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._EnhancedService = None
        self._InstanceChargeType = None
        self._InstanceMarketOptions = None
        self._InstanceTypes = None
        self._InstanceTypeOptions = None
        self._Zones = None
        self._VirtualPrivateClouds = None

    @property
    def InstanceType(self):
        """CVM instance type. It cannot be specified together with `InstanceTypes` or `InstanceTypeOptions`.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ImageId(self):
        """CVM image ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def SystemDisk(self):
        """System disk configuration of the instance
        :rtype: :class:`tencentcloud.batch.v20170312.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """Data disk configuration of the instance
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def VirtualPrivateCloud(self):
        """Information of the VPC configuration. It cannot be specified together with `Zones` and `VirtualPrivateClouds`.
        :rtype: :class:`tencentcloud.batch.v20170312.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def InternetAccessible(self):
        """Public network bandwidth configuration
        :rtype: :class:`tencentcloud.batch.v20170312.models.InternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        """CVM instance display name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def LoginSettings(self):
        """Instance login settings
        :rtype: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        """Security groups associated with the instance
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def EnhancedService(self):
        """Whether to activate CWPP agent and Cloud Monitor. CWPP agent and Cloud Monitor are activated by default.
        :rtype: :class:`tencentcloud.batch.v20170312.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def InstanceChargeType(self):
        """CVM instance billing method <br><li>`POSTPAID_BY_HOUR` (default): Hourly-billed pay-as-you-go <br><li>`SPOTPAID`: Spot instance <br>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceMarketOptions(self):
        """Market-related options for instances, such as parameters related to spot instances.
        :rtype: :class:`tencentcloud.batch.v20170312.models.InstanceMarketOptionsRequest`
        """
        return self._InstanceMarketOptions

    @InstanceMarketOptions.setter
    def InstanceMarketOptions(self, InstanceMarketOptions):
        self._InstanceMarketOptions = InstanceMarketOptions

    @property
    def InstanceTypes(self):
        """Types of CVM instances to create (up to 10). The system creates compute nodes of types specified in this list from top to down till the creation is successful. It cannot be specified together with `InstanceType` or `InstanceTypeOptions`. 
        :rtype: list of str
        """
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def InstanceTypeOptions(self):
        """CVM instance model configuration. It cannot be specified together with `InstanceType` or `InstanceTypes`.
        :rtype: :class:`tencentcloud.batch.v20170312.models.InstanceTypeOptions`
        """
        return self._InstanceTypeOptions

    @InstanceTypeOptions.setter
    def InstanceTypeOptions(self, InstanceTypeOptions):
        self._InstanceTypeOptions = InstanceTypeOptions

    @property
    def Zones(self):
        """List of availability zones. You can create CVM cross AZs in the same region. It cannot be specified together with `VirtualPrivateCloud` or `VirtualPrivateClouds`.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def VirtualPrivateClouds(self):
        """List of VPCs (creation of CVM instances across VPCs is supported). It cannot be specified together with `VirtualPrivateCloud` or `Zones`.
        :rtype: list of VirtualPrivateCloud
        """
        return self._VirtualPrivateClouds

    @VirtualPrivateClouds.setter
    def VirtualPrivateClouds(self, VirtualPrivateClouds):
        self._VirtualPrivateClouds = VirtualPrivateClouds


    def _deserialize(self, params):
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
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self._InstanceMarketOptions = InstanceMarketOptionsRequest()
            self._InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self._InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTypeOptions") is not None:
            self._InstanceTypeOptions = InstanceTypeOptions()
            self._InstanceTypeOptions._deserialize(params.get("InstanceTypeOptions"))
        self._Zones = params.get("Zones")
        if params.get("VirtualPrivateClouds") is not None:
            self._VirtualPrivateClouds = []
            for item in params.get("VirtualPrivateClouds"):
                obj = VirtualPrivateCloud()
                obj._deserialize(item)
                self._VirtualPrivateClouds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    """Environment variable

    """

    def __init__(self):
        r"""
        :param _Name: Environment variable name
        :type Name: str
        :param _Value: Environment variable value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Environment variable name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Environment variable value
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
        


class EventConfig(AbstractModel):
    """Event configuration

    """

    def __init__(self):
        r"""
        :param _EventName: Event type. Value range: <br/><li>`JOB_RUNNING`: The job is running, applicable to `SubmitJob`. </li><li>`JOB_SUCCEED`: The job succeeded, applicable to `SubmitJob`. </li><li>`JOB_FAILED`: The job failed, applicable to `SubmitJob`. </li><li>`JOB_FAILED_INTERRUPTED`: The job failed and the instance is retained, applicable to `SubmitJob`. </li><li>`TASK_RUNNING`: The task is running, applicable to `SubmitJob`. </li><li>`TASK_SUCCEED`: The task succeeded, applicable to `SubmitJob`. </li><li>`TASK_FAILED`: The task failed, applicable to `SubmitJob`. </li><li>`TASK_FAILED_INTERRUPTED`: The task failed and the instance is retained, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_RUNNING`: The task instance is running, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_SUCCEED`: The task instance succeeded, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_FAILED`: The task instance failed, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_FAILED_INTERRUPTED`: The task instance failed and the instance is retained, applicable to `SubmitJob`. </li><li>`COMPUTE_ENV_CREATED`: the compute environment has been created, applicable to "CreateComputeEnv". </li><li>`COMPUTE_ENV_DELETED`: The compute environment has been deleted, applicable to `CreateComputeEnv`. </li><li>`COMPUTE_NODE_CREATED`: The compute node has been created, applicable to `CreateComputeEnv` and `SubmitJob`. </li><li>`COMPUTE_NODE_CREATION_FAILED`: The compute node creation failed, applicable to `CreateComputeEnv` and `SubmitJob`. </li><li>`COMPUTE_NODE_RUNNING`: The compute node is running, applicable to `CreateComputeEnv` and `SubmitJob`. </li><li>`COMPUTE_NODE_ABNORMAL`: The compute node is exceptional, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>`COMPUTE_NODE_DELETING`: The compute node has been deleted, applicable to `CreateComputeEnv` and `SubmitJob`. </li>
        :type EventName: str
        :param _EventVars: Custom key-value pair
        :type EventVars: list of EventVar
        """
        self._EventName = None
        self._EventVars = None

    @property
    def EventName(self):
        """Event type. Value range: <br/><li>`JOB_RUNNING`: The job is running, applicable to `SubmitJob`. </li><li>`JOB_SUCCEED`: The job succeeded, applicable to `SubmitJob`. </li><li>`JOB_FAILED`: The job failed, applicable to `SubmitJob`. </li><li>`JOB_FAILED_INTERRUPTED`: The job failed and the instance is retained, applicable to `SubmitJob`. </li><li>`TASK_RUNNING`: The task is running, applicable to `SubmitJob`. </li><li>`TASK_SUCCEED`: The task succeeded, applicable to `SubmitJob`. </li><li>`TASK_FAILED`: The task failed, applicable to `SubmitJob`. </li><li>`TASK_FAILED_INTERRUPTED`: The task failed and the instance is retained, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_RUNNING`: The task instance is running, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_SUCCEED`: The task instance succeeded, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_FAILED`: The task instance failed, applicable to `SubmitJob`. </li><li>`TASK_INSTANCE_FAILED_INTERRUPTED`: The task instance failed and the instance is retained, applicable to `SubmitJob`. </li><li>`COMPUTE_ENV_CREATED`: the compute environment has been created, applicable to "CreateComputeEnv". </li><li>`COMPUTE_ENV_DELETED`: The compute environment has been deleted, applicable to `CreateComputeEnv`. </li><li>`COMPUTE_NODE_CREATED`: The compute node has been created, applicable to `CreateComputeEnv` and `SubmitJob`. </li><li>`COMPUTE_NODE_CREATION_FAILED`: The compute node creation failed, applicable to `CreateComputeEnv` and `SubmitJob`. </li><li>`COMPUTE_NODE_RUNNING`: The compute node is running, applicable to `CreateComputeEnv` and `SubmitJob`. </li><li>`COMPUTE_NODE_ABNORMAL`: The compute node is exceptional, applicable to "CreateComputeEnv" and "SubmitJob". </li><li>`COMPUTE_NODE_DELETING`: The compute node has been deleted, applicable to `CreateComputeEnv` and `SubmitJob`. </li>
        :rtype: str
        """
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def EventVars(self):
        """Custom key-value pair
        :rtype: list of EventVar
        """
        return self._EventVars

    @EventVars.setter
    def EventVars(self, EventVars):
        self._EventVars = EventVars


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        if params.get("EventVars") is not None:
            self._EventVars = []
            for item in params.get("EventVars"):
                obj = EventVar()
                obj._deserialize(item)
                self._EventVars.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventVar(AbstractModel):
    """Custom key-value pair

    """

    def __init__(self):
        r"""
        :param _Name: Custom key
        :type Name: str
        :param _Value: Custom value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Custom key
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Custom value
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
        :type StorageBlockAttr: :class:`tencentcloud.batch.v20170312.models.StorageBlock`
        """
        self._ReleaseAddress = None
        self._UnsupportNetworks = None
        self._StorageBlockAttr = None

    @property
    def ReleaseAddress(self):
        """Release address
Note: This field may return null, indicating that no valid value is found.
        :rtype: bool
        """
        return self._ReleaseAddress

    @ReleaseAddress.setter
    def ReleaseAddress(self, ReleaseAddress):
        self._ReleaseAddress = ReleaseAddress

    @property
    def UnsupportNetworks(self):
        """Not supported network. Value: <br><li>BASIC: classic network<br><li>VPC1.0: VPC1.0
Note: This field may return null, indicating that no valid value was found.
        :rtype: list of str
        """
        return self._UnsupportNetworks

    @UnsupportNetworks.setter
    def UnsupportNetworks(self, UnsupportNetworks):
        self._UnsupportNetworks = UnsupportNetworks

    @property
    def StorageBlockAttr(self):
        """Attributes of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :rtype: :class:`tencentcloud.batch.v20170312.models.StorageBlock`
        """
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
        """Filters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filter values.
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
        


class InputMapping(AbstractModel):
    """Input mapping

    """

    def __init__(self):
        r"""
        :param _SourcePath: Source path
        :type SourcePath: str
        :param _DestinationPath: Destination path
        :type DestinationPath: str
        :param _MountOptionParameter: Mounting configuration item parameter
        :type MountOptionParameter: str
        """
        self._SourcePath = None
        self._DestinationPath = None
        self._MountOptionParameter = None

    @property
    def SourcePath(self):
        """Source path
        :rtype: str
        """
        return self._SourcePath

    @SourcePath.setter
    def SourcePath(self, SourcePath):
        self._SourcePath = SourcePath

    @property
    def DestinationPath(self):
        """Destination path
        :rtype: str
        """
        return self._DestinationPath

    @DestinationPath.setter
    def DestinationPath(self, DestinationPath):
        self._DestinationPath = DestinationPath

    @property
    def MountOptionParameter(self):
        """Mounting configuration item parameter
        :rtype: str
        """
        return self._MountOptionParameter

    @MountOptionParameter.setter
    def MountOptionParameter(self, MountOptionParameter):
        self._MountOptionParameter = MountOptionParameter


    def _deserialize(self, params):
        self._SourcePath = params.get("SourcePath")
        self._DestinationPath = params.get("DestinationPath")
        self._MountOptionParameter = params.get("MountOptionParameter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """Describes information of an instance

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _ImageId: Image ID
        :type ImageId: str
        :param _LoginSettings: Instance login settings.
        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        """
        self._InstanceId = None
        self._ImageId = None
        self._LoginSettings = None

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
    def ImageId(self):
        """Image ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def LoginSettings(self):
        """Instance login settings.
        :rtype: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ImageId = params.get("ImageId")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceCategoryItem(AbstractModel):
    """List of instance categories

    """

    def __init__(self):
        r"""
        :param _InstanceCategory: Instance type name
        :type InstanceCategory: str
        :param _InstanceFamilySet: List of instance families
        :type InstanceFamilySet: list of str
        """
        self._InstanceCategory = None
        self._InstanceFamilySet = None

    @property
    def InstanceCategory(self):
        """Instance type name
        :rtype: str
        """
        return self._InstanceCategory

    @InstanceCategory.setter
    def InstanceCategory(self, InstanceCategory):
        self._InstanceCategory = InstanceCategory

    @property
    def InstanceFamilySet(self):
        """List of instance families
        :rtype: list of str
        """
        return self._InstanceFamilySet

    @InstanceFamilySet.setter
    def InstanceFamilySet(self, InstanceFamilySet):
        self._InstanceFamilySet = InstanceFamilySet


    def _deserialize(self, params):
        self._InstanceCategory = params.get("InstanceCategory")
        self._InstanceFamilySet = params.get("InstanceFamilySet")
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
        :type SpotOptions: :class:`tencentcloud.batch.v20170312.models.SpotMarketOptions`
        :param _MarketType: Market type. Valid value: `spot`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MarketType: str
        """
        self._SpotOptions = None
        self._MarketType = None

    @property
    def SpotOptions(self):
        """Spot-related options
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.batch.v20170312.models.SpotMarketOptions`
        """
        return self._SpotOptions

    @SpotOptions.setter
    def SpotOptions(self, SpotOptions):
        self._SpotOptions = SpotOptions

    @property
    def MarketType(self):
        """Market type. Valid value: `spot`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        


class InstanceTypeConfig(AbstractModel):
    """Information of InstanceTypeConfig available to BatchCompute

    """

    def __init__(self):
        r"""
        :param _Mem: Memory size in GB.
        :type Mem: int
        :param _Cpu: Number of CPU cores.
        :type Cpu: int
        :param _InstanceType: Instance model.
        :type InstanceType: str
        :param _Zone: Availability zone.
        :type Zone: str
        :param _InstanceFamily: Instance model family.
        :type InstanceFamily: str
        """
        self._Mem = None
        self._Cpu = None
        self._InstanceType = None
        self._Zone = None
        self._InstanceFamily = None

    @property
    def Mem(self):
        """Memory size in GB.
        :rtype: int
        """
        return self._Mem

    @Mem.setter
    def Mem(self, Mem):
        self._Mem = Mem

    @property
    def Cpu(self):
        """Number of CPU cores.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def InstanceType(self):
        """Instance model.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Zone(self):
        """Availability zone.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceFamily(self):
        """Instance model family.
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily


    def _deserialize(self, params):
        self._Mem = params.get("Mem")
        self._Cpu = params.get("Cpu")
        self._InstanceType = params.get("InstanceType")
        self._Zone = params.get("Zone")
        self._InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeOptions(AbstractModel):
    """Instance model configuration.

    """

    def __init__(self):
        r"""
        :param _CPU: Number of CPU cores
        :type CPU: int
        :param _Memory: Memory size in GB.
        :type Memory: int
        :param _InstanceCategories: Instance model category. Values: `ALL` (default), `GENERAL`, `GENERAL_2`, `GENERAL_3`, `COMPUTE`, `COMPUTE_2`, and `COMPUTE_3`. 
        :type InstanceCategories: list of str
        """
        self._CPU = None
        self._Memory = None
        self._InstanceCategories = None

    @property
    def CPU(self):
        """Number of CPU cores
        :rtype: int
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        """Memory size in GB.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceCategories(self):
        """Instance model category. Values: `ALL` (default), `GENERAL`, `GENERAL_2`, `GENERAL_3`, `COMPUTE`, `COMPUTE_2`, and `COMPUTE_3`. 
        :rtype: list of str
        """
        return self._InstanceCategories

    @InstanceCategories.setter
    def InstanceCategories(self, InstanceCategories):
        self._InstanceCategories = InstanceCategories


    def _deserialize(self, params):
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._InstanceCategories = params.get("InstanceCategories")
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
        :type Externals: :class:`tencentcloud.batch.v20170312.models.Externals`
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
        :type Price: :class:`tencentcloud.batch.v20170312.models.ItemPrice`
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
        """Availability zone.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        """Instance model.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeType(self):
        """Instance billing plan. Valid values: <br><li>POSTPAID_BY_HOUR: pay after use. You are billed for your traffic by the hour.<br><li>`CDHPAID`: [`CDH`](https://intl.cloud.tencent.com/document/product/416?from_cn_redirect=1) billing plan. Applicable to `CDH` only, not the instances on the host.
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def NetworkCard(self):
        """ENI type. For example, 25 represents an ENI of 25 GB.
        :rtype: int
        """
        return self._NetworkCard

    @NetworkCard.setter
    def NetworkCard(self, NetworkCard):
        self._NetworkCard = NetworkCard

    @property
    def Externals(self):
        """Additional data.
Note: This field may return null, indicating that no valid value is found.
        :rtype: :class:`tencentcloud.batch.v20170312.models.Externals`
        """
        return self._Externals

    @Externals.setter
    def Externals(self, Externals):
        self._Externals = Externals

    @property
    def Cpu(self):
        """Number of CPU cores of an instance model.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """Instance memory capacity; unit: `GB`.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InstanceFamily(self):
        """Instance model family.
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def TypeName(self):
        """Model name.
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def LocalDiskTypeList(self):
        """List of local disk specifications. If the parameter returns null, it means that local disks cannot be created.
        :rtype: list of LocalDiskType
        """
        return self._LocalDiskTypeList

    @LocalDiskTypeList.setter
    def LocalDiskTypeList(self, LocalDiskTypeList):
        self._LocalDiskTypeList = LocalDiskTypeList

    @property
    def Status(self):
        """Whether an instance model is available. Valid values: <br><li>SELL: available <br><li>SOLD_OUT: sold out
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Price(self):
        """Price of an instance model.
        :rtype: :class:`tencentcloud.batch.v20170312.models.ItemPrice`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def SoldOutReason(self):
        """Details of out-of-stock items
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._SoldOutReason

    @SoldOutReason.setter
    def SoldOutReason(self, SoldOutReason):
        self._SoldOutReason = SoldOutReason

    @property
    def InstanceBandwidth(self):
        """Private network bandwidth, in Gbps.
        :rtype: float
        """
        return self._InstanceBandwidth

    @InstanceBandwidth.setter
    def InstanceBandwidth(self, InstanceBandwidth):
        self._InstanceBandwidth = InstanceBandwidth

    @property
    def InstancePps(self):
        """The max packet sending and receiving capability (in 10k PPS).
        :rtype: int
        """
        return self._InstancePps

    @InstancePps.setter
    def InstancePps(self, InstancePps):
        self._InstancePps = InstancePps

    @property
    def StorageBlockAmount(self):
        """Number of local storage blocks.
        :rtype: int
        """
        return self._StorageBlockAmount

    @StorageBlockAmount.setter
    def StorageBlockAmount(self, StorageBlockAmount):
        self._StorageBlockAmount = StorageBlockAmount

    @property
    def CpuType(self):
        """CPU type.
        :rtype: str
        """
        return self._CpuType

    @CpuType.setter
    def CpuType(self, CpuType):
        self._CpuType = CpuType

    @property
    def Gpu(self):
        """Number of GPUs of the instance.
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Fpga(self):
        """Number of FPGAs of the instance.
        :rtype: int
        """
        return self._Fpga

    @Fpga.setter
    def Fpga(self, Fpga):
        self._Fpga = Fpga

    @property
    def Remark(self):
        """Descriptive information of the instance.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def GpuCount(self):
        """
        :rtype: float
        """
        return self._GpuCount

    @GpuCount.setter
    def GpuCount(self, GpuCount):
        self._GpuCount = GpuCount

    @property
    def Frequency(self):
        """CPU clock rate of the instance
        :rtype: str
        """
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
        :param _PublicIpAssigned: Whether to allocate a public IP address. Valid values:<br><li>true: Allocate a public IP address.</li><li>false: Do not allocate a public IP address.</li><br>When the public network bandwidth is greater than 0 Mbps, you can choose whether to enable the public IP address. The public IP address is enabled by default. When the public network bandwidth is 0, allocating the public IP address is not supported. This parameter is only used as an input parameter in the RunInstances API.
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
        """Network connection billing plan. Valid value: <br><li>TRAFFIC_POSTPAID_BY_HOUR: pay after use. You are billed for your traffic, by the hour.
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        """The maximum outbound bandwidth of the public network, in Mbps. The default value is 0 Mbps. The upper limit of bandwidth varies for different models. For more information, see [Purchase Network Bandwidth](https://intl.cloud.tencent.com/document/product/213/12523?from_cn_redirect=1).
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def PublicIpAssigned(self):
        """Whether to allocate a public IP address. Valid values:<br><li>true: Allocate a public IP address.</li><li>false: Do not allocate a public IP address.</li><br>When the public network bandwidth is greater than 0 Mbps, you can choose whether to enable the public IP address. The public IP address is enabled by default. When the public network bandwidth is 0, allocating the public IP address is not supported. This parameter is only used as an input parameter in the RunInstances API.
        :rtype: bool
        """
        return self._PublicIpAssigned

    @PublicIpAssigned.setter
    def PublicIpAssigned(self, PublicIpAssigned):
        self._PublicIpAssigned = PublicIpAssigned

    @property
    def BandwidthPackageId(self):
        """Bandwidth package ID. To obatin the IDs, you can call [`DescribeBandwidthPackages`](https://intl.cloud.tencent.com/document/api/215/19209?from_cn_redirect=1) and look for the `BandwidthPackageId` fields in the response.
        :rtype: str
        """
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
        """The original unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def ChargeUnit(self):
        """Billing unit for pay-as-you-go mode. Valid values: <br><li>HOUR: billed on an hourly basis. It's used for hourly postpaid instances (`POSTPAID_BY_HOUR`). <br><li>GB: bill by traffic in GB. It's used for postpaid products that are billed by the hourly traffic (`TRAFFIC_POSTPAID_BY_HOUR`).
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def OriginalPrice(self):
        """The original price of a pay-in-advance instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice

    @property
    def DiscountPrice(self):
        """Discount price of a prepaid instance, in USD.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def Discount(self):
        """Percentage of the original price. For example, if you enter "20.0", the discounted price will be 20% of the original price.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def UnitPriceDiscount(self):
        """The discounted unit price for pay-as-you-go mode in USD. <br><li>When a billing tier is returned, it indicates the price fo the returned billing tier. For example, if `UnitPriceSecondStep` is returned, it refers to the unit price for the usage between 0 to 96 hours. Otherwise, it refers to that the unit price for unlimited usage.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount

    @property
    def UnitPriceSecondStep(self):
        """Original unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._UnitPriceSecondStep

    @UnitPriceSecondStep.setter
    def UnitPriceSecondStep(self, UnitPriceSecondStep):
        self._UnitPriceSecondStep = UnitPriceSecondStep

    @property
    def UnitPriceDiscountSecondStep(self):
        """Discounted unit price for the usage between 96 to 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._UnitPriceDiscountSecondStep

    @UnitPriceDiscountSecondStep.setter
    def UnitPriceDiscountSecondStep(self, UnitPriceDiscountSecondStep):
        self._UnitPriceDiscountSecondStep = UnitPriceDiscountSecondStep

    @property
    def UnitPriceThirdStep(self):
        """Original unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._UnitPriceThirdStep

    @UnitPriceThirdStep.setter
    def UnitPriceThirdStep(self, UnitPriceThirdStep):
        self._UnitPriceThirdStep = UnitPriceThirdStep

    @property
    def UnitPriceDiscountThirdStep(self):
        """Discounted unit price for the usage after 360 hours in USD. It's applicable to pay-as-you-go mode.
Note: this field may return null, indicating that no valid value is obtained.
        :rtype: float
        """
        return self._UnitPriceDiscountThirdStep

    @UnitPriceDiscountThirdStep.setter
    def UnitPriceDiscountThirdStep(self, UnitPriceDiscountThirdStep):
        self._UnitPriceDiscountThirdStep = UnitPriceDiscountThirdStep

    @property
    def OriginalPriceThreeYear(self):
        """Original 3-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._OriginalPriceThreeYear

    @OriginalPriceThreeYear.setter
    def OriginalPriceThreeYear(self, OriginalPriceThreeYear):
        self._OriginalPriceThreeYear = OriginalPriceThreeYear

    @property
    def DiscountPriceThreeYear(self):
        """Discounted 3-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._DiscountPriceThreeYear

    @DiscountPriceThreeYear.setter
    def DiscountPriceThreeYear(self, DiscountPriceThreeYear):
        self._DiscountPriceThreeYear = DiscountPriceThreeYear

    @property
    def DiscountThreeYear(self):
        """Discount for 3-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._DiscountThreeYear

    @DiscountThreeYear.setter
    def DiscountThreeYear(self, DiscountThreeYear):
        self._DiscountThreeYear = DiscountThreeYear

    @property
    def OriginalPriceFiveYear(self):
        """Original 5-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._OriginalPriceFiveYear

    @OriginalPriceFiveYear.setter
    def OriginalPriceFiveYear(self, OriginalPriceFiveYear):
        self._OriginalPriceFiveYear = OriginalPriceFiveYear

    @property
    def DiscountPriceFiveYear(self):
        """Discounted 5-year upfront payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._DiscountPriceFiveYear

    @DiscountPriceFiveYear.setter
    def DiscountPriceFiveYear(self, DiscountPriceFiveYear):
        self._DiscountPriceFiveYear = DiscountPriceFiveYear

    @property
    def DiscountFiveYear(self):
        """Discount for 5-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._DiscountFiveYear

    @DiscountFiveYear.setter
    def DiscountFiveYear(self, DiscountFiveYear):
        self._DiscountFiveYear = DiscountFiveYear

    @property
    def OriginalPriceOneYear(self):
        """Original 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._OriginalPriceOneYear

    @OriginalPriceOneYear.setter
    def OriginalPriceOneYear(self, OriginalPriceOneYear):
        self._OriginalPriceOneYear = OriginalPriceOneYear

    @property
    def DiscountPriceOneYear(self):
        """Discounted 1-year payment, in USD. This parameter is only available to upfront payment mode.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
        return self._DiscountPriceOneYear

    @DiscountPriceOneYear.setter
    def DiscountPriceOneYear(self, DiscountPriceOneYear):
        self._DiscountPriceOneYear = DiscountPriceOneYear

    @property
    def DiscountOneYear(self):
        """Discount for 1-year upfront payment. For example, 20.0 indicates 80% off.
Note: this field may return `null`, indicating that no valid value was found.
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: float
        """
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
        


class JobView(AbstractModel):
    """Job information

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        :param _JobName: Job name
        :type JobName: str
        :param _JobState: Job state
        :type JobState: str
        :param _Priority: Job priority
        :type Priority: int
        :param _Placement: Location information
Note: This field may return `null`, indicating that no valid value was found.
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _EndTime: End time
Note: This field may return `null`, indicating that no valid value was found.
        :type EndTime: str
        :param _TaskMetrics: Task statistical metrics
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        :param _Tags: List of tags bound with the job.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self._JobId = None
        self._JobName = None
        self._JobState = None
        self._Priority = None
        self._Placement = None
        self._CreateTime = None
        self._EndTime = None
        self._TaskMetrics = None
        self._Tags = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobName(self):
        """Job name
        :rtype: str
        """
        return self._JobName

    @JobName.setter
    def JobName(self, JobName):
        self._JobName = JobName

    @property
    def JobState(self):
        """Job state
        :rtype: str
        """
        return self._JobState

    @JobState.setter
    def JobState(self, JobState):
        self._JobState = JobState

    @property
    def Priority(self):
        """Job priority
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Placement(self):
        """Location information
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: :class:`tencentcloud.batch.v20170312.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

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
    def EndTime(self):
        """End time
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskMetrics(self):
        """Task statistical metrics
        :rtype: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        """
        return self._TaskMetrics

    @TaskMetrics.setter
    def TaskMetrics(self, TaskMetrics):
        self._TaskMetrics = TaskMetrics

    @property
    def Tags(self):
        """List of tags bound with the job.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobName = params.get("JobName")
        self._JobState = params.get("JobState")
        self._Priority = params.get("Priority")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        if params.get("TaskMetrics") is not None:
            self._TaskMetrics = TaskMetrics()
            self._TaskMetrics._deserialize(params.get("TaskMetrics"))
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
        """Type of a local disk.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PartitionType(self):
        """Attributes of a local disk.
        :rtype: str
        """
        return self._PartitionType

    @PartitionType.setter
    def PartitionType(self, PartitionType):
        self._PartitionType = PartitionType

    @property
    def MinSize(self):
        """Minimum size of a local disk.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """Maximum size of a local disk.
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def Required(self):
        """Whether a local disk is required during purchase. Valid values:<br><li>REQUIRED: required<br><li>OPTIONAL: optional
        :rtype: str
        """
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
        :param _Password: Login password of the instance. <br><li>Linux instances: 8-16 characters, containing at least two of the following categories: [a-z, A-Z], [0-9] and [()`~!@#$%^&*-+=|{}[]:;',.?/]. <br><li>Windows instances: 12-16 characters, containing at least three of the following categories: [a-z], [A-Z], [0-9] and [()`~!@#$%^&*-+={}[]:;',.?/]. <br><br>If this parameter is not specified, a random password will be generated and sent to you via the Message Center.
        :type Password: str
        :param _KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
        :type KeyIds: list of str
        :param _KeepImageLogin: Whether to keep the original settings of an image. Values: `TRUE` (default), `FALSE`. It cannot be specified together with `Password` or `KeyIds.N`. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. 
        :type KeepImageLogin: str
        """
        self._Password = None
        self._KeyIds = None
        self._KeepImageLogin = None

    @property
    def Password(self):
        """Login password of the instance. <br><li>Linux instances: 8-16 characters, containing at least two of the following categories: [a-z, A-Z], [0-9] and [()`~!@#$%^&*-+=|{}[]:;',.?/]. <br><li>Windows instances: 12-16 characters, containing at least three of the following categories: [a-z], [A-Z], [0-9] and [()`~!@#$%^&*-+={}[]:;',.?/]. <br><br>If this parameter is not specified, a random password will be generated and sent to you via the Message Center.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def KeyIds(self):
        """List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        """Whether to keep the original settings of an image. Values: `TRUE` (default), `FALSE`. It cannot be specified together with `Password` or `KeyIds.N`. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. 
        :rtype: str
        """
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
        


class ModifyComputeEnvRequest(AbstractModel):
    """ModifyComputeEnv request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param _EnvName: Compute environment name
        :type EnvName: str
        :param _EnvDescription: Compute environment description
        :type EnvDescription: str
        :param _EnvData: Compute environment attributes
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.ComputeEnvData`
        """
        self._EnvId = None
        self._DesiredComputeNodeCount = None
        self._EnvName = None
        self._EnvDescription = None
        self._EnvData = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DesiredComputeNodeCount(self):
        """Number of desired compute nodes
        :rtype: int
        """
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def EnvName(self):
        """Compute environment name
        :rtype: str
        """
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnvDescription(self):
        """Compute environment description
        :rtype: str
        """
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvData(self):
        """Compute environment attributes
        :rtype: :class:`tencentcloud.batch.v20170312.models.ComputeEnvData`
        """
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._EnvName = params.get("EnvName")
        self._EnvDescription = params.get("EnvDescription")
        if params.get("EnvData") is not None:
            self._EnvData = ComputeEnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyComputeEnvResponse(AbstractModel):
    """ModifyComputeEnv response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTaskTemplateRequest(AbstractModel):
    """ModifyTaskTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TaskTemplateId: Task template ID
        :type TaskTemplateId: str
        :param _TaskTemplateName: Task template name
        :type TaskTemplateName: str
        :param _TaskTemplateDescription: Task template description
        :type TaskTemplateDescription: str
        :param _TaskTemplateInfo: Task template information
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        """
        self._TaskTemplateId = None
        self._TaskTemplateName = None
        self._TaskTemplateDescription = None
        self._TaskTemplateInfo = None

    @property
    def TaskTemplateId(self):
        """Task template ID
        :rtype: str
        """
        return self._TaskTemplateId

    @TaskTemplateId.setter
    def TaskTemplateId(self, TaskTemplateId):
        self._TaskTemplateId = TaskTemplateId

    @property
    def TaskTemplateName(self):
        """Task template name
        :rtype: str
        """
        return self._TaskTemplateName

    @TaskTemplateName.setter
    def TaskTemplateName(self, TaskTemplateName):
        self._TaskTemplateName = TaskTemplateName

    @property
    def TaskTemplateDescription(self):
        """Task template description
        :rtype: str
        """
        return self._TaskTemplateDescription

    @TaskTemplateDescription.setter
    def TaskTemplateDescription(self, TaskTemplateDescription):
        self._TaskTemplateDescription = TaskTemplateDescription

    @property
    def TaskTemplateInfo(self):
        """Task template information
        :rtype: :class:`tencentcloud.batch.v20170312.models.Task`
        """
        return self._TaskTemplateInfo

    @TaskTemplateInfo.setter
    def TaskTemplateInfo(self, TaskTemplateInfo):
        self._TaskTemplateInfo = TaskTemplateInfo


    def _deserialize(self, params):
        self._TaskTemplateId = params.get("TaskTemplateId")
        self._TaskTemplateName = params.get("TaskTemplateName")
        self._TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self._TaskTemplateInfo = Task()
            self._TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTaskTemplateResponse(AbstractModel):
    """ModifyTaskTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MountDataDisk(AbstractModel):
    """Data disk mounting option

    """

    def __init__(self):
        r"""
        :param _LocalPath: Mounting point. A valid path (for Linux) for a drive (for Windows, such as "H:\\")
        :type LocalPath: str
        :param _FileSystemType: File system type. Linux: `EXT3` (default) and `EXT4`. Windows: `NTFS`
        :type FileSystemType: str
        """
        self._LocalPath = None
        self._FileSystemType = None

    @property
    def LocalPath(self):
        """Mounting point. A valid path (for Linux) for a drive (for Windows, such as "H:\\")
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def FileSystemType(self):
        """File system type. Linux: `EXT3` (default) and `EXT4`. Windows: `NTFS`
        :rtype: str
        """
        return self._FileSystemType

    @FileSystemType.setter
    def FileSystemType(self, FileSystemType):
        self._FileSystemType = FileSystemType


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._FileSystemType = params.get("FileSystemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamedComputeEnv(AbstractModel):
    """Compute environment

    """

    def __init__(self):
        r"""
        :param _EnvName: Compute environment name
        :type EnvName: str
        :param _DesiredComputeNodeCount: Number of desired compute nodes
        :type DesiredComputeNodeCount: int
        :param _EnvDescription: Compute environment description
        :type EnvDescription: str
        :param _EnvType: Compute environment management type
        :type EnvType: str
        :param _EnvData: Compute environment's specific parameters
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param _MountDataDisks: Data disk mounting option
        :type MountDataDisks: list of MountDataDisk
        :param _Authentications: Authorization information
        :type Authentications: list of Authentication
        :param _InputMappings: Input mapping information
        :type InputMappings: list of InputMapping
        :param _AgentRunningMode: Agent running mode; applicable for Windows
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        :param _Notifications: Notification information
        :type Notifications: list of Notification
        :param _ActionIfComputeNodeInactive: Policy for inactive nodes. Default: `RECREATE`, which means that instance resources will be re-created periodically for compute nodes where instance creation fails or is abnormally returned.
        :type ActionIfComputeNodeInactive: str
        :param _ResourceMaxRetryCount: When the instances are failed to be created or returned because of exceptions, the related compute node will retry to create instances periodically. This parameter specifies the maximum retry attempts. The max value is 100 and the default value is `7`.
        :type ResourceMaxRetryCount: int
        :param _Tags: List of tags to bind with a compute environment. Each compute environment can have up to 10 tags.
        :type Tags: list of Tag
        :param _NotificationTarget: Target of the notification
Values: `CMQ`, `TDMQ_CMQ`
`CMQ`: Tencent Cloud CMQ (default)
`TDMQ_CMQ`: Tencent Cloud TDMQ_CMQ.<br/>Note: CMQ has been discontinued. Please use `TDMQ_CMQ`. See [CMQ Queue Migration to TDMQ for CMQ](https://intl.cloud.tencent.com/document/product/406/60860?from_cn_redirect=1)
        :type NotificationTarget: str
        """
        self._EnvName = None
        self._DesiredComputeNodeCount = None
        self._EnvDescription = None
        self._EnvType = None
        self._EnvData = None
        self._MountDataDisks = None
        self._Authentications = None
        self._InputMappings = None
        self._AgentRunningMode = None
        self._Notifications = None
        self._ActionIfComputeNodeInactive = None
        self._ResourceMaxRetryCount = None
        self._Tags = None
        self._NotificationTarget = None

    @property
    def EnvName(self):
        """Compute environment name
        :rtype: str
        """
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def DesiredComputeNodeCount(self):
        """Number of desired compute nodes
        :rtype: int
        """
        return self._DesiredComputeNodeCount

    @DesiredComputeNodeCount.setter
    def DesiredComputeNodeCount(self, DesiredComputeNodeCount):
        self._DesiredComputeNodeCount = DesiredComputeNodeCount

    @property
    def EnvDescription(self):
        """Compute environment description
        :rtype: str
        """
        return self._EnvDescription

    @EnvDescription.setter
    def EnvDescription(self, EnvDescription):
        self._EnvDescription = EnvDescription

    @property
    def EnvType(self):
        """Compute environment management type
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvData(self):
        """Compute environment's specific parameters
        :rtype: :class:`tencentcloud.batch.v20170312.models.EnvData`
        """
        return self._EnvData

    @EnvData.setter
    def EnvData(self, EnvData):
        self._EnvData = EnvData

    @property
    def MountDataDisks(self):
        """Data disk mounting option
        :rtype: list of MountDataDisk
        """
        return self._MountDataDisks

    @MountDataDisks.setter
    def MountDataDisks(self, MountDataDisks):
        self._MountDataDisks = MountDataDisks

    @property
    def Authentications(self):
        """Authorization information
        :rtype: list of Authentication
        """
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def InputMappings(self):
        """Input mapping information
        :rtype: list of InputMapping
        """
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def AgentRunningMode(self):
        """Agent running mode; applicable for Windows
        :rtype: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        """
        return self._AgentRunningMode

    @AgentRunningMode.setter
    def AgentRunningMode(self, AgentRunningMode):
        self._AgentRunningMode = AgentRunningMode

    @property
    def Notifications(self):
        """Notification information
        :rtype: list of Notification
        """
        return self._Notifications

    @Notifications.setter
    def Notifications(self, Notifications):
        self._Notifications = Notifications

    @property
    def ActionIfComputeNodeInactive(self):
        """Policy for inactive nodes. Default: `RECREATE`, which means that instance resources will be re-created periodically for compute nodes where instance creation fails or is abnormally returned.
        :rtype: str
        """
        return self._ActionIfComputeNodeInactive

    @ActionIfComputeNodeInactive.setter
    def ActionIfComputeNodeInactive(self, ActionIfComputeNodeInactive):
        self._ActionIfComputeNodeInactive = ActionIfComputeNodeInactive

    @property
    def ResourceMaxRetryCount(self):
        """When the instances are failed to be created or returned because of exceptions, the related compute node will retry to create instances periodically. This parameter specifies the maximum retry attempts. The max value is 100 and the default value is `7`.
        :rtype: int
        """
        return self._ResourceMaxRetryCount

    @ResourceMaxRetryCount.setter
    def ResourceMaxRetryCount(self, ResourceMaxRetryCount):
        self._ResourceMaxRetryCount = ResourceMaxRetryCount

    @property
    def Tags(self):
        """List of tags to bind with a compute environment. Each compute environment can have up to 10 tags.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NotificationTarget(self):
        """Target of the notification
Values: `CMQ`, `TDMQ_CMQ`
`CMQ`: Tencent Cloud CMQ (default)
`TDMQ_CMQ`: Tencent Cloud TDMQ_CMQ.<br/>Note: CMQ has been discontinued. Please use `TDMQ_CMQ`. See [CMQ Queue Migration to TDMQ for CMQ](https://intl.cloud.tencent.com/document/product/406/60860?from_cn_redirect=1)
        :rtype: str
        """
        return self._NotificationTarget

    @NotificationTarget.setter
    def NotificationTarget(self, NotificationTarget):
        self._NotificationTarget = NotificationTarget


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        self._DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self._EnvDescription = params.get("EnvDescription")
        self._EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self._EnvData = EnvData()
            self._EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self._MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self._MountDataDisks.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("AgentRunningMode") is not None:
            self._AgentRunningMode = AgentRunningMode()
            self._AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        if params.get("Notifications") is not None:
            self._Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self._Notifications.append(obj)
        self._ActionIfComputeNodeInactive = params.get("ActionIfComputeNodeInactive")
        self._ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NotificationTarget = params.get("NotificationTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Notification(AbstractModel):
    """Notification information

    """

    def __init__(self):
        r"""
        :param _TopicName: CMQ topic name which should be valid and associated with a subscription
        :type TopicName: str
        :param _EventConfigs: Event configuration
        :type EventConfigs: list of EventConfig
        """
        self._TopicName = None
        self._EventConfigs = None

    @property
    def TopicName(self):
        """CMQ topic name which should be valid and associated with a subscription
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def EventConfigs(self):
        """Event configuration
        :rtype: list of EventConfig
        """
        return self._EventConfigs

    @EventConfigs.setter
    def EventConfigs(self, EventConfigs):
        self._EventConfigs = EventConfigs


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        if params.get("EventConfigs") is not None:
            self._EventConfigs = []
            for item in params.get("EventConfigs"):
                obj = EventConfig()
                obj._deserialize(item)
                self._EventConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMapping(AbstractModel):
    """Output mapping

    """

    def __init__(self):
        r"""
        :param _SourcePath: Source path
        :type SourcePath: str
        :param _DestinationPath: Destination path
        :type DestinationPath: str
        :param _OutputMappingOption: Output mapping options
Note: This field may return `null`, indicating that no valid value was found.
        :type OutputMappingOption: :class:`tencentcloud.batch.v20170312.models.OutputMappingOption`
        """
        self._SourcePath = None
        self._DestinationPath = None
        self._OutputMappingOption = None

    @property
    def SourcePath(self):
        """Source path
        :rtype: str
        """
        return self._SourcePath

    @SourcePath.setter
    def SourcePath(self, SourcePath):
        self._SourcePath = SourcePath

    @property
    def DestinationPath(self):
        """Destination path
        :rtype: str
        """
        return self._DestinationPath

    @DestinationPath.setter
    def DestinationPath(self, DestinationPath):
        self._DestinationPath = DestinationPath

    @property
    def OutputMappingOption(self):
        """Output mapping options
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: :class:`tencentcloud.batch.v20170312.models.OutputMappingOption`
        """
        return self._OutputMappingOption

    @OutputMappingOption.setter
    def OutputMappingOption(self, OutputMappingOption):
        self._OutputMappingOption = OutputMappingOption


    def _deserialize(self, params):
        self._SourcePath = params.get("SourcePath")
        self._DestinationPath = params.get("DestinationPath")
        if params.get("OutputMappingOption") is not None:
            self._OutputMappingOption = OutputMappingOption()
            self._OutputMappingOption._deserialize(params.get("OutputMappingOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMappingConfig(AbstractModel):
    """Output mapping configuration

    """

    def __init__(self):
        r"""
        :param _Scene: Storage type. Only `COS` is supported.
        :type Scene: str
        :param _WorkerNum: Number of concurrent workers
        :type WorkerNum: int
        :param _WorkerPartSize: Size of a worker part, in MB.
        :type WorkerPartSize: int
        """
        self._Scene = None
        self._WorkerNum = None
        self._WorkerPartSize = None

    @property
    def Scene(self):
        """Storage type. Only `COS` is supported.
        :rtype: str
        """
        return self._Scene

    @Scene.setter
    def Scene(self, Scene):
        self._Scene = Scene

    @property
    def WorkerNum(self):
        """Number of concurrent workers
        :rtype: int
        """
        return self._WorkerNum

    @WorkerNum.setter
    def WorkerNum(self, WorkerNum):
        self._WorkerNum = WorkerNum

    @property
    def WorkerPartSize(self):
        """Size of a worker part, in MB.
        :rtype: int
        """
        return self._WorkerPartSize

    @WorkerPartSize.setter
    def WorkerPartSize(self, WorkerPartSize):
        self._WorkerPartSize = WorkerPartSize


    def _deserialize(self, params):
        self._Scene = params.get("Scene")
        self._WorkerNum = params.get("WorkerNum")
        self._WorkerPartSize = params.get("WorkerPartSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputMappingOption(AbstractModel):
    """Output mapping options

    """

    def __init__(self):
        r"""
        :param _Workspace: The mapped output workspace on the container side for the instance.
`BATCH_WORKSPACE` (Default): The workspace is the workspace defined for the usage of Batch Compute. Batch Compute ensures the isolation between jobs.
`GLOBAL_WORKSPACE`: The workspace is the instance OS space..
Note: This field may return `null`, indicating that no valid value was found.
        :type Workspace: str
        """
        self._Workspace = None

    @property
    def Workspace(self):
        """The mapped output workspace on the container side for the instance.
`BATCH_WORKSPACE` (Default): The workspace is the workspace defined for the usage of Batch Compute. Batch Compute ensures the isolation between jobs.
`GLOBAL_WORKSPACE`: The workspace is the instance OS space..
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Workspace

    @Workspace.setter
    def Workspace(self, Workspace):
        self._Workspace = Workspace


    def _deserialize(self, params):
        self._Workspace = params.get("Workspace")
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
        :param _HostId: The ID of the CDH to which the instance belongs, only used as an output parameter.
        :type HostId: str
        """
        self._Zone = None
        self._ProjectId = None
        self._HostIds = None
        self._HostId = None

    @property
    def Zone(self):
        """ID of the availability zone where the instance resides. You can call the [DescribeZones](https://intl.cloud.tencent.com/document/product/213/35071) API and obtain the ID in the returned `Zone` field.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ProjectId(self):
        """ID of the project to which the instance belongs. This parameter can be obtained from the `projectId` returned by [DescribeProject](https://intl.cloud.tencent.com/document/api/651/78725?from_cn_redirect=1). If this is left empty, the default project is used.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def HostIds(self):
        """ID list of CDHs from which the instance can be created. If you have purchased CDHs and specify this parameter, the instances you purchase will be randomly deployed on the CDHs.
        :rtype: list of str
        """
        return self._HostIds

    @HostIds.setter
    def HostIds(self, HostIds):
        self._HostIds = HostIds

    @property
    def HostId(self):
        """The ID of the CDH to which the instance belongs, only used as an output parameter.
        :rtype: str
        """
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ProjectId = params.get("ProjectId")
        self._HostIds = params.get("HostIds")
        self._HostId = params.get("HostId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedirectInfo(AbstractModel):
    """Redirection information

    """

    def __init__(self):
        r"""
        :param _StdoutRedirectPath: Standard output redirection path
        :type StdoutRedirectPath: str
        :param _StderrRedirectPath: Standard error redirection path
        :type StderrRedirectPath: str
        :param _StdoutRedirectFileName: Standard output redirection file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :type StdoutRedirectFileName: str
        :param _StderrRedirectFileName: Standard error redirection file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :type StderrRedirectFileName: str
        """
        self._StdoutRedirectPath = None
        self._StderrRedirectPath = None
        self._StdoutRedirectFileName = None
        self._StderrRedirectFileName = None

    @property
    def StdoutRedirectPath(self):
        """Standard output redirection path
        :rtype: str
        """
        return self._StdoutRedirectPath

    @StdoutRedirectPath.setter
    def StdoutRedirectPath(self, StdoutRedirectPath):
        self._StdoutRedirectPath = StdoutRedirectPath

    @property
    def StderrRedirectPath(self):
        """Standard error redirection path
        :rtype: str
        """
        return self._StderrRedirectPath

    @StderrRedirectPath.setter
    def StderrRedirectPath(self, StderrRedirectPath):
        self._StderrRedirectPath = StderrRedirectPath

    @property
    def StdoutRedirectFileName(self):
        """Standard output redirection file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :rtype: str
        """
        return self._StdoutRedirectFileName

    @StdoutRedirectFileName.setter
    def StdoutRedirectFileName(self, StdoutRedirectFileName):
        self._StdoutRedirectFileName = StdoutRedirectFileName

    @property
    def StderrRedirectFileName(self):
        """Standard error redirection file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :rtype: str
        """
        return self._StderrRedirectFileName

    @StderrRedirectFileName.setter
    def StderrRedirectFileName(self, StderrRedirectFileName):
        self._StderrRedirectFileName = StderrRedirectFileName


    def _deserialize(self, params):
        self._StdoutRedirectPath = params.get("StdoutRedirectPath")
        self._StderrRedirectPath = params.get("StderrRedirectPath")
        self._StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self._StderrRedirectFileName = params.get("StderrRedirectFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedirectLocalInfo(AbstractModel):
    """Local redirection information

    """

    def __init__(self):
        r"""
        :param _StdoutLocalPath: Standard output redirection local path
        :type StdoutLocalPath: str
        :param _StderrLocalPath: Standard error redirection local path
        :type StderrLocalPath: str
        :param _StdoutLocalFileName: Standard output redirection local file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :type StdoutLocalFileName: str
        :param _StderrLocalFileName: Standard error redirection local file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :type StderrLocalFileName: str
        """
        self._StdoutLocalPath = None
        self._StderrLocalPath = None
        self._StdoutLocalFileName = None
        self._StderrLocalFileName = None

    @property
    def StdoutLocalPath(self):
        """Standard output redirection local path
        :rtype: str
        """
        return self._StdoutLocalPath

    @StdoutLocalPath.setter
    def StdoutLocalPath(self, StdoutLocalPath):
        self._StdoutLocalPath = StdoutLocalPath

    @property
    def StderrLocalPath(self):
        """Standard error redirection local path
        :rtype: str
        """
        return self._StderrLocalPath

    @StderrLocalPath.setter
    def StderrLocalPath(self, StderrLocalPath):
        self._StderrLocalPath = StderrLocalPath

    @property
    def StdoutLocalFileName(self):
        """Standard output redirection local file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :rtype: str
        """
        return self._StdoutLocalFileName

    @StdoutLocalFileName.setter
    def StdoutLocalFileName(self, StdoutLocalFileName):
        self._StdoutLocalFileName = StdoutLocalFileName

    @property
    def StderrLocalFileName(self):
        """Standard error redirection local file name, which supports three placeholders: `${BATCH_JOB_ID}`, `${BATCH_TASK_NAME}`, and `${BATCH_TASK_INSTANCE_INDEX}`
        :rtype: str
        """
        return self._StderrLocalFileName

    @StderrLocalFileName.setter
    def StderrLocalFileName(self, StderrLocalFileName):
        self._StderrLocalFileName = StderrLocalFileName


    def _deserialize(self, params):
        self._StdoutLocalPath = params.get("StdoutLocalPath")
        self._StderrLocalPath = params.get("StderrLocalPath")
        self._StdoutLocalFileName = params.get("StdoutLocalFileName")
        self._StderrLocalFileName = params.get("StderrLocalFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryJobsRequest(AbstractModel):
    """RetryJobs request structure.

    """

    def __init__(self):
        r"""
        :param _JobIds: List of job IDs.
        :type JobIds: list of str
        """
        self._JobIds = None

    @property
    def JobIds(self):
        """List of job IDs.
        :rtype: list of str
        """
        return self._JobIds

    @JobIds.setter
    def JobIds(self, JobIds):
        self._JobIds = JobIds


    def _deserialize(self, params):
        self._JobIds = params.get("JobIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryJobsResponse(AbstractModel):
    """RetryJobs response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
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
        """Whether to enable the TAT service. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default: `FALSE`.
        :rtype: bool
        """
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
        """Whether to enable [Cloud Monitor](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Monitor <br><li>FALSE: do not enable Cloud Monitor <br><br>Default value: TRUE.
        :rtype: bool
        """
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
        """Whether to enable [Cloud Security](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Security <br><li>FALSE: do not enable Cloud Security <br><br>Default value: TRUE.
        :rtype: bool
        """
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
        """Bidding price
        :rtype: str
        """
        return self._MaxPrice

    @MaxPrice.setter
    def MaxPrice(self, MaxPrice):
        self._MaxPrice = MaxPrice

    @property
    def SpotInstanceType(self):
        """Bidding request type. Currently only "one-time" is supported.
        :rtype: str
        """
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
        """Local HDD storage type. Value: LOCAL_PRO.
Note: This field may return null, indicating that no valid value is found.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def MinSize(self):
        """Minimum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        """Maximum capacity of local HDD storage
Note: This field may return null, indicating that no valid value is found.
        :rtype: int
        """
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
        """System disk type. For more information about the limits of system disk types, please see [Storage Overview](https://intl.cloud.tencent.com/document/product/213/4952?from_cn_redirect=1). Valid values:<br><li>LOCAL_BASIC: local disk<br><li>LOCAL_SSD: local SSD disk<br><li>CLOUD_BASIC: HDD cloud disk<br><li>CLOUD_SSD: SSD cloud disk<br><li>CLOUD_PREMIUM: Premium cloud storage<br><li>CLOUD_BSSD: Balanced SSD<br><br>The disk currently in stock will be used by default.
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        """System disk ID. System disks whose type is `LOCAL_BASIC` or `LOCAL_SSD` do not have an ID and do not support this parameter.
It is only used as a response parameter for APIs such as `DescribeInstances`, and cannot be used as a request parameter for APIs such as `RunInstances`.
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        """System disk size; unit: GB; default value: 50 GB.
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def CdcId(self):
        """ID of the dedicated cluster to which the instance belongs.
        :rtype: str
        """
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
    """Information on tags

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
Note: This field may return `null`, indicating that no valid value was found.
        :type Key: str
        :param _Value: Tag value
Note: This field may return `null`, indicating that no valid value was found.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Tag key
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value
Note: This field may return `null`, indicating that no valid value was found.
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
        


class Task(AbstractModel):
    """Task

    """

    def __init__(self):
        r"""
        :param _Application: Application information
        :type Application: :class:`tencentcloud.batch.v20170312.models.Application`
        :param _TaskName: Task name, which should be unique within a job
        :type TaskName: str
        :param _TaskInstanceNum: Number of running task instances
        :type TaskInstanceNum: int
        :param _ComputeEnv: Compute environment information. One (and only one) parameter must be specified for ComputeEnv and EnvId.
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.AnonymousComputeEnv`
        :param _EnvId: Compute environment ID. One (and only one) parameter must be specified for ComputeEnv and EnvId.
        :type EnvId: str
        :param _RedirectInfo: Redirection information
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param _RedirectLocalInfo: Local redirection information
        :type RedirectLocalInfo: :class:`tencentcloud.batch.v20170312.models.RedirectLocalInfo`
        :param _InputMappings: Input mapping
        :type InputMappings: list of InputMapping
        :param _OutputMappings: Output mapping
        :type OutputMappings: list of OutputMapping
        :param _OutputMappingConfigs: Output mapping configuration
        :type OutputMappingConfigs: list of OutputMappingConfig
        :param _EnvVars: Custom environment variable
        :type EnvVars: list of EnvVar
        :param _Authentications: Authorization information
        :type Authentications: list of Authentication
        :param _FailedAction: The processing method after the TaskInstance fails; Value range: `TERMINATE` (default), `INTERRUPT`, `FAST_INTERRUPT`.
        :type FailedAction: str
        :param _MaxRetryCount: The maximum number of retries after the task fails. Range: 0 - 5. Default value: 0
        :type MaxRetryCount: int
        :param _Timeout: Timeout period of the task in seconds. Defaults value: 86400
        :type Timeout: int
        :param _MaxConcurrentNum: The maximum number of concurrent tasks. Range: 0 - 200000. There is no limit by default.
        :type MaxConcurrentNum: int
        :param _RestartComputeNode: Restarts the compute node after the task is completed. This is suitable for specifying the compute environment for task execution.
        :type RestartComputeNode: bool
        :param _ResourceMaxRetryCount: Maximum number of retry attempts after failing to create computing resources such as the CVM in the task launch process. Default: `0`; Maximum: `100`.
        :type ResourceMaxRetryCount: int
        """
        self._Application = None
        self._TaskName = None
        self._TaskInstanceNum = None
        self._ComputeEnv = None
        self._EnvId = None
        self._RedirectInfo = None
        self._RedirectLocalInfo = None
        self._InputMappings = None
        self._OutputMappings = None
        self._OutputMappingConfigs = None
        self._EnvVars = None
        self._Authentications = None
        self._FailedAction = None
        self._MaxRetryCount = None
        self._Timeout = None
        self._MaxConcurrentNum = None
        self._RestartComputeNode = None
        self._ResourceMaxRetryCount = None

    @property
    def Application(self):
        """Application information
        :rtype: :class:`tencentcloud.batch.v20170312.models.Application`
        """
        return self._Application

    @Application.setter
    def Application(self, Application):
        self._Application = Application

    @property
    def TaskName(self):
        """Task name, which should be unique within a job
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskInstanceNum(self):
        """Number of running task instances
        :rtype: int
        """
        return self._TaskInstanceNum

    @TaskInstanceNum.setter
    def TaskInstanceNum(self, TaskInstanceNum):
        self._TaskInstanceNum = TaskInstanceNum

    @property
    def ComputeEnv(self):
        """Compute environment information. One (and only one) parameter must be specified for ComputeEnv and EnvId.
        :rtype: :class:`tencentcloud.batch.v20170312.models.AnonymousComputeEnv`
        """
        return self._ComputeEnv

    @ComputeEnv.setter
    def ComputeEnv(self, ComputeEnv):
        self._ComputeEnv = ComputeEnv

    @property
    def EnvId(self):
        """Compute environment ID. One (and only one) parameter must be specified for ComputeEnv and EnvId.
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def RedirectInfo(self):
        """Redirection information
        :rtype: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        """
        return self._RedirectInfo

    @RedirectInfo.setter
    def RedirectInfo(self, RedirectInfo):
        self._RedirectInfo = RedirectInfo

    @property
    def RedirectLocalInfo(self):
        """Local redirection information
        :rtype: :class:`tencentcloud.batch.v20170312.models.RedirectLocalInfo`
        """
        return self._RedirectLocalInfo

    @RedirectLocalInfo.setter
    def RedirectLocalInfo(self, RedirectLocalInfo):
        self._RedirectLocalInfo = RedirectLocalInfo

    @property
    def InputMappings(self):
        """Input mapping
        :rtype: list of InputMapping
        """
        return self._InputMappings

    @InputMappings.setter
    def InputMappings(self, InputMappings):
        self._InputMappings = InputMappings

    @property
    def OutputMappings(self):
        """Output mapping
        :rtype: list of OutputMapping
        """
        return self._OutputMappings

    @OutputMappings.setter
    def OutputMappings(self, OutputMappings):
        self._OutputMappings = OutputMappings

    @property
    def OutputMappingConfigs(self):
        """Output mapping configuration
        :rtype: list of OutputMappingConfig
        """
        return self._OutputMappingConfigs

    @OutputMappingConfigs.setter
    def OutputMappingConfigs(self, OutputMappingConfigs):
        self._OutputMappingConfigs = OutputMappingConfigs

    @property
    def EnvVars(self):
        """Custom environment variable
        :rtype: list of EnvVar
        """
        return self._EnvVars

    @EnvVars.setter
    def EnvVars(self, EnvVars):
        self._EnvVars = EnvVars

    @property
    def Authentications(self):
        """Authorization information
        :rtype: list of Authentication
        """
        return self._Authentications

    @Authentications.setter
    def Authentications(self, Authentications):
        self._Authentications = Authentications

    @property
    def FailedAction(self):
        """The processing method after the TaskInstance fails; Value range: `TERMINATE` (default), `INTERRUPT`, `FAST_INTERRUPT`.
        :rtype: str
        """
        return self._FailedAction

    @FailedAction.setter
    def FailedAction(self, FailedAction):
        self._FailedAction = FailedAction

    @property
    def MaxRetryCount(self):
        """The maximum number of retries after the task fails. Range: 0 - 5. Default value: 0
        :rtype: int
        """
        return self._MaxRetryCount

    @MaxRetryCount.setter
    def MaxRetryCount(self, MaxRetryCount):
        self._MaxRetryCount = MaxRetryCount

    @property
    def Timeout(self):
        """Timeout period of the task in seconds. Defaults value: 86400
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def MaxConcurrentNum(self):
        """The maximum number of concurrent tasks. Range: 0 - 200000. There is no limit by default.
        :rtype: int
        """
        return self._MaxConcurrentNum

    @MaxConcurrentNum.setter
    def MaxConcurrentNum(self, MaxConcurrentNum):
        self._MaxConcurrentNum = MaxConcurrentNum

    @property
    def RestartComputeNode(self):
        """Restarts the compute node after the task is completed. This is suitable for specifying the compute environment for task execution.
        :rtype: bool
        """
        return self._RestartComputeNode

    @RestartComputeNode.setter
    def RestartComputeNode(self, RestartComputeNode):
        self._RestartComputeNode = RestartComputeNode

    @property
    def ResourceMaxRetryCount(self):
        """Maximum number of retry attempts after failing to create computing resources such as the CVM in the task launch process. Default: `0`; Maximum: `100`.
        :rtype: int
        """
        return self._ResourceMaxRetryCount

    @ResourceMaxRetryCount.setter
    def ResourceMaxRetryCount(self, ResourceMaxRetryCount):
        self._ResourceMaxRetryCount = ResourceMaxRetryCount


    def _deserialize(self, params):
        if params.get("Application") is not None:
            self._Application = Application()
            self._Application._deserialize(params.get("Application"))
        self._TaskName = params.get("TaskName")
        self._TaskInstanceNum = params.get("TaskInstanceNum")
        if params.get("ComputeEnv") is not None:
            self._ComputeEnv = AnonymousComputeEnv()
            self._ComputeEnv._deserialize(params.get("ComputeEnv"))
        self._EnvId = params.get("EnvId")
        if params.get("RedirectInfo") is not None:
            self._RedirectInfo = RedirectInfo()
            self._RedirectInfo._deserialize(params.get("RedirectInfo"))
        if params.get("RedirectLocalInfo") is not None:
            self._RedirectLocalInfo = RedirectLocalInfo()
            self._RedirectLocalInfo._deserialize(params.get("RedirectLocalInfo"))
        if params.get("InputMappings") is not None:
            self._InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self._InputMappings.append(obj)
        if params.get("OutputMappings") is not None:
            self._OutputMappings = []
            for item in params.get("OutputMappings"):
                obj = OutputMapping()
                obj._deserialize(item)
                self._OutputMappings.append(obj)
        if params.get("OutputMappingConfigs") is not None:
            self._OutputMappingConfigs = []
            for item in params.get("OutputMappingConfigs"):
                obj = OutputMappingConfig()
                obj._deserialize(item)
                self._OutputMappingConfigs.append(obj)
        if params.get("EnvVars") is not None:
            self._EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self._EnvVars.append(obj)
        if params.get("Authentications") is not None:
            self._Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self._Authentications.append(obj)
        self._FailedAction = params.get("FailedAction")
        self._MaxRetryCount = params.get("MaxRetryCount")
        self._Timeout = params.get("Timeout")
        self._MaxConcurrentNum = params.get("MaxConcurrentNum")
        self._RestartComputeNode = params.get("RestartComputeNode")
        self._ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceLog(AbstractModel):
    """Task instance log details.

    """

    def __init__(self):
        r"""
        :param _TaskInstanceIndex: Task instance
        :type TaskInstanceIndex: int
        :param _StdoutLog: Standard output log (Base64-encoded, up to 2048 bytes after decompression)
Note: This field may return `null`, indicating that no valid value was found.
        :type StdoutLog: str
        :param _StderrLog: Standard error log (Base64-encoded, up to 2048 bytes after decompression)
Note: This field may return `null`, indicating that no valid value was found.
        :type StderrLog: str
        :param _StdoutRedirectPath: Standard output redirection path
Note: This field may return `null`, indicating that no valid value was found.
        :type StdoutRedirectPath: str
        :param _StderrRedirectPath: Standard error redirection path
Note: This field may return `null`, indicating that no valid value was found.
        :type StderrRedirectPath: str
        :param _StdoutRedirectFileName: Standard output redirection file name
Note: This field may return `null`, indicating that no valid value was found.
        :type StdoutRedirectFileName: str
        :param _StderrRedirectFileName: Standard error redirection file name
Note: This field may return `null`, indicating that no valid value was found.
        :type StderrRedirectFileName: str
        """
        self._TaskInstanceIndex = None
        self._StdoutLog = None
        self._StderrLog = None
        self._StdoutRedirectPath = None
        self._StderrRedirectPath = None
        self._StdoutRedirectFileName = None
        self._StderrRedirectFileName = None

    @property
    def TaskInstanceIndex(self):
        """Task instance
        :rtype: int
        """
        return self._TaskInstanceIndex

    @TaskInstanceIndex.setter
    def TaskInstanceIndex(self, TaskInstanceIndex):
        self._TaskInstanceIndex = TaskInstanceIndex

    @property
    def StdoutLog(self):
        """Standard output log (Base64-encoded, up to 2048 bytes after decompression)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._StdoutLog

    @StdoutLog.setter
    def StdoutLog(self, StdoutLog):
        self._StdoutLog = StdoutLog

    @property
    def StderrLog(self):
        """Standard error log (Base64-encoded, up to 2048 bytes after decompression)
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._StderrLog

    @StderrLog.setter
    def StderrLog(self, StderrLog):
        self._StderrLog = StderrLog

    @property
    def StdoutRedirectPath(self):
        """Standard output redirection path
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._StdoutRedirectPath

    @StdoutRedirectPath.setter
    def StdoutRedirectPath(self, StdoutRedirectPath):
        self._StdoutRedirectPath = StdoutRedirectPath

    @property
    def StderrRedirectPath(self):
        """Standard error redirection path
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._StderrRedirectPath

    @StderrRedirectPath.setter
    def StderrRedirectPath(self, StderrRedirectPath):
        self._StderrRedirectPath = StderrRedirectPath

    @property
    def StdoutRedirectFileName(self):
        """Standard output redirection file name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._StdoutRedirectFileName

    @StdoutRedirectFileName.setter
    def StdoutRedirectFileName(self, StdoutRedirectFileName):
        self._StdoutRedirectFileName = StdoutRedirectFileName

    @property
    def StderrRedirectFileName(self):
        """Standard error redirection file name
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._StderrRedirectFileName

    @StderrRedirectFileName.setter
    def StderrRedirectFileName(self, StderrRedirectFileName):
        self._StderrRedirectFileName = StderrRedirectFileName


    def _deserialize(self, params):
        self._TaskInstanceIndex = params.get("TaskInstanceIndex")
        self._StdoutLog = params.get("StdoutLog")
        self._StderrLog = params.get("StderrLog")
        self._StdoutRedirectPath = params.get("StdoutRedirectPath")
        self._StderrRedirectPath = params.get("StderrRedirectPath")
        self._StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self._StderrRedirectFileName = params.get("StderrRedirectFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceMetrics(AbstractModel):
    """Task instance statistical metrics

    """

    def __init__(self):
        r"""
        :param _SubmittedCount: Number of submitted tasks
        :type SubmittedCount: int
        :param _PendingCount: Number of pending tasks
        :type PendingCount: int
        :param _RunnableCount: Number of Runnable tasks
        :type RunnableCount: int
        :param _StartingCount: Number of starting tasks
        :type StartingCount: int
        :param _RunningCount: Number of running tasks
        :type RunningCount: int
        :param _SucceedCount: Number of successful tasks
        :type SucceedCount: int
        :param _FailedInterruptedCount: Number of failed and interrupted tasks
        :type FailedInterruptedCount: int
        :param _FailedCount: Number of failed tasks
        :type FailedCount: int
        """
        self._SubmittedCount = None
        self._PendingCount = None
        self._RunnableCount = None
        self._StartingCount = None
        self._RunningCount = None
        self._SucceedCount = None
        self._FailedInterruptedCount = None
        self._FailedCount = None

    @property
    def SubmittedCount(self):
        """Number of submitted tasks
        :rtype: int
        """
        return self._SubmittedCount

    @SubmittedCount.setter
    def SubmittedCount(self, SubmittedCount):
        self._SubmittedCount = SubmittedCount

    @property
    def PendingCount(self):
        """Number of pending tasks
        :rtype: int
        """
        return self._PendingCount

    @PendingCount.setter
    def PendingCount(self, PendingCount):
        self._PendingCount = PendingCount

    @property
    def RunnableCount(self):
        """Number of Runnable tasks
        :rtype: int
        """
        return self._RunnableCount

    @RunnableCount.setter
    def RunnableCount(self, RunnableCount):
        self._RunnableCount = RunnableCount

    @property
    def StartingCount(self):
        """Number of starting tasks
        :rtype: int
        """
        return self._StartingCount

    @StartingCount.setter
    def StartingCount(self, StartingCount):
        self._StartingCount = StartingCount

    @property
    def RunningCount(self):
        """Number of running tasks
        :rtype: int
        """
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def SucceedCount(self):
        """Number of successful tasks
        :rtype: int
        """
        return self._SucceedCount

    @SucceedCount.setter
    def SucceedCount(self, SucceedCount):
        self._SucceedCount = SucceedCount

    @property
    def FailedInterruptedCount(self):
        """Number of failed and interrupted tasks
        :rtype: int
        """
        return self._FailedInterruptedCount

    @FailedInterruptedCount.setter
    def FailedInterruptedCount(self, FailedInterruptedCount):
        self._FailedInterruptedCount = FailedInterruptedCount

    @property
    def FailedCount(self):
        """Number of failed tasks
        :rtype: int
        """
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount


    def _deserialize(self, params):
        self._SubmittedCount = params.get("SubmittedCount")
        self._PendingCount = params.get("PendingCount")
        self._RunnableCount = params.get("RunnableCount")
        self._StartingCount = params.get("StartingCount")
        self._RunningCount = params.get("RunningCount")
        self._SucceedCount = params.get("SucceedCount")
        self._FailedInterruptedCount = params.get("FailedInterruptedCount")
        self._FailedCount = params.get("FailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInstanceView(AbstractModel):
    """Task instance view information

    """

    def __init__(self):
        r"""
        :param _TaskInstanceIndex: Task instance index
        :type TaskInstanceIndex: int
        :param _TaskInstanceState: Task instance state
        :type TaskInstanceState: str
        :param _ExitCode: Exit code after application execution is completed
Note: This field may return `null`, indicating that no valid value was found.
        :type ExitCode: int
        :param _StateReason: Task instance state reason. If the task instance fails, the reason for the failure will be logged.
        :type StateReason: str
        :param _ComputeNodeInstanceId: The `InstanceId` of the compute node (e.g., CVM instance) where the task instance is running. This field is empty if the task instance is not running or has already been completed and will change when the task instance is retried.
Note: This field may return `null`, indicating that no valid value was found.
        :type ComputeNodeInstanceId: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _LaunchTime: Start time
Note: This field may return `null`, indicating that no valid value was found.
        :type LaunchTime: str
        :param _RunningTime: Running start time
Note: This field may return `null`, indicating that no valid value was found.
        :type RunningTime: str
        :param _EndTime: Task end time
Note: This field may return `null`, indicating that no valid value was found.
        :type EndTime: str
        :param _RedirectInfo: Redirection information
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param _StateDetailedReason: Task instance state reason details. If the task instance fails, the reason for the failure will be logged
        :type StateDetailedReason: str
        """
        self._TaskInstanceIndex = None
        self._TaskInstanceState = None
        self._ExitCode = None
        self._StateReason = None
        self._ComputeNodeInstanceId = None
        self._CreateTime = None
        self._LaunchTime = None
        self._RunningTime = None
        self._EndTime = None
        self._RedirectInfo = None
        self._StateDetailedReason = None

    @property
    def TaskInstanceIndex(self):
        """Task instance index
        :rtype: int
        """
        return self._TaskInstanceIndex

    @TaskInstanceIndex.setter
    def TaskInstanceIndex(self, TaskInstanceIndex):
        self._TaskInstanceIndex = TaskInstanceIndex

    @property
    def TaskInstanceState(self):
        """Task instance state
        :rtype: str
        """
        return self._TaskInstanceState

    @TaskInstanceState.setter
    def TaskInstanceState(self, TaskInstanceState):
        self._TaskInstanceState = TaskInstanceState

    @property
    def ExitCode(self):
        """Exit code after application execution is completed
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: int
        """
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode

    @property
    def StateReason(self):
        """Task instance state reason. If the task instance fails, the reason for the failure will be logged.
        :rtype: str
        """
        return self._StateReason

    @StateReason.setter
    def StateReason(self, StateReason):
        self._StateReason = StateReason

    @property
    def ComputeNodeInstanceId(self):
        """The `InstanceId` of the compute node (e.g., CVM instance) where the task instance is running. This field is empty if the task instance is not running or has already been completed and will change when the task instance is retried.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._ComputeNodeInstanceId

    @ComputeNodeInstanceId.setter
    def ComputeNodeInstanceId(self, ComputeNodeInstanceId):
        self._ComputeNodeInstanceId = ComputeNodeInstanceId

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
    def LaunchTime(self):
        """Start time
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._LaunchTime

    @LaunchTime.setter
    def LaunchTime(self, LaunchTime):
        self._LaunchTime = LaunchTime

    @property
    def RunningTime(self):
        """Running start time
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._RunningTime

    @RunningTime.setter
    def RunningTime(self, RunningTime):
        self._RunningTime = RunningTime

    @property
    def EndTime(self):
        """Task end time
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RedirectInfo(self):
        """Redirection information
        :rtype: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        """
        return self._RedirectInfo

    @RedirectInfo.setter
    def RedirectInfo(self, RedirectInfo):
        self._RedirectInfo = RedirectInfo

    @property
    def StateDetailedReason(self):
        """Task instance state reason details. If the task instance fails, the reason for the failure will be logged
        :rtype: str
        """
        return self._StateDetailedReason

    @StateDetailedReason.setter
    def StateDetailedReason(self, StateDetailedReason):
        self._StateDetailedReason = StateDetailedReason


    def _deserialize(self, params):
        self._TaskInstanceIndex = params.get("TaskInstanceIndex")
        self._TaskInstanceState = params.get("TaskInstanceState")
        self._ExitCode = params.get("ExitCode")
        self._StateReason = params.get("StateReason")
        self._ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self._CreateTime = params.get("CreateTime")
        self._LaunchTime = params.get("LaunchTime")
        self._RunningTime = params.get("RunningTime")
        self._EndTime = params.get("EndTime")
        if params.get("RedirectInfo") is not None:
            self._RedirectInfo = RedirectInfo()
            self._RedirectInfo._deserialize(params.get("RedirectInfo"))
        self._StateDetailedReason = params.get("StateDetailedReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskMetrics(AbstractModel):
    """Task statistical metrics

    """

    def __init__(self):
        r"""
        :param _SubmittedCount: Number of submitted tasks
        :type SubmittedCount: int
        :param _PendingCount: Number of pending tasks
        :type PendingCount: int
        :param _RunnableCount: Number of Runnable tasks
        :type RunnableCount: int
        :param _StartingCount: Number of starting tasks
        :type StartingCount: int
        :param _RunningCount: Number of running tasks
        :type RunningCount: int
        :param _SucceedCount: Number of successful tasks
        :type SucceedCount: int
        :param _FailedInterruptedCount: Number of failed and interrupted tasks
        :type FailedInterruptedCount: int
        :param _FailedCount: Failed count
        :type FailedCount: int
        """
        self._SubmittedCount = None
        self._PendingCount = None
        self._RunnableCount = None
        self._StartingCount = None
        self._RunningCount = None
        self._SucceedCount = None
        self._FailedInterruptedCount = None
        self._FailedCount = None

    @property
    def SubmittedCount(self):
        """Number of submitted tasks
        :rtype: int
        """
        return self._SubmittedCount

    @SubmittedCount.setter
    def SubmittedCount(self, SubmittedCount):
        self._SubmittedCount = SubmittedCount

    @property
    def PendingCount(self):
        """Number of pending tasks
        :rtype: int
        """
        return self._PendingCount

    @PendingCount.setter
    def PendingCount(self, PendingCount):
        self._PendingCount = PendingCount

    @property
    def RunnableCount(self):
        """Number of Runnable tasks
        :rtype: int
        """
        return self._RunnableCount

    @RunnableCount.setter
    def RunnableCount(self, RunnableCount):
        self._RunnableCount = RunnableCount

    @property
    def StartingCount(self):
        """Number of starting tasks
        :rtype: int
        """
        return self._StartingCount

    @StartingCount.setter
    def StartingCount(self, StartingCount):
        self._StartingCount = StartingCount

    @property
    def RunningCount(self):
        """Number of running tasks
        :rtype: int
        """
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def SucceedCount(self):
        """Number of successful tasks
        :rtype: int
        """
        return self._SucceedCount

    @SucceedCount.setter
    def SucceedCount(self, SucceedCount):
        self._SucceedCount = SucceedCount

    @property
    def FailedInterruptedCount(self):
        """Number of failed and interrupted tasks
        :rtype: int
        """
        return self._FailedInterruptedCount

    @FailedInterruptedCount.setter
    def FailedInterruptedCount(self, FailedInterruptedCount):
        self._FailedInterruptedCount = FailedInterruptedCount

    @property
    def FailedCount(self):
        """Failed count
        :rtype: int
        """
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount


    def _deserialize(self, params):
        self._SubmittedCount = params.get("SubmittedCount")
        self._PendingCount = params.get("PendingCount")
        self._RunnableCount = params.get("RunnableCount")
        self._StartingCount = params.get("StartingCount")
        self._RunningCount = params.get("RunningCount")
        self._SucceedCount = params.get("SucceedCount")
        self._FailedInterruptedCount = params.get("FailedInterruptedCount")
        self._FailedCount = params.get("FailedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskTemplateView(AbstractModel):
    """Task template information

    """

    def __init__(self):
        r"""
        :param _TaskTemplateId: Task template ID
        :type TaskTemplateId: str
        :param _TaskTemplateName: Task template name
        :type TaskTemplateName: str
        :param _TaskTemplateDescription: Task template description
        :type TaskTemplateDescription: str
        :param _TaskTemplateInfo: Task template information
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Tags: Tag list bound to the task template.
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self._TaskTemplateId = None
        self._TaskTemplateName = None
        self._TaskTemplateDescription = None
        self._TaskTemplateInfo = None
        self._CreateTime = None
        self._Tags = None

    @property
    def TaskTemplateId(self):
        """Task template ID
        :rtype: str
        """
        return self._TaskTemplateId

    @TaskTemplateId.setter
    def TaskTemplateId(self, TaskTemplateId):
        self._TaskTemplateId = TaskTemplateId

    @property
    def TaskTemplateName(self):
        """Task template name
        :rtype: str
        """
        return self._TaskTemplateName

    @TaskTemplateName.setter
    def TaskTemplateName(self, TaskTemplateName):
        self._TaskTemplateName = TaskTemplateName

    @property
    def TaskTemplateDescription(self):
        """Task template description
        :rtype: str
        """
        return self._TaskTemplateDescription

    @TaskTemplateDescription.setter
    def TaskTemplateDescription(self, TaskTemplateDescription):
        self._TaskTemplateDescription = TaskTemplateDescription

    @property
    def TaskTemplateInfo(self):
        """Task template information
        :rtype: :class:`tencentcloud.batch.v20170312.models.Task`
        """
        return self._TaskTemplateInfo

    @TaskTemplateInfo.setter
    def TaskTemplateInfo(self, TaskTemplateInfo):
        self._TaskTemplateInfo = TaskTemplateInfo

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
    def Tags(self):
        """Tag list bound to the task template.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TaskTemplateId = params.get("TaskTemplateId")
        self._TaskTemplateName = params.get("TaskTemplateName")
        self._TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self._TaskTemplateInfo = Task()
            self._TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self._CreateTime = params.get("CreateTime")
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
        


class TaskView(AbstractModel):
    """Task view information

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name
        :type TaskName: str
        :param _TaskState: Task status
        :type TaskState: str
        :param _CreateTime: Start time
        :type CreateTime: str
        :param _EndTime: End time
Note: This field may return `null`, indicating that no valid value was found.
        :type EndTime: str
        """
        self._TaskName = None
        self._TaskState = None
        self._CreateTime = None
        self._EndTime = None

    @property
    def TaskName(self):
        """Task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskState(self):
        """Task status
        :rtype: str
        """
        return self._TaskState

    @TaskState.setter
    def TaskState(self, TaskState):
        self._TaskState = TaskState

    @property
    def CreateTime(self):
        """Start time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EndTime(self):
        """End time
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._TaskState = params.get("TaskState")
        self._CreateTime = params.get("CreateTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodeRequest(AbstractModel):
    """TerminateComputeNode request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _ComputeNodeId: Compute node ID
        :type ComputeNodeId: str
        """
        self._EnvId = None
        self._ComputeNodeId = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ComputeNodeId(self):
        """Compute node ID
        :rtype: str
        """
        return self._ComputeNodeId

    @ComputeNodeId.setter
    def ComputeNodeId(self, ComputeNodeId):
        self._ComputeNodeId = ComputeNodeId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ComputeNodeId = params.get("ComputeNodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodeResponse(AbstractModel):
    """TerminateComputeNode response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TerminateComputeNodesRequest(AbstractModel):
    """TerminateComputeNodes request structure.

    """

    def __init__(self):
        r"""
        :param _EnvId: Compute environment ID
        :type EnvId: str
        :param _ComputeNodeIds: List of compute node IDs
        :type ComputeNodeIds: list of str
        """
        self._EnvId = None
        self._ComputeNodeIds = None

    @property
    def EnvId(self):
        """Compute environment ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def ComputeNodeIds(self):
        """List of compute node IDs
        :rtype: list of str
        """
        return self._ComputeNodeIds

    @ComputeNodeIds.setter
    def ComputeNodeIds(self, ComputeNodeIds):
        self._ComputeNodeIds = ComputeNodeIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._ComputeNodeIds = params.get("ComputeNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateComputeNodesResponse(AbstractModel):
    """TerminateComputeNodes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TerminateJobRequest(AbstractModel):
    """TerminateJob request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateJobResponse(AbstractModel):
    """TerminateJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TerminateTaskInstanceRequest(AbstractModel):
    """TerminateTaskInstance request structure.

    """

    def __init__(self):
        r"""
        :param _JobId: Job ID
        :type JobId: str
        :param _TaskName: Task name
        :type TaskName: str
        :param _TaskInstanceIndex: Task instance index
        :type TaskInstanceIndex: int
        """
        self._JobId = None
        self._TaskName = None
        self._TaskInstanceIndex = None

    @property
    def JobId(self):
        """Job ID
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def TaskName(self):
        """Task name
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def TaskInstanceIndex(self):
        """Task instance index
        :rtype: int
        """
        return self._TaskInstanceIndex

    @TaskInstanceIndex.setter
    def TaskInstanceIndex(self, TaskInstanceIndex):
        self._TaskInstanceIndex = TaskInstanceIndex


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._TaskName = params.get("TaskName")
        self._TaskInstanceIndex = params.get("TaskInstanceIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateTaskInstanceResponse(AbstractModel):
    """TerminateTaskInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
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
        :param _AsVpcGateway: Whether it is used as a public gateway. A public gateway can only be used normally when an instance has a public IP address and is in a VPC. Valid values:<li>true: It is used as a public gateway.</li><li>false: It is not used as a public gateway.</li>Default value: false.
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
        """VPC ID in the format of `vpc-xxx`. To obtain valid VPC IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/vpc?rid=1) or call the [DescribeVpcEx](https://intl.cloud.tencent.com/document/api/215/1372?from_cn_redirect=1) API and look for the `unVpcId` fields in the response. If you specify `DEFAULT` for both `VpcId` and `SubnetId` when creating an instance, the default VPC will be used.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """VPC subnet ID in the format `subnet-xxx`. To obtain valid subnet IDs, you can log in to the [console](https://console.cloud.tencent.com/vpc/subnet?rid=1) or call [DescribeSubnets](https://intl.cloud.tencent.com/document/api/215/15784?from_cn_redirect=1) and look for the `unSubnetId` fields in the response. If you specify `DEFAULT` for both `SubnetId` and `VpcId` when creating an instance, the default VPC will be used.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AsVpcGateway(self):
        """Whether it is used as a public gateway. A public gateway can only be used normally when an instance has a public IP address and is in a VPC. Valid values:<li>true: It is used as a public gateway.</li><li>false: It is not used as a public gateway.</li>Default value: false.
        :rtype: bool
        """
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        """Array of VPC subnet IPs. You can use this parameter when creating instances or modifying VPC attributes of instances. Currently you can specify multiple IPs in one subnet only when creating multiple instances at the same time.
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        """Number of IPv6 addresses randomly generated for the ENI.
        :rtype: int
        """
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
        