# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
    r"""TAT agent information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _Version: Agent version.
        :type Version: str
        :param _LastHeartbeatTime: Last heartbeat time
        :type LastHeartbeatTime: str
        :param _AgentStatus: Agent status. valid values:.
Online: Online, Offline: Offline.

        :type AgentStatus: str
        :param _Environment: Agent execution environment. valid values: Linux: Linux instance. Windows: Windows instance.
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
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Version(self):
        r"""Agent version.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LastHeartbeatTime(self):
        r"""Last heartbeat time
        :rtype: str
        """
        return self._LastHeartbeatTime

    @LastHeartbeatTime.setter
    def LastHeartbeatTime(self, LastHeartbeatTime):
        self._LastHeartbeatTime = LastHeartbeatTime

    @property
    def AgentStatus(self):
        r"""Agent status. valid values:.
Online: Online, Offline: Offline.

        :rtype: str
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def Environment(self):
        r"""Agent execution environment. valid values: Linux: Linux instance. Windows: Windows instance.
        :rtype: str
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def SupportFeatures(self):
        r"""Features supported by the TAT agent.
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
    r"""CancelInvocation request structure.

    """

    def __init__(self):
        r"""
        :param _InvocationId: Execution activity ID.

Call the [DescribeInvocations](https://www.tencentcloud.comom/document/api/1340/52679?from_cn_redirect=1) api to query execution.
        :type InvocationId: str
        :param _InstanceIds: Instance ID list. upper limit: 100.

Instance ID can be obtained through the query instance interface of corresponding cloud services. currently supported instance types:.
- CVM
- Lighthouse
- TAT Register instance.
        :type InstanceIds: list of str
        """
        self._InvocationId = None
        self._InstanceIds = None

    @property
    def InvocationId(self):
        r"""Execution activity ID.

Call the [DescribeInvocations](https://www.tencentcloud.comom/document/api/1340/52679?from_cn_redirect=1) api to query execution.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InstanceIds(self):
        r"""Instance ID list. upper limit: 100.

Instance ID can be obtained through the query instance interface of corresponding cloud services. currently supported instance types:.
- CVM
- Lighthouse
- TAT Register instance.
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
    r"""CancelInvocation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Command(AbstractModel):
    r"""Command details.

    """

    def __init__(self):
        r"""
        :param _CommandId: <p>Command ID.</p>.
        :type CommandId: str
        :param _CommandName: <P>Command name.</p>.
        :type CommandName: str
        :param _Description: <P>Command description.</p>.
        :type Description: str
        :param _Content: <p>The Base64-encoded command content.</p>.
        :type Content: str
        :param _CommandType: <p>Command type. value is one of SHELL, POWERSHELL, BAT.</p>.
        :type CommandType: str
        :param _WorkingDirectory: <P>Command execution path.</p>.
        :type WorkingDirectory: str
        :param _Timeout: <p>Command timeout time.</p><p>unit: seconds.</p><p>when specifying the OutputCOSBucketUrl parameter, the timeout period includes the time taken to upload command output to COS.</p>.
        :type Timeout: int
        :param _CreatedTime: <p>Command creation time. the format is YYYY-MM-DDThh:MM:ssZ.</p>.
        :type CreatedTime: str
        :param _UpdatedTime: <p>Command last update time. format: YYYY-MM-DDThh:MM:ssZ.</p>.
        :type UpdatedTime: str
        :param _EnableParameter: <P>Whether to enable the custom parameter feature.</p>.
        :type EnableParameter: bool
        :param _DefaultParameters: <P>Default value of custom parameter.</p>.
        :type DefaultParameters: str
        :param _DefaultParameterConfs: <P>Default value of custom parameters.</p>.
        :type DefaultParameterConfs: list of DefaultParameterConf
        :param _Scenes: <P>Command association scenarios</p>.
        :type Scenes: list of str
        :param _FormattedDescription: <P>Structured description of the command. public commands have values, and user commands are empty strings.</p>.
        :type FormattedDescription: str
        :param _CreatedBy: <p>Command creator.</p><p>enumeration value:</p><ul><li>TAT: public command</li><li>USER: personal creation command</li></ul>.
        :type CreatedBy: str
        :param _Tags: <P>Tag list associated with the command.</p>.
        :type Tags: list of Tag
        :param _Username: <P>Username to run command on the instance.</p>.
        :type Username: str
        :param _OutputCOSBucketUrl: <P>The cos bucket address for log upload.</p>.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: <P>Directory of logs in the cos bucket.</p>.
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
        self._DefaultParameterConfs = None
        self._Scenes = None
        self._FormattedDescription = None
        self._CreatedBy = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        r"""<p>Command ID.</p>.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CommandName(self):
        r"""<P>Command name.</p>.
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        r"""<P>Command description.</p>.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        r"""<p>The Base64-encoded command content.</p>.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        r"""<p>Command type. value is one of SHELL, POWERSHELL, BAT.</p>.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        r"""<P>Command execution path.</p>.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        r"""<p>Command timeout time.</p><p>unit: seconds.</p><p>when specifying the OutputCOSBucketUrl parameter, the timeout period includes the time taken to upload command output to COS.</p>.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def CreatedTime(self):
        r"""<p>Command creation time. the format is YYYY-MM-DDThh:MM:ssZ.</p>.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""<p>Command last update time. format: YYYY-MM-DDThh:MM:ssZ.</p>.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def EnableParameter(self):
        r"""<P>Whether to enable the custom parameter feature.</p>.
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        r"""<P>Default value of custom parameter.</p>.
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        r"""<P>Default value of custom parameters.</p>.
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Scenes(self):
        r"""<P>Command association scenarios</p>.
        :rtype: list of str
        """
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes

    @property
    def FormattedDescription(self):
        r"""<P>Structured description of the command. public commands have values, and user commands are empty strings.</p>.
        :rtype: str
        """
        return self._FormattedDescription

    @FormattedDescription.setter
    def FormattedDescription(self, FormattedDescription):
        self._FormattedDescription = FormattedDescription

    @property
    def CreatedBy(self):
        r"""<p>Command creator.</p><p>enumeration value:</p><ul><li>TAT: public command</li><li>USER: personal creation command</li></ul>.
        :rtype: str
        """
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def Tags(self):
        r"""<P>Tag list associated with the command.</p>.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        r"""<P>Username to run command on the instance.</p>.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        r"""<P>The cos bucket address for log upload.</p>.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        r"""<P>Directory of logs in the cos bucket.</p>.
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
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
        self._Scenes = params.get("Scenes")
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
    r"""Command execution details.

    """

    def __init__(self):
        r"""
        :param _Content: Base64-encoded command.
        :type Content: str
        :param _CommandType: Command type. value is one of SHELL, POWERSHELL, BAT.
        :type CommandType: str
        :param _Timeout: Timeout period. unit: seconds.
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
        r"""Base64-encoded command.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        r"""Command type. value is one of SHELL, POWERSHELL, BAT.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def Timeout(self):
        r"""Timeout period. unit: seconds.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def WorkingDirectory(self):
        r"""Execution path.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Username(self):
        r"""The user who executes the command.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        r"""URL of the COS bucket to store the output
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        r"""Prefix of the output file name 
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
    r"""CreateCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param _Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param _Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param _CommandType: Command type. currently supports SHELL, POWERSHELL, BAT. default: SHELL.
        :type CommandType: str
        :param _WorkingDirectory: Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :type WorkingDirectory: str
        :param _Timeout: Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :type Timeout: int
        :param _EnableParameter: Whether to enable the custom parameter feature.
This cannot be modified once created.
Default value: `false`.
        :type EnableParameter: bool
        :param _DefaultParameters: Enable the custom parameter feature. default value of the custom parameter. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
If no parameter value is provided when invoking the command, the default value here will be used to replace it.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
Allow settings only when the EnableParameter parameter is true.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
        :type DefaultParameters: str
        :param _DefaultParameterConfs: Custom parameter array.
If no parameter value is provided when invoking the command, the default value here will be used to replace it.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
Allow settings only when the EnableParameter parameter is true.
Custom parameters can be up to 20.
        :type DefaultParameterConfs: list of DefaultParameterConf
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
        self._DefaultParameterConfs = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandName(self):
        r"""Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Content(self):
        r"""Base64-encoded command. The maximum length is 64 KB.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        r"""Command description. The maximum length is 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CommandType(self):
        r"""Command type. currently supports SHELL, POWERSHELL, BAT. default: SHELL.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        r"""Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        r"""Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def EnableParameter(self):
        r"""Whether to enable the custom parameter feature.
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
        r"""Enable the custom parameter feature. default value of the custom parameter. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
If no parameter value is provided when invoking the command, the default value here will be used to replace it.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
Allow settings only when the EnableParameter parameter is true.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        r"""Custom parameter array.
If no parameter value is provided when invoking the command, the default value here will be used to replace it.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
Allow settings only when the EnableParameter parameter is true.
Custom parameters can be up to 20.
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Tags(self):
        r"""Tags bound to the command. At most 10 tags are allowed.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        r"""The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the root user is used to execute commands on Linux and the System user is used on Windows.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        r"""The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        r"""The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
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
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
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
    r"""CreateCommand response structure.

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
        r"""Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""CreateInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Executor name. length not exceeding 120 characters.
        :type Name: str
        :param _Type: Executor type.

Selectable values (currently only support one):.

-`SCHEDULE`: period type executor.
        :type Type: str
        :param _CommandId: Remote command ID.

Call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :type CommandId: str
        :param _InstanceIds: Trigger associated instance ID. list cap 100.

You can get the instance ID through the query instance interface of corresponding cloud services. currently supports instance types: CVM, Lighthouse, and TAT managed instances.

The instance needs to have the TAT client installed, and the client must be in Online status. you can query client status via the [DescribeAutomationAgentStatus](https://www.tencentcloud.comom/document/api/1340/52682?from_cn_redirect=1) api.
        :type InstanceIds: list of str
        :param _Username: Command execution user. length not exceeding 256 characters.
        :type Username: str
        :param _Parameters: Command custom parameter. field type is JSON encode string.

This parameter can be set only when EnableParameter of the command specified by CommandId is true. obtain the EnableParameter settings through the [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
        :type Parameters: str
        :param _ScheduleSettings: Recurring invoker settings.

When the executor type is `SCHEDULE`, specify this parameter.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        :param _Tags: Tag associated with the command. list length not exceeding 10.
        :type Tags: list of Tag
        """
        self._Name = None
        self._Type = None
        self._CommandId = None
        self._InstanceIds = None
        self._Username = None
        self._Parameters = None
        self._ScheduleSettings = None
        self._Tags = None

    @property
    def Name(self):
        r"""Executor name. length not exceeding 120 characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Executor type.

Selectable values (currently only support one):.

-`SCHEDULE`: period type executor.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        r"""Remote command ID.

Call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InstanceIds(self):
        r"""Trigger associated instance ID. list cap 100.

You can get the instance ID through the query instance interface of corresponding cloud services. currently supports instance types: CVM, Lighthouse, and TAT managed instances.

The instance needs to have the TAT client installed, and the client must be in Online status. you can query client status via the [DescribeAutomationAgentStatus](https://www.tencentcloud.comom/document/api/1340/52682?from_cn_redirect=1) api.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Username(self):
        r"""Command execution user. length not exceeding 256 characters.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        r"""Command custom parameter. field type is JSON encode string.

This parameter can be set only when EnableParameter of the command specified by CommandId is true. obtain the EnableParameter settings through the [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def ScheduleSettings(self):
        r"""Recurring invoker settings.

When the executor type is `SCHEDULE`, specify this parameter.
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings

    @property
    def Tags(self):
        r"""Tag associated with the command. list length not exceeding 10.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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
        


class CreateInvokerResponse(AbstractModel):
    r"""CreateInvoker response structure.

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
        r"""Invoker ID.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        self._RequestId = params.get("RequestId")


class CreateRegisterCodeRequest(AbstractModel):
    r"""CreateRegisterCode request structure.

    """

    def __init__(self):
        r"""
        :param _Description: Describes the registration code. maximum length is 128 characters.
        :type Description: str
        :param _InstanceNamePrefix: Prefix of the registered instance name. maximum length is 32 characters.
        :type InstanceNamePrefix: str
        :param _RegisterLimit: Number of instances allowed by the registration code. default value is 10, minimum value is 1, maximum value is 10000.
        :type RegisterLimit: int
        :param _EffectiveTime: The validity time of the registration code is measured in hours. default value is 4.

-If the input value is less than or equal to 99999, the time is deemed valid in hours.
-If the input value is more than 99999, it is set to permanently valid.
        :type EffectiveTime: int
        :param _IpAddressRange: Restrict the registration code to register only from the public outbound ip described by IpAddressRange.

Empty by default, meaning no restrictions.

The value should be in standard IPv4 or CIDRv4 format, such as 192.168.1.1 or 192.168.0.0/16.
        :type IpAddressRange: str
        """
        self._Description = None
        self._InstanceNamePrefix = None
        self._RegisterLimit = None
        self._EffectiveTime = None
        self._IpAddressRange = None

    @property
    def Description(self):
        r"""Describes the registration code. maximum length is 128 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceNamePrefix(self):
        r"""Prefix of the registered instance name. maximum length is 32 characters.
        :rtype: str
        """
        return self._InstanceNamePrefix

    @InstanceNamePrefix.setter
    def InstanceNamePrefix(self, InstanceNamePrefix):
        self._InstanceNamePrefix = InstanceNamePrefix

    @property
    def RegisterLimit(self):
        r"""Number of instances allowed by the registration code. default value is 10, minimum value is 1, maximum value is 10000.
        :rtype: int
        """
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def EffectiveTime(self):
        r"""The validity time of the registration code is measured in hours. default value is 4.

-If the input value is less than or equal to 99999, the time is deemed valid in hours.
-If the input value is more than 99999, it is set to permanently valid.
        :rtype: int
        """
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def IpAddressRange(self):
        r"""Restrict the registration code to register only from the public outbound ip described by IpAddressRange.

Empty by default, meaning no restrictions.

The value should be in standard IPv4 or CIDRv4 format, such as 192.168.1.1 or 192.168.0.0/16.
        :rtype: str
        """
        return self._IpAddressRange

    @IpAddressRange.setter
    def IpAddressRange(self, IpAddressRange):
        self._IpAddressRange = IpAddressRange


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._InstanceNamePrefix = params.get("InstanceNamePrefix")
        self._RegisterLimit = params.get("RegisterLimit")
        self._EffectiveTime = params.get("EffectiveTime")
        self._IpAddressRange = params.get("IpAddressRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRegisterCodeResponse(AbstractModel):
    r"""CreateRegisterCode response structure.

    """

    def __init__(self):
        r"""
        :param _RegisterCodeId: Registration code ID.
        :type RegisterCodeId: str
        :param _RegisterCodeValue: Registration code value.
        :type RegisterCodeValue: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RegisterCodeId = None
        self._RegisterCodeValue = None
        self._RequestId = None

    @property
    def RegisterCodeId(self):
        r"""Registration code ID.
        :rtype: str
        """
        return self._RegisterCodeId

    @RegisterCodeId.setter
    def RegisterCodeId(self, RegisterCodeId):
        self._RegisterCodeId = RegisterCodeId

    @property
    def RegisterCodeValue(self):
        r"""Registration code value.
        :rtype: str
        """
        return self._RegisterCodeValue

    @RegisterCodeValue.setter
    def RegisterCodeValue(self, RegisterCodeValue):
        self._RegisterCodeValue = RegisterCodeValue

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RegisterCodeId = params.get("RegisterCodeId")
        self._RegisterCodeValue = params.get("RegisterCodeValue")
        self._RequestId = params.get("RequestId")


class DefaultParameterConf(AbstractModel):
    r"""Custom parameter.

    """

    def __init__(self):
        r"""
        :param _ParameterName: Parameter name.
        :type ParameterName: str
        :param _ParameterValue: Default parameter value.
        :type ParameterValue: str
        :param _ParameterDescription: Parameter description.
        :type ParameterDescription: str
        """
        self._ParameterName = None
        self._ParameterValue = None
        self._ParameterDescription = None

    @property
    def ParameterName(self):
        r"""Parameter name.
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ParameterValue(self):
        r"""Default parameter value.
        :rtype: str
        """
        return self._ParameterValue

    @ParameterValue.setter
    def ParameterValue(self, ParameterValue):
        self._ParameterValue = ParameterValue

    @property
    def ParameterDescription(self):
        r"""Parameter description.
        :rtype: str
        """
        return self._ParameterDescription

    @ParameterDescription.setter
    def ParameterDescription(self, ParameterDescription):
        self._ParameterDescription = ParameterDescription


    def _deserialize(self, params):
        self._ParameterName = params.get("ParameterName")
        self._ParameterValue = params.get("ParameterValue")
        self._ParameterDescription = params.get("ParameterDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandRequest(AbstractModel):
    r"""DeleteCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: Command ID to be deleted. call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :type CommandId: str
        """
        self._CommandId = None

    @property
    def CommandId(self):
        r"""Command ID to be deleted. call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
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
    r"""DeleteCommand response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCommandsRequest(AbstractModel):
    r"""DeleteCommands request structure.

    """

    def __init__(self):
        r"""
        :param _CommandIds: Command ID to be deleted. call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :type CommandIds: list of str
        """
        self._CommandIds = None

    @property
    def CommandIds(self):
        r"""Command ID to be deleted. call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :rtype: list of str
        """
        return self._CommandIds

    @CommandIds.setter
    def CommandIds(self, CommandIds):
        self._CommandIds = CommandIds


    def _deserialize(self, params):
        self._CommandIds = params.get("CommandIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandsResponse(AbstractModel):
    r"""DeleteCommands response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteInvokerRequest(AbstractModel):
    r"""DeleteInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Pending deletion executor ID.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        r"""Pending deletion executor ID.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
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
    r"""DeleteInvoker response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRegisterCodesRequest(AbstractModel):
    r"""DeleteRegisterCodes request structure.

    """

    def __init__(self):
        r"""
        :param _RegisterCodeIds: Registration code ID list. limits the input registration code ID quantity to more than 0 and less than 100.

Call the [DescribeRegisterCodes](https://www.tencentcloud.comom/document/api/1340/96925?from_cn_redirect=1) api to query registration codes.
        :type RegisterCodeIds: list of str
        """
        self._RegisterCodeIds = None

    @property
    def RegisterCodeIds(self):
        r"""Registration code ID list. limits the input registration code ID quantity to more than 0 and less than 100.

Call the [DescribeRegisterCodes](https://www.tencentcloud.comom/document/api/1340/96925?from_cn_redirect=1) api to query registration codes.
        :rtype: list of str
        """
        return self._RegisterCodeIds

    @RegisterCodeIds.setter
    def RegisterCodeIds(self, RegisterCodeIds):
        self._RegisterCodeIds = RegisterCodeIds


    def _deserialize(self, params):
        self._RegisterCodeIds = params.get("RegisterCodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRegisterCodesResponse(AbstractModel):
    r"""DeleteRegisterCodes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRegisterInstanceRequest(AbstractModel):
    r"""DeleteRegisterInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Managed instance ID.

Call the [DescribeRegisterInstances](https://www.tencentcloud.comom/document/api/1340/96924?from_cn_redirect=1) api to query managed instances.
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""Managed instance ID.

Call the [DescribeRegisterInstances](https://www.tencentcloud.comom/document/api/1340/96924?from_cn_redirect=1) api to query managed instances.
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
        


class DeleteRegisterInstanceResponse(AbstractModel):
    r"""DeleteRegisterInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAutomationAgentStatusRequest(AbstractModel):
    r"""DescribeAutomationAgentStatus request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: List of instance ids to be queried.

You can get the instance ID through the query instance interface of corresponding cloud services. currently supports instance types: CVM, Lighthouse, and TAT managed instances.

The maximum per request is 100.

Parameters must not be specified simultaneously `InstanceIds` and `Filters`.
        :type InstanceIds: list of str
        :param _Filters: -agent-status - String - required: no - (filter condition) filters by agent status. valid values: Online, Offline. 
-environment - String - required: no - (filter condition) query by agent runtime environment. valid values: Linux, Windows.
-instance-id - String - required: no - (filter condition) filter by instance id. you can get the instance id through the query instance API of the corresponding cloud services. currently supports instance types: CVM, Lighthouse, and managed instances.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InstanceIds` and `Filters` parameters cannot be specified at the same time.
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
        r"""List of instance ids to be queried.

You can get the instance ID through the query instance interface of corresponding cloud services. currently supports instance types: CVM, Lighthouse, and TAT managed instances.

The maximum per request is 100.

Parameters must not be specified simultaneously `InstanceIds` and `Filters`.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        r"""-agent-status - String - required: no - (filter condition) filters by agent status. valid values: Online, Offline. 
-environment - String - required: no - (filter condition) query by agent runtime environment. valid values: Linux, Windows.
-instance-id - String - required: no - (filter condition) filter by instance id. you can get the instance id through the query instance API of the corresponding cloud services. currently supports instance types: CVM, Lighthouse, and managed instances.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InstanceIds` and `Filters` parameters cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
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
    r"""DescribeAutomationAgentStatus response structure.

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
        r"""Agent information list.
        :rtype: list of AutomationAgentInfo
        """
        return self._AutomationAgentSet

    @AutomationAgentSet.setter
    def AutomationAgentSet(self, AutomationAgentSet):
        self._AutomationAgentSet = AutomationAgentSet

    @property
    def TotalCount(self):
        r"""Total number of matching agents.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeCommands request structure.

    """

    def __init__(self):
        r"""
        :param _CommandIds: List of command IDs. Up to 100 IDs are allowed for each request. `CommandIds` and `Filters` cannot be specified at the same time.
        :type CommandIds: list of str
        :param _Filters: Filter criteria

- command-id - String - required: no - (filter condition) filter by the command id.
- command-name - String - required: no - (filter condition) filter by the command name.
-command-type - String - required: no - (filtering conditions) filters by command type. valid values: SHELL, POWERSHELL, BAT.
-scene-id - String - required: no - (filter condition) filter by scenario id. obtain scenario id through the [DescribeScenes (query scenario)](https://www.tencentcloud.comom/document/api/1340/109968?from_cn_redirect=1) api.
-created-by - String - required: no - (filter condition) filter by command creator, value is TAT or USER. TAT represents public command, USER represents USER created command.
- tag-key - String - required: no - (filter condition) filter by the tag key.
- tag-value - String - required: no - (filter condition) filter by the tag value.
- tag:tag-key - String - required: no - (filter condition) filter by the tag-key - value pair. replace tag-key with a specific tag key. for usage, see example 4.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `CommandIds` and `Filters` parameters cannot be specified at the same time.
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
        r"""List of command IDs. Up to 100 IDs are allowed for each request. `CommandIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._CommandIds

    @CommandIds.setter
    def CommandIds(self, CommandIds):
        self._CommandIds = CommandIds

    @property
    def Filters(self):
        r"""Filter criteria

- command-id - String - required: no - (filter condition) filter by the command id.
- command-name - String - required: no - (filter condition) filter by the command name.
-command-type - String - required: no - (filtering conditions) filters by command type. valid values: SHELL, POWERSHELL, BAT.
-scene-id - String - required: no - (filter condition) filter by scenario id. obtain scenario id through the [DescribeScenes (query scenario)](https://www.tencentcloud.comom/document/api/1340/109968?from_cn_redirect=1) api.
-created-by - String - required: no - (filter condition) filter by command creator, value is TAT or USER. TAT represents public command, USER represents USER created command.
- tag-key - String - required: no - (filter condition) filter by the tag key.
- tag-value - String - required: no - (filter condition) filter by the tag value.
- tag:tag-key - String - required: no - (filter condition) filter by the tag-key - value pair. replace tag-key with a specific tag key. for usage, see example 4.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `CommandIds` and `Filters` parameters cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
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
    r"""DescribeCommands response structure.

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
        r"""Total number of matching commands.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CommandSet(self):
        r"""List of command details.
        :rtype: list of Command
        """
        return self._CommandSet

    @CommandSet.setter
    def CommandSet(self, CommandSet):
        self._CommandSet = CommandSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeInvocationTasks request structure.

    """

    def __init__(self):
        r"""
        :param _InvocationTaskIds: List of execution task IDs. Up to 100 IDs are allowed for each request. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :type InvocationTaskIds: list of str
        :param _Filters: Filter conditions.<br>.

-invocation-task-id - String - required: no - (filter condition) filter by executing task id.
- invocation-id - String - required: no - (filter condition) filter by the execution activity id. you can obtain it through the [DescribeInvocations](https://www.tencentcloud.comom/document/api/1340/52679?from_cn_redirect=1) api.
-instance-id - String - required: no - (filtering conditions) filter by instance id. you can get the instance id through the query instance interface of corresponding cloud services. currently supported instance types: CVM, Lighthouse, and managed instances of TAT.
-command-id - String - required: no - (filter criteria) filter by command id. obtain through the api [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1).

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InvocationTaskIds` and `Filters` parameters cannot be specified at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param _HideOutput: Whether to hide the command output result. valid values:.

-true: hide output.
- false: do not hide.
 
The default value is true.
        :type HideOutput: bool
        """
        self._InvocationTaskIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._HideOutput = None

    @property
    def InvocationTaskIds(self):
        r"""List of execution task IDs. Up to 100 IDs are allowed for each request. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._InvocationTaskIds

    @InvocationTaskIds.setter
    def InvocationTaskIds(self, InvocationTaskIds):
        self._InvocationTaskIds = InvocationTaskIds

    @property
    def Filters(self):
        r"""Filter conditions.<br>.

-invocation-task-id - String - required: no - (filter condition) filter by executing task id.
- invocation-id - String - required: no - (filter condition) filter by the execution activity id. you can obtain it through the [DescribeInvocations](https://www.tencentcloud.comom/document/api/1340/52679?from_cn_redirect=1) api.
-instance-id - String - required: no - (filtering conditions) filter by instance id. you can get the instance id through the query instance interface of corresponding cloud services. currently supported instance types: CVM, Lighthouse, and managed instances of TAT.
-command-id - String - required: no - (filter criteria) filter by command id. obtain through the api [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1).

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InvocationTaskIds` and `Filters` parameters cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def HideOutput(self):
        r"""Whether to hide the command output result. valid values:.

-true: hide output.
- false: do not hide.
 
The default value is true.
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
    r"""DescribeInvocationTasks response structure.

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
        r"""Total number of matching execution tasks.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvocationTaskSet(self):
        r"""List of execution tasks.
        :rtype: list of InvocationTask
        """
        return self._InvocationTaskSet

    @InvocationTaskSet.setter
    def InvocationTaskSet(self, InvocationTaskSet):
        self._InvocationTaskSet = InvocationTaskSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeInvocations request structure.

    """

    def __init__(self):
        r"""
        :param _InvocationIds: List of execution activity IDs. Up to 100 IDs are allowed for each request. `InvocationIds` and `Filters` cannot be specified at the same time.
        :type InvocationIds: list of str
        :param _Filters: Filter conditions.<br>.

<li> invocation-id - String - required: no - (filter condition) filter by execution activity id.</li>.
<li>command-id - String - required: no - (filter condition) filter by command id.</li>. 
<li> command-created-by - String - required: no - (filter criteria) filter by executed command type. valid values: TAT or USER. TAT represents public command, USER represents USER created command.</li>.
<li> instance-kind - String - required: no - (filtering conditions) filter by running instance type. valid values: CVM or LIGHTHOUSE. CVM represents cloud virtual machine, LIGHTHOUSE represents tencent cloud LIGHTHOUSE.</li>.
The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InvocationIds` and `Filters` parameters cannot be specified at the same time.
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
        r"""List of execution activity IDs. Up to 100 IDs are allowed for each request. `InvocationIds` and `Filters` cannot be specified at the same time.
        :rtype: list of str
        """
        return self._InvocationIds

    @InvocationIds.setter
    def InvocationIds(self, InvocationIds):
        self._InvocationIds = InvocationIds

    @property
    def Filters(self):
        r"""Filter conditions.<br>.

<li> invocation-id - String - required: no - (filter condition) filter by execution activity id.</li>.
<li>command-id - String - required: no - (filter condition) filter by command id.</li>. 
<li> command-created-by - String - required: no - (filter criteria) filter by executed command type. valid values: TAT or USER. TAT represents public command, USER represents USER created command.</li>.
<li> instance-kind - String - required: no - (filtering conditions) filter by running instance type. valid values: CVM or LIGHTHOUSE. CVM represents cloud virtual machine, LIGHTHOUSE represents tencent cloud LIGHTHOUSE.</li>.
The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InvocationIds` and `Filters` parameters cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
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
    r"""DescribeInvocations response structure.

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
        r"""Total number of matching execution activities.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvocationSet(self):
        r"""List of execution activities.
        :rtype: list of Invocation
        """
        return self._InvocationSet

    @InvocationSet.setter
    def InvocationSet(self, InvocationSet):
        self._InvocationSet = InvocationSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeInvokerRecords request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerIds: Executor ID list. the list has a cap of 100.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
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
        r"""Executor ID list. the list has a cap of 100.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
        :rtype: list of str
        """
        return self._InvokerIds

    @InvokerIds.setter
    def InvokerIds(self, InvokerIds):
        self._InvokerIds = InvokerIds

    @property
    def Limit(self):
        r"""Number of returned results. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
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
    r"""DescribeInvokerRecords response structure.

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
        r"""Number of matching records.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvokerRecordSet(self):
        r"""Execution history of an invoker.
        :rtype: list of InvokerRecord
        """
        return self._InvokerRecordSet

    @InvokerRecordSet.setter
    def InvokerRecordSet(self, InvokerRecordSet):
        self._InvokerRecordSet = InvokerRecordSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""DescribeInvokers request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerIds: Executor ID list.

The maximum per request is 100.

Parameters must not be specified simultaneously `InvokerIds` and `Filters`.

        :type InvokerIds: list of str
        :param _Filters: Filter criteria:.

- invoker-id - String - required: no - (filter condition) filter by executor id.
-command-id - String - required: no - (filter condition) filters commands by id. you can obtain the id through the [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
- invoker-type - String - required: no - (filter condition) filter by the executor type. currently only support SCHEDULE.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InvokerIds` and `Filters` parameters cannot be specified at the same time.
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
        r"""Executor ID list.

The maximum per request is 100.

Parameters must not be specified simultaneously `InvokerIds` and `Filters`.

        :rtype: list of str
        """
        return self._InvokerIds

    @InvokerIds.setter
    def InvokerIds(self, InvokerIds):
        self._InvokerIds = InvokerIds

    @property
    def Filters(self):
        r"""Filter criteria:.

- invoker-id - String - required: no - (filter condition) filter by executor id.
-command-id - String - required: no - (filter condition) filters commands by id. you can obtain the id through the [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
- invoker-type - String - required: no - (filter condition) filter by the executor type. currently only support SCHEDULE.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `InvokerIds` and `Filters` parameters cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of returned results. Default value: 20. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
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
    r"""DescribeInvokers response structure.

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
        r"""Number of matching invokers.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvokerSet(self):
        r"""Invoker information.
        :rtype: list of Invoker
        """
        return self._InvokerSet

    @InvokerSet.setter
    def InvokerSet(self, InvokerSet):
        self._InvokerSet = InvokerSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DescribeQuotasRequest(AbstractModel):
    r"""DescribeQuotas request structure.

    """

    def __init__(self):
        r"""
        :param _ResourceNames: Resource name

Value is:.

- COMMAND: COMMAND.
-REGISTER_CODE: managed instance registration code.
        :type ResourceNames: list of str
        """
        self._ResourceNames = None

    @property
    def ResourceNames(self):
        r"""Resource name

Value is:.

- COMMAND: COMMAND.
-REGISTER_CODE: managed instance registration code.
        :rtype: list of str
        """
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames


    def _deserialize(self, params):
        self._ResourceNames = params.get("ResourceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuotasResponse(AbstractModel):
    r"""DescribeQuotas response structure.

    """

    def __init__(self):
        r"""
        :param _GeneralResourceQuotaSet: Resource quota list.
        :type GeneralResourceQuotaSet: list of GeneralResourceQuotaSet
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._GeneralResourceQuotaSet = None
        self._RequestId = None

    @property
    def GeneralResourceQuotaSet(self):
        r"""Resource quota list.
        :rtype: list of GeneralResourceQuotaSet
        """
        return self._GeneralResourceQuotaSet

    @GeneralResourceQuotaSet.setter
    def GeneralResourceQuotaSet(self, GeneralResourceQuotaSet):
        self._GeneralResourceQuotaSet = GeneralResourceQuotaSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GeneralResourceQuotaSet") is not None:
            self._GeneralResourceQuotaSet = []
            for item in params.get("GeneralResourceQuotaSet"):
                obj = GeneralResourceQuotaSet()
                obj._deserialize(item)
                self._GeneralResourceQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions response structure.

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
        r"""Number of regions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        r"""Region information list
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class DescribeRegisterCodesRequest(AbstractModel):
    r"""DescribeRegisterCodes request structure.

    """

    def __init__(self):
        r"""
        :param _RegisterCodeIds: Registration code ID.

The maximum per request is 100.

Parameters must not be specified simultaneously `RegisterCodeIds` and `Filters`.
        :type RegisterCodeIds: list of str
        :param _Offset: Offset. default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results, defaults to 20, maximum value is 100.
        :type Limit: int
        """
        self._RegisterCodeIds = None
        self._Offset = None
        self._Limit = None

    @property
    def RegisterCodeIds(self):
        r"""Registration code ID.

The maximum per request is 100.

Parameters must not be specified simultaneously `RegisterCodeIds` and `Filters`.
        :rtype: list of str
        """
        return self._RegisterCodeIds

    @RegisterCodeIds.setter
    def RegisterCodeIds(self, RegisterCodeIds):
        self._RegisterCodeIds = RegisterCodeIds

    @property
    def Offset(self):
        r"""Offset. default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results, defaults to 20, maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RegisterCodeIds = params.get("RegisterCodeIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegisterCodesResponse(AbstractModel):
    r"""DescribeRegisterCodes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of queried registration codes.
        :type TotalCount: int
        :param _RegisterCodeSet: Registration code information list.
        :type RegisterCodeSet: list of RegisterCodeInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegisterCodeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of queried registration codes.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegisterCodeSet(self):
        r"""Registration code information list.
        :rtype: list of RegisterCodeInfo
        """
        return self._RegisterCodeSet

    @RegisterCodeSet.setter
    def RegisterCodeSet(self, RegisterCodeSet):
        self._RegisterCodeSet = RegisterCodeSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegisterCodeSet") is not None:
            self._RegisterCodeSet = []
            for item in params.get("RegisterCodeSet"):
                obj = RegisterCodeInfo()
                obj._deserialize(item)
                self._RegisterCodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegisterInstancesRequest(AbstractModel):
    r"""DescribeRegisterInstances request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceIds: Managed instance id.

The maximum per request is 100.

Parameters must not be specified simultaneously `InstanceIds` and `Filters`.

        :type InstanceIds: list of str
        :param _Filters: Filter list. the maximum number of `Filters` is 10 per request, and the maximum number of `Filter.Values` is 5. parameters must not be specified simultaneously for `InstanceIds` and `Filters`.


- instance-name

Filter by [managed instance name].
Type: String.
Required: No

- instance-id

Filter by [managed instance ID].
Type: String.
Required: No

- register-status

Filter by [managed instance status]. valid values: Online | Offline.
Type: String.
Required: No

- local-ip

Filter by [managed instance nic IP].
Type: String.
Required: No

- register-code-id

Filter by [managed instance registration code ID]. call the [DescribeRegisterCodes](https://www.tencentcloud.comom/document/api/1340/96925?from_cn_redirect=1) api to query registration codes.
Type: String.
Required: No

- sys-name

Filter by [operating system type]. valid values: Linux | Windows.
Type: String.
Required: No

- tag-key

Filter by [tag key].
Type: String.
Required: No

- tag-value

Filter by [tag value].
Type: String.
Required: No

- tag:tag-key

Filter by [tag key-value pair]. replace tag-key with a specific Tag key.
Type: String.
Required: No

For example, the Filter is {"Name": "tag:key1", "Values": ["v1", "v2"] }, which queries all resources belonging to tag key1:v1 or key1:v2.


        :type Filters: list of Filter
        :param _Offset: Offset. default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results, defaults to 20, maximum value is 100.
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        r"""Managed instance id.

The maximum per request is 100.

Parameters must not be specified simultaneously `InstanceIds` and `Filters`.

        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        r"""Filter list. the maximum number of `Filters` is 10 per request, and the maximum number of `Filter.Values` is 5. parameters must not be specified simultaneously for `InstanceIds` and `Filters`.


- instance-name

Filter by [managed instance name].
Type: String.
Required: No

- instance-id

Filter by [managed instance ID].
Type: String.
Required: No

- register-status

Filter by [managed instance status]. valid values: Online | Offline.
Type: String.
Required: No

- local-ip

Filter by [managed instance nic IP].
Type: String.
Required: No

- register-code-id

Filter by [managed instance registration code ID]. call the [DescribeRegisterCodes](https://www.tencentcloud.comom/document/api/1340/96925?from_cn_redirect=1) api to query registration codes.
Type: String.
Required: No

- sys-name

Filter by [operating system type]. valid values: Linux | Windows.
Type: String.
Required: No

- tag-key

Filter by [tag key].
Type: String.
Required: No

- tag-value

Filter by [tag value].
Type: String.
Required: No

- tag:tag-key

Filter by [tag key-value pair]. replace tag-key with a specific Tag key.
Type: String.
Required: No

For example, the Filter is {"Name": "tag:key1", "Values": ["v1", "v2"] }, which queries all resources belonging to tag key1:v1 or key1:v2.


        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""Offset. default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results, defaults to 20, maximum value is 100.
        :rtype: int
        """
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
        


class DescribeRegisterInstancesResponse(AbstractModel):
    r"""DescribeRegisterInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of registration codes registered by the instance.
        :type TotalCount: int
        :param _RegisterInstanceSet: List of managed instance information.
        :type RegisterInstanceSet: list of RegisterInstanceInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegisterInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""The total number of registration codes registered by the instance.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegisterInstanceSet(self):
        r"""List of managed instance information.
        :rtype: list of RegisterInstanceInfo
        """
        return self._RegisterInstanceSet

    @RegisterInstanceSet.setter
    def RegisterInstanceSet(self, RegisterInstanceSet):
        self._RegisterInstanceSet = RegisterInstanceSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RegisterInstanceSet") is not None:
            self._RegisterInstanceSet = []
            for item in params.get("RegisterInstanceSet"):
                obj = RegisterInstanceInfo()
                obj._deserialize(item)
                self._RegisterInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    r"""DescribeScenes request structure.

    """

    def __init__(self):
        r"""
        :param _SceneIds: Scene ID array.

The maximum per request is 100.

Parameters must not specify both `SceneIds` and `Filters` simultaneously.

        :type SceneIds: list of str
        :param _Filters: Filter criteria

- scene-id - String - required: no - (filter condition) filter by the scene id.
-scene-name - String - required: no - (filtering conditions) filter by scenario name.
-created-by - String - required: no - (filter criteria) filter by scene creator, currently only support TAT, representing public scenarios.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `SceneIds` and `Filters` parameters cannot be specified at the same time.
        :type Filters: list of Filter
        :param _Limit: Number of returned results, defaults to 20 with a maximum value of 100. for further introduction about `Limit`, see relevant sections in the API [overview](https://www.tencentcloud.comom/document/API/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param _Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self._SceneIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def SceneIds(self):
        r"""Scene ID array.

The maximum per request is 100.

Parameters must not specify both `SceneIds` and `Filters` simultaneously.

        :rtype: list of str
        """
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds

    @property
    def Filters(self):
        r"""Filter criteria

- scene-id - String - required: no - (filter condition) filter by the scene id.
-scene-name - String - required: no - (filtering conditions) filter by scenario name.
-created-by - String - required: no - (filter criteria) filter by scene creator, currently only support TAT, representing public scenarios.

The maximum number of `Filters` per request is 10, and that of `Filter.Values` is 5. the `SceneIds` and `Filters` parameters cannot be specified at the same time.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""Number of returned results, defaults to 20 with a maximum value of 100. for further introduction about `Limit`, see relevant sections in the API [overview](https://www.tencentcloud.comom/document/API/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
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
        


class DescribeScenesResponse(AbstractModel):
    r"""DescribeScenes response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of eligible scenarios.
        :type TotalCount: int
        :param _SceneSet: List of scenario details.
        :type SceneSet: list of Scene
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SceneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Total number of eligible scenarios.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SceneSet(self):
        r"""List of scenario details.
        :rtype: list of Scene
        """
        return self._SceneSet

    @SceneSet.setter
    def SceneSet(self, SceneSet):
        self._SceneSet = SceneSet

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SceneSet") is not None:
            self._SceneSet = []
            for item in params.get("SceneSet"):
                obj = Scene()
                obj._deserialize(item)
                self._SceneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisableInvokerRequest(AbstractModel):
    r"""DisableInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: ID of the executor to terminate.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        r"""ID of the executor to terminate.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
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
    r"""DisableInvoker response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableRegisterCodesRequest(AbstractModel):
    r"""DisableRegisterCodes request structure.

    """

    def __init__(self):
        r"""
        :param _RegisterCodeIds: Registration code ID.

Call the [DescribeRegisterCodes](https://www.tencentcloud.comom/document/api/1340/96925?from_cn_redirect=1) api to query registration codes.
        :type RegisterCodeIds: list of str
        """
        self._RegisterCodeIds = None

    @property
    def RegisterCodeIds(self):
        r"""Registration code ID.

Call the [DescribeRegisterCodes](https://www.tencentcloud.comom/document/api/1340/96925?from_cn_redirect=1) api to query registration codes.
        :rtype: list of str
        """
        return self._RegisterCodeIds

    @RegisterCodeIds.setter
    def RegisterCodeIds(self, RegisterCodeIds):
        self._RegisterCodeIds = RegisterCodeIds


    def _deserialize(self, params):
        self._RegisterCodeIds = params.get("RegisterCodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRegisterCodesResponse(AbstractModel):
    r"""DisableRegisterCodes response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableInvokerRequest(AbstractModel):
    r"""EnableInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Executor ID to be enabled.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        r"""Executor ID to be enabled.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
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
    r"""EnableInvoker response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""Describes the key-value pair filter, which is used for conditional filtering queries. for example, filter by ID, name, and status.
    - if there are multiple `Filter`s, the logical relationship between them is `AND`.
    - if there are multiple Values in the same Filter, the relationship between Values under the same Filter is logical OR.
    >
    Take the `Filters` of the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api as an example. if we need to query commands with the `command-name` "print working directory" and the `command-type` "POWERSHELL" or "BAT", it can be implemented as follows:.
    ```
    Filters.0.Name=command-name
    &Filters.0.Values.0=Print working directory.

    &Filters.1.Name=command-type
    &Filters.1.Values.0=POWERSHELL
    &Filters.1.Values.1=BAT
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
        r"""Field to be filtered.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter values of the field.
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
        


class GeneralResourceQuotaSet(AbstractModel):
    r"""User quota information.

    """

    def __init__(self):
        r"""
        :param _ResourceName: Resource name

Value is:.

- COMMAND: COMMAND.
-REGISTER_CODE: managed instance registration code.
        :type ResourceName: str
        :param _ResourceQuotaUsed: Used credit limit.
        :type ResourceQuotaUsed: int
        :param _ResourceQuotaTotal: Total quota.
        :type ResourceQuotaTotal: int
        """
        self._ResourceName = None
        self._ResourceQuotaUsed = None
        self._ResourceQuotaTotal = None

    @property
    def ResourceName(self):
        r"""Resource name

Value is:.

- COMMAND: COMMAND.
-REGISTER_CODE: managed instance registration code.
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceQuotaUsed(self):
        r"""Used credit limit.
        :rtype: int
        """
        return self._ResourceQuotaUsed

    @ResourceQuotaUsed.setter
    def ResourceQuotaUsed(self, ResourceQuotaUsed):
        self._ResourceQuotaUsed = ResourceQuotaUsed

    @property
    def ResourceQuotaTotal(self):
        r"""Total quota.
        :rtype: int
        """
        return self._ResourceQuotaTotal

    @ResourceQuotaTotal.setter
    def ResourceQuotaTotal(self, ResourceQuotaTotal):
        self._ResourceQuotaTotal = ResourceQuotaTotal


    def _deserialize(self, params):
        self._ResourceName = params.get("ResourceName")
        self._ResourceQuotaUsed = params.get("ResourceQuotaUsed")
        self._ResourceQuotaTotal = params.get("ResourceQuotaTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Invocation(AbstractModel):
    r"""Execution activity details.

    """

    def __init__(self):
        r"""
        :param _InvocationId: Execution activity ID.
        :type InvocationId: str
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _CommandName: Name of the executed command.
        :type CommandName: str
        :param _InvocationStatus: Execution task status. valid values:.

-PENDING: waiting for distribution.
- RUNNING: command RUNNING.
-Canceling.
-SUCCESS: command success.
-TIMEOUT: command timeout.
- FAILED: command FAILED.
-CANCELLED: all commands canceled.
-PARTIAL_FAILED: the command partially failed.
-PARTIAL_CANCELLED: the command is partially canceled.
        :type InvocationStatus: str
        :param _InvocationTaskBasicInfoSet: Execution task information list.
        :type InvocationTaskBasicInfoSet: list of InvocationTaskBasicInfo
        :param _Description: Execution activity description.
        :type Description: str
        :param _StartTime: Execute the activity start time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type StartTime: str
        :param _EndTime: Execute activity end time. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _CreatedTime: Execution activity createtime. format: YYYY-MM-DDThh:MM:ssZ.
        :type CreatedTime: str
        :param _UpdatedTime: Update time of the execution activity. the format is YYYY-MM-DDThh:MM:ssZ.
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

-USER: originate from user invocation.
-INVOKER: originate from scheduled execution.
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
        self._CommandName = None
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
        r"""Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def CommandId(self):
        r"""Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CommandName(self):
        r"""Name of the executed command.
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def InvocationStatus(self):
        r"""Execution task status. valid values:.

-PENDING: waiting for distribution.
- RUNNING: command RUNNING.
-Canceling.
-SUCCESS: command success.
-TIMEOUT: command timeout.
- FAILED: command FAILED.
-CANCELLED: all commands canceled.
-PARTIAL_FAILED: the command partially failed.
-PARTIAL_CANCELLED: the command is partially canceled.
        :rtype: str
        """
        return self._InvocationStatus

    @InvocationStatus.setter
    def InvocationStatus(self, InvocationStatus):
        self._InvocationStatus = InvocationStatus

    @property
    def InvocationTaskBasicInfoSet(self):
        r"""Execution task information list.
        :rtype: list of InvocationTaskBasicInfo
        """
        return self._InvocationTaskBasicInfoSet

    @InvocationTaskBasicInfoSet.setter
    def InvocationTaskBasicInfoSet(self, InvocationTaskBasicInfoSet):
        self._InvocationTaskBasicInfoSet = InvocationTaskBasicInfoSet

    @property
    def Description(self):
        r"""Execution activity description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StartTime(self):
        r"""Execute the activity start time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Execute activity end time. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        r"""Execution activity createtime. format: YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""Update time of the execution activity. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Parameters(self):
        r"""Values of custom parameters.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def DefaultParameters(self):
        r"""Default custom parameter value.
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def InstanceKind(self):
        r"""Type of the instance executing the command. Valid values: `CVM`, `LIGHTHOUSE`.
        :rtype: str
        """
        return self._InstanceKind

    @InstanceKind.setter
    def InstanceKind(self, InstanceKind):
        self._InstanceKind = InstanceKind

    @property
    def Username(self):
        r"""The user who executes the command on the instance.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def InvocationSource(self):
        r"""Invocation source.

-USER: originate from user invocation.
-INVOKER: originate from scheduled execution.
        :rtype: str
        """
        return self._InvocationSource

    @InvocationSource.setter
    def InvocationSource(self, InvocationSource):
        self._InvocationSource = InvocationSource

    @property
    def CommandContent(self):
        r"""Base64-encoded command
        :rtype: str
        """
        return self._CommandContent

    @CommandContent.setter
    def CommandContent(self, CommandContent):
        self._CommandContent = CommandContent

    @property
    def CommandType(self):
        r"""Command type
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def Timeout(self):
        r"""Command timeout period, in seconds.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def WorkingDirectory(self):
        r"""Working directory for executing the command.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def OutputCOSBucketUrl(self):
        r"""The COS bucket URL for uploading logs.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        r"""The COS bucket directory where the logs are saved.
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._InvocationId = params.get("InvocationId")
        self._CommandId = params.get("CommandId")
        self._CommandName = params.get("CommandName")
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
    r"""Execution task.

    """

    def __init__(self):
        r"""
        :param _InvocationId: Execution activity ID.
        :type InvocationId: str
        :param _InvocationTaskId: Execution task ID.
        :type InvocationTaskId: str
        :param _CommandId: Command ID.
        :type CommandId: str
        :param _TaskStatus: Execution task status. valid values:.

-PENDING: waiting for distribution.
-DELIVERING: distributing.
-DELIVER_DELAYED: delivery delay.
-DELIVER_FAILED: delivery fail.
-START_FAILED: command start failed.
- RUNNING: command RUNNING.
-SUCCESS: command success.
-FAILED: command execution failed, exit code not 0.
-TIMEOUT: command timeout.
-TASK_TIMEOUT: client no response.
-Canceling.
- CANCELLED: canceled (command canceled before startup).
-TERMINATED: suspended (canceled during command execution).
        :type TaskStatus: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        :param _TaskResult: Execution result.
        :type TaskResult: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        :param _StartTime: Task start time. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: Task end time. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _CreatedTime: Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type CreatedTime: str
        :param _UpdatedTime: Update time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type UpdatedTime: str
        :param _CommandDocument: Command details of the execution task.
        :type CommandDocument: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        :param _ErrorInfo: Error message displayed when the execution task fails.
        :type ErrorInfo: str
        :param _InvocationSource: Invocation source.

-USER: originate from user invocation.
-INVOKER: originate from scheduled execution.
        :type InvocationSource: str
        :param _CommandName: Name of the executed command.
        :type CommandName: str
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
        self._CommandName = None

    @property
    def InvocationId(self):
        r"""Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvocationTaskId(self):
        r"""Execution task ID.
        :rtype: str
        """
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def CommandId(self):
        r"""Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def TaskStatus(self):
        r"""Execution task status. valid values:.

-PENDING: waiting for distribution.
-DELIVERING: distributing.
-DELIVER_DELAYED: delivery delay.
-DELIVER_FAILED: delivery fail.
-START_FAILED: command start failed.
- RUNNING: command RUNNING.
-SUCCESS: command success.
-FAILED: command execution failed, exit code not 0.
-TIMEOUT: command timeout.
-TASK_TIMEOUT: client no response.
-Canceling.
- CANCELLED: canceled (command canceled before startup).
-TERMINATED: suspended (canceled during command execution).
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def InstanceId(self):
        r"""Instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskResult(self):
        r"""Execution result.
        :rtype: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

    @property
    def StartTime(self):
        r"""Task start time. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Task end time. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        r"""Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""Update time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def CommandDocument(self):
        r"""Command details of the execution task.
        :rtype: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        """
        return self._CommandDocument

    @CommandDocument.setter
    def CommandDocument(self, CommandDocument):
        self._CommandDocument = CommandDocument

    @property
    def ErrorInfo(self):
        r"""Error message displayed when the execution task fails.
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def InvocationSource(self):
        r"""Invocation source.

-USER: originate from user invocation.
-INVOKER: originate from scheduled execution.
        :rtype: str
        """
        return self._InvocationSource

    @InvocationSource.setter
    def InvocationSource(self, InvocationSource):
        self._InvocationSource = InvocationSource

    @property
    def CommandName(self):
        r"""Name of the executed command.
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName


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
        self._CommandName = params.get("CommandName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTaskBasicInfo(AbstractModel):
    r"""Execution task description.

    """

    def __init__(self):
        r"""
        :param _InvocationTaskId: Execution task ID.
        :type InvocationTaskId: str
        :param _TaskStatus: Execution task status. valid values:.

-PENDING: waiting for distribution.
-DELIVERING: distributing.
-DELIVER_DELAYED: delivery delay.
-DELIVER_FAILED: delivery fail.
-START_FAILED: command start failed.
- RUNNING: command RUNNING.
-SUCCESS: command success.
-FAILED: command execution failed, exit code not 0.
-TIMEOUT: command timeout.
-TASK_TIMEOUT: client no response.
-Canceling.
- CANCELLED: canceled (command canceled before startup).
-TERMINATED: suspended (canceled during command execution).
        :type TaskStatus: str
        :param _InstanceId: Instance ID.
        :type InstanceId: str
        """
        self._InvocationTaskId = None
        self._TaskStatus = None
        self._InstanceId = None

    @property
    def InvocationTaskId(self):
        r"""Execution task ID.
        :rtype: str
        """
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def TaskStatus(self):
        r"""Execution task status. valid values:.

-PENDING: waiting for distribution.
-DELIVERING: distributing.
-DELIVER_DELAYED: delivery delay.
-DELIVER_FAILED: delivery fail.
-START_FAILED: command start failed.
- RUNNING: command RUNNING.
-SUCCESS: command success.
-FAILED: command execution failed, exit code not 0.
-TIMEOUT: command timeout.
-TASK_TIMEOUT: client no response.
-Canceling.
- CANCELLED: canceled (command canceled before startup).
-TERMINATED: suspended (canceled during command execution).
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def InstanceId(self):
        r"""Instance ID.
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
    r"""InvokeCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: Pending trigger command ID. call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :type CommandId: str
        :param _InstanceIds: Instance ID list for the command to be executed, with a cap of 200.

Instance ID can be obtained through the query instance interface of corresponding cloud services. currently supported instance types:.
- CVM
- Lighthouse
-TAT register instance.
        :type InstanceIds: list of str
        :param _Parameters: Custom parameter of Command. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
This parameter can be set only when the EnableParameter of the command is true. you can obtain the EnableParameter settings through the [DescribeCommands (detailed command information)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
If the parameter value is not provided, the DefaultParameters or DefaultParameterConfs of Command will be used to replace it.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
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
        r"""Pending trigger command ID. call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InstanceIds(self):
        r"""Instance ID list for the command to be executed, with a cap of 200.

Instance ID can be obtained through the query instance interface of corresponding cloud services. currently supported instance types:.
- CVM
- Lighthouse
-TAT register instance.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Parameters(self):
        r"""Custom parameter of Command. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
This parameter can be set only when the EnableParameter of the command is true. you can obtain the EnableParameter settings through the [DescribeCommands (detailed command information)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
If the parameter value is not provided, the DefaultParameters or DefaultParameterConfs of Command will be used to replace it.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Username(self):
        r"""The username used to execute the command on the CVM or Lighthouse instance.
The principle of the least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. If this is not specified, the Username of the command is used by default.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def WorkingDirectory(self):
        r"""Execution path of the command. The WorkingDirectory of the command is used by default.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        r"""Command timeout period. Value range: [1, 86400]. The Timeout of the command is used by default.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def OutputCOSBucketUrl(self):
        r"""The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        r"""The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
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
    r"""InvokeCommand response structure.

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
        r"""Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""Invoker information.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Invoker ID.
        :type InvokerId: str
        :param _Name: Invoker name.
        :type Name: str
        :param _Type: Executor type. currently only support SCHEDULE.
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
        :param _ScheduleSettings: Executor periodic schedule. recurring invoker will return this field.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        :param _CreatedTime: Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type CreatedTime: str
        :param _UpdatedTime: Last modified. the format is YYYY-MM-DDThh:MM:ssZ.
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
        r"""Invoker ID.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def Name(self):
        r"""Invoker name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Executor type. currently only support SCHEDULE.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        r"""Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Username(self):
        r"""Username.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        r"""Custom parameters.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def InstanceIds(self):
        r"""Instance ID list.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Enable(self):
        r"""Whether to enable the invoker.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ScheduleSettings(self):
        r"""Executor periodic schedule. recurring invoker will return this field.
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings

    @property
    def CreatedTime(self):
        r"""Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""Last modified. the format is YYYY-MM-DDThh:MM:ssZ.
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
    r"""Execution history of the invoker.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Invoker ID.
        :type InvokerId: str
        :param _InvokeTime: Execution time. format: YYYY-MM-DDThh:MM:ssZ.
        :type InvokeTime: str
        :param _Reason: Execution reason.
        :type Reason: str
        :param _InvocationId: Command execution ID.
        :type InvocationId: str
        :param _Result: Trigger result.

-PENDING: waiting for distribution.
- RUNNING: command RUNNING.
-Canceling.
-SUCCESS: command success.
-TIMEOUT: command timeout.
- FAILED: command FAILED.
-CANCELLED: all commands canceled.
-PARTIAL_FAILED: the command partially failed.
-PARTIAL_CANCELLED: the command is partially canceled.
        :type Result: str
        """
        self._InvokerId = None
        self._InvokeTime = None
        self._Reason = None
        self._InvocationId = None
        self._Result = None

    @property
    def InvokerId(self):
        r"""Invoker ID.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def InvokeTime(self):
        r"""Execution time. format: YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._InvokeTime

    @InvokeTime.setter
    def InvokeTime(self, InvokeTime):
        self._InvokeTime = InvokeTime

    @property
    def Reason(self):
        r"""Execution reason.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def InvocationId(self):
        r"""Command execution ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def Result(self):
        r"""Trigger result.

-PENDING: waiting for distribution.
- RUNNING: command RUNNING.
-Canceling.
-SUCCESS: command success.
-TIMEOUT: command timeout.
- FAILED: command FAILED.
-CANCELLED: all commands canceled.
-PARTIAL_FAILED: the command partially failed.
-PARTIAL_CANCELLED: the command is partially canceled.
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
    r"""ModifyCommand request structure.

    """

    def __init__(self):
        r"""
        :param _CommandId: <p>Command ID. call the <a href="https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1">DescribeCommands</a> api to query command details.</p>.
        :type CommandId: str
        :param _CommandName: <p>Command name. name only supports chinese, english, digits, underscore, separator "-", and decimal point. the maximum length cannot exceed 60 bytes.</p>.
        :type CommandName: str
        :param _Description: <P>Command description. no more than 120 characters.</p>.
        :type Description: str
        :param _Content: <p>The Base64-encoded command content, length cannot exceed 64KB.</p>.
        :type Content: str
        :param _CommandType: <p>Command type. currently supports SHELL, POWERSHELL, BAT.</p>.
        :type CommandType: str
        :param _WorkingDirectory: <P>Command execution path.</p>.
        :type WorkingDirectory: str
        :param _Timeout: <p>Command timeout time.</p><p>value range: [1, 86400].</p><p>unit: seconds.</p><p>default value: 60.</p><p>when specifying the OutputCOSBucketUrl parameter, the timeout period includes the time taken to upload command output to COS.</p>.
        :type Timeout: int
        :param _DefaultParameters: <p>The default value of custom parameters when the custom parameter feature is enabled. the field type is a json-encoded string, for example: {"varA": "222"}.<br>parameters must not be specified simultaneously for <code>DefaultParameters</code> and <code>DefaultParameterConfs</code>.<br>a comprehensive modification is applied, meaning all new default values must be provided when modifying.<br>this parameter can be modified only when EnableParameter of the command is true. obtain the EnableParameter settings of the command through the <a href="https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1">DescribeCommands (query command details)</a> api.<br>the key is the custom parameter name, and the value is the default value of this parameter. both key and value are string-type.<br>there is an upper limit of 20 custom parameters.<br>custom parameter names must meet the following requirements: the upper limit of character quantity is 64, and the optional range is [a-zA-Z0-9-_].</p>.
        :type DefaultParameters: str
        :param _DefaultParameterConfs: <p>Custom parameter array. if no parameter value is provided when invoking the command, the default value here will be used to replace it.<br>parameters do not support specifying both <code>DefaultParameters</code> and <code>DefaultParameterConfs</code>.<br>this parameter can be modified only when EnableParameter of the command is true. obtain the EnableParameter settings through the <a href="https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1">DescribeCommands (query command details)</a> api.<br>up to 20 custom parameters are allowed.</p>.
        :type DefaultParameterConfs: list of DefaultParameterConf
        :param _Username: <p>The username to run commands in a CVM or Lighthouse instance.<br>using minimum permission to execute commands is the best practice for permission management. we recommend running cloud assistant commands as a regular user identity.</p>.
        :type Username: str
        :param _OutputCOSBucketUrl: <p>Specifies the cos bucket address for the uploaded log, which must start with https, such as https://BucketName-123454321.cos.ap-beijing.myqcloud.com.</p>.
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: <P>Specify the directory for logs in the cos bucket. the directory naming has the following rules:</p><ol><li>use a combination of numbers, chinese and english, and visible characters, with a maximum length of 60.</li><li>use / to split the path and quickly create subdirectories.</li><li>consecutive / are not allowed; cannot start with /; cannot use .. as the folder name.</li></ol>.
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
        self._DefaultParameterConfs = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        r"""<p>Command ID. call the <a href="https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1">DescribeCommands</a> api to query command details.</p>.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CommandName(self):
        r"""<p>Command name. name only supports chinese, english, digits, underscore, separator "-", and decimal point. the maximum length cannot exceed 60 bytes.</p>.
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        r"""<P>Command description. no more than 120 characters.</p>.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        r"""<p>The Base64-encoded command content, length cannot exceed 64KB.</p>.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        r"""<p>Command type. currently supports SHELL, POWERSHELL, BAT.</p>.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        r"""<P>Command execution path.</p>.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        r"""<p>Command timeout time.</p><p>value range: [1, 86400].</p><p>unit: seconds.</p><p>default value: 60.</p><p>when specifying the OutputCOSBucketUrl parameter, the timeout period includes the time taken to upload command output to COS.</p>.
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def DefaultParameters(self):
        r"""<p>The default value of custom parameters when the custom parameter feature is enabled. the field type is a json-encoded string, for example: {"varA": "222"}.<br>parameters must not be specified simultaneously for <code>DefaultParameters</code> and <code>DefaultParameterConfs</code>.<br>a comprehensive modification is applied, meaning all new default values must be provided when modifying.<br>this parameter can be modified only when EnableParameter of the command is true. obtain the EnableParameter settings of the command through the <a href="https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1">DescribeCommands (query command details)</a> api.<br>the key is the custom parameter name, and the value is the default value of this parameter. both key and value are string-type.<br>there is an upper limit of 20 custom parameters.<br>custom parameter names must meet the following requirements: the upper limit of character quantity is 64, and the optional range is [a-zA-Z0-9-_].</p>.
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        r"""<p>Custom parameter array. if no parameter value is provided when invoking the command, the default value here will be used to replace it.<br>parameters do not support specifying both <code>DefaultParameters</code> and <code>DefaultParameterConfs</code>.<br>this parameter can be modified only when EnableParameter of the command is true. obtain the EnableParameter settings through the <a href="https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1">DescribeCommands (query command details)</a> api.<br>up to 20 custom parameters are allowed.</p>.
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Username(self):
        r"""<p>The username to run commands in a CVM or Lighthouse instance.<br>using minimum permission to execute commands is the best practice for permission management. we recommend running cloud assistant commands as a regular user identity.</p>.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        r"""<p>Specifies the cos bucket address for the uploaded log, which must start with https, such as https://BucketName-123454321.cos.ap-beijing.myqcloud.com.</p>.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        r"""<P>Specify the directory for logs in the cos bucket. the directory naming has the following rules:</p><ol><li>use a combination of numbers, chinese and english, and visible characters, with a maximum length of 60.</li><li>use / to split the path and quickly create subdirectories.</li><li>consecutive / are not allowed; cannot start with /; cannot use .. as the folder name.</li></ol>.
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
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
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
    r"""ModifyCommand response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyInvokerRequest(AbstractModel):
    r"""ModifyInvoker request structure.

    """

    def __init__(self):
        r"""
        :param _InvokerId: Executor ID to be modified.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
        :type InvokerId: str
        :param _Name: Executor name to be modified. length not exceeding 120 characters.
        :type Name: str
        :param _Type: Executor type to be modified.

Selectable values (currently only support one):.

-`SCHEDULE`: period type executor.
        :type Type: str
        :param _CommandId: Command ID to be modified.

Call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :type CommandId: str
        :param _Username: Username to be modified. length not exceeding 256 characters.
        :type Username: str
        :param _Parameters: Custom parameters to be modified. field type is JSON encode string.

This parameter can be set only when EnableParameter of the command specified by CommandId is true. obtain the EnableParameter settings through the [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
        :type Parameters: str
        :param _InstanceIds: List of instance ids to be modified. list length limit 100.

You can get the instance ID through the query instance interface of corresponding cloud services. currently supports instance types: CVM, Lighthouse, and TAT managed instances.

The instance needs to have the TAT client installed, and the client must be in Online status. you can query client status via the [DescribeAutomationAgentStatus](https://www.tencentcloud.comom/document/api/1340/52682?from_cn_redirect=1) api.
        :type InstanceIds: list of str
        :param _ScheduleSettings: Recurring invoker settings to be modified.

Change the executor type to `SCHEDULE` and specify this parameter.
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
        r"""Executor ID to be modified.

Call the [DescribeInvokers](https://www.tencentcloud.comom/document/api/1340/61759?from_cn_redirect=1) api to query execution.
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def Name(self):
        r"""Executor name to be modified. length not exceeding 120 characters.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Executor type to be modified.

Selectable values (currently only support one):.

-`SCHEDULE`: period type executor.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        r"""Command ID to be modified.

Call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Username(self):
        r"""Username to be modified. length not exceeding 256 characters.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        r"""Custom parameters to be modified. field type is JSON encode string.

This parameter can be set only when EnableParameter of the command specified by CommandId is true. obtain the EnableParameter settings through the [DescribeCommands (query command details)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def InstanceIds(self):
        r"""List of instance ids to be modified. list length limit 100.

You can get the instance ID through the query instance interface of corresponding cloud services. currently supports instance types: CVM, Lighthouse, and TAT managed instances.

The instance needs to have the TAT client installed, and the client must be in Online status. you can query client status via the [DescribeAutomationAgentStatus](https://www.tencentcloud.comom/document/api/1340/52682?from_cn_redirect=1) api.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ScheduleSettings(self):
        r"""Recurring invoker settings to be modified.

Change the executor type to `SCHEDULE` and specify this parameter.
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
    r"""ModifyInvoker response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRegisterInstanceRequest(AbstractModel):
    r"""ModifyRegisterInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Managed instance ID.

Call the [DescribeRegisterInstances](https://www.tencentcloud.comom/document/api/1340/96924?from_cn_redirect=1) api to query managed instances.
        :type InstanceId: str
        :param _InstanceName: Instance name. valid length is 1–60 characters.
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        r"""Managed instance ID.

Call the [DescribeRegisterInstances](https://www.tencentcloud.comom/document/api/1340/96924?from_cn_redirect=1) api to query managed instances.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Instance name. valid length is 1–60 characters.
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
        


class ModifyRegisterInstanceResponse(AbstractModel):
    r"""ModifyRegisterInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PreviewReplacedCommandContentRequest(AbstractModel):
    r"""PreviewReplacedCommandContent request structure.

    """

    def __init__(self):
        r"""
        :param _Parameters: The preview uses custom parameters. field type is json encoded string, for example: {"varA": "222"}.
This parameter can be set only when the EnableParameter of the command is true. you can obtain the EnableParameter settings through the [DescribeCommands (detailed command information)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
If DefaultParameters or DefaultParameterConfs has set, it will overlay with Parameters and prioritize the value of Parameters.

key specifies the custom parameter name, and value specifies the parameter. both kv are string-type.
Custom parameters are limited to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
If the previewed CommandId has DefaultParameters set, this parameter can be empty.
        :type Parameters: str
        :param _CommandId: Perform the replace preview command.
Call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
CommandId and Content, you must provide one and can only provide one.
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
        r"""The preview uses custom parameters. field type is json encoded string, for example: {"varA": "222"}.
This parameter can be set only when the EnableParameter of the command is true. you can obtain the EnableParameter settings through the [DescribeCommands (detailed command information)](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api.
If DefaultParameters or DefaultParameterConfs has set, it will overlay with Parameters and prioritize the value of Parameters.

key specifies the custom parameter name, and value specifies the parameter. both kv are string-type.
Custom parameters are limited to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
If the previewed CommandId has DefaultParameters set, this parameter can be empty.
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def CommandId(self):
        r"""Perform the replace preview command.
Call the [DescribeCommands](https://www.tencentcloud.comom/document/api/1340/52681?from_cn_redirect=1) api to query command details.
CommandId and Content, you must provide one and can only provide one.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Content(self):
        r"""Base64-encoded command to be previewed. The maximum length is 64 KB.
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
    r"""PreviewReplacedCommandContent response structure.

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
        r"""Base64-encoded command with custom parameters.
        :rtype: str
        """
        return self._ReplacedContent

    @ReplacedContent.setter
    def ReplacedContent(self, ReplacedContent):
        self._ReplacedContent = ReplacedContent

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
    r"""Information of a region.

    """

    def __init__(self):
        r"""
        :param _Region: Region name, such as `ap-guangzhou`
        :type Region: str
        :param _RegionName: Region description, such as `Guangzhou`
        :type RegionName: str
        :param _RegionState: Region availability status. AVAILABLE indicates the region is AVAILABLE. UNAVAILABLE indicates the region is UNAVAILABLE.
        :type RegionState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None

    @property
    def Region(self):
        r"""Region name, such as `ap-guangzhou`
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""Region description, such as `Guangzhou`
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        r"""Region availability status. AVAILABLE indicates the region is AVAILABLE. UNAVAILABLE indicates the region is UNAVAILABLE.
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
        


class RegisterCodeInfo(AbstractModel):
    r"""Register code info.

    """

    def __init__(self):
        r"""
        :param _RegisterCodeId: Registration code ID.
        :type RegisterCodeId: str
        :param _Description: Describes the registration code.
        :type Description: str
        :param _InstanceNamePrefix: Prefix of the registered instance name.
        :type InstanceNamePrefix: str
        :param _RegisterLimit: The number of instances the registration code allows.
        :type RegisterLimit: int
        :param _ExpiredTime: The expiry date of the registration code is in ISO8601 standard representation and uses UTC time. 
The format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpiredTime: str
        :param _IpAddressRange: The registration code limits tat_agent to register only from the public outbound ip described by IpAddressRange.
        :type IpAddressRange: str
        :param _Enabled: Is the registration code available.
        :type Enabled: bool
        :param _RegisteredCount: The number of registered registration codes.
        :type RegisteredCount: int
        :param _CreatedTime: Registration code creation time, represented as ISO8601 standard and using UTC time. 
The format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param _UpdatedTime: Last update time of the registration code, as ISO8601 standard representation and using UTC time. 
The format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedTime: str
        """
        self._RegisterCodeId = None
        self._Description = None
        self._InstanceNamePrefix = None
        self._RegisterLimit = None
        self._ExpiredTime = None
        self._IpAddressRange = None
        self._Enabled = None
        self._RegisteredCount = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def RegisterCodeId(self):
        r"""Registration code ID.
        :rtype: str
        """
        return self._RegisterCodeId

    @RegisterCodeId.setter
    def RegisterCodeId(self, RegisterCodeId):
        self._RegisterCodeId = RegisterCodeId

    @property
    def Description(self):
        r"""Describes the registration code.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceNamePrefix(self):
        r"""Prefix of the registered instance name.
        :rtype: str
        """
        return self._InstanceNamePrefix

    @InstanceNamePrefix.setter
    def InstanceNamePrefix(self, InstanceNamePrefix):
        self._InstanceNamePrefix = InstanceNamePrefix

    @property
    def RegisterLimit(self):
        r"""The number of instances the registration code allows.
        :rtype: int
        """
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def ExpiredTime(self):
        r"""The expiry date of the registration code is in ISO8601 standard representation and uses UTC time. 
The format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def IpAddressRange(self):
        r"""The registration code limits tat_agent to register only from the public outbound ip described by IpAddressRange.
        :rtype: str
        """
        return self._IpAddressRange

    @IpAddressRange.setter
    def IpAddressRange(self, IpAddressRange):
        self._IpAddressRange = IpAddressRange

    @property
    def Enabled(self):
        r"""Is the registration code available.
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def RegisteredCount(self):
        r"""The number of registered registration codes.
        :rtype: int
        """
        return self._RegisteredCount

    @RegisteredCount.setter
    def RegisteredCount(self, RegisteredCount):
        self._RegisteredCount = RegisteredCount

    @property
    def CreatedTime(self):
        r"""Registration code creation time, represented as ISO8601 standard and using UTC time. 
The format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""Last update time of the registration code, as ISO8601 standard representation and using UTC time. 
The format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._RegisterCodeId = params.get("RegisterCodeId")
        self._Description = params.get("Description")
        self._InstanceNamePrefix = params.get("InstanceNamePrefix")
        self._RegisterLimit = params.get("RegisterLimit")
        self._ExpiredTime = params.get("ExpiredTime")
        self._IpAddressRange = params.get("IpAddressRange")
        self._Enabled = params.get("Enabled")
        self._RegisteredCount = params.get("RegisteredCount")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterInstanceInfo(AbstractModel):
    r"""Register instance info.

    """

    def __init__(self):
        r"""
        :param _RegisterCodeId: Registration code ID.
        :type RegisterCodeId: str
        :param _InstanceId: Managed instance ID.
        :type InstanceId: str
        :param _InstanceName: Managed instance name.
        :type InstanceName: str
        :param _MachineId: Machine ID.
        :type MachineId: str
        :param _SystemName: System name. valid values: Linux | Windows.
        :type SystemName: str
        :param _HostName: Host name.
        :type HostName: str
        :param _LocalIp: Private network IP
        :type LocalIp: str
        :param _PublicKey: Public key.
        :type PublicKey: str
        :param _Status: Hosting status.
Return Online means the instance is managed, return Offline means the instance is unhosted.
        :type Status: str
        :param _CreatedTime: Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type CreatedTime: str
        :param _UpdatedTime: Last update time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type UpdatedTime: str
        :param _Tags: Tag.
        :type Tags: list of Tag
        """
        self._RegisterCodeId = None
        self._InstanceId = None
        self._InstanceName = None
        self._MachineId = None
        self._SystemName = None
        self._HostName = None
        self._LocalIp = None
        self._PublicKey = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Tags = None

    @property
    def RegisterCodeId(self):
        r"""Registration code ID.
        :rtype: str
        """
        return self._RegisterCodeId

    @RegisterCodeId.setter
    def RegisterCodeId(self, RegisterCodeId):
        self._RegisterCodeId = RegisterCodeId

    @property
    def InstanceId(self):
        r"""Managed instance ID.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""Managed instance name.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def MachineId(self):
        r"""Machine ID.
        :rtype: str
        """
        return self._MachineId

    @MachineId.setter
    def MachineId(self, MachineId):
        self._MachineId = MachineId

    @property
    def SystemName(self):
        r"""System name. valid values: Linux | Windows.
        :rtype: str
        """
        return self._SystemName

    @SystemName.setter
    def SystemName(self, SystemName):
        self._SystemName = SystemName

    @property
    def HostName(self):
        r"""Host name.
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def LocalIp(self):
        r"""Private network IP
        :rtype: str
        """
        return self._LocalIp

    @LocalIp.setter
    def LocalIp(self, LocalIp):
        self._LocalIp = LocalIp

    @property
    def PublicKey(self):
        r"""Public key.
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Status(self):
        r"""Hosting status.
Return Online means the instance is managed, return Offline means the instance is unhosted.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        r"""Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""Last update time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Tags(self):
        r"""Tag.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RegisterCodeId = params.get("RegisterCodeId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._MachineId = params.get("MachineId")
        self._SystemName = params.get("SystemName")
        self._HostName = params.get("HostName")
        self._LocalIp = params.get("LocalIp")
        self._PublicKey = params.get("PublicKey")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
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
        


class RunCommandRequest(AbstractModel):
    r"""RunCommand request structure.

    """

    def __init__(self):
        r"""
        :param _Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param _InstanceIds: Instance ID list for the command to be executed, with a cap of 200.

Instance ID can be obtained through the query instance interface of corresponding cloud services. currently supported instance types:.
- CVM
- Lighthouse
-TAT register instance.
        :type InstanceIds: list of str
        :param _CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param _Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param _CommandType: Command type. currently supports SHELL, POWERSHELL, BAT. default: SHELL.
        :type CommandType: str
        :param _WorkingDirectory: Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :type WorkingDirectory: str
        :param _Timeout: Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :type Timeout: int
        :param _SaveCommand: Whether to save the command. value range:.
<li>true: save</li>.
<li>false: not saved.</li>.
The default value is false.
        :type SaveCommand: bool
        :param _EnableParameter: Whether to enable the custom parameter feature.
Once created, this value does not offer modification.
Valid values:.
<li>true: enable</li>.
<li>false: disabled.</li>.
The default value is false.
        :type EnableParameter: bool
        :param _DefaultParameters: Enable the custom parameter feature. default value of the custom parameter. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
This parameter can be set only when the EnableParameter of the command is true.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
If Parameters is not provided, the default value here will be used to replace.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
        :type DefaultParameters: str
        :param _DefaultParameterConfs: Custom parameter array. if Parameters is not provided, the default value here will be used to replace. up to 20 custom Parameters are allowed.
If Parameters is not provided, the default value here will be used to replace.
This parameter can be set only when the EnableParameter of the command is true.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
        :type DefaultParameterConfs: list of DefaultParameterConf
        :param _Parameters: Custom parameter of Command. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
This parameter can be set only when the EnableParameter of the command is true.
If the parameter value is not provided, DefaultParameters or DefaultParameterConfs will be used.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
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
        self._DefaultParameterConfs = None
        self._Parameters = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def Content(self):
        r"""Base64-encoded command. The maximum length is 64 KB.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def InstanceIds(self):
        r"""Instance ID list for the command to be executed, with a cap of 200.

Instance ID can be obtained through the query instance interface of corresponding cloud services. currently supported instance types:.
- CVM
- Lighthouse
-TAT register instance.
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def CommandName(self):
        r"""Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        r"""Command description. The maximum length is 120 characters.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CommandType(self):
        r"""Command type. currently supports SHELL, POWERSHELL, BAT. default: SHELL.
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        r"""Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        r"""Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def SaveCommand(self):
        r"""Whether to save the command. value range:.
<li>true: save</li>.
<li>false: not saved.</li>.
The default value is false.
        :rtype: bool
        """
        return self._SaveCommand

    @SaveCommand.setter
    def SaveCommand(self, SaveCommand):
        self._SaveCommand = SaveCommand

    @property
    def EnableParameter(self):
        r"""Whether to enable the custom parameter feature.
Once created, this value does not offer modification.
Valid values:.
<li>true: enable</li>.
<li>false: disabled.</li>.
The default value is false.
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        r"""Enable the custom parameter feature. default value of the custom parameter. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
This parameter can be set only when the EnableParameter of the command is true.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
If Parameters is not provided, the default value here will be used to replace.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        r"""Custom parameter array. if Parameters is not provided, the default value here will be used to replace. up to 20 custom Parameters are allowed.
If Parameters is not provided, the default value here will be used to replace.
This parameter can be set only when the EnableParameter of the command is true.
Parameters must not be specified simultaneously `DefaultParameters` and `DefaultParameterConfs`.
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Parameters(self):
        r"""Custom parameter of Command. field type is json encoded string. for example: {"varA": "222"}.
The key is the custom parameter name, and the value is the default. both kv are string-type.
This parameter can be set only when the EnableParameter of the command is true.
If the parameter value is not provided, DefaultParameters or DefaultParameterConfs will be used.
Custom parameters can be up to 20.
The custom parameter name must meet the following standard: the number of characters has a cap of 64, and the optional range is [a-zA-Z0-9-_].
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Tags(self):
        r"""The tags of the command. It is available when `SaveCommand` is `True`. A maximum of 10 tags are allowed.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        r"""The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the user `root` is used to execute commands on Linux and the user `System` is used on Windows.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        r"""The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        r"""The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
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
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
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
    r"""RunCommand response structure.

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
        r"""Command ID.
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InvocationId(self):
        r"""Execution activity ID.
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def RequestId(self):
        r"""The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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


class Scene(AbstractModel):
    r"""Scenario details.

    """

    def __init__(self):
        r"""
        :param _SceneId: Scene ID.
        :type SceneId: str
        :param _SceneName: Scenario name.
        :type SceneName: str
        :param _CreatedBy: Scene creator.

- TAT: public scenario.
        :type CreatedBy: str
        :param _CreatedTime: Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type CreatedTime: str
        :param _UpdatedTime: Update time. the format is YYYY-MM-DDThh:MM:ssZ.
        :type UpdatedTime: str
        """
        self._SceneId = None
        self._SceneName = None
        self._CreatedBy = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def SceneId(self):
        r"""Scene ID.
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def SceneName(self):
        r"""Scenario name.
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def CreatedBy(self):
        r"""Scene creator.

- TAT: public scenario.
        :rtype: str
        """
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreatedTime(self):
        r"""Creation time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""Update time. the format is YYYY-MM-DDThh:MM:ssZ.
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._SceneName = params.get("SceneName")
        self._CreatedBy = params.get("CreatedBy")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleSettings(AbstractModel):
    r"""Settings of a scheduled invoker

    """

    def __init__(self):
        r"""
        :param _Policy: Execution policy.

-ONCE: one-time execution.
-RECURRENCE: execute periodically.
        :type Policy: str
        :param _Recurrence: Trigger the crontab expression. This field is required if `Policy` is `RECURRENCE`. The crontab expression is parsed in UTC+8.
        :type Recurrence: str
        :param _InvokeTime: Next execution time of the executor. this field requires specifying when Policy is ONCE.

The time format is YYYY-MM-DDThh:MM:ssZ.
        :type InvokeTime: str
        """
        self._Policy = None
        self._Recurrence = None
        self._InvokeTime = None

    @property
    def Policy(self):
        r"""Execution policy.

-ONCE: one-time execution.
-RECURRENCE: execute periodically.
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Recurrence(self):
        r"""Trigger the crontab expression. This field is required if `Policy` is `RECURRENCE`. The crontab expression is parsed in UTC+8.
        :rtype: str
        """
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence

    @property
    def InvokeTime(self):
        r"""Next execution time of the executor. this field requires specifying when Policy is ONCE.

The time format is YYYY-MM-DDThh:MM:ssZ.
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
    r"""Information on tags

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
        r"""Tag key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Tag value.
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
    r"""Task result.

    """

    def __init__(self):
        r"""
        :param _ExitCode: ExitCode of the execution.
        :type ExitCode: int
        :param _Output: Base64-encoded command output. The maximum length is 24 KB.
        :type Output: str
        :param _ExecStartTime: Command execution start time. the format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExecStartTime: str
        :param _ExecEndTime: Execution end time of the command. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
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
        r"""ExitCode of the execution.
        :rtype: int
        """
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode

    @property
    def Output(self):
        r"""Base64-encoded command output. The maximum length is 24 KB.
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def ExecStartTime(self):
        r"""Command execution start time. the format is YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExecStartTime

    @ExecStartTime.setter
    def ExecStartTime(self, ExecStartTime):
        self._ExecStartTime = ExecStartTime

    @property
    def ExecEndTime(self):
        r"""Execution end time of the command. format: YYYY-MM-DDThh:MM:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExecEndTime

    @ExecEndTime.setter
    def ExecEndTime(self, ExecEndTime):
        self._ExecEndTime = ExecEndTime

    @property
    def Dropped(self):
        r"""Dropped bytes of the command output.
        :rtype: int
        """
        return self._Dropped

    @Dropped.setter
    def Dropped(self, Dropped):
        self._Dropped = Dropped

    @property
    def OutputUrl(self):
        r"""COS URL of the logs.
        :rtype: str
        """
        return self._OutputUrl

    @OutputUrl.setter
    def OutputUrl(self, OutputUrl):
        self._OutputUrl = OutputUrl

    @property
    def OutputUploadCOSErrorInfo(self):
        r"""Error message for uploading logs to COS.
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
        