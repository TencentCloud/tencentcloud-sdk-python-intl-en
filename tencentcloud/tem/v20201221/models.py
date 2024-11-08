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
        :param _RequestId: Unique request ID
        :type RequestId: str
        :param _Bucket: Bucket name
        :type Bucket: str
        :param _Region: Bucket region
        :type Region: str
        :param _TmpSecretId: `SecretId` of temporary key
        :type TmpSecretId: str
        :param _TmpSecretKey: `SecretKey` of temporary key
        :type TmpSecretKey: str
        :param _SessionToken: `sessionToken` of temporary key
        :type SessionToken: str
        :param _StartTime: `StartTime` of temporary key acquisition
        :type StartTime: str
        :param _ExpiredTime: `ExpiredTime` of temporary key
        :type ExpiredTime: str
        :param _FullPath: Full package path
        :type FullPath: str
        """
        self._RequestId = None
        self._Bucket = None
        self._Region = None
        self._TmpSecretId = None
        self._TmpSecretKey = None
        self._SessionToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._FullPath = None

    @property
    def RequestId(self):
        """Unique request ID
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Bucket(self):
        """Bucket name
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        """Bucket region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TmpSecretId(self):
        """`SecretId` of temporary key
        :rtype: str
        """
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        """`SecretKey` of temporary key
        :rtype: str
        """
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def SessionToken(self):
        """`sessionToken` of temporary key
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def StartTime(self):
        """`StartTime` of temporary key acquisition
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        """`ExpiredTime` of temporary key
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FullPath(self):
        """Full package path
        :rtype: str
        """
        return self._FullPath

    @FullPath.setter
    def FullPath(self, FullPath):
        self._FullPath = FullPath


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._TmpSecretId = params.get("TmpSecretId")
        self._TmpSecretKey = params.get("TmpSecretKey")
        self._SessionToken = params.get("SessionToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._FullPath = params.get("FullPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenV2Request(AbstractModel):
    """CreateCosTokenV2 request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _PkgName: Package name
        :type PkgName: str
        :param _OptType: optType. 1: upload; 2: query
        :type OptType: int
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _TimeVersion: Input parameter of `deployVersion`
        :type TimeVersion: str
        """
        self._ServiceId = None
        self._PkgName = None
        self._OptType = None
        self._SourceChannel = None
        self._TimeVersion = None

    @property
    def ServiceId(self):
        """Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PkgName(self):
        """Package name
        :rtype: str
        """
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def OptType(self):
        """optType. 1: upload; 2: query
        :rtype: int
        """
        return self._OptType

    @OptType.setter
    def OptType(self, OptType):
        self._OptType = OptType

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def TimeVersion(self):
        """Input parameter of `deployVersion`
        :rtype: str
        """
        return self._TimeVersion

    @TimeVersion.setter
    def TimeVersion(self, TimeVersion):
        self._TimeVersion = TimeVersion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._PkgName = params.get("PkgName")
        self._OptType = params.get("OptType")
        self._SourceChannel = params.get("SourceChannel")
        self._TimeVersion = params.get("TimeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCosTokenV2Response(AbstractModel):
    """CreateCosTokenV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Result: `CosToken` object in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.tem.v20201221.models.CosToken`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """`CosToken` object in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tem.v20201221.models.CosToken`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = CosToken()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _Vpc: VPC name
        :type Vpc: str
        :param _SubnetIds: Subnet list
        :type SubnetIds: list of str
        :param _Description: Namespace description
        :type Description: str
        :param _K8sVersion: K8s version
        :type K8sVersion: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _EnableTswTraceService: Whether to enable the TSW service.
        :type EnableTswTraceService: bool
        """
        self._NamespaceName = None
        self._Vpc = None
        self._SubnetIds = None
        self._Description = None
        self._K8sVersion = None
        self._SourceChannel = None
        self._EnableTswTraceService = None

    @property
    def NamespaceName(self):
        """Namespace name
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Vpc(self):
        """VPC name
        :rtype: str
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        """Subnet list
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Description(self):
        """Namespace description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def K8sVersion(self):
        """K8s version
        :rtype: str
        """
        return self._K8sVersion

    @K8sVersion.setter
    def K8sVersion(self, K8sVersion):
        self._K8sVersion = K8sVersion

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnableTswTraceService(self):
        """Whether to enable the TSW service.
        :rtype: bool
        """
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService


    def _deserialize(self, params):
        self._NamespaceName = params.get("NamespaceName")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._Description = params.get("Description")
        self._K8sVersion = params.get("K8sVersion")
        self._SourceChannel = params.get("SourceChannel")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateResourceRequest(AbstractModel):
    """CreateResource request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: Namespace ID
        :type NamespaceId: str
        :param _ResourceType: Resource type. Valid values: CFS (file system), CLS (log service), TSE_SRE (registry)
        :type ResourceType: str
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._ResourceType = None
        self._ResourceId = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        """Namespace ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ResourceType(self):
        """Resource type. Valid values: CFS (file system), CLS (log service), TSE_SRE (registry)
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        """Resource ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateResourceResponse(AbstractModel):
    """CreateResource response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success or failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Success or failure
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateServiceV2Request(AbstractModel):
    """CreateServiceV2 request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceName: Service name
        :type ServiceName: str
        :param _Description: Description
        :type Description: str
        :param _UseDefaultImageService: Whether to use the default image service. 1: yes; 0: no
        :type UseDefaultImageService: int
        :param _RepoType: Type of the bound repository. 0: Personal Edition; 1: Enterprise Edition
        :type RepoType: int
        :param _InstanceId: Instance ID of Enterprise Edition image service
        :type InstanceId: str
        :param _RepoServer: Address of the bound image server
        :type RepoServer: str
        :param _RepoName: Name of the bound image repository
        :type RepoName: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _SubnetList: Service subnet
        :type SubnetList: list of str
        :param _CodingLanguage: Programming language 
- JAVA
- OTHER
        :type CodingLanguage: str
        :param _DeployMode: Deployment mode 
- IMAGE
- JAR
- WAR
        :type DeployMode: str
        """
        self._ServiceName = None
        self._Description = None
        self._UseDefaultImageService = None
        self._RepoType = None
        self._InstanceId = None
        self._RepoServer = None
        self._RepoName = None
        self._SourceChannel = None
        self._SubnetList = None
        self._CodingLanguage = None
        self._DeployMode = None

    @property
    def ServiceName(self):
        """Service name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UseDefaultImageService(self):
        """Whether to use the default image service. 1: yes; 0: no
        :rtype: int
        """
        return self._UseDefaultImageService

    @UseDefaultImageService.setter
    def UseDefaultImageService(self, UseDefaultImageService):
        self._UseDefaultImageService = UseDefaultImageService

    @property
    def RepoType(self):
        """Type of the bound repository. 0: Personal Edition; 1: Enterprise Edition
        :rtype: int
        """
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def InstanceId(self):
        """Instance ID of Enterprise Edition image service
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepoServer(self):
        """Address of the bound image server
        :rtype: str
        """
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def RepoName(self):
        """Name of the bound image repository
        :rtype: str
        """
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def SubnetList(self):
        """Service subnet
        :rtype: list of str
        """
        return self._SubnetList

    @SubnetList.setter
    def SubnetList(self, SubnetList):
        self._SubnetList = SubnetList

    @property
    def CodingLanguage(self):
        """Programming language 
- JAVA
- OTHER
        :rtype: str
        """
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def DeployMode(self):
        """Deployment mode 
- IMAGE
- JAR
- WAR
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._Description = params.get("Description")
        self._UseDefaultImageService = params.get("UseDefaultImageService")
        self._RepoType = params.get("RepoType")
        self._InstanceId = params.get("InstanceId")
        self._RepoServer = params.get("RepoServer")
        self._RepoName = params.get("RepoName")
        self._SourceChannel = params.get("SourceChannel")
        self._SubnetList = params.get("SubnetList")
        self._CodingLanguage = params.get("CodingLanguage")
        self._DeployMode = params.get("DeployMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceV2Response(AbstractModel):
    """CreateServiceV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Service code
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Service code
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteIngressRequest(AbstractModel):
    """DeleteIngress request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: tem NamespaceId
        :type NamespaceId: str
        :param _EksNamespace: EKS namespace name
        :type EksNamespace: str
        :param _Name: Ingress rule name
        :type Name: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._Name = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        """tem NamespaceId
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        """EKS namespace name
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def Name(self):
        """Ingress rule name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIngressResponse(AbstractModel):
    """DeleteIngress response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether deletion succeeded
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Whether deletion succeeded
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeployServiceV2Request(AbstractModel):
    """DeployServiceV2 request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _ContainerPort: Container port
        :type ContainerPort: int
        :param _InitPodNum: Number of initialized pods
        :type InitPodNum: int
        :param _CpuSpec: CPU specification
        :type CpuSpec: float
        :param _MemorySpec: Memory specification
        :type MemorySpec: float
        :param _NamespaceId: Environment ID
        :type NamespaceId: str
        :param _ImgRepo: Image repository
        :type ImgRepo: str
        :param _VersionDesc: Version description
        :type VersionDesc: str
        :param _JvmOpts: Launch parameters
        :type JvmOpts: str
        :param _EsInfo: Auto scaling configuration. If this parameter is left empty, auto scaling will not be enabled
        :type EsInfo: :class:`tencentcloud.tem.v20201221.models.EsInfo`
        :param _EnvConf: Environment variable configuration
        :type EnvConf: list of Pair
        :param _LogConfs: Log configuration
        :type LogConfs: list of str
        :param _StorageConfs: Data volume configuration
        :type StorageConfs: list of StorageConf
        :param _StorageMountConfs: Data volume mount configuration
        :type StorageMountConfs: list of StorageMountConf
        :param _DeployMode: Deployment type.
- JAR: deployment through JAR package
- WAR: deployment through WAR package
- IMAGE: deployment through image
        :type DeployMode: str
        :param _DeployVersion: When the deployment type is `IMAGE`, this parameter indicates the image tag.
When the deployment type is `JAR` or `WAR`, this parameter indicates the package version number.
        :type DeployVersion: str
        :param _PkgName: Package name, which is required when using JAR or WAR packages for deployment.
        :type PkgName: str
        :param _JdkVersion: JDK version.
- KONA: use KONA JDK.
- OPEN: use open JDK.
        :type JdkVersion: str
        :param _SecurityGroupIds: Security group IDs
        :type SecurityGroupIds: list of str
        :param _LogOutputConf: Log output configuration
        :type LogOutputConf: :class:`tencentcloud.tem.v20201221.models.LogOutputConf`
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _Description: Version description
        :type Description: str
        :param _ImageCommand: Image command
        :type ImageCommand: str
        :param _ImageArgs: Image command parameters
        :type ImageArgs: list of str
        :param _PortMappings: Service port mapping.
        :type PortMappings: list of PortMapping
        :param _UseRegistryDefaultConfig: Whether to add the registry’s default configurations.
        :type UseRegistryDefaultConfig: bool
        :param _SettingConfs: Mounting configurations
        :type SettingConfs: list of MountedSettingConf
        :param _EksService: EKS access configuration
        :type EksService: :class:`tencentcloud.tem.v20201221.models.EksService`
        :param _VersionId: ID of the version that you want to roll back to
        :type VersionId: str
        :param _PostStart: The script to run after startup
        :type PostStart: str
        :param _PreStop: The script to run before stop
        :type PreStop: str
        :param _DeployStrategyConf: Configuration of 
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20201221.models.DeployStrategyConf`
        :param _Liveness: Configuration of aliveness probe
        :type Liveness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        :param _Readiness: Configuration of readiness probe
        :type Readiness: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        self._ServiceId = None
        self._ContainerPort = None
        self._InitPodNum = None
        self._CpuSpec = None
        self._MemorySpec = None
        self._NamespaceId = None
        self._ImgRepo = None
        self._VersionDesc = None
        self._JvmOpts = None
        self._EsInfo = None
        self._EnvConf = None
        self._LogConfs = None
        self._StorageConfs = None
        self._StorageMountConfs = None
        self._DeployMode = None
        self._DeployVersion = None
        self._PkgName = None
        self._JdkVersion = None
        self._SecurityGroupIds = None
        self._LogOutputConf = None
        self._SourceChannel = None
        self._Description = None
        self._ImageCommand = None
        self._ImageArgs = None
        self._PortMappings = None
        self._UseRegistryDefaultConfig = None
        self._SettingConfs = None
        self._EksService = None
        self._VersionId = None
        self._PostStart = None
        self._PreStop = None
        self._DeployStrategyConf = None
        self._Liveness = None
        self._Readiness = None

    @property
    def ServiceId(self):
        """Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ContainerPort(self):
        """Container port
        :rtype: int
        """
        return self._ContainerPort

    @ContainerPort.setter
    def ContainerPort(self, ContainerPort):
        self._ContainerPort = ContainerPort

    @property
    def InitPodNum(self):
        """Number of initialized pods
        :rtype: int
        """
        return self._InitPodNum

    @InitPodNum.setter
    def InitPodNum(self, InitPodNum):
        self._InitPodNum = InitPodNum

    @property
    def CpuSpec(self):
        """CPU specification
        :rtype: float
        """
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def MemorySpec(self):
        """Memory specification
        :rtype: float
        """
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def NamespaceId(self):
        """Environment ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ImgRepo(self):
        """Image repository
        :rtype: str
        """
        return self._ImgRepo

    @ImgRepo.setter
    def ImgRepo(self, ImgRepo):
        self._ImgRepo = ImgRepo

    @property
    def VersionDesc(self):
        """Version description
        :rtype: str
        """
        return self._VersionDesc

    @VersionDesc.setter
    def VersionDesc(self, VersionDesc):
        self._VersionDesc = VersionDesc

    @property
    def JvmOpts(self):
        """Launch parameters
        :rtype: str
        """
        return self._JvmOpts

    @JvmOpts.setter
    def JvmOpts(self, JvmOpts):
        self._JvmOpts = JvmOpts

    @property
    def EsInfo(self):
        """Auto scaling configuration. If this parameter is left empty, auto scaling will not be enabled
        :rtype: :class:`tencentcloud.tem.v20201221.models.EsInfo`
        """
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def EnvConf(self):
        """Environment variable configuration
        :rtype: list of Pair
        """
        return self._EnvConf

    @EnvConf.setter
    def EnvConf(self, EnvConf):
        self._EnvConf = EnvConf

    @property
    def LogConfs(self):
        """Log configuration
        :rtype: list of str
        """
        return self._LogConfs

    @LogConfs.setter
    def LogConfs(self, LogConfs):
        self._LogConfs = LogConfs

    @property
    def StorageConfs(self):
        """Data volume configuration
        :rtype: list of StorageConf
        """
        return self._StorageConfs

    @StorageConfs.setter
    def StorageConfs(self, StorageConfs):
        self._StorageConfs = StorageConfs

    @property
    def StorageMountConfs(self):
        """Data volume mount configuration
        :rtype: list of StorageMountConf
        """
        return self._StorageMountConfs

    @StorageMountConfs.setter
    def StorageMountConfs(self, StorageMountConfs):
        self._StorageMountConfs = StorageMountConfs

    @property
    def DeployMode(self):
        """Deployment type.
- JAR: deployment through JAR package
- WAR: deployment through WAR package
- IMAGE: deployment through image
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def DeployVersion(self):
        """When the deployment type is `IMAGE`, this parameter indicates the image tag.
When the deployment type is `JAR` or `WAR`, this parameter indicates the package version number.
        :rtype: str
        """
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PkgName(self):
        """Package name, which is required when using JAR or WAR packages for deployment.
        :rtype: str
        """
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def JdkVersion(self):
        """JDK version.
- KONA: use KONA JDK.
- OPEN: use open JDK.
        :rtype: str
        """
        return self._JdkVersion

    @JdkVersion.setter
    def JdkVersion(self, JdkVersion):
        self._JdkVersion = JdkVersion

    @property
    def SecurityGroupIds(self):
        """Security group IDs
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LogOutputConf(self):
        """Log output configuration
        :rtype: :class:`tencentcloud.tem.v20201221.models.LogOutputConf`
        """
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Description(self):
        """Version description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ImageCommand(self):
        """Image command
        :rtype: str
        """
        return self._ImageCommand

    @ImageCommand.setter
    def ImageCommand(self, ImageCommand):
        self._ImageCommand = ImageCommand

    @property
    def ImageArgs(self):
        """Image command parameters
        :rtype: list of str
        """
        return self._ImageArgs

    @ImageArgs.setter
    def ImageArgs(self, ImageArgs):
        self._ImageArgs = ImageArgs

    @property
    def PortMappings(self):
        """Service port mapping.
        :rtype: list of PortMapping
        """
        return self._PortMappings

    @PortMappings.setter
    def PortMappings(self, PortMappings):
        self._PortMappings = PortMappings

    @property
    def UseRegistryDefaultConfig(self):
        """Whether to add the registry’s default configurations.
        :rtype: bool
        """
        return self._UseRegistryDefaultConfig

    @UseRegistryDefaultConfig.setter
    def UseRegistryDefaultConfig(self, UseRegistryDefaultConfig):
        self._UseRegistryDefaultConfig = UseRegistryDefaultConfig

    @property
    def SettingConfs(self):
        """Mounting configurations
        :rtype: list of MountedSettingConf
        """
        return self._SettingConfs

    @SettingConfs.setter
    def SettingConfs(self, SettingConfs):
        self._SettingConfs = SettingConfs

    @property
    def EksService(self):
        """EKS access configuration
        :rtype: :class:`tencentcloud.tem.v20201221.models.EksService`
        """
        return self._EksService

    @EksService.setter
    def EksService(self, EksService):
        self._EksService = EksService

    @property
    def VersionId(self):
        """ID of the version that you want to roll back to
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def PostStart(self):
        """The script to run after startup
        :rtype: str
        """
        return self._PostStart

    @PostStart.setter
    def PostStart(self, PostStart):
        self._PostStart = PostStart

    @property
    def PreStop(self):
        """The script to run before stop
        :rtype: str
        """
        return self._PreStop

    @PreStop.setter
    def PreStop(self, PreStop):
        self._PreStop = PreStop

    @property
    def DeployStrategyConf(self):
        """Configuration of 
        :rtype: :class:`tencentcloud.tem.v20201221.models.DeployStrategyConf`
        """
        return self._DeployStrategyConf

    @DeployStrategyConf.setter
    def DeployStrategyConf(self, DeployStrategyConf):
        self._DeployStrategyConf = DeployStrategyConf

    @property
    def Liveness(self):
        """Configuration of aliveness probe
        :rtype: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        return self._Liveness

    @Liveness.setter
    def Liveness(self, Liveness):
        self._Liveness = Liveness

    @property
    def Readiness(self):
        """Configuration of readiness probe
        :rtype: :class:`tencentcloud.tem.v20201221.models.HealthCheckConfig`
        """
        return self._Readiness

    @Readiness.setter
    def Readiness(self, Readiness):
        self._Readiness = Readiness


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ContainerPort = params.get("ContainerPort")
        self._InitPodNum = params.get("InitPodNum")
        self._CpuSpec = params.get("CpuSpec")
        self._MemorySpec = params.get("MemorySpec")
        self._NamespaceId = params.get("NamespaceId")
        self._ImgRepo = params.get("ImgRepo")
        self._VersionDesc = params.get("VersionDesc")
        self._JvmOpts = params.get("JvmOpts")
        if params.get("EsInfo") is not None:
            self._EsInfo = EsInfo()
            self._EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self._EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self._EnvConf.append(obj)
        self._LogConfs = params.get("LogConfs")
        if params.get("StorageConfs") is not None:
            self._StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self._StorageConfs.append(obj)
        if params.get("StorageMountConfs") is not None:
            self._StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self._StorageMountConfs.append(obj)
        self._DeployMode = params.get("DeployMode")
        self._DeployVersion = params.get("DeployVersion")
        self._PkgName = params.get("PkgName")
        self._JdkVersion = params.get("JdkVersion")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LogOutputConf") is not None:
            self._LogOutputConf = LogOutputConf()
            self._LogOutputConf._deserialize(params.get("LogOutputConf"))
        self._SourceChannel = params.get("SourceChannel")
        self._Description = params.get("Description")
        self._ImageCommand = params.get("ImageCommand")
        self._ImageArgs = params.get("ImageArgs")
        if params.get("PortMappings") is not None:
            self._PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self._PortMappings.append(obj)
        self._UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self._SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self._SettingConfs.append(obj)
        if params.get("EksService") is not None:
            self._EksService = EksService()
            self._EksService._deserialize(params.get("EksService"))
        self._VersionId = params.get("VersionId")
        self._PostStart = params.get("PostStart")
        self._PreStop = params.get("PreStop")
        if params.get("DeployStrategyConf") is not None:
            self._DeployStrategyConf = DeployStrategyConf()
            self._DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("Liveness") is not None:
            self._Liveness = HealthCheckConfig()
            self._Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self._Readiness = HealthCheckConfig()
            self._Readiness._deserialize(params.get("Readiness"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployServiceV2Response(AbstractModel):
    """DeployServiceV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Version ID (which can be ignored for the frontend)
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Version ID (which can be ignored for the frontend)
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeployStrategyConf(AbstractModel):
    """Configuration of batch release policies

    """

    def __init__(self):
        r"""
        :param _TotalBatchCount: Total batches
        :type TotalBatchCount: int
        :param _BetaBatchNum: Number of instances for the beta batch
        :type BetaBatchNum: int
        :param _DeployStrategyType: Batch deploy policy. `0`: automatically; `1`: manually. If you use beta batch, the policy for beta batch must be `0`. The policy specified here only applies to the rest batches.
        :type DeployStrategyType: int
        :param _BatchInterval: Interval between batches
        :type BatchInterval: int
        """
        self._TotalBatchCount = None
        self._BetaBatchNum = None
        self._DeployStrategyType = None
        self._BatchInterval = None

    @property
    def TotalBatchCount(self):
        """Total batches
        :rtype: int
        """
        return self._TotalBatchCount

    @TotalBatchCount.setter
    def TotalBatchCount(self, TotalBatchCount):
        self._TotalBatchCount = TotalBatchCount

    @property
    def BetaBatchNum(self):
        """Number of instances for the beta batch
        :rtype: int
        """
        return self._BetaBatchNum

    @BetaBatchNum.setter
    def BetaBatchNum(self, BetaBatchNum):
        self._BetaBatchNum = BetaBatchNum

    @property
    def DeployStrategyType(self):
        """Batch deploy policy. `0`: automatically; `1`: manually. If you use beta batch, the policy for beta batch must be `0`. The policy specified here only applies to the rest batches.
        :rtype: int
        """
        return self._DeployStrategyType

    @DeployStrategyType.setter
    def DeployStrategyType(self, DeployStrategyType):
        self._DeployStrategyType = DeployStrategyType

    @property
    def BatchInterval(self):
        """Interval between batches
        :rtype: int
        """
        return self._BatchInterval

    @BatchInterval.setter
    def BatchInterval(self, BatchInterval):
        self._BatchInterval = BatchInterval


    def _deserialize(self, params):
        self._TotalBatchCount = params.get("TotalBatchCount")
        self._BetaBatchNum = params.get("BetaBatchNum")
        self._DeployStrategyType = params.get("DeployStrategyType")
        self._BatchInterval = params.get("BatchInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: tem namespaceId
        :type NamespaceId: str
        :param _EksNamespace: EKS namespace name
        :type EksNamespace: str
        :param _Name: Ingress rule name
        :type Name: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._Name = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        """tem namespaceId
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        """EKS namespace name
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def Name(self):
        """Ingress rule name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressResponse(AbstractModel):
    """DescribeIngress response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Ingress rule configuration
        :type Result: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Ingress rule configuration
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = IngressInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIngressesRequest(AbstractModel):
    """DescribeIngresses request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: namespace id
        :type NamespaceId: str
        :param _EksNamespace: namespace
        :type EksNamespace: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _Names: Ingress rule name list.
        :type Names: list of str
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._SourceChannel = None
        self._Names = None

    @property
    def NamespaceId(self):
        """namespace id
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        """namespace
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Names(self):
        """Ingress rule name list.
        :rtype: list of str
        """
        return self._Names

    @Names.setter
    def Names(self, Names):
        self._Names = Names


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIngressesResponse(AbstractModel):
    """DescribeIngresses response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Ingress array
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: list of IngressInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Ingress array
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of IngressInfo
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of items per page
        :type Limit: int
        :param _Offset: Page number
        :type Offset: int
        :param _SourceChannel: Source
        :type SourceChannel: int
        """
        self._Limit = None
        self._Offset = None
        self._SourceChannel = None

    @property
    def Limit(self):
        """Number of items per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SourceChannel(self):
        """Source
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20201221.models.NamespacePage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.tem.v20201221.models.NamespacePage`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = NamespacePage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeRelatedIngressesRequest(AbstractModel):
    """DescribeRelatedIngresses request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: Environment ID.
        :type NamespaceId: str
        :param _EksNamespace: EKS namespace.
        :type EksNamespace: str
        :param _SourceChannel: Source channel.
        :type SourceChannel: int
        :param _ServiceId: Service ID.
        :type ServiceId: str
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._SourceChannel = None
        self._ServiceId = None

    @property
    def NamespaceId(self):
        """Environment ID.
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        """EKS namespace.
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def SourceChannel(self):
        """Source channel.
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ServiceId(self):
        """Service ID.
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelatedIngressesResponse(AbstractModel):
    """DescribeRelatedIngresses response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Ingress array.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Result: list of IngressInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Ingress array.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of IngressInfo
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = IngressInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunPodPage(AbstractModel):
    """Version pod list

    """

    def __init__(self):
        r"""
        :param _Offset: Page number
        :type Offset: int
        :param _Limit: Number of items per page
        :type Limit: int
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _RequestId: Request ID
        :type RequestId: str
        :param _PodList: Number of items
        :type PodList: list of RunVersionPod
        """
        self._Offset = None
        self._Limit = None
        self._TotalCount = None
        self._RequestId = None
        self._PodList = None

    @property
    def Offset(self):
        """Page number
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of items per page
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """Request ID
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def PodList(self):
        """Number of items
        :rtype: list of RunVersionPod
        """
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")
        if params.get("PodList") is not None:
            self._PodList = []
            for item in params.get("PodList"):
                obj = RunVersionPod()
                obj._deserialize(item)
                self._PodList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceRunPodListV2Request(AbstractModel):
    """DescribeServiceRunPodListV2 request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: Environment ID
        :type NamespaceId: str
        :param _ServiceId: Service name ID
        :type ServiceId: str
        :param _Limit: Number of items per page. Default value: 20
        :type Limit: int
        :param _Offset: Page number. Default value: 0
        :type Offset: int
        :param _Status: Pod status 
- Running 
- Pending 
- Error
        :type Status: str
        :param _PodName: Pod name
        :type PodName: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._ServiceId = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._PodName = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        """Environment ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ServiceId(self):
        """Service name ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        """Number of items per page. Default value: 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number. Default value: 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        """Pod status 
- Running 
- Pending 
- Error
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PodName(self):
        """Pod name
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._PodName = params.get("PodName")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceRunPodListV2Response(AbstractModel):
    """DescribeServiceRunPodListV2 response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20201221.models.DescribeRunPodPage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned result
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeRunPodPage`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        if params.get("Result") is not None:
            self._Result = DescribeRunPodPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class EksService(AbstractModel):
    """EKS service information

    """

    def __init__(self):
        r"""
        :param _Name: Service name
        :type Name: str
        :param _Ports: Available ports
        :type Ports: list of int
        :param _Yaml: Yaml contents
        :type Yaml: str
        :param _ServiceName: Service name
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ServiceName: str
        :param _VersionName: Version name
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type VersionName: str
        :param _ClusterIp: Private IP
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ClusterIp: list of str
        :param _ExternalIp: Public IP
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ExternalIp: str
        :param _Type: The access type. Valid values:
- EXTERNAL (internet access)
- VPC（Intra-VPC access)
- CLUSTER (Intra-cluster access)
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param _SubnetId: Subnet ID. It is filled when the access type is `VPC`.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type SubnetId: str
        :param _LoadBalanceId: Load balancer ID. It is filled when the access type is `EXTERNAL` or `CLUSTER`. It’s created automatically by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LoadBalanceId: str
        :param _PortMappings: Port Mapping
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PortMappings: list of PortMapping
        """
        self._Name = None
        self._Ports = None
        self._Yaml = None
        self._ServiceName = None
        self._VersionName = None
        self._ClusterIp = None
        self._ExternalIp = None
        self._Type = None
        self._SubnetId = None
        self._LoadBalanceId = None
        self._PortMappings = None

    @property
    def Name(self):
        """Service name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ports(self):
        """Available ports
        :rtype: list of int
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Yaml(self):
        """Yaml contents
        :rtype: str
        """
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def ServiceName(self):
        """Service name
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def VersionName(self):
        """Version name
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ClusterIp(self):
        """Private IP
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of str
        """
        return self._ClusterIp

    @ClusterIp.setter
    def ClusterIp(self, ClusterIp):
        self._ClusterIp = ClusterIp

    @property
    def ExternalIp(self):
        """Public IP
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._ExternalIp

    @ExternalIp.setter
    def ExternalIp(self, ExternalIp):
        self._ExternalIp = ExternalIp

    @property
    def Type(self):
        """The access type. Valid values:
- EXTERNAL (internet access)
- VPC（Intra-VPC access)
- CLUSTER (Intra-cluster access)
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubnetId(self):
        """Subnet ID. It is filled when the access type is `VPC`.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LoadBalanceId(self):
        """Load balancer ID. It is filled when the access type is `EXTERNAL` or `CLUSTER`. It’s created automatically by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._LoadBalanceId

    @LoadBalanceId.setter
    def LoadBalanceId(self, LoadBalanceId):
        self._LoadBalanceId = LoadBalanceId

    @property
    def PortMappings(self):
        """Port Mapping
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of PortMapping
        """
        return self._PortMappings

    @PortMappings.setter
    def PortMappings(self, PortMappings):
        self._PortMappings = PortMappings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Ports = params.get("Ports")
        self._Yaml = params.get("Yaml")
        self._ServiceName = params.get("ServiceName")
        self._VersionName = params.get("VersionName")
        self._ClusterIp = params.get("ClusterIp")
        self._ExternalIp = params.get("ExternalIp")
        self._Type = params.get("Type")
        self._SubnetId = params.get("SubnetId")
        self._LoadBalanceId = params.get("LoadBalanceId")
        if params.get("PortMappings") is not None:
            self._PortMappings = []
            for item in params.get("PortMappings"):
                obj = PortMapping()
                obj._deserialize(item)
                self._PortMappings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EsInfo(AbstractModel):
    """Auto scaling configuration

    """

    def __init__(self):
        r"""
        :param _MinAliveInstances: Minimum number of instances
        :type MinAliveInstances: int
        :param _MaxAliveInstances: Maximum number of instances
        :type MaxAliveInstances: int
        :param _EsStrategy: Auto scaling policy. 1: CPU; 2: memory
        :type EsStrategy: int
        :param _Threshold: Auto scaling condition value
        :type Threshold: int
        :param _VersionId: Version ID
        :type VersionId: str
        """
        self._MinAliveInstances = None
        self._MaxAliveInstances = None
        self._EsStrategy = None
        self._Threshold = None
        self._VersionId = None

    @property
    def MinAliveInstances(self):
        """Minimum number of instances
        :rtype: int
        """
        return self._MinAliveInstances

    @MinAliveInstances.setter
    def MinAliveInstances(self, MinAliveInstances):
        self._MinAliveInstances = MinAliveInstances

    @property
    def MaxAliveInstances(self):
        """Maximum number of instances
        :rtype: int
        """
        return self._MaxAliveInstances

    @MaxAliveInstances.setter
    def MaxAliveInstances(self, MaxAliveInstances):
        self._MaxAliveInstances = MaxAliveInstances

    @property
    def EsStrategy(self):
        """Auto scaling policy. 1: CPU; 2: memory
        :rtype: int
        """
        return self._EsStrategy

    @EsStrategy.setter
    def EsStrategy(self, EsStrategy):
        self._EsStrategy = EsStrategy

    @property
    def Threshold(self):
        """Auto scaling condition value
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def VersionId(self):
        """Version ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._MinAliveInstances = params.get("MinAliveInstances")
        self._MaxAliveInstances = params.get("MaxAliveInstances")
        self._EsStrategy = params.get("EsStrategy")
        self._Threshold = params.get("Threshold")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDownloadUrlRequest(AbstractModel):
    """GenerateDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID
        :type ServiceId: str
        :param _PkgName: Package Name
        :type PkgName: str
        :param _DeployVersion: Version of the package to download
        :type DeployVersion: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._ServiceId = None
        self._PkgName = None
        self._DeployVersion = None
        self._SourceChannel = None

    @property
    def ServiceId(self):
        """Service ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PkgName(self):
        """Package Name
        :rtype: str
        """
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def DeployVersion(self):
        """Version of the package to download
        :rtype: str
        """
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._PkgName = params.get("PkgName")
        self._DeployVersion = params.get("DeployVersion")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDownloadUrlResponse(AbstractModel):
    """GenerateDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Temp download URL for the package
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Temp download URL for the package
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class HealthCheckConfig(AbstractModel):
    """Health Check Configuration

    """

    def __init__(self):
        r"""
        :param _Type: Health check type. Valid values: `HttpGet`，`TcpSocket`，`Exec`
        :type Type: str
        :param _Protocol: The protocol type. It’s only valid when the health check type is `HttpGet`.
        :type Protocol: str
        :param _Path: The request path. It’s only valid when the health check type is `HttpGet`.
        :type Path: str
        :param _Exec: The script to be executed. It’s only valid when the health check type is `Exec`.
        :type Exec: str
        :param _Port: The request port. It’s only valid when the health check type is `HttpGet` or `TcpSocket `.
        :type Port: int
        :param _InitialDelaySeconds: The initial delay for health check in seconds. Default: `0`
        :type InitialDelaySeconds: int
        :param _TimeoutSeconds: Timeout period in seconds. Default: `1`
        :type TimeoutSeconds: int
        :param _PeriodSeconds: Interval period in seconds. Default: `10`
        :type PeriodSeconds: int
        """
        self._Type = None
        self._Protocol = None
        self._Path = None
        self._Exec = None
        self._Port = None
        self._InitialDelaySeconds = None
        self._TimeoutSeconds = None
        self._PeriodSeconds = None

    @property
    def Type(self):
        """Health check type. Valid values: `HttpGet`，`TcpSocket`，`Exec`
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Protocol(self):
        """The protocol type. It’s only valid when the health check type is `HttpGet`.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        """The request path. It’s only valid when the health check type is `HttpGet`.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Exec(self):
        """The script to be executed. It’s only valid when the health check type is `Exec`.
        :rtype: str
        """
        return self._Exec

    @Exec.setter
    def Exec(self, Exec):
        self._Exec = Exec

    @property
    def Port(self):
        """The request port. It’s only valid when the health check type is `HttpGet` or `TcpSocket `.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InitialDelaySeconds(self):
        """The initial delay for health check in seconds. Default: `0`
        :rtype: int
        """
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def TimeoutSeconds(self):
        """Timeout period in seconds. Default: `1`
        :rtype: int
        """
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def PeriodSeconds(self):
        """Interval period in seconds. Default: `10`
        :rtype: int
        """
        return self._PeriodSeconds

    @PeriodSeconds.setter
    def PeriodSeconds(self, PeriodSeconds):
        self._PeriodSeconds = PeriodSeconds


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Protocol = params.get("Protocol")
        self._Path = params.get("Path")
        self._Exec = params.get("Exec")
        self._Port = params.get("Port")
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._TimeoutSeconds = params.get("TimeoutSeconds")
        self._PeriodSeconds = params.get("PeriodSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressInfo(AbstractModel):
    """Ingress configuration

    """

    def __init__(self):
        r"""
        :param _NamespaceId: tem namespaceId
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceId: str
        :param _EksNamespace: eks namespace
        :type EksNamespace: str
        :param _AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param _Name: ingress name
        :type Name: str
        :param _Rules: Rules configuration
        :type Rules: list of IngressRule
        :param _ClbId: clb ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClbId: str
        :param _Tls: TLS configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tls: list of IngressTls
        :param _ClusterId: eks clusterId
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _Vip: clb ip
Note: this field may return null, indicating that no valid values can be obtained.
        :type Vip: str
        :param _CreateTime: Creation time.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type CreateTime: str
        :param _Mixed: Whether to listen on both the HTTP Port 80 and HTTPS Port 443. The default value is `false`. The optional value `true` means listening on both the HTTP Port 80 and HTTPS Port 443.
        :type Mixed: bool
        """
        self._NamespaceId = None
        self._EksNamespace = None
        self._AddressIPVersion = None
        self._Name = None
        self._Rules = None
        self._ClbId = None
        self._Tls = None
        self._ClusterId = None
        self._Vip = None
        self._CreateTime = None
        self._Mixed = None

    @property
    def NamespaceId(self):
        """tem namespaceId
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def EksNamespace(self):
        """eks namespace
        :rtype: str
        """
        return self._EksNamespace

    @EksNamespace.setter
    def EksNamespace(self, EksNamespace):
        self._EksNamespace = EksNamespace

    @property
    def AddressIPVersion(self):
        """ip version
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def Name(self):
        """ingress name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rules(self):
        """Rules configuration
        :rtype: list of IngressRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ClbId(self):
        """clb ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClbId

    @ClbId.setter
    def ClbId(self, ClbId):
        self._ClbId = ClbId

    @property
    def Tls(self):
        """TLS configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of IngressTls
        """
        return self._Tls

    @Tls.setter
    def Tls(self, Tls):
        self._Tls = Tls

    @property
    def ClusterId(self):
        """eks clusterId
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Vip(self):
        """clb ip
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def CreateTime(self):
        """Creation time.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Mixed(self):
        """Whether to listen on both the HTTP Port 80 and HTTPS Port 443. The default value is `false`. The optional value `true` means listening on both the HTTP Port 80 and HTTPS Port 443.
        :rtype: bool
        """
        return self._Mixed

    @Mixed.setter
    def Mixed(self, Mixed):
        self._Mixed = Mixed


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._EksNamespace = params.get("EksNamespace")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._Name = params.get("Name")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = IngressRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ClbId = params.get("ClbId")
        if params.get("Tls") is not None:
            self._Tls = []
            for item in params.get("Tls"):
                obj = IngressTls()
                obj._deserialize(item)
                self._Tls.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._Vip = params.get("Vip")
        self._CreateTime = params.get("CreateTime")
        self._Mixed = params.get("Mixed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRule(AbstractModel):
    """Ingress rule configuration

    """

    def __init__(self):
        r"""
        :param _Http: ingress rule value
        :type Http: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`
        :param _Host: Host address
Note: this field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param _Protocol: Protocol. Options include HTTP and HTTPS. The default option is HTTP.
        :type Protocol: str
        """
        self._Http = None
        self._Host = None
        self._Protocol = None

    @property
    def Http(self):
        """ingress rule value
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressRuleValue`
        """
        return self._Http

    @Http.setter
    def Http(self, Http):
        self._Http = Http

    @property
    def Host(self):
        """Host address
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Protocol(self):
        """Protocol. Options include HTTP and HTTPS. The default option is HTTP.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        if params.get("Http") is not None:
            self._Http = IngressRuleValue()
            self._Http._deserialize(params.get("Http"))
        self._Host = params.get("Host")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleBackend(AbstractModel):
    """Ingress rule backend configuration

    """

    def __init__(self):
        r"""
        :param _ServiceName: EKS service name
        :type ServiceName: str
        :param _ServicePort: EKS service port
        :type ServicePort: int
        """
        self._ServiceName = None
        self._ServicePort = None

    @property
    def ServiceName(self):
        """EKS service name
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServicePort(self):
        """EKS service port
        :rtype: int
        """
        return self._ServicePort

    @ServicePort.setter
    def ServicePort(self, ServicePort):
        self._ServicePort = ServicePort


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._ServicePort = params.get("ServicePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRulePath(AbstractModel):
    """Ingress rule path configuration

    """

    def __init__(self):
        r"""
        :param _Path: Path information
        :type Path: str
        :param _Backend: Backend configuration
        :type Backend: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`
        """
        self._Path = None
        self._Backend = None

    @property
    def Path(self):
        """Path information
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Backend(self):
        """Backend configuration
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressRuleBackend`
        """
        return self._Backend

    @Backend.setter
    def Backend(self, Backend):
        self._Backend = Backend


    def _deserialize(self, params):
        self._Path = params.get("Path")
        if params.get("Backend") is not None:
            self._Backend = IngressRuleBackend()
            self._Backend._deserialize(params.get("Backend"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressRuleValue(AbstractModel):
    """Ingress rule value configuration

    """

    def __init__(self):
        r"""
        :param _Paths: Overall rule configuration
        :type Paths: list of IngressRulePath
        """
        self._Paths = None

    @property
    def Paths(self):
        """Overall rule configuration
        :rtype: list of IngressRulePath
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        if params.get("Paths") is not None:
            self._Paths = []
            for item in params.get("Paths"):
                obj = IngressRulePath()
                obj._deserialize(item)
                self._Paths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressTls(AbstractModel):
    """Ingress TLS configuration

    """

    def __init__(self):
        r"""
        :param _Hosts: Host array. An empty array indicates the default certificate for all domain names.
        :type Hosts: list of str
        :param _SecretName: Secret name. If a certificate is used, this field is left empty.
        :type SecretName: str
        :param _CertificateId: SSL Certificate Id
        :type CertificateId: str
        """
        self._Hosts = None
        self._SecretName = None
        self._CertificateId = None

    @property
    def Hosts(self):
        """Host array. An empty array indicates the default certificate for all domain names.
        :rtype: list of str
        """
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def SecretName(self):
        """Secret name. If a certificate is used, this field is left empty.
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def CertificateId(self):
        """SSL Certificate Id
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._Hosts = params.get("Hosts")
        self._SecretName = params.get("SecretName")
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogOutputConf(AbstractModel):
    """Log output configuration

    """

    def __init__(self):
        r"""
        :param _OutputType: Log consumer type
        :type OutputType: str
        :param _ClsLogsetName: CLS logset
        :type ClsLogsetName: str
        :param _ClsLogTopicId: CLS log topic
        :type ClsLogTopicId: str
        :param _ClsLogsetId: CLS logset ID
        :type ClsLogsetId: str
        :param _ClsLogTopicName: CLS log topic name
        :type ClsLogTopicName: str
        """
        self._OutputType = None
        self._ClsLogsetName = None
        self._ClsLogTopicId = None
        self._ClsLogsetId = None
        self._ClsLogTopicName = None

    @property
    def OutputType(self):
        """Log consumer type
        :rtype: str
        """
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def ClsLogsetName(self):
        """CLS logset
        :rtype: str
        """
        return self._ClsLogsetName

    @ClsLogsetName.setter
    def ClsLogsetName(self, ClsLogsetName):
        self._ClsLogsetName = ClsLogsetName

    @property
    def ClsLogTopicId(self):
        """CLS log topic
        :rtype: str
        """
        return self._ClsLogTopicId

    @ClsLogTopicId.setter
    def ClsLogTopicId(self, ClsLogTopicId):
        self._ClsLogTopicId = ClsLogTopicId

    @property
    def ClsLogsetId(self):
        """CLS logset ID
        :rtype: str
        """
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsLogTopicName(self):
        """CLS log topic name
        :rtype: str
        """
        return self._ClsLogTopicName

    @ClsLogTopicName.setter
    def ClsLogTopicName(self, ClsLogTopicName):
        self._ClsLogTopicName = ClsLogTopicName


    def _deserialize(self, params):
        self._OutputType = params.get("OutputType")
        self._ClsLogsetName = params.get("ClsLogsetName")
        self._ClsLogTopicId = params.get("ClsLogTopicId")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._ClsLogTopicName = params.get("ClsLogTopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress request structure.

    """

    def __init__(self):
        r"""
        :param _Ingress: Ingress rule configuration
        :type Ingress: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._Ingress = None
        self._SourceChannel = None

    @property
    def Ingress(self):
        """Ingress rule configuration
        :rtype: :class:`tencentcloud.tem.v20201221.models.IngressInfo`
        """
        return self._Ingress

    @Ingress.setter
    def Ingress(self, Ingress):
        self._Ingress = Ingress

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self._Ingress = IngressInfo()
            self._Ingress._deserialize(params.get("Ingress"))
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIngressResponse(AbstractModel):
    """ModifyIngress response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Created successfully
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Created successfully
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: Environment ID
        :type NamespaceId: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _Description: Namespace description
        :type Description: str
        :param _Vpc: VPC name
        :type Vpc: str
        :param _SubnetIds: Subnet
        :type SubnetIds: list of str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._NamespaceName = None
        self._Description = None
        self._Vpc = None
        self._SubnetIds = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        """Environment ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def NamespaceName(self):
        """Namespace name
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Description(self):
        """Namespace description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vpc(self):
        """VPC name
        :rtype: str
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        """Subnet
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SourceChannel(self):
        """Source channel
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._NamespaceName = params.get("NamespaceName")
        self._Description = params.get("Description")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Namespace ID in case of success and `null` in case of failure
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyServiceInfoRequest(AbstractModel):
    """ModifyServiceInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ServiceId: Service ID.
        :type ServiceId: str
        :param _Description: Description.
        :type Description: str
        :param _SourceChannel: Source channel.
        :type SourceChannel: int
        """
        self._ServiceId = None
        self._Description = None
        self._SourceChannel = None

    @property
    def ServiceId(self):
        """Service ID.
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Description(self):
        """Description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SourceChannel(self):
        """Source channel.
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Description = params.get("Description")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceInfoResponse(AbstractModel):
    """ModifyServiceInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Results.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Results.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class MountedSettingConf(AbstractModel):
    """Mounting configuration information

    """

    def __init__(self):
        r"""
        :param _ConfigDataName: Configuration Name
        :type ConfigDataName: str
        :param _MountedPath: Mount point path
        :type MountedPath: str
        :param _Data: Configuration Content
        :type Data: list of Pair
        """
        self._ConfigDataName = None
        self._MountedPath = None
        self._Data = None

    @property
    def ConfigDataName(self):
        """Configuration Name
        :rtype: str
        """
        return self._ConfigDataName

    @ConfigDataName.setter
    def ConfigDataName(self, ConfigDataName):
        self._ConfigDataName = ConfigDataName

    @property
    def MountedPath(self):
        """Mount point path
        :rtype: str
        """
        return self._MountedPath

    @MountedPath.setter
    def MountedPath(self, MountedPath):
        self._MountedPath = MountedPath

    @property
    def Data(self):
        """Configuration Content
        :rtype: list of Pair
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ConfigDataName = params.get("ConfigDataName")
        self._MountedPath = params.get("MountedPath")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self._Data.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespacePage(AbstractModel):
    """Namespace pagination

    """

    def __init__(self):
        r"""
        :param _Records: Records
        :type Records: list of TemNamespaceInfo
        :param _Total: Total number
        :type Total: int
        :param _Size: Number of items
        :type Size: int
        :param _Pages: Number of pages
        :type Pages: int
        """
        self._Records = None
        self._Total = None
        self._Size = None
        self._Pages = None

    @property
    def Records(self):
        """Records
        :rtype: list of TemNamespaceInfo
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def Total(self):
        """Total number
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Size(self):
        """Number of items
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Pages(self):
        """Number of pages
        :rtype: int
        """
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = TemNamespaceInfo()
                obj._deserialize(item)
                self._Records.append(obj)
        self._Total = params.get("Total")
        self._Size = params.get("Size")
        self._Pages = params.get("Pages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pair(AbstractModel):
    """Key-Value pair

    """

    def __init__(self):
        r"""
        :param _Key: Key
        :type Key: str
        :param _Value: Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Value
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
        


class PortMapping(AbstractModel):
    """Service port mapping

    """

    def __init__(self):
        r"""
        :param _Port: Port.
        :type Port: int
        :param _TargetPort: Mapped port.
        :type TargetPort: int
        :param _Protocol: TCP/UDP protocol stack.
        :type Protocol: str
        """
        self._Port = None
        self._TargetPort = None
        self._Protocol = None

    @property
    def Port(self):
        """Port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetPort(self):
        """Mapped port.
        :rtype: int
        """
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def Protocol(self):
        """TCP/UDP protocol stack.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetPort = params.get("TargetPort")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartServiceRunPodRequest(AbstractModel):
    """RestartServiceRunPod request structure.

    """

    def __init__(self):
        r"""
        :param _NamespaceId: Environment ID.
        :type NamespaceId: str
        :param _ServiceId: Service ID.
        :type ServiceId: str
        :param _PodName: Pod name.
        :type PodName: str
        :param _Limit: Number of items per page.
        :type Limit: int
        :param _Offset: Page number.
        :type Offset: int
        :param _Status: Pod status.
        :type Status: str
        :param _SourceChannel: Source channel.
        :type SourceChannel: int
        """
        self._NamespaceId = None
        self._ServiceId = None
        self._PodName = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._SourceChannel = None

    @property
    def NamespaceId(self):
        """Environment ID.
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def ServiceId(self):
        """Service ID.
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PodName(self):
        """Pod name.
        :rtype: str
        """
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Limit(self):
        """Number of items per page.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        """Pod status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceChannel(self):
        """Source channel.
        :rtype: int
        """
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._ServiceId = params.get("ServiceId")
        self._PodName = params.get("PodName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Status = params.get("Status")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartServiceRunPodResponse(AbstractModel):
    """RestartServiceRunPod response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned results.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned results.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """Pod

    """

    def __init__(self):
        r"""
        :param _Webshell: Shell address
        :type Webshell: str
        :param _PodId: Pod ID
        :type PodId: str
        :param _Status: Status
        :type Status: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _PodIp: Pod IP.
        :type PodIp: str
        :param _Zone: Availability zone.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param _DeployVersion: Deployed version.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type DeployVersion: str
        :param _RestartCount: Number of Restarts
Note: This is field may return `null`, indicating that no valid value can be obtained.
        :type RestartCount: int
        """
        self._Webshell = None
        self._PodId = None
        self._Status = None
        self._CreateTime = None
        self._PodIp = None
        self._Zone = None
        self._DeployVersion = None
        self._RestartCount = None

    @property
    def Webshell(self):
        """Shell address
        :rtype: str
        """
        return self._Webshell

    @Webshell.setter
    def Webshell(self, Webshell):
        self._Webshell = Webshell

    @property
    def PodId(self):
        """Pod ID
        :rtype: str
        """
        return self._PodId

    @PodId.setter
    def PodId(self, PodId):
        self._PodId = PodId

    @property
    def Status(self):
        """Status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
    def PodIp(self):
        """Pod IP.
        :rtype: str
        """
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def Zone(self):
        """Availability zone.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DeployVersion(self):
        """Deployed version.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def RestartCount(self):
        """Number of Restarts
Note: This is field may return `null`, indicating that no valid value can be obtained.
        :rtype: int
        """
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount


    def _deserialize(self, params):
        self._Webshell = params.get("Webshell")
        self._PodId = params.get("PodId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._PodIp = params.get("PodIp")
        self._Zone = params.get("Zone")
        self._DeployVersion = params.get("DeployVersion")
        self._RestartCount = params.get("RestartCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageConf(AbstractModel):
    """Storage volume configuration

    """

    def __init__(self):
        r"""
        :param _StorageVolName: Storage volume name
        :type StorageVolName: str
        :param _StorageVolPath: Storage volume path
        :type StorageVolPath: str
        :param _StorageVolIp: Storage volume IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type StorageVolIp: str
        """
        self._StorageVolName = None
        self._StorageVolPath = None
        self._StorageVolIp = None

    @property
    def StorageVolName(self):
        """Storage volume name
        :rtype: str
        """
        return self._StorageVolName

    @StorageVolName.setter
    def StorageVolName(self, StorageVolName):
        self._StorageVolName = StorageVolName

    @property
    def StorageVolPath(self):
        """Storage volume path
        :rtype: str
        """
        return self._StorageVolPath

    @StorageVolPath.setter
    def StorageVolPath(self, StorageVolPath):
        self._StorageVolPath = StorageVolPath

    @property
    def StorageVolIp(self):
        """Storage volume IP
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StorageVolIp

    @StorageVolIp.setter
    def StorageVolIp(self, StorageVolIp):
        self._StorageVolIp = StorageVolIp


    def _deserialize(self, params):
        self._StorageVolName = params.get("StorageVolName")
        self._StorageVolPath = params.get("StorageVolPath")
        self._StorageVolIp = params.get("StorageVolIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageMountConf(AbstractModel):
    """Data volume mount information

    """

    def __init__(self):
        r"""
        :param _VolumeName: Data volume name
        :type VolumeName: str
        :param _MountPath: Data volume binding path
        :type MountPath: str
        """
        self._VolumeName = None
        self._MountPath = None

    @property
    def VolumeName(self):
        """Data volume name
        :rtype: str
        """
        return self._VolumeName

    @VolumeName.setter
    def VolumeName(self, VolumeName):
        self._VolumeName = VolumeName

    @property
    def MountPath(self):
        """Data volume binding path
        :rtype: str
        """
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath


    def _deserialize(self, params):
        self._VolumeName = params.get("VolumeName")
        self._MountPath = params.get("MountPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemNamespaceInfo(AbstractModel):
    """Namespace object

    """

    def __init__(self):
        r"""
        :param _NamespaceId: Namespace ID
        :type NamespaceId: str
        :param _Channel: Channel
        :type Channel: str
        :param _NamespaceName: Namespace name
        :type NamespaceName: str
        :param _Region: Region name
        :type Region: str
        :param _Description: Namespace description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Status: Status. 1: terminated; 0: normal
        :type Status: int
        :param _Vpc: VPC
        :type Vpc: str
        :param _CreateDate: Creation time
        :type CreateDate: str
        :param _ModifyDate: Modification time
        :type ModifyDate: str
        :param _Modifier: Modifier
        :type Modifier: str
        :param _Creator: Creator
        :type Creator: str
        :param _ServiceNum: Number of services
        :type ServiceNum: int
        :param _RunInstancesNum: Number of running instances
        :type RunInstancesNum: int
        :param _SubnetId: Subnet
        :type SubnetId: str
        :param _TcbEnvStatus: TCB environment status
        :type TcbEnvStatus: str
        :param _ClusterStatus: eks cluster status
        :type ClusterStatus: str
        :param _EnableTswTraceService: Whether to enable TSW
        :type EnableTswTraceService: bool
        """
        self._NamespaceId = None
        self._Channel = None
        self._NamespaceName = None
        self._Region = None
        self._Description = None
        self._Status = None
        self._Vpc = None
        self._CreateDate = None
        self._ModifyDate = None
        self._Modifier = None
        self._Creator = None
        self._ServiceNum = None
        self._RunInstancesNum = None
        self._SubnetId = None
        self._TcbEnvStatus = None
        self._ClusterStatus = None
        self._EnableTswTraceService = None

    @property
    def NamespaceId(self):
        """Namespace ID
        :rtype: str
        """
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Channel(self):
        """Channel
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def NamespaceName(self):
        """Namespace name
        :rtype: str
        """
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Region(self):
        """Region name
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Description(self):
        """Namespace description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """Status. 1: terminated; 0: normal
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vpc(self):
        """VPC
        :rtype: str
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def CreateDate(self):
        """Creation time
        :rtype: str
        """
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        """Modification time
        :rtype: str
        """
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def Modifier(self):
        """Modifier
        :rtype: str
        """
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        """Creator
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def ServiceNum(self):
        """Number of services
        :rtype: int
        """
        return self._ServiceNum

    @ServiceNum.setter
    def ServiceNum(self, ServiceNum):
        self._ServiceNum = ServiceNum

    @property
    def RunInstancesNum(self):
        """Number of running instances
        :rtype: int
        """
        return self._RunInstancesNum

    @RunInstancesNum.setter
    def RunInstancesNum(self, RunInstancesNum):
        self._RunInstancesNum = RunInstancesNum

    @property
    def SubnetId(self):
        """Subnet
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def TcbEnvStatus(self):
        """TCB environment status
        :rtype: str
        """
        return self._TcbEnvStatus

    @TcbEnvStatus.setter
    def TcbEnvStatus(self, TcbEnvStatus):
        self._TcbEnvStatus = TcbEnvStatus

    @property
    def ClusterStatus(self):
        """eks cluster status
        :rtype: str
        """
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def EnableTswTraceService(self):
        """Whether to enable TSW
        :rtype: bool
        """
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._Channel = params.get("Channel")
        self._NamespaceName = params.get("NamespaceName")
        self._Region = params.get("Region")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Vpc = params.get("Vpc")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        self._ServiceNum = params.get("ServiceNum")
        self._RunInstancesNum = params.get("RunInstancesNum")
        self._SubnetId = params.get("SubnetId")
        self._TcbEnvStatus = params.get("TcbEnvStatus")
        self._ClusterStatus = params.get("ClusterStatus")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        