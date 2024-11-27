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


class AutomationAgentInfo(AbstractModel):
    """TAT agent information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Version: Agent version.
        :type Version: str
        :param _LastHeartbeatTime: Last heartbeat time
        :type LastHeartbeatTime: str
        :param _AgentStatus: Agent status. Valid values:
<li> `Online`
<li> `Offline`
        :type AgentStatus: str
        :param _Environment: Agent runtime environment. Valid values:
<li> `Linux`: Linux instance
<li> `Windows`: Windows instance
        :type Environment: str
        :param _SupportFeatures: Features supported by the TAT agent.
        :type SupportFeatures: list of str
        """
        self._InstanceId = None
        self._Version = None
        self._LastHeartbeatTime = None
        self._AgentStatus = None
        self._Environment = None
        self._SupportFeatures = None

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
    def Version(self):
        """Agent version.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LastHeartbeatTime(self):
        """Last heartbeat time
        :rtype: str
        """
        return self._LastHeartbeatTime

    @LastHeartbeatTime.setter
    def LastHeartbeatTime(self, LastHeartbeatTime):
        self._LastHeartbeatTime = LastHeartbeatTime

    @property
    def AgentStatus(self):
        """Agent status. Valid values:
<li> `Online`
<li> `Offline`
        :rtype: str
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def Environment(self):
        """Agent runtime environment. Valid values:
<li> `Linux`: Linux instance
<li> `Windows`: Windows instance
        :rtype: str
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def SupportFeatures(self):
        """Features supported by the TAT agent.
        :rtype: list of str
        """
        return self._SupportFeatures

    @SupportFeatures.setter
    def SupportFeatures(self, SupportFeatures):
        self._SupportFeatures = SupportFeatures


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Version = params.get("Version")
        self._LastHeartbeatTime = params.get("LastHeartbeatTime")
        self._AgentStatus = params.get("AgentStatus")
        self._Environment = params.get("Environment")
        self._SupportFeatures = params.get("SupportFeatures")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInvocationRequest(AbstractModel):
    """CancelInvocation request structure.

    """

    def __init__(self):
        r"""
        :param _InvocationId: Execution activity ID
        :type InvocationId: str
        :param _InstanceIds: Instance ID list. A maximum of 100 IDs are allowed. Supported instance types:
<li> `CVM`
<li> `LIGHTHOUSE`
        :type InstanceIds: list of str
        """
        self._InvocationId = None
        self._InstanceIds = None

    @property
    def InvocationId(self):
        """Execution activity ID
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InstanceIds(self):
        """Instance ID list. A maximum of 100 IDs are allowed. Supported instance types:
<li> `CVM`
<li> `LIGHTHOUSE`
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InvocationId = params.get("InvocationId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInvocationResponse(AbstractModel):
    """CancelInvocation response structure.

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


class Command(AbstractModel):
    """Command details.

    """

    def __init__(self):
        r"""
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _CommandName: Command name.
        :type CommandName: str
        :param _Description: Command description.
        :type Description: str
        :param _Content: Base64-encoded command.
        :type Content: str
        :param _CommandType: Command type.
        :type CommandType: str
        :param _WorkingDirectory: Command execution path.
        :type WorkingDirectory: str
        :param _Timeout: Command timeout period.
        :type Timeout: int
        :param _CreatedTime: Command creation time.
        :type CreatedTime: str
        :param _UpdatedTime: Command update time.
        :type UpdatedTime: str
        :param _EnableParameter: Whether to enable the custom parameter feature.
        :type EnableParameter: bool
        :param _DefaultParameters: Default custom parameter value.
        :type DefaultParameters: str
        :param _FormattedDescription: Formatted description of the command. This parameter is an empty string for user commands and contains values for public commands.
        :type FormattedDescription: str
        :param _CreatedBy: Command creator. `TAT` indicates a public command and `USER` indicates a personal command.
        :type CreatedBy: str
        :param _Tags: The list of tags bound to the command.
        :type Tags: list of Tag
        :param _Username: The user who executes the command on the instance.
        :type Username: str
        :param _OutputCOSBucketUrl: The COS bucket URL for uploading logs.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: The COS bucket directory where the logs are saved.
        :type OutputCOSKeyPrefix: str
        """
        self._CommandId = None
        self._CommandName = None
        self._Description = None
        self._Content = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._EnableParameter = None
        self._DefaultParameters = None
        self._FormattedDescription = None
        self._CreatedBy = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CommandName(self):
        """Command name.
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        """Command description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        """Base64-encoded command.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        """Command type.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """Command execution path.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """Command timeout period.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def CreatedTime(self):
        """Command creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """Command update time.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def EnableParameter(self):
        """Whether to enable the custom parameter feature.
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        """Default custom parameter value.
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def FormattedDescription(self):
        """Formatted description of the command. This parameter is an empty string for user commands and contains values for public commands.
        :rtype: str
        """
        return self._FormattedDescription

    @FormattedDescription.setter
    def FormattedDescription(self, FormattedDescription):
        self._FormattedDescription = FormattedDescription

    @property
    def CreatedBy(self):
        """Command creator. `TAT` indicates a public command and `USER` indicates a personal command.
        :rtype: str
        """
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def Tags(self):
        """The list of tags bound to the command.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        """The user who executes the command on the instance.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """The COS bucket URL for uploading logs.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """The COS bucket directory where the logs are saved.
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._CommandName = params.get("CommandName")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._EnableParameter = params.get("EnableParameter")
        self._DefaultParameters = params.get("DefaultParameters")
        self._FormattedDescription = params.get("FormattedDescription")
        self._CreatedBy = params.get("CreatedBy")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommandDocument(AbstractModel):
    """Command execution details.

    """

    def __init__(self):
        r"""
        :param _Content: Base64-encoded command.
        :type Content: str
        :param _CommandType: Command type.
        :type CommandType: str
        :param _Timeout: Timeout period.
        :type Timeout: int
        :param _WorkingDirectory: Execution path.
        :type WorkingDirectory: str
        :param _Username: The user who executes the command.
        :type Username: str
        :param _OutputCOSBucketUrl: URL of the COS bucket to store the output
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: Prefix of the output file name 
        :type OutputCOSKeyPrefix: str
        """
        self._Content = None
        self._CommandType = None
        self._Timeout = None
        self._WorkingDirectory = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def Content(self):
        """Base64-encoded command.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        """Command type.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def Timeout(self):
        """Timeout period.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def WorkingDirectory(self):
        """Execution path.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Username(self):
        """The user who executes the command.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """URL of the COS bucket to store the output
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """Prefix of the output file name 
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._CommandType = params.get("CommandType")
        self._Timeout = params.get("Timeout")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandRequest(AbstractModel):
    """CreateCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param _Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param _Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param _CommandType: Command type. `SHELL` and `POWERSHELL` are supported. The default value is `SHELL`.
        :type CommandType: str
        :param _WorkingDirectory: Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :type WorkingDirectory: str
        :param _Timeout: Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :type Timeout: int
        :param _EnableParameter: Whether to enable the custom parameter feature.
This cannot be modified once created.
Default value: `false`.
        :type EnableParameter: bool
        :param _DefaultParameters: The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided in the `InvokeCommand` API, the default value is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type DefaultParameters: str
        :param _Tags: Tags bound to the command. At most 10 tags are allowed.
        :type Tags: list of Tag
        :param _Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the root user is used to execute commands on Linux and the System user is used on Windows.
        :type Username: str
        :param _OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. Consecutive dots (.) and slashes (/) are not allowed. It can not start with a slash (/). 
        :type OutputCOSKeyPrefix: str
        """
        self._CommandName = None
        self._Content = None
        self._Description = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._EnableParameter = None
        self._DefaultParameters = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandName(self):
        """Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Content(self):
        """Base64-encoded command. The maximum length is 64 KB.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        """Command description. The maximum length is 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CommandType(self):
        """Command type. `SHELL` and `POWERSHELL` are supported. The default value is `SHELL`.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def EnableParameter(self):
        """Whether to enable the custom parameter feature.
This cannot be modified once created.
Default value: `false`.
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        """The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided in the `InvokeCommand` API, the default value is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def Tags(self):
        """Tags bound to the command. At most 10 tags are allowed.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        """The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the root user is used to execute commands on Linux and the System user is used on Windows.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. Consecutive dots (.) and slashes (/) are not allowed. It can not start with a slash (/). 
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandName = params.get("CommandName")
        self._Content = params.get("Content")
        self._Description = params.get("Description")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._EnableParameter = params.get("EnableParameter")
        self._DefaultParameters = params.get("DefaultParameters")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandResponse(AbstractModel):
    """CreateCommand response structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CommandId = None
        self._RequestId = None

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

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
        self._CommandId = params.get("CommandId")
        self._RequestId = params.get("RequestId")


class CreateInvokerRequest(AbstractModel):
    """CreateInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Invoker name.
        :type Name: str
        :param _Type: Invoker type. It can only be `SCHEDULE` (recurring invokers).
        :type Type: str
        :param _CommandId: Remote command ID.
        :type CommandId: str
        :param _InstanceIds: ID of the instance bound to the trigger. Up to 100 IDs are allowed.
        :type InstanceIds: list of str
        :param _Username: The user who executes the command.
        :type Username: str
        :param _Parameters: Custom parameters of the command.
        :type Parameters: str
        :param _ScheduleSettings: Settings required for a recurring invoker.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        self._Name = None
        self._Type = None
        self._CommandId = None
        self._InstanceIds = None
        self._Username = None
        self._Parameters = None
        self._ScheduleSettings = None

    @property
    def Name(self):
        """Invoker name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Invoker type. It can only be `SCHEDULE` (recurring invokers).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        """Remote command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InstanceIds(self):
        """ID of the instance bound to the trigger. Up to 100 IDs are allowed.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Username(self):
        """The user who executes the command.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        """Custom parameters of the command.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def ScheduleSettings(self):
        """Settings required for a recurring invoker.
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CommandId = params.get("CommandId")
        self._InstanceIds = params.get("InstanceIds")
        self._Username = params.get("Username")
        self._Parameters = params.get("Parameters")
        if params.get("ScheduleSettings") is not None:
            self._ScheduleSettings = ScheduleSettings()
            self._ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvokerResponse(AbstractModel):
    """CreateInvoker response structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Invoker ID.
        :type InvokerId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvokerId = None
        self._RequestId = None

    @property
    def InvokerId(self):
        """Invoker ID.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

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
        self._InvokerId = params.get("InvokerId")
        self._RequestId = params.get("RequestId")


class DeleteCommandRequest(AbstractModel):
    """DeleteCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: ID of the command to be deleted.
        :type CommandId: str
        """
        self._CommandId = None

    @property
    def CommandId(self):
        """ID of the command to be deleted.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandResponse(AbstractModel):
    """DeleteCommand response structure.

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


class DeleteInvokerRequest(AbstractModel):
    """DeleteInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: ID of the invoker to be deleted.
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        """ID of the invoker to be deleted.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInvokerResponse(AbstractModel):
    """DeleteInvoker response structure.

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


class DescribeAutomationAgentStatusRequest(AbstractModel):
    """DescribeAutomationAgentStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance IDs for the query.
        :type InstanceIds: list of str
        :param _Filters: Filter conditions.<br> <li>`agent-status` - String - Required: No - (Filter condition) Filter by agent status. Valid values: `Online`, `Offline`.<br> <li> `environment` - String - Required: No - (Filter condition) Filter by the agent environment. Valid value: `Linux`.<br> <li> `instance-id` - String - Required: No - (Filter condition) Filter by the instance ID. <br>Up to 10 `Filters` allowed in one request. For each filter, five `Filter.Values` can be specified. `InstanceIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceIds(self):
        """List of instance IDs for the query.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        """Filter conditions.<br> <li>`agent-status` - String - Required: No - (Filter condition) Filter by agent status. Valid values: `Online`, `Offline`.<br> <li> `environment` - String - Required: No - (Filter condition) Filter by the agent environment. Valid value: `Linux`.<br> <li> `instance-id` - String - Required: No - (Filter condition) Filter by the instance ID. <br>Up to 10 `Filters` allowed in one request. For each filter, five `Filter.Values` can be specified. `InstanceIds` and `Filters` cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
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
        


class DescribeAutomationAgentStatusResponse(AbstractModel):
    """DescribeAutomationAgentStatus response structure.

    """

    def __init__(self):
        r"""
        :param _AutomationAgentSet: Agent information list.
        :type AutomationAgentSet: list of AutomationAgentInfo
        :param _TotalCount: Total number of matching agents.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AutomationAgentSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutomationAgentSet(self):
        """Agent information list.
        :rtype: list of AutomationAgentInfo
        """
        return self._AutomationAgentSet

    @AutomationAgentSet.setter
    def AutomationAgentSet(self, AutomationAgentSet):
        self._AutomationAgentSet = AutomationAgentSet

    @property
    def TotalCount(self):
        """Total number of matching agents.
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
        if params.get("AutomationAgentSet") is not None:
            self._AutomationAgentSet = []
            for item in params.get("AutomationAgentSet"):
                obj = AutomationAgentInfo()
                obj._deserialize(item)
                self._AutomationAgentSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCommandsRequest(AbstractModel):
    """DescribeCommands request structure.

    """

    def __init__(self):
        r"""
        :param _CommandIds: List of command IDs. Up to 100 IDs are allowed for each request. `CommandIds` and `Filters` cannot be specified at the same time.
        :type CommandIds: list of str
        :param _Filters: Filter conditions.
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID.
<li> `command-name` - String - Required: No - (Filter condition) Filter by the command name.
<li> `command-type` - String - Required: No - (Filter condition) Filter by the command type. Valid values: `SHELL` or `POWERSHELL`.
<li> `created-by` - String - Required: No - (Filter condition) Filter by the creator. Valid values: `TAT` (public commands) or `USER` (custom commands).
<li> `tag-key` - String - Required: No - (Filter condition) Filter by the tag key.</li>
<li> `tag-value` - String - Required: No - (Filter condition) Filter by the tag value.</li>
<li> `tag:tag-key` - String - Required: No - (Filter) Filter by the tag key-value pair. The tag-key should be replaced with a specified tag key. For detailed usage, see sample 4.</li>

Up to 10 `Filters` are allowed in one request. Each filter can have up to 5 `Filter.Values`. `CommandIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._CommandIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def CommandIds(self):
        """List of command IDs. Up to 100 IDs are allowed for each request. `CommandIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._CommandIds

    @CommandIds.setter
    def CommandIds(self, CommandIds):
        self._CommandIds = CommandIds

    @property
    def Filters(self):
        """Filter conditions.
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID.
<li> `command-name` - String - Required: No - (Filter condition) Filter by the command name.
<li> `command-type` - String - Required: No - (Filter condition) Filter by the command type. Valid values: `SHELL` or `POWERSHELL`.
<li> `created-by` - String - Required: No - (Filter condition) Filter by the creator. Valid values: `TAT` (public commands) or `USER` (custom commands).
<li> `tag-key` - String - Required: No - (Filter condition) Filter by the tag key.</li>
<li> `tag-value` - String - Required: No - (Filter condition) Filter by the tag value.</li>
<li> `tag:tag-key` - String - Required: No - (Filter) Filter by the tag key-value pair. The tag-key should be replaced with a specified tag key. For detailed usage, see sample 4.</li>

Up to 10 `Filters` are allowed in one request. Each filter can have up to 5 `Filter.Values`. `CommandIds` and `Filters` cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._CommandIds = params.get("CommandIds")
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
        


class DescribeCommandsResponse(AbstractModel):
    """DescribeCommands response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of matching commands.
        :type TotalCount: int
        :param _CommandSet: List of command details.
        :type CommandSet: list of Command
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._CommandSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of matching commands.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CommandSet(self):
        """List of command details.
        :rtype: list of Command
        """
        return self._CommandSet

    @CommandSet.setter
    def CommandSet(self, CommandSet):
        self._CommandSet = CommandSet

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
        if params.get("CommandSet") is not None:
            self._CommandSet = []
            for item in params.get("CommandSet"):
                obj = Command()
                obj._deserialize(item)
                self._CommandSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvocationTasksRequest(AbstractModel):
    """DescribeInvocationTasks request structure.

    """

    def __init__(self):
        r"""
        :param _InvocationTaskIds: List of execution task IDs. Up to 100 IDs are allowed for each request. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :type InvocationTaskIds: list of str
        :param _Filters: Filter conditions.<br> <li> `invocation-id` - String - Required: No - (Filter condition) Filter by the execution activity ID.<br> <li> `invocation-task-id` - String - Required: No - (Filter condition) Filter by the execution task ID.<br> <li> `instance-id` - String - Required: No - (Filter condition) Filter by the instance ID. <br> <li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID. <br>Up to 10 `Filters` are allowed for each request. Each filter can have up to five `Filter.Values`. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _HideOutput: Whether to hide the output. Valid values:<br><li>`True` (default): Hide the output <br><li>`False`: Show the output <br>
        :type HideOutput: bool
        """
        self._InvocationTaskIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._HideOutput = None

    @property
    def InvocationTaskIds(self):
        """List of execution task IDs. Up to 100 IDs are allowed for each request. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._InvocationTaskIds

    @InvocationTaskIds.setter
    def InvocationTaskIds(self, InvocationTaskIds):
        self._InvocationTaskIds = InvocationTaskIds

    @property
    def Filters(self):
        """Filter conditions.<br> <li> `invocation-id` - String - Required: No - (Filter condition) Filter by the execution activity ID.<br> <li> `invocation-task-id` - String - Required: No - (Filter condition) Filter by the execution task ID.<br> <li> `instance-id` - String - Required: No - (Filter condition) Filter by the instance ID. <br> <li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID. <br>Up to 10 `Filters` are allowed for each request. Each filter can have up to five `Filter.Values`. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def HideOutput(self):
        """Whether to hide the output. Valid values:<br><li>`True` (default): Hide the output <br><li>`False`: Show the output <br>
        :rtype: bool
        """
        return self._HideOutput

    @HideOutput.setter
    def HideOutput(self, HideOutput):
        self._HideOutput = HideOutput


    def _deserialize(self, params):
        self._InvocationTaskIds = params.get("InvocationTaskIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._HideOutput = params.get("HideOutput")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationTasksResponse(AbstractModel):
    """DescribeInvocationTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of matching execution tasks.
        :type TotalCount: int
        :param _InvocationTaskSet: List of execution tasks.
        :type InvocationTaskSet: list of InvocationTask
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvocationTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of matching execution tasks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvocationTaskSet(self):
        """List of execution tasks.
        :rtype: list of InvocationTask
        """
        return self._InvocationTaskSet

    @InvocationTaskSet.setter
    def InvocationTaskSet(self, InvocationTaskSet):
        self._InvocationTaskSet = InvocationTaskSet

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
        if params.get("InvocationTaskSet") is not None:
            self._InvocationTaskSet = []
            for item in params.get("InvocationTaskSet"):
                obj = InvocationTask()
                obj._deserialize(item)
                self._InvocationTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvocationsRequest(AbstractModel):
    """DescribeInvocations request structure.

    """

    def __init__(self):
        r"""
        :param _InvocationIds: List of execution activity IDs. Up to 100 IDs are allowed for each request. `InvocationIds` and `Filters` cannot be specified at the same time.
        :type InvocationIds: list of str
        :param _Filters: Filter conditions.<br> <li> `invocation-id` - String - Required: No - (Filter condition) Filter by the execution activity ID.<br> 
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID. 
<li> `command-created-by` - String - Required: No - (Filter condition) Filter by the command type. Valid values: `TAT` (public commands) or `USER` (custom commands).
<li> `instance-kind` - String - Required: No - (Filter condition) Filter by the instance type. Valid values: `CVM` or `LIGHTHOUSE`. 
<br>Up to 10 `Filters` are allowed for each request. Each filter can have up to five `Filter.Values`. `InvocationIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._InvocationIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def InvocationIds(self):
        """List of execution activity IDs. Up to 100 IDs are allowed for each request. `InvocationIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._InvocationIds

    @InvocationIds.setter
    def InvocationIds(self, InvocationIds):
        self._InvocationIds = InvocationIds

    @property
    def Filters(self):
        """Filter conditions.<br> <li> `invocation-id` - String - Required: No - (Filter condition) Filter by the execution activity ID.<br> 
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID. 
<li> `command-created-by` - String - Required: No - (Filter condition) Filter by the command type. Valid values: `TAT` (public commands) or `USER` (custom commands).
<li> `instance-kind` - String - Required: No - (Filter condition) Filter by the instance type. Valid values: `CVM` or `LIGHTHOUSE`. 
<br>Up to 10 `Filters` are allowed for each request. Each filter can have up to five `Filter.Values`. `InvocationIds` and `Filters` cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InvocationIds = params.get("InvocationIds")
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
        


class DescribeInvocationsResponse(AbstractModel):
    """DescribeInvocations response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of matching execution activities.
        :type TotalCount: int
        :param _InvocationSet: List of execution activities.
        :type InvocationSet: list of Invocation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvocationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of matching execution activities.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvocationSet(self):
        """List of execution activities.
        :rtype: list of Invocation
        """
        return self._InvocationSet

    @InvocationSet.setter
    def InvocationSet(self, InvocationSet):
        self._InvocationSet = InvocationSet

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
        if params.get("InvocationSet") is not None:
            self._InvocationSet = []
            for item in params.get("InvocationSet"):
                obj = Invocation()
                obj._deserialize(item)
                self._InvocationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvokerRecordsRequest(AbstractModel):
    """DescribeInvokerRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerIds: List of invoker IDs. Up to 100 IDs are allowed.
        :type InvokerIds: list of str
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._InvokerIds = None
        self._Limit = None
        self._Offset = None

    @property
    def InvokerIds(self):
        """List of invoker IDs. Up to 100 IDs are allowed.
        :rtype: list of str
        """
        return self._InvokerIds

    @InvokerIds.setter
    def InvokerIds(self, InvokerIds):
        self._InvokerIds = InvokerIds

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InvokerIds = params.get("InvokerIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvokerRecordsResponse(AbstractModel):
    """DescribeInvokerRecords response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of matching records.
        :type TotalCount: int
        :param _InvokerRecordSet: Execution history of an invoker.
        :type InvokerRecordSet: list of InvokerRecord
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvokerRecordSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of matching records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvokerRecordSet(self):
        """Execution history of an invoker.
        :rtype: list of InvokerRecord
        """
        return self._InvokerRecordSet

    @InvokerRecordSet.setter
    def InvokerRecordSet(self, InvokerRecordSet):
        self._InvokerRecordSet = InvokerRecordSet

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
        if params.get("InvokerRecordSet") is not None:
            self._InvokerRecordSet = []
            for item in params.get("InvokerRecordSet"):
                obj = InvokerRecord()
                obj._deserialize(item)
                self._InvokerRecordSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvokersRequest(AbstractModel):
    """DescribeInvokers request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerIds: List of invoker IDs.
        :type InvokerIds: list of str
        :param _Filters: Filter conditions:

<li> `invoker-id` - String - Required: No - (Filter condition) Filter by the invoker ID.
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID.
<li> `type` - String - Required: No - (Filter condition) Filter by the invoker type.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self._InvokerIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def InvokerIds(self):
        """List of invoker IDs.
        :rtype: list of str
        """
        return self._InvokerIds

    @InvokerIds.setter
    def InvokerIds(self, InvokerIds):
        self._InvokerIds = InvokerIds

    @property
    def Filters(self):
        """Filter conditions:

<li> `invoker-id` - String - Required: No - (Filter condition) Filter by the invoker ID.
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID.
<li> `type` - String - Required: No - (Filter condition) Filter by the invoker type.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """Number of returned results. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InvokerIds = params.get("InvokerIds")
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
        


class DescribeInvokersResponse(AbstractModel):
    """DescribeInvokers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of matching invokers.
        :type TotalCount: int
        :param _InvokerSet: Invoker information.
        :type InvokerSet: list of Invoker
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvokerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of matching invokers.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvokerSet(self):
        """Invoker information.
        :rtype: list of Invoker
        """
        return self._InvokerSet

    @InvokerSet.setter
    def InvokerSet(self, InvokerSet):
        self._InvokerSet = InvokerSet

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
        if params.get("InvokerSet") is not None:
            self._InvokerSet = []
            for item in params.get("InvokerSet"):
                obj = Invoker()
                obj._deserialize(item)
                self._InvokerSet.append(obj)
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
        :param _RegionSet: Region information list
        :type RegionSet: list of RegionInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of regions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        """Region information list
        :rtype: list of RegionInfo
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
        self._TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisableInvokerRequest(AbstractModel):
    """DisableInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: ID of the invoker to be disabled.
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        """ID of the invoker to be disabled.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInvokerResponse(AbstractModel):
    """DisableInvoker response structure.

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


class EnableInvokerRequest(AbstractModel):
    """EnableInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: ID of the invoker to be enabled.
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        """ID of the invoker to be enabled.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableInvokerResponse(AbstractModel):
    """EnableInvoker response structure.

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


class Filter(AbstractModel):
    """> Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.
    > * If there are multiple `Filter` parameters, the relationship among them is the logical `AND`.
    > * If there are multiple `Values` for the same `Filter`, the relationship among the `Values` for the same `Filter` is the logical `OR`.
    >
    > Take the [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) API as an example. You can use the following filters to query the instances whose availability zone (`zone`) is Guangzhou 1 ***and*** billing method (`instance-charge-type`) is prepaid ***or*** pay-as-you-go:
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        r"""
        :param _Name: Field to be filtered.
        :type Name: str
        :param _Values: Filter values of the field.
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Field to be filtered.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filter values of the field.
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
        


class Invocation(AbstractModel):
    """Execution activity details.

    """

    def __init__(self):
        r"""
        :param _InvocationId: Execution activity ID.
        :type InvocationId: str
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _InvocationStatus: Execution task status. Valid values:
<li> PENDING: Pending 
<li> RUNNING: Running
<li> SUCCESS: Success
<li> FAILED: Failed
<li> TIMEOUT: Command timed out
<li> PARTIAL_FAILED: Partial failure
        :type InvocationStatus: str
        :param _InvocationTaskBasicInfoSet: Execution task information list.
        :type InvocationTaskBasicInfoSet: list of InvocationTaskBasicInfo
        :param _Description: Execution activity description.
        :type Description: str
        :param _StartTime: Start time of the execution activity.
        :type StartTime: str
        :param _EndTime: End time of the execution activity.
        :type EndTime: str
        :param _CreatedTime: Time when the execution activity is created.
        :type CreatedTime: str
        :param _UpdatedTime: Time when the execution activity is updated.
        :type UpdatedTime: str
        :param _Parameters: Values of custom parameters.
        :type Parameters: str
        :param _DefaultParameters: Default custom parameter value.
        :type DefaultParameters: str
        :param _InstanceKind: Type of the instance executing the command. Valid values: `CVM`, `LIGHTHOUSE`.
        :type InstanceKind: str
        :param _Username: The user who executes the command on the instance.
        :type Username: str
        :param _InvocationSource: Invocation source.
        :type InvocationSource: str
        :param _CommandContent: Base64-encoded command
        :type CommandContent: str
        :param _CommandType: Command type
        :type CommandType: str
        :param _Timeout: Command timeout period, in seconds.
        :type Timeout: int
        :param _WorkingDirectory: Working directory for executing the command.
        :type WorkingDirectory: str
        :param _OutputCOSBucketUrl: The COS bucket URL for uploading logs.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: The COS bucket directory where the logs are saved.
        :type OutputCOSKeyPrefix: str
        """
        self._InvocationId = None
        self._CommandId = None
        self._InvocationStatus = None
        self._InvocationTaskBasicInfoSet = None
        self._Description = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Parameters = None
        self._DefaultParameters = None
        self._InstanceKind = None
        self._Username = None
        self._InvocationSource = None
        self._CommandContent = None
        self._CommandType = None
        self._Timeout = None
        self._WorkingDirectory = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def InvocationId(self):
        """Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InvocationStatus(self):
        """Execution task status. Valid values:
<li> PENDING: Pending 
<li> RUNNING: Running
<li> SUCCESS: Success
<li> FAILED: Failed
<li> TIMEOUT: Command timed out
<li> PARTIAL_FAILED: Partial failure
        :rtype: str
        """
        return self._InvocationStatus

    @InvocationStatus.setter
    def InvocationStatus(self, InvocationStatus):
        self._InvocationStatus = InvocationStatus

    @property
    def InvocationTaskBasicInfoSet(self):
        """Execution task information list.
        :rtype: list of InvocationTaskBasicInfo
        """
        return self._InvocationTaskBasicInfoSet

    @InvocationTaskBasicInfoSet.setter
    def InvocationTaskBasicInfoSet(self, InvocationTaskBasicInfoSet):
        self._InvocationTaskBasicInfoSet = InvocationTaskBasicInfoSet

    @property
    def Description(self):
        """Execution activity description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StartTime(self):
        """Start time of the execution activity.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the execution activity.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        """Time when the execution activity is created.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """Time when the execution activity is updated.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Parameters(self):
        """Values of custom parameters.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def DefaultParameters(self):
        """Default custom parameter value.
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def InstanceKind(self):
        """Type of the instance executing the command. Valid values: `CVM`, `LIGHTHOUSE`.
        :rtype: str
        """
        return self._InstanceKind

    @InstanceKind.setter
    def InstanceKind(self, InstanceKind):
        self._InstanceKind = InstanceKind

    @property
    def Username(self):
        """The user who executes the command on the instance.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def InvocationSource(self):
        """Invocation source.
        :rtype: str
        """
        return self._InvocationSource

    @InvocationSource.setter
    def InvocationSource(self, InvocationSource):
        self._InvocationSource = InvocationSource

    @property
    def CommandContent(self):
        """Base64-encoded command
        :rtype: str
        """
        return self._CommandContent

    @CommandContent.setter
    def CommandContent(self, CommandContent):
        self._CommandContent = CommandContent

    @property
    def CommandType(self):
        """Command type
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def Timeout(self):
        """Command timeout period, in seconds.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def WorkingDirectory(self):
        """Working directory for executing the command.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def OutputCOSBucketUrl(self):
        """The COS bucket URL for uploading logs.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """The COS bucket directory where the logs are saved.
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._InvocationId = params.get("InvocationId")
        self._CommandId = params.get("CommandId")
        self._InvocationStatus = params.get("InvocationStatus")
        if params.get("InvocationTaskBasicInfoSet") is not None:
            self._InvocationTaskBasicInfoSet = []
            for item in params.get("InvocationTaskBasicInfoSet"):
                obj = InvocationTaskBasicInfo()
                obj._deserialize(item)
                self._InvocationTaskBasicInfoSet.append(obj)
        self._Description = params.get("Description")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Parameters = params.get("Parameters")
        self._DefaultParameters = params.get("DefaultParameters")
        self._InstanceKind = params.get("InstanceKind")
        self._Username = params.get("Username")
        self._InvocationSource = params.get("InvocationSource")
        self._CommandContent = params.get("CommandContent")
        self._CommandType = params.get("CommandType")
        self._Timeout = params.get("Timeout")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTask(AbstractModel):
    """Execution task.

    """

    def __init__(self):
        r"""
        :param _InvocationId: Execution activity ID.
        :type InvocationId: str
        :param _InvocationTaskId: Execution task ID.
        :type InvocationTaskId: str
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _TaskStatus: Execution task status. Valid values:
<li> PENDING: Pending 
<li> DELIVERING: Delivering
<li> DELIVER_DELAYED: Delivery delayed 
<li> DELIVER_FAILED: Delivery failed
<li> START_FAILED: Failed to start the command
<li> RUNNING: Running
<li> SUCCESS: Success
<li> FAILED: Failed to execute the command. The exit code is not 0 after execution.
<li> TIMEOUT: Command timed out
<li> TASK_TIMEOUT: Task timed out
<li> CANCELLING: Canceling
<li> CANCELLED: Canceled (canceled before execution)
<li> TERMINATED: Terminated (canceled during execution)
        :type TaskStatus: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _TaskResult: Execution result.
        :type TaskResult: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        :param _StartTime: Start time of the execution task.
        :type StartTime: str
        :param _EndTime: End time of the execution task.
        :type EndTime: str
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _UpdatedTime: Update time.
        :type UpdatedTime: str
        :param _CommandDocument: Command details of the execution task.
        :type CommandDocument: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        :param _ErrorInfo: Error message displayed when the execution task fails.
        :type ErrorInfo: str
        :param _InvocationSource: Invocation source.
        :type InvocationSource: str
        """
        self._InvocationId = None
        self._InvocationTaskId = None
        self._CommandId = None
        self._TaskStatus = None
        self._InstanceId = None
        self._TaskResult = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._CommandDocument = None
        self._ErrorInfo = None
        self._InvocationSource = None

    @property
    def InvocationId(self):
        """Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvocationTaskId(self):
        """Execution task ID.
        :rtype: str
        """
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def TaskStatus(self):
        """Execution task status. Valid values:
<li> PENDING: Pending 
<li> DELIVERING: Delivering
<li> DELIVER_DELAYED: Delivery delayed 
<li> DELIVER_FAILED: Delivery failed
<li> START_FAILED: Failed to start the command
<li> RUNNING: Running
<li> SUCCESS: Success
<li> FAILED: Failed to execute the command. The exit code is not 0 after execution.
<li> TIMEOUT: Command timed out
<li> TASK_TIMEOUT: Task timed out
<li> CANCELLING: Canceling
<li> CANCELLED: Canceled (canceled before execution)
<li> TERMINATED: Terminated (canceled during execution)
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

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
    def TaskResult(self):
        """Execution result.
        :rtype: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

    @property
    def StartTime(self):
        """Start time of the execution task.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time of the execution task.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """Update time.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def CommandDocument(self):
        """Command details of the execution task.
        :rtype: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        """
        return self._CommandDocument

    @CommandDocument.setter
    def CommandDocument(self, CommandDocument):
        self._CommandDocument = CommandDocument

    @property
    def ErrorInfo(self):
        """Error message displayed when the execution task fails.
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def InvocationSource(self):
        """Invocation source.
        :rtype: str
        """
        return self._InvocationSource

    @InvocationSource.setter
    def InvocationSource(self, InvocationSource):
        self._InvocationSource = InvocationSource


    def _deserialize(self, params):
        self._InvocationId = params.get("InvocationId")
        self._InvocationTaskId = params.get("InvocationTaskId")
        self._CommandId = params.get("CommandId")
        self._TaskStatus = params.get("TaskStatus")
        self._InstanceId = params.get("InstanceId")
        if params.get("TaskResult") is not None:
            self._TaskResult = TaskResult()
            self._TaskResult._deserialize(params.get("TaskResult"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        if params.get("CommandDocument") is not None:
            self._CommandDocument = CommandDocument()
            self._CommandDocument._deserialize(params.get("CommandDocument"))
        self._ErrorInfo = params.get("ErrorInfo")
        self._InvocationSource = params.get("InvocationSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTaskBasicInfo(AbstractModel):
    """Execution task description.

    """

    def __init__(self):
        r"""
        :param _InvocationTaskId: Execution task ID.
        :type InvocationTaskId: str
        :param _TaskStatus: Execution task status. Valid values:
<li> PENDING: Pending 
<li> DELIVERING: Delivering
<li> DELIVER_DELAYED: Delivery delayed 
<li> DELIVER_FAILED: Delivery failed
<li> START_FAILED: Failed to start the command
<li> RUNNING: Running
<li> SUCCESS: Success
<li> FAILED: Failed to execute the command. The exit code is not 0 after execution.
<li> TIMEOUT: Command timed out
<li> TASK_TIMEOUT: Task timed out
<li> CANCELLING: Canceling
<li> CANCELLED: Canceled (canceled before execution)
<li> TERMINATED: Terminated (canceled during execution)
        :type TaskStatus: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InvocationTaskId = None
        self._TaskStatus = None
        self._InstanceId = None

    @property
    def InvocationTaskId(self):
        """Execution task ID.
        :rtype: str
        """
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def TaskStatus(self):
        """Execution task status. Valid values:
<li> PENDING: Pending 
<li> DELIVERING: Delivering
<li> DELIVER_DELAYED: Delivery delayed 
<li> DELIVER_FAILED: Delivery failed
<li> START_FAILED: Failed to start the command
<li> RUNNING: Running
<li> SUCCESS: Success
<li> FAILED: Failed to execute the command. The exit code is not 0 after execution.
<li> TIMEOUT: Command timed out
<li> TASK_TIMEOUT: Task timed out
<li> CANCELLING: Canceling
<li> CANCELLED: Canceled (canceled before execution)
<li> TERMINATED: Terminated (canceled during execution)
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def InstanceId(self):
        """Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InvocationTaskId = params.get("InvocationTaskId")
        self._TaskStatus = params.get("TaskStatus")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandRequest(AbstractModel):
    """InvokeCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: ID of the command to be triggered.
        :type CommandId: str
        :param _InstanceIds: IDs of instances about to execute commands. At most 100 IDs are allowed.
        :type InstanceIds: list of str
        :param _Parameters: Custom parameters of the command. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided, the DefaultParameters of the command is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type Parameters: str
        :param _Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of the least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. If this is not specified, the Username of the command is used by default.
        :type Username: str
        :param _WorkingDirectory: Execution path of the command. The WorkingDirectory of the command is used by default.
        :type WorkingDirectory: str
        :param _Timeout: Command timeout period. Value range: [1, 86400]. The Timeout of the command is used by default.
        :type Timeout: int
        :param _OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :type OutputCOSKeyPrefix: str
        """
        self._CommandId = None
        self._InstanceIds = None
        self._Parameters = None
        self._Username = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        """ID of the command to be triggered.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InstanceIds(self):
        """IDs of instances about to execute commands. At most 100 IDs are allowed.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Parameters(self):
        """Custom parameters of the command. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided, the DefaultParameters of the command is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Username(self):
        """The username used to execute the command on the CVM or Lighthouse instance.
The principle of the least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. If this is not specified, the Username of the command is used by default.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def WorkingDirectory(self):
        """Execution path of the command. The WorkingDirectory of the command is used by default.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """Command timeout period. Value range: [1, 86400]. The Timeout of the command is used by default.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def OutputCOSBucketUrl(self):
        """The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._InstanceIds = params.get("InstanceIds")
        self._Parameters = params.get("Parameters")
        self._Username = params.get("Username")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandResponse(AbstractModel):
    """InvokeCommand response structure.

    """

    def __init__(self):
        r"""
        :param _InvocationId: Execution activity ID.
        :type InvocationId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InvocationId = None
        self._RequestId = None

    @property
    def InvocationId(self):
        """Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

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
        self._InvocationId = params.get("InvocationId")
        self._RequestId = params.get("RequestId")


class Invoker(AbstractModel):
    """Invoker information.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Invoker ID.
        :type InvokerId: str
        :param _Name: Invoker name.
        :type Name: str
        :param _Type: Invoker type.
        :type Type: str
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _Username: Username.
        :type Username: str
        :param _Parameters: Custom parameters.
        :type Parameters: str
        :param _InstanceIds: Instance ID list.
        :type InstanceIds: list of str
        :param _Enable: Whether to enable the invoker.
        :type Enable: bool
        :param _ScheduleSettings: Execution schedule of the invoker. This field is returned for recurring invokers.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        :param _CreatedTime: Creation time.
        :type CreatedTime: str
        :param _UpdatedTime: Modification time.
        :type UpdatedTime: str
        """
        self._InvokerId = None
        self._Name = None
        self._Type = None
        self._CommandId = None
        self._Username = None
        self._Parameters = None
        self._InstanceIds = None
        self._Enable = None
        self._ScheduleSettings = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def InvokerId(self):
        """Invoker ID.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def Name(self):
        """Invoker name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Invoker type.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Username(self):
        """Username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        """Custom parameters.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

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
    def Enable(self):
        """Whether to enable the invoker.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ScheduleSettings(self):
        """Execution schedule of the invoker. This field is returned for recurring invokers.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings

    @property
    def CreatedTime(self):
        """Creation time.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """Modification time.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CommandId = params.get("CommandId")
        self._Username = params.get("Username")
        self._Parameters = params.get("Parameters")
        self._InstanceIds = params.get("InstanceIds")
        self._Enable = params.get("Enable")
        if params.get("ScheduleSettings") is not None:
            self._ScheduleSettings = ScheduleSettings()
            self._ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokerRecord(AbstractModel):
    """Execution history of the invoker.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Invoker ID.
        :type InvokerId: str
        :param _InvokeTime: Execution time.
        :type InvokeTime: str
        :param _Reason: Execution reason.
        :type Reason: str
        :param _InvocationId: Command execution ID.
        :type InvocationId: str
        :param _Result: Trigger result.
        :type Result: str
        """
        self._InvokerId = None
        self._InvokeTime = None
        self._Reason = None
        self._InvocationId = None
        self._Result = None

    @property
    def InvokerId(self):
        """Invoker ID.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def InvokeTime(self):
        """Execution time.
        :rtype: str
        """
        return self._InvokeTime

    @InvokeTime.setter
    def InvokeTime(self, InvokeTime):
        self._InvokeTime = InvokeTime

    @property
    def Reason(self):
        """Execution reason.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def InvocationId(self):
        """Command execution ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def Result(self):
        """Trigger result.
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        self._InvokeTime = params.get("InvokeTime")
        self._Reason = params.get("Reason")
        self._InvocationId = params.get("InvocationId")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCommandRequest(AbstractModel):
    """ModifyCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param _Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param _Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param _CommandType: Command type. `SHELL` and `POWERSHELL` are supported.
        :type CommandType: str
        :param _WorkingDirectory: Command execution path.
        :type WorkingDirectory: str
        :param _Timeout: Command timeout period. Value range: [1, 86400].
        :type Timeout: int
        :param _DefaultParameters: The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
All parameters are overwritten. All default values are required for modification.
Modification is only allowed when `EnableParameter` is `true`.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type DefaultParameters: str
        :param _Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user.
        :type Username: str
        :param _OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :type OutputCOSKeyPrefix: str
        """
        self._CommandId = None
        self._CommandName = None
        self._Description = None
        self._Content = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._DefaultParameters = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CommandName(self):
        """Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        """Command description. The maximum length is 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        """Base64-encoded command. The maximum length is 64 KB.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        """Command type. `SHELL` and `POWERSHELL` are supported.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """Command execution path.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """Command timeout period. Value range: [1, 86400].
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def DefaultParameters(self):
        """The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
All parameters are overwritten. All default values are required for modification.
Modification is only allowed when `EnableParameter` is `true`.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def Username(self):
        """The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._CommandName = params.get("CommandName")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._DefaultParameters = params.get("DefaultParameters")
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCommandResponse(AbstractModel):
    """ModifyCommand response structure.

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


class ModifyInvokerRequest(AbstractModel):
    """ModifyInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: ID of the invoker to be modified.
        :type InvokerId: str
        :param _Name: Name of the invoker to be modified.
        :type Name: str
        :param _Type: Invoker type. It can only be `SCHEDULE` (recurring invokers).
        :type Type: str
        :param _CommandId: ID of the command to be modified.
        :type CommandId: str
        :param _Username: The username to be modified.
        :type Username: str
        :param _Parameters: Custom parameters to be modified.
        :type Parameters: str
        :param _InstanceIds: List of instance IDs to be modified. Up to 100 IDs are allowed.
        :type InstanceIds: list of str
        :param _ScheduleSettings: Scheduled invoker settings to be modified.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        self._InvokerId = None
        self._Name = None
        self._Type = None
        self._CommandId = None
        self._Username = None
        self._Parameters = None
        self._InstanceIds = None
        self._ScheduleSettings = None

    @property
    def InvokerId(self):
        """ID of the invoker to be modified.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def Name(self):
        """Name of the invoker to be modified.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Invoker type. It can only be `SCHEDULE` (recurring invokers).
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        """ID of the command to be modified.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Username(self):
        """The username to be modified.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        """Custom parameters to be modified.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def InstanceIds(self):
        """List of instance IDs to be modified. Up to 100 IDs are allowed.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ScheduleSettings(self):
        """Scheduled invoker settings to be modified.
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CommandId = params.get("CommandId")
        self._Username = params.get("Username")
        self._Parameters = params.get("Parameters")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ScheduleSettings") is not None:
            self._ScheduleSettings = ScheduleSettings()
            self._ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInvokerResponse(AbstractModel):
    """ModifyInvoker response structure.

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


class PreviewReplacedCommandContentRequest(AbstractModel):
    """PreviewReplacedCommandContent request structure.

    """

    def __init__(self):
        r"""
        :param _Parameters: Custom parameters for the preview. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and "value" is its specified value. Both "key" and "value" are strings.
At most 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can only contain [a-z], [A-Z], [0-9], [-_].
This parameter can be left empty if DefaultParameters is set for the previewed CommandId.
        :type Parameters: str
        :param _CommandId: The command to be previewed. If DefaultParameters is set, it is combined with Parameters and Parameters takes priority.
`CommandId` or `Content` must be specified.
        :type CommandId: str
        :param _Content: Base64-encoded command to be previewed. The maximum length is 64 KB.
CommandId or Content must be specified.
        :type Content: str
        """
        self._Parameters = None
        self._CommandId = None
        self._Content = None

    @property
    def Parameters(self):
        """Custom parameters for the preview. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and "value" is its specified value. Both "key" and "value" are strings.
At most 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can only contain [a-z], [A-Z], [0-9], [-_].
This parameter can be left empty if DefaultParameters is set for the previewed CommandId.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def CommandId(self):
        """The command to be previewed. If DefaultParameters is set, it is combined with Parameters and Parameters takes priority.
`CommandId` or `Content` must be specified.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Content(self):
        """Base64-encoded command to be previewed. The maximum length is 64 KB.
CommandId or Content must be specified.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Parameters = params.get("Parameters")
        self._CommandId = params.get("CommandId")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewReplacedCommandContentResponse(AbstractModel):
    """PreviewReplacedCommandContent response structure.

    """

    def __init__(self):
        r"""
        :param _ReplacedContent: Base64-encoded command with custom parameters.
        :type ReplacedContent: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReplacedContent = None
        self._RequestId = None

    @property
    def ReplacedContent(self):
        """Base64-encoded command with custom parameters.
        :rtype: str
        """
        return self._ReplacedContent

    @ReplacedContent.setter
    def ReplacedContent(self, ReplacedContent):
        self._ReplacedContent = ReplacedContent

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
        self._ReplacedContent = params.get("ReplacedContent")
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Information of a region.

    """

    def __init__(self):
        r"""
        :param _Region: Region name, such as `ap-guangzhou`
        :type Region: str
        :param _RegionName: Region description, such as `Guangzhou`
        :type RegionName: str
        :param _RegionState: Region status. `AVAILABLE` indicates the region is available.
        :type RegionState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None

    @property
    def Region(self):
        """Region name, such as `ap-guangzhou`
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        """Region description, such as `Guangzhou`
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        """Region status. `AVAILABLE` indicates the region is available.
        :rtype: str
        """
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
        


class RunCommandRequest(AbstractModel):
    """RunCommand request structure.

    """

    def __init__(self):
        r"""
        :param _Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param _InstanceIds: IDs of instances about to execute commands. Up to 100 IDs are allowed. Supported instance types:
<li> `CVM`
<li> `LIGHTHOUSE`
        :type InstanceIds: list of str
        :param _CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param _Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param _CommandType: Command type. `SHELL` and `POWERSHELL` are supported. The default value is `SHELL`.
        :type CommandType: str
        :param _WorkingDirectory: Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :type WorkingDirectory: str
        :param _Timeout: Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :type Timeout: int
        :param _SaveCommand: Whether to save the command. Valid values:
<li> `True`: Save
<li> `False`: Do not save
The default value is `False`.
        :type SaveCommand: bool
        :param _EnableParameter: Whether to enable the custom parameter feature.
This cannot be modified once created.
Default value: `false`.
        :type EnableParameter: bool
        :param _DefaultParameters: The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If Parameters is not provided, the default values specified here are used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type DefaultParameters: str
        :param _Parameters: Custom parameters of `Command`. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided, the `DefaultParameters` is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type Parameters: str
        :param _Tags: The tags of the command. It is available when `SaveCommand` is `True`. A maximum of 10 tags are allowed.
        :type Tags: list of Tag
        :param _Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the user `root` is used to execute commands on Linux and the user `System` is used on Windows.
        :type Username: str
        :param _OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :type OutputCOSKeyPrefix: str
        """
        self._Content = None
        self._InstanceIds = None
        self._CommandName = None
        self._Description = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._SaveCommand = None
        self._EnableParameter = None
        self._DefaultParameters = None
        self._Parameters = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def Content(self):
        """Base64-encoded command. The maximum length is 64 KB.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def InstanceIds(self):
        """IDs of instances about to execute commands. Up to 100 IDs are allowed. Supported instance types:
<li> `CVM`
<li> `LIGHTHOUSE`
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def CommandName(self):
        """Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        """Command description. The maximum length is 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CommandType(self):
        """Command type. `SHELL` and `POWERSHELL` are supported. The default value is `SHELL`.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def SaveCommand(self):
        """Whether to save the command. Valid values:
<li> `True`: Save
<li> `False`: Do not save
The default value is `False`.
        :rtype: bool
        """
        return self._SaveCommand

    @SaveCommand.setter
    def SaveCommand(self, SaveCommand):
        self._SaveCommand = SaveCommand

    @property
    def EnableParameter(self):
        """Whether to enable the custom parameter feature.
This cannot be modified once created.
Default value: `false`.
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        """The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If Parameters is not provided, the default values specified here are used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def Parameters(self):
        """Custom parameters of `Command`. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided, the `DefaultParameters` is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Tags(self):
        """The tags of the command. It is available when `SaveCommand` is `True`. A maximum of 10 tags are allowed.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        """The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the user `root` is used to execute commands on Linux and the user `System` is used on Windows.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._InstanceIds = params.get("InstanceIds")
        self._CommandName = params.get("CommandName")
        self._Description = params.get("Description")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._SaveCommand = params.get("SaveCommand")
        self._EnableParameter = params.get("EnableParameter")
        self._DefaultParameters = params.get("DefaultParameters")
        self._Parameters = params.get("Parameters")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCommandResponse(AbstractModel):
    """RunCommand response structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _InvocationId: Execution activity ID.
        :type InvocationId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CommandId = None
        self._InvocationId = None
        self._RequestId = None

    @property
    def CommandId(self):
        """Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InvocationId(self):
        """Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

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
        self._CommandId = params.get("CommandId")
        self._InvocationId = params.get("InvocationId")
        self._RequestId = params.get("RequestId")


class ScheduleSettings(AbstractModel):
    """Settings of a scheduled invoker

    """

    def __init__(self):
        r"""
        :param _Policy: Execution policy:
<br><li>`ONCE`: Execute once
<br><li>`RECURRENCE`: Execute repeatedly
        :type Policy: str
        :param _Recurrence: Trigger the crontab expression. This field is required if `Policy` is `RECURRENCE`. The crontab expression is parsed in UTC+8.
        :type Recurrence: str
        :param _InvokeTime: The next execution time of the invoker. This field is required if `Policy` is `ONCE`.
        :type InvokeTime: str
        """
        self._Policy = None
        self._Recurrence = None
        self._InvokeTime = None

    @property
    def Policy(self):
        """Execution policy:
<br><li>`ONCE`: Execute once
<br><li>`RECURRENCE`: Execute repeatedly
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Recurrence(self):
        """Trigger the crontab expression. This field is required if `Policy` is `RECURRENCE`. The crontab expression is parsed in UTC+8.
        :rtype: str
        """
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence

    @property
    def InvokeTime(self):
        """The next execution time of the invoker. This field is required if `Policy` is `ONCE`.
        :rtype: str
        """
        return self._InvokeTime

    @InvokeTime.setter
    def InvokeTime(self, InvokeTime):
        self._InvokeTime = InvokeTime


    def _deserialize(self, params):
        self._Policy = params.get("Policy")
        self._Recurrence = params.get("Recurrence")
        self._InvokeTime = params.get("InvokeTime")
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
        :param _Key: Tag key.
        :type Key: str
        :param _Value: Tag value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Tag key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value.
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
        


class TaskResult(AbstractModel):
    """Task result.

    """

    def __init__(self):
        r"""
        :param _ExitCode: ExitCode of the execution.
        :type ExitCode: int
        :param _Output: Base64-encoded command output. The maximum length is 24 KB.
        :type Output: str
        :param _ExecStartTime: Time when the execution is started.
        :type ExecStartTime: str
        :param _ExecEndTime: Time when the execution is ended.
        :type ExecEndTime: str
        :param _Dropped: Dropped bytes of the command output.
        :type Dropped: int
        :param _OutputUrl: COS URL of the logs.
        :type OutputUrl: str
        :param _OutputUploadCOSErrorInfo: Error message for uploading logs to COS.
        :type OutputUploadCOSErrorInfo: str
        """
        self._ExitCode = None
        self._Output = None
        self._ExecStartTime = None
        self._ExecEndTime = None
        self._Dropped = None
        self._OutputUrl = None
        self._OutputUploadCOSErrorInfo = None

    @property
    def ExitCode(self):
        """ExitCode of the execution.
        :rtype: int
        """
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode

    @property
    def Output(self):
        """Base64-encoded command output. The maximum length is 24 KB.
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def ExecStartTime(self):
        """Time when the execution is started.
        :rtype: str
        """
        return self._ExecStartTime

    @ExecStartTime.setter
    def ExecStartTime(self, ExecStartTime):
        self._ExecStartTime = ExecStartTime

    @property
    def ExecEndTime(self):
        """Time when the execution is ended.
        :rtype: str
        """
        return self._ExecEndTime

    @ExecEndTime.setter
    def ExecEndTime(self, ExecEndTime):
        self._ExecEndTime = ExecEndTime

    @property
    def Dropped(self):
        """Dropped bytes of the command output.
        :rtype: int
        """
        return self._Dropped

    @Dropped.setter
    def Dropped(self, Dropped):
        self._Dropped = Dropped

    @property
    def OutputUrl(self):
        """COS URL of the logs.
        :rtype: str
        """
        return self._OutputUrl

    @OutputUrl.setter
    def OutputUrl(self, OutputUrl):
        self._OutputUrl = OutputUrl

    @property
    def OutputUploadCOSErrorInfo(self):
        """Error message for uploading logs to COS.
        :rtype: str
        """
        return self._OutputUploadCOSErrorInfo

    @OutputUploadCOSErrorInfo.setter
    def OutputUploadCOSErrorInfo(self, OutputUploadCOSErrorInfo):
        self._OutputUploadCOSErrorInfo = OutputUploadCOSErrorInfo


    def _deserialize(self, params):
        self._ExitCode = params.get("ExitCode")
        self._Output = params.get("Output")
        self._ExecStartTime = params.get("ExecStartTime")
        self._ExecEndTime = params.get("ExecEndTime")
        self._Dropped = params.get("Dropped")
        self._OutputUrl = params.get("OutputUrl")
        self._OutputUploadCOSErrorInfo = params.get("OutputUploadCOSErrorInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        