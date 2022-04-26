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
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param Version: Agent version.
        :type Version: str
        :param LastHeartbeatTime: Last heartbeat time
        :type LastHeartbeatTime: str
        :param AgentStatus: Agent status. Valid values:
<li> `Online`
<li> `Offline`
        :type AgentStatus: str
        :param Environment: Agent runtime environment. Valid values:
<li> `Linux`: Linux instance
<li> `Windows`: Windows instance
        :type Environment: str
        """
        self.InstanceId = None
        self.Version = None
        self.LastHeartbeatTime = None
        self.AgentStatus = None
        self.Environment = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Version = params.get("Version")
        self.LastHeartbeatTime = params.get("LastHeartbeatTime")
        self.AgentStatus = params.get("AgentStatus")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInvocationRequest(AbstractModel):
    """CancelInvocation request structure.

    """

    def __init__(self):
        r"""
        :param InvocationId: Execution activity ID
        :type InvocationId: str
        :param InstanceIds: Instance ID list. A maximum of 100 IDs are allowed. Supported instance types:
<li> `CVM`
<li> `LIGHTHOUSE`
        :type InstanceIds: list of str
        """
        self.InvocationId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInvocationResponse(AbstractModel):
    """CancelInvocation response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Command(AbstractModel):
    """Command details.

    """

    def __init__(self):
        r"""
        :param CommandId: Command ID.
        :type CommandId: str
        :param CommandName: Command name.
        :type CommandName: str
        :param Description: Command description.
        :type Description: str
        :param Content: Base64-encoded command.
        :type Content: str
        :param CommandType: Command type.
        :type CommandType: str
        :param WorkingDirectory: Command execution path.
        :type WorkingDirectory: str
        :param Timeout: Command timeout period.
        :type Timeout: int
        :param CreatedTime: Command creation time.
        :type CreatedTime: str
        :param UpdatedTime: Command update time.
        :type UpdatedTime: str
        :param EnableParameter: Whether to enable the custom parameter feature.
        :type EnableParameter: bool
        :param DefaultParameters: Default custom parameter value.
        :type DefaultParameters: str
        :param FormattedDescription: Formatted description of the command. This parameter is an empty string for user commands and contains values for public commands.
        :type FormattedDescription: str
        :param CreatedBy: Command creator. `TAT` indicates a public command and `USER` indicates a personal command.
        :type CreatedBy: str
        :param Tags: The list of tags bound to the command.
        :type Tags: list of Tag
        :param Username: The user who executes the command on the instance.
        :type Username: str
        :param OutputCOSBucketUrl: The COS bucket URL for uploading logs.
        :type OutputCOSBucketUrl: str
        :param OutputCOSKeyPrefix: The COS bucket directory where the logs are saved.
        :type OutputCOSKeyPrefix: str
        """
        self.CommandId = None
        self.CommandName = None
        self.Description = None
        self.Content = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.EnableParameter = None
        self.DefaultParameters = None
        self.FormattedDescription = None
        self.CreatedBy = None
        self.Tags = None
        self.Username = None
        self.OutputCOSBucketUrl = None
        self.OutputCOSKeyPrefix = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.CommandName = params.get("CommandName")
        self.Description = params.get("Description")
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.EnableParameter = params.get("EnableParameter")
        self.DefaultParameters = params.get("DefaultParameters")
        self.FormattedDescription = params.get("FormattedDescription")
        self.CreatedBy = params.get("CreatedBy")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Username = params.get("Username")
        self.OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self.OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommandDocument(AbstractModel):
    """Command execution details.

    """

    def __init__(self):
        r"""
        :param Content: Base64-encoded command.
        :type Content: str
        :param CommandType: Command type.
        :type CommandType: str
        :param Timeout: Timeout period.
        :type Timeout: int
        :param WorkingDirectory: Execution path.
        :type WorkingDirectory: str
        :param Username: The user who executes the command.
        :type Username: str
        """
        self.Content = None
        self.CommandType = None
        self.Timeout = None
        self.WorkingDirectory = None
        self.Username = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.Timeout = params.get("Timeout")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandRequest(AbstractModel):
    """CreateCommand request structure.

    """

    def __init__(self):
        r"""
        :param CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param CommandType: Command type. `SHELL` and `POWERSHELL` are supported. The default value is `SHELL`.
        :type CommandType: str
        :param WorkingDirectory: Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :type WorkingDirectory: str
        :param Timeout: Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :type Timeout: int
        :param EnableParameter: Whether to enable the custom parameter feature.
This cannot be modified once created.
Default value: `false`.
        :type EnableParameter: bool
        :param DefaultParameters: The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided in the `InvokeCommand` API, the default value is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type DefaultParameters: str
        :param Tags: Tags bound to the command. At most 10 tags are allowed.
        :type Tags: list of Tag
        :param Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the root user is used to execute commands on Linux and the System user is used on Windows.
        :type Username: str
        :param OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. Consecutive dots (.) and slashes (/) are not allowed. It can not start with a slash (/). 
        :type OutputCOSKeyPrefix: str
        """
        self.CommandName = None
        self.Content = None
        self.Description = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.EnableParameter = None
        self.DefaultParameters = None
        self.Tags = None
        self.Username = None
        self.OutputCOSBucketUrl = None
        self.OutputCOSKeyPrefix = None


    def _deserialize(self, params):
        self.CommandName = params.get("CommandName")
        self.Content = params.get("Content")
        self.Description = params.get("Description")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.EnableParameter = params.get("EnableParameter")
        self.DefaultParameters = params.get("DefaultParameters")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Username = params.get("Username")
        self.OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self.OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandResponse(AbstractModel):
    """CreateCommand response structure.

    """

    def __init__(self):
        r"""
        :param CommandId: Command ID.
        :type CommandId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CommandId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.RequestId = params.get("RequestId")


class CreateInvokerRequest(AbstractModel):
    """CreateInvoker request structure.

    """

    def __init__(self):
        r"""
        :param Name: Invoker name.
        :type Name: str
        :param Type: Invoker type. It can only be `SCHEDULE` (recurring invokers).
        :type Type: str
        :param CommandId: Remote command ID.
        :type CommandId: str
        :param InstanceIds: ID of the instance bound to the trigger. Up to 100 IDs are allowed.
        :type InstanceIds: list of str
        :param Username: The user who executes the command.
        :type Username: str
        :param Parameters: Custom parameters of the command.
        :type Parameters: str
        :param ScheduleSettings: Settings required for a recurring invoker.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        self.Name = None
        self.Type = None
        self.CommandId = None
        self.InstanceIds = None
        self.Username = None
        self.Parameters = None
        self.ScheduleSettings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.CommandId = params.get("CommandId")
        self.InstanceIds = params.get("InstanceIds")
        self.Username = params.get("Username")
        self.Parameters = params.get("Parameters")
        if params.get("ScheduleSettings") is not None:
            self.ScheduleSettings = ScheduleSettings()
            self.ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvokerResponse(AbstractModel):
    """CreateInvoker response structure.

    """

    def __init__(self):
        r"""
        :param InvokerId: Invoker ID.
        :type InvokerId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InvokerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvokerId = params.get("InvokerId")
        self.RequestId = params.get("RequestId")


class DeleteCommandRequest(AbstractModel):
    """DeleteCommand request structure.

    """

    def __init__(self):
        r"""
        :param CommandId: ID of the command to be deleted.
        :type CommandId: str
        """
        self.CommandId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandResponse(AbstractModel):
    """DeleteCommand response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInvokerRequest(AbstractModel):
    """DeleteInvoker request structure.

    """

    def __init__(self):
        r"""
        :param InvokerId: ID of the invoker to be deleted.
        :type InvokerId: str
        """
        self.InvokerId = None


    def _deserialize(self, params):
        self.InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInvokerResponse(AbstractModel):
    """DeleteInvoker response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAutomationAgentStatusRequest(AbstractModel):
    """DescribeAutomationAgentStatus request structure.

    """

    def __init__(self):
        r"""
        :param InstanceIds: List of instance IDs for the query.
        :type InstanceIds: list of str
        :param Filters: Filter conditions.<br> <li>`agent-status` - String - Required: No - (Filter condition) Filter by agent status. Valid values: `Online`, `Offline`.<br> <li> `environment` - String - Required: No - (Filter condition) Filter by the agent environment. Valid value: `Linux`.<br> <li> `instance-id` - String - Required: No - (Filter condition) Filter by the instance ID. <br>Up to 10 `Filters` allowed in one request. For each filter, five `Filter.Values` can be specified. `InstanceIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutomationAgentStatusResponse(AbstractModel):
    """DescribeAutomationAgentStatus response structure.

    """

    def __init__(self):
        r"""
        :param AutomationAgentSet: Agent information list.
        :type AutomationAgentSet: list of AutomationAgentInfo
        :param TotalCount: Total number of matching agents.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AutomationAgentSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutomationAgentSet") is not None:
            self.AutomationAgentSet = []
            for item in params.get("AutomationAgentSet"):
                obj = AutomationAgentInfo()
                obj._deserialize(item)
                self.AutomationAgentSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCommandsRequest(AbstractModel):
    """DescribeCommands request structure.

    """

    def __init__(self):
        r"""
        :param CommandIds: List of command IDs. Up to 100 IDs are allowed for each request. `CommandIds` and `Filters` cannot be specified at the same time.
        :type CommandIds: list of str
        :param Filters: Filter conditions.
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID.
<li> `command-name` - String - Required: No - (Filter condition) Filter by the command name.
<li> `command-type` - String - Required: No - (Filter condition) Filter by the command type. Valid values: `SHELL` or `POWERSHELL`.
<li> `created-by` - String - Required: No - (Filter condition) Filter by the creator. Valid values: `TAT` (public commands) or `USER` (custom commands).
<li> `tag-key` - String - Required: No - (Filter condition) Filter by the tag key.</li>
<li> `tag-value` - String - Required: No - (Filter condition) Filter by the tag value.</li>
<li> `tag:tag-key` - String - Required: No - (Filter) Filter by the tag key-value pair. The tag-key should be replaced with a specified tag key. For detailed usage, see sample 4.</li>

Up to 10 `Filters` are allowed in one request. Each filter can have up to 5 `Filter.Values`. `CommandIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self.CommandIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.CommandIds = params.get("CommandIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCommandsResponse(AbstractModel):
    """DescribeCommands response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of matching commands.
        :type TotalCount: int
        :param CommandSet: List of command details.
        :type CommandSet: list of Command
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.CommandSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CommandSet") is not None:
            self.CommandSet = []
            for item in params.get("CommandSet"):
                obj = Command()
                obj._deserialize(item)
                self.CommandSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInvocationTasksRequest(AbstractModel):
    """DescribeInvocationTasks request structure.

    """

    def __init__(self):
        r"""
        :param InvocationTaskIds: List of execution task IDs. Up to 100 IDs are allowed for each request. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :type InvocationTaskIds: list of str
        :param Filters: Filter conditions.<br> <li> `invocation-id` - String - Required: No - (Filter condition) Filter by the execution activity ID.<br> <li> `invocation-task-id` - String - Required: No - (Filter condition) Filter by the execution task ID.<br> <li> `instance-id` - String - Required: No - (Filter condition) Filter by the instance ID. <br> <li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID. <br>Up to 10 `Filters` are allowed for each request. Each filter can have up to five `Filter.Values`. `InvocationTaskIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param HideOutput: Whether to hide the output. Valid values:<br><li>`True` (default): Hide the output <br><li>`False`: Show the output <br>
        :type HideOutput: bool
        """
        self.InvocationTaskIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.HideOutput = None


    def _deserialize(self, params):
        self.InvocationTaskIds = params.get("InvocationTaskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.HideOutput = params.get("HideOutput")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationTasksResponse(AbstractModel):
    """DescribeInvocationTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of matching execution tasks.
        :type TotalCount: int
        :param InvocationTaskSet: List of execution tasks.
        :type InvocationTaskSet: list of InvocationTask
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InvocationTaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InvocationTaskSet") is not None:
            self.InvocationTaskSet = []
            for item in params.get("InvocationTaskSet"):
                obj = InvocationTask()
                obj._deserialize(item)
                self.InvocationTaskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInvocationsRequest(AbstractModel):
    """DescribeInvocations request structure.

    """

    def __init__(self):
        r"""
        :param InvocationIds: List of execution activity IDs. Up to 100 IDs are allowed for each request. `InvocationIds` and `Filters` cannot be specified at the same time.
        :type InvocationIds: list of str
        :param Filters: Filter conditions.<br> <li> `invocation-id` - String - Required: No - (Filter condition) Filter by the execution activity ID.<br> 
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID. 
<li> `command-created-by` - String - Required: No - (Filter condition) Filter by the command type. Valid values: `TAT` (public commands) or `USER` (custom commands).
<li> `instance-kind` - String - Required: No - (Filter condition) Filter by the instance type. Valid values: `CVM` or `LIGHTHOUSE`. 
<br>Up to 10 `Filters` are allowed for each request. Each filter can have up to five `Filter.Values`. `InvocationIds` and `Filters` cannot be specified at the same time.
        :type Filters: list of Filter
        :param Limit: Number of returned results. It defaults to `20`. The maximum is 100. For more information on `Limit`, see the relevant section in the API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param Offset: Offset. The default value is `0`. For more information on `Offset`, see the relevant section in API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        """
        self.InvocationIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InvocationIds = params.get("InvocationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationsResponse(AbstractModel):
    """DescribeInvocations response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of matching execution activities.
        :type TotalCount: int
        :param InvocationSet: List of execution activities.
        :type InvocationSet: list of Invocation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InvocationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InvocationSet") is not None:
            self.InvocationSet = []
            for item in params.get("InvocationSet"):
                obj = Invocation()
                obj._deserialize(item)
                self.InvocationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInvokerRecordsRequest(AbstractModel):
    """DescribeInvokerRecords request structure.

    """

    def __init__(self):
        r"""
        :param InvokerIds: List of invoker IDs. Up to 100 IDs are allowed.
        :type InvokerIds: list of str
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.InvokerIds = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InvokerIds = params.get("InvokerIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvokerRecordsResponse(AbstractModel):
    """DescribeInvokerRecords response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of matching records.
        :type TotalCount: int
        :param InvokerRecordSet: Execution history of an invoker.
        :type InvokerRecordSet: list of InvokerRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InvokerRecordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InvokerRecordSet") is not None:
            self.InvokerRecordSet = []
            for item in params.get("InvokerRecordSet"):
                obj = InvokerRecord()
                obj._deserialize(item)
                self.InvokerRecordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInvokersRequest(AbstractModel):
    """DescribeInvokers request structure.

    """

    def __init__(self):
        r"""
        :param InvokerIds: List of invoker IDs.
        :type InvokerIds: list of str
        :param Filters: Filter conditions:

<li> `invoker-id` - String - Required: No - (Filter condition) Filter by the invoker ID.
<li> `command-id` - String - Required: No - (Filter condition) Filter by the command ID.
<li> `type` - String - Required: No - (Filter condition) Filter by the invoker type.
        :type Filters: list of Filter
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100.
        :type Limit: int
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        """
        self.InvokerIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InvokerIds = params.get("InvokerIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvokersResponse(AbstractModel):
    """DescribeInvokers response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of matching invokers.
        :type TotalCount: int
        :param InvokerSet: Invoker information.
        :type InvokerSet: list of Invoker
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InvokerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InvokerSet") is not None:
            self.InvokerSet = []
            for item in params.get("InvokerSet"):
                obj = Invoker()
                obj._deserialize(item)
                self.InvokerSet.append(obj)
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
        :param RegionSet: Region information list
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


class DisableInvokerRequest(AbstractModel):
    """DisableInvoker request structure.

    """

    def __init__(self):
        r"""
        :param InvokerId: ID of the invoker to be disabled.
        :type InvokerId: str
        """
        self.InvokerId = None


    def _deserialize(self, params):
        self.InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInvokerResponse(AbstractModel):
    """DisableInvoker response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableInvokerRequest(AbstractModel):
    """EnableInvoker request structure.

    """

    def __init__(self):
        r"""
        :param InvokerId: ID of the invoker to be enabled.
        :type InvokerId: str
        """
        self.InvokerId = None


    def _deserialize(self, params):
        self.InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableInvokerResponse(AbstractModel):
    """EnableInvoker response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :param Name: Field to be filtered.
        :type Name: str
        :param Values: Filter values of the field.
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
        


class Invocation(AbstractModel):
    """Execution activity details.

    """

    def __init__(self):
        r"""
        :param InvocationId: Execution activity ID.
        :type InvocationId: str
        :param CommandId: Command ID.
        :type CommandId: str
        :param InvocationStatus: Execution task status. Valid values:
<li> PENDING: Pending 
<li> RUNNING: Running
<li> SUCCESS: Success
<li> FAILED: Failed
<li> TIMEOUT: Command timed out
<li> PARTIAL_FAILED: Partial failure
        :type InvocationStatus: str
        :param InvocationTaskBasicInfoSet: Execution task information list.
        :type InvocationTaskBasicInfoSet: list of InvocationTaskBasicInfo
        :param Description: Execution activity description.
        :type Description: str
        :param StartTime: Start time of the execution activity.
        :type StartTime: str
        :param EndTime: End time of the execution activity.
        :type EndTime: str
        :param CreatedTime: Time when the execution activity is created.
        :type CreatedTime: str
        :param UpdatedTime: Time when the execution activity is updated.
        :type UpdatedTime: str
        :param Parameters: Values of custom parameters.
        :type Parameters: str
        :param DefaultParameters: Default custom parameter value.
        :type DefaultParameters: str
        :param InstanceKind: Type of the instance executing the command. Valid values: `CVM`, `LIGHTHOUSE`.
        :type InstanceKind: str
        :param Username: The user who executes the command on the instance.
        :type Username: str
        :param InvocationSource: Invocation source.
        :type InvocationSource: str
        :param CommandContent: Base64-encoded command
        :type CommandContent: str
        :param CommandType: Command type
        :type CommandType: str
        :param Timeout: Command timeout period, in seconds.
        :type Timeout: int
        :param WorkingDirectory: Working directory for executing the command.
        :type WorkingDirectory: str
        :param OutputCOSBucketUrl: The COS bucket URL for uploading logs.
        :type OutputCOSBucketUrl: str
        :param OutputCOSKeyPrefix: The COS bucket directory where the logs are saved.
        :type OutputCOSKeyPrefix: str
        """
        self.InvocationId = None
        self.CommandId = None
        self.InvocationStatus = None
        self.InvocationTaskBasicInfoSet = None
        self.Description = None
        self.StartTime = None
        self.EndTime = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.Parameters = None
        self.DefaultParameters = None
        self.InstanceKind = None
        self.Username = None
        self.InvocationSource = None
        self.CommandContent = None
        self.CommandType = None
        self.Timeout = None
        self.WorkingDirectory = None
        self.OutputCOSBucketUrl = None
        self.OutputCOSKeyPrefix = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.CommandId = params.get("CommandId")
        self.InvocationStatus = params.get("InvocationStatus")
        if params.get("InvocationTaskBasicInfoSet") is not None:
            self.InvocationTaskBasicInfoSet = []
            for item in params.get("InvocationTaskBasicInfoSet"):
                obj = InvocationTaskBasicInfo()
                obj._deserialize(item)
                self.InvocationTaskBasicInfoSet.append(obj)
        self.Description = params.get("Description")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Parameters = params.get("Parameters")
        self.DefaultParameters = params.get("DefaultParameters")
        self.InstanceKind = params.get("InstanceKind")
        self.Username = params.get("Username")
        self.InvocationSource = params.get("InvocationSource")
        self.CommandContent = params.get("CommandContent")
        self.CommandType = params.get("CommandType")
        self.Timeout = params.get("Timeout")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self.OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTask(AbstractModel):
    """Execution task.

    """

    def __init__(self):
        r"""
        :param InvocationId: Execution activity ID.
        :type InvocationId: str
        :param InvocationTaskId: Execution task ID.
        :type InvocationTaskId: str
        :param CommandId: Command ID.
        :type CommandId: str
        :param TaskStatus: Execution task status. Valid values:
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
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param TaskResult: Execution result.
        :type TaskResult: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        :param StartTime: Start time of the execution task.
        :type StartTime: str
        :param EndTime: End time of the execution task.
        :type EndTime: str
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param UpdatedTime: Update time.
        :type UpdatedTime: str
        :param CommandDocument: Command details of the execution task.
        :type CommandDocument: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        :param ErrorInfo: Error message displayed when the execution task fails.
        :type ErrorInfo: str
        :param InvocationSource: Invocation source.
        :type InvocationSource: str
        """
        self.InvocationId = None
        self.InvocationTaskId = None
        self.CommandId = None
        self.TaskStatus = None
        self.InstanceId = None
        self.TaskResult = None
        self.StartTime = None
        self.EndTime = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.CommandDocument = None
        self.ErrorInfo = None
        self.InvocationSource = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.InvocationTaskId = params.get("InvocationTaskId")
        self.CommandId = params.get("CommandId")
        self.TaskStatus = params.get("TaskStatus")
        self.InstanceId = params.get("InstanceId")
        if params.get("TaskResult") is not None:
            self.TaskResult = TaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("CommandDocument") is not None:
            self.CommandDocument = CommandDocument()
            self.CommandDocument._deserialize(params.get("CommandDocument"))
        self.ErrorInfo = params.get("ErrorInfo")
        self.InvocationSource = params.get("InvocationSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTaskBasicInfo(AbstractModel):
    """Execution task description.

    """

    def __init__(self):
        r"""
        :param InvocationTaskId: Execution task ID.
        :type InvocationTaskId: str
        :param TaskStatus: Execution task status. Valid values:
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
        :param InstanceId: Instance ID.
        :type InstanceId: str
        """
        self.InvocationTaskId = None
        self.TaskStatus = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.InvocationTaskId = params.get("InvocationTaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandRequest(AbstractModel):
    """InvokeCommand request structure.

    """

    def __init__(self):
        r"""
        :param CommandId: ID of the command to be triggered.
        :type CommandId: str
        :param InstanceIds: IDs of instances about to execute commands. At most 100 IDs are allowed.
        :type InstanceIds: list of str
        :param Parameters: Custom parameters of the command. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided, the DefaultParameters of the command is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type Parameters: str
        :param Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of the least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. If this is not specified, the Username of the command is used by default.
        :type Username: str
        :param WorkingDirectory: Execution path of the command. The WorkingDirectory of the command is used by default.
        :type WorkingDirectory: str
        :param Timeout: Command timeout period. Value range: [1, 86400]. The Timeout of the command is used by default.
        :type Timeout: int
        :param OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :type OutputCOSKeyPrefix: str
        """
        self.CommandId = None
        self.InstanceIds = None
        self.Parameters = None
        self.Username = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.OutputCOSBucketUrl = None
        self.OutputCOSKeyPrefix = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.InstanceIds = params.get("InstanceIds")
        self.Parameters = params.get("Parameters")
        self.Username = params.get("Username")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self.OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandResponse(AbstractModel):
    """InvokeCommand response structure.

    """

    def __init__(self):
        r"""
        :param InvocationId: Execution activity ID.
        :type InvocationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InvocationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvocationId = params.get("InvocationId")
        self.RequestId = params.get("RequestId")


class Invoker(AbstractModel):
    """Invoker information.

    """

    def __init__(self):
        r"""
        :param InvokerId: Invoker ID.
        :type InvokerId: str
        :param Name: Invoker name.
        :type Name: str
        :param Type: Invoker type.
        :type Type: str
        :param CommandId: Command ID.
        :type CommandId: str
        :param Username: Username.
        :type Username: str
        :param Parameters: Custom parameters.
        :type Parameters: str
        :param InstanceIds: Instance ID list.
        :type InstanceIds: list of str
        :param Enable: Whether to enable the invoker.
        :type Enable: bool
        :param ScheduleSettings: Execution schedule of the invoker. This field is returned for recurring invokers.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        :param CreatedTime: Creation time.
        :type CreatedTime: str
        :param UpdatedTime: Modification time.
        :type UpdatedTime: str
        """
        self.InvokerId = None
        self.Name = None
        self.Type = None
        self.CommandId = None
        self.Username = None
        self.Parameters = None
        self.InstanceIds = None
        self.Enable = None
        self.ScheduleSettings = None
        self.CreatedTime = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.InvokerId = params.get("InvokerId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.CommandId = params.get("CommandId")
        self.Username = params.get("Username")
        self.Parameters = params.get("Parameters")
        self.InstanceIds = params.get("InstanceIds")
        self.Enable = params.get("Enable")
        if params.get("ScheduleSettings") is not None:
            self.ScheduleSettings = ScheduleSettings()
            self.ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokerRecord(AbstractModel):
    """Execution history of the invoker.

    """

    def __init__(self):
        r"""
        :param InvokerId: Invoker ID.
        :type InvokerId: str
        :param InvokeTime: Execution time.
        :type InvokeTime: str
        :param Reason: Execution reason.
        :type Reason: str
        :param InvocationId: Command execution ID.
        :type InvocationId: str
        :param Result: Trigger result.
        :type Result: str
        """
        self.InvokerId = None
        self.InvokeTime = None
        self.Reason = None
        self.InvocationId = None
        self.Result = None


    def _deserialize(self, params):
        self.InvokerId = params.get("InvokerId")
        self.InvokeTime = params.get("InvokeTime")
        self.Reason = params.get("Reason")
        self.InvocationId = params.get("InvocationId")
        self.Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCommandRequest(AbstractModel):
    """ModifyCommand request structure.

    """

    def __init__(self):
        r"""
        :param CommandId: Command ID.
        :type CommandId: str
        :param CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param CommandType: Command type. `SHELL` and `POWERSHELL` are supported.
        :type CommandType: str
        :param WorkingDirectory: Command execution path.
        :type WorkingDirectory: str
        :param Timeout: Command timeout period. Value range: [1, 86400].
        :type Timeout: int
        :param DefaultParameters: The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
All parameters are overwritten. All default values are required for modification.
Modification is only allowed when `EnableParameter` is `true`.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type DefaultParameters: str
        :param Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user.
        :type Username: str
        :param OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :type OutputCOSKeyPrefix: str
        """
        self.CommandId = None
        self.CommandName = None
        self.Description = None
        self.Content = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.DefaultParameters = None
        self.Username = None
        self.OutputCOSBucketUrl = None
        self.OutputCOSKeyPrefix = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.CommandName = params.get("CommandName")
        self.Description = params.get("Description")
        self.Content = params.get("Content")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.DefaultParameters = params.get("DefaultParameters")
        self.Username = params.get("Username")
        self.OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self.OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCommandResponse(AbstractModel):
    """ModifyCommand response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInvokerRequest(AbstractModel):
    """ModifyInvoker request structure.

    """

    def __init__(self):
        r"""
        :param InvokerId: ID of the invoker to be modified.
        :type InvokerId: str
        :param Name: Name of the invoker to be modified.
        :type Name: str
        :param Type: Invoker type. It can only be `SCHEDULE` (recurring invokers).
        :type Type: str
        :param CommandId: ID of the command to be modified.
        :type CommandId: str
        :param Username: The username to be modified.
        :type Username: str
        :param Parameters: Custom parameters to be modified.
        :type Parameters: str
        :param InstanceIds: List of instance IDs to be modified. Up to 100 IDs are allowed.
        :type InstanceIds: list of str
        :param ScheduleSettings: Scheduled invoker settings to be modified.
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        self.InvokerId = None
        self.Name = None
        self.Type = None
        self.CommandId = None
        self.Username = None
        self.Parameters = None
        self.InstanceIds = None
        self.ScheduleSettings = None


    def _deserialize(self, params):
        self.InvokerId = params.get("InvokerId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.CommandId = params.get("CommandId")
        self.Username = params.get("Username")
        self.Parameters = params.get("Parameters")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ScheduleSettings") is not None:
            self.ScheduleSettings = ScheduleSettings()
            self.ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInvokerResponse(AbstractModel):
    """ModifyInvoker response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PreviewReplacedCommandContentRequest(AbstractModel):
    """PreviewReplacedCommandContent request structure.

    """

    def __init__(self):
        r"""
        :param Parameters: Custom parameters for the preview. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and "value" is its specified value. Both "key" and "value" are strings.
At most 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can only contain [a-z], [A-Z], [0-9], [-_].
This parameter can be left empty if DefaultParameters is set for the previewed CommandId.
        :type Parameters: str
        :param CommandId: The command to be previewed. If DefaultParameters is set, it is combined with Parameters and Parameters takes priority.
`CommandId` or `Content` must be specified.
        :type CommandId: str
        :param Content: Base64-encoded command to be previewed. The maximum length is 64 KB.
CommandId or Content must be specified.
        :type Content: str
        """
        self.Parameters = None
        self.CommandId = None
        self.Content = None


    def _deserialize(self, params):
        self.Parameters = params.get("Parameters")
        self.CommandId = params.get("CommandId")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewReplacedCommandContentResponse(AbstractModel):
    """PreviewReplacedCommandContent response structure.

    """

    def __init__(self):
        r"""
        :param ReplacedContent: Base64-encoded command with custom parameters.
        :type ReplacedContent: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReplacedContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReplacedContent = params.get("ReplacedContent")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Information of a region.

    """

    def __init__(self):
        r"""
        :param Region: Region name, such as `ap-guangzhou`
        :type Region: str
        :param RegionName: Region description, such as `Guangzhou`
        :type RegionName: str
        :param RegionState: Region status. `AVAILABLE` indicates the region is available.
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
        


class RunCommandRequest(AbstractModel):
    """RunCommand request structure.

    """

    def __init__(self):
        r"""
        :param Content: Base64-encoded command. The maximum length is 64 KB.
        :type Content: str
        :param InstanceIds: IDs of instances about to execute commands. Up to 100 IDs are allowed. Supported instance types:
<li> `CVM`
<li> `LIGHTHOUSE`
        :type InstanceIds: list of str
        :param CommandName: Command name. The name can be up to 60 bytes, and contain [a-z], [A-Z], [0-9] and [_-.].
        :type CommandName: str
        :param Description: Command description. The maximum length is 120 characters.
        :type Description: str
        :param CommandType: Command type. `SHELL` and `POWERSHELL` are supported. The default value is `SHELL`.
        :type CommandType: str
        :param WorkingDirectory: Command execution path. The default value is /root for `SHELL` commands and C:\Program Files\qcloud\tat_agent\workdir for `POWERSHELL` commands.
        :type WorkingDirectory: str
        :param Timeout: Command timeout period. Default value: 60 seconds. Value range: [1, 86400].
        :type Timeout: int
        :param SaveCommand: Whether to save the command. Valid values:
<li> `True`: Save
<li> `False`: Do not save
The default value is `False`.
        :type SaveCommand: bool
        :param EnableParameter: Whether to enable the custom parameter feature.
This cannot be modified once created.
Default value: `false`.
        :type EnableParameter: bool
        :param DefaultParameters: The default value of the custom parameter value when it is enabled. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If Parameters is not provided, the default values specified here are used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type DefaultParameters: str
        :param Parameters: Custom parameters of `Command`. The field type is JSON encoded string. For example, {\"varA\": \"222\"}.
`key` is the name of the custom parameter and `value` is the default value. Both `key` and `value` are strings.
If no parameter value is provided, the `DefaultParameters` is used.
Up to 20 custom parameters are supported.
The name of the custom parameter cannot exceed 64 characters and can contain [a-z], [A-Z], [0-9] and [-_].
        :type Parameters: str
        :param Tags: The tags of the command. It is available when `SaveCommand` is `True`. A maximum of 10 tags are allowed.
        :type Tags: list of Tag
        :param Username: The username used to execute the command on the CVM or Lighthouse instance.
The principle of least privilege is the best practice for permission management. We recommend you execute TAT commands as a general user. By default, the user `root` is used to execute commands on Linux and the user `System` is used on Windows.
        :type Username: str
        :param OutputCOSBucketUrl: The COS bucket URL for uploading logs. The URL must start with `https`, such as `https://BucketName-123454321.cos.ap-beijing.myqcloud.com`.
        :type OutputCOSBucketUrl: str
        :param OutputCOSKeyPrefix: The COS bucket directory where the logs are saved. Check below for the rules of the directory name. 
1. It must be a combination of number, letters, and visible characters. Up to 60 characters are allowed.
2. Use a slash (/) to create a subdirectory.
3. ".." can not be used as the folder name. It cannot start with a slash (/), and cannot contain consecutive slashes.
        :type OutputCOSKeyPrefix: str
        """
        self.Content = None
        self.InstanceIds = None
        self.CommandName = None
        self.Description = None
        self.CommandType = None
        self.WorkingDirectory = None
        self.Timeout = None
        self.SaveCommand = None
        self.EnableParameter = None
        self.DefaultParameters = None
        self.Parameters = None
        self.Tags = None
        self.Username = None
        self.OutputCOSBucketUrl = None
        self.OutputCOSKeyPrefix = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.InstanceIds = params.get("InstanceIds")
        self.CommandName = params.get("CommandName")
        self.Description = params.get("Description")
        self.CommandType = params.get("CommandType")
        self.WorkingDirectory = params.get("WorkingDirectory")
        self.Timeout = params.get("Timeout")
        self.SaveCommand = params.get("SaveCommand")
        self.EnableParameter = params.get("EnableParameter")
        self.DefaultParameters = params.get("DefaultParameters")
        self.Parameters = params.get("Parameters")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Username = params.get("Username")
        self.OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self.OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCommandResponse(AbstractModel):
    """RunCommand response structure.

    """

    def __init__(self):
        r"""
        :param CommandId: Command ID.
        :type CommandId: str
        :param InvocationId: Execution activity ID.
        :type InvocationId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CommandId = None
        self.InvocationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CommandId = params.get("CommandId")
        self.InvocationId = params.get("InvocationId")
        self.RequestId = params.get("RequestId")


class ScheduleSettings(AbstractModel):
    """Settings of a scheduled invoker

    """

    def __init__(self):
        r"""
        :param Policy: Execution policy:
<br><li>`ONCE`: Execute once
<br><li>`RECURRENCE`: Execute repeatedly
        :type Policy: str
        :param Recurrence: Trigger the crontab expression. This field is required if `Policy` is `RECURRENCE`. The crontab expression is parsed in UTC+8.
        :type Recurrence: str
        :param InvokeTime: The next execution time of the invoker. This field is required if `Policy` is `ONCE`.
        :type InvokeTime: str
        """
        self.Policy = None
        self.Recurrence = None
        self.InvokeTime = None


    def _deserialize(self, params):
        self.Policy = params.get("Policy")
        self.Recurrence = params.get("Recurrence")
        self.InvokeTime = params.get("InvokeTime")
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
        :type Key: str
        :param Value: Tag value.
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
        


class TaskResult(AbstractModel):
    """Task result.

    """

    def __init__(self):
        r"""
        :param ExitCode: ExitCode of the execution.
        :type ExitCode: int
        :param Output: Base64-encoded command output. The maximum length is 24 KB.
        :type Output: str
        :param ExecStartTime: Time when the execution is started.
        :type ExecStartTime: str
        :param ExecEndTime: Time when the execution is ended.
        :type ExecEndTime: str
        :param Dropped: Dropped bytes of the command output.
        :type Dropped: int
        :param OutputUrl: COS URL of the logs.
        :type OutputUrl: str
        :param OutputUploadCOSErrorInfo: Error message for uploading logs to COS.
        :type OutputUploadCOSErrorInfo: str
        """
        self.ExitCode = None
        self.Output = None
        self.ExecStartTime = None
        self.ExecEndTime = None
        self.Dropped = None
        self.OutputUrl = None
        self.OutputUploadCOSErrorInfo = None


    def _deserialize(self, params):
        self.ExitCode = params.get("ExitCode")
        self.Output = params.get("Output")
        self.ExecStartTime = params.get("ExecStartTime")
        self.ExecEndTime = params.get("ExecEndTime")
        self.Dropped = params.get("Dropped")
        self.OutputUrl = params.get("OutputUrl")
        self.OutputUploadCOSErrorInfo = params.get("OutputUploadCOSErrorInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        