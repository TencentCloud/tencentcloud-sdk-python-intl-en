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

from tencentcloud.common.abstract_model import AbstractModel


class AccessInfo(AbstractModel):
    """HTTP domain name-related information

    """

    def __init__(self):
        """
        :param Host: Domain name
        :type Host: str
        :param Vip: VIP
        :type Vip: str
        """
        self.Host = None
        self.Vip = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Vip = params.get("Vip")


class Alias(AbstractModel):
    """Version alias of function

    """

    def __init__(self):
        """
        :param FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param Name: Alias name
        :type Name: str
        :param RoutingConfig: Routing information of alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: Description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddTime: str
        :param ModTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModTime: str
        """
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


class CfsConfig(AbstractModel):
    """File system (CFS) configuration description

    """

    def __init__(self):
        """
        :param CfsInsList: File system information list
        :type CfsInsList: list of CfsInsInfo
        """
        self.CfsInsList = None


    def _deserialize(self, params):
        if params.get("CfsInsList") is not None:
            self.CfsInsList = []
            for item in params.get("CfsInsList"):
                obj = CfsInsInfo()
                obj._deserialize(item)
                self.CfsInsList.append(obj)


class CfsInsInfo(AbstractModel):
    """Configuration information of the CFS instance associated with function

    """

    def __init__(self):
        """
        :param UserId: User ID
        :type UserId: str
        :param UserGroupId: User group ID
        :type UserGroupId: str
        :param CfsId: CFS instance ID
        :type CfsId: str
        :param MountInsId: File system mount target ID
        :type MountInsId: str
        :param LocalMountDir: Local mount target
        :type LocalMountDir: str
        :param RemoteMountDir: Remote mount target
        :type RemoteMountDir: str
        :param IpAddress: File system IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpAddress: str
        :param MountVpcId: VPC ID of file system
Note: this field may return null, indicating that no valid values can be obtained.
        :type MountVpcId: str
        :param MountSubnetId: VPC subnet ID of file system
Note: this field may return null, indicating that no valid values can be obtained.
        :type MountSubnetId: str
        """
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


class Code(AbstractModel):
    """Function code

    """

    def __init__(self):
        """
        :param CosBucketName: COS bucket name
        :type CosBucketName: str
        :param CosObjectName: COS object path
        :type CosObjectName: str
        :param ZipFile: It contains a function code file and its dependencies in the ZIP format. When you use this API, the ZIP file needs to be encoded with Base64. Up to 20 MB is supported.
        :type ZipFile: str
        :param CosBucketRegion: COS region. For Beijing regions, you need to import `ap-beijing`. For Beijing Region 1, you need to input `ap-beijing-1`. For other regions, no import is required.
        :type CosBucketRegion: str
        :param DemoId: `DemoId` is required if Demo is used for the creation.
        :type DemoId: str
        :param TempCosObjectName: `TempCosObjectName` is required if TempCos is used for the creation.
        :type TempCosObjectName: str
        :param GitUrl: Git address
        :type GitUrl: str
        :param GitUserName: Git user name
        :type GitUserName: str
        :param GitPassword: Git password
        :type GitPassword: str
        :param GitPasswordSecret: Git password after encryption. In general, this value is not required.
        :type GitPasswordSecret: str
        :param GitBranch: Git branch
        :type GitBranch: str
        :param GitDirectory: Code path in Git repository
        :type GitDirectory: str
        :param GitCommitId: Version to be pulled
        :type GitCommitId: str
        :param GitUserNameSecret: Git user name after encryption. In general, this value is not required.
        :type GitUserNameSecret: str
        """
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


class CopyFunctionRequest(AbstractModel):
    """CopyFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function to be replicated
        :type FunctionName: str
        :param NewFunctionName: Name of the new function
        :type NewFunctionName: str
        :param Namespace: Namespace of the function to be replicated. The default value is `default`.
        :type Namespace: str
        :param TargetNamespace: Namespace of the replicated function. The default value is default.
        :type TargetNamespace: str
        :param Description: Description of the new function
        :type Description: str
        :param TargetRegion: Region of the target of the function replication. If the value is not set, the current region is used by default.
        :type TargetRegion: str
        :param Override: It specifies whether to replace the function with the same name in the target namespace. The default option is `FALSE`.
(Note: The `TRUE` option results in deletion of the function in the target namespace. Please operate with caution.)
TRUE: Replaces the function.
FALSE: Does not replace the function.
        :type Override: bool
        :param CopyConfiguration: It specifies whether to replicate the function attributes, including environment variables, memory, timeout, function description, labels, and VPC. The default value is `TRUE`.
TRUE: Replicates the function configuration.
FALSE: Does not replicate the function configuration.
        :type CopyConfiguration: bool
        """
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


class CopyFunctionResponse(AbstractModel):
    """CopyFunction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAliasRequest(AbstractModel):
    """CreateAlias request structure.

    """

    def __init__(self):
        """
        :param Name: Alias name, which must be unique in the function, can contain 1 to 64 letters, digits, `_`, and `-`, and must begin with a letter
        :type Name: str
        :param FunctionName: Function name
        :type FunctionName: str
        :param FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param RoutingConfig: Request routing configuration of alias
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: Alias description
        :type Description: str
        """
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


class CreateAliasResponse(AbstractModel):
    """CreateAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFunctionRequest(AbstractModel):
    """CreateFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the new function. The name can contain 2 to 60 characters, including English letters, digits, hyphens (-), and underscores (_). The name must start with a letter and cannot end with a hyphen or underscore.
        :type FunctionName: str
        :param Code: Function code. Note: You cannot specify `Cos` and `ZipFile` at the same time.
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param Handler: Name of the handler, which is in the 'file name.handler name' form. Use periods (.) to separate a file name and function name. The file name and function name must start and end with a letter and can contain 2 to 60 characters, including letters, digits, hyphens (-), and underscores (_).
        :type Handler: str
        :param Description: Function description. It can contain up to 1,000 characters including letters, digits, spaces, commas (,), periods (.), and Chinese characters.
        :type Description: str
        :param MemorySize: Memory size available for function during execution. Default value: 128 MB. Value range: 64 or 128-3072 MB in increments of 128 MB
        :type MemorySize: int
        :param Timeout: Maximum execution duration of function in seconds. Value range: 1-900 seconds. Default value: 3 seconds
        :type Timeout: int
        :param Environment: Function environment variable
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param Runtime: Function runtime environment. Valid values: Python2.7, Python3.6, Nodejs6.10, Nodejs8.9, Nodejs10.15, Nodejs12.16, PHP5, PHP7, Golang1 and Java8. Default value: Python2.7
        :type Runtime: str
        :param VpcConfig: Function VPC configuration
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param Namespace: Function namespace
        :type Namespace: str
        :param Role: Role bound to the function
        :type Role: str
        :param ClsLogsetId: CLS Logset ID to which the function logs are shipped
        :type ClsLogsetId: str
        :param ClsTopicId: CLS Topic ID to which the function logs are shipped
        :type ClsTopicId: str
        :param Type: Function type. The default value is `Event`. Enter `Event` if you need to create a trigger function. Enter `HTTP` if you need to create an HTTP function service.
        :type Type: str
        :param CodeSource: Code source, including ZipFile, Cos, Demo, TempCos, and Git. This field is required if the source is Git.
        :type CodeSource: str
        :param Layers: List of layer versions to be associate with the function. Layers will be overwritten sequentially in the order in the list.
        :type Layers: list of LayerVersionSimple
        :param DeadLetterConfig: Dead letter queue parameter
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param PublicNetConfig: Public network access configuration
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`
        :param CfsConfig: File system configuration parameter, which is used for the function to mount the file system
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        """
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


class CreateFunctionResponse(AbstractModel):
    """CreateFunction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace name
        :type Namespace: str
        :param Description: Namespace description
        :type Description: str
        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function bound to the new trigger
        :type FunctionName: str
        :param TriggerName: Name of a new trigger. For a timer trigger, the name can contain up to 100 letters, digits, dashes, and underscores; for a COS trigger, it should be an access domain name of the corresponding COS bucket applicable to the XML API (e.g., 5401-5ff414-12345.cos.ap-shanghai.myqcloud.com); for other triggers, please see the descriptions of parameters bound to the specific trigger.
        :type TriggerName: str
        :param Type: Trigger type. Currently, COS, CMQ, timer, and ckafka triggers are supported.
        :type Type: str
        :param TriggerDesc: For parameters of triggers, see [Trigger Description](https://cloud.tencent.com/document/product/583/39901)
        :type TriggerDesc: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param Qualifier: Function version
        :type Qualifier: str
        :param Enable: Initial enabling status of the trigger. `OPEN` indicates enabled, and `CLOSE` indicates disabled.
        :type Enable: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Namespace = None
        self.Qualifier = None
        self.Enable = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Namespace = params.get("Namespace")
        self.Qualifier = params.get("Qualifier")
        self.Enable = params.get("Enable")


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger response structure.

    """

    def __init__(self):
        """
        :param TriggerInfo: Trigger information
        :type TriggerInfo: :class:`tencentcloud.scf.v20180416.models.Trigger`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Type: Dead letter queue mode
        :type Type: str
        :param Name: Dead letter queue name
        :type Name: str
        :param FilterType: Tag form of a dead letter queue topic mode
        :type FilterType: str
        """
        self.Type = None
        self.Name = None
        self.FilterType = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.FilterType = params.get("FilterType")


class DeleteAliasRequest(AbstractModel):
    """DeleteAlias request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param Name: Alias name
        :type Name: str
        :param Namespace: Function namespace
        :type Namespace: str
        """
        self.FunctionName = None
        self.Name = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")


class DeleteAliasResponse(AbstractModel):
    """DeleteAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function to be deleted
        :type FunctionName: str
        :param Namespace: Function namespace
        :type Namespace: str
        """
        self.FunctionName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Namespace = params.get("Namespace")


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLayerVersionRequest(AbstractModel):
    """DeleteLayerVersion request structure.

    """

    def __init__(self):
        """
        :param LayerName: Layer name
        :type LayerName: str
        :param LayerVersion: Version number
        :type LayerVersion: int
        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")


class DeleteLayerVersionResponse(AbstractModel):
    """DeleteLayerVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace name
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param TriggerName: Name of the trigger to be deleted
        :type TriggerName: str
        :param Type: Type of the trigger to be deleted. Currently, COS, CMQ, timer, and ckafka triggers are supported.
        :type Type: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param TriggerDesc: This field is required if a COS trigger is to be deleted. It stores the data {"event":"cos:ObjectCreated:*"} in the JSON format. The data content of this field is in the same format as that of SetTrigger. This field is optional if a scheduled trigger or CMQ trigger is to be deleted.
        :type TriggerDesc: str
        :param Qualifier: Function version information
        :type Qualifier: str
        """
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


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EipConfigIn(AbstractModel):
    """Fixed IP configuration for public network access

    """

    def __init__(self):
        """
        :param EipStatus: Status of the EIP. Values: ['ENABLE','DISABLE']
        :type EipStatus: str
        """
        self.EipStatus = None


    def _deserialize(self, params):
        self.EipStatus = params.get("EipStatus")


class EipConfigOut(AbstractModel):
    """Fixed IP configuration for public network access

    """

    def __init__(self):
        """
        :param EipStatus: Whether it is a fixed IP. Valid values: ["ENABLE","DISABLE"]
        :type EipStatus: str
        :param EipAddress: IP list
Note: This field may return null, indicating that no valid values can be obtained.
        :type EipAddress: list of str
        """
        self.EipStatus = None
        self.EipAddress = None


    def _deserialize(self, params):
        self.EipStatus = params.get("EipStatus")
        self.EipAddress = params.get("EipAddress")


class EipOutConfig(AbstractModel):
    """EipOutConfig

    """

    def __init__(self):
        """
        :param EipFixed: It specifies whether the IP is fixed. The value is `TRUE` or `FALSE`.
        :type EipFixed: str
        :param Eips: IP list
        :type Eips: list of str
        """
        self.EipFixed = None
        self.Eips = None


    def _deserialize(self, params):
        self.EipFixed = params.get("EipFixed")
        self.Eips = params.get("Eips")


class Environment(AbstractModel):
    """Environment variable parameter of the function

    """

    def __init__(self):
        """
        :param Variables: Environment variable array
        :type Variables: list of Variable
        """
        self.Variables = None


    def _deserialize(self, params):
        if params.get("Variables") is not None:
            self.Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self.Variables.append(obj)


class Filter(AbstractModel):
    """Key-value pair filters for conditional filtering queries, such as filtering ID, name, and status.
    If more than one filter exists, the logical relationship between these filters is `AND`.
    If multiple values exist in one filter, the logical relationship between these values under the same filter is `OR`.

    """

    def __init__(self):
        """
        :param Name: Fields to be filtered
        :type Name: str
        :param Values: Filter values of the field
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Function(AbstractModel):
    """Function list

    """

    def __init__(self):
        """
        :param ModTime: Modification time
        :type ModTime: str
        :param AddTime: Creation time
        :type AddTime: str
        :param Runtime: Running
        :type Runtime: str
        :param FunctionName: Function name
        :type FunctionName: str
        :param FunctionId: Function ID
        :type FunctionId: str
        :param Namespace: Namespace
        :type Namespace: str
        :param Status: Function status
        :type Status: str
        :param StatusDesc: Function status details
        :type StatusDesc: str
        :param Description: Function description
        :type Description: str
        :param Tags: Function tag
        :type Tags: list of Tag
        :param Type: Function type. The value is `HTTP` or `Event`.
        :type Type: str
        """
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


class FunctionLog(AbstractModel):
    """Log information

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param RetMsg: Return value after the function is executed
        :type RetMsg: str
        :param RequestId: RequestId corresponding to the executed function
        :type RequestId: str
        :param StartTime: Start time of the function execution
        :type StartTime: str
        :param RetCode: Function execution result. `0` indicates successful execution and other values indicate failure.
        :type RetCode: int
        :param InvokeFinished: It specifies whether the function invocation is finished. `1` indicates execution completion and other values indicate that exceptions occurred during the invocation.
        :type InvokeFinished: int
        :param Duration: Duration of the function execution. The unit is millisecond (ms).
        :type Duration: float
        :param BillDuration: Function billing duration. The unit is millisecond (ms). The value is rounded up to a multiple of 100 ms.
        :type BillDuration: int
        :param MemUsage: Actual memory size used during the function execution. The unit is byte.
        :type MemUsage: int
        :param Log: Function execution logs
        :type Log: str
        :param Level: Log level
        :type Level: str
        :param Source: Log source
        :type Source: str
        :param RetryNum: Number of retries
        :type RetryNum: int
        """
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


class FunctionVersion(AbstractModel):
    """Function version information

    """

    def __init__(self):
        """
        :param Version: Function version name
        :type Version: str
        :param Description: Version description
Note: This field may return null, indicating that no valid values is found.
        :type Description: str
        :param AddTime: The creation time
Note: This field may return null, indicating that no valid value was found.
        :type AddTime: str
        :param ModTime: Update time
Note: This field may return null, indicating that no valid value was found.
        :type ModTime: str
        """
        self.Version = None
        self.Description = None
        self.AddTime = None
        self.ModTime = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.ModTime = params.get("ModTime")


class GetAliasRequest(AbstractModel):
    """GetAlias request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param Name: Alias name
        :type Name: str
        :param Namespace: Function namespace
        :type Namespace: str
        """
        self.FunctionName = None
        self.Name = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")


class GetAliasResponse(AbstractModel):
    """GetAlias response structure.

    """

    def __init__(self):
        """
        :param FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param Name: Alias name
        :type Name: str
        :param RoutingConfig: Routing information of alias
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: Alias description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param AddTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type AddTime: str
        :param ModTime: Update time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ModTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param FunctionName: Function name
        :type FunctionName: str
        :param Qualifier: Function version
        :type Qualifier: str
        :param Namespace: Function namespace
        :type Namespace: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")


class GetFunctionAddressResponse(AbstractModel):
    """GetFunctionAddress response structure.

    """

    def __init__(self):
        """
        :param Url: Cos address of the function
        :type Url: str
        :param CodeSha256: SHA256 code of the function
        :type CodeSha256: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Url = None
        self.CodeSha256 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.CodeSha256 = params.get("CodeSha256")
        self.RequestId = params.get("RequestId")


class GetFunctionLogsRequest(AbstractModel):
    """GetFunctionLogs request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param Offset: Data offset. The addition of `Offset` and `Limit` cannot exceed 10,000.
        :type Offset: int
        :param Limit: Length of the return data. The addition of `Offset` and `Limit` cannot exceed 10,000.
        :type Limit: int
        :param Order: It specifies whether to sort the logs in an ascending or descending order. The value is `desc` or `asc`.
        :type Order: str
        :param OrderBy: It specifies the sorting order of the logs based on a specified field, such as `function_name`, `duration`, `mem_usage`, and `start_time`.
        :type OrderBy: str
        :param Filter: Log filter used to identify whether to return logs of successful or failed requests. `filter.RetCode=not0` indicates that only the logs of failed requests will be returned. `filter.RetCode=is0` indicates that only the logs of successful requests will be returned. If this parameter is left blank, all logs will be returned. 
        :type Filter: :class:`tencentcloud.scf.v20180416.models.LogFilter`
        :param Namespace: Function namespace
        :type Namespace: str
        :param Qualifier: Function version
        :type Qualifier: str
        :param FunctionRequestId: RequestId corresponding to the executed function
        :type FunctionRequestId: str
        :param StartTime: Query date, for example, 2017-05-16 20:00:00. The date must be within one day of the end time.
        :type StartTime: str
        :param EndTime: Query date, for example, 2017-05-16 20:59:59. The date must be within one day of the start time.
        :type EndTime: str
        :param SearchContext: Service log related parameter. `Offset` on the first page is a null string. Enter other pages based on SearchContext in the response field.
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        """
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


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of function logs
        :type TotalCount: int
        :param Data: Function log information
        :type Data: list of FunctionLog
        :param SearchContext: Parameter on the log service page
        :type SearchContext: :class:`tencentcloud.scf.v20180416.models.LogSearchContext`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param FunctionName: Name of the function to obtain details
        :type FunctionName: str
        :param Qualifier: Function version number
        :type Qualifier: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param ShowCode: It indicates whether to display the code. `TRUE` means displaying the code, and `FALSE` means hiding the code. The code will not be displayed for entry files exceeding 1 MB.
        :type ShowCode: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.Namespace = None
        self.ShowCode = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.Namespace = params.get("Namespace")
        self.ShowCode = params.get("ShowCode")


class GetFunctionResponse(AbstractModel):
    """GetFunction response structure.

    """

    def __init__(self):
        """
        :param ModTime: Latest modification time of the function
        :type ModTime: str
        :param CodeInfo: Function code
        :type CodeInfo: str
        :param Description: Function description
        :type Description: str
        :param Triggers: Function trigger list
        :type Triggers: list of Trigger
        :param Handler: Function entry
        :type Handler: str
        :param CodeSize: Function code size
        :type CodeSize: int
        :param Timeout: Function timeout
        :type Timeout: int
        :param FunctionVersion: Function version
        :type FunctionVersion: str
        :param MemorySize: Maximum available memory of the function
        :type MemorySize: int
        :param Runtime: Function running environment
        :type Runtime: str
        :param FunctionName: Function name
        :type FunctionName: str
        :param VpcConfig: Function VPC
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param UseGpu: Whether to use GPU
        :type UseGpu: str
        :param Environment: Function environment variable
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param CodeResult: Whether the code is correct
        :type CodeResult: str
        :param CodeError: Code error information
        :type CodeError: str
        :param ErrNo: Error code
        :type ErrNo: int
        :param Namespace: Function namespace
        :type Namespace: str
        :param Role: Role bound to the function
        :type Role: str
        :param InstallDependency: Whether to install dependencies automatically
        :type InstallDependency: str
        :param Status: Function status
        :type Status: str
        :param StatusDesc: Status description
        :type StatusDesc: str
        :param ClsLogsetId: CLS logset to which logs are shipped
        :type ClsLogsetId: str
        :param ClsTopicId: CLS Topic to which logs are shipped
        :type ClsTopicId: str
        :param FunctionId: Function ID
        :type FunctionId: str
        :param Tags: Function tag list
        :type Tags: list of Tag
        :param EipConfig: EipConfig configuration
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipOutConfig`
        :param AccessInfo: Domain name information
        :type AccessInfo: :class:`tencentcloud.scf.v20180416.models.AccessInfo`
        :param Type: Function type. The value is `HTTP` or `Event`.
        :type Type: str
        :param L5Enable: Whether to enable L5
        :type L5Enable: str
        :param Layers: Version information of a layer associated with a function
        :type Layers: list of LayerVersionInfo
        :param DeadLetterConfig: Information of a dead letter queue associated with a function
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param AddTime: Function creation time
        :type AddTime: str
        :param PublicNetConfig: Public network access configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigOut`
        :param OnsEnable: Whether Ons is enabled
Note: This field may return null, indicating that no valid value was found.
        :type OnsEnable: str
        :param CfsConfig: File system configuration parameter, which is used for the function to mount the file system
Note: this field may return null, indicating that no valid values can be obtained.
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        :param AvailableStatus: Function billing status
Note: this field may return null, indicating that no valid values can be obtained.
        :type AvailableStatus: str
        :param Qualifier: Function version
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qualifier: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        self.RequestId = params.get("RequestId")


class GetLayerVersionRequest(AbstractModel):
    """GetLayerVersion request structure.

    """

    def __init__(self):
        """
        :param LayerName: Layer name
        :type LayerName: str
        :param LayerVersion: Version number
        :type LayerVersion: int
        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")


class GetLayerVersionResponse(AbstractModel):
    """GetLayerVersion response structure.

    """

    def __init__(self):
        """
        :param CompatibleRuntimes: Compatible runtimes
        :type CompatibleRuntimes: list of str
        :param CodeSha256: SHA256 encoding of version file on the layer
        :type CodeSha256: str
        :param Location: Download address of version file on the layer
        :type Location: str
        :param AddTime: Version creation time
        :type AddTime: str
        :param Description: Version description
        :type Description: str
        :param LicenseInfo: License information
        :type LicenseInfo: str
        :param LayerVersion: Version number
        :type LayerVersion: int
        :param LayerName: Layer name
        :type LayerName: str
        :param Status: Current status of specific layer version. Valid values:
Active: normal
Publishing: publishing
PublishFailed: publishing failed
Deleted: deleted
        :type Status: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class InvokeRequest(AbstractModel):
    """Invoke request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param InvocationType: The value is `RequestResponse` (synchronous) or `Event` (asynchronous). The default value is synchronous.
        :type InvocationType: str
        :param Qualifier: Version number of the triggered function
        :type Qualifier: str
        :param ClientContext: Function running parameter, which is in the JSON format. Maximum parameter size is 1 MB.
        :type ClientContext: str
        :param LogType: If this field is specified for a synchronous invocation, the return value will contain a 4-KB log. The value is `None` (default) or `Tail`. If the value is `Tail`, `logMsg` in the return parameter will contain the corresponding function execution log.
        :type LogType: str
        :param Namespace: Namespace
        :type Namespace: str
        :param RoutingKey: Traffic routing config in json format, e.g., {"k":"v"}. Please note that both "k" and "v" must be strings. Up to 1024 bytes allowed.
        :type RoutingKey: str
        """
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


class InvokeResponse(AbstractModel):
    """Invoke response structure.

    """

    def __init__(self):
        """
        :param Result: Function execution result
        :type Result: :class:`tencentcloud.scf.v20180416.models.Result`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
Note: This field may return null, indicating that no valid values can be obtained.
        :type CompatibleRuntimes: list of str
        :param AddTime: Creation time
        :type AddTime: str
        :param Description: Version description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param LicenseInfo: License information
Note: This field may return null, indicating that no valid values can be obtained.
        :type LicenseInfo: str
        :param LayerVersion: Version number
        :type LayerVersion: int
        :param LayerName: Layer name
        :type LayerName: str
        :param Status: The status of the layer version. Values can be: 
`Active`: normal
`Publishing`: publishing
`PublishFailed`: failed to publish
`Deleted`: deleted
        :type Status: str
        """
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


class LayerVersionSimple(AbstractModel):
    """Specifies a layer version

    """

    def __init__(self):
        """
        :param LayerName: Layer name
        :type LayerName: str
        :param LayerVersion: Version number
        :type LayerVersion: int
        """
        self.LayerName = None
        self.LayerVersion = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.LayerVersion = params.get("LayerVersion")


class ListAliasesRequest(AbstractModel):
    """ListAliases request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param FunctionVersion: If this parameter is provided, only aliases associated with this function version will be returned.
        :type FunctionVersion: str
        :param Offset: Data offset. Default value: 0
        :type Offset: str
        :param Limit: Number of results to be returned. Default value: 20
        :type Limit: str
        """
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


class ListAliasesResponse(AbstractModel):
    """ListAliases response structure.

    """

    def __init__(self):
        """
        :param Aliases: Alias list
        :type Aliases: list of Alias
        :param TotalCount: Total number of aliases
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class ListFunctionsRequest(AbstractModel):
    """ListFunctions request structure.

    """

    def __init__(self):
        """
        :param Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.
        :type Order: str
        :param Orderby: It specifies the sorting order of the results according to a specified field, such as `AddTime`, `ModTime`, and `FunctionName`.
        :type Orderby: str
        :param Offset: Data offset. The default value is `0`.
        :type Offset: int
        :param Limit: Return data length. The default value is `20`.
        :type Limit: int
        :param SearchKey: It specifies whether to support fuzzy matching for the function name.
        :type SearchKey: str
        :param Namespace: Namespace
        :type Namespace: str
        :param Description: Function description. Fuzzy search is supported.
        :type Description: str
        :param Filters: Filters
- tag:tag-key - String - Required: No - Filtering criteria based on tag-key - value pairs. Replace `tag-key` with a specific tag-key.

The maximum number of `Filters` for each request is 10, and that of `Filter.Values` is 5.
        :type Filters: list of Filter
        """
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


class ListFunctionsResponse(AbstractModel):
    """ListFunctions response structure.

    """

    def __init__(self):
        """
        :param Functions: Function list
        :type Functions: list of Function
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param LayerName: Layer name
        :type LayerName: str
        :param CompatibleRuntime: Compatible runtimes
        :type CompatibleRuntime: list of str
        """
        self.LayerName = None
        self.CompatibleRuntime = None


    def _deserialize(self, params):
        self.LayerName = params.get("LayerName")
        self.CompatibleRuntime = params.get("CompatibleRuntime")


class ListLayerVersionsResponse(AbstractModel):
    """ListLayerVersions response structure.

    """

    def __init__(self):
        """
        :param LayerVersions: Layer version list
        :type LayerVersions: list of LayerVersionInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param CompatibleRuntime: Compatible runtimes
        :type CompatibleRuntime: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        :param SearchKey: Query key, which fuzzily matches the name
        :type SearchKey: str
        """
        self.CompatibleRuntime = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.CompatibleRuntime = params.get("CompatibleRuntime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")


class ListLayersResponse(AbstractModel):
    """ListLayers response structure.

    """

    def __init__(self):
        """
        :param Layers: Layer list
        :type Layers: list of LayerVersionInfo
        :param TotalCount: Total number of layers
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param Limit: Return data length. The default value is `20`.
        :type Limit: int
        :param Offset: Data offset. The default value is `0`.
        :type Offset: int
        :param Orderby: It specifies the sorting order of the results according to a specified field, such as `Name` and `Updatetime`.
        :type Orderby: str
        :param Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.
        :type Order: str
        """
        self.Limit = None
        self.Offset = None
        self.Orderby = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Orderby = params.get("Orderby")
        self.Order = params.get("Order")


class ListNamespacesResponse(AbstractModel):
    """ListNamespaces response structure.

    """

    def __init__(self):
        """
        :param Namespaces: Namespace details
        :type Namespaces: list of Namespace
        :param TotalCount: Number of return namespaces
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param FunctionName: Function name
        :type FunctionName: str
        :param Namespace: Namespace. Default value: default
        :type Namespace: str
        :param Offset: Data offset. Default value: 0
        :type Offset: int
        :param Limit: Number of results to be returned. Default value: 20
        :type Limit: int
        :param OrderBy: Indicates by which field to sort the returned results. Valid values: AddTime, ModTime. Default value: ModTime
        :type OrderBy: str
        :param Order: Indicates whether the returned results are sorted in ascending or descending order. Valid values: ASC, DESC. Default value: DESC
        :type Order: str
        :param Filters: * Qualifier:
Function version, alias
        :type Filters: list of Filter
        """
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


class ListTriggersResponse(AbstractModel):
    """ListTriggers response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of triggers
        :type TotalCount: int
        :param Triggers: Trigger list
        :type Triggers: list of TriggerInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param FunctionName: Function Name
        :type FunctionName: str
        :param Namespace: The namespace where the function locates
        :type Namespace: str
        :param Offset: Data offset. The default value is `0`.
        :type Offset: int
        :param Limit: Return data length. The default value is `20`.
        :type Limit: int
        :param Order: It specifies whether to return the results in ascending or descending order. The value is `ASC` or `DESC`.
        :type Order: str
        :param OrderBy: It specifies the sorting order of the results according to a specified field, such as `AddTime`, `ModTime`.
        :type OrderBy: str
        """
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


class ListVersionByFunctionResponse(AbstractModel):
    """ListVersionByFunction response structure.

    """

    def __init__(self):
        """
        :param FunctionVersion: Function version
        :type FunctionVersion: list of str
        :param Versions: Function version list
Note: This field may return null, indicating that no valid values is found.
        :type Versions: list of FunctionVersion
        :param TotalCount: Total number of function versions
Note: This field may return null, indicating that no valid value was found.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
Blank, indicating that all logs will be returned.
        :type RetCode: str
        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")


class LogSearchContext(AbstractModel):
    """Log search context

    """

    def __init__(self):
        """
        :param Offset: Offset.
        :type Offset: str
        :param Limit: Log record number
        :type Limit: int
        :param Keyword: Log keyword
        :type Keyword: str
        :param Type: Log type. The value is `Application` (default) or `Platform`.
        :type Type: str
        """
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Type = params.get("Type")


class Namespace(AbstractModel):
    """Namespace

    """

    def __init__(self):
        """
        :param ModTime: Creation time of the namespace
        :type ModTime: str
        :param AddTime: Modification time of the namespace
        :type AddTime: str
        :param Description: Namespace description
        :type Description: str
        :param Name: Namespace name
        :type Name: str
        :param Type: The default value is default. TCB indicates that the namespace is developed and created through the mini-program cloud.
        :type Type: str
        """
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


class PublicNetConfigIn(AbstractModel):
    """Public network access configuration

    """

    def __init__(self):
        """
        :param PublicNetStatus: Whether to enable public network access. Valid values: ['DISABLE', 'ENABLE']
        :type PublicNetStatus: str
        :param EipConfig: EIP configuration
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigIn`
        """
        self.PublicNetStatus = None
        self.EipConfig = None


    def _deserialize(self, params):
        self.PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self.EipConfig = EipConfigIn()
            self.EipConfig._deserialize(params.get("EipConfig"))


class PublicNetConfigOut(AbstractModel):
    """Public network access configuration

    """

    def __init__(self):
        """
        :param PublicNetStatus: Whether to enable public network access. Valid values: ['DISABLE', 'ENABLE']
        :type PublicNetStatus: str
        :param EipConfig: EIP configuration
        :type EipConfig: :class:`tencentcloud.scf.v20180416.models.EipConfigOut`
        """
        self.PublicNetStatus = None
        self.EipConfig = None


    def _deserialize(self, params):
        self.PublicNetStatus = params.get("PublicNetStatus")
        if params.get("EipConfig") is not None:
            self.EipConfig = EipConfigOut()
            self.EipConfig._deserialize(params.get("EipConfig"))


class PublishLayerVersionRequest(AbstractModel):
    """PublishLayerVersion request structure.

    """

    def __init__(self):
        """
        :param LayerName: Layer name, which can contain 1-64 English letters, digits, hyphens, and underscores, must begin with a letter, and cannot end with a hyphen or underscore
        :type LayerName: str
        :param CompatibleRuntimes: Runtimes compatible with layer. Multiple choices are allowed. The valid values of this parameter correspond to the valid values of the `Runtime` of the function.
        :type CompatibleRuntimes: list of str
        :param Content: Layer file source or content
        :type Content: :class:`tencentcloud.scf.v20180416.models.Code`
        :param Description: Layer version description
        :type Description: str
        :param LicenseInfo: Software license of layer
        :type LicenseInfo: str
        """
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


class PublishLayerVersionResponse(AbstractModel):
    """PublishLayerVersion response structure.

    """

    def __init__(self):
        """
        :param LayerVersion: Version number of the layer created in this request
        :type LayerVersion: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        :param FunctionName: Name of the released function
        :type FunctionName: str
        :param Description: Function description
        :type Description: str
        :param Namespace: Function namespace
        :type Namespace: str
        """
        self.FunctionName = None
        self.Description = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.Namespace = params.get("Namespace")


class PublishVersionResponse(AbstractModel):
    """PublishVersion response structure.

    """

    def __init__(self):
        """
        :param FunctionVersion: Function version
        :type FunctionVersion: str
        :param CodeSize: Code size
        :type CodeSize: int
        :param MemorySize: Maximum available memory
        :type MemorySize: int
        :param Description: Function description
        :type Description: str
        :param Handler: Function entry
        :type Handler: str
        :param Timeout: Function timeout
        :type Timeout: int
        :param Runtime: Function running environment
        :type Runtime: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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


class Result(AbstractModel):
    """Response of the executed function

    """

    def __init__(self):
        """
        :param Log: It indicates the log output during the function execution. Null is returned for asynchronous invocations.
        :type Log: str
        :param RetMsg: It indicates the response from the executed function. Null is returned for asynchronous invocations.
        :type RetMsg: str
        :param ErrMsg: It indicates the error message of the executed function. Null is returned for asynchronous invocations.
        :type ErrMsg: str
        :param MemUsage: It indicates the memory size (in bytes) when the function is running. Null is returned for asynchronous invocations.
        :type MemUsage: int
        :param Duration: It indicates the duration (in milliseconds) required for running the function. Null is returned for asynchronous invocations.
        :type Duration: float
        :param BillDuration: It indicates the billing duration (in milliseconds) for the function. Null is returned for asynchronous invocations.
        :type BillDuration: int
        :param FunctionRequestId: ID of the executed function
        :type FunctionRequestId: str
        :param InvokeResult: `0` indicates successful execution. Null is returned for asynchronous invocations.
        :type InvokeResult: int
        """
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


class RoutingConfig(AbstractModel):
    """Version routing configuration of alias

    """

    def __init__(self):
        """
        :param AdditionalVersionWeights: Additional version with random weight-based routing
        :type AdditionalVersionWeights: list of VersionWeight
        :param AddtionVersionMatchs: Additional version with rule-based routing
        :type AddtionVersionMatchs: list of VersionMatch
        """
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


class Tag(AbstractModel):
    """Function tag

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


class Trigger(AbstractModel):
    """Trigger type

    """

    def __init__(self):
        """
        :param ModTime: Latest modification time of the trigger
        :type ModTime: str
        :param Type: Trigger type
        :type Type: str
        :param TriggerDesc: Detailed trigger configuration
        :type TriggerDesc: str
        :param TriggerName: Trigger name
        :type TriggerName: str
        :param AddTime: Creation time of the trigger
        :type AddTime: str
        :param Enable: Enabling switch
        :type Enable: int
        :param CustomArgument: Custom parameter
        :type CustomArgument: str
        :param AvailableStatus: Trigger status
        :type AvailableStatus: str
        """
        self.ModTime = None
        self.Type = None
        self.TriggerDesc = None
        self.TriggerName = None
        self.AddTime = None
        self.Enable = None
        self.CustomArgument = None
        self.AvailableStatus = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.TriggerName = params.get("TriggerName")
        self.AddTime = params.get("AddTime")
        self.Enable = params.get("Enable")
        self.CustomArgument = params.get("CustomArgument")
        self.AvailableStatus = params.get("AvailableStatus")


class TriggerInfo(AbstractModel):
    """Trigger information

    """

    def __init__(self):
        """
        :param Enable: Whether to enable
        :type Enable: int
        :param Qualifier: Function version or alias
        :type Qualifier: str
        :param TriggerName: Trigger name
        :type TriggerName: str
        :param Type: Trigger type
        :type Type: str
        :param TriggerDesc: Detailed configuration of trigger
        :type TriggerDesc: str
        :param AvailableStatus: Whether the trigger is available
        :type AvailableStatus: str
        :param CustomArgument: Custom parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type CustomArgument: str
        :param AddTime: Trigger creation time
        :type AddTime: str
        :param ModTime: Trigger last modified time
        :type ModTime: str
        """
        self.Enable = None
        self.Qualifier = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.AvailableStatus = None
        self.CustomArgument = None
        self.AddTime = None
        self.ModTime = None


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


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Function name
        :type FunctionName: str
        :param Name: Alias name
        :type Name: str
        :param FunctionVersion: Master version pointed to by the alias
        :type FunctionVersion: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param RoutingConfig: Routing information of alias, which is required if you need to specify an additional version for the alias.
        :type RoutingConfig: :class:`tencentcloud.scf.v20180416.models.RoutingConfig`
        :param Description: Alias description
        :type Description: str
        """
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


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionCodeRequest(AbstractModel):
    """UpdateFunctionCode request structure.

    """

    def __init__(self):
        """
        :param Handler: Function handler name, which is in the `file name.function name` form. Use a period (.) to separate a file name and function name. The file name and function name must start and end with letters and contain 2-60 characters, including letters, digits, underscores (_), and hyphens (-).
        :type Handler: str
        :param FunctionName: Name of the function to be modified
        :type FunctionName: str
        :param CosBucketName: COS bucket name
        :type CosBucketName: str
        :param CosObjectName: COS object path
        :type CosObjectName: str
        :param ZipFile: It contains a function code file and its dependencies in the ZIP format. When you use this API, the ZIP file needs to be encoded with Base64. Up to 20 MB is supported.
        :type ZipFile: str
        :param Namespace: Function namespace
        :type Namespace: str
        :param CosBucketRegion: COS region. Note: Beijing includes ap-beijing and ap-beijing-1.
        :type CosBucketRegion: str
        :param EnvId: Function environment
        :type EnvId: str
        :param Publish: It specifies whether to synchronously release a new version during the update. The default value is `FALSE`, indicating not to release a new version.
        :type Publish: str
        :param Code: Function code
        :type Code: :class:`tencentcloud.scf.v20180416.models.Code`
        :param CodeSource: Source mode of code. Valid values: `ZipFile`, `Cos`, `Inline`, `TempCos` and `Git`. This field must be specified if the source is Git
        :type CodeSource: str
        """
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


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionConfigurationRequest(AbstractModel):
    """UpdateFunctionConfiguration request structure.

    """

    def __init__(self):
        """
        :param FunctionName: Name of the function to be modified
        :type FunctionName: str
        :param Description: Function description. It can contain up to 1,000 characters, including letters, digits, spaces, commas (,), periods (.), and Chinese characters.
        :type Description: str
        :param MemorySize: Memory size available for function during execution. Default value: 128 MB. Value range: 64 or 128-3,072 MB in increments of 128 MB.
        :type MemorySize: int
        :param Timeout: Maximum execution duration of function in seconds. Value range: 1-900 seconds. Default value: 3 seconds
        :type Timeout: int
        :param Runtime: Function runtime environment. Valid values: Python2.7, Python3.6, Nodejs6.10, Nodejs8.9, Nodejs10.15, Nodejs12.16, PHP5, PHP7, Golang1 and Java8
        :type Runtime: str
        :param Environment: Function environment variable
        :type Environment: :class:`tencentcloud.scf.v20180416.models.Environment`
        :param Namespace: Function namespace
        :type Namespace: str
        :param VpcConfig: Function VPC configuration
        :type VpcConfig: :class:`tencentcloud.scf.v20180416.models.VpcConfig`
        :param Role: Role bound to the function
        :type Role: str
        :param ClsLogsetId: CLS logset ID to which logs are shipped
        :type ClsLogsetId: str
        :param ClsTopicId: CLS Topic ID to which logs are shipped
        :type ClsTopicId: str
        :param Publish: It specifies whether to synchronously release a new version during the update. The default value is `FALSE`, indicating not to release a new version.
        :type Publish: str
        :param L5Enable: Whether to enable L5 access. TRUE: enable; FALSE: not enable
        :type L5Enable: str
        :param Layers: List of layer versions that bound with the function. Files with the same name will be overridden by the bound layer versions according to the ascending order in the list. 
        :type Layers: list of LayerVersionSimple
        :param DeadLetterConfig: Information of a dead letter queue associated with a function
        :type DeadLetterConfig: :class:`tencentcloud.scf.v20180416.models.DeadLetterConfig`
        :param PublicNetConfig: Public network access configuration
        :type PublicNetConfig: :class:`tencentcloud.scf.v20180416.models.PublicNetConfigIn`
        :param CfsConfig: File system configuration input parameter, which is used for the function to bind the file system
        :type CfsConfig: :class:`tencentcloud.scf.v20180416.models.CfsConfig`
        """
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


class UpdateFunctionConfigurationResponse(AbstractModel):
    """UpdateFunctionConfiguration response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateNamespaceRequest(AbstractModel):
    """UpdateNamespace request structure.

    """

    def __init__(self):
        """
        :param Namespace: Namespace name
        :type Namespace: str
        :param Description: Namespace description
        :type Description: str
        """
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")


class UpdateNamespaceResponse(AbstractModel):
    """UpdateNamespace response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Variable(AbstractModel):
    """Variable parameter

    """

    def __init__(self):
        """
        :param Key: Variable name
        :type Key: str
        :param Value: Variable value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class VersionMatch(AbstractModel):
    """Function version with match rule

    """

    def __init__(self):
        """
        :param Version: Function version name
        :type Version: str
        :param Key: Matching rule key. When the API is called, pass in the `key` to route the request to the specified version based on the matching rule
Header method:
Enter "invoke.headers.User" for `key` and pass in `RoutingKey:{"User":"value"}` when invoking a function through `invoke` for invocation based on rule matching
        :type Key: str
        :param Method: Match method. Valid values:
range: range match
exact: exact string match
        :type Method: str
        :param Expression: Rule requirements for range match:
It should be described in an open or closed range, i.e., `(a,b)` or `[a,b]`, where both a and b are integers
Rule requirements for exact match:
Exact string match
        :type Expression: str
        """
        self.Version = None
        self.Key = None
        self.Method = None
        self.Expression = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Key = params.get("Key")
        self.Method = params.get("Method")
        self.Expression = params.get("Expression")


class VersionWeight(AbstractModel):
    """Function version with weight

    """

    def __init__(self):
        """
        :param Version: Function version name
        :type Version: str
        :param Weight: Version weight
        :type Weight: float
        """
        self.Version = None
        self.Weight = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Weight = params.get("Weight")


class VpcConfig(AbstractModel):
    """VPC parameter configuration

    """

    def __init__(self):
        """
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")