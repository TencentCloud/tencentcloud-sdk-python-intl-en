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


class Autoscaler(AbstractModel):
    """Scaling rule

    """

    def __init__(self):
        r"""
        :param MinReplicas: Minimum number of instances in a scaling group
        :type MinReplicas: int
        :param MaxReplicas: Maximum number of instances in a scaling group
        :type MaxReplicas: int
        :param HorizontalAutoscaler: Policy of the scaling rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param CronHorizontalAutoscaler: Scheduled auto-scaler policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param AutoscalerId: Scaling rule ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutoscalerId: str
        :param AutoscalerName: Scaling rule name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutoscalerName: str
        :param Description: Description of the scaling rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param CreateDate: Creation time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param ModifyDate: Modification time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ModifyDate: str
        :param EnableDate: Start Time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableDate: str
        :param Enabled: Whether it is enabled
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self.MinReplicas = None
        self.MaxReplicas = None
        self.HorizontalAutoscaler = None
        self.CronHorizontalAutoscaler = None
        self.AutoscalerId = None
        self.AutoscalerName = None
        self.Description = None
        self.CreateDate = None
        self.ModifyDate = None
        self.EnableDate = None
        self.Enabled = None


    def _deserialize(self, params):
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        if params.get("HorizontalAutoscaler") is not None:
            self.HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self.HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self.CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self.CronHorizontalAutoscaler.append(obj)
        self.AutoscalerId = params.get("AutoscalerId")
        self.AutoscalerName = params.get("AutoscalerName")
        self.Description = params.get("Description")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.EnableDate = params.get("EnableDate")
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigData(AbstractModel):
    """Configuration

    """

    def __init__(self):
        r"""
        :param Name: Configuration name
        :type Name: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param RelatedApplications: List of associated applications
        :type RelatedApplications: list of TemService
        :param Data: Configuration item
        :type Data: list of Pair
        """
        self.Name = None
        self.CreateTime = None
        self.RelatedApplications = None
        self.Data = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        if params.get("RelatedApplications") is not None:
            self.RelatedApplications = []
            for item in params.get("RelatedApplications"):
                obj = TemService()
                obj._deserialize(item)
                self.RelatedApplications.append(obj)
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosToken(AbstractModel):
    """Cos token

    """

    def __init__(self):
        r"""
        :param RequestId: Unique request ID
        :type RequestId: str
        :param Bucket: Bucket name
        :type Bucket: str
        :param Region: Bucket region
        :type Region: str
        :param TmpSecretId: Temporary key SecretId
        :type TmpSecretId: str
        :param TmpSecretKey: Temporary key SecretKey
        :type TmpSecretKey: str
        :param SessionToken: `sessionToken` of temporary key
        :type SessionToken: str
        :param StartTime: Start time of temporary key acquisition
        :type StartTime: str
        :param ExpiredTime: `ExpiredTime` of temporary key
        :type ExpiredTime: str
        :param FullPath: Full package path
        :type FullPath: str
        """
        self.RequestId = None
        self.Bucket = None
        self.Region = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.SessionToken = None
        self.StartTime = None
        self.ExpiredTime = None
        self.FullPath = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.SessionToken = params.get("SessionToken")
        self.StartTime = params.get("StartTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.FullPath = params.get("FullPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAutoscalerRequest(AbstractModel):
    """CreateApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param Autoscaler: Auto scaling rule
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.Autoscaler = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Autoscaler") is not None:
            self.Autoscaler = Autoscaler()
            self.Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAutoscalerResponse(AbstractModel):
    """CreateApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param Result: Scaling rule ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateApplicationRequest(AbstractModel):
    """CreateApplication request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationName: Application name
        :type ApplicationName: str
        :param Description: Description
        :type Description: str
        :param UseDefaultImageService: Whether to use the default image service. `1`: yes; `0`: no
        :type UseDefaultImageService: int
        :param RepoType: Type of the bound repository. `0`: TCR Personal; `1`: TCR Enterprise
        :type RepoType: int
        :param InstanceId: TCR Enterprise instance ID
        :type InstanceId: str
        :param RepoServer: Address of the bound image server
        :type RepoServer: str
        :param RepoName: Name of the bound image repository
        :type RepoName: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param SubnetList: Application subnet
        :type SubnetList: list of str
        :param CodingLanguage: Programming language 
- JAVA
- OTHER
        :type CodingLanguage: str
        :param DeployMode: Deployment mode 
- IMAGE
- JAR
- WAR
        :type DeployMode: str
        :param EnableTracing: Whether to enable APM tracing for the Java application. `1`: Enable, `0`: Disable
        :type EnableTracing: int
        :param UseDefaultImageServiceParameters: Parameters of the default image service
        :type UseDefaultImageServiceParameters: :class:`tencentcloud.tem.v20210701.models.UseDefaultRepoParameters`
        :param Tags: Tag
        :type Tags: list of Tag
        """
        self.ApplicationName = None
        self.Description = None
        self.UseDefaultImageService = None
        self.RepoType = None
        self.InstanceId = None
        self.RepoServer = None
        self.RepoName = None
        self.SourceChannel = None
        self.SubnetList = None
        self.CodingLanguage = None
        self.DeployMode = None
        self.EnableTracing = None
        self.UseDefaultImageServiceParameters = None
        self.Tags = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.Description = params.get("Description")
        self.UseDefaultImageService = params.get("UseDefaultImageService")
        self.RepoType = params.get("RepoType")
        self.InstanceId = params.get("InstanceId")
        self.RepoServer = params.get("RepoServer")
        self.RepoName = params.get("RepoName")
        self.SourceChannel = params.get("SourceChannel")
        self.SubnetList = params.get("SubnetList")
        self.CodingLanguage = params.get("CodingLanguage")
        self.DeployMode = params.get("DeployMode")
        self.EnableTracing = params.get("EnableTracing")
        if params.get("UseDefaultImageServiceParameters") is not None:
            self.UseDefaultImageServiceParameters = UseDefaultRepoParameters()
            self.UseDefaultImageServiceParameters._deserialize(params.get("UseDefaultImageServiceParameters"))
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
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication response structure.

    """

    def __init__(self):
        r"""
        :param Result: ID of the created application
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateApplicationServiceRequest(AbstractModel):
    """CreateApplicationService request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param Service: Details of the access policy
        :type Service: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.Service = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self.Service = ServicePortMapping()
            self.Service._deserialize(params.get("Service"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationServiceResponse(AbstractModel):
    """CreateApplicationService response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateConfigDataRequest(AbstractModel):
    """CreateConfigData request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param Data: Configuration information
        :type Data: list of Pair
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None
        self.Data = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigDataResponse(AbstractModel):
    """CreateConfigData response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the creation is successful
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateCosTokenRequest(AbstractModel):
    """CreateCosToken request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param PkgName: Package name
        :type PkgName: str
        :param OptType: Operation type. 1: upload; 2: query
        :type OptType: int
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param TimeVersion: Input parameter of `deployVersion`
        :type TimeVersion: str
        """
        self.ApplicationId = None
        self.PkgName = None
        self.OptType = None
        self.SourceChannel = None
        self.TimeVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgName = params.get("PkgName")
        self.OptType = params.get("OptType")
        self.SourceChannel = params.get("SourceChannel")
        self.TimeVersion = params.get("TimeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenResponse(AbstractModel):
    """CreateCosToken response structure.

    """

    def __init__(self):
        r"""
        :param Result: `CosToken` object in case of success and `null` in case of failure
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.tem.v20210701.models.CosToken`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosToken()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentName: Environment name
        :type EnvironmentName: str
        :param Vpc: VPC name
        :type Vpc: str
        :param SubnetIds: List of subnets
        :type SubnetIds: list of str
        :param Description: Environment description
        :type Description: str
        :param K8sVersion: Kubernetes version
        :type K8sVersion: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param EnableTswTraceService: Whether to enable the TSW service
        :type EnableTswTraceService: bool
        :param Tags: Tag
        :type Tags: list of Tag
        :param EnvType: Environment type. Values: `test`, `pre`, `prod`
        :type EnvType: str
        :param CreateRegion: The region to create the environment
        :type CreateRegion: str
        """
        self.EnvironmentName = None
        self.Vpc = None
        self.SubnetIds = None
        self.Description = None
        self.K8sVersion = None
        self.SourceChannel = None
        self.EnableTswTraceService = None
        self.Tags = None
        self.EnvType = None
        self.CreateRegion = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.Description = params.get("Description")
        self.K8sVersion = params.get("K8sVersion")
        self.SourceChannel = params.get("SourceChannel")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.EnvType = params.get("EnvType")
        self.CreateRegion = params.get("CreateRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param Result: Environment ID in case of success and `null` in case of failure
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateLogConfigRequest(AbstractModel):
    """CreateLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param InputType: Collection type. Values: `container_stdout` (standard); `container_file` (file)
        :type InputType: str
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param LogType: Log withdrawal mode. Values: `minimalist_log` (full text in a single line); `multiline_log` (full text in multiple lines); `json_log` (JSON); `fullregex_log` (regex in a single line); `multiline_fullregex_log` (regex in multiple lines)
        :type LogType: str
        :param BeginningRegex: The first line regex. It’s valid when `LogType` is `multiline_log`.
        :type BeginningRegex: str
        :param LogPath: Directory of files to collect. It’s valid when `InputType` is `container_file`.
        :type LogPath: str
        :param FilePattern: Name pattern of files to collect. It’s valid when `InputType` is `container_file`.
        :type FilePattern: str
        :param ExtractRule: Export
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self.EnvironmentId = None
        self.Name = None
        self.InputType = None
        self.ApplicationId = None
        self.LogsetId = None
        self.TopicId = None
        self.LogType = None
        self.BeginningRegex = None
        self.LogPath = None
        self.FilePattern = None
        self.ExtractRule = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.InputType = params.get("InputType")
        self.ApplicationId = params.get("ApplicationId")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.LogType = params.get("LogType")
        self.BeginningRegex = params.get("BeginningRegex")
        self.LogPath = params.get("LogPath")
        self.FilePattern = params.get("FilePattern")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = LogConfigExtractRule()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogConfigResponse(AbstractModel):
    """CreateLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the creation is successful
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    """CreateResource request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ResourceType: Resource type. Valid values: `CFS` (file system), `CLS` (log service), `TSE_SRE` (registry)
        :type ResourceType: str
        :param ResourceId: Resource ID
        :type ResourceId: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param ResourceFrom: Source of the resource. Values: `existing` (choose an existing resource), `creating` (create a new resource)
        :type ResourceFrom: str
        :param ResourceConfig: Resource extra configuration
        :type ResourceConfig: str
        """
        self.EnvironmentId = None
        self.ResourceType = None
        self.ResourceId = None
        self.SourceChannel = None
        self.ResourceFrom = None
        self.ResourceConfig = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.SourceChannel = params.get("SourceChannel")
        self.ResourceFrom = params.get("ResourceFrom")
        self.ResourceConfig = params.get("ResourceConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    """CreateResource response structure.

    """

    def __init__(self):
        r"""
        :param Result: Result
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CronHorizontalAutoscaler(AbstractModel):
    """Scheduled Scaling Policy

    """

    def __init__(self):
        r"""
        :param Name: Name of a scheduled scaling policy
        :type Name: str
        :param Period: Policy period
"* * *" indicates three ranges. The first is day, the second month, and the third week. The three parts are separated by spaces.
Examples:
* * * (every day)
* * 0-3 (every Sunday through Wednesday)
1,11,21 * * (1st, 11th, and 21st of every month)
        :type Period: str
        :param Schedules: Details of a scheduled scaling policy
        :type Schedules: list of CronHorizontalAutoscalerSchedule
        :param Enabled: Enabled or not
        :type Enabled: bool
        :param Priority: Policy priority. The higher the value, the higher the priority. The minimum value is 0.
        :type Priority: int
        """
        self.Name = None
        self.Period = None
        self.Schedules = None
        self.Enabled = None
        self.Priority = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Period = params.get("Period")
        if params.get("Schedules") is not None:
            self.Schedules = []
            for item in params.get("Schedules"):
                obj = CronHorizontalAutoscalerSchedule()
                obj._deserialize(item)
                self.Schedules.append(obj)
        self.Enabled = params.get("Enabled")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronHorizontalAutoscalerSchedule(AbstractModel):
    """Details of a scheduled scaling policy

    """

    def __init__(self):
        r"""
        :param StartAt: Triggering time, in the format of HH:MM
Example:
00:00 (Trigger at midnight)
        :type StartAt: str
        :param TargetReplicas: Number of target pods (less than 50)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetReplicas: int
        """
        self.StartAt = None
        self.TargetReplicas = None


    def _deserialize(self, params):
        self.StartAt = params.get("StartAt")
        self.TargetReplicas = params.get("TargetReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerRequest(AbstractModel):
    """DeleteApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerResponse(AbstractModel):
    """DeleteApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the action is successful
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApplicationRequest(AbstractModel):
    """DeleteApplication request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID.
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param DeleteApplicationIfNoRunningVersion: Whether to delete this application automatically when there is no running version.
        :type DeleteApplicationIfNoRunningVersion: bool
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.DeleteApplicationIfNoRunningVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.DeleteApplicationIfNoRunningVersion = params.get("DeleteApplicationIfNoRunningVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationResponse(AbstractModel):
    """DeleteApplication response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApplicationServiceRequest(AbstractModel):
    """DeleteApplicationService request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ServiceName: Service name
        :type ServiceName: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationServiceResponse(AbstractModel):
    """DeleteApplicationService response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteIngressRequest(AbstractModel):
    """DeleteIngress request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param IngressName: Ingress rule name
        :type IngressName: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.IngressName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.IngressName = params.get("IngressName")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIngressResponse(AbstractModel):
    """DeleteIngress response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether deletion is successful
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployApplicationRequest(AbstractModel):
    """DeployApplication request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param InitPodNum: Number of initialized pods
        :type InitPodNum: int
        :param CpuSpec: CPU specification
        :type CpuSpec: float
        :param MemorySpec: Memory specification
        :type MemorySpec: float
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ImgRepo: Image repository
        :type ImgRepo: str
        :param VersionDesc: Version description
        :type VersionDesc: str
        :param JvmOpts: Launch parameters
        :type JvmOpts: str
        :param EsInfo: Auto scaling configuration (This field is disused. Please use `HorizontalAutoscaler` to set the auto scaling policy.)
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
        :param EnvConf: Environment variable configuration
        :type EnvConf: list of Pair
        :param LogConfs: Log configuration
        :type LogConfs: list of str
        :param StorageConfs: Data volume configuration
        :type StorageConfs: list of StorageConf
        :param StorageMountConfs: Data volume mount configuration
        :type StorageMountConfs: list of StorageMountConf
        :param DeployMode: Deployment type
- JAR: deployment through JAR package
- WAR: deployment through WAR package
- IMAGE: deployment through image
        :type DeployMode: str
        :param DeployVersion: When the deployment type is `IMAGE`, this parameter indicates the image tag
When the deployment type is `JAR` or `WAR`, this parameter indicates the package version number
        :type DeployVersion: str
        :param PkgName: Package name, which is required when using JAR or WAR packages for deployment
        :type PkgName: str
        :param JdkVersion: JDK version
- KONA: use KONA JDK
- OPEN: use open JDK
- KONA: use KONA JDK
- OPEN: use open JDK
        :type JdkVersion: str
        :param SecurityGroupIds: Security group IDs
        :type SecurityGroupIds: list of str
        :param LogOutputConf: Log output configuration
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param Description: Version description
        :type Description: str
        :param ImageCommand: Image command
        :type ImageCommand: str
        :param ImageArgs: Image command parameters
        :type ImageArgs: list of str
        :param UseRegistryDefaultConfig: Whether to add the registry's default configurations
        :type UseRegistryDefaultConfig: bool
        :param SettingConfs: Mounting configurations
        :type SettingConfs: list of MountedSettingConf
        :param Service: Application access configuration
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param VersionId: ID of the version that you want to roll back to
        :type VersionId: str
        :param PostStart: The script to run after startup
        :type PostStart: str
        :param PreStop: The script to run before stop
        :type PreStop: str
        :param Liveness: Configuration of aliveness probe
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param Readiness: Configuration of readiness probe
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param DeployStrategyConf: Configuration of batch release policies
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param HorizontalAutoscaler: Auto scaling policy. (Disused. Please use APIs for auto scaling policy combinations)
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param CronHorizontalAutoscaler: Scheduled scaling policy (Disused. Please use APIs for auto scaling policy combinations)
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param LogEnable: Specifies whether to enable logging. `1`: enable; `0`: do not enable
        :type LogEnable: int
        :param ConfEdited: Whether the configuration is modified (except for the image configuration)
        :type ConfEdited: bool
        :param SpeedUp: Whether the application acceleration is enabled 
        :type SpeedUp: bool
        :param StartupProbe: Whether to enable probing
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param OsFlavour: The version of the operating system
If `openjdk` is selected, the value can be: 
- ALPINE
- CENTOS
If `konajdk` is selected, the value can be: 
- ALPINE
- TENCENTOS
        :type OsFlavour: str
        :param EnablePrometheusConf: Configuration of metrics of this application
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param EnableTracing: `1`: Automatically enable APM tracing (Skywalking)
`0`: Disable APM tracing
        :type EnableTracing: int
        :param EnableMetrics: `1`: Automatically enable metrics collection (open-telemetry)
`0`: Disable metrics collection
        :type EnableMetrics: int
        :param TcrInstanceId: ID of the TCR instance used for image deployment
        :type TcrInstanceId: str
        :param RepoServer: Image server address for image deployment
        :type RepoServer: str
        :param RepoType: Type of the repository. `0`: TCR Personal; `1`: TCR Enterprise; `2`: Public repository; `3`: TEM hosted repository; `4`: Demo repository
        :type RepoType: int
        """
        self.ApplicationId = None
        self.InitPodNum = None
        self.CpuSpec = None
        self.MemorySpec = None
        self.EnvironmentId = None
        self.ImgRepo = None
        self.VersionDesc = None
        self.JvmOpts = None
        self.EsInfo = None
        self.EnvConf = None
        self.LogConfs = None
        self.StorageConfs = None
        self.StorageMountConfs = None
        self.DeployMode = None
        self.DeployVersion = None
        self.PkgName = None
        self.JdkVersion = None
        self.SecurityGroupIds = None
        self.LogOutputConf = None
        self.SourceChannel = None
        self.Description = None
        self.ImageCommand = None
        self.ImageArgs = None
        self.UseRegistryDefaultConfig = None
        self.SettingConfs = None
        self.Service = None
        self.VersionId = None
        self.PostStart = None
        self.PreStop = None
        self.Liveness = None
        self.Readiness = None
        self.DeployStrategyConf = None
        self.HorizontalAutoscaler = None
        self.CronHorizontalAutoscaler = None
        self.LogEnable = None
        self.ConfEdited = None
        self.SpeedUp = None
        self.StartupProbe = None
        self.OsFlavour = None
        self.EnablePrometheusConf = None
        self.EnableTracing = None
        self.EnableMetrics = None
        self.TcrInstanceId = None
        self.RepoServer = None
        self.RepoType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.InitPodNum = params.get("InitPodNum")
        self.CpuSpec = params.get("CpuSpec")
        self.MemorySpec = params.get("MemorySpec")
        self.EnvironmentId = params.get("EnvironmentId")
        self.ImgRepo = params.get("ImgRepo")
        self.VersionDesc = params.get("VersionDesc")
        self.JvmOpts = params.get("JvmOpts")
        if params.get("EsInfo") is not None:
            self.EsInfo = EsInfo()
            self.EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self.EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self.EnvConf.append(obj)
        self.LogConfs = params.get("LogConfs")
        if params.get("StorageConfs") is not None:
            self.StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self.StorageConfs.append(obj)
        if params.get("StorageMountConfs") is not None:
            self.StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self.StorageMountConfs.append(obj)
        self.DeployMode = params.get("DeployMode")
        self.DeployVersion = params.get("DeployVersion")
        self.PkgName = params.get("PkgName")
        self.JdkVersion = params.get("JdkVersion")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LogOutputConf") is not None:
            self.LogOutputConf = LogOutputConf()
            self.LogOutputConf._deserialize(params.get("LogOutputConf"))
        self.SourceChannel = params.get("SourceChannel")
        self.Description = params.get("Description")
        self.ImageCommand = params.get("ImageCommand")
        self.ImageArgs = params.get("ImageArgs")
        self.UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self.SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self.SettingConfs.append(obj)
        if params.get("Service") is not None:
            self.Service = EksService()
            self.Service._deserialize(params.get("Service"))
        self.VersionId = params.get("VersionId")
        self.PostStart = params.get("PostStart")
        self.PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self.Liveness = HealthCheckConfig()
            self.Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self.Readiness = HealthCheckConfig()
            self.Readiness._deserialize(params.get("Readiness"))
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("HorizontalAutoscaler") is not None:
            self.HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self.HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self.CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self.CronHorizontalAutoscaler.append(obj)
        self.LogEnable = params.get("LogEnable")
        self.ConfEdited = params.get("ConfEdited")
        self.SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self.StartupProbe = HealthCheckConfig()
            self.StartupProbe._deserialize(params.get("StartupProbe"))
        self.OsFlavour = params.get("OsFlavour")
        if params.get("EnablePrometheusConf") is not None:
            self.EnablePrometheusConf = EnablePrometheusConf()
            self.EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self.EnableTracing = params.get("EnableTracing")
        self.EnableMetrics = params.get("EnableMetrics")
        self.TcrInstanceId = params.get("TcrInstanceId")
        self.RepoServer = params.get("RepoServer")
        self.RepoType = params.get("RepoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployApplicationResponse(AbstractModel):
    """DeployApplication response structure.

    """

    def __init__(self):
        r"""
        :param Result: Version ID (which can be ignored for the frontend)
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployStrategyConf(AbstractModel):
    """Configuration of batch release policies

    """

    def __init__(self):
        r"""
        :param TotalBatchCount: Total batches
        :type TotalBatchCount: int
        :param BetaBatchNum: Number of pods for the beta batch
        :type BetaBatchNum: int
        :param DeployStrategyType: Batch deployment policy. `0`: automatically; `1`: manually; `2`: beta batch (manual), `3`: initial release
        :type DeployStrategyType: int
        :param BatchInterval: Interval between batches
        :type BatchInterval: int
        :param MinAvailable: The minimum number of available pods
        :type MinAvailable: int
        :param Force: Whether to enable force release
        :type Force: bool
        """
        self.TotalBatchCount = None
        self.BetaBatchNum = None
        self.DeployStrategyType = None
        self.BatchInterval = None
        self.MinAvailable = None
        self.Force = None


    def _deserialize(self, params):
        self.TotalBatchCount = params.get("TotalBatchCount")
        self.BetaBatchNum = params.get("BetaBatchNum")
        self.DeployStrategyType = params.get("DeployStrategyType")
        self.BatchInterval = params.get("BatchInterval")
        self.MinAvailable = params.get("MinAvailable")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListRequest(AbstractModel):
    """DescribeApplicationAutoscalerList request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListResponse(AbstractModel):
    """DescribeApplicationAutoscalerList response structure.

    """

    def __init__(self):
        r"""
        :param Result: Scaling rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: list of Autoscaler
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Autoscaler()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeApplicationInfoRequest(AbstractModel):
    """DescribeApplicationInfo request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationInfoResponse(AbstractModel):
    """DescribeApplicationInfo response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result.
        :type Result: :class:`tencentcloud.tem.v20210701.models.TemServiceVersionInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TemServiceVersionInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationPodsRequest(AbstractModel):
    """DescribeApplicationPods request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param Limit: Number of items per page. Default value: 20
        :type Limit: int
        :param Offset: Page number. Default value: 0
        :type Offset: int
        :param Status: Pod status 
- Running 
- Pending 
- Error
        :type Status: str
        :param PodName: Pod name
        :type PodName: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ApplicationId = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.PodName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.PodName = params.get("PodName")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationPodsResponse(AbstractModel):
    """DescribeApplicationPods response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeRunPodPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationServiceListRequest(AbstractModel):
    """DescribeApplicationServiceList request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: ID of the environment
        :type EnvironmentId: str
        :param ApplicationId: ID of the application
        :type ApplicationId: str
        :param SourceChannel: xx
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ApplicationId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationServiceListResponse(AbstractModel):
    """DescribeApplicationServiceList response structure.

    """

    def __init__(self):
        r"""
        :param Result: Application EKS service list
        :type Result: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = EksService()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: ID of the environment
        :type EnvironmentId: str
        :param Limit: Pagination limit
        :type Limit: int
        :param Offset: Pagination offset
        :type Offset: int
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param Keyword: Keyword for searching.
        :type Keyword: str
        :param Filters: Filters for query 
        :type Filters: list of QueryFilter
        :param SortInfo: Sorting field
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        """
        self.EnvironmentId = None
        self.Limit = None
        self.Offset = None
        self.SourceChannel = None
        self.ApplicationId = None
        self.Keyword = None
        self.Filters = None
        self.SortInfo = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceChannel = params.get("SourceChannel")
        self.ApplicationId = params.get("ApplicationId")
        self.Keyword = params.get("Keyword")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("SortInfo") is not None:
            self.SortInfo = SortType()
            self.SortInfo._deserialize(params.get("SortInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result.
        :type Result: :class:`tencentcloud.tem.v20210701.models.ServicePage`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServicePage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationsStatusRequest(AbstractModel):
    """DescribeApplicationsStatus request structure.

    """

    def __init__(self):
        r"""
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsStatusResponse(AbstractModel):
    """DescribeApplicationsStatus response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result.
        :type Result: list of ServiceVersionBrief
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConfigDataListPage(AbstractModel):
    """Query the list of configurations

    """

    def __init__(self):
        r"""
        :param Records: Record
        :type Records: list of ConfigData
        :param ContinueToken: Paging cursor
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ContinueToken: str
        :param RemainingCount: Remaining number
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RemainingCount: int
        """
        self.Records = None
        self.ContinueToken = None
        self.RemainingCount = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = ConfigData()
                obj._deserialize(item)
                self.Records.append(obj)
        self.ContinueToken = params.get("ContinueToken")
        self.RemainingCount = params.get("RemainingCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListRequest(AbstractModel):
    """DescribeConfigDataList request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param ContinueToken: Paging cursor
        :type ContinueToken: str
        :param Limit: Pagination limit
        :type Limit: int
        """
        self.EnvironmentId = None
        self.SourceChannel = None
        self.ContinueToken = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.ContinueToken = params.get("ContinueToken")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListResponse(AbstractModel):
    """DescribeConfigDataList response structure.

    """

    def __init__(self):
        r"""
        :param Result: Configuration list.
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListPage`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeConfigDataListPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigDataRequest(AbstractModel):
    """DescribeConfigData request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataResponse(AbstractModel):
    """DescribeConfigData response structure.

    """

    def __init__(self):
        r"""
        :param Result: Configuration
        :type Result: :class:`tencentcloud.tem.v20210701.models.ConfigData`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConfigData()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentRequest(AbstractModel):
    """DescribeEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Namespace ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentResponse(AbstractModel):
    """DescribeEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param Result: Environment information
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespaceInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = NamespaceInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentStatusRequest(AbstractModel):
    """DescribeEnvironmentStatus request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentIds: ID of the environment
        :type EnvironmentIds: list of str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.EnvironmentIds = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentStatusResponse(AbstractModel):
    """DescribeEnvironmentStatus response structure.

    """

    def __init__(self):
        r"""
        :param Result: List of environment status
        :type Result: list of NamespaceStatusInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = NamespaceStatusInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Pagination limit
        :type Limit: int
        :param Offset: Page offset
        :type Offset: int
        :param SourceChannel: Source
        :type SourceChannel: int
        :param Filters: Filters for query 
        :type Filters: list of QueryFilter
        :param SortInfo: Sorting field
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self.Limit = None
        self.Offset = None
        self.SourceChannel = None
        self.Filters = None
        self.SortInfo = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("SortInfo") is not None:
            self.SortInfo = SortType()
            self.SortInfo._deserialize(params.get("SortInfo"))
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespacePage`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = NamespacePage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param IngressName: Ingress rule name
        :type IngressName: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.IngressName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.IngressName = params.get("IngressName")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressResponse(AbstractModel):
    """DescribeIngress response structure.

    """

    def __init__(self):
        r"""
        :param Result: Ingress rule configuration
        :type Result: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IngressInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIngressesRequest(AbstractModel):
    """DescribeIngresses request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param IngressNames: Ingress rule name list
        :type IngressNames: list of str
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.SourceChannel = None
        self.IngressNames = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.IngressNames = params.get("IngressNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressesResponse(AbstractModel):
    """DescribeIngresses response structure.

    """

    def __init__(self):
        r"""
        :param Result: Ingress array
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: list of IngressInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogConfigRequest(AbstractModel):
    """DescribeLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param ApplicationId: Application ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.Name = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogConfigResponse(AbstractModel):
    """DescribeLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param Result: Configuration
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = LogConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePagedLogConfigListRequest(AbstractModel):
    """DescribePagedLogConfigList request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param ApplicationName: Application name
        :type ApplicationName: str
        :param Name: Name of the rule
        :type Name: str
        :param Limit: Number of entries per page. Default value: 20
        :type Limit: int
        :param ContinueToken: Paging cursor
        :type ContinueToken: str
        """
        self.EnvironmentId = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.Name = None
        self.Limit = None
        self.ContinueToken = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.Name = params.get("Name")
        self.Limit = params.get("Limit")
        self.ContinueToken = params.get("ContinueToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePagedLogConfigListResponse(AbstractModel):
    """DescribePagedLogConfigList response structure.

    """

    def __init__(self):
        r"""
        :param Result: List of log collecting configurations
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfigListPage`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = LogConfigListPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRelatedIngressesRequest(AbstractModel):
    """DescribeRelatedIngresses request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param ApplicationId: Application ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.SourceChannel = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelatedIngressesResponse(AbstractModel):
    """DescribeRelatedIngresses response structure.

    """

    def __init__(self):
        r"""
        :param Result: Ingress array
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: list of IngressInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRunPodPage(AbstractModel):
    """Version pod list

    """

    def __init__(self):
        r"""
        :param Offset: Page offset
        :type Offset: int
        :param Limit: Number of records per page
        :type Limit: int
        :param TotalCount: Total number of returned records
        :type TotalCount: int
        :param RequestId: Request ID
        :type RequestId: str
        :param PodList: List of pods
        :type PodList: list of RunVersionPod
        """
        self.Offset = None
        self.Limit = None
        self.TotalCount = None
        self.RequestId = None
        self.PodList = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        if params.get("PodList") is not None:
            self.PodList = []
            for item in params.get("PodList"):
                obj = RunVersionPod()
                obj._deserialize(item)
                self.PodList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyConfigDataRequest(AbstractModel):
    """DestroyConfigData request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyConfigDataResponse(AbstractModel):
    """DestroyConfigData response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DestroyEnvironmentRequest(AbstractModel):
    """DestroyEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Namespace ID.
        :type EnvironmentId: str
        :param SourceChannel: Namespace
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyEnvironmentResponse(AbstractModel):
    """DestroyEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DestroyLogConfigRequest(AbstractModel):
    """DestroyLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param ApplicationId: Application ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.Name = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyLogConfigResponse(AbstractModel):
    """DestroyLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableApplicationAutoscalerRequest(AbstractModel):
    """DisableApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApplicationAutoscalerResponse(AbstractModel):
    """DisableApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EksService(AbstractModel):
    """EKS service information

    """

    def __init__(self):
        r"""
        :param Name: Service name
        :type Name: str
        :param Ports: Available ports
        :type Ports: list of int
        :param Yaml: Yaml contents
        :type Yaml: str
        :param ApplicationName: Service name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param VersionName: Version name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VersionName: str
        :param ClusterIp: Private IP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClusterIp: list of str
        :param ExternalIp: Public IP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExternalIp: str
        :param Type: The access type. Valid values:
- EXTERNAL (internet access)
- VPC (Intra-VPC access)
- CLUSTER (Intra-cluster access)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        :param SubnetId: Subnet ID. It is filled when the access type is `VPC`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param LoadBalanceId: Load balancer ID. It is filled when the access type is `EXTERNAL` or `CLUSTER`. It’s created automatically by default.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalanceId: str
        :param PortMappings: Port mapping
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PortMappings: list of PortMapping
        :param ServicePortMappingList: Details of each type of access configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServicePortMappingList: list of ServicePortMapping
        :param FlushAll: Flush all types
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FlushAll: bool
        :param EnableRegistryNextDeploy: `0`: Do not inject. `1`: Inject registry information automatically for the next deployment
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableRegistryNextDeploy: int
        :param ApplicationId: The application ID returned.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param AllIpDone: Whether all the application IPs are ready
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AllIpDone: bool
        """
        self.Name = None
        self.Ports = None
        self.Yaml = None
        self.ApplicationName = None
        self.VersionName = None
        self.ClusterIp = None
        self.ExternalIp = None
        self.Type = None
        self.SubnetId = None
        self.LoadBalanceId = None
        self.PortMappings = None
        self.ServicePortMappingList = None
        self.FlushAll = None
        self.EnableRegistryNextDeploy = None
        self.ApplicationId = None
        self.AllIpDone = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Ports = params.get("Ports")
        self.Yaml = params.get("Yaml")
        self.ApplicationName = params.get("ApplicationName")
        self.VersionName = params.get("VersionName")
        self.ClusterIp = params.get("ClusterIp")
        self.ExternalIp = params.get("ExternalIp")
        self.Type = params.get("Type")
        self.SubnetId = params.get("SubnetId")
        self.LoadBalanceId = params.get("LoadBalanceId")
        if params.get("PortMappings") is not None:
            self.PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self.PortMappings.append(obj)
        if params.get("ServicePortMappingList") is not None:
            self.ServicePortMappingList = []
            for item in params.get("ServicePortMappingList"):
                obj = ServicePortMapping()
                obj._deserialize(item)
                self.ServicePortMappingList.append(obj)
        self.FlushAll = params.get("FlushAll")
        self.EnableRegistryNextDeploy = params.get("EnableRegistryNextDeploy")
        self.ApplicationId = params.get("ApplicationId")
        self.AllIpDone = params.get("AllIpDone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerRequest(AbstractModel):
    """EnableApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Service ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerResponse(AbstractModel):
    """EnableApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EnablePrometheusConf(AbstractModel):
    """Enable Prometheus monitoring

    """

    def __init__(self):
        r"""
        :param Port: The listening port of the applicaiton
        :type Port: int
        :param Path: URL path for monitoring
        :type Path: str
        """
        self.Port = None
        self.Path = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsInfo(AbstractModel):
    """Auto scaling configuration

    """

    def __init__(self):
        r"""
        :param MinAliveInstances: Minimum number of instances
        :type MinAliveInstances: int
        :param MaxAliveInstances: Maximum number of instances
        :type MaxAliveInstances: int
        :param EsStrategy: Auto scaling policy. 1: CPU; 2: memory
        :type EsStrategy: int
        :param Threshold: Auto scaling condition value
        :type Threshold: int
        :param VersionId: Version ID
        :type VersionId: str
        """
        self.MinAliveInstances = None
        self.MaxAliveInstances = None
        self.EsStrategy = None
        self.Threshold = None
        self.VersionId = None


    def _deserialize(self, params):
        self.MinAliveInstances = params.get("MinAliveInstances")
        self.MaxAliveInstances = params.get("MaxAliveInstances")
        self.EsStrategy = params.get("EsStrategy")
        self.Threshold = params.get("Threshold")
        self.VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApplicationPackageDownloadUrlRequest(AbstractModel):
    """GenerateApplicationPackageDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param PkgName: Package name
        :type PkgName: str
        :param DeployVersion: Version of the package to download
        :type DeployVersion: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.ApplicationId = None
        self.PkgName = None
        self.DeployVersion = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgName = params.get("PkgName")
        self.DeployVersion = params.get("DeployVersion")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApplicationPackageDownloadUrlResponse(AbstractModel):
    """GenerateApplicationPackageDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param Result: Temp download URL for the package
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class HealthCheckConfig(AbstractModel):
    """Health check configuration

    """

    def __init__(self):
        r"""
        :param Type: Health check type. Valid values: `HttpGet`, `TcpSocket`, `Exec`
        :type Type: str
        :param Protocol: The protocol type. It’s only valid when the health check type is `HttpGet`.
        :type Protocol: str
        :param Path: The request path. It’s only valid when the health check type is `HttpGet`.
        :type Path: str
        :param Exec: The script to be executed. It’s only valid when the health check type is `Exec`.
        :type Exec: str
        :param Port: The request port. It’s only valid when the health check type is `HttpGet` or `TcpSocket `.
        :type Port: int
        :param InitialDelaySeconds: The initial delay for health check in seconds. Default: `0`
        :type InitialDelaySeconds: int
        :param TimeoutSeconds: Timeout period in seconds. Default: `1`
        :type TimeoutSeconds: int
        :param PeriodSeconds: Interval period in seconds. Default: `10`
        :type PeriodSeconds: int
        """
        self.Type = None
        self.Protocol = None
        self.Path = None
        self.Exec = None
        self.Port = None
        self.InitialDelaySeconds = None
        self.TimeoutSeconds = None
        self.PeriodSeconds = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Protocol = params.get("Protocol")
        self.Path = params.get("Path")
        self.Exec = params.get("Exec")
        self.Port = params.get("Port")
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.TimeoutSeconds = params.get("TimeoutSeconds")
        self.PeriodSeconds = params.get("PeriodSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalAutoscaler(AbstractModel):
    """Auto scaling policy

    """

    def __init__(self):
        r"""
        :param MinReplicas: (Optional) Minimum number of instances
        :type MinReplicas: int
        :param MaxReplicas: (Optional) Maximum number of instances
        :type MaxReplicas: int
        :param Metrics: Metric measurement
`CPU`: CPU utilization (%)
`MEMORY`: Memory utilization (%)
`CPU_CORE_USED`: CPU usage (core)
`MEMORY_SIZE_USED`: Memory usage (MiB)
`NETWORK_BANDWIDTH_RECEIVE`: Network bandwidth in (Mbps)
`NETWORK_BANDWIDTH_TRANSMIT`: Network bandwidth out (Mbps)
`NETWORK_TRAFFIC_RECEIVE`: Network traffic in (MiB/s)
`NETWORK_TRAFFIC_TRANSMIT`: Network traffic  out (MiB/s)
`NETWORK_PACKETS_RECEIVE`: Network packets in (packets/sec)
`NETWORK_PACKETS_TRANSMIT`: Network packets out (packets/sec)
`FS_IOPS_WRITE`: Disk writes (count/sec)
`FS_IOPS_READ`: Disk reads (count/sec)
`FS_SIZE_WRITE`: Disk write size (MiB/s)
`FS_SIZE_READ`: Disk read size (MiB/s)
        :type Metrics: str
        :param Threshold: The value of threshold (integer)
        :type Threshold: int
        :param Enabled: Whether it is enabled
        :type Enabled: bool
        :param DoubleThreshold: The value of threshold (demical)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DoubleThreshold: float
        """
        self.MinReplicas = None
        self.MaxReplicas = None
        self.Metrics = None
        self.Threshold = None
        self.Enabled = None
        self.DoubleThreshold = None


    def _deserialize(self, params):
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        self.Metrics = params.get("Metrics")
        self.Threshold = params.get("Threshold")
        self.Enabled = params.get("Enabled")
        self.DoubleThreshold = params.get("DoubleThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressInfo(AbstractModel):
    """Ingress configuration

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param IngressName: ingress name
        :type IngressName: str
        :param Rules: Rules configuration
        :type Rules: list of IngressRule
        :param ClbId: clb ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClbId: str
        :param Tls: TLS configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tls: list of IngressTls
        :param ClusterId: Environment cluster ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param Vip: clb ip
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vip: str
        :param CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param Mixed: Whether to listen on both the HTTP 80 port and HTTPS 443 port. The default value is `false`. The optional value `true` means listening on both the HTTP 80 port and HTTPS 443 port.
        :type Mixed: bool
        :param RewriteType: Redirection mode. Values:
- `AUTO` (automatically redirect HTTP to HTTPS)
- `NONE` (no redirection)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RewriteType: str
        """
        self.EnvironmentId = None
        self.ClusterNamespace = None
        self.AddressIPVersion = None
        self.IngressName = None
        self.Rules = None
        self.ClbId = None
        self.Tls = None
        self.ClusterId = None
        self.Vip = None
        self.CreateTime = None
        self.Mixed = None
        self.RewriteType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterNamespace = params.get("ClusterNamespace")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.IngressName = params.get("IngressName")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = IngressRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.ClbId = params.get("ClbId")
        if params.get("Tls") is not None:
            self.Tls = []
            for item in params.get("Tls"):
                obj = IngressTls()
                obj._deserialize(item)
                self.Tls.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.Vip = params.get("Vip")
        self.CreateTime = params.get("CreateTime")
        self.Mixed = params.get("Mixed")
        self.RewriteType = params.get("RewriteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRule(AbstractModel):
    """Ingress rule configuration

    """

    def __init__(self):
        r"""
        :param Http: ingress rule value
        :type Http: :class:`tencentcloud.tem.v20210701.models.IngressRuleValue`
        :param Host: Host address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Host: str
        :param Protocol: Protocol. Options include HTTP and HTTPS. The default option is HTTP.
        :type Protocol: str
        """
        self.Http = None
        self.Host = None
        self.Protocol = None


    def _deserialize(self, params):
        if params.get("Http") is not None:
            self.Http = IngressRuleValue()
            self.Http._deserialize(params.get("Http"))
        self.Host = params.get("Host")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleBackend(AbstractModel):
    """Ingress rule backend configuration

    """

    def __init__(self):
        r"""
        :param ServiceName: EKS service name
        :type ServiceName: str
        :param ServicePort: EKS service port
        :type ServicePort: int
        """
        self.ServiceName = None
        self.ServicePort = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.ServicePort = params.get("ServicePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRulePath(AbstractModel):
    """Ingress rule path configuration

    """

    def __init__(self):
        r"""
        :param Path: Path information
        :type Path: str
        :param Backend: Backend configuration
        :type Backend: :class:`tencentcloud.tem.v20210701.models.IngressRuleBackend`
        """
        self.Path = None
        self.Backend = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        if params.get("Backend") is not None:
            self.Backend = IngressRuleBackend()
            self.Backend._deserialize(params.get("Backend"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleValue(AbstractModel):
    """Ingress rule value configuration

    """

    def __init__(self):
        r"""
        :param Paths: Overall rule configuration
        :type Paths: list of IngressRulePath
        """
        self.Paths = None


    def _deserialize(self, params):
        if params.get("Paths") is not None:
            self.Paths = []
            for item in params.get("Paths"):
                obj = IngressRulePath()
                obj._deserialize(item)
                self.Paths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressTls(AbstractModel):
    """Ingress TLS configuration

    """

    def __init__(self):
        r"""
        :param Hosts: Host array. An empty array indicates the default certificate for all domain names.
        :type Hosts: list of str
        :param SecretName: Secret name. If a certificate is used, this field is left empty.
        :type SecretName: str
        :param CertificateId: SSL Certificate Id
        :type CertificateId: str
        """
        self.Hosts = None
        self.SecretName = None
        self.CertificateId = None


    def _deserialize(self, params):
        self.Hosts = params.get("Hosts")
        self.SecretName = params.get("SecretName")
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfig(AbstractModel):
    """Log collection configuration

    """

    def __init__(self):
        r"""
        :param Name: Name.
        :type Name: str
        :param InputType: Collection type. Values: `container_stdout` (standard); `container_file` (file)
        :type InputType: str
        :param LogsetId: Logset ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogsetId: str
        :param TopicId: Log topic ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TopicId: str
        :param LogType: Log withdrawal mode. Values: `minimalist_log` (full text in a single line); `multiline_log` (full text in multiple lines); `fullregex_log` (regex in a single line); `multiline_fullregex_log` (regex in multiple lines), `json_log` (JSON); 
        :type LogType: str
        :param BeginningRegex: First line regex. It’s valid when `LogType` is `multiline_log` or `multiline_fullregex_log`.
Note: This field may return `null`, indicating that no valid value was found.
        :type BeginningRegex: str
        :param LogPath: Directory of files to collect. It’s valid when `InputType` is `container_file`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogPath: str
        :param FilePattern: Name pattern of files to collect. It’s valid when `InputType` is `container_file`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FilePattern: str
        :param CreateDate: Creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param ModifyDate: Update time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ModifyDate: str
        :param ApplicationId: Application ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param ExtractRule: Export rules
Note: This field may return `null`, indicating that no valid value was found.
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self.Name = None
        self.InputType = None
        self.LogsetId = None
        self.TopicId = None
        self.LogType = None
        self.BeginningRegex = None
        self.LogPath = None
        self.FilePattern = None
        self.CreateDate = None
        self.ModifyDate = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ExtractRule = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.InputType = params.get("InputType")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.LogType = params.get("LogType")
        self.BeginningRegex = params.get("BeginningRegex")
        self.LogPath = params.get("LogPath")
        self.FilePattern = params.get("FilePattern")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        if params.get("ExtractRule") is not None:
            self.ExtractRule = LogConfigExtractRule()
            self.ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigExtractRule(AbstractModel):
    """Configuration of log exporting rule

    """

    def __init__(self):
        r"""
        :param BeginningRegex: First line regex
Note: This field may return `null`, indicating that no valid value was found.
        :type BeginningRegex: str
        :param Keys: Withdrawl result
Note: This field may return `null`, indicating that no valid value was found.
        :type Keys: list of str
        :param FilterKeys: Filter keys
Note: This field may return `null`, indicating that no valid value was found.
        :type FilterKeys: list of str
        :param FilterRegex: Filter values
Note: This field may return `null`, indicating that no valid value was found.
        :type FilterRegex: list of str
        :param LogRegex: Log regex
Note: This field may return `null`, indicating that no valid value was found.
        :type LogRegex: str
        :param TimeKey: Time field
Note: This field may return `null`, indicating that no valid value was found.
        :type TimeKey: str
        :param TimeFormat: Time Format
Note: This field may return `null`, indicating that no valid value was found.
        :type TimeFormat: str
        :param UnMatchUpload: - Enable the upload of the log that failed to parse
Note: This field may return `null`, indicating that no valid value was found.
        :type UnMatchUpload: str
        :param UnMatchedKey: Key of log failed to be parsed
Note: This field may return `null`, indicating that no valid value was found.
        :type UnMatchedKey: str
        """
        self.BeginningRegex = None
        self.Keys = None
        self.FilterKeys = None
        self.FilterRegex = None
        self.LogRegex = None
        self.TimeKey = None
        self.TimeFormat = None
        self.UnMatchUpload = None
        self.UnMatchedKey = None


    def _deserialize(self, params):
        self.BeginningRegex = params.get("BeginningRegex")
        self.Keys = params.get("Keys")
        self.FilterKeys = params.get("FilterKeys")
        self.FilterRegex = params.get("FilterRegex")
        self.LogRegex = params.get("LogRegex")
        self.TimeKey = params.get("TimeKey")
        self.TimeFormat = params.get("TimeFormat")
        self.UnMatchUpload = params.get("UnMatchUpload")
        self.UnMatchedKey = params.get("UnMatchedKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigListPage(AbstractModel):
    """List of LogConfig

    """

    def __init__(self):
        r"""
        :param Records: Record
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Records: list of LogConfig
        :param ContinueToken: Paging cursor
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ContinueToken: str
        """
        self.Records = None
        self.ContinueToken = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = LogConfig()
                obj._deserialize(item)
                self.Records.append(obj)
        self.ContinueToken = params.get("ContinueToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogOutputConf(AbstractModel):
    """Log output configuration

    """

    def __init__(self):
        r"""
        :param OutputType: Log consumer type
        :type OutputType: str
        :param ClsLogsetName: CLS logset
        :type ClsLogsetName: str
        :param ClsLogTopicId: CLS log topic
        :type ClsLogTopicId: str
        :param ClsLogsetId: CLS logset ID
        :type ClsLogsetId: str
        :param ClsLogTopicName: CLS log topic name
        :type ClsLogTopicName: str
        """
        self.OutputType = None
        self.ClsLogsetName = None
        self.ClsLogTopicId = None
        self.ClsLogsetId = None
        self.ClsLogTopicName = None


    def _deserialize(self, params):
        self.OutputType = params.get("OutputType")
        self.ClsLogsetName = params.get("ClsLogsetName")
        self.ClsLogTopicId = params.get("ClsLogTopicId")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsLogTopicName = params.get("ClsLogTopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationAutoscalerRequest(AbstractModel):
    """ModifyApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        :param Autoscaler: Auto scaling policy
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.AutoscalerId = None
        self.Autoscaler = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        self.AutoscalerId = params.get("AutoscalerId")
        if params.get("Autoscaler") is not None:
            self.Autoscaler = Autoscaler()
            self.Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationAutoscalerResponse(AbstractModel):
    """ModifyApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the action is successful
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyApplicationInfoRequest(AbstractModel):
    """ModifyApplicationInfo request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param Description: Description
        :type Description: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param EnableTracing: (Disused) Whether to enable the call chain. 
        :type EnableTracing: int
        """
        self.ApplicationId = None
        self.Description = None
        self.SourceChannel = None
        self.EnableTracing = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.Description = params.get("Description")
        self.SourceChannel = params.get("SourceChannel")
        self.EnableTracing = params.get("EnableTracing")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationInfoResponse(AbstractModel):
    """ModifyApplicationInfo response structure.

    """

    def __init__(self):
        r"""
        :param Result: Success or not
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyApplicationServiceRequest(AbstractModel):
    """ModifyApplicationService request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param Service: Full access mode settings
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param Data: Single entry access mode settings
        :type Data: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.SourceChannel = None
        self.Service = None
        self.Data = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self.Service = EksService()
            self.Service._deserialize(params.get("Service"))
        if params.get("Data") is not None:
            self.Data = ServicePortMapping()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationServiceResponse(AbstractModel):
    """ModifyApplicationService response structure.

    """

    def __init__(self):
        r"""
        :param Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyConfigDataRequest(AbstractModel):
    """ModifyConfigData request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param Data: Configuration information
        :type Data: list of Pair
        """
        self.EnvironmentId = None
        self.Name = None
        self.SourceChannel = None
        self.Data = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        self.SourceChannel = params.get("SourceChannel")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self.Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigDataResponse(AbstractModel):
    """ModifyConfigData response structure.

    """

    def __init__(self):
        r"""
        :param Result: Result of the modification
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyEnvironmentRequest(AbstractModel):
    """ModifyEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param EnvironmentName: Environment name
        :type EnvironmentName: str
        :param Description: Environment description
        :type Description: str
        :param Vpc: VPC name
        :type Vpc: str
        :param SubnetIds: Subnets
        :type SubnetIds: list of str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param EnvType: Environment type. Values: `test`, `pre`, `prod`
        :type EnvType: str
        """
        self.EnvironmentId = None
        self.EnvironmentName = None
        self.Description = None
        self.Vpc = None
        self.SubnetIds = None
        self.SourceChannel = None
        self.EnvType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Description = params.get("Description")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentResponse(AbstractModel):
    """ModifyEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param Result: Environment ID in case of success and `null` in case of failure
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress request structure.

    """

    def __init__(self):
        r"""
        :param Ingress: Ingress rule configuration
        :type Ingress: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.Ingress = None
        self.SourceChannel = None


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self.Ingress = IngressInfo()
            self.Ingress._deserialize(params.get("Ingress"))
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIngressResponse(AbstractModel):
    """ModifyIngress response structure.

    """

    def __init__(self):
        r"""
        :param Result: Created successfully.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyLogConfigRequest(AbstractModel):
    """ModifyLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Name: Configuration name
        :type Name: str
        :param Data: Log collector configuration
        :type Data: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param ApplicationId: Application ID
        :type ApplicationId: str
        """
        self.EnvironmentId = None
        self.Name = None
        self.Data = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Name = params.get("Name")
        if params.get("Data") is not None:
            self.Data = LogConfig()
            self.Data._deserialize(params.get("Data"))
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogConfigResponse(AbstractModel):
    """ModifyLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param Result: Result of the modification
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class MountedSettingConf(AbstractModel):
    """Mounting configurations

    """

    def __init__(self):
        r"""
        :param ConfigDataName: Configuration name
        :type ConfigDataName: str
        :param MountedPath: Mount point path
        :type MountedPath: str
        :param Data: Configuration content
        :type Data: list of Pair
        :param SecretDataName: Encrypt configuration name
        :type SecretDataName: str
        """
        self.ConfigDataName = None
        self.MountedPath = None
        self.Data = None
        self.SecretDataName = None


    def _deserialize(self, params):
        self.ConfigDataName = params.get("ConfigDataName")
        self.MountedPath = params.get("MountedPath")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self.Data.append(obj)
        self.SecretDataName = params.get("SecretDataName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfo(AbstractModel):
    """Basic information of the namespace

    """

    def __init__(self):
        r"""
        :param EnvironmentId: ID
        :type EnvironmentId: str
        :param NamespaceName: (Disused) Name
        :type NamespaceName: str
        :param Region: Region
        :type Region: str
        :param VpcId: vpc id
        :type VpcId: str
        :param SubnetIds: Array of subnet IDs
        :type SubnetIds: list of str
        :param Description: Description
        :type Description: str
        :param CreatedDate: Creation time
        :type CreatedDate: str
        :param EnvironmentName: Environment name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param ApmInstanceId: APM instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApmInstanceId: str
        :param Locked: Whether the environment is locked. `1`: Locked, `0`: Not locked
Note: This field may return null, indicating that no valid values can be obtained.
        :type Locked: int
        :param Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param EnvType: Environment type. Values: `test`, `pre`, `prod`
Note: This field may return `null`, indicating that no valid value was found.
        :type EnvType: str
        """
        self.EnvironmentId = None
        self.NamespaceName = None
        self.Region = None
        self.VpcId = None
        self.SubnetIds = None
        self.Description = None
        self.CreatedDate = None
        self.EnvironmentName = None
        self.ApmInstanceId = None
        self.Locked = None
        self.Tags = None
        self.EnvType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.NamespaceName = params.get("NamespaceName")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.Description = params.get("Description")
        self.CreatedDate = params.get("CreatedDate")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApmInstanceId = params.get("ApmInstanceId")
        self.Locked = params.get("Locked")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespacePage(AbstractModel):
    """Namespace query result pagination

    """

    def __init__(self):
        r"""
        :param Records: Details of the returned records
        :type Records: list of TemNamespaceInfo
        :param Total: Total number of returned records
        :type Total: int
        :param Size: Number of records per page
        :type Size: int
        :param Pages: Total number of pages
        :type Pages: int
        :param Current: Current entry
Note: This field may return null, indicating that no valid values can be obtained.
        :type Current: int
        """
        self.Records = None
        self.Total = None
        self.Size = None
        self.Pages = None
        self.Current = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = TemNamespaceInfo()
                obj._deserialize(item)
                self.Records.append(obj)
        self.Total = params.get("Total")
        self.Size = params.get("Size")
        self.Pages = params.get("Pages")
        self.Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceStatusInfo(AbstractModel):
    """Environment status

    """

    def __init__(self):
        r"""
        :param EnvironmentId: ID of the environment
        :type EnvironmentId: str
        :param EnvironmentName: Environment name
        :type EnvironmentName: str
        :param ClusterId: TCB envId | EKS clusterId
        :type ClusterId: str
        :param ClusterStatus: Environment status
        :type ClusterStatus: str
        :param EnvironmentStartingStatus: Whether the environment is being started. `null` is returned if it’s not being started.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentStartingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStartingStatus`
        :param EnvironmentStoppingStatus: Whether the environment is being stopped. `null` is returned if it’s not being stopped.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentStoppingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStoppingStatus`
        """
        self.EnvironmentId = None
        self.EnvironmentName = None
        self.ClusterId = None
        self.ClusterStatus = None
        self.EnvironmentStartingStatus = None
        self.EnvironmentStoppingStatus = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterStatus = params.get("ClusterStatus")
        if params.get("EnvironmentStartingStatus") is not None:
            self.EnvironmentStartingStatus = TemEnvironmentStartingStatus()
            self.EnvironmentStartingStatus._deserialize(params.get("EnvironmentStartingStatus"))
        if params.get("EnvironmentStoppingStatus") is not None:
            self.EnvironmentStoppingStatus = TemEnvironmentStoppingStatus()
            self.EnvironmentStoppingStatus._deserialize(params.get("EnvironmentStoppingStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param Name: Node name
        :type Name: str
        :param Zone: Availability zone of the node
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Zone: str
        :param SubnetId: Node subnet ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param AvailableIpCount: Number of available IPs
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AvailableIpCount: str
        :param Cidr: CIDR block
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Cidr: str
        """
        self.Name = None
        self.Zone = None
        self.SubnetId = None
        self.AvailableIpCount = None
        self.Cidr = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")
        self.AvailableIpCount = params.get("AvailableIpCount")
        self.Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pair(AbstractModel):
    """Key value pair

    """

    def __init__(self):
        r"""
        :param Key: Key
        :type Key: str
        :param Value: Value
        :type Value: str
        :param Type: `default``: Custom. `reserved`: System variable. `referenced`: Referenced configuration item.
Note: This field may return `null`, indicating that no valid value can be found.
        :type Type: str
        :param Config: Configuration name
Note: This field may return `null`, indicating that no valid value can be found.
        :type Config: str
        :param Secret: Encrypt configuration name
Note: This field may return `null`, indicating that no valid value was found.
        :type Secret: str
        """
        self.Key = None
        self.Value = None
        self.Type = None
        self.Config = None
        self.Secret = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Type = params.get("Type")
        self.Config = params.get("Config")
        self.Secret = params.get("Secret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortMapping(AbstractModel):
    """Service port mapping

    """

    def __init__(self):
        r"""
        :param Port: Port.
        :type Port: int
        :param TargetPort: Mapped port
        :type TargetPort: int
        :param Protocol: TCP/UDP protocol stack.
        :type Protocol: str
        :param ServiceName: K8s service name
        :type ServiceName: str
        """
        self.Port = None
        self.TargetPort = None
        self.Protocol = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.Protocol = params.get("Protocol")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """Filters for query

    """

    def __init__(self):
        r"""
        :param Name: Name of the field to query
        :type Name: str
        :param Value: Value of the field to query
        :type Value: list of str
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
        


class RestartApplicationPodRequest(AbstractModel):
    """RestartApplicationPod request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param PodName: Name
        :type PodName: str
        :param Limit: Number of items per page
        :type Limit: int
        :param Offset: Page offset
        :type Offset: int
        :param Status: Pod status
        :type Status: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.EnvironmentId = None
        self.ApplicationId = None
        self.PodName = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ApplicationId = params.get("ApplicationId")
        self.PodName = params.get("PodName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartApplicationPodResponse(AbstractModel):
    """RestartApplicationPod response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RestartApplicationRequest(AbstractModel):
    """RestartApplication request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param SourceChannel: Retain as default
        :type SourceChannel: int
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartApplicationResponse(AbstractModel):
    """RestartApplication response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RollingUpdateApplicationByVersionRequest(AbstractModel):
    """RollingUpdateApplicationByVersion request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param DeployVersion: Update version. For image-based deployment, it is the value. For deployment with JAR/WAR files, it is `Version`.
        :type DeployVersion: str
        :param PackageName: JAR/WAR package name. It’s only required for deployment with JAR/WAR files.
        :type PackageName: str
        :param From: Request source. Options: `IntelliJ`, `Coding`
        :type From: str
        :param DeployStrategyType: The deployment policy. Values: `AUTO` (automatically deploy), `BETA` (deploy a small batch first to test the result, and deploy the rest automatically) and `MANUAL` (manually deploy)
        :type DeployStrategyType: str
        :param TotalBatchCount: Total number of batches
        :type TotalBatchCount: int
        :param BatchInterval: Interval between the batches
        :type BatchInterval: int
        :param BetaBatchNum: Number of instances in a beta batch
        :type BetaBatchNum: int
        :param MinAvailable: Minimum number of available instances during the deployment
        :type MinAvailable: int
        """
        self.ApplicationId = None
        self.EnvironmentId = None
        self.DeployVersion = None
        self.PackageName = None
        self.From = None
        self.DeployStrategyType = None
        self.TotalBatchCount = None
        self.BatchInterval = None
        self.BetaBatchNum = None
        self.MinAvailable = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.DeployVersion = params.get("DeployVersion")
        self.PackageName = params.get("PackageName")
        self.From = params.get("From")
        self.DeployStrategyType = params.get("DeployStrategyType")
        self.TotalBatchCount = params.get("TotalBatchCount")
        self.BatchInterval = params.get("BatchInterval")
        self.BetaBatchNum = params.get("BetaBatchNum")
        self.MinAvailable = params.get("MinAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollingUpdateApplicationByVersionResponse(AbstractModel):
    """RollingUpdateApplicationByVersion response structure.

    """

    def __init__(self):
        r"""
        :param Result: Version ID
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """Application pod

    """

    def __init__(self):
        r"""
        :param Webshell: Shell address
        :type Webshell: str
        :param PodId: Pod ID
        :type PodId: str
        :param Status: Status
        :type Status: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param PodIp: Pod IP
        :type PodIp: str
        :param Zone: Availability zone
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Zone: str
        :param DeployVersion: Deployed version
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeployVersion: str
        :param RestartCount: Number of restarts
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RestartCount: int
        :param Ready: Whether the pod is ready
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ready: bool
        :param ContainerState: Container status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ContainerState: str
        :param NodeInfo: Information of the node whether the instance locates
Note: This field may return `null`, indicating that no valid value was found.
        :type NodeInfo: :class:`tencentcloud.tem.v20210701.models.NodeInfo`
        :param StartTime: Start time
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type StartTime: str
        :param Unhealthy: Whether the status is unhealthy or healthy
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Unhealthy: bool
        :param UnhealthyWarningMsg: Warning message when the result is unhealthy
Note: This field may return `null`, indicating that no valid value was found.
        :type UnhealthyWarningMsg: str
        :param VersionId: Version ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VersionId: str
        :param ApplicationName: Application name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        """
        self.Webshell = None
        self.PodId = None
        self.Status = None
        self.CreateTime = None
        self.PodIp = None
        self.Zone = None
        self.DeployVersion = None
        self.RestartCount = None
        self.Ready = None
        self.ContainerState = None
        self.NodeInfo = None
        self.StartTime = None
        self.Unhealthy = None
        self.UnhealthyWarningMsg = None
        self.VersionId = None
        self.ApplicationName = None


    def _deserialize(self, params):
        self.Webshell = params.get("Webshell")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.PodIp = params.get("PodIp")
        self.Zone = params.get("Zone")
        self.DeployVersion = params.get("DeployVersion")
        self.RestartCount = params.get("RestartCount")
        self.Ready = params.get("Ready")
        self.ContainerState = params.get("ContainerState")
        if params.get("NodeInfo") is not None:
            self.NodeInfo = NodeInfo()
            self.NodeInfo._deserialize(params.get("NodeInfo"))
        self.StartTime = params.get("StartTime")
        self.Unhealthy = params.get("Unhealthy")
        self.UnhealthyWarningMsg = params.get("UnhealthyWarningMsg")
        self.VersionId = params.get("VersionId")
        self.ApplicationName = params.get("ApplicationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePage(AbstractModel):
    """List of returned applications

    """

    def __init__(self):
        r"""
        :param Records: List of applications
        :type Records: list of TemService
        :param Total: Total number of applications
        :type Total: int
        :param Size: Number of applications per page
        :type Size: int
        :param Pages: Total number of pages
        :type Pages: int
        :param Current: Number of current entries
Note: This field may return `null`, indicating that no valid value was found.
        :type Current: int
        """
        self.Records = None
        self.Total = None
        self.Size = None
        self.Pages = None
        self.Current = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = TemService()
                obj._deserialize(item)
                self.Records.append(obj)
        self.Total = params.get("Total")
        self.Size = params.get("Size")
        self.Pages = params.get("Pages")
        self.Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMapping(AbstractModel):
    """Port mapping details

    """

    def __init__(self):
        r"""
        :param Type: Specifies how a layer-4 proxy is created.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        :param ServiceName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param ClusterIp: VIP for access within the environment
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterIp: str
        :param ExternalIp: Cluster external IP
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExternalIp: str
        :param SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param VpcId: VPC ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VpcId: str
        :param LoadBalanceId: Load balancer ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalanceId: str
        :param Yaml: YAML contents
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Yaml: str
        :param Ports: List of exposed ports
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Ports: list of int
        :param PortMappingItemList: Port mapping array 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PortMappingItemList: list of ServicePortMappingItem
        """
        self.Type = None
        self.ServiceName = None
        self.ClusterIp = None
        self.ExternalIp = None
        self.SubnetId = None
        self.VpcId = None
        self.LoadBalanceId = None
        self.Yaml = None
        self.Ports = None
        self.PortMappingItemList = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ServiceName = params.get("ServiceName")
        self.ClusterIp = params.get("ClusterIp")
        self.ExternalIp = params.get("ExternalIp")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.LoadBalanceId = params.get("LoadBalanceId")
        self.Yaml = params.get("Yaml")
        self.Ports = params.get("Ports")
        if params.get("PortMappingItemList") is not None:
            self.PortMappingItemList = []
            for item in params.get("PortMappingItemList"):
                obj = ServicePortMappingItem()
                obj._deserialize(item)
                self.PortMappingItemList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMappingItem(AbstractModel):
    """Application port mapping

    """

    def __init__(self):
        r"""
        :param Port: Application access port
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Port: int
        :param TargetPort: Application listening port
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TargetPort: int
        :param Protocol: Protocol type
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Protocol: str
        """
        self.Port = None
        self.TargetPort = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceVersionBrief(AbstractModel):
    """List of application versions

    """

    def __init__(self):
        r"""
        :param VersionName: Version name
        :type VersionName: str
        :param Status: Status of version
        :type Status: str
        :param EnableEs: (Disused) Whether to enable elastic scaling
        :type EnableEs: int
        :param CurrentInstances: Number of current instances
        :type CurrentInstances: int
        :param VersionId: Version ID
        :type VersionId: str
        :param LogOutputConf: (Disused) Log output configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param ExpectedInstances: Expected number of instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectedInstances: int
        :param DeployMode: Deployment mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployMode: str
        :param BuildTaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BuildTaskId: str
        :param EnvironmentId: Environment ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param EnvironmentName: Environment name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param ApplicationId: Application ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param ApplicationName: Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param UnderDeploying: Whether the application is being deployed
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnderDeploying: bool
        :param BatchDeployStatus: Status of batch deployment
Note: This field may return `null`, indicating that no valid value was found.
        :type BatchDeployStatus: str
        :param Zones: Availability zones
Note: This field may return `null`, indicating that no valid value was found.
        :type Zones: list of str
        :param NodeInfos: Node information
Note: This field may return `null`, indicating that no valid value was found.
        :type NodeInfos: list of NodeInfo
        :param PodList: Pod information
Note: This field may return `null`, indicating that no valid value was found.
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param WorkloadInfo: Workload information
Note: This field may return `null`, indicating that no valid value was found.
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param CreateDate: Creation time
Note: This field may return `null`, indicating that no valid value was found.
        :type CreateDate: str
        """
        self.VersionName = None
        self.Status = None
        self.EnableEs = None
        self.CurrentInstances = None
        self.VersionId = None
        self.LogOutputConf = None
        self.ExpectedInstances = None
        self.DeployMode = None
        self.BuildTaskId = None
        self.EnvironmentId = None
        self.EnvironmentName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.UnderDeploying = None
        self.BatchDeployStatus = None
        self.Zones = None
        self.NodeInfos = None
        self.PodList = None
        self.WorkloadInfo = None
        self.CreateDate = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.Status = params.get("Status")
        self.EnableEs = params.get("EnableEs")
        self.CurrentInstances = params.get("CurrentInstances")
        self.VersionId = params.get("VersionId")
        if params.get("LogOutputConf") is not None:
            self.LogOutputConf = LogOutputConf()
            self.LogOutputConf._deserialize(params.get("LogOutputConf"))
        self.ExpectedInstances = params.get("ExpectedInstances")
        self.DeployMode = params.get("DeployMode")
        self.BuildTaskId = params.get("BuildTaskId")
        self.EnvironmentId = params.get("EnvironmentId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.UnderDeploying = params.get("UnderDeploying")
        self.BatchDeployStatus = params.get("BatchDeployStatus")
        self.Zones = params.get("Zones")
        if params.get("NodeInfos") is not None:
            self.NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfos.append(obj)
        if params.get("PodList") is not None:
            self.PodList = DescribeRunPodPage()
            self.PodList._deserialize(params.get("PodList"))
        if params.get("WorkloadInfo") is not None:
            self.WorkloadInfo = WorkloadInfo()
            self.WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self.CreateDate = params.get("CreateDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortType(AbstractModel):
    """Query filter

    """

    def __init__(self):
        r"""
        :param Key: Name of the sorting field
        :type Key: str
        :param Type: `0`: Ascending; `1`: Descending 
        :type Type: int
        """
        self.Key = None
        self.Type = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationRequest(AbstractModel):
    """StopApplication request structure.

    """

    def __init__(self):
        r"""
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param SourceChannel: Retain as default
        :type SourceChannel: int
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self.ApplicationId = None
        self.SourceChannel = None
        self.EnvironmentId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SourceChannel = params.get("SourceChannel")
        self.EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationResponse(AbstractModel):
    """StopApplication response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class StorageConf(AbstractModel):
    """Storage volume configuration

    """

    def __init__(self):
        r"""
        :param StorageVolName: Storage volume name
        :type StorageVolName: str
        :param StorageVolPath: Storage volume path
        :type StorageVolPath: str
        :param StorageVolIp: Storage volume IP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageVolIp: str
        """
        self.StorageVolName = None
        self.StorageVolPath = None
        self.StorageVolIp = None


    def _deserialize(self, params):
        self.StorageVolName = params.get("StorageVolName")
        self.StorageVolPath = params.get("StorageVolPath")
        self.StorageVolIp = params.get("StorageVolIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageMountConf(AbstractModel):
    """Data volume mount information

    """

    def __init__(self):
        r"""
        :param VolumeName: Data volume name
        :type VolumeName: str
        :param MountPath: Data volume binding path
        :type MountPath: str
        """
        self.VolumeName = None
        self.MountPath = None


    def _deserialize(self, params):
        self.VolumeName = params.get("VolumeName")
        self.MountPath = params.get("MountPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Information of tags

    """

    def __init__(self):
        r"""
        :param TagKey: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param TagValue: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStartingStatus(AbstractModel):
    """Environment startup processes (Only applications started by the environment startup)

    """

    def __init__(self):
        r"""
        :param ApplicationNumNeedToStart: Number of applications to start
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationNumNeedToStart: int
        :param StartedApplicationNum: Number of started applictions
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StartedApplicationNum: int
        """
        self.ApplicationNumNeedToStart = None
        self.StartedApplicationNum = None


    def _deserialize(self, params):
        self.ApplicationNumNeedToStart = params.get("ApplicationNumNeedToStart")
        self.StartedApplicationNum = params.get("StartedApplicationNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStoppingStatus(AbstractModel):
    """Processes stopped by the environment (Only applications stopped by the action of stopping the environment)

    """

    def __init__(self):
        r"""
        :param ApplicationNumNeedToStop: Number of applications to stop
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationNumNeedToStop: int
        :param StoppedApplicationNum: Number of stopped applications
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StoppedApplicationNum: int
        """
        self.ApplicationNumNeedToStop = None
        self.StoppedApplicationNum = None


    def _deserialize(self, params):
        self.ApplicationNumNeedToStop = params.get("ApplicationNumNeedToStop")
        self.StoppedApplicationNum = params.get("StoppedApplicationNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemNamespaceInfo(AbstractModel):
    """Namespace object

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param Channel: Channel
        :type Channel: str
        :param EnvironmentName: Environment name
        :type EnvironmentName: str
        :param Region: Region name
        :type Region: str
        :param Description: Environment description
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param Status: Status. `1`: terminated; `0`: normal
        :type Status: int
        :param Vpc: VPC network
        :type Vpc: str
        :param CreateDate: Creation time
        :type CreateDate: str
        :param ModifyDate: Modification time
        :type ModifyDate: str
        :param Modifier: Modifier
        :type Modifier: str
        :param Creator: Creator
        :type Creator: str
        :param ApplicationNum: Number of applications
        :type ApplicationNum: int
        :param RunInstancesNum: Number of running instances
        :type RunInstancesNum: int
        :param SubnetId: Subnet
        :type SubnetId: str
        :param ClusterStatus: Environment cluster status
        :type ClusterStatus: str
        :param EnableTswTraceService: Whether to enable TSW
        :type EnableTswTraceService: bool
        :param Locked: Whether the environment is locked. `1`: locked; `0`: not locked
        :type Locked: int
        :param AppId: User AppId
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: str
        :param Uin: User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param SubAccountUin: The UIN of sub-account
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubAccountUin: str
        :param ClusterId: Application ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param Tags: Tag.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param HasAuthority: Whether it’s authorized to access the resource
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasAuthority: bool
        :param EnvType: Environment type. Values: `test`, `pre`, `prod`
Note: This field may return `null`, indicating that no valid value was found.
        :type EnvType: str
        :param RegionId: Region code
Note: This field may return `null`, indicating that no valid value was found.
        :type RegionId: str
        """
        self.EnvironmentId = None
        self.Channel = None
        self.EnvironmentName = None
        self.Region = None
        self.Description = None
        self.Status = None
        self.Vpc = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Modifier = None
        self.Creator = None
        self.ApplicationNum = None
        self.RunInstancesNum = None
        self.SubnetId = None
        self.ClusterStatus = None
        self.EnableTswTraceService = None
        self.Locked = None
        self.AppId = None
        self.Uin = None
        self.SubAccountUin = None
        self.ClusterId = None
        self.Tags = None
        self.HasAuthority = None
        self.EnvType = None
        self.RegionId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.Channel = params.get("Channel")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Region = params.get("Region")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Vpc = params.get("Vpc")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        self.ApplicationNum = params.get("ApplicationNum")
        self.RunInstancesNum = params.get("RunInstancesNum")
        self.SubnetId = params.get("SubnetId")
        self.ClusterStatus = params.get("ClusterStatus")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
        self.Locked = params.get("Locked")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.SubAccountUin = params.get("SubAccountUin")
        self.ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HasAuthority = params.get("HasAuthority")
        self.EnvType = params.get("EnvType")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemService(AbstractModel):
    """Application details

    """

    def __init__(self):
        r"""
        :param ApplicationId: Version ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param Description: Description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param EnvironmentId: ID of the environment
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param CreateDate: Creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param ModifyDate: Modification time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ModifyDate: str
        :param Modifier: Modifier
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Modifier: str
        :param Creator: Creator account
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Creator: str
        :param RepoType: TCR Individual or TCR Enterprise
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoType: int
        :param InstanceId: ID of the TCR Enterprise instance
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param RepoName: Name of the TCR instance
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoName: str
        :param CodingLanguage: Programming Language
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CodingLanguage: str
        :param DeployMode: Deployment mode
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployMode: str
        :param EnvironmentName: Environment name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param ActiveVersions: The instance information where the application is running
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ActiveVersions: list of ServiceVersionBrief
        :param EnableTracing: Whether to enable link tracing
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableTracing: int
        :param Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param HasAuthority: Whether it’s authorized to access the resource
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasAuthority: bool
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.Description = None
        self.EnvironmentId = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Modifier = None
        self.Creator = None
        self.RepoType = None
        self.InstanceId = None
        self.RepoName = None
        self.CodingLanguage = None
        self.DeployMode = None
        self.EnvironmentName = None
        self.ActiveVersions = None
        self.EnableTracing = None
        self.Tags = None
        self.HasAuthority = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.Description = params.get("Description")
        self.EnvironmentId = params.get("EnvironmentId")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        self.RepoType = params.get("RepoType")
        self.InstanceId = params.get("InstanceId")
        self.RepoName = params.get("RepoName")
        self.CodingLanguage = params.get("CodingLanguage")
        self.DeployMode = params.get("DeployMode")
        self.EnvironmentName = params.get("EnvironmentName")
        if params.get("ActiveVersions") is not None:
            self.ActiveVersions = []
            for item in params.get("ActiveVersions"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self.ActiveVersions.append(obj)
        self.EnableTracing = params.get("EnableTracing")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HasAuthority = params.get("HasAuthority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemServiceVersionInfo(AbstractModel):
    """Version information

    """

    def __init__(self):
        r"""
        :param VersionId: Version ID
        :type VersionId: str
        :param ApplicationId: Application ID
        :type ApplicationId: str
        :param DeployMode: Deployment mode
        :type DeployMode: str
        :param JdkVersion: JDK version
        :type JdkVersion: str
        :param Description: Description
        :type Description: str
        :param DeployVersion: Deployed version
        :type DeployVersion: str
        :param PublishMode: Publish mode
        :type PublishMode: str
        :param JvmOpts: Launch parameter
        :type JvmOpts: str
        :param InitPodNum: Number of initial pods
        :type InitPodNum: int
        :param CpuSpec: CPU specification
        :type CpuSpec: float
        :param MemorySpec: Memory specification
        :type MemorySpec: float
        :param ImgRepo: Image path
        :type ImgRepo: str
        :param ImgName: Image name
        :type ImgName: str
        :param ImgVersion: Image version
        :type ImgVersion: str
        :param EsInfo: Scaling configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
        :param EnvConf: Environment configuration
        :type EnvConf: list of Pair
        :param StorageConfs: Storage configuration
        :type StorageConfs: list of StorageConf
        :param Status: Running status
        :type Status: str
        :param Vpc: VPC
        :type Vpc: str
        :param SubnetId: Subnets
        :type SubnetId: str
        :param CreateDate: Creation time
        :type CreateDate: str
        :param ModifyDate: Modification time
        :type ModifyDate: str
        :param StorageMountConfs: Mounting configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StorageMountConfs: list of StorageMountConf
        :param VersionName: Version name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VersionName: str
        :param LogOutputConf: Log output configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param ApplicationDescription: Application description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationDescription: str
        :param EnvironmentName: Environment name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param EnvironmentId: Environment ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param PublicDomain: Public network address
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PublicDomain: str
        :param EnablePublicAccess: Whether to enable public network access
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnablePublicAccess: bool
        :param CurrentInstances: Number of current instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CurrentInstances: int
        :param ExpectedInstances: Number of expected instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExpectedInstances: int
        :param CodingLanguage: Programming Language
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CodingLanguage: str
        :param PkgName: Program package name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PkgName: str
        :param EsEnable: Whether to enable auto scaling
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EsEnable: int
        :param EsStrategy: Auto scaling policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EsStrategy: int
        :param ImageTag: Image tag
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageTag: str
        :param LogEnable: Whether to enable logging
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogEnable: int
        :param MinAliveInstances: Minimum number of instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MinAliveInstances: str
        :param SecurityGroupIds: Security group IDs
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroupIds: list of str
        :param ImageCommand: Image command
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageCommand: str
        :param ImageArgs: Image command parameters
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageArgs: list of str
        :param UseRegistryDefaultConfig: Whether to use the default registry configurations
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UseRegistryDefaultConfig: bool
        :param Service: EKS access configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param SettingConfs: Mounting configurations
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SettingConfs: list of MountedSettingConf
        :param LogConfs: Log path information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogConfs: list of str
        :param PostStart: The script to execute right after the startup
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PostStart: str
        :param PreStop: The script to run before stop
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PreStop: str
        :param Liveness: Configuration of aliveness probe
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param Readiness: Configuration of readiness probe
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param HorizontalAutoscaler: Auto scaling policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param CronHorizontalAutoscaler: Scheduled auto scaling policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param Zones: Availability zone of the application
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param LastDeployDate: The latest deployment time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastDeployDate: str
        :param LastDeploySuccessDate: The latest successful deployment time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastDeploySuccessDate: str
        :param NodeInfos: Information of the node whether the application is deployed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NodeInfos: list of NodeInfo
        :param ImageType: Image type. Values: `0` (Demo image), `1` (Normal image)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageType: int
        :param EnableTracing: Whether to 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableTracing: int
        :param EnableTracingReport: (Disused) Whether to enable linkage tracing and report. It only takes effect when EnableTracing = `1`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableTracingReport: int
        :param RepoType: Image type. `0`: Individual image; `1`: Enterprise image; `2`: Public image
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoType: int
        :param BatchDeployStatus: Status of batch deployment: `batch_updating`, `batch_updating_waiting_confirm`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BatchDeployStatus: str
        :param ApmInstanceId: APM instance ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApmInstanceId: str
        :param WorkloadInfo: Workload information 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param SpeedUp: Whether to enable application acceleration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SpeedUp: bool
        :param StartupProbe: Configuration of the startup probe
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param OsFlavour: OS version. Values:
- ALPINE
- CENTOS
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OsFlavour: str
        :param RepoServer: Image repository server
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoServer: str
        :param UnderDeploying: Whether the application is being deployed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UnderDeploying: bool
        :param EnablePrometheusConf: Whether to enable application metric monitoring 
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param StoppedManually: Whether it’s stopped manually
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StoppedManually: bool
        :param TcrInstanceId: TCR instance ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TcrInstanceId: str
        :param EnableMetrics: `1`: Automatically enable metrics collection (open-telemetry)
`0`: Disable metrics collection
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableMetrics: int
        :param AppId: User AppId
Note: This field may return `null`, indicating that no valid value was found.
        :type AppId: str
        :param SubAccountUin: Sub Account UIN
Note: This field may return `null`, indicating that no valid value was found.
        :type SubAccountUin: str
        :param Uin: User UIN
Note: This field may return `null`, indicating that no valid value was found.
        :type Uin: str
        :param Region: Region
Note: This field may return `null`, indicating that no valid value was found.
        :type Region: str
        :param GroupId: Application group ID
Note: This field may return `null`, indicating that no valid value was found.
        :type GroupId: str
        :param EnableRegistry: Whether to enable registry
Note: This field may return `null`, indicating that no valid value was found.
        :type EnableRegistry: int
        :param AutoscalerList: Array of scaling rules
Note: This field may return `null`, indicating that no valid value was found.
        :type AutoscalerList: list of Autoscaler
        :param Modifier: Modifier
Note: This field may return `null`, indicating that no valid value was found.
        :type Modifier: str
        :param Creator: Creator
Note: This field may return `null`, indicating that no valid value was found.
        :type Creator: str
        :param DeployStrategyConf: Deployment strategy
Note: This field may return `null`, indicating that no valid value was found.
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param PodList: List of pods
Note: This field may return `null`, indicating that no valid value was found.
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param ConfEdited: Whether the configuration has been changed during deployment
Note: This field may return `null`, indicating that no valid value was found.
        :type ConfEdited: bool
        :param Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        """
        self.VersionId = None
        self.ApplicationId = None
        self.DeployMode = None
        self.JdkVersion = None
        self.Description = None
        self.DeployVersion = None
        self.PublishMode = None
        self.JvmOpts = None
        self.InitPodNum = None
        self.CpuSpec = None
        self.MemorySpec = None
        self.ImgRepo = None
        self.ImgName = None
        self.ImgVersion = None
        self.EsInfo = None
        self.EnvConf = None
        self.StorageConfs = None
        self.Status = None
        self.Vpc = None
        self.SubnetId = None
        self.CreateDate = None
        self.ModifyDate = None
        self.StorageMountConfs = None
        self.VersionName = None
        self.LogOutputConf = None
        self.ApplicationName = None
        self.ApplicationDescription = None
        self.EnvironmentName = None
        self.EnvironmentId = None
        self.PublicDomain = None
        self.EnablePublicAccess = None
        self.CurrentInstances = None
        self.ExpectedInstances = None
        self.CodingLanguage = None
        self.PkgName = None
        self.EsEnable = None
        self.EsStrategy = None
        self.ImageTag = None
        self.LogEnable = None
        self.MinAliveInstances = None
        self.SecurityGroupIds = None
        self.ImageCommand = None
        self.ImageArgs = None
        self.UseRegistryDefaultConfig = None
        self.Service = None
        self.SettingConfs = None
        self.LogConfs = None
        self.PostStart = None
        self.PreStop = None
        self.Liveness = None
        self.Readiness = None
        self.HorizontalAutoscaler = None
        self.CronHorizontalAutoscaler = None
        self.Zones = None
        self.LastDeployDate = None
        self.LastDeploySuccessDate = None
        self.NodeInfos = None
        self.ImageType = None
        self.EnableTracing = None
        self.EnableTracingReport = None
        self.RepoType = None
        self.BatchDeployStatus = None
        self.ApmInstanceId = None
        self.WorkloadInfo = None
        self.SpeedUp = None
        self.StartupProbe = None
        self.OsFlavour = None
        self.RepoServer = None
        self.UnderDeploying = None
        self.EnablePrometheusConf = None
        self.StoppedManually = None
        self.TcrInstanceId = None
        self.EnableMetrics = None
        self.AppId = None
        self.SubAccountUin = None
        self.Uin = None
        self.Region = None
        self.GroupId = None
        self.EnableRegistry = None
        self.AutoscalerList = None
        self.Modifier = None
        self.Creator = None
        self.DeployStrategyConf = None
        self.PodList = None
        self.ConfEdited = None
        self.Tags = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.ApplicationId = params.get("ApplicationId")
        self.DeployMode = params.get("DeployMode")
        self.JdkVersion = params.get("JdkVersion")
        self.Description = params.get("Description")
        self.DeployVersion = params.get("DeployVersion")
        self.PublishMode = params.get("PublishMode")
        self.JvmOpts = params.get("JvmOpts")
        self.InitPodNum = params.get("InitPodNum")
        self.CpuSpec = params.get("CpuSpec")
        self.MemorySpec = params.get("MemorySpec")
        self.ImgRepo = params.get("ImgRepo")
        self.ImgName = params.get("ImgName")
        self.ImgVersion = params.get("ImgVersion")
        if params.get("EsInfo") is not None:
            self.EsInfo = EsInfo()
            self.EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self.EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self.EnvConf.append(obj)
        if params.get("StorageConfs") is not None:
            self.StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self.StorageConfs.append(obj)
        self.Status = params.get("Status")
        self.Vpc = params.get("Vpc")
        self.SubnetId = params.get("SubnetId")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        if params.get("StorageMountConfs") is not None:
            self.StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self.StorageMountConfs.append(obj)
        self.VersionName = params.get("VersionName")
        if params.get("LogOutputConf") is not None:
            self.LogOutputConf = LogOutputConf()
            self.LogOutputConf._deserialize(params.get("LogOutputConf"))
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationDescription = params.get("ApplicationDescription")
        self.EnvironmentName = params.get("EnvironmentName")
        self.EnvironmentId = params.get("EnvironmentId")
        self.PublicDomain = params.get("PublicDomain")
        self.EnablePublicAccess = params.get("EnablePublicAccess")
        self.CurrentInstances = params.get("CurrentInstances")
        self.ExpectedInstances = params.get("ExpectedInstances")
        self.CodingLanguage = params.get("CodingLanguage")
        self.PkgName = params.get("PkgName")
        self.EsEnable = params.get("EsEnable")
        self.EsStrategy = params.get("EsStrategy")
        self.ImageTag = params.get("ImageTag")
        self.LogEnable = params.get("LogEnable")
        self.MinAliveInstances = params.get("MinAliveInstances")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.ImageCommand = params.get("ImageCommand")
        self.ImageArgs = params.get("ImageArgs")
        self.UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("Service") is not None:
            self.Service = EksService()
            self.Service._deserialize(params.get("Service"))
        if params.get("SettingConfs") is not None:
            self.SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self.SettingConfs.append(obj)
        self.LogConfs = params.get("LogConfs")
        self.PostStart = params.get("PostStart")
        self.PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self.Liveness = HealthCheckConfig()
            self.Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self.Readiness = HealthCheckConfig()
            self.Readiness._deserialize(params.get("Readiness"))
        if params.get("HorizontalAutoscaler") is not None:
            self.HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self.HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self.CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self.CronHorizontalAutoscaler.append(obj)
        self.Zones = params.get("Zones")
        self.LastDeployDate = params.get("LastDeployDate")
        self.LastDeploySuccessDate = params.get("LastDeploySuccessDate")
        if params.get("NodeInfos") is not None:
            self.NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self.NodeInfos.append(obj)
        self.ImageType = params.get("ImageType")
        self.EnableTracing = params.get("EnableTracing")
        self.EnableTracingReport = params.get("EnableTracingReport")
        self.RepoType = params.get("RepoType")
        self.BatchDeployStatus = params.get("BatchDeployStatus")
        self.ApmInstanceId = params.get("ApmInstanceId")
        if params.get("WorkloadInfo") is not None:
            self.WorkloadInfo = WorkloadInfo()
            self.WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self.SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self.StartupProbe = HealthCheckConfig()
            self.StartupProbe._deserialize(params.get("StartupProbe"))
        self.OsFlavour = params.get("OsFlavour")
        self.RepoServer = params.get("RepoServer")
        self.UnderDeploying = params.get("UnderDeploying")
        if params.get("EnablePrometheusConf") is not None:
            self.EnablePrometheusConf = EnablePrometheusConf()
            self.EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self.StoppedManually = params.get("StoppedManually")
        self.TcrInstanceId = params.get("TcrInstanceId")
        self.EnableMetrics = params.get("EnableMetrics")
        self.AppId = params.get("AppId")
        self.SubAccountUin = params.get("SubAccountUin")
        self.Uin = params.get("Uin")
        self.Region = params.get("Region")
        self.GroupId = params.get("GroupId")
        self.EnableRegistry = params.get("EnableRegistry")
        if params.get("AutoscalerList") is not None:
            self.AutoscalerList = []
            for item in params.get("AutoscalerList"):
                obj = Autoscaler()
                obj._deserialize(item)
                self.AutoscalerList.append(obj)
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("PodList") is not None:
            self.PodList = DescribeRunPodPage()
            self.PodList._deserialize(params.get("PodList"))
        self.ConfEdited = params.get("ConfEdited")
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
        


class UseDefaultRepoParameters(AbstractModel):
    """Repository parameters

    """

    def __init__(self):
        r"""
        :param EnterpriseInstanceName: TCR Enterprise instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnterpriseInstanceName: str
        :param EnterpriseInstanceChargeType: TCR Enterprise billing mode. `0`: Pay-as-you-go 
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnterpriseInstanceChargeType: int
        :param EnterpriseInstanceType: Edition of the TCR Enterprise. Values: `basic`, `standard`, `premium` (Advanced edition)
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnterpriseInstanceType: str
        """
        self.EnterpriseInstanceName = None
        self.EnterpriseInstanceChargeType = None
        self.EnterpriseInstanceType = None


    def _deserialize(self, params):
        self.EnterpriseInstanceName = params.get("EnterpriseInstanceName")
        self.EnterpriseInstanceChargeType = params.get("EnterpriseInstanceChargeType")
        self.EnterpriseInstanceType = params.get("EnterpriseInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadInfo(AbstractModel):
    """Workload details

    """

    def __init__(self):
        r"""
        :param ClusterId: The resource ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param VersionName: Version name
Note: This field may return `null`, indicating that no valid value was found.
        :type VersionName: str
        :param ReadyReplicas: Number of ready replicas
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReadyReplicas: int
        :param Replicas: Number of replicas
Note: This field may return `null`, indicating that no valid value was found.
        :type Replicas: int
        :param UpdatedReplicas: Number of updated replicas
Note: This field may return `null`, indicating that no valid value was found.
        :type UpdatedReplicas: int
        :param UpdatedReadyReplicas: Number of replicas ready for update
Note: This field may return `null`, indicating that no valid value was found.
        :type UpdatedReadyReplicas: int
        :param UpdateRevision: ## Version Updates
Note: This field may return `null`, indicating that no valid value was found.
        :type UpdateRevision: str
        :param CurrentRevision: Current Version
Note: This field may return `null`, indicating that no valid value was found.
        :type CurrentRevision: str
        """
        self.ClusterId = None
        self.ApplicationName = None
        self.VersionName = None
        self.ReadyReplicas = None
        self.Replicas = None
        self.UpdatedReplicas = None
        self.UpdatedReadyReplicas = None
        self.UpdateRevision = None
        self.CurrentRevision = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ApplicationName = params.get("ApplicationName")
        self.VersionName = params.get("VersionName")
        self.ReadyReplicas = params.get("ReadyReplicas")
        self.Replicas = params.get("Replicas")
        self.UpdatedReplicas = params.get("UpdatedReplicas")
        self.UpdatedReadyReplicas = params.get("UpdatedReadyReplicas")
        self.UpdateRevision = params.get("UpdateRevision")
        self.CurrentRevision = params.get("CurrentRevision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        