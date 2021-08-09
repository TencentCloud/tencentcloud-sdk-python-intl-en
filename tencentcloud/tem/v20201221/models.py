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
        """
        :param RequestId: Unique request ID\n        :type RequestId: str\n        :param Bucket: Bucket name\n        :type Bucket: str\n        :param Region: Bucket region\n        :type Region: str\n        :param TmpSecretId: `SecretId` of temporary key\n        :type TmpSecretId: str\n        :param TmpSecretKey: `SecretKey` of temporary key\n        :type TmpSecretKey: str\n        :param SessionToken: `sessionToken` of temporary key\n        :type SessionToken: str\n        :param StartTime: `StartTime` of temporary key acquisition\n        :type StartTime: str\n        :param ExpiredTime: `ExpiredTime` of temporary key\n        :type ExpiredTime: str\n        :param FullPath: Full package path\n        :type FullPath: str\n        """
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
        """
        :param ServiceId: Service ID\n        :type ServiceId: str\n        :param PkgName: Package name\n        :type PkgName: str\n        :param OptType: optType. 1: upload; 2: query\n        :type OptType: int\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        :param TimeVersion: Input parameter of `deployVersion`\n        :type TimeVersion: str\n        """
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
        """
        :param Result: `CosToken` object in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param NamespaceName: Namespace name\n        :type NamespaceName: str\n        :param Vpc: VPC name\n        :type Vpc: str\n        :param SubnetIds: Subnet list\n        :type SubnetIds: list of str\n        :param Description: Namespace description\n        :type Description: str\n        :param K8sVersion: K8s version\n        :type K8sVersion: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        :param EnableTswTraceService: Whether to enable the TSW service.\n        :type EnableTswTraceService: bool\n        """
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
        """
        :param Result: Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    """CreateResource request structure.

    """

    def __init__(self):
        """
        :param NamespaceId: Namespace ID\n        :type NamespaceId: str\n        :param ResourceType: Resource type. Valid values: CFS (file system), CLS (log service), TSE_SRE (registry)\n        :type ResourceType: str\n        :param ResourceId: Resource ID\n        :type ResourceId: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Success or failure
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateServiceV2Request(AbstractModel):
    """CreateServiceV2 request structure.

    """

    def __init__(self):
        """
        :param ServiceName: Service name\n        :type ServiceName: str\n        :param Description: Description\n        :type Description: str\n        :param UseDefaultImageService: Whether to use the default image service. 1: yes; 0: no\n        :type UseDefaultImageService: int\n        :param RepoType: Type of the bound repository. 0: Personal Edition; 1: Enterprise Edition\n        :type RepoType: int\n        :param InstanceId: Instance ID of Enterprise Edition image service\n        :type InstanceId: str\n        :param RepoServer: Address of the bound image server\n        :type RepoServer: str\n        :param RepoName: Name of the bound image repository\n        :type RepoName: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        :param SubnetList: Service subnet\n        :type SubnetList: list of str\n        :param CodingLanguage: Programming language 
- JAVA
- OTHER\n        :type CodingLanguage: str\n        :param DeployMode: Deployment mode 
- IMAGE
- JAR
- WAR\n        :type DeployMode: str\n        """
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
        """
        :param Result: Service code\n        :type Result: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteIngressRequest(AbstractModel):
    """DeleteIngress request structure.

    """

    def __init__(self):
        """
        :param NamespaceId: tem NamespaceId\n        :type NamespaceId: str\n        :param EksNamespace: EKS namespace name\n        :type EksNamespace: str\n        :param Name: Ingress rule name\n        :type Name: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Whether deletion succeeded\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployServiceV2Request(AbstractModel):
    """DeployServiceV2 request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Service ID\n        :type ServiceId: str\n        :param ContainerPort: Container port\n        :type ContainerPort: int\n        :param InitPodNum: Number of initialized pods\n        :type InitPodNum: int\n        :param CpuSpec: CPU specification\n        :type CpuSpec: float\n        :param MemorySpec: Memory specification\n        :type MemorySpec: float\n        :param NamespaceId: Environment ID\n        :type NamespaceId: str\n        :param ImgRepo: Image repository\n        :type ImgRepo: str\n        :param VersionDesc: Version description\n        :type VersionDesc: str\n        :param JvmOpts: Launch parameters\n        :type JvmOpts: str\n        :param EsInfo: Auto scaling configuration. If this parameter is left empty, auto scaling will not be enabled\n        :type EsInfo: :class:`tencentcloud.tem.v20201221.models.EsInfo`\n        :param EnvConf: Environment variable configuration\n        :type EnvConf: list of Pair\n        :param LogConfs: Log configuration\n        :type LogConfs: list of str\n        :param StorageConfs: Data volume configuration\n        :type StorageConfs: list of StorageConf\n        :param StorageMountConfs: Data volume mount configuration\n        :type StorageMountConfs: list of StorageMountConf\n        :param DeployMode: Deployment type.
- JAR: deployment through JAR package
- WAR: deployment through WAR package
- IMAGE: deployment through image\n        :type DeployMode: str\n        :param DeployVersion: When the deployment type is `IMAGE`, this parameter indicates the image tag.
When the deployment type is `JAR` or `WAR`, this parameter indicates the package version number.\n        :type DeployVersion: str\n        :param PkgName: Package name, which is required when using JAR or WAR packages for deployment.\n        :type PkgName: str\n        :param JdkVersion: JDK version.
- KONA: use KONA JDK.
- OPEN: use open JDK.\n        :type JdkVersion: str\n        :param SecurityGroupIds: Security group IDs\n        :type SecurityGroupIds: list of str\n        :param LogOutputConf: Log output configuration\n        :type LogOutputConf: :class:`tencentcloud.tem.v20201221.models.LogOutputConf`\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        :param Description: Version description\n        :type Description: str\n        :param ImageCommand: Image command\n        :type ImageCommand: str\n        :param ImageArgs: Image command parameters\n        :type ImageArgs: list of str\n        :param PortMappings: Service port mapping.\n        :type PortMappings: list of PortMapping\n        :param UseRegistryDefaultConfig: Whether to add the registry’s default configurations.\n        :type UseRegistryDefaultConfig: bool\n        :param SettingConfs: Mounting configurations\n        :type SettingConfs: list of MountedSettingConf\n        :param EksService: EKS access configuration\n        :type EksService: :class:`tencentcloud.tem.v20201221.models.EksService`\n        :param VersionId: ID of the version that you want to roll back to\n        :type VersionId: str\n        """
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
        """
        :param Result: Version ID (which can be ignored for the frontend)\n        :type Result: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress request structure.

    """

    def __init__(self):
        """
        :param NamespaceId: tem namespaceId\n        :type NamespaceId: str\n        :param EksNamespace: EKS namespace name\n        :type EksNamespace: str\n        :param Name: Ingress rule name\n        :type Name: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Ingress rule configuration\n        :type Result: :class:`tencentcloud.tem.v20201221.models.IngressInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param NamespaceId: namespace id\n        :type NamespaceId: str\n        :param EksNamespace: namespace\n        :type EksNamespace: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        :param Names: Ingress rule name list.\n        :type Names: list of str\n        """
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
        """
        :param Result: Ingress array
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: list of IngressInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Limit: Number of items per page\n        :type Limit: int\n        :param Offset: Page number\n        :type Offset: int\n        :param SourceChannel: Source\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.tem.v20201221.models.NamespacePage`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param NamespaceId: Environment ID.\n        :type NamespaceId: str\n        :param EksNamespace: EKS namespace.\n        :type EksNamespace: str\n        :param SourceChannel: Source channel.\n        :type SourceChannel: int\n        :param ServiceId: Service ID.\n        :type ServiceId: str\n        """
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
        """
        :param Result: Ingress array.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Result: list of IngressInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Offset: Page number\n        :type Offset: int\n        :param Limit: Number of items per page\n        :type Limit: int\n        :param TotalCount: Total number\n        :type TotalCount: int\n        :param RequestId: Request ID\n        :type RequestId: str\n        :param PodList: Number of items\n        :type PodList: list of RunVersionPod\n        """
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
        """
        :param NamespaceId: Environment ID\n        :type NamespaceId: str\n        :param ServiceId: Service name ID\n        :type ServiceId: str\n        :param Limit: Number of items per page. Default value: 20\n        :type Limit: int\n        :param Offset: Page number. Default value: 0\n        :type Offset: int\n        :param Status: Pod status 
- Running 
- Pending 
- Error\n        :type Status: str\n        :param PodName: Pod name\n        :type PodName: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.tem.v20201221.models.DescribeRunPodPage`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Name: Service name\n        :type Name: str\n        :param Ports: Available ports\n        :type Ports: list of int\n        :param Yaml: Yaml contents\n        :type Yaml: str\n        :param ServiceName: Service name
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type ServiceName: str\n        :param VersionName: Version name
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type VersionName: str\n        :param ClusterIp: Private IP
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type ClusterIp: list of str\n        :param ExternalIp: Public IP
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type ExternalIp: str\n        :param Type: The access type. Valid values:
- EXTERNAL (internet access)
- VPC（Intra-VPC access)
- CLUSTER (Intra-cluster access)
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Type: str\n        :param SubnetId: Subnet ID. It is filled when the access type is `VPC`.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type SubnetId: str\n        :param LoadBalanceId: Load balancer ID. It is filled when the access type is `EXTERNAL` or `CLUSTER`. It’s created automatically by default.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type LoadBalanceId: str\n        :param PortMappings: Port Mapping
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type PortMappings: list of PortMapping\n        """
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
        """
        :param MinAliveInstances: Minimum number of instances\n        :type MinAliveInstances: int\n        :param MaxAliveInstances: Maximum number of instances\n        :type MaxAliveInstances: int\n        :param EsStrategy: Auto scaling policy. 1: CPU; 2: memory\n        :type EsStrategy: int\n        :param Threshold: Auto scaling condition value\n        :type Threshold: int\n        :param VersionId: Version ID\n        :type VersionId: str\n        """
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
        """
        :param ServiceId: Service ID\n        :type ServiceId: str\n        :param PkgName: Package Name\n        :type PkgName: str\n        :param DeployVersion: Version of the package to download\n        :type DeployVersion: str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Temp download URL for the package
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Result: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class IngressInfo(AbstractModel):
    """Ingress configuration

    """

    def __init__(self):
        """
        :param NamespaceId: tem namespaceId
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NamespaceId: str\n        :param EksNamespace: eks namespace\n        :type EksNamespace: str\n        :param AddressIPVersion: ip version\n        :type AddressIPVersion: str\n        :param Name: ingress name\n        :type Name: str\n        :param Rules: Rules configuration\n        :type Rules: list of IngressRule\n        :param ClbId: clb ID
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClbId: str\n        :param Tls: TLS configuration
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tls: list of IngressTls\n        :param ClusterId: eks clusterId
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClusterId: str\n        :param Vip: clb ip
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Vip: str\n        :param CreateTime: Creation time.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type CreateTime: str\n        :param Mixed: Whether to listen on both the HTTP Port 80 and HTTPS Port 443. The default value is `false`. The optional value `true` means listening on both the HTTP Port 80 and HTTPS Port 443.\n        :type Mixed: bool\n        """
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
        """
        :param Http: ingress rule value\n        :type Http: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`\n        :param Host: Host address
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Host: str\n        :param Protocol: Protocol. Options include HTTP and HTTPS. The default option is HTTP.\n        :type Protocol: str\n        """
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
        """
        :param ServiceName: EKS service name\n        :type ServiceName: str\n        :param ServicePort: EKS service port\n        :type ServicePort: int\n        """
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
        """
        :param Path: Path information\n        :type Path: str\n        :param Backend: Backend configuration\n        :type Backend: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`\n        """
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
        """
        :param Paths: Overall rule configuration\n        :type Paths: list of IngressRulePath\n        """
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
        """
        :param Hosts: Host array. An empty array indicates the default certificate for all domain names.\n        :type Hosts: list of str\n        :param SecretName: Secret name. If a certificate is used, this field is left empty.\n        :type SecretName: str\n        :param CertificateId: SSL Certificate Id\n        :type CertificateId: str\n        """
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
        """
        :param OutputType: Log consumer type\n        :type OutputType: str\n        :param ClsLogsetName: CLS logset\n        :type ClsLogsetName: str\n        :param ClsLogTopicId: CLS log topic\n        :type ClsLogTopicId: str\n        :param ClsLogsetId: CLS logset ID\n        :type ClsLogsetId: str\n        :param ClsLogTopicName: CLS log topic name\n        :type ClsLogTopicName: str\n        """
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
        """
        :param Ingress: Ingress rule configuration\n        :type Ingress: :class:`tencentcloud.tem.v20201221.models.IngressInfo`\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Created successfully
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace request structure.

    """

    def __init__(self):
        """
        :param NamespaceId: Environment ID\n        :type NamespaceId: str\n        :param NamespaceName: Namespace name\n        :type NamespaceName: str\n        :param Description: Namespace description\n        :type Description: str\n        :param Vpc: VPC name\n        :type Vpc: str\n        :param SubnetIds: Subnet\n        :type SubnetIds: list of str\n        :param SourceChannel: Source channel\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceInfoRequest(AbstractModel):
    """ModifyServiceInfo request structure.

    """

    def __init__(self):
        """
        :param ServiceId: Service ID.\n        :type ServiceId: str\n        :param Description: Description.\n        :type Description: str\n        :param SourceChannel: Source channel.\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Results.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class MountedSettingConf(AbstractModel):
    """Mounting configuration information

    """

    def __init__(self):
        """
        :param ConfigDataName: Configuration Name\n        :type ConfigDataName: str\n        :param MountedPath: Mount point path\n        :type MountedPath: str\n        :param Data: Configuration Content\n        :type Data: list of Pair\n        """
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
        """
        :param Records: Records\n        :type Records: list of TemNamespaceInfo\n        :param Total: Total number\n        :type Total: int\n        :param Size: Number of items\n        :type Size: int\n        :param Pages: Number of pages\n        :type Pages: int\n        """
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
        """
        :param Key: Key\n        :type Key: str\n        :param Value: Value\n        :type Value: str\n        """
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
        """
        :param Port: Port.\n        :type Port: int\n        :param TargetPort: Mapped port.\n        :type TargetPort: int\n        :param Protocol: TCP/UDP protocol stack.\n        :type Protocol: str\n        """
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
        """
        :param NamespaceId: Environment ID.\n        :type NamespaceId: str\n        :param ServiceId: Service ID.\n        :type ServiceId: str\n        :param PodName: Pod name.\n        :type PodName: str\n        :param Limit: Number of items per page.\n        :type Limit: int\n        :param Offset: Page number.\n        :type Offset: int\n        :param Status: Pod status.\n        :type Status: str\n        :param SourceChannel: Source channel.\n        :type SourceChannel: int\n        """
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
        """
        :param Result: Returned results.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Result: bool\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """Pod

    """

    def __init__(self):
        """
        :param Webshell: Shell address\n        :type Webshell: str\n        :param PodId: Pod ID\n        :type PodId: str\n        :param Status: Status\n        :type Status: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param PodIp: Pod IP.\n        :type PodIp: str\n        :param Zone: Availability zone.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type Zone: str\n        :param DeployVersion: Deployed version.
Note: this field may return `null`, indicating that no valid value can be obtained.\n        :type DeployVersion: str\n        """
        self.Webshell = None
        self.PodId = None
        self.Status = None
        self.CreateTime = None
        self.PodIp = None
        self.Zone = None
        self.DeployVersion = None


    def _deserialize(self, params):
        self.Webshell = params.get("Webshell")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.PodIp = params.get("PodIp")
        self.Zone = params.get("Zone")
        self.DeployVersion = params.get("DeployVersion")
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
        """
        :param StorageVolName: Storage volume name\n        :type StorageVolName: str\n        :param StorageVolPath: Storage volume path\n        :type StorageVolPath: str\n        :param StorageVolIp: Storage volume IP
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StorageVolIp: str\n        """
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
        """
        :param VolumeName: Data volume name\n        :type VolumeName: str\n        :param MountPath: Data volume binding path\n        :type MountPath: str\n        """
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
        """
        :param NamespaceId: Namespace ID\n        :type NamespaceId: str\n        :param Channel: Channel\n        :type Channel: str\n        :param NamespaceName: Namespace name\n        :type NamespaceName: str\n        :param Region: Region name\n        :type Region: str\n        :param Description: Namespace description
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param Status: Status. 1: terminated; 0: normal\n        :type Status: int\n        :param Vpc: VPC\n        :type Vpc: str\n        :param CreateDate: Creation time\n        :type CreateDate: str\n        :param ModifyDate: Modification time\n        :type ModifyDate: str\n        :param Modifier: Modifier\n        :type Modifier: str\n        :param Creator: Creator\n        :type Creator: str\n        :param ServiceNum: Number of services\n        :type ServiceNum: int\n        :param RunInstancesNum: Number of running instances\n        :type RunInstancesNum: int\n        :param SubnetId: Subnet\n        :type SubnetId: str\n        :param TcbEnvStatus: TCB environment status\n        :type TcbEnvStatus: str\n        :param ClusterStatus: eks cluster status\n        :type ClusterStatus: str\n        :param EnableTswTraceService: Whether to enable TSW\n        :type EnableTswTraceService: bool\n        """
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
        