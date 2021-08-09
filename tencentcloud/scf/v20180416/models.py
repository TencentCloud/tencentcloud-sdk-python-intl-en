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


class AccessInfo(AbstractModel):
    """HTTP domain name-related information

    """

    def __init__(self):
        """
        :param Host: Domain name\n        :type Host: str\n        :param Vip: VIP\n        :type Vip: str\n        """
        self.Host = None
        self.Vip = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Alias(AbstractModel):
    """Version alias of function

    """

    def __init__(self):
        """
        :param FunctionVersion: Master version pointed to by the alias\n        :type FunctionVersion: str\n        :param Name: Alias name\n        :type Name: str\n        :param RoutingConfig: Routing information of alias
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`\n        :param Description: Description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AddTime: str\n        :param ModTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModTime: str\n        """
        self.FunctionVersion = None
        self.Name = None
        self.RoutingConfig = None
        self.Description = None
        self.AddTime = None
        self.ModTime = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        self.Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncEvent(AbstractModel):
    """Async event

    """

    def __init__(self):
        """
        :param InvokeRequestId: Invocation request ID\n        :type InvokeRequestId: str\n        :param InvokeType: Invocation type\n        :type InvokeType: str\n        :param Qualifier: Function version\n        :type Qualifier: str\n        :param Status: Event status\n        :type Status: str\n        :param StartTime: Invocation start time in the format of "%Y-%m-%d %H:%M:%S.%f"\n        :type StartTime: str\n        :param EndTime: Invocation end time in the format of "%Y-%m-%d %H:%M:%S.%f"\n        :type EndTime: str\n        """
        self.InvokeRequestId = None
        self.InvokeType = None
        self.Qualifier = None
        self.Status = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InvokeRequestId = params.get("InvokeRequestId")
        self.InvokeType = params.get("InvokeType")
        self.Qualifier = params.get("Qualifier")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsyncTriggerConfig(AbstractModel):
    """Async retry configuration details of function

    """

    def __init__(self):
        """
        :param RetryConfig: Async retry configuration of function upon user error\n        :type RetryConfig: list of RetryConfig\n        :param MsgTTL: Message retention period\n        :type MsgTTL: int\n        """
        self.RetryConfig = None
        self.MsgTTL = None


    def _deserialize(self, params):
        if params.get("RetryConfig") is not None:
            self.RetryConfig = []
            for item in params.get("RetryConfig"):
                obj = RetryConfig()
                obj._deserialize(item)
                self.RetryConfig.append(obj)
        self.MsgTTL = params.get("MsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfsConfig(AbstractModel):
    """File system (CFS) configuration description

    """

    def __init__(self):
        """
        :param CfsInsList: File system information list\n        :type CfsInsList: list of CfsInsInfo\n        """
        self.CfsInsList = None


    def _deserialize(self, params):
        if params.get("CfsInsList") is not None:
            self.CfsInsList = []
            for item in params.get("CfsInsList"):
                obj = CfsInsInfo()
                obj._deserialize(item)
                self.CfsInsList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CfsInsInfo(AbstractModel):
    """Configuration information of the CFS instance associated with function

    """

    def __init__(self):
        """
        :param UserId: User ID\n        :type UserId: str\n        :param UserGroupId: User group ID\n        :type UserGroupId: str\n        :param CfsId: CFS instance ID\n        :type CfsId: str\n        :param MountInsId: File system mount target ID\n        :type MountInsId: str\n        :param LocalMountDir: Local mount target\n        :type LocalMountDir: str\n        :param RemoteMountDir: Remote mount target\n        :type RemoteMountDir: str\n        :param IpAddress: File system IP, which is not required when you configure CFS.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpAddress: str\n        :param MountVpcId: VPC ID of file system, which is not required when you configure CFS.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MountVpcId: str\n        :param MountSubnetId: VPC subnet ID of file system, which is not required when you configure CFS.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MountSubnetId: str\n        """
        self.UserId = None
        self.UserGroupId = None
        self.CfsId = None
        self.MountInsId = None
        self.LocalMountDir = None
        self.RemoteMountDir = None
        self.IpAddress = None
        self.MountVpcId = None
        self.MountSubnetId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserGroupId = params.get("UserGroupId")
        self.CfsId = params.get("CfsId")
        self.MountInsId = params.get("MountInsId")
        self.LocalMountDir = params.get("LocalMountDir")
        self.RemoteMountDir = params.get("RemoteMountDir")
        self.IpAddress = params.get("IpAddress")
        self.MountVpcId = params.get("MountVpcId")
        self.MountSubnetId = params.get("MountSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Code(AbstractModel):
    """Function code

    """

    def __init__(self):
        """
        :param CosBucketName: Object bucket name (enter the custom part of the bucket name without `-appid`)\n        :type CosBucketName: str\n        :param CosObjectName: COS object path\n        :type CosObjectName: str\n        :param ZipFile: This parameter contains a .zip file (up to 50 MB) of the function code file and its dependencies. When this API is used, the content of the .zip file needs to be Base64-encoded\n        :type ZipFile: str\n        :param CosBucketRegion: COS region. For Beijing regions, you need to import `ap-beijing`. For Beijing Region 1, you need to input `ap-beijing-1`. For other regions, no import is required.\n        :type CosBucketRegion: str\n        :param DemoId: `DemoId` is required if Demo is used for the creation.\n        :type DemoId: str\n        :param TempCosObjectName: `TempCosObjectName` is required if TempCos is used for the creation.\n        :type TempCosObjectName: str\n        :param GitUrl: Git address\n        :type GitUrl: str\n        :param GitUserName: Git user name\n        :type GitUserName: str\n        :param GitPassword: Git password\n        :type GitPassword: str\n        :param GitPasswordSecret: Git password after encryption. In general, this value is not required.\n        :type GitPasswordSecret: str\n        :param GitBranch: Git branch\n        :type GitBranch: str\n        :param GitDirectory: Code path in Git repository\n        :type GitDirectory: str\n        :param GitCommitId: Version to be pulled\n        :type GitCommitId: str\n        :param GitUserNameSecret: Git user name after encryption. In general, this value is not required.\n        :type GitUserNameSecret: str\n        """
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.CosBucketRegion = None
        self.DemoId = None
        self.TempCosObjectName = None
        self.GitUrl = None
        self.GitUserName = None
        self.GitPassword = None
        self.GitPasswordSecret = None
        self.GitBranch = None
        self.GitDirectory = None
        self.GitCommitId = None
        self.GitUserNameSecret = None


    def _deserialize(self, params):
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.CosBucketRegion = params.get("CosBucketRegion")
        self.DemoId = params.get("DemoId")
        self.TempCosObjectName = params.get("TempCosObjectName")
        self.GitUrl = params.get("GitUrl")
        self.GitUserName = params.get("GitUserName")
        self.GitPassword = params.get("GitPassword")
        self.GitPasswordSecret = params.get("GitPasswordSecret")
        self.GitBranch = params.get("GitBranch")
        self.GitDirectory = params.get("GitDirectory")
        self.GitCommitId = params.get("GitCommitId")
        self.GitUserNameSecret = params.get("GitUserNameSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionRequest(AbstractModel):
    """CopyFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function to be replicated\n        :type FunctionName: str\n        :param NewFunctionName: Name of the new function\n        :type NewFunctionName: str\n        :param Namespace: Namespace of the function to be replicated. The default value is `default`.\n        :type Namespace: str\n        :param TargetNamespace: Namespace of the replicated function. The default value is default.\n        :type TargetNamespace: str\n        :param Description: Description of the new function\n        :type Description: str\n        :param TargetRegion: Region of the target of the function replication. If the value is not set, the current region is used by default.\n        :type TargetRegion: str\n        :param Override: It specifies whether to replace the function with the same name in the target namespace. The default option is `FALSE`.
(Note: The `TRUE` option results in deletion of the function in the target namespace. Please operate with caution.)
TRUE: Replaces the function.
FALSE: Does not replace the function.\n        :type Override: bool\n        :param CopyConfiguration: It specifies whether to replicate the function attributes, including environment variables, memory, timeout, function description, labels, and VPC. The default value is `TRUE`.
TRUE: Replicates the function configuration.
FALSE: Does not replicate the function configuration.\n        :type CopyConfiguration: bool\n        """
        self.FunctionName = None
        self.NewFunctionName = None
        self.Namespace = None
        self.TargetNamespace = None
        self.Description = None
        self.TargetRegion = None
        self.Override = None
        self.CopyConfiguration = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.NewFunctionName = params.get("NewFunctionName")
        self.Namespace = params.get("Namespace")
        self.TargetNamespace = params.get("TargetNamespace")
        self.Description = params.get("Description")
        self.TargetRegion = params.get("TargetRegion")
        self.Override = params.get("Override")
        self.CopyConfiguration = params.get("CopyConfiguration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyFunctionResponse(AbstractModel):
    """CopyFunction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAliasRequest(AbstractModel):
    """CreateAlias request structure.

    """

    def __init__(self):
        """
        :param Name: Alias name, which must be unique in the function, can contain 1 to 64 letters, digits, `_`, and `-`, and must begin with a letter\n        :type Name: str\n        :param FunctionName: Function name\n        :type FunctionName: str\n        :param FunctionVersion: Master version pointed to by the alias\n        :type FunctionVersion: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param RoutingConfig: Request routing configuration of alias\n        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`\n        :param Description: Alias description\n        :type Description: str\n        """
        self.Name = None
        self.FunctionName = None
        self.FunctionVersion = None
        self.Namespace = None
        self.RoutingConfig = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.FunctionName = params.get("FunctionName")
        self.FunctionVersion = params.get("FunctionVersion")
        self.Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAliasResponse(AbstractModel):
    """CreateAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFunctionRequest(AbstractModel):
    """CreateFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the new function. The name can contain 2 to 60 characters, including English letters, digits, hyphens (-), and underscores (_). The name must start with a letter and cannot end with a hyphen or underscore.\n        :type FunctionName: str\n        :param Code: Function code. Note: `COS`, `ZipFile`, and `DemoId` cannot be specified at the same time.\n        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`\n        :param Handler: Function handler name. It supports the format of "file name.handler name" where the file name and handler name are separated with a "." (for Java, it is in the format of "package name.class name::handler name"). File and handler names can contain 2–60 letters, digits, underscores, and dashes and must start and end with letters\n        :type Handler: str\n        :param Description: Function description. It can contain up to 1,000 characters including letters, digits, spaces, commas (,), periods (.), and Chinese characters.\n        :type Description: str\n        :param MemorySize: Memory size available for function during execution. Default value: 128 MB. Value range: 64 or 128-3072 MB in increments of 128 MB\n        :type MemorySize: int\n        :param Timeout: Maximum execution duration of function in seconds. Value range: 1-900 seconds. Default value: 3 seconds\n        :type Timeout: int\n        :param Environment: Function environment variable\n        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`\n        :param Runtime: Function runtime environment. Valid values: Python2.7, Python3.6, Nodejs6.10, Nodejs8.9, Nodejs10.15, Nodejs12.16, Php5, Php7, Go1, Java8, CustomRuntime. Default value: Python2.7\n        :type Runtime: str\n        :param VpcConfig: Function VPC configuration\n        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param Role: Role bound to the function\n        :type Role: str\n        :param ClsLogsetId: CLS Logset ID to which the function logs are shipped\n        :type ClsLogsetId: str\n        :param ClsTopicId: CLS Topic ID to which the function logs are shipped\n        :type ClsTopicId: str\n        :param Type: Function type. The default value is `Event`. Enter `Event` if you need to create a trigger function. Enter `HTTP` if you need to create an HTTP function service.\n        :type Type: str\n        :param CodeSource: Code source. Valid values: ZipFile, Cos, Demo\n        :type CodeSource: str\n        :param Layers: List of layer versions to be associate with the function. Layers will be overwritten sequentially in the order in the list.\n        :type Layers: list of LayerVersionSimple\n        :param DeadLetterConfig: Dead letter queue parameter\n        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`\n        :param PublicNetConfig: Public network access configuration\n        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`\n        :param CfsConfig: File system configuration parameter, which is used for the function to mount the file system\n        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`\n        :param InitTimeout: Timeout period for function initialization\n        :type InitTimeout: int\n        :param Tags: Tag parameter of the function. It is an array of key-value pairs.\n        :type Tags: list of Tag\n        :param AsyncRunEnable: Whether to enable the async attribute. TRUE: yes; FALSE: no\n        :type AsyncRunEnable: str\n        :param TraceEnable: Whether to enable event tracking. TRUE: yes; FALSE: no\n        :type TraceEnable: str\n        """
        self.FunctionName = None
        self.Code = None
        self.Handler = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Environment = None
        self.Runtime = None
        self.VpcConfig = None
        self.Namespace = None
        self.Role = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.Type = None
        self.CodeSource = None
        self.Layers = None
        self.DeadLetterConfig = None
        self.PublicNetConfig = None
        self.CfsConfig = None
        self.InitTimeout = None
        self.Tags = None
        self.AsyncRunEnable = None
        self.TraceEnable = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        if params.get("Code") is not None:
            self.Code = Code()
            self.Code._deserialize(params.get("Code"))
        self.Handler = params.get("Handler")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.Runtime = params.get("Runtime")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.Namespace = params.get("Namespace")
        self.Role = params.get("Role")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.Type = params.get("Type")
        self.CodeSource = params.get("CodeSource")
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionSimple()
                obj._deserialize(item)
                self.Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        if params.get("PublicNetConfig") is not None:
            self.PublicNetConfig = PublicNetConfigIn()
            self.PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        if params.get("CfsConfig") is not None:
            self.CfsConfig = CfsConfig()
            self.CfsConfig._deserialize(params.get("CfsConfig"))
        self.InitTimeout = params.get("InitTimeout")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AsyncRunEnable = params.get("AsyncRunEnable")
        self.TraceEnable = params.get("TraceEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFunctionResponse(AbstractModel):
    """CreateFunction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace name\n        :type Namespace: str\n        :param Description: Namespace description\n        :type Description: str\n        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function bound to the new trigger\n        :type FunctionName: str\n        :param TriggerName: Name of a new trigger. For a timer trigger, the name can contain up to 100 letters, digits, dashes, and underscores; for a COS trigger, it should be an access domain name of the corresponding COS bucket applicable to the XML API (e.g., 5401-5ff414-12345.cos.ap-shanghai.myqcloud.com); for other triggers, please see the descriptions of parameters bound to the specific trigger.\n        :type TriggerName: str\n        :param Type: Trigger type. Currently, COS, CMQ, timer, and ckafka triggers are supported.\n        :type Type: str\n        :param TriggerDesc: For parameters of triggers, see [Trigger Description](https://intl.cloud.tencent.com/document/product/583/39901?from_cn_redirect=1)\n        :type TriggerDesc: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param Qualifier: Function version\n        :type Qualifier: str\n        :param Enable: Initial enabling status of the trigger. `OPEN` indicates enabled, and `CLOSE` indicates disabled.\n        :type Enable: str\n        :param CustomArgument: Custom argument, supporting only the timer trigger.\n        :type CustomArgument: str\n        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Namespace = None
        self.Qualifier = None
        self.Enable = None
        self.CustomArgument = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.Enable = params.get("Enable")
        self.CustomArgument = params.get("CustomArgument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger response structure.

    """

    def __init__(self):
        """
        :param TriggerInfo: Trigger information\n        :type TriggerInfo: :class:`tencentcloud.scf.v20180416.models.Trigger`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TriggerInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TriggerInfo") is not None:
            self.TriggerInfo = Trigger()
            self.TriggerInfo._deserialize(params.get("TriggerInfo"))
        self.RequestId = params.get("RequestId")


class DeadLetterConfig(AbstractModel):
    """Dead letter queue parameter

    """

    def __init__(self):
        """
        :param Type: Dead letter queue mode\n        :type Type: str\n        :param Name: Dead letter queue name\n        :type Name: str\n        :param FilterType: Tag form of a dead letter queue topic mode\n        :type FilterType: str\n        """
        self.Type = None
        self.Name = None
        self.FilterType = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasRequest(AbstractModel):
    """DeleteAlias request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Name: Alias name\n        :type Name: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Name = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAliasResponse(AbstractModel):
    """DeleteAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function to be deleted\n        :type FunctionName: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLayerVersionRequest(AbstractModel):
    """DeleteLayerVersion request structure.

    """

    def __init__(self):
        """
        :param LayerName: Layer name\n        :type LayerName: str\n        :param LayerVersion: Version number\n        :type LayerVersion: int\n        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLayerVersionResponse(AbstractModel):
    """DeleteLayerVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace name\n        :type Namespace: str\n        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProvisionedConcurrencyConfigRequest(AbstractModel):
    """DeleteProvisionedConcurrencyConfig request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function for which to delete the provisioned concurrency\n        :type FunctionName: str\n        :param Qualifier: Function version number\n        :type Qualifier: str\n        :param Namespace: Function namespace. Default value: `default`\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProvisionedConcurrencyConfigResponse(AbstractModel):
    """DeleteProvisionedConcurrencyConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReservedConcurrencyConfigRequest(AbstractModel):
    """DeleteReservedConcurrencyConfig request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function for which to delete the provisioned concurrency\n        :type FunctionName: str\n        :param Namespace: Function namespace. Default value: `default`\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReservedConcurrencyConfigResponse(AbstractModel):
    """DeleteReservedConcurrencyConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param TriggerName: Name of the trigger to be deleted\n        :type TriggerName: str\n        :param Type: Type of the trigger to be deleted. Currently, COS, CMQ, timer, and ckafka triggers are supported.\n        :type Type: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param TriggerDesc: This field is required if a COS trigger is to be deleted. It stores the data {"event":"cos:ObjectCreated:*"} in the JSON format. The data content of this field is in the same format as that of SetTrigger. This field is optional if a scheduled trigger or CMQ trigger is to be deleted.\n        :type TriggerDesc: str\n        :param Qualifier: Function version information\n        :type Qualifier: str\n        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.Namespace = None
        self.TriggerDesc = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.Namespace = params.get("Namespace")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EipConfigIn(AbstractModel):
    """Fixed IP configuration for public network access

    """

    def __init__(self):
        """
        :param EipStatus: Status of the EIP. Values: ['ENABLE','DISABLE']\n        :type EipStatus: str\n        """
        self.EipStatus = None


    def _deserialize(self, params):
        self.EipStatus = params.get("EipStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipConfigOut(AbstractModel):
    """Fixed IP configuration for public network access

    """

    def __init__(self):
        """
        :param EipStatus: Whether it is a fixed IP. Valid values: ["ENABLE","DISABLE"]\n        :type EipStatus: str\n        :param EipAddress: IP list
Note: This field may return null, indicating that no valid values can be obtained.\n        :type EipAddress: list of str\n        """
        self.EipStatus = None
        self.EipAddress = None


    def _deserialize(self, params):
        self.EipStatus = params.get("EipStatus")
        self.EipAddress = params.get("EipAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipOutConfig(AbstractModel):
    """EipOutConfig

    """

    def __init__(self):
        """
        :param EipFixed: It specifies whether the IP is fixed. The value is `TRUE` or `FALSE`.\n        :type EipFixed: str\n        :param Eips: IP list\n        :type Eips: list of str\n        """
        self.EipFixed = None
        self.Eips = None


    def _deserialize(self, params):
        self.EipFixed = params.get("EipFixed")
        self.Eips = params.get("Eips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Environment(AbstractModel):
    """Environment variable parameter of the function

    """

    def __init__(self):
        """
        :param Variables: Environment variable array\n        :type Variables: list of Variable\n        """
        self.Variables = None


    def _deserialize(self, params):
        if params.get("Variables") is not None:
            self.Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self.Variables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.
    If more than one filter exists, the logical relationship between these filters is `AND`.
    If multiple values exist in one filter, the logical relationship between these values under the same filter is `OR`.

    """

    def __init__(self):
        """
        :param Name: Fields to be filtered\n        :type Name: str\n        :param Values: Filter values of the field\n        :type Values: list of str\n        """
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
        


class Function(AbstractModel):
    """Function list

    """

    def __init__(self):
        """
        :param ModTime: Modification time\n        :type ModTime: str\n        :param AddTime: Creation time\n        :type AddTime: str\n        :param Runtime: Running\n        :type Runtime: str\n        :param FunctionName: Function name\n        :type FunctionName: str\n        :param FunctionId: Function ID\n        :type FunctionId: str\n        :param Namespace: Namespace\n        :type Namespace: str\n        :param Status: Function status. For valid values and status change process, please see [here](https://intl.cloud.tencent.com/document/product/583/47175?from_cn_redirect=1)\n        :type Status: str\n        :param StatusDesc: Function status details\n        :type StatusDesc: str\n        :param Description: Function description\n        :type Description: str\n        :param Tags: Function tag\n        :type Tags: list of Tag\n        :param Type: Function type. The value is `HTTP` or `Event`.\n        :type Type: str\n        :param StatusReasons: Cause of function failure\n        :type StatusReasons: list of StatusReason\n        :param TotalProvisionedConcurrencyMem: Sum of provisioned concurrence memory for all function versions
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalProvisionedConcurrencyMem: int\n        :param ReservedConcurrencyMem: Reserved memory for function concurrence
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReservedConcurrencyMem: int\n        """
        self.ModTime = None
        self.AddTime = None
        self.Runtime = None
        self.FunctionName = None
        self.FunctionId = None
        self.Namespace = None
        self.Status = None
        self.StatusDesc = None
        self.Description = None
        self.Tags = None
        self.Type = None
        self.StatusReasons = None
        self.TotalProvisionedConcurrencyMem = None
        self.ReservedConcurrencyMem = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        self.FunctionId = params.get("FunctionId")
        self.Namespace = params.get("Namespace")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Type = params.get("Type")
        if params.get("StatusReasons") is not None:
            self.StatusReasons = []
            for item in params.get("StatusReasons"):
                obj = StatusReason()
                obj._deserialize(item)
                self.StatusReasons.append(obj)
        self.TotalProvisionedConcurrencyMem = params.get("TotalProvisionedConcurrencyMem")
        self.ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionLog(AbstractModel):
    """Log information

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param RetMsg: Return value after the function is executed\n        :type RetMsg: str\n        :param RequestId: RequestId corresponding to the executed function\n        :type RequestId: str\n        :param StartTime: Start time of the function execution\n        :type StartTime: str\n        :param RetCode: Function execution result. `0` indicates successful execution and other values indicate failure.\n        :type RetCode: int\n        :param InvokeFinished: It specifies whether the function invocation is finished. `1` indicates execution completion and other values indicate that exceptions occurred during the invocation.\n        :type InvokeFinished: int\n        :param Duration: Duration of the function execution. The unit is millisecond (ms).\n        :type Duration: float\n        :param BillDuration: Function billing duration. The unit is millisecond (ms). The value is rounded up to a multiple of 100 ms.\n        :type BillDuration: int\n        :param MemUsage: Actual memory size used during the function execution. The unit is byte.\n        :type MemUsage: int\n        :param Log: Function execution logs\n        :type Log: str\n        :param Level: Log level\n        :type Level: str\n        :param Source: Log source\n        :type Source: str\n        :param RetryNum: Number of retries\n        :type RetryNum: int\n        """
        self.FunctionName = None
        self.RetMsg = None
        self.RequestId = None
        self.StartTime = None
        self.RetCode = None
        self.InvokeFinished = None
        self.Duration = None
        self.BillDuration = None
        self.MemUsage = None
        self.Log = None
        self.Level = None
        self.Source = None
        self.RetryNum = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")
        self.StartTime = params.get("StartTime")
        self.RetCode = params.get("RetCode")
        self.InvokeFinished = params.get("InvokeFinished")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.MemUsage = params.get("MemUsage")
        self.Log = params.get("Log")
        self.Level = params.get("Level")
        self.Source = params.get("Source")
        self.RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FunctionVersion(AbstractModel):
    """Function version information

    """

    def __init__(self):
        """
        :param Version: Function version name\n        :type Version: str\n        :param Description: Version description
Note: This field may return null, indicating that no valid values is found.\n        :type Description: str\n        :param AddTime: The creation time
Note: This field may return null, indicating that no valid value was found.\n        :type AddTime: str\n        :param ModTime: Update time
Note: This field may return null, indicating that no valid value was found.\n        :type ModTime: str\n        """
        self.Version = None
        self.Description = None
        self.AddTime = None
        self.ModTime = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAccountRequest(AbstractModel):
    """GetAccount request structure.

    """


class GetAccountResponse(AbstractModel):
    """GetAccount response structure.

    """

    def __init__(self):
        """
        :param AccountUsage: Namespace usage information\n        :type AccountUsage: :class:`tencentcloud.scf.v20180416.models.UsageInfo`\n        :param AccountLimit: Namespace limit information\n        :type AccountLimit: :class:`tencentcloud.scf.v20180416.models.LimitsInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AccountUsage = None
        self.AccountLimit = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountUsage") is not None:
            self.AccountUsage = UsageInfo()
            self.AccountUsage._deserialize(params.get("AccountUsage"))
        if params.get("AccountLimit") is not None:
            self.AccountLimit = LimitsInfo()
            self.AccountLimit._deserialize(params.get("AccountLimit"))
        self.RequestId = params.get("RequestId")


class GetAliasRequest(AbstractModel):
    """GetAlias request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Name: Alias name\n        :type Name: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Name = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetAliasResponse(AbstractModel):
    """GetAlias response structure.

    """

    def __init__(self):
        """
        :param FunctionVersion: Master version pointed to by the alias\n        :type FunctionVersion: str\n        :param Name: Alias name\n        :type Name: str\n        :param RoutingConfig: Routing information of alias\n        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`\n        :param Description: Alias description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AddTime: str\n        :param ModTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ModTime: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FunctionVersion = None
        self.Name = None
        self.RoutingConfig = None
        self.Description = None
        self.AddTime = None
        self.ModTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        self.Name = params.get("Name")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        self.RequestId = params.get("RequestId")


class GetFunctionAddressRequest(AbstractModel):
    """GetFunctionAddress request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Qualifier: Function version\n        :type Qualifier: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionAddressResponse(AbstractModel):
    """GetFunctionAddress response structure.

    """

    def __init__(self):
        """
        :param Url: Cos address of the function\n        :type Url: str\n        :param CodeSha256: SHA256 code of the function\n        :type CodeSha256: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Url = None
        self.CodeSha256 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.CodeSha256 = params.get("CodeSha256")
        self.RequestId = params.get("RequestId")


class GetFunctionEventInvokeConfigRequest(AbstractModel):
    """GetFunctionEventInvokeConfig request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Namespace: Function namespace. Default value: default\n        :type Namespace: str\n        :param Qualifier: Function version. Default value: $LATEST\n        :type Qualifier: str\n        """
        self.FunctionName = None
        self.Namespace = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionEventInvokeConfigResponse(AbstractModel):
    """GetFunctionEventInvokeConfig response structure.

    """

    def __init__(self):
        """
        :param AsyncTriggerConfig: Async retry configuration information\n        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AsyncTriggerConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self.AsyncTriggerConfig = AsyncTriggerConfig()
            self.AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self.RequestId = params.get("RequestId")


class GetFunctionLogsRequest(AbstractModel):
    """GetFunctionLogs request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name.
- To ensure the compatibility of the [`GetFunctionLogs`](https://intl.cloud.tencent.com/document/product/583/18583?from_cn_redirect=1) API, the input parameter `FunctionName` is optional, but we recommend you enter it; otherwise, log acquisition may fail.
- After the function is connected to CLS, we recommend you use the [related CLS API](https://intl.cloud.tencent.com/document/product/614/16875?from_cn_redirect=1) to get the best log retrieval experience.\n        :type FunctionName: str\n        :param Offset: Data offset. The addition of `Offset` and `Limit` cannot exceed 10,000.\n        :type Offset: int\n        :param Limit: Length of the return data. The addition of `Offset` and `Limit` cannot exceed 10,000.\n        :type Limit: int\n        :param Order: It specifies whether to sort the logs in an ascending or descending order. The value is `desc` or `asc`.\n        :type Order: str\n        :param OrderBy: It specifies the sorting order of the logs based on a specified field, such as `function_name`, `duration`, `mem_usage`, and `start_time`.\n        :type OrderBy: str\n        :param Filter: Log filter used to identify whether to return logs of successful or failed requests. `filter.RetCode=not0` indicates that only the logs of failed requests will be returned. `filter.RetCode=is0` indicates that only the logs of successful requests will be returned. If this parameter is left blank, all logs will be returned. \n        :type Filter: :class:`tencentcloud.scf.v20180416.models.LogFilter`\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param Qualifier: Function version\n        :type Qualifier: str\n        :param FunctionRequestId: RequestId corresponding to the executed function\n        :type FunctionRequestId: str\n        :param StartTime: Query date, for example, 2017-05-16 20:00:00. The date must be within one day of the end time.\n        :type StartTime: str\n        :param EndTime: Query date, for example, 2017-05-16 20:59:59. The date must be within one day of the start time.\n        :type EndTime: str\n        :param SearchContext: This field is disused.\n        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`\n        """
        self.FunctionName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None
        self.Namespace = None
        self.Qualifier = None
        self.FunctionRequestId = None
        self.StartTime = None
        self.EndTime = None
        self.SearchContext = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = LogFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("SearchContext") is not None:
            self.SearchContext = LogSearchContext()
            self.SearchContext._deserialize(params.get("SearchContext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of function logs\n        :type TotalCount: int\n        :param Data: Function log information\n        :type Data: list of FunctionLog\n        :param SearchContext: This field is disused.\n        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Data = None
        self.SearchContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = FunctionLog()
                obj._deserialize(item)
                self.Data.append(obj)
        if params.get("SearchContext") is not None:
            self.SearchContext = LogSearchContext()
            self.SearchContext._deserialize(params.get("SearchContext"))
        self.RequestId = params.get("RequestId")


class GetFunctionRequest(AbstractModel):
    """GetFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function to obtain details\n        :type FunctionName: str\n        :param Qualifier: Function version number\n        :type Qualifier: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param ShowCode: It indicates whether to display the code. `TRUE` means displaying the code, and `FALSE` means hiding the code. The code will not be displayed for entry files exceeding 1 MB.\n        :type ShowCode: str\n        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None
        self.ShowCode = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
        self.ShowCode = params.get("ShowCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFunctionResponse(AbstractModel):
    """GetFunction response structure.

    """

    def __init__(self):
        """
        :param ModTime: Latest modification time of the function\n        :type ModTime: str\n        :param CodeInfo: Function code\n        :type CodeInfo: str\n        :param Description: Function description\n        :type Description: str\n        :param Triggers: Function trigger list\n        :type Triggers: list of Trigger\n        :param Handler: Function entry\n        :type Handler: str\n        :param CodeSize: Function code size\n        :type CodeSize: int\n        :param Timeout: Function timeout\n        :type Timeout: int\n        :param FunctionVersion: Function version\n        :type FunctionVersion: str\n        :param MemorySize: Maximum available memory of the function\n        :type MemorySize: int\n        :param Runtime: Function running environment\n        :type Runtime: str\n        :param FunctionName: Function name\n        :type FunctionName: str\n        :param VpcConfig: Function VPC\n        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`\n        :param UseGpu: Whether to use GPU\n        :type UseGpu: str\n        :param Environment: Function environment variable\n        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`\n        :param CodeResult: Whether the code is correct\n        :type CodeResult: str\n        :param CodeError: Code error information\n        :type CodeError: str\n        :param ErrNo: Error code\n        :type ErrNo: int\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param Role: Role bound to the function\n        :type Role: str\n        :param InstallDependency: Whether to install dependencies automatically\n        :type InstallDependency: str\n        :param Status: Function status. For valid values and status change process, please see [here](https://intl.cloud.tencent.com/document/product/583/47175?from_cn_redirect=1)\n        :type Status: str\n        :param StatusDesc: Status description\n        :type StatusDesc: str\n        :param ClsLogsetId: CLS logset to which logs are shipped\n        :type ClsLogsetId: str\n        :param ClsTopicId: CLS Topic to which logs are shipped\n        :type ClsTopicId: str\n        :param FunctionId: Function ID\n        :type FunctionId: str\n        :param Tags: Function tag list\n        :type Tags: list of Tag\n        :param EipConfig: EipConfig configuration\n        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipOutConfig`\n        :param AccessInfo: Domain name information\n        :type AccessInfo: :class:`tencentcloud.scf.v20180416.models.AccessInfo`\n        :param Type: Function type. The value is `HTTP` or `Event`.\n        :type Type: str\n        :param L5Enable: Whether to enable L5\n        :type L5Enable: str\n        :param Layers: Version information of a layer associated with a function\n        :type Layers: list of LayerVersionInfo\n        :param DeadLetterConfig: Information of a dead letter queue associated with a function\n        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`\n        :param AddTime: Function creation time\n        :type AddTime: str\n        :param PublicNetConfig: Public network access configuration
Note: This field may return null, indicating that no valid values can be obtained.\n        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigOut`\n        :param OnsEnable: Whether Ons is enabled
Note: This field may return null, indicating that no valid value was found.\n        :type OnsEnable: str\n        :param CfsConfig: File system configuration parameter, which is used for the function to mount the file system
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`\n        :param AvailableStatus: Function billing status. For valid values, please see [here](https://intl.cloud.tencent.com/document/product/583/47175?from_cn_redirect=1#.E5.87.BD.E6.95.B0.E8.AE.A1.E8.B4.B9.E7.8A.B6.E6.80.81)
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AvailableStatus: str\n        :param Qualifier: Function version
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Qualifier: str\n        :param InitTimeout: Timeout period for function initialization\n        :type InitTimeout: int\n        :param StatusReasons: Cause of function failure
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StatusReasons: list of StatusReason\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ModTime = None
        self.CodeInfo = None
        self.Description = None
        self.Triggers = None
        self.Handler = None
        self.CodeSize = None
        self.Timeout = None
        self.FunctionVersion = None
        self.MemorySize = None
        self.Runtime = None
        self.FunctionName = None
        self.VpcConfig = None
        self.UseGpu = None
        self.Environment = None
        self.CodeResult = None
        self.CodeError = None
        self.ErrNo = None
        self.Namespace = None
        self.Role = None
        self.InstallDependency = None
        self.Status = None
        self.StatusDesc = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.FunctionId = None
        self.Tags = None
        self.EipConfig = None
        self.AccessInfo = None
        self.Type = None
        self.L5Enable = None
        self.Layers = None
        self.DeadLetterConfig = None
        self.AddTime = None
        self.PublicNetConfig = None
        self.OnsEnable = None
        self.CfsConfig = None
        self.AvailableStatus = None
        self.Qualifier = None
        self.InitTimeout = None
        self.StatusReasons = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.CodeInfo = params.get("CodeInfo")
        self.Description = params.get("Description")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = Trigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.Handler = params.get("Handler")
        self.CodeSize = params.get("CodeSize")
        self.Timeout = params.get("Timeout")
        self.FunctionVersion = params.get("FunctionVersion")
        self.MemorySize = params.get("MemorySize")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.UseGpu = params.get("UseGpu")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.CodeResult = params.get("CodeResult")
        self.CodeError = params.get("CodeError")
        self.ErrNo = params.get("ErrNo")
        self.Namespace = params.get("Namespace")
        self.Role = params.get("Role")
        self.InstallDependency = params.get("InstallDependency")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.FunctionId = params.get("FunctionId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("EipConfig") is not None:
            self.EipConfig = EipOutConfig()
            self.EipConfig._deserialize(params.get("EipConfig"))
        if params.get("AccessInfo") is not None:
            self.AccessInfo = AccessInfo()
            self.AccessInfo._deserialize(params.get("AccessInfo"))
        self.Type = params.get("Type")
        self.L5Enable = params.get("L5Enable")
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self.Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        self.AddTime = params.get("AddTime")
        if params.get("PublicNetConfig") is not None:
            self.PublicNetConfig = PublicNetConfigOut()
            self.PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        self.OnsEnable = params.get("OnsEnable")
        if params.get("CfsConfig") is not None:
            self.CfsConfig = CfsConfig()
            self.CfsConfig._deserialize(params.get("CfsConfig"))
        self.AvailableStatus = params.get("AvailableStatus")
        self.Qualifier = params.get("Qualifier")
        self.InitTimeout = params.get("InitTimeout")
        if params.get("StatusReasons") is not None:
            self.StatusReasons = []
            for item in params.get("StatusReasons"):
                obj = StatusReason()
                obj._deserialize(item)
                self.StatusReasons.append(obj)
        self.RequestId = params.get("RequestId")


class GetLayerVersionRequest(AbstractModel):
    """GetLayerVersion request structure.

    """

    def __init__(self):
        """
        :param LayerName: Layer name\n        :type LayerName: str\n        :param LayerVersion: Version number\n        :type LayerVersion: int\n        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetLayerVersionResponse(AbstractModel):
    """GetLayerVersion response structure.

    """

    def __init__(self):
        """
        :param CompatibleRuntimes: Compatible runtimes\n        :type CompatibleRuntimes: list of str\n        :param CodeSha256: SHA256 encoding of version file on the layer\n        :type CodeSha256: str\n        :param Location: Download address of version file on the layer\n        :type Location: str\n        :param AddTime: Version creation time\n        :type AddTime: str\n        :param Description: Version description\n        :type Description: str\n        :param LicenseInfo: License information\n        :type LicenseInfo: str\n        :param LayerVersion: Version number\n        :type LayerVersion: int\n        :param LayerName: Layer name\n        :type LayerName: str\n        :param Status: Current status of specific layer version. Valid values:
Active: normal
Publishing: publishing
PublishFailed: publishing failed
Deleted: deleted\n        :type Status: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CompatibleRuntimes = None
        self.CodeSha256 = None
        self.Location = None
        self.AddTime = None
        self.Description = None
        self.LicenseInfo = None
        self.LayerVersion = None
        self.LayerName = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompatibleRuntimes = params.get("CompatibleRuntimes")
        self.CodeSha256 = params.get("CodeSha256")
        self.Location = params.get("Location")
        self.AddTime = params.get("AddTime")
        self.Description = params.get("Description")
        self.LicenseInfo = params.get("LicenseInfo")
        self.LayerVersion = params.get("LayerVersion")
        self.LayerName = params.get("LayerName")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class GetProvisionedConcurrencyConfigRequest(AbstractModel):
    """GetProvisionedConcurrencyConfig request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function for which to get the provisioned concurrency details.\n        :type FunctionName: str\n        :param Namespace: Function namespace. Default value: default.\n        :type Namespace: str\n        :param Qualifier: Function version number. If this parameter is left empty, the provisioned concurrency information of all function versions will be returned.\n        :type Qualifier: str\n        """
        self.FunctionName = None
        self.Namespace = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProvisionedConcurrencyConfigResponse(AbstractModel):
    """GetProvisionedConcurrencyConfig response structure.

    """

    def __init__(self):
        """
        :param UnallocatedConcurrencyNum: Unallocated provisioned concurrency amount of function.\n        :type UnallocatedConcurrencyNum: int\n        :param Allocated: Allocated provisioned concurrency amount of function.\n        :type Allocated: list of VersionProvisionedConcurrencyInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.UnallocatedConcurrencyNum = None
        self.Allocated = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UnallocatedConcurrencyNum = params.get("UnallocatedConcurrencyNum")
        if params.get("Allocated") is not None:
            self.Allocated = []
            for item in params.get("Allocated"):
                obj = VersionProvisionedConcurrencyInfo()
                obj._deserialize(item)
                self.Allocated.append(obj)
        self.RequestId = params.get("RequestId")


class GetReservedConcurrencyConfigRequest(AbstractModel):
    """GetReservedConcurrencyConfig request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function for which to get the provisioned concurrency details.\n        :type FunctionName: str\n        :param Namespace: Function namespace. Default value: default.\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReservedConcurrencyConfigResponse(AbstractModel):
    """GetReservedConcurrencyConfig response structure.

    """

    def __init__(self):
        """
        :param ReservedMem: Reserved concurrency memory of function.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ReservedMem: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.ReservedMem = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMem = params.get("ReservedMem")
        self.RequestId = params.get("RequestId")


class InvokeFunctionRequest(AbstractModel):
    """InvokeFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Qualifier: Version number or alias of the triggered function\n        :type Qualifier: str\n        :param Event: Function running parameter, which is in the JSON format. Maximum parameter size is 1 MB.\n        :type Event: str\n        :param LogType: If this field is specified for a synchronous invocation, the return value will contain a 4 KB log. Valid value: `None` (default) or `Tail`. If the value is `Tail`, `log` in the return parameter will contain the corresponding function execution log.\n        :type LogType: str\n        :param Namespace: Namespace\n        :type Namespace: str\n        :param RoutingKey: Traffic routing config in json format, e.g., {"k":"v"}. Please note that both "k" and "v" must be strings. Up to 1024 bytes allowed.\n        :type RoutingKey: str\n        """
        self.FunctionName = None
        self.Qualifier = None
        self.Event = None
        self.LogType = None
        self.Namespace = None
        self.RoutingKey = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Event = params.get("Event")
        self.LogType = params.get("LogType")
        self.Namespace = params.get("Namespace")
        self.RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeFunctionResponse(AbstractModel):
    """InvokeFunction response structure.

    """

    def __init__(self):
        """
        :param Result: Function execution result\n        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Result()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param InvocationType: The value is `RequestResponse` (synchronous) or `Event` (asynchronous). The default value is synchronous.\n        :type InvocationType: str\n        :param Qualifier: Version number or name of the triggered function\n        :type Qualifier: str\n        :param ClientContext: Function running parameter, which is in the JSON format. Maximum parameter size is 1 MB.\n        :type ClientContext: str\n        :param LogType: If this field is specified during sync invocation, the returned value will contain 4 KB of logs. Valid values: None, Tail. Default value: None. If the value is `Tail`, the `Log` field in the returned parameter will contain the corresponding function execution log\n        :type LogType: str\n        :param Namespace: Namespace\n        :type Namespace: str\n        :param RoutingKey: Traffic routing config in json format, e.g., {"k":"v"}. Please note that both "k" and "v" must be strings. Up to 1024 bytes allowed.\n        :type RoutingKey: str\n        """
        self.FunctionName = None
        self.InvocationType = None
        self.Qualifier = None
        self.ClientContext = None
        self.LogType = None
        self.Namespace = None
        self.RoutingKey = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.InvocationType = params.get("InvocationType")
        self.Qualifier = params.get("Qualifier")
        self.ClientContext = params.get("ClientContext")
        self.LogType = params.get("LogType")
        self.Namespace = params.get("Namespace")
        self.RoutingKey = params.get("RoutingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeResponse(AbstractModel):
    """Invoke response structure.

    """

    def __init__(self):
        """
        :param Result: Function execution result\n        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Result()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class LayerVersionInfo(AbstractModel):
    """Layer version information

    """

    def __init__(self):
        """
        :param CompatibleRuntimes: Runtime applicable to a version
Note: This field may return null, indicating that no valid values can be obtained.\n        :type CompatibleRuntimes: list of str\n        :param AddTime: Creation time\n        :type AddTime: str\n        :param Description: Version description
Note: This field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param LicenseInfo: License information
Note: This field may return null, indicating that no valid values can be obtained.\n        :type LicenseInfo: str\n        :param LayerVersion: Version number\n        :type LayerVersion: int\n        :param LayerName: Layer name\n        :type LayerName: str\n        :param Status: Current status of specific layer version. For valid values, please see [here](https://intl.cloud.tencent.com/document/product/583/47175?from_cn_redirect=1#.E5.B1.82.EF.BC.88layer.EF.BC.89.E7.8A.B6.E6.80.81)\n        :type Status: str\n        """
        self.CompatibleRuntimes = None
        self.AddTime = None
        self.Description = None
        self.LicenseInfo = None
        self.LayerVersion = None
        self.LayerName = None
        self.Status = None


    def _deserialize(self, params):
        self.CompatibleRuntimes = params.get("CompatibleRuntimes")
        self.AddTime = params.get("AddTime")
        self.Description = params.get("Description")
        self.LicenseInfo = params.get("LicenseInfo")
        self.LayerVersion = params.get("LayerVersion")
        self.LayerName = params.get("LayerName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LayerVersionSimple(AbstractModel):
    """Specifies a layer version

    """

    def __init__(self):
        """
        :param LayerName: Layer name\n        :type LayerName: str\n        :param LayerVersion: Version number\n        :type LayerVersion: int\n        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitsInfo(AbstractModel):
    """Limit information

    """

    def __init__(self):
        """
        :param NamespacesCount: Limit of namespace quantity\n        :type NamespacesCount: int\n        :param Namespace: Namespace limit information\n        :type Namespace: list of NamespaceLimit\n        """
        self.NamespacesCount = None
        self.Namespace = None


    def _deserialize(self, params):
        self.NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self.Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceLimit()
                obj._deserialize(item)
                self.Namespace.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesRequest(AbstractModel):
    """ListAliases request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param FunctionVersion: If this parameter is provided, only aliases associated with this function version will be returned.\n        :type FunctionVersion: str\n        :param Offset: Data offset. Default value: 0\n        :type Offset: str\n        :param Limit: Number of results to be returned. Default value: 20\n        :type Limit: str\n        """
        self.FunctionName = None
        self.Namespace = None
        self.FunctionVersion = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.FunctionVersion = params.get("FunctionVersion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAliasesResponse(AbstractModel):
    """ListAliases response structure.

    """

    def __init__(self):
        """
        :param Aliases: Alias list\n        :type Aliases: list of Alias\n        :param TotalCount: Total number of aliases
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Aliases = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Aliases") is not None:
            self.Aliases = []
            for item in params.get("Aliases"):
                obj = Alias()
                obj._deserialize(item)
                self.Aliases.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListAsyncEventsRequest(AbstractModel):
    """ListAsyncEvents request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Namespace: Namespace\n        :type Namespace: str\n        :param Qualifier: Filter (function version)\n        :type Qualifier: str\n        :param InvokeType: Filter (invocation type list)\n        :type InvokeType: list of str\n        :param Status: Filter (event status list)\n        :type Status: list of str\n        :param StartTimeInterval: Filter (left-closed-right-open range of execution start time)\n        :type StartTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`\n        :param EndTimeInterval: Filter (left-closed-right-open range of execution end time)\n        :type EndTimeInterval: :class:`tencentcloud.scf.v20180416.models.TimeInterval`\n        :param Order: Valid values: ASC, DESC. Default value: DESC\n        :type Order: str\n        :param Orderby: Valid values: StartTime, EndTime. Default value: StartTime\n        :type Orderby: str\n        :param Offset: Data offset. Default value: 0\n        :type Offset: int\n        :param Limit: Number of results to be returned. Default value: 20. Maximum value: 100\n        :type Limit: int\n        :param InvokeRequestId: Filter (event invocation request ID)\n        :type InvokeRequestId: str\n        """
        self.FunctionName = None
        self.Namespace = None
        self.Qualifier = None
        self.InvokeType = None
        self.Status = None
        self.StartTimeInterval = None
        self.EndTimeInterval = None
        self.Order = None
        self.Orderby = None
        self.Offset = None
        self.Limit = None
        self.InvokeRequestId = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.InvokeType = params.get("InvokeType")
        self.Status = params.get("Status")
        if params.get("StartTimeInterval") is not None:
            self.StartTimeInterval = TimeInterval()
            self.StartTimeInterval._deserialize(params.get("StartTimeInterval"))
        if params.get("EndTimeInterval") is not None:
            self.EndTimeInterval = TimeInterval()
            self.EndTimeInterval._deserialize(params.get("EndTimeInterval"))
        self.Order = params.get("Order")
        self.Orderby = params.get("Orderby")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InvokeRequestId = params.get("InvokeRequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAsyncEventsResponse(AbstractModel):
    """ListAsyncEvents response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of events that meet the filter\n        :type TotalCount: int\n        :param EventList: Async event list\n        :type EventList: list of AsyncEvent\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.EventList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = AsyncEvent()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.RequestId = params.get("RequestId")


class ListFunctionsRequest(AbstractModel):
    """ListFunctions request structure.

    """

    def __init__(self):
        """
        :param Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.\n        :type Order: str\n        :param Orderby: It specifies the sorting order of the results according to a specified field, such as `AddTime`, `ModTime`, and `FunctionName`.\n        :type Orderby: str\n        :param Offset: Data offset. The default value is `0`.\n        :type Offset: int\n        :param Limit: Return data length. The default value is `20`.\n        :type Limit: int\n        :param SearchKey: It specifies whether to support fuzzy matching for the function name.\n        :type SearchKey: str\n        :param Namespace: Namespace\n        :type Namespace: str\n        :param Description: Function description. Fuzzy search is supported.\n        :type Description: str\n        :param Filters: Filters
- tag:tag-key - String - Required: No - Filtering criteria based on tag-key - value pairs. Replace `tag-key` with a specific tag-key.

The maximum number of `Filters` for each request is 10, and that of `Filter.Values` is 5.\n        :type Filters: list of Filter\n        """
        self.Order = None
        self.Orderby = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.Namespace = None
        self.Description = None
        self.Filters = None


    def _deserialize(self, params):
        self.Order = params.get("Order")
        self.Orderby = params.get("Orderby")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
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
        


class ListFunctionsResponse(AbstractModel):
    """ListFunctions response structure.

    """

    def __init__(self):
        """
        :param Functions: Function list\n        :type Functions: list of Function\n        :param TotalCount: Total number\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Functions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = []
            for item in params.get("Functions"):
                obj = Function()
                obj._deserialize(item)
                self.Functions.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListLayerVersionsRequest(AbstractModel):
    """ListLayerVersions request structure.

    """

    def __init__(self):
        """
        :param LayerName: Layer name\n        :type LayerName: str\n        :param CompatibleRuntime: Compatible runtimes\n        :type CompatibleRuntime: list of str\n        """
        self.LayerName = None
        self.CompatibleRuntime = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.CompatibleRuntime = params.get("CompatibleRuntime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayerVersionsResponse(AbstractModel):
    """ListLayerVersions response structure.

    """

    def __init__(self):
        """
        :param LayerVersions: Layer version list\n        :type LayerVersions: list of LayerVersionInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LayerVersions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LayerVersions") is not None:
            self.LayerVersions = []
            for item in params.get("LayerVersions"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self.LayerVersions.append(obj)
        self.RequestId = params.get("RequestId")


class ListLayersRequest(AbstractModel):
    """ListLayers request structure.

    """

    def __init__(self):
        """
        :param CompatibleRuntime: Compatible runtimes\n        :type CompatibleRuntime: str\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Limit\n        :type Limit: int\n        :param SearchKey: Query key, which fuzzily matches the name\n        :type SearchKey: str\n        """
        self.CompatibleRuntime = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.CompatibleRuntime = params.get("CompatibleRuntime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListLayersResponse(AbstractModel):
    """ListLayers response structure.

    """

    def __init__(self):
        """
        :param Layers: Layer list\n        :type Layers: list of LayerVersionInfo\n        :param TotalCount: Total number of layers\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Layers = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionInfo()
                obj._deserialize(item)
                self.Layers.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListNamespacesRequest(AbstractModel):
    """ListNamespaces request structure.

    """

    def __init__(self):
        """
        :param Limit: Return data length. The default value is `20`.\n        :type Limit: int\n        :param Offset: Data offset. The default value is `0`.\n        :type Offset: int\n        :param Orderby: It specifies the sorting order of the results according to a specified field, such as `Name` and `Updatetime`.\n        :type Orderby: str\n        :param Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.\n        :type Order: str\n        """
        self.Limit = None
        self.Offset = None
        self.Orderby = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Orderby = params.get("Orderby")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListNamespacesResponse(AbstractModel):
    """ListNamespaces response structure.

    """

    def __init__(self):
        """
        :param Namespaces: Namespace details\n        :type Namespaces: list of Namespace\n        :param TotalCount: Number of return namespaces\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Namespaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Namespaces") is not None:
            self.Namespaces = []
            for item in params.get("Namespaces"):
                obj = Namespace()
                obj._deserialize(item)
                self.Namespaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListTriggersRequest(AbstractModel):
    """ListTriggers request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Namespace: Namespace. Default value: default\n        :type Namespace: str\n        :param Offset: Data offset. Default value: 0\n        :type Offset: int\n        :param Limit: Number of results to be returned. Default value: 20\n        :type Limit: int\n        :param OrderBy: Indicates by which field to sort the returned results. Valid values: add_time, mod_time. Default value: mod_time\n        :type OrderBy: str\n        :param Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC, DESC. Default value: DESC\n        :type Order: str\n        :param Filters: * Qualifier:
Function version, alias\n        :type Filters: list of Filter\n        """
        self.FunctionName = None
        self.Namespace = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.Order = None
        self.Filters = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.Order = params.get("Order")
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
        


class ListTriggersResponse(AbstractModel):
    """ListTriggers response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of triggers\n        :type TotalCount: int\n        :param Triggers: Trigger list\n        :type Triggers: list of TriggerInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Triggers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = TriggerInfo()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.RequestId = params.get("RequestId")


class ListVersionByFunctionRequest(AbstractModel):
    """ListVersionByFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function Name\n        :type FunctionName: str\n        :param Namespace: The namespace where the function locates\n        :type Namespace: str\n        :param Offset: Data offset. The default value is `0`.\n        :type Offset: int\n        :param Limit: Return data length. The default value is `20`.\n        :type Limit: int\n        :param Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.\n        :type Order: str\n        :param OrderBy: It specifies the sorting order of the results according to a specified field, such as `AddTime`, `ModTime`.\n        :type OrderBy: str\n        """
        self.FunctionName = None
        self.Namespace = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVersionByFunctionResponse(AbstractModel):
    """ListVersionByFunction response structure.

    """

    def __init__(self):
        """
        :param FunctionVersion: Function version\n        :type FunctionVersion: list of str\n        :param Versions: Function version list
Note: This field may return null, indicating that no valid values is found.\n        :type Versions: list of FunctionVersion\n        :param TotalCount: Total number of function versions
Note: This field may return null, indicating that no valid value was found.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FunctionVersion = None
        self.Versions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = FunctionVersion()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class LogFilter(AbstractModel):
    """Log filtering criteria, which is for distinguishing between logs of successful and failed execution

    """

    def __init__(self):
        """
        :param RetCode: Values of `filter.RetCode` include:
not0, indicating that only logs of failed execution will be returned.
is0, indicating that only logs of successful execution will be returned.
TimeLimitExceeded, indicating that logs of function invocations which timed out will be returned.
ResourceLimitExceeded, indicating that logs of function invocations during which resources exceeded the upper limit will be returned.
UserCodeException, indicating that logs of function invocations during which a user code error occurred will be returned.
Blank, indicating that all logs will be returned.\n        :type RetCode: str\n        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogSearchContext(AbstractModel):
    """Log search context

    """

    def __init__(self):
        """
        :param Offset: Offset.\n        :type Offset: str\n        :param Limit: Log record number\n        :type Limit: int\n        :param Keyword: Log keyword\n        :type Keyword: str\n        :param Type: Log type. The value is `Application` (default) or `Platform`.\n        :type Type: str\n        """
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Namespace(AbstractModel):
    """Namespace

    """

    def __init__(self):
        """
        :param ModTime: Creation time of the namespace\n        :type ModTime: str\n        :param AddTime: Modification time of the namespace\n        :type AddTime: str\n        :param Description: Namespace description\n        :type Description: str\n        :param Name: Namespace name\n        :type Name: str\n        :param Type: The default value is default. TCB indicates that the namespace is developed and created through the mini-program cloud.\n        :type Type: str\n        """
        self.ModTime = None
        self.AddTime = None
        self.Description = None
        self.Name = None
        self.Type = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceLimit(AbstractModel):
    """Namespace limit

    """

    def __init__(self):
        """
        :param FunctionsCount: Total number of functions\n        :type FunctionsCount: int\n        :param Trigger: Trigger information\n        :type Trigger: :class:`tencentcloud.scf.v20180416.models.TriggerCount`\n        :param Namespace: Namespace name\n        :type Namespace: str\n        :param ConcurrentExecutions: Concurrency\n        :type ConcurrentExecutions: int\n        :param TimeoutLimit: Timeout limit\n        :type TimeoutLimit: int\n        :param TestModelLimit: Test event limit
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TestModelLimit: int\n        :param InitTimeoutLimit: Initialization timeout limit\n        :type InitTimeoutLimit: int\n        :param RetryNumLimit: Limit of async retry attempt quantity\n        :type RetryNumLimit: int\n        :param MinMsgTTL: Lower limit of message retention time for async retry\n        :type MinMsgTTL: int\n        :param MaxMsgTTL: Upper limit of message retention time for async retry\n        :type MaxMsgTTL: int\n        """
        self.FunctionsCount = None
        self.Trigger = None
        self.Namespace = None
        self.ConcurrentExecutions = None
        self.TimeoutLimit = None
        self.TestModelLimit = None
        self.InitTimeoutLimit = None
        self.RetryNumLimit = None
        self.MinMsgTTL = None
        self.MaxMsgTTL = None


    def _deserialize(self, params):
        self.FunctionsCount = params.get("FunctionsCount")
        if params.get("Trigger") is not None:
            self.Trigger = TriggerCount()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")
        self.ConcurrentExecutions = params.get("ConcurrentExecutions")
        self.TimeoutLimit = params.get("TimeoutLimit")
        self.TestModelLimit = params.get("TestModelLimit")
        self.InitTimeoutLimit = params.get("InitTimeoutLimit")
        self.RetryNumLimit = params.get("RetryNumLimit")
        self.MinMsgTTL = params.get("MinMsgTTL")
        self.MaxMsgTTL = params.get("MaxMsgTTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceUsage(AbstractModel):
    """Namespace usage information

    """

    def __init__(self):
        """
        :param Functions: Function array\n        :type Functions: list of str\n        :param Namespace: Namespace name\n        :type Namespace: str\n        :param FunctionsCount: Number of functions in namespace\n        :type FunctionsCount: int\n        """
        self.Functions = None
        self.Namespace = None
        self.FunctionsCount = None


    def _deserialize(self, params):
        self.Functions = params.get("Functions")
        self.Namespace = params.get("Namespace")
        self.FunctionsCount = params.get("FunctionsCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetConfigIn(AbstractModel):
    """Public network access configuration

    """

    def __init__(self):
        """
        :param PublicNetStatus: Whether to enable public network access. Valid values: ['DISABLE', 'ENABLE']\n        :type PublicNetStatus: str\n        :param EipConfig: EIP configuration\n        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigIn`\n        """
        self.PublicNetStatus = None
        self.EipConfig = None


    def _deserialize(self, params):
        self.PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self.EipConfig = EipConfigIn()
            self.EipConfig._deserialize(params.get("EipConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicNetConfigOut(AbstractModel):
    """Public network access configuration

    """

    def __init__(self):
        """
        :param PublicNetStatus: Whether to enable public network access. Valid values: ['DISABLE', 'ENABLE']\n        :type PublicNetStatus: str\n        :param EipConfig: EIP configuration\n        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigOut`\n        """
        self.PublicNetStatus = None
        self.EipConfig = None


    def _deserialize(self, params):
        self.PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self.EipConfig = EipConfigOut()
            self.EipConfig._deserialize(params.get("EipConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionRequest(AbstractModel):
    """PublishLayerVersion request structure.

    """

    def __init__(self):
        """
        :param LayerName: Layer name, which can contain 1-64 English letters, digits, hyphens, and underscores, must begin with a letter, and cannot end with a hyphen or underscore\n        :type LayerName: str\n        :param CompatibleRuntimes: Runtimes compatible with layer. Multiple choices are allowed. The valid values of this parameter correspond to the valid values of the `Runtime` of the function.\n        :type CompatibleRuntimes: list of str\n        :param Content: Layer file source or content\n        :type Content: :class:`tencentcloud.scf.v20180416.models.Code`\n        :param Description: Layer version description\n        :type Description: str\n        :param LicenseInfo: Software license of layer\n        :type LicenseInfo: str\n        """
        self.LayerName = None
        self.CompatibleRuntimes = None
        self.Content = None
        self.Description = None
        self.LicenseInfo = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.CompatibleRuntimes = params.get("CompatibleRuntimes")
        if params.get("Content") is not None:
            self.Content = Code()
            self.Content._deserialize(params.get("Content"))
        self.Description = params.get("Description")
        self.LicenseInfo = params.get("LicenseInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishLayerVersionResponse(AbstractModel):
    """PublishLayerVersion response structure.

    """

    def __init__(self):
        """
        :param LayerVersion: Version number of the layer created in this request\n        :type LayerVersion: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.LayerVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LayerVersion = params.get("LayerVersion")
        self.RequestId = params.get("RequestId")


class PublishVersionRequest(AbstractModel):
    """PublishVersion request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the released function\n        :type FunctionName: str\n        :param Description: Function description\n        :type Description: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Description = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishVersionResponse(AbstractModel):
    """PublishVersion response structure.

    """

    def __init__(self):
        """
        :param FunctionVersion: Function version\n        :type FunctionVersion: str\n        :param CodeSize: Code size\n        :type CodeSize: int\n        :param MemorySize: Maximum available memory\n        :type MemorySize: int\n        :param Description: Function description\n        :type Description: str\n        :param Handler: Function entry\n        :type Handler: str\n        :param Timeout: Function timeout\n        :type Timeout: int\n        :param Runtime: Function running environment\n        :type Runtime: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.FunctionVersion = None
        self.CodeSize = None
        self.MemorySize = None
        self.Description = None
        self.Handler = None
        self.Timeout = None
        self.Runtime = None
        self.Namespace = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FunctionVersion = params.get("FunctionVersion")
        self.CodeSize = params.get("CodeSize")
        self.MemorySize = params.get("MemorySize")
        self.Description = params.get("Description")
        self.Handler = params.get("Handler")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        self.Namespace = params.get("Namespace")
        self.RequestId = params.get("RequestId")


class PutProvisionedConcurrencyConfigRequest(AbstractModel):
    """PutProvisionedConcurrencyConfig request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function for which to set the provisioned concurrency\n        :type FunctionName: str\n        :param Qualifier: Function version number. Note: the `$LATEST` version does not support provisioned concurrency\n        :type Qualifier: str\n        :param VersionProvisionedConcurrencyNum: Provisioned concurrency amount. Note: there is an upper limit for the sum of provisioned concurrency amounts of all versions, which currently is the function's maximum concurrency quota minus 100\n        :type VersionProvisionedConcurrencyNum: int\n        :param Namespace: Function namespace. Default value: `default`\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.Qualifier = None
        self.VersionProvisionedConcurrencyNum = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.VersionProvisionedConcurrencyNum = params.get("VersionProvisionedConcurrencyNum")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutProvisionedConcurrencyConfigResponse(AbstractModel):
    """PutProvisionedConcurrencyConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutReservedConcurrencyConfigRequest(AbstractModel):
    """PutReservedConcurrencyConfig request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function for which to set the provisioned concurrency\n        :type FunctionName: str\n        :param ReservedConcurrencyMem: Reserved concurrency memory of function. Note: the upper limit for the total reserved concurrency memory of the function is the user's total concurrency memory minus 12800\n        :type ReservedConcurrencyMem: int\n        :param Namespace: Function namespace. Default value: `default`\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.ReservedConcurrencyMem = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.ReservedConcurrencyMem = params.get("ReservedConcurrencyMem")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutReservedConcurrencyConfigResponse(AbstractModel):
    """PutReservedConcurrencyConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PutTotalConcurrencyConfigRequest(AbstractModel):
    """PutTotalConcurrencyConfig request structure.

    """

    def __init__(self):
        """
        :param TotalConcurrencyMem: Account concurrency memory quota. Note: the lower limit for the account concurrency memory quota is the user's total concurrency memory used + 12800\n        :type TotalConcurrencyMem: int\n        :param Namespace: Namespace. Default value: `default`\n        :type Namespace: str\n        """
        self.TotalConcurrencyMem = None
        self.Namespace = None


    def _deserialize(self, params):
        self.TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutTotalConcurrencyConfigResponse(AbstractModel):
    """PutTotalConcurrencyConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Result(AbstractModel):
    """Response of the executed function

    """

    def __init__(self):
        """
        :param Log: It indicates the log output during the function execution. Null is returned for asynchronous invocations.\n        :type Log: str\n        :param RetMsg: It indicates the response from the executed function. Null is returned for asynchronous invocations.\n        :type RetMsg: str\n        :param ErrMsg: It indicates the error message of the executed function. Null is returned for asynchronous invocations.\n        :type ErrMsg: str\n        :param MemUsage: It indicates the memory size (in bytes) when the function is running. Null is returned for asynchronous invocations.\n        :type MemUsage: int\n        :param Duration: It indicates the duration (in milliseconds) required for running the function. Null is returned for asynchronous invocations.\n        :type Duration: float\n        :param BillDuration: It indicates the billing duration (in milliseconds) for the function. Null is returned for asynchronous invocations.\n        :type BillDuration: int\n        :param FunctionRequestId: ID of the executed function\n        :type FunctionRequestId: str\n        :param InvokeResult: `0` indicates successful execution. Null is returned for asynchronous invocations.\n        :type InvokeResult: int\n        """
        self.Log = None
        self.RetMsg = None
        self.ErrMsg = None
        self.MemUsage = None
        self.Duration = None
        self.BillDuration = None
        self.FunctionRequestId = None
        self.InvokeResult = None


    def _deserialize(self, params):
        self.Log = params.get("Log")
        self.RetMsg = params.get("RetMsg")
        self.ErrMsg = params.get("ErrMsg")
        self.MemUsage = params.get("MemUsage")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.InvokeResult = params.get("InvokeResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryConfig(AbstractModel):
    """Async retry configuration

    """

    def __init__(self):
        """
        :param RetryNum: Number of retry attempts\n        :type RetryNum: int\n        """
        self.RetryNum = None


    def _deserialize(self, params):
        self.RetryNum = params.get("RetryNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoutingConfig(AbstractModel):
    """Version routing configuration of alias

    """

    def __init__(self):
        """
        :param AdditionalVersionWeights: Additional version with random weight-based routing\n        :type AdditionalVersionWeights: list of VersionWeight\n        :param AddtionVersionMatchs: Additional version with rule-based routing\n        :type AddtionVersionMatchs: list of VersionMatch\n        """
        self.AdditionalVersionWeights = None
        self.AddtionVersionMatchs = None


    def _deserialize(self, params):
        if params.get("AdditionalVersionWeights") is not None:
            self.AdditionalVersionWeights = []
            for item in params.get("AdditionalVersionWeights"):
                obj = VersionWeight()
                obj._deserialize(item)
                self.AdditionalVersionWeights.append(obj)
        if params.get("AddtionVersionMatchs") is not None:
            self.AddtionVersionMatchs = []
            for item in params.get("AddtionVersionMatchs"):
                obj = VersionMatch()
                obj._deserialize(item)
                self.AddtionVersionMatchs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusReason(AbstractModel):
    """State reason description

    """

    def __init__(self):
        """
        :param ErrorCode: Error code\n        :type ErrorCode: str\n        :param ErrorMessage: Error message\n        :type ErrorMessage: str\n        """
        self.ErrorCode = None
        self.ErrorMessage = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Function tag

    """

    def __init__(self):
        """
        :param Key: Tag key\n        :type Key: str\n        :param Value: Tag value\n        :type Value: str\n        """
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
        


class TerminateAsyncEventRequest(AbstractModel):
    """TerminateAsyncEvent request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param InvokeRequestId: Terminated invocation request ID\n        :type InvokeRequestId: str\n        :param Namespace: Namespace\n        :type Namespace: str\n        """
        self.FunctionName = None
        self.InvokeRequestId = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.InvokeRequestId = params.get("InvokeRequestId")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateAsyncEventResponse(AbstractModel):
    """TerminateAsyncEvent response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TimeInterval(AbstractModel):
    """Left-closed-right-open time range between the start time and end time in the format of "%Y-%m-%d %H:%M:%S"

    """

    def __init__(self):
        """
        :param Start: Start time (inclusive) in the format of "%Y-%m-%d %H:%M:%S"\n        :type Start: str\n        :param End: End time (exclusive) in the format of "%Y-%m-%d %H:%M:%S"\n        :type End: str\n        """
        self.Start = None
        self.End = None


    def _deserialize(self, params):
        self.Start = params.get("Start")
        self.End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Trigger(AbstractModel):
    """Trigger type

    """

    def __init__(self):
        """
        :param ModTime: Latest modification time of the trigger\n        :type ModTime: str\n        :param Type: Trigger type\n        :type Type: str\n        :param TriggerDesc: Detailed trigger configuration\n        :type TriggerDesc: str\n        :param TriggerName: Trigger name\n        :type TriggerName: str\n        :param AddTime: Creation time of the trigger\n        :type AddTime: str\n        :param Enable: Enabling switch\n        :type Enable: int\n        :param CustomArgument: Custom parameter\n        :type CustomArgument: str\n        :param AvailableStatus: Trigger status\n        :type AvailableStatus: str\n        :param ResourceId: Minimum resource ID of trigger\n        :type ResourceId: str\n        :param BindStatus: Trigger-Function binding status\n        :type BindStatus: str\n        :param TriggerAttribute: Trigger type. Two-way means that the trigger can be manipulated in both consoles, while one-way means that the trigger can be created only in the SCF Console\n        :type TriggerAttribute: str\n        :param Qualifier: The alias or version bound with the trigger\n        :type Qualifier: str\n        """
        self.ModTime = None
        self.Type = None
        self.TriggerDesc = None
        self.TriggerName = None
        self.AddTime = None
        self.Enable = None
        self.CustomArgument = None
        self.AvailableStatus = None
        self.ResourceId = None
        self.BindStatus = None
        self.TriggerAttribute = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.TriggerName = params.get("TriggerName")
        self.AddTime = params.get("AddTime")
        self.Enable = params.get("Enable")
        self.CustomArgument = params.get("CustomArgument")
        self.AvailableStatus = params.get("AvailableStatus")
        self.ResourceId = params.get("ResourceId")
        self.BindStatus = params.get("BindStatus")
        self.TriggerAttribute = params.get("TriggerAttribute")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerCount(AbstractModel):
    """`TriggerCount` describes the numbers of triggers in different types

    """

    def __init__(self):
        """
        :param Cos: Number of COS triggers\n        :type Cos: int\n        :param Timer: Number of timer triggers\n        :type Timer: int\n        :param Cmq: Number of CMQ triggers\n        :type Cmq: int\n        :param Total: Total number of triggers\n        :type Total: int\n        :param Ckafka: Number of CKafka triggers\n        :type Ckafka: int\n        :param Apigw: Number of API Gateway triggers\n        :type Apigw: int\n        :param Cls: Number of CLS triggers\n        :type Cls: int\n        :param Clb: Number of CLB triggers\n        :type Clb: int\n        :param Mps: Number of MPS triggers\n        :type Mps: int\n        :param Cm: Number of CM triggers\n        :type Cm: int\n        :param Vod: Number of VOD triggers\n        :type Vod: int\n        """
        self.Cos = None
        self.Timer = None
        self.Cmq = None
        self.Total = None
        self.Ckafka = None
        self.Apigw = None
        self.Cls = None
        self.Clb = None
        self.Mps = None
        self.Cm = None
        self.Vod = None


    def _deserialize(self, params):
        self.Cos = params.get("Cos")
        self.Timer = params.get("Timer")
        self.Cmq = params.get("Cmq")
        self.Total = params.get("Total")
        self.Ckafka = params.get("Ckafka")
        self.Apigw = params.get("Apigw")
        self.Cls = params.get("Cls")
        self.Clb = params.get("Clb")
        self.Mps = params.get("Mps")
        self.Cm = params.get("Cm")
        self.Vod = params.get("Vod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerInfo(AbstractModel):
    """Trigger information

    """

    def __init__(self):
        """
        :param Enable: Whether to enable\n        :type Enable: int\n        :param Qualifier: Function version or alias\n        :type Qualifier: str\n        :param TriggerName: Trigger name\n        :type TriggerName: str\n        :param Type: Trigger type\n        :type Type: str\n        :param TriggerDesc: Detailed configuration of trigger\n        :type TriggerDesc: str\n        :param AvailableStatus: Whether the trigger is available\n        :type AvailableStatus: str\n        :param CustomArgument: Custom parameter
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CustomArgument: str\n        :param AddTime: Trigger creation time\n        :type AddTime: str\n        :param ModTime: Trigger last modified time\n        :type ModTime: str\n        :param ResourceId: Minimum resource ID of trigger\n        :type ResourceId: str\n        :param BindStatus: Trigger-Function binding status\n        :type BindStatus: str\n        :param TriggerAttribute: Trigger type. Two-way means that the trigger can be manipulated in both consoles, while one-way means that the trigger can be created only in the SCF Console\n        :type TriggerAttribute: str\n        """
        self.Enable = None
        self.Qualifier = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.AvailableStatus = None
        self.CustomArgument = None
        self.AddTime = None
        self.ModTime = None
        self.ResourceId = None
        self.BindStatus = None
        self.TriggerAttribute = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.Qualifier = params.get("Qualifier")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.AvailableStatus = params.get("AvailableStatus")
        self.CustomArgument = params.get("CustomArgument")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")
        self.ResourceId = params.get("ResourceId")
        self.BindStatus = params.get("BindStatus")
        self.TriggerAttribute = params.get("TriggerAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Name: Alias name\n        :type Name: str\n        :param FunctionVersion: Master version pointed to by the alias\n        :type FunctionVersion: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param RoutingConfig: Routing information of alias, which is required if you need to specify an additional version for the alias.\n        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`\n        :param Description: Alias description\n        :type Description: str\n        """
        self.FunctionName = None
        self.Name = None
        self.FunctionVersion = None
        self.Namespace = None
        self.RoutingConfig = None
        self.Description = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.FunctionVersion = params.get("FunctionVersion")
        self.Namespace = params.get("Namespace")
        if params.get("RoutingConfig") is not None:
            self.RoutingConfig = RoutingConfig()
            self.RoutingConfig._deserialize(params.get("RoutingConfig"))
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionCodeRequest(AbstractModel):
    """UpdateFunctionCode request structure.

    """

    def __init__(self):
        """
        :param Handler: Function handler name, which is in the `file name.function name` form. Use a period (.) to separate a file name and function name. The file name and function name must start and end with letters and contain 2-60 characters, including letters, digits, underscores (_), and hyphens (-).\n        :type Handler: str\n        :param FunctionName: Name of the function to be modified\n        :type FunctionName: str\n        :param CosBucketName: COS bucket name\n        :type CosBucketName: str\n        :param CosObjectName: COS object path\n        :type CosObjectName: str\n        :param ZipFile: It contains a function code file and its dependencies in the ZIP format. When you use this API, the ZIP file needs to be encoded with Base64. Up to 20 MB is supported.\n        :type ZipFile: str\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param CosBucketRegion: COS region. Note: Beijing includes ap-beijing and ap-beijing-1.\n        :type CosBucketRegion: str\n        :param EnvId: Function environment\n        :type EnvId: str\n        :param Publish: It specifies whether to synchronously release a new version during the update. The default value is `FALSE`, indicating not to release a new version.\n        :type Publish: str\n        :param Code: Function code\n        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`\n        :param CodeSource: Code source. Valid values: ZipFile, Cos, Inline\n        :type CodeSource: str\n        """
        self.Handler = None
        self.FunctionName = None
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.Namespace = None
        self.CosBucketRegion = None
        self.EnvId = None
        self.Publish = None
        self.Code = None
        self.CodeSource = None


    def _deserialize(self, params):
        self.Handler = params.get("Handler")
        self.FunctionName = params.get("FunctionName")
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.Namespace = params.get("Namespace")
        self.CosBucketRegion = params.get("CosBucketRegion")
        self.EnvId = params.get("EnvId")
        self.Publish = params.get("Publish")
        if params.get("Code") is not None:
            self.Code = Code()
            self.Code._deserialize(params.get("Code"))
        self.CodeSource = params.get("CodeSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionConfigurationRequest(AbstractModel):
    """UpdateFunctionConfiguration request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function to be modified\n        :type FunctionName: str\n        :param Description: Function description. It can contain up to 1,000 characters, including letters, digits, spaces, commas (,), periods (.), and Chinese characters.\n        :type Description: str\n        :param MemorySize: Memory size available for function during execution. Default value: 128 MB. Value range: 64 or 128-3,072 MB in increments of 128 MB.\n        :type MemorySize: int\n        :param Timeout: Maximum execution duration of function in seconds. Value range: 1-900 seconds. Default value: 3 seconds\n        :type Timeout: int\n        :param Runtime: Function runtime environment. Valid values: Python2.7, Python3.6, Nodejs6.10, Nodejs8.9, Nodejs10.15, Nodejs12.16, PHP5, PHP7, Go1, Java8, CustomRuntime\n        :type Runtime: str\n        :param Environment: Function environment variable\n        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`\n        :param Namespace: Function namespace\n        :type Namespace: str\n        :param VpcConfig: Function VPC configuration\n        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`\n        :param Role: Role bound to the function\n        :type Role: str\n        :param ClsLogsetId: CLS logset ID to which logs are shipped\n        :type ClsLogsetId: str\n        :param ClsTopicId: CLS Topic ID to which logs are shipped\n        :type ClsTopicId: str\n        :param Publish: It specifies whether to synchronously publish a new version during the update. The default value is `FALSE`, indicating not to publish a new version\n        :type Publish: str\n        :param L5Enable: Whether to enable L5 access. TRUE: enable; FALSE: not enable\n        :type L5Enable: str\n        :param Layers: List of layer versions that bound with the function. Files with the same name will be overridden by the bound layer versions according to the ascending order in the list. \n        :type Layers: list of LayerVersionSimple\n        :param DeadLetterConfig: Information of a dead letter queue associated with a function\n        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`\n        :param PublicNetConfig: Public network access configuration\n        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`\n        :param CfsConfig: File system configuration input parameter, which is used for the function to bind the CFS file system\n        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`\n        :param InitTimeout: Timeout period for function initialization. Default value: 15 seconds\n        :type InitTimeout: int\n        """
        self.FunctionName = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Runtime = None
        self.Environment = None
        self.Namespace = None
        self.VpcConfig = None
        self.Role = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.Publish = None
        self.L5Enable = None
        self.Layers = None
        self.DeadLetterConfig = None
        self.PublicNetConfig = None
        self.CfsConfig = None
        self.InitTimeout = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.Namespace = params.get("Namespace")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.Role = params.get("Role")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.Publish = params.get("Publish")
        self.L5Enable = params.get("L5Enable")
        if params.get("Layers") is not None:
            self.Layers = []
            for item in params.get("Layers"):
                obj = LayerVersionSimple()
                obj._deserialize(item)
                self.Layers.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self.DeadLetterConfig = DeadLetterConfig()
            self.DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        if params.get("PublicNetConfig") is not None:
            self.PublicNetConfig = PublicNetConfigIn()
            self.PublicNetConfig._deserialize(params.get("PublicNetConfig"))
        if params.get("CfsConfig") is not None:
            self.CfsConfig = CfsConfig()
            self.CfsConfig._deserialize(params.get("CfsConfig"))
        self.InitTimeout = params.get("InitTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionConfigurationResponse(AbstractModel):
    """UpdateFunctionConfiguration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionEventInvokeConfigRequest(AbstractModel):
    """UpdateFunctionEventInvokeConfig request structure.

    """

    def __init__(self):
        """
        :param AsyncTriggerConfig: Async retry configuration information\n        :type AsyncTriggerConfig: :class:`tencentcloud.scf.v20180416.models.AsyncTriggerConfig`\n        :param FunctionName: Function name\n        :type FunctionName: str\n        :param Namespace: Function namespace. Default value: default\n        :type Namespace: str\n        """
        self.AsyncTriggerConfig = None
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        if params.get("AsyncTriggerConfig") is not None:
            self.AsyncTriggerConfig = AsyncTriggerConfig()
            self.AsyncTriggerConfig._deserialize(params.get("AsyncTriggerConfig"))
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateFunctionEventInvokeConfigResponse(AbstractModel):
    """UpdateFunctionEventInvokeConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateNamespaceRequest(AbstractModel):
    """UpdateNamespace request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace name\n        :type Namespace: str\n        :param Description: Namespace description\n        :type Description: str\n        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNamespaceResponse(AbstractModel):
    """UpdateNamespace response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsageInfo(AbstractModel):
    """Usage information

    """

    def __init__(self):
        """
        :param NamespacesCount: Number of namespaces\n        :type NamespacesCount: int\n        :param Namespace: Namespace details\n        :type Namespace: list of NamespaceUsage\n        :param TotalConcurrencyMem: Upper limit of user concurrency memory in the current region\n        :type TotalConcurrencyMem: int\n        :param TotalAllocatedConcurrencyMem: Quota of configured user concurrency memory in the current region\n        :type TotalAllocatedConcurrencyMem: int\n        :param UserConcurrencyMemLimit: Quota of account concurrency actually configured by user\n        :type UserConcurrencyMemLimit: int\n        """
        self.NamespacesCount = None
        self.Namespace = None
        self.TotalConcurrencyMem = None
        self.TotalAllocatedConcurrencyMem = None
        self.UserConcurrencyMemLimit = None


    def _deserialize(self, params):
        self.NamespacesCount = params.get("NamespacesCount")
        if params.get("Namespace") is not None:
            self.Namespace = []
            for item in params.get("Namespace"):
                obj = NamespaceUsage()
                obj._deserialize(item)
                self.Namespace.append(obj)
        self.TotalConcurrencyMem = params.get("TotalConcurrencyMem")
        self.TotalAllocatedConcurrencyMem = params.get("TotalAllocatedConcurrencyMem")
        self.UserConcurrencyMemLimit = params.get("UserConcurrencyMemLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Variable(AbstractModel):
    """Variable parameter

    """

    def __init__(self):
        """
        :param Key: Variable name\n        :type Key: str\n        :param Value: Variable value\n        :type Value: str\n        """
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
        


class VersionMatch(AbstractModel):
    """Function version with match rule

    """

    def __init__(self):
        """
        :param Version: Function version name\n        :type Version: str\n        :param Key: Matching rule key. When the API is called, pass in the `key` to route the request to the specified version based on the matching rule
Header method:
Enter "invoke.headers.User" for `key` and pass in `RoutingKey:{"User":"value"}` when invoking a function through `invoke` for invocation based on rule matching\n        :type Key: str\n        :param Method: Match method. Valid values:
range: range match
exact: exact string match\n        :type Method: str\n        :param Expression: Rule requirements for range match:
It should be described in an open or closed range, i.e., `(a,b)` or `[a,b]`, where both a and b are integers
Rule requirements for exact match:
Exact string match\n        :type Expression: str\n        """
        self.Version = None
        self.Key = None
        self.Method = None
        self.Expression = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Key = params.get("Key")
        self.Method = params.get("Method")
        self.Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionProvisionedConcurrencyInfo(AbstractModel):
    """Provisioned concurrency information of function version, including the set provisioned concurrency amount, available provisioned concurrency amount, and provisioned concurrency setting task status.

    """

    def __init__(self):
        """
        :param AllocatedProvisionedConcurrencyNum: Set provisioned concurrency amount.\n        :type AllocatedProvisionedConcurrencyNum: int\n        :param AvailableProvisionedConcurrencyNum: Currently available provisioned concurrency amount.\n        :type AvailableProvisionedConcurrencyNum: int\n        :param Status: Provisioned concurrency setting task status. `Done`: completed; `InProgress`: in progress; `Failed`: partially or completely failed.\n        :type Status: str\n        :param StatusReason: Status description of provisioned concurrency setting task.\n        :type StatusReason: str\n        :param Qualifier: Function version number\n        :type Qualifier: str\n        """
        self.AllocatedProvisionedConcurrencyNum = None
        self.AvailableProvisionedConcurrencyNum = None
        self.Status = None
        self.StatusReason = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.AllocatedProvisionedConcurrencyNum = params.get("AllocatedProvisionedConcurrencyNum")
        self.AvailableProvisionedConcurrencyNum = params.get("AvailableProvisionedConcurrencyNum")
        self.Status = params.get("Status")
        self.StatusReason = params.get("StatusReason")
        self.Qualifier = params.get("Qualifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionWeight(AbstractModel):
    """Function version with weight

    """

    def __init__(self):
        """
        :param Version: Function version name\n        :type Version: str\n        :param Weight: Version weight\n        :type Weight: float\n        """
        self.Version = None
        self.Weight = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConfig(AbstractModel):
    """VPC parameter configuration

    """

    def __init__(self):
        """
        :param VpcId: VPC ID\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        