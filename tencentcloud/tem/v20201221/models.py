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
        :param TmpSecretId: `SecretId` of temporary key
        :type TmpSecretId: str
        :param TmpSecretKey: `SecretKey` of temporary key
        :type TmpSecretKey: str
        :param SessionToken: `sessionToken` of temporary key
        :type SessionToken: str
        :param StartTime: `StartTime` of temporary key acquisition
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
        


class CreateCosTokenV2Request(AbstractModel):
    """CreateCosTokenV2 request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Service ID
        :type ServiceId: str
        :param PkgName: Package name
        :type PkgName: str
        :param OptType: optType. 1: upload; 2: query
        :type OptType: int
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param TimeVersion: Input parameter of `deployVersion`
        :type TimeVersion: str
        """
        self.ServiceId = None
        self.PkgName = None
        self.OptType = None
        self.SourceChannel = None
        self.TimeVersion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
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
        


class CreateCosTokenV2Response(AbstractModel):
    """CreateCosTokenV2 response structure.

    """

    def __init__(self):
        r"""
        :param Result: `CosToken` object in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`
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


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace request structure.

    """

    def __init__(self):
        r"""
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param Vpc: VPC name
        :type Vpc: str
        :param SubnetIds: Subnet list
        :type SubnetIds: list of str
        :param Description: Namespace description
        :type Description: str
        :param K8sVersion: K8s version
        :type K8sVersion: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param EnableTswTraceService: Whether to enable the TSW service.
        :type EnableTswTraceService: bool
        """
        self.NamespaceName = None
        self.Vpc = None
        self.SubnetIds = None
        self.Description = None
        self.K8sVersion = None
        self.SourceChannel = None
        self.EnableTswTraceService = None


    def _deserialize(self, params):
        self.NamespaceName = params.get("NamespaceName")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.Description = params.get("Description")
        self.K8sVersion = params.get("K8sVersion")
        self.SourceChannel = params.get("SourceChannel")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
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
        r"""
        :param Result: Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: str
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
        :param NamespaceId: Namespace ID
        :type NamespaceId: str
        :param ResourceType: Resource type. Valid values: CFS (file system), CLS (log service), TSE_SRE (registry)
        :type ResourceType: str
        :param ResourceId: Resource ID
        :type ResourceId: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.ResourceType = None
        self.ResourceId = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.SourceChannel = params.get("SourceChannel")
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
        :param Result: Success or failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateServiceV2Request(AbstractModel):
    """CreateServiceV2 request structure.

    """

    def __init__(self):
        r"""
        :param ServiceName: Service name
        :type ServiceName: str
        :param Description: Description
        :type Description: str
        :param UseDefaultImageService: Whether to use the default image service. 1: yes; 0: no
        :type UseDefaultImageService: int
        :param RepoType: Type of the bound repository. 0: Personal Edition; 1: Enterprise Edition
        :type RepoType: int
        :param InstanceId: Instance ID of Enterprise Edition image service
        :type InstanceId: str
        :param RepoServer: Address of the bound image server
        :type RepoServer: str
        :param RepoName: Name of the bound image repository
        :type RepoName: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param SubnetList: Service subnet
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
        """
        self.ServiceName = None
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


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceV2Response(AbstractModel):
    """CreateServiceV2 response structure.

    """

    def __init__(self):
        r"""
        :param Result: Service code
        :type Result: str
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
        :param NamespaceId: tem NamespaceId
        :type NamespaceId: str
        :param EksNamespace: EKS namespace name
        :type EksNamespace: str
        :param Name: Ingress rule name
        :type Name: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.Name = params.get("Name")
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
        :param Result: Whether deletion succeeded
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployServiceV2Request(AbstractModel):
    """DeployServiceV2 request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Service ID
        :type ServiceId: str
        :param ContainerPort: Container port
        :type ContainerPort: int
        :param InitPodNum: Number of initialized pods
        :type InitPodNum: int
        :param CpuSpec: CPU specification
        :type CpuSpec: float
        :param MemorySpec: Memory specification
        :type MemorySpec: float
        :param NamespaceId: Environment ID
        :type NamespaceId: str
        :param ImgRepo: Image repository
        :type ImgRepo: str
        :param VersionDesc: Version description
        :type VersionDesc: str
        :param JvmOpts: Launch parameters
        :type JvmOpts: str
        :param EsInfo: Auto scaling configuration. If this parameter is left empty, auto scaling will not be enabled
        :type EsInfo: :class:`tencentcloud.tem.v20201221.models.EsInfo`
        :param EnvConf: Environment variable configuration
        :type EnvConf: list of Pair
        :param LogConfs: Log configuration
        :type LogConfs: list of str
        :param StorageConfs: Data volume configuration
        :type StorageConfs: list of StorageConf
        :param StorageMountConfs: Data volume mount configuration
        :type StorageMountConfs: list of StorageMountConf
        :param DeployMode: Deployment type.
- JAR: deployment through JAR package
- WAR: deployment through WAR package
- IMAGE: deployment through image
        :type DeployMode: str
        :param DeployVersion: When the deployment type is `IMAGE`, this parameter indicates the image tag.
When the deployment type is `JAR` or `WAR`, this parameter indicates the package version number.
        :type DeployVersion: str
        :param PkgName: Package name, which is required when using JAR or WAR packages for deployment.
        :type PkgName: str
        :param JdkVersion: JDK version.
- KONA: use KONA JDK.
- OPEN: use open JDK.
        :type JdkVersion: str
        :param SecurityGroupIds: Security group IDs
        :type SecurityGroupIds: list of str
        :param LogOutputConf: Log output configuration
        :type LogOutputConf: :class:`tencentcloud.tem.v20201221.models.LogOutputConf`
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param Description: Version description
        :type Description: str
        :param ImageCommand: Image command
        :type ImageCommand: str
        :param ImageArgs: Image command parameters
        :type ImageArgs: list of str
        :param PortMappings: Service port mapping.
        :type PortMappings: list of PortMapping
        :param UseRegistryDefaultConfig: Whether to add the registry’s default configurations.
        :type UseRegistryDefaultConfig: bool
        :param SettingConfs: Mounting configurations
        :type SettingConfs: list of MountedSettingConf
        :param EksService: EKS access configuration
        :type EksService: :class:`tencentcloud.tem.v20201221.models.EksService`
        :param VersionId: ID of the version that you want to roll back to
        :type VersionId: str
        :param PostStart: The script to run after startup
        :type PostStart: str
        :param PreStop: The script to run before stop
        :type PreStop: str
        :param DeployStrategyConf: Configuration of 
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20201221.models.DeployStrategyConf`
        :param Liveness: Configuration of aliveness probe
        :type Liveness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        :param Readiness: Configuration of readiness probe
        :type Readiness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        self.ServiceId = None
        self.ContainerPort = None
        self.InitPodNum = None
        self.CpuSpec = None
        self.MemorySpec = None
        self.NamespaceId = None
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
        self.PortMappings = None
        self.UseRegistryDefaultConfig = None
        self.SettingConfs = None
        self.EksService = None
        self.VersionId = None
        self.PostStart = None
        self.PreStop = None
        self.DeployStrategyConf = None
        self.Liveness = None
        self.Readiness = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ContainerPort = params.get("ContainerPort")
        self.InitPodNum = params.get("InitPodNum")
        self.CpuSpec = params.get("CpuSpec")
        self.MemorySpec = params.get("MemorySpec")
        self.NamespaceId = params.get("NamespaceId")
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
        if params.get("PortMappings") is not None:
            self.PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self.PortMappings.append(obj)
        self.UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self.SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self.SettingConfs.append(obj)
        if params.get("EksService") is not None:
            self.EksService = EksService()
            self.EksService._deserialize(params.get("EksService"))
        self.VersionId = params.get("VersionId")
        self.PostStart = params.get("PostStart")
        self.PreStop = params.get("PreStop")
        if params.get("DeployStrategyConf") is not None:
            self.DeployStrategyConf = DeployStrategyConf()
            self.DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("Liveness") is not None:
            self.Liveness = HealthCheckConfig()
            self.Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self.Readiness = HealthCheckConfig()
            self.Readiness._deserialize(params.get("Readiness"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServiceV2Response(AbstractModel):
    """DeployServiceV2 response structure.

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
        :param BetaBatchNum: Number of instances for the beta batch
        :type BetaBatchNum: int
        :param DeployStrategyType: Batch deploy policy. `0`: automatically; `1`: manually. If you use beta batch, the policy for beta batch must be `0`. The policy specified here only applies to the rest batches.
        :type DeployStrategyType: int
        :param BatchInterval: Interval between batches
        :type BatchInterval: int
        """
        self.TotalBatchCount = None
        self.BetaBatchNum = None
        self.DeployStrategyType = None
        self.BatchInterval = None


    def _deserialize(self, params):
        self.TotalBatchCount = params.get("TotalBatchCount")
        self.BetaBatchNum = params.get("BetaBatchNum")
        self.DeployStrategyType = params.get("DeployStrategyType")
        self.BatchInterval = params.get("BatchInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress request structure.

    """

    def __init__(self):
        r"""
        :param NamespaceId: tem namespaceId
        :type NamespaceId: str
        :param EksNamespace: EKS namespace name
        :type EksNamespace: str
        :param Name: Ingress rule name
        :type Name: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.Name = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.Name = params.get("Name")
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
        :type Result: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
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
        :param NamespaceId: namespace id
        :type NamespaceId: str
        :param EksNamespace: namespace
        :type EksNamespace: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        :param Names: Ingress rule name list.
        :type Names: list of str
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.SourceChannel = None
        self.Names = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.Names = params.get("Names")
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
Note: this field may return null, indicating that no valid values can be obtained.
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


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param Limit: Number of items per page
        :type Limit: int
        :param Offset: Page number
        :type Offset: int
        :param SourceChannel: Source
        :type SourceChannel: int
        """
        self.Limit = None
        self.Offset = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20201221.models.NamespacePage`
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


class DescribeRelatedIngressesRequest(AbstractModel):
    """DescribeRelatedIngresses request structure.

    """

    def __init__(self):
        r"""
        :param NamespaceId: Environment ID.
        :type NamespaceId: str
        :param EksNamespace: EKS namespace.
        :type EksNamespace: str
        :param SourceChannel: Source channel.
        :type SourceChannel: int
        :param ServiceId: Service ID.
        :type ServiceId: str
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.SourceChannel = None
        self.ServiceId = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.SourceChannel = params.get("SourceChannel")
        self.ServiceId = params.get("ServiceId")
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
        :param Result: Ingress array.
Note: this field may return `null`, indicating that no valid value can be obtained.
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
        :param Offset: Page number
        :type Offset: int
        :param Limit: Number of items per page
        :type Limit: int
        :param TotalCount: Total number
        :type TotalCount: int
        :param RequestId: Request ID
        :type RequestId: str
        :param PodList: Number of items
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
        


class DescribeServiceRunPodListV2Request(AbstractModel):
    """DescribeServiceRunPodListV2 request structure.

    """

    def __init__(self):
        r"""
        :param NamespaceId: Environment ID
        :type NamespaceId: str
        :param ServiceId: Service name ID
        :type ServiceId: str
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
        self.NamespaceId = None
        self.ServiceId = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.PodName = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ServiceId = params.get("ServiceId")
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
        


class DescribeServiceRunPodListV2Response(AbstractModel):
    """DescribeServiceRunPodListV2 response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20201221.models.DescribeRunPodPage`
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
        :param ServiceName: Service name
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ServiceName: str
        :param VersionName: Version name
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type VersionName: str
        :param ClusterIp: Private IP
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ClusterIp: list of str
        :param ExternalIp: Public IP
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ExternalIp: str
        :param Type: The access type. Valid values:
- EXTERNAL (internet access)
- VPC（Intra-VPC access)
- CLUSTER (Intra-cluster access)
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param SubnetId: Subnet ID. It is filled when the access type is `VPC`.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type SubnetId: str
        :param LoadBalanceId: Load balancer ID. It is filled when the access type is `EXTERNAL` or `CLUSTER`. It’s created automatically by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LoadBalanceId: str
        :param PortMappings: Port Mapping
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PortMappings: list of PortMapping
        """
        self.Name = None
        self.Ports = None
        self.Yaml = None
        self.ServiceName = None
        self.VersionName = None
        self.ClusterIp = None
        self.ExternalIp = None
        self.Type = None
        self.SubnetId = None
        self.LoadBalanceId = None
        self.PortMappings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Ports = params.get("Ports")
        self.Yaml = params.get("Yaml")
        self.ServiceName = params.get("ServiceName")
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
        


class GenerateDownloadUrlRequest(AbstractModel):
    """GenerateDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Service ID
        :type ServiceId: str
        :param PkgName: Package Name
        :type PkgName: str
        :param DeployVersion: Version of the package to download
        :type DeployVersion: str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.ServiceId = None
        self.PkgName = None
        self.DeployVersion = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.PkgName = params.get("PkgName")
        self.DeployVersion = params.get("DeployVersion")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDownloadUrlResponse(AbstractModel):
    """GenerateDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param Result: Temp download URL for the package
Note: this field may return `null`, indicating that no valid value can be obtained.
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
    """Health Check Configuration

    """

    def __init__(self):
        r"""
        :param Type: Health check type. Valid values: `HttpGet`，`TcpSocket`，`Exec`
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
        


class IngressInfo(AbstractModel):
    """Ingress configuration

    """

    def __init__(self):
        r"""
        :param NamespaceId: tem namespaceId
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceId: str
        :param EksNamespace: eks namespace
        :type EksNamespace: str
        :param AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param Name: ingress name
        :type Name: str
        :param Rules: Rules configuration
        :type Rules: list of IngressRule
        :param ClbId: clb ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClbId: str
        :param Tls: TLS configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tls: list of IngressTls
        :param ClusterId: eks clusterId
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param Vip: clb ip
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vip: str
        :param CreateTime: Creation time.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type CreateTime: str
        :param Mixed: Whether to listen on both the HTTP Port 80 and HTTPS Port 443. The default value is `false`. The optional value `true` means listening on both the HTTP Port 80 and HTTPS Port 443.
        :type Mixed: bool
        """
        self.NamespaceId = None
        self.EksNamespace = None
        self.AddressIPVersion = None
        self.Name = None
        self.Rules = None
        self.ClbId = None
        self.Tls = None
        self.ClusterId = None
        self.Vip = None
        self.CreateTime = None
        self.Mixed = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.EksNamespace = params.get("EksNamespace")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.Name = params.get("Name")
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
        :type Http: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`
        :param Host: Host address
Note: this field may return null, indicating that no valid values can be obtained.
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
        :type Backend: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`
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
        


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress request structure.

    """

    def __init__(self):
        r"""
        :param Ingress: Ingress rule configuration
        :type Ingress: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
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
        :param Result: Created successfully
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace request structure.

    """

    def __init__(self):
        r"""
        :param NamespaceId: Environment ID
        :type NamespaceId: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param Description: Namespace description
        :type Description: str
        :param Vpc: VPC name
        :type Vpc: str
        :param SubnetIds: Subnet
        :type SubnetIds: list of str
        :param SourceChannel: Source channel
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.NamespaceName = None
        self.Description = None
        self.Vpc = None
        self.SubnetIds = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.Description = params.get("Description")
        self.Vpc = params.get("Vpc")
        self.SubnetIds = params.get("SubnetIds")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace response structure.

    """

    def __init__(self):
        r"""
        :param Result: Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceInfoRequest(AbstractModel):
    """ModifyServiceInfo request structure.

    """

    def __init__(self):
        r"""
        :param ServiceId: Service ID.
        :type ServiceId: str
        :param Description: Description.
        :type Description: str
        :param SourceChannel: Source channel.
        :type SourceChannel: int
        """
        self.ServiceId = None
        self.Description = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Description = params.get("Description")
        self.SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceInfoResponse(AbstractModel):
    """ModifyServiceInfo response structure.

    """

    def __init__(self):
        r"""
        :param Result: Results.
Note: this field may return `null`, indicating that no valid value can be obtained.
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
    """Mounting configuration information

    """

    def __init__(self):
        r"""
        :param ConfigDataName: Configuration Name
        :type ConfigDataName: str
        :param MountedPath: Mount point path
        :type MountedPath: str
        :param Data: Configuration Content
        :type Data: list of Pair
        """
        self.ConfigDataName = None
        self.MountedPath = None
        self.Data = None


    def _deserialize(self, params):
        self.ConfigDataName = params.get("ConfigDataName")
        self.MountedPath = params.get("MountedPath")
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
        


class NamespacePage(AbstractModel):
    """Namespace pagination

    """

    def __init__(self):
        r"""
        :param Records: Records
        :type Records: list of TemNamespaceInfo
        :param Total: Total number
        :type Total: int
        :param Size: Number of items
        :type Size: int
        :param Pages: Number of pages
        :type Pages: int
        """
        self.Records = None
        self.Total = None
        self.Size = None
        self.Pages = None


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pair(AbstractModel):
    """Key-Value pair

    """

    def __init__(self):
        r"""
        :param Key: Key
        :type Key: str
        :param Value: Value
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
        


class PortMapping(AbstractModel):
    """Service port mapping

    """

    def __init__(self):
        r"""
        :param Port: Port.
        :type Port: int
        :param TargetPort: Mapped port.
        :type TargetPort: int
        :param Protocol: TCP/UDP protocol stack.
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
        


class RestartServiceRunPodRequest(AbstractModel):
    """RestartServiceRunPod request structure.

    """

    def __init__(self):
        r"""
        :param NamespaceId: Environment ID.
        :type NamespaceId: str
        :param ServiceId: Service ID.
        :type ServiceId: str
        :param PodName: Pod name.
        :type PodName: str
        :param Limit: Number of items per page.
        :type Limit: int
        :param Offset: Page number.
        :type Offset: int
        :param Status: Pod status.
        :type Status: str
        :param SourceChannel: Source channel.
        :type SourceChannel: int
        """
        self.NamespaceId = None
        self.ServiceId = None
        self.PodName = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.SourceChannel = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ServiceId = params.get("ServiceId")
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
        


class RestartServiceRunPodResponse(AbstractModel):
    """RestartServiceRunPod response structure.

    """

    def __init__(self):
        r"""
        :param Result: Returned results.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """Pod

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
        :param PodIp: Pod IP.
        :type PodIp: str
        :param Zone: Availability zone.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param DeployVersion: Deployed version.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type DeployVersion: str
        :param RestartCount: Number of Restarts
Note: This is field may return `null`, indicating that no valid value can be obtained.
        :type RestartCount: int
        """
        self.Webshell = None
        self.PodId = None
        self.Status = None
        self.CreateTime = None
        self.PodIp = None
        self.Zone = None
        self.DeployVersion = None
        self.RestartCount = None


    def _deserialize(self, params):
        self.Webshell = params.get("Webshell")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.PodIp = params.get("PodIp")
        self.Zone = params.get("Zone")
        self.DeployVersion = params.get("DeployVersion")
        self.RestartCount = params.get("RestartCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
Note: this field may return null, indicating that no valid values can be obtained.
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
        


class TemNamespaceInfo(AbstractModel):
    """Namespace object

    """

    def __init__(self):
        r"""
        :param NamespaceId: Namespace ID
        :type NamespaceId: str
        :param Channel: Channel
        :type Channel: str
        :param NamespaceName: Namespace name
        :type NamespaceName: str
        :param Region: Region name
        :type Region: str
        :param Description: Namespace description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param Status: Status. 1: terminated; 0: normal
        :type Status: int
        :param Vpc: VPC
        :type Vpc: str
        :param CreateDate: Creation time
        :type CreateDate: str
        :param ModifyDate: Modification time
        :type ModifyDate: str
        :param Modifier: Modifier
        :type Modifier: str
        :param Creator: Creator
        :type Creator: str
        :param ServiceNum: Number of services
        :type ServiceNum: int
        :param RunInstancesNum: Number of running instances
        :type RunInstancesNum: int
        :param SubnetId: Subnet
        :type SubnetId: str
        :param TcbEnvStatus: TCB environment status
        :type TcbEnvStatus: str
        :param ClusterStatus: eks cluster status
        :type ClusterStatus: str
        :param EnableTswTraceService: Whether to enable TSW
        :type EnableTswTraceService: bool
        """
        self.NamespaceId = None
        self.Channel = None
        self.NamespaceName = None
        self.Region = None
        self.Description = None
        self.Status = None
        self.Vpc = None
        self.CreateDate = None
        self.ModifyDate = None
        self.Modifier = None
        self.Creator = None
        self.ServiceNum = None
        self.RunInstancesNum = None
        self.SubnetId = None
        self.TcbEnvStatus = None
        self.ClusterStatus = None
        self.EnableTswTraceService = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Channel = params.get("Channel")
        self.NamespaceName = params.get("NamespaceName")
        self.Region = params.get("Region")
        self.Description = params.get("Description")
        self.Status = params.get("Status")
        self.Vpc = params.get("Vpc")
        self.CreateDate = params.get("CreateDate")
        self.ModifyDate = params.get("ModifyDate")
        self.Modifier = params.get("Modifier")
        self.Creator = params.get("Creator")
        self.ServiceNum = params.get("ServiceNum")
        self.RunInstancesNum = params.get("RunInstancesNum")
        self.SubnetId = params.get("SubnetId")
        self.TcbEnvStatus = params.get("TcbEnvStatus")
        self.ClusterStatus = params.get("ClusterStatus")
        self.EnableTswTraceService = params.get("EnableTswTraceService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        