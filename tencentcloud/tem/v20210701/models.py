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
        :param _MinReplicas: Minimum number of instances in a scaling group
        :type MinReplicas: int
        :param _MaxReplicas: Maximum number of instances in a scaling group
        :type MaxReplicas: int
        :param _HorizontalAutoscaler: Policy of the scaling rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param _CronHorizontalAutoscaler: Scheduled auto-scaler policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param _AutoscalerId: Scaling rule ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutoscalerId: str
        :param _AutoscalerName: Scaling rule name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutoscalerName: str
        :param _Description: Description of the scaling rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param _CreateDate: Creation time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param _ModifyDate: Modification time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ModifyDate: str
        :param _EnableDate: Start Time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableDate: str
        :param _Enabled: Whether it is enabled
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Enabled: bool
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._HorizontalAutoscaler = None
        self._CronHorizontalAutoscaler = None
        self._AutoscalerId = None
        self._AutoscalerName = None
        self._Description = None
        self._CreateDate = None
        self._ModifyDate = None
        self._EnableDate = None
        self._Enabled = None

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def HorizontalAutoscaler(self):
        return self._HorizontalAutoscaler

    @HorizontalAutoscaler.setter
    def HorizontalAutoscaler(self, HorizontalAutoscaler):
        self._HorizontalAutoscaler = HorizontalAutoscaler

    @property
    def CronHorizontalAutoscaler(self):
        return self._CronHorizontalAutoscaler

    @CronHorizontalAutoscaler.setter
    def CronHorizontalAutoscaler(self, CronHorizontalAutoscaler):
        self._CronHorizontalAutoscaler = CronHorizontalAutoscaler

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId

    @property
    def AutoscalerName(self):
        return self._AutoscalerName

    @AutoscalerName.setter
    def AutoscalerName(self, AutoscalerName):
        self._AutoscalerName = AutoscalerName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def EnableDate(self):
        return self._EnableDate

    @EnableDate.setter
    def EnableDate(self, EnableDate):
        self._EnableDate = EnableDate

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("HorizontalAutoscaler") is not None:
            self._HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self._HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self._CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self._CronHorizontalAutoscaler.append(obj)
        self._AutoscalerId = params.get("AutoscalerId")
        self._AutoscalerName = params.get("AutoscalerName")
        self._Description = params.get("Description")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._EnableDate = params.get("EnableDate")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigData(AbstractModel):
    """Configuration

    """

    def __init__(self):
        r"""
        :param _Name: Configuration name
        :type Name: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _RelatedApplications: List of associated applications
        :type RelatedApplications: list of TemService
        :param _Data: Configuration item
        :type Data: list of Pair
        """
        self._Name = None
        self._CreateTime = None
        self._RelatedApplications = None
        self._Data = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RelatedApplications(self):
        return self._RelatedApplications

    @RelatedApplications.setter
    def RelatedApplications(self, RelatedApplications):
        self._RelatedApplications = RelatedApplications

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreateTime = params.get("CreateTime")
        if params.get("RelatedApplications") is not None:
            self._RelatedApplications = []
            for item in params.get("RelatedApplications"):
                obj = TemService()
                obj._deserialize(item)
                self._RelatedApplications.append(obj)
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
        :param _TmpSecretId: Temporary key SecretId
        :type TmpSecretId: str
        :param _TmpSecretKey: Temporary key SecretKey
        :type TmpSecretKey: str
        :param _SessionToken: `sessionToken` of temporary key
        :type SessionToken: str
        :param _StartTime: Start time of temporary key acquisition
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
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def TmpSecretId(self):
        return self._TmpSecretId

    @TmpSecretId.setter
    def TmpSecretId(self, TmpSecretId):
        self._TmpSecretId = TmpSecretId

    @property
    def TmpSecretKey(self):
        return self._TmpSecretKey

    @TmpSecretKey.setter
    def TmpSecretKey(self, TmpSecretKey):
        self._TmpSecretKey = TmpSecretKey

    @property
    def SessionToken(self):
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def FullPath(self):
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
        


class CreateApplicationAutoscalerRequest(AbstractModel):
    """CreateApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _Autoscaler: Auto scaling rule
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._Autoscaler = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Autoscaler(self):
        return self._Autoscaler

    @Autoscaler.setter
    def Autoscaler(self, Autoscaler):
        self._Autoscaler = Autoscaler


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Autoscaler") is not None:
            self._Autoscaler = Autoscaler()
            self._Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationAutoscalerResponse(AbstractModel):
    """CreateApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Scaling rule ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateApplicationRequest(AbstractModel):
    """CreateApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _Description: Description
        :type Description: str
        :param _UseDefaultImageService: Whether to use the default image service. `1`: yes; `0`: no
        :type UseDefaultImageService: int
        :param _RepoType: Type of the bound repository. `0`: TCR Personal; `1`: TCR Enterprise
        :type RepoType: int
        :param _InstanceId: TCR Enterprise instance ID
        :type InstanceId: str
        :param _RepoServer: Address of the bound image server
        :type RepoServer: str
        :param _RepoName: Name of the bound image repository
        :type RepoName: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _SubnetList: Application subnet
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
        :param _EnableTracing: Whether to enable APM tracing for the Java application. `1`: Enable, `0`: Disable
        :type EnableTracing: int
        :param _UseDefaultImageServiceParameters: Parameters of the default image service
        :type UseDefaultImageServiceParameters: :class:`tencentcloud.tem.v20210701.models.UseDefaultRepoParameters`
        :param _Tags: Tag
        :type Tags: list of Tag
        """
        self._ApplicationName = None
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
        self._EnableTracing = None
        self._UseDefaultImageServiceParameters = None
        self._Tags = None

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UseDefaultImageService(self):
        return self._UseDefaultImageService

    @UseDefaultImageService.setter
    def UseDefaultImageService(self, UseDefaultImageService):
        self._UseDefaultImageService = UseDefaultImageService

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepoServer(self):
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def SubnetList(self):
        return self._SubnetList

    @SubnetList.setter
    def SubnetList(self, SubnetList):
        self._SubnetList = SubnetList

    @property
    def CodingLanguage(self):
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def UseDefaultImageServiceParameters(self):
        return self._UseDefaultImageServiceParameters

    @UseDefaultImageServiceParameters.setter
    def UseDefaultImageServiceParameters(self, UseDefaultImageServiceParameters):
        self._UseDefaultImageServiceParameters = UseDefaultImageServiceParameters

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ApplicationName = params.get("ApplicationName")
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
        self._EnableTracing = params.get("EnableTracing")
        if params.get("UseDefaultImageServiceParameters") is not None:
            self._UseDefaultImageServiceParameters = UseDefaultRepoParameters()
            self._UseDefaultImageServiceParameters._deserialize(params.get("UseDefaultImageServiceParameters"))
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
        


class CreateApplicationResponse(AbstractModel):
    """CreateApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Result: ID of the created application
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateApplicationServiceRequest(AbstractModel):
    """CreateApplicationService request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _Service: Details of the access policy
        :type Service: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._Service = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self._Service = ServicePortMapping()
            self._Service._deserialize(params.get("Service"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationServiceResponse(AbstractModel):
    """CreateApplicationService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateConfigDataRequest(AbstractModel):
    """CreateConfigData request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _Data: Configuration information
        :type Data: list of Pair
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None
        self._Data = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
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
        


class CreateConfigDataResponse(AbstractModel):
    """CreateConfigData response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the creation is successful
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateCosTokenRequest(AbstractModel):
    """CreateCosToken request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _PkgName: Package name
        :type PkgName: str
        :param _OptType: Operation type. 1: upload; 2: query
        :type OptType: int
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _TimeVersion: Input parameter of `deployVersion`
        :type TimeVersion: str
        """
        self._ApplicationId = None
        self._PkgName = None
        self._OptType = None
        self._SourceChannel = None
        self._TimeVersion = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def OptType(self):
        return self._OptType

    @OptType.setter
    def OptType(self, OptType):
        self._OptType = OptType

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def TimeVersion(self):
        return self._TimeVersion

    @TimeVersion.setter
    def TimeVersion(self, TimeVersion):
        self._TimeVersion = TimeVersion


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
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
        


class CreateCosTokenResponse(AbstractModel):
    """CreateCosToken response structure.

    """

    def __init__(self):
        r"""
        :param _Result: `CosToken` object in case of success and `null` in case of failure
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.tem.v20210701.models.CosToken`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CosToken()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: Environment name
        :type EnvironmentName: str
        :param _Description: Environment description
        :type Description: str
        :param _Vpc: VPC name
        :type Vpc: str
        :param _SubnetIds: List of subnets
        :type SubnetIds: list of str
        :param _K8sVersion: Kubernetes version
        :type K8sVersion: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _EnableTswTraceService: Whether to enable the TSW service
        :type EnableTswTraceService: bool
        :param _Tags: Tag
        :type Tags: list of Tag
        :param _EnvType: Environment type. Values: `test`, `pre`, `prod`
        :type EnvType: str
        :param _CreateRegion: The region to create the environment
        :type CreateRegion: str
        :param _SetupVpc: Whether to create a VPC
        :type SetupVpc: bool
        :param _SetupPrometheus: Whether to create a TMP instance
        :type SetupPrometheus: bool
        :param _PrometheusId: TMP instance ID
        :type PrometheusId: str
        :param _ApmId: APM ID
        :type ApmId: str
        """
        self._EnvironmentName = None
        self._Description = None
        self._Vpc = None
        self._SubnetIds = None
        self._K8sVersion = None
        self._SourceChannel = None
        self._EnableTswTraceService = None
        self._Tags = None
        self._EnvType = None
        self._CreateRegion = None
        self._SetupVpc = None
        self._SetupPrometheus = None
        self._PrometheusId = None
        self._ApmId = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def K8sVersion(self):
        return self._K8sVersion

    @K8sVersion.setter
    def K8sVersion(self, K8sVersion):
        self._K8sVersion = K8sVersion

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnableTswTraceService(self):
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def CreateRegion(self):
        return self._CreateRegion

    @CreateRegion.setter
    def CreateRegion(self, CreateRegion):
        self._CreateRegion = CreateRegion

    @property
    def SetupVpc(self):
        return self._SetupVpc

    @SetupVpc.setter
    def SetupVpc(self, SetupVpc):
        self._SetupVpc = SetupVpc

    @property
    def SetupPrometheus(self):
        return self._SetupPrometheus

    @SetupPrometheus.setter
    def SetupPrometheus(self, SetupPrometheus):
        self._SetupPrometheus = SetupPrometheus

    @property
    def PrometheusId(self):
        return self._PrometheusId

    @PrometheusId.setter
    def PrometheusId(self, PrometheusId):
        self._PrometheusId = PrometheusId

    @property
    def ApmId(self):
        return self._ApmId

    @ApmId.setter
    def ApmId(self, ApmId):
        self._ApmId = ApmId


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Description = params.get("Description")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._K8sVersion = params.get("K8sVersion")
        self._SourceChannel = params.get("SourceChannel")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnvType = params.get("EnvType")
        self._CreateRegion = params.get("CreateRegion")
        self._SetupVpc = params.get("SetupVpc")
        self._SetupPrometheus = params.get("SetupPrometheus")
        self._PrometheusId = params.get("PrometheusId")
        self._ApmId = params.get("ApmId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Environment ID in case of success and `null` in case of failure
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateLogConfigRequest(AbstractModel):
    """CreateLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _InputType: Collection type. Values: `container_stdout` (standard); `container_file` (file)
        :type InputType: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _LogType: Log withdrawal mode. Values: `minimalist_log` (full text in a single line); `multiline_log` (full text in multiple lines); `json_log` (JSON); `fullregex_log` (regex in a single line); `multiline_fullregex_log` (regex in multiple lines)
        :type LogType: str
        :param _BeginningRegex: The first line regex. It’s valid when `LogType` is `multiline_log`.
        :type BeginningRegex: str
        :param _LogPath: Directory of files to collect. It’s valid when `InputType` is `container_file`.
        :type LogPath: str
        :param _FilePattern: Name pattern of files to collect. It’s valid when `InputType` is `container_file`.
        :type FilePattern: str
        :param _ExtractRule: Export
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self._EnvironmentId = None
        self._Name = None
        self._InputType = None
        self._ApplicationId = None
        self._LogsetId = None
        self._TopicId = None
        self._LogType = None
        self._BeginningRegex = None
        self._LogPath = None
        self._FilePattern = None
        self._ExtractRule = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def BeginningRegex(self):
        return self._BeginningRegex

    @BeginningRegex.setter
    def BeginningRegex(self, BeginningRegex):
        self._BeginningRegex = BeginningRegex

    @property
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._InputType = params.get("InputType")
        self._ApplicationId = params.get("ApplicationId")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._LogType = params.get("LogType")
        self._BeginningRegex = params.get("BeginningRegex")
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = LogConfigExtractRule()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogConfigResponse(AbstractModel):
    """CreateLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the creation is successful
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ResourceType: Resource type. Valid values: `CFS` (file system), `CLS` (log service), `TSE_SRE` (registry)
        :type ResourceType: str
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _ResourceFrom: Source of the resource. Values: `existing` (choose an existing resource), `creating` (create a new resource)
        :type ResourceFrom: str
        :param _ResourceConfig: Resource extra configuration
        :type ResourceConfig: str
        """
        self._EnvironmentId = None
        self._ResourceType = None
        self._ResourceId = None
        self._SourceChannel = None
        self._ResourceFrom = None
        self._ResourceConfig = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ResourceFrom(self):
        return self._ResourceFrom

    @ResourceFrom.setter
    def ResourceFrom(self, ResourceFrom):
        self._ResourceFrom = ResourceFrom

    @property
    def ResourceConfig(self):
        return self._ResourceConfig

    @ResourceConfig.setter
    def ResourceConfig(self, ResourceConfig):
        self._ResourceConfig = ResourceConfig


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        self._SourceChannel = params.get("SourceChannel")
        self._ResourceFrom = params.get("ResourceFrom")
        self._ResourceConfig = params.get("ResourceConfig")
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
        :param _Result: Result
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CronHorizontalAutoscaler(AbstractModel):
    """Scheduled Scaling Policy

    """

    def __init__(self):
        r"""
        :param _Name: Name of a scheduled scaling policy
        :type Name: str
        :param _Period: Policy period
"* * *" indicates three ranges. The first is day, the second month, and the third week. The three parts are separated by spaces.
Examples:
* * * (every day)
* * 0-3 (every Sunday through Wednesday)
1,11,21 * * (1st, 11th, and 21st of every month)
        :type Period: str
        :param _Schedules: Details of a scheduled scaling policy
        :type Schedules: list of CronHorizontalAutoscalerSchedule
        :param _Enabled: Enabled or not
        :type Enabled: bool
        :param _Priority: Policy priority. The higher the value, the higher the priority. The minimum value is 0.
        :type Priority: int
        """
        self._Name = None
        self._Period = None
        self._Schedules = None
        self._Enabled = None
        self._Priority = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Schedules(self):
        return self._Schedules

    @Schedules.setter
    def Schedules(self, Schedules):
        self._Schedules = Schedules

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Period = params.get("Period")
        if params.get("Schedules") is not None:
            self._Schedules = []
            for item in params.get("Schedules"):
                obj = CronHorizontalAutoscalerSchedule()
                obj._deserialize(item)
                self._Schedules.append(obj)
        self._Enabled = params.get("Enabled")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CronHorizontalAutoscalerSchedule(AbstractModel):
    """Details of a scheduled scaling policy

    """

    def __init__(self):
        r"""
        :param _StartAt: Triggering time, in the format of HH:MM
Example:
00:00 (Trigger at midnight)
        :type StartAt: str
        :param _TargetReplicas: Number of target pods (less than 50)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TargetReplicas: int
        """
        self._StartAt = None
        self._TargetReplicas = None

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def TargetReplicas(self):
        return self._TargetReplicas

    @TargetReplicas.setter
    def TargetReplicas(self, TargetReplicas):
        self._TargetReplicas = TargetReplicas


    def _deserialize(self, params):
        self._StartAt = params.get("StartAt")
        self._TargetReplicas = params.get("TargetReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerRequest(AbstractModel):
    """DeleteApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationAutoscalerResponse(AbstractModel):
    """DeleteApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the action is successful
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApplicationRequest(AbstractModel):
    """DeleteApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _DeleteApplicationIfNoRunningVersion: Whether to delete this application automatically when there is no running version.
        :type DeleteApplicationIfNoRunningVersion: bool
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._DeleteApplicationIfNoRunningVersion = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def DeleteApplicationIfNoRunningVersion(self):
        return self._DeleteApplicationIfNoRunningVersion

    @DeleteApplicationIfNoRunningVersion.setter
    def DeleteApplicationIfNoRunningVersion(self, DeleteApplicationIfNoRunningVersion):
        self._DeleteApplicationIfNoRunningVersion = DeleteApplicationIfNoRunningVersion


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._DeleteApplicationIfNoRunningVersion = params.get("DeleteApplicationIfNoRunningVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationResponse(AbstractModel):
    """DeleteApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApplicationServiceRequest(AbstractModel):
    """DeleteApplicationService request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ServiceName: Service name
        :type ServiceName: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None
        self._ServiceName = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationServiceResponse(AbstractModel):
    """DeleteApplicationService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param _IngressName: Ingress rule name
        :type IngressName: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._IngressName = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._IngressName = params.get("IngressName")
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
        :param _Result: Whether deletion is successful
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeployApplicationRequest(AbstractModel):
    """DeployApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _InitPodNum: Number of initialized pods
        :type InitPodNum: int
        :param _CpuSpec: CPU specification
        :type CpuSpec: float
        :param _MemorySpec: Memory specification
        :type MemorySpec: float
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ImgRepo: Image repository
        :type ImgRepo: str
        :param _VersionDesc: Version description
        :type VersionDesc: str
        :param _JvmOpts: Launch parameters
        :type JvmOpts: str
        :param _EsInfo: Auto scaling configuration (This field is disused. Please use `HorizontalAutoscaler` to set the auto scaling policy.)
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
        :param _EnvConf: Environment variable configuration
        :type EnvConf: list of Pair
        :param _LogConfs: Log configuration
        :type LogConfs: list of str
        :param _StorageConfs: Data volume configuration
        :type StorageConfs: list of StorageConf
        :param _StorageMountConfs: Data volume mount configuration
        :type StorageMountConfs: list of StorageMountConf
        :param _DeployMode: Deployment type
- JAR: deployment through JAR package
- WAR: deployment through WAR package
- IMAGE: deployment through image
        :type DeployMode: str
        :param _DeployVersion: When the deployment type is `IMAGE`, this parameter indicates the image tag
When the deployment type is `JAR` or `WAR`, this parameter indicates the package version number
        :type DeployVersion: str
        :param _PkgName: Package name, which is required when using JAR or WAR packages for deployment
        :type PkgName: str
        :param _JdkVersion: JDK version
- KONA: use KONA JDK
- OPEN: use open JDK
- KONA: use KONA JDK
- OPEN: use open JDK
        :type JdkVersion: str
        :param _SecurityGroupIds: Security group IDs
        :type SecurityGroupIds: list of str
        :param _LogOutputConf: Log output configuration
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _Description: Version description
        :type Description: str
        :param _ImageCommand: Image command
        :type ImageCommand: str
        :param _ImageArgs: Image command parameters
        :type ImageArgs: list of str
        :param _UseRegistryDefaultConfig: Whether to add the registry's default configurations
        :type UseRegistryDefaultConfig: bool
        :param _SettingConfs: Mounting configurations
        :type SettingConfs: list of MountedSettingConf
        :param _Service: Application access configuration
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _VersionId: ID of the version that you want to roll back to
        :type VersionId: str
        :param _PostStart: The script to run after startup
        :type PostStart: str
        :param _PreStop: The script to run before stop
        :type PreStop: str
        :param _Liveness: Configuration of aliveness probe
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _Readiness: Configuration of readiness probe
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _DeployStrategyConf: Configuration of batch release policies
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param _HorizontalAutoscaler: Auto scaling policy. (Disused. Please use APIs for auto scaling policy combinations)
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param _CronHorizontalAutoscaler: Scheduled scaling policy (Disused. Please use APIs for auto scaling policy combinations)
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param _LogEnable: Specifies whether to enable logging. `1`: enable; `0`: do not enable
        :type LogEnable: int
        :param _ConfEdited: Whether the configuration is modified (except for the image configuration)
        :type ConfEdited: bool
        :param _SpeedUp: Whether the application acceleration is enabled 
        :type SpeedUp: bool
        :param _StartupProbe: Whether to enable probing
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _OsFlavour: The version of the operating system
If `openjdk` is selected, the value can be: 
- ALPINE
- CENTOS
If `konajdk` is selected, the value can be: 
- ALPINE
- TENCENTOS
        :type OsFlavour: str
        :param _EnablePrometheusConf: Configuration of metrics of this application
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param _EnableTracing: `1`: Automatically enable APM tracing (Skywalking)
`0`: Disable APM tracing
        :type EnableTracing: int
        :param _EnableMetrics: `1`: Automatically enable metrics collection (open-telemetry)
`0`: Disable metrics collection
        :type EnableMetrics: int
        :param _TcrInstanceId: ID of the TCR instance used for image deployment
        :type TcrInstanceId: str
        :param _RepoServer: Image server address for image deployment
        :type RepoServer: str
        :param _RepoType: Type of the repository. `0`: TCR Personal; `1`: TCR Enterprise; `2`: Public repository; `3`: TEM hosted repository; `4`: Demo repository
        :type RepoType: int
        """
        self._ApplicationId = None
        self._InitPodNum = None
        self._CpuSpec = None
        self._MemorySpec = None
        self._EnvironmentId = None
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
        self._UseRegistryDefaultConfig = None
        self._SettingConfs = None
        self._Service = None
        self._VersionId = None
        self._PostStart = None
        self._PreStop = None
        self._Liveness = None
        self._Readiness = None
        self._DeployStrategyConf = None
        self._HorizontalAutoscaler = None
        self._CronHorizontalAutoscaler = None
        self._LogEnable = None
        self._ConfEdited = None
        self._SpeedUp = None
        self._StartupProbe = None
        self._OsFlavour = None
        self._EnablePrometheusConf = None
        self._EnableTracing = None
        self._EnableMetrics = None
        self._TcrInstanceId = None
        self._RepoServer = None
        self._RepoType = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def InitPodNum(self):
        return self._InitPodNum

    @InitPodNum.setter
    def InitPodNum(self, InitPodNum):
        self._InitPodNum = InitPodNum

    @property
    def CpuSpec(self):
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def MemorySpec(self):
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ImgRepo(self):
        return self._ImgRepo

    @ImgRepo.setter
    def ImgRepo(self, ImgRepo):
        self._ImgRepo = ImgRepo

    @property
    def VersionDesc(self):
        return self._VersionDesc

    @VersionDesc.setter
    def VersionDesc(self, VersionDesc):
        self._VersionDesc = VersionDesc

    @property
    def JvmOpts(self):
        return self._JvmOpts

    @JvmOpts.setter
    def JvmOpts(self, JvmOpts):
        self._JvmOpts = JvmOpts

    @property
    def EsInfo(self):
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def EnvConf(self):
        return self._EnvConf

    @EnvConf.setter
    def EnvConf(self, EnvConf):
        self._EnvConf = EnvConf

    @property
    def LogConfs(self):
        return self._LogConfs

    @LogConfs.setter
    def LogConfs(self, LogConfs):
        self._LogConfs = LogConfs

    @property
    def StorageConfs(self):
        return self._StorageConfs

    @StorageConfs.setter
    def StorageConfs(self, StorageConfs):
        self._StorageConfs = StorageConfs

    @property
    def StorageMountConfs(self):
        return self._StorageMountConfs

    @StorageMountConfs.setter
    def StorageMountConfs(self, StorageMountConfs):
        self._StorageMountConfs = StorageMountConfs

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def JdkVersion(self):
        return self._JdkVersion

    @JdkVersion.setter
    def JdkVersion(self, JdkVersion):
        self._JdkVersion = JdkVersion

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LogOutputConf(self):
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ImageCommand(self):
        return self._ImageCommand

    @ImageCommand.setter
    def ImageCommand(self, ImageCommand):
        self._ImageCommand = ImageCommand

    @property
    def ImageArgs(self):
        return self._ImageArgs

    @ImageArgs.setter
    def ImageArgs(self, ImageArgs):
        self._ImageArgs = ImageArgs

    @property
    def UseRegistryDefaultConfig(self):
        return self._UseRegistryDefaultConfig

    @UseRegistryDefaultConfig.setter
    def UseRegistryDefaultConfig(self, UseRegistryDefaultConfig):
        self._UseRegistryDefaultConfig = UseRegistryDefaultConfig

    @property
    def SettingConfs(self):
        return self._SettingConfs

    @SettingConfs.setter
    def SettingConfs(self, SettingConfs):
        self._SettingConfs = SettingConfs

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def PostStart(self):
        return self._PostStart

    @PostStart.setter
    def PostStart(self, PostStart):
        self._PostStart = PostStart

    @property
    def PreStop(self):
        return self._PreStop

    @PreStop.setter
    def PreStop(self, PreStop):
        self._PreStop = PreStop

    @property
    def Liveness(self):
        return self._Liveness

    @Liveness.setter
    def Liveness(self, Liveness):
        self._Liveness = Liveness

    @property
    def Readiness(self):
        return self._Readiness

    @Readiness.setter
    def Readiness(self, Readiness):
        self._Readiness = Readiness

    @property
    def DeployStrategyConf(self):
        return self._DeployStrategyConf

    @DeployStrategyConf.setter
    def DeployStrategyConf(self, DeployStrategyConf):
        self._DeployStrategyConf = DeployStrategyConf

    @property
    def HorizontalAutoscaler(self):
        return self._HorizontalAutoscaler

    @HorizontalAutoscaler.setter
    def HorizontalAutoscaler(self, HorizontalAutoscaler):
        self._HorizontalAutoscaler = HorizontalAutoscaler

    @property
    def CronHorizontalAutoscaler(self):
        return self._CronHorizontalAutoscaler

    @CronHorizontalAutoscaler.setter
    def CronHorizontalAutoscaler(self, CronHorizontalAutoscaler):
        self._CronHorizontalAutoscaler = CronHorizontalAutoscaler

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def ConfEdited(self):
        return self._ConfEdited

    @ConfEdited.setter
    def ConfEdited(self, ConfEdited):
        self._ConfEdited = ConfEdited

    @property
    def SpeedUp(self):
        return self._SpeedUp

    @SpeedUp.setter
    def SpeedUp(self, SpeedUp):
        self._SpeedUp = SpeedUp

    @property
    def StartupProbe(self):
        return self._StartupProbe

    @StartupProbe.setter
    def StartupProbe(self, StartupProbe):
        self._StartupProbe = StartupProbe

    @property
    def OsFlavour(self):
        return self._OsFlavour

    @OsFlavour.setter
    def OsFlavour(self, OsFlavour):
        self._OsFlavour = OsFlavour

    @property
    def EnablePrometheusConf(self):
        return self._EnablePrometheusConf

    @EnablePrometheusConf.setter
    def EnablePrometheusConf(self, EnablePrometheusConf):
        self._EnablePrometheusConf = EnablePrometheusConf

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def EnableMetrics(self):
        return self._EnableMetrics

    @EnableMetrics.setter
    def EnableMetrics(self, EnableMetrics):
        self._EnableMetrics = EnableMetrics

    @property
    def TcrInstanceId(self):
        return self._TcrInstanceId

    @TcrInstanceId.setter
    def TcrInstanceId(self, TcrInstanceId):
        self._TcrInstanceId = TcrInstanceId

    @property
    def RepoServer(self):
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._InitPodNum = params.get("InitPodNum")
        self._CpuSpec = params.get("CpuSpec")
        self._MemorySpec = params.get("MemorySpec")
        self._EnvironmentId = params.get("EnvironmentId")
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
        self._UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("SettingConfs") is not None:
            self._SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self._SettingConfs.append(obj)
        if params.get("Service") is not None:
            self._Service = EksService()
            self._Service._deserialize(params.get("Service"))
        self._VersionId = params.get("VersionId")
        self._PostStart = params.get("PostStart")
        self._PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self._Liveness = HealthCheckConfig()
            self._Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self._Readiness = HealthCheckConfig()
            self._Readiness._deserialize(params.get("Readiness"))
        if params.get("DeployStrategyConf") is not None:
            self._DeployStrategyConf = DeployStrategyConf()
            self._DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("HorizontalAutoscaler") is not None:
            self._HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self._HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self._CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self._CronHorizontalAutoscaler.append(obj)
        self._LogEnable = params.get("LogEnable")
        self._ConfEdited = params.get("ConfEdited")
        self._SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self._StartupProbe = HealthCheckConfig()
            self._StartupProbe._deserialize(params.get("StartupProbe"))
        self._OsFlavour = params.get("OsFlavour")
        if params.get("EnablePrometheusConf") is not None:
            self._EnablePrometheusConf = EnablePrometheusConf()
            self._EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self._EnableTracing = params.get("EnableTracing")
        self._EnableMetrics = params.get("EnableMetrics")
        self._TcrInstanceId = params.get("TcrInstanceId")
        self._RepoServer = params.get("RepoServer")
        self._RepoType = params.get("RepoType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployApplicationResponse(AbstractModel):
    """DeployApplication response structure.

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
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _BetaBatchNum: Number of pods for the beta batch
        :type BetaBatchNum: int
        :param _DeployStrategyType: Batch deployment policy. `0`: automatically; `1`: manually; `2`: beta batch (manual), `3`: initial release
        :type DeployStrategyType: int
        :param _BatchInterval: Interval between batches
        :type BatchInterval: int
        :param _MinAvailable: The minimum number of available pods
        :type MinAvailable: int
        :param _Force: Whether to enable force release
        :type Force: bool
        """
        self._TotalBatchCount = None
        self._BetaBatchNum = None
        self._DeployStrategyType = None
        self._BatchInterval = None
        self._MinAvailable = None
        self._Force = None

    @property
    def TotalBatchCount(self):
        return self._TotalBatchCount

    @TotalBatchCount.setter
    def TotalBatchCount(self, TotalBatchCount):
        self._TotalBatchCount = TotalBatchCount

    @property
    def BetaBatchNum(self):
        return self._BetaBatchNum

    @BetaBatchNum.setter
    def BetaBatchNum(self, BetaBatchNum):
        self._BetaBatchNum = BetaBatchNum

    @property
    def DeployStrategyType(self):
        return self._DeployStrategyType

    @DeployStrategyType.setter
    def DeployStrategyType(self, DeployStrategyType):
        self._DeployStrategyType = DeployStrategyType

    @property
    def BatchInterval(self):
        return self._BatchInterval

    @BatchInterval.setter
    def BatchInterval(self, BatchInterval):
        self._BatchInterval = BatchInterval

    @property
    def MinAvailable(self):
        return self._MinAvailable

    @MinAvailable.setter
    def MinAvailable(self, MinAvailable):
        self._MinAvailable = MinAvailable

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._TotalBatchCount = params.get("TotalBatchCount")
        self._BetaBatchNum = params.get("BetaBatchNum")
        self._DeployStrategyType = params.get("DeployStrategyType")
        self._BatchInterval = params.get("BatchInterval")
        self._MinAvailable = params.get("MinAvailable")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListRequest(AbstractModel):
    """DescribeApplicationAutoscalerList request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationAutoscalerListResponse(AbstractModel):
    """DescribeApplicationAutoscalerList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Scaling rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: list of Autoscaler
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = Autoscaler()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationInfoRequest(AbstractModel):
    """DescribeApplicationInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationInfoResponse(AbstractModel):
    """DescribeApplicationInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.tem.v20210701.models.TemServiceVersionInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = TemServiceVersionInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationPodsRequest(AbstractModel):
    """DescribeApplicationPods request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
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
        self._EnvironmentId = None
        self._ApplicationId = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._PodName = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
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
        


class DescribeApplicationPodsResponse(AbstractModel):
    """DescribeApplicationPods response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeRunPodPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationServiceListRequest(AbstractModel):
    """DescribeApplicationServiceList request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: ID of the environment
        :type EnvironmentId: str
        :param _ApplicationId: ID of the application
        :type ApplicationId: str
        :param _SourceChannel: xx
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ApplicationId = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationServiceListResponse(AbstractModel):
    """DescribeApplicationServiceList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Application EKS service list
        :type Result: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = EksService()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: ID of the environment
        :type EnvironmentId: str
        :param _Limit: Pagination limit
        :type Limit: int
        :param _Offset: Pagination offset
        :type Offset: int
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _Keyword: Keyword for searching.
        :type Keyword: str
        :param _Filters: Filters for query 
        :type Filters: list of QueryFilter
        :param _SortInfo: Sorting field
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        """
        self._EnvironmentId = None
        self._Limit = None
        self._Offset = None
        self._SourceChannel = None
        self._ApplicationId = None
        self._Keyword = None
        self._Filters = None
        self._SortInfo = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortInfo(self):
        return self._SortInfo

    @SortInfo.setter
    def SortInfo(self, SortInfo):
        self._SortInfo = SortInfo


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceChannel = params.get("SourceChannel")
        self._ApplicationId = params.get("ApplicationId")
        self._Keyword = params.get("Keyword")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortInfo") is not None:
            self._SortInfo = SortType()
            self._SortInfo._deserialize(params.get("SortInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: :class:`tencentcloud.tem.v20210701.models.ServicePage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServicePage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApplicationsStatusRequest(AbstractModel):
    """DescribeApplicationsStatus request structure.

    """

    def __init__(self):
        r"""
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsStatusResponse(AbstractModel):
    """DescribeApplicationsStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: list of ServiceVersionBrief
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigDataListPage(AbstractModel):
    """Query the list of configurations

    """

    def __init__(self):
        r"""
        :param _Records: Record
        :type Records: list of ConfigData
        :param _ContinueToken: Paging cursor
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ContinueToken: str
        :param _RemainingCount: Remaining number
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RemainingCount: int
        """
        self._Records = None
        self._ContinueToken = None
        self._RemainingCount = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken

    @property
    def RemainingCount(self):
        return self._RemainingCount

    @RemainingCount.setter
    def RemainingCount(self, RemainingCount):
        self._RemainingCount = RemainingCount


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = ConfigData()
                obj._deserialize(item)
                self._Records.append(obj)
        self._ContinueToken = params.get("ContinueToken")
        self._RemainingCount = params.get("RemainingCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListRequest(AbstractModel):
    """DescribeConfigDataList request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _ContinueToken: Paging cursor
        :type ContinueToken: str
        :param _Limit: Pagination limit
        :type Limit: int
        """
        self._EnvironmentId = None
        self._SourceChannel = None
        self._ContinueToken = None
        self._Limit = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._ContinueToken = params.get("ContinueToken")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataListResponse(AbstractModel):
    """DescribeConfigDataList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Configuration list.
        :type Result: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListPage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeConfigDataListPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConfigDataRequest(AbstractModel):
    """DescribeConfigData request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigDataResponse(AbstractModel):
    """DescribeConfigData response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Configuration
        :type Result: :class:`tencentcloud.tem.v20210701.models.ConfigData`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ConfigData()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentRequest(AbstractModel):
    """DescribeEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Namespace ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentResponse(AbstractModel):
    """DescribeEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Environment information
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespaceInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = NamespaceInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentStatusRequest(AbstractModel):
    """DescribeEnvironmentStatus request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentIds: ID of the environment
        :type EnvironmentIds: list of str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._EnvironmentIds = None
        self._SourceChannel = None

    @property
    def EnvironmentIds(self):
        return self._EnvironmentIds

    @EnvironmentIds.setter
    def EnvironmentIds(self, EnvironmentIds):
        self._EnvironmentIds = EnvironmentIds

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentIds = params.get("EnvironmentIds")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentStatusResponse(AbstractModel):
    """DescribeEnvironmentStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of environment status
        :type Result: list of NamespaceStatusInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = []
            for item in params.get("Result"):
                obj = NamespaceStatusInfo()
                obj._deserialize(item)
                self._Result.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Pagination limit
        :type Limit: int
        :param _Offset: Page offset
        :type Offset: int
        :param _SourceChannel: Source
        :type SourceChannel: int
        :param _Filters: Filters for query 
        :type Filters: list of QueryFilter
        :param _SortInfo: Sorting field
        :type SortInfo: :class:`tencentcloud.tem.v20210701.models.SortType`
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self._Limit = None
        self._Offset = None
        self._SourceChannel = None
        self._Filters = None
        self._SortInfo = None
        self._EnvironmentId = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortInfo(self):
        return self._SortInfo

    @SortInfo.setter
    def SortInfo(self, SortInfo):
        self._SortInfo = SortInfo

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortInfo") is not None:
            self._SortInfo = SortType()
            self._SortInfo._deserialize(params.get("SortInfo"))
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: :class:`tencentcloud.tem.v20210701.models.NamespacePage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = NamespacePage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIngressRequest(AbstractModel):
    """DescribeIngress request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param _IngressName: Ingress rule name
        :type IngressName: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._IngressName = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._IngressName = params.get("IngressName")
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
        :type Result: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _IngressNames: Ingress rule name list
        :type IngressNames: list of str
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._SourceChannel = None
        self._IngressNames = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def IngressNames(self):
        return self._IngressNames

    @IngressNames.setter
    def IngressNames(self, IngressNames):
        self._IngressNames = IngressNames


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._IngressNames = params.get("IngressNames")
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
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: list of IngressInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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


class DescribeLogConfigRequest(AbstractModel):
    """DescribeLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogConfigResponse(AbstractModel):
    """DescribeLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Configuration
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = LogConfig()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePagedLogConfigListRequest(AbstractModel):
    """DescribePagedLogConfigList request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _Name: Name of the rule
        :type Name: str
        :param _Limit: Number of entries per page. Default value: 20
        :type Limit: int
        :param _ContinueToken: Paging cursor
        :type ContinueToken: str
        """
        self._EnvironmentId = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._Name = None
        self._Limit = None
        self._ContinueToken = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._Name = params.get("Name")
        self._Limit = params.get("Limit")
        self._ContinueToken = params.get("ContinueToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePagedLogConfigListResponse(AbstractModel):
    """DescribePagedLogConfigList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: List of log collecting configurations
        :type Result: :class:`tencentcloud.tem.v20210701.models.LogConfigListPage`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = LogConfigListPage()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeRelatedIngressesRequest(AbstractModel):
    """DescribeRelatedIngresses request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._SourceChannel = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._SourceChannel = params.get("SourceChannel")
        self._ApplicationId = params.get("ApplicationId")
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
        :param _Result: Ingress array
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: list of IngressInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
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
        :param _Offset: Page offset
        :type Offset: int
        :param _Limit: Number of records per page
        :type Limit: int
        :param _TotalCount: Total number of returned records
        :type TotalCount: int
        :param _RequestId: Request ID
        :type RequestId: str
        :param _PodList: List of pods
        :type PodList: list of RunVersionPod
        """
        self._Offset = None
        self._Limit = None
        self._TotalCount = None
        self._RequestId = None
        self._PodList = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def PodList(self):
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
        


class DestroyConfigDataRequest(AbstractModel):
    """DestroyConfigData request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyConfigDataResponse(AbstractModel):
    """DestroyConfigData response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DestroyEnvironmentRequest(AbstractModel):
    """DestroyEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Namespace ID.
        :type EnvironmentId: str
        :param _SourceChannel: Namespace
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyEnvironmentResponse(AbstractModel):
    """DestroyEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DestroyLogConfigRequest(AbstractModel):
    """DestroyLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyLogConfigResponse(AbstractModel):
    """DestroyLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DisableApplicationAutoscalerRequest(AbstractModel):
    """DisableApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApplicationAutoscalerResponse(AbstractModel):
    """DisableApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
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
        :param _ApplicationName: Service name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _VersionName: Version name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VersionName: str
        :param _ClusterIp: Private IP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClusterIp: list of str
        :param _ExternalIp: Public IP
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExternalIp: str
        :param _Type: The access type. Valid values:
- EXTERNAL (internet access)
- VPC (Intra-VPC access)
- CLUSTER (Intra-cluster access)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        :param _SubnetId: Subnet ID. It is filled when the access type is `VPC`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _LoadBalanceId: Load balancer ID. It is filled when the access type is `EXTERNAL` or `CLUSTER`. It’s created automatically by default.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalanceId: str
        :param _PortMappings: Port mapping
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PortMappings: list of PortMapping
        :param _ServicePortMappingList: Details of each type of access configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServicePortMappingList: list of ServicePortMapping
        :param _FlushAll: Flush all types
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FlushAll: bool
        :param _EnableRegistryNextDeploy: `0`: Do not inject. `1`: Inject registry information automatically for the next deployment
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableRegistryNextDeploy: int
        :param _ApplicationId: The application ID returned.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _AllIpDone: Whether all the application IPs are ready
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AllIpDone: bool
        :param _ExternalDomain: CLB domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExternalDomain: str
        """
        self._Name = None
        self._Ports = None
        self._Yaml = None
        self._ApplicationName = None
        self._VersionName = None
        self._ClusterIp = None
        self._ExternalIp = None
        self._Type = None
        self._SubnetId = None
        self._LoadBalanceId = None
        self._PortMappings = None
        self._ServicePortMappingList = None
        self._FlushAll = None
        self._EnableRegistryNextDeploy = None
        self._ApplicationId = None
        self._AllIpDone = None
        self._ExternalDomain = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ClusterIp(self):
        return self._ClusterIp

    @ClusterIp.setter
    def ClusterIp(self, ClusterIp):
        self._ClusterIp = ClusterIp

    @property
    def ExternalIp(self):
        return self._ExternalIp

    @ExternalIp.setter
    def ExternalIp(self, ExternalIp):
        self._ExternalIp = ExternalIp

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def LoadBalanceId(self):
        return self._LoadBalanceId

    @LoadBalanceId.setter
    def LoadBalanceId(self, LoadBalanceId):
        self._LoadBalanceId = LoadBalanceId

    @property
    def PortMappings(self):
        return self._PortMappings

    @PortMappings.setter
    def PortMappings(self, PortMappings):
        self._PortMappings = PortMappings

    @property
    def ServicePortMappingList(self):
        return self._ServicePortMappingList

    @ServicePortMappingList.setter
    def ServicePortMappingList(self, ServicePortMappingList):
        self._ServicePortMappingList = ServicePortMappingList

    @property
    def FlushAll(self):
        return self._FlushAll

    @FlushAll.setter
    def FlushAll(self, FlushAll):
        self._FlushAll = FlushAll

    @property
    def EnableRegistryNextDeploy(self):
        return self._EnableRegistryNextDeploy

    @EnableRegistryNextDeploy.setter
    def EnableRegistryNextDeploy(self, EnableRegistryNextDeploy):
        self._EnableRegistryNextDeploy = EnableRegistryNextDeploy

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def AllIpDone(self):
        return self._AllIpDone

    @AllIpDone.setter
    def AllIpDone(self, AllIpDone):
        self._AllIpDone = AllIpDone

    @property
    def ExternalDomain(self):
        return self._ExternalDomain

    @ExternalDomain.setter
    def ExternalDomain(self, ExternalDomain):
        self._ExternalDomain = ExternalDomain


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Ports = params.get("Ports")
        self._Yaml = params.get("Yaml")
        self._ApplicationName = params.get("ApplicationName")
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
        if params.get("ServicePortMappingList") is not None:
            self._ServicePortMappingList = []
            for item in params.get("ServicePortMappingList"):
                obj = ServicePortMapping()
                obj._deserialize(item)
                self._ServicePortMappingList.append(obj)
        self._FlushAll = params.get("FlushAll")
        self._EnableRegistryNextDeploy = params.get("EnableRegistryNextDeploy")
        self._ApplicationId = params.get("ApplicationId")
        self._AllIpDone = params.get("AllIpDone")
        self._ExternalDomain = params.get("ExternalDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerRequest(AbstractModel):
    """EnableApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Service ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApplicationAutoscalerResponse(AbstractModel):
    """EnableApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class EnablePrometheusConf(AbstractModel):
    """Enable Prometheus monitoring

    """

    def __init__(self):
        r"""
        :param _Port: The listening port of the applicaiton
        :type Port: int
        :param _Path: URL path for monitoring
        :type Path: str
        """
        self._Port = None
        self._Path = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._Path = params.get("Path")
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
        return self._MinAliveInstances

    @MinAliveInstances.setter
    def MinAliveInstances(self, MinAliveInstances):
        self._MinAliveInstances = MinAliveInstances

    @property
    def MaxAliveInstances(self):
        return self._MaxAliveInstances

    @MaxAliveInstances.setter
    def MaxAliveInstances(self, MaxAliveInstances):
        self._MaxAliveInstances = MaxAliveInstances

    @property
    def EsStrategy(self):
        return self._EsStrategy

    @EsStrategy.setter
    def EsStrategy(self, EsStrategy):
        self._EsStrategy = EsStrategy

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def VersionId(self):
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
        


class GenerateApplicationPackageDownloadUrlRequest(AbstractModel):
    """GenerateApplicationPackageDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _PkgName: Package name
        :type PkgName: str
        :param _DeployVersion: Version of the package to download
        :type DeployVersion: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._ApplicationId = None
        self._PkgName = None
        self._DeployVersion = None
        self._SourceChannel = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
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
        


class GenerateApplicationPackageDownloadUrlResponse(AbstractModel):
    """GenerateApplicationPackageDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Temp download URL for the package
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class HealthCheckConfig(AbstractModel):
    """Health check configuration

    """

    def __init__(self):
        r"""
        :param _Type: Health check type. Valid values: `HttpGet`, `TcpSocket`, `Exec`
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Exec(self):
        return self._Exec

    @Exec.setter
    def Exec(self, Exec):
        self._Exec = Exec

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InitialDelaySeconds(self):
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def TimeoutSeconds(self):
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def PeriodSeconds(self):
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
        


class HorizontalAutoscaler(AbstractModel):
    """Auto scaling policy

    """

    def __init__(self):
        r"""
        :param _MinReplicas: (Optional) Minimum number of instances
        :type MinReplicas: int
        :param _MaxReplicas: (Optional) Maximum number of instances
        :type MaxReplicas: int
        :param _Metrics: Metric measurement
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
        :param _Threshold: The value of threshold (integer)
        :type Threshold: int
        :param _Enabled: Whether it is enabled
        :type Enabled: bool
        :param _DoubleThreshold: The value of threshold (demical)
Note: This field may return null, indicating that no valid values can be obtained.
        :type DoubleThreshold: float
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._Metrics = None
        self._Threshold = None
        self._Enabled = None
        self._DoubleThreshold = None

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Threshold(self):
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def DoubleThreshold(self):
        return self._DoubleThreshold

    @DoubleThreshold.setter
    def DoubleThreshold(self, DoubleThreshold):
        self._DoubleThreshold = DoubleThreshold


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._Metrics = params.get("Metrics")
        self._Threshold = params.get("Threshold")
        self._Enabled = params.get("Enabled")
        self._DoubleThreshold = params.get("DoubleThreshold")
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
        :param _EnvironmentId: Environment ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param _ClusterNamespace: Environment namespace
        :type ClusterNamespace: str
        :param _AddressIPVersion: ip version
        :type AddressIPVersion: str
        :param _IngressName: ingress name
        :type IngressName: str
        :param _Rules: Rules configuration
        :type Rules: list of IngressRule
        :param _ClbId: clb ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClbId: str
        :param _Tls: TLS configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tls: list of IngressTls
        :param _ClusterId: Environment cluster ID
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _Vip: clb ip
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Vip: str
        :param _CreateTime: Creation time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _Mixed: Whether to listen on both the HTTP 80 port and HTTPS 443 port. The default value is `false`. The optional value `true` means listening on both the HTTP 80 port and HTTPS 443 port.
        :type Mixed: bool
        :param _RewriteType: Redirection mode. Values:
- `AUTO` (automatically redirect HTTP to HTTPS)
- `NONE` (no redirection)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RewriteType: str
        :param _Domain: CLB domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domain: str
        """
        self._EnvironmentId = None
        self._ClusterNamespace = None
        self._AddressIPVersion = None
        self._IngressName = None
        self._Rules = None
        self._ClbId = None
        self._Tls = None
        self._ClusterId = None
        self._Vip = None
        self._CreateTime = None
        self._Mixed = None
        self._RewriteType = None
        self._Domain = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterNamespace(self):
        return self._ClusterNamespace

    @ClusterNamespace.setter
    def ClusterNamespace(self, ClusterNamespace):
        self._ClusterNamespace = ClusterNamespace

    @property
    def AddressIPVersion(self):
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ClbId(self):
        return self._ClbId

    @ClbId.setter
    def ClbId(self, ClbId):
        self._ClbId = ClbId

    @property
    def Tls(self):
        return self._Tls

    @Tls.setter
    def Tls(self, Tls):
        self._Tls = Tls

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Mixed(self):
        return self._Mixed

    @Mixed.setter
    def Mixed(self, Mixed):
        self._Mixed = Mixed

    @property
    def RewriteType(self):
        return self._RewriteType

    @RewriteType.setter
    def RewriteType(self, RewriteType):
        self._RewriteType = RewriteType

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterNamespace = params.get("ClusterNamespace")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._IngressName = params.get("IngressName")
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
        self._RewriteType = params.get("RewriteType")
        self._Domain = params.get("Domain")
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
        :type Http: :class:`tencentcloud.tem.v20210701.models.IngressRuleValue`
        :param _Host: Host address
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Host: str
        :param _Protocol: Protocol. Options include HTTP and HTTPS. The default option is HTTP.
        :type Protocol: str
        """
        self._Http = None
        self._Host = None
        self._Protocol = None

    @property
    def Http(self):
        return self._Http

    @Http.setter
    def Http(self, Http):
        self._Http = Http

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Protocol(self):
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
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServicePort(self):
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
        :type Backend: :class:`tencentcloud.tem.v20210701.models.IngressRuleBackend`
        """
        self._Path = None
        self._Backend = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Backend(self):
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
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def CertificateId(self):
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
        


class LogConfig(AbstractModel):
    """Log collection configuration

    """

    def __init__(self):
        r"""
        :param _Name: Name.
        :type Name: str
        :param _InputType: Collection type. Values: `container_stdout` (standard); `container_file` (file)
        :type InputType: str
        :param _LogsetId: Logset ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogsetId: str
        :param _TopicId: Log topic ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TopicId: str
        :param _LogType: Log withdrawal mode. Values: `minimalist_log` (full text in a single line); `multiline_log` (full text in multiple lines); `fullregex_log` (regex in a single line); `multiline_fullregex_log` (regex in multiple lines), `json_log` (JSON); 
        :type LogType: str
        :param _BeginningRegex: First line regex. It’s valid when `LogType` is `multiline_log` or `multiline_fullregex_log`.
Note: This field may return `null`, indicating that no valid value was found.
        :type BeginningRegex: str
        :param _LogPath: Directory of files to collect. It’s valid when `InputType` is `container_file`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogPath: str
        :param _FilePattern: Name pattern of files to collect. It’s valid when `InputType` is `container_file`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FilePattern: str
        :param _CreateDate: Creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param _ModifyDate: Update time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ModifyDate: str
        :param _ApplicationId: Application ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _ExtractRule: Export rules
Note: This field may return `null`, indicating that no valid value was found.
        :type ExtractRule: :class:`tencentcloud.tem.v20210701.models.LogConfigExtractRule`
        """
        self._Name = None
        self._InputType = None
        self._LogsetId = None
        self._TopicId = None
        self._LogType = None
        self._BeginningRegex = None
        self._LogPath = None
        self._FilePattern = None
        self._CreateDate = None
        self._ModifyDate = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._ExtractRule = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InputType(self):
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType

    @property
    def BeginningRegex(self):
        return self._BeginningRegex

    @BeginningRegex.setter
    def BeginningRegex(self, BeginningRegex):
        self._BeginningRegex = BeginningRegex

    @property
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def FilePattern(self):
        return self._FilePattern

    @FilePattern.setter
    def FilePattern(self, FilePattern):
        self._FilePattern = FilePattern

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ExtractRule(self):
        return self._ExtractRule

    @ExtractRule.setter
    def ExtractRule(self, ExtractRule):
        self._ExtractRule = ExtractRule


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InputType = params.get("InputType")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._LogType = params.get("LogType")
        self._BeginningRegex = params.get("BeginningRegex")
        self._LogPath = params.get("LogPath")
        self._FilePattern = params.get("FilePattern")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        if params.get("ExtractRule") is not None:
            self._ExtractRule = LogConfigExtractRule()
            self._ExtractRule._deserialize(params.get("ExtractRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigExtractRule(AbstractModel):
    """Configuration of log exporting rule

    """

    def __init__(self):
        r"""
        :param _BeginningRegex: First line regex
Note: This field may return `null`, indicating that no valid value was found.
        :type BeginningRegex: str
        :param _Keys: Withdrawl result
Note: This field may return `null`, indicating that no valid value was found.
        :type Keys: list of str
        :param _FilterKeys: Filter keys
Note: This field may return `null`, indicating that no valid value was found.
        :type FilterKeys: list of str
        :param _FilterRegex: Filter values
Note: This field may return `null`, indicating that no valid value was found.
        :type FilterRegex: list of str
        :param _LogRegex: Log regex
Note: This field may return `null`, indicating that no valid value was found.
        :type LogRegex: str
        :param _TimeKey: Time field
Note: This field may return `null`, indicating that no valid value was found.
        :type TimeKey: str
        :param _TimeFormat: Time Format
Note: This field may return `null`, indicating that no valid value was found.
        :type TimeFormat: str
        :param _UnMatchUpload: - Enable the upload of the log that failed to parse
Note: This field may return `null`, indicating that no valid value was found.
        :type UnMatchUpload: str
        :param _UnMatchedKey: Key of log failed to be parsed
Note: This field may return `null`, indicating that no valid value was found.
        :type UnMatchedKey: str
        :param _Backtracking: tracking
Note: This field may return null, indicating that no valid values can be obtained.
        :type Backtracking: str
        :param _Delimiter: Separator
Note: This field may return null, indicating that no valid values can be obtained.
        :type Delimiter: str
        """
        self._BeginningRegex = None
        self._Keys = None
        self._FilterKeys = None
        self._FilterRegex = None
        self._LogRegex = None
        self._TimeKey = None
        self._TimeFormat = None
        self._UnMatchUpload = None
        self._UnMatchedKey = None
        self._Backtracking = None
        self._Delimiter = None

    @property
    def BeginningRegex(self):
        return self._BeginningRegex

    @BeginningRegex.setter
    def BeginningRegex(self, BeginningRegex):
        self._BeginningRegex = BeginningRegex

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def FilterKeys(self):
        return self._FilterKeys

    @FilterKeys.setter
    def FilterKeys(self, FilterKeys):
        self._FilterKeys = FilterKeys

    @property
    def FilterRegex(self):
        return self._FilterRegex

    @FilterRegex.setter
    def FilterRegex(self, FilterRegex):
        self._FilterRegex = FilterRegex

    @property
    def LogRegex(self):
        return self._LogRegex

    @LogRegex.setter
    def LogRegex(self, LogRegex):
        self._LogRegex = LogRegex

    @property
    def TimeKey(self):
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def UnMatchUpload(self):
        return self._UnMatchUpload

    @UnMatchUpload.setter
    def UnMatchUpload(self, UnMatchUpload):
        self._UnMatchUpload = UnMatchUpload

    @property
    def UnMatchedKey(self):
        return self._UnMatchedKey

    @UnMatchedKey.setter
    def UnMatchedKey(self, UnMatchedKey):
        self._UnMatchedKey = UnMatchedKey

    @property
    def Backtracking(self):
        return self._Backtracking

    @Backtracking.setter
    def Backtracking(self, Backtracking):
        self._Backtracking = Backtracking

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter


    def _deserialize(self, params):
        self._BeginningRegex = params.get("BeginningRegex")
        self._Keys = params.get("Keys")
        self._FilterKeys = params.get("FilterKeys")
        self._FilterRegex = params.get("FilterRegex")
        self._LogRegex = params.get("LogRegex")
        self._TimeKey = params.get("TimeKey")
        self._TimeFormat = params.get("TimeFormat")
        self._UnMatchUpload = params.get("UnMatchUpload")
        self._UnMatchedKey = params.get("UnMatchedKey")
        self._Backtracking = params.get("Backtracking")
        self._Delimiter = params.get("Delimiter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfigListPage(AbstractModel):
    """List of LogConfig

    """

    def __init__(self):
        r"""
        :param _Records: Record
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Records: list of LogConfig
        :param _ContinueToken: Paging cursor
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ContinueToken: str
        """
        self._Records = None
        self._ContinueToken = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def ContinueToken(self):
        return self._ContinueToken

    @ContinueToken.setter
    def ContinueToken(self, ContinueToken):
        self._ContinueToken = ContinueToken


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = LogConfig()
                obj._deserialize(item)
                self._Records.append(obj)
        self._ContinueToken = params.get("ContinueToken")
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
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def ClsLogsetName(self):
        return self._ClsLogsetName

    @ClsLogsetName.setter
    def ClsLogsetName(self, ClsLogsetName):
        self._ClsLogsetName = ClsLogsetName

    @property
    def ClsLogTopicId(self):
        return self._ClsLogTopicId

    @ClsLogTopicId.setter
    def ClsLogTopicId(self, ClsLogTopicId):
        self._ClsLogTopicId = ClsLogTopicId

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def ClsLogTopicName(self):
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
        


class ModifyApplicationAutoscalerRequest(AbstractModel):
    """ModifyApplicationAutoscaler request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _AutoscalerId: Scaling rule ID
        :type AutoscalerId: str
        :param _Autoscaler: Auto scaling policy
        :type Autoscaler: :class:`tencentcloud.tem.v20210701.models.Autoscaler`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._AutoscalerId = None
        self._Autoscaler = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def AutoscalerId(self):
        return self._AutoscalerId

    @AutoscalerId.setter
    def AutoscalerId(self, AutoscalerId):
        self._AutoscalerId = AutoscalerId

    @property
    def Autoscaler(self):
        return self._Autoscaler

    @Autoscaler.setter
    def Autoscaler(self, Autoscaler):
        self._Autoscaler = Autoscaler


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        self._AutoscalerId = params.get("AutoscalerId")
        if params.get("Autoscaler") is not None:
            self._Autoscaler = Autoscaler()
            self._Autoscaler._deserialize(params.get("Autoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationAutoscalerResponse(AbstractModel):
    """ModifyApplicationAutoscaler response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the action is successful
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApplicationInfoRequest(AbstractModel):
    """ModifyApplicationInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _Description: Description
        :type Description: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _EnableTracing: (Disused) Whether to enable the call chain. 
        :type EnableTracing: int
        """
        self._ApplicationId = None
        self._Description = None
        self._SourceChannel = None
        self._EnableTracing = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._Description = params.get("Description")
        self._SourceChannel = params.get("SourceChannel")
        self._EnableTracing = params.get("EnableTracing")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationInfoResponse(AbstractModel):
    """ModifyApplicationInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Success or not
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApplicationServiceRequest(AbstractModel):
    """ModifyApplicationService request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _Service: Full access mode settings
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _Data: Single entry access mode settings
        :type Data: :class:`tencentcloud.tem.v20210701.models.ServicePortMapping`
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._SourceChannel = None
        self._Service = None
        self._Data = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._SourceChannel = params.get("SourceChannel")
        if params.get("Service") is not None:
            self._Service = EksService()
            self._Service._deserialize(params.get("Service"))
        if params.get("Data") is not None:
            self._Data = ServicePortMapping()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationServiceResponse(AbstractModel):
    """ModifyApplicationService response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Whether the action succeeded 
Note: This field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyConfigDataRequest(AbstractModel):
    """ModifyConfigData request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _SourceChannel: Source channel. Please keep the default value.
        :type SourceChannel: int
        :param _Data: Configuration information
        :type Data: list of Pair
        """
        self._EnvironmentId = None
        self._Name = None
        self._SourceChannel = None
        self._Data = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._SourceChannel = params.get("SourceChannel")
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
        


class ModifyConfigDataResponse(AbstractModel):
    """ModifyConfigData response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of the modification
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyEnvironmentRequest(AbstractModel):
    """ModifyEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _EnvironmentName: Environment name
        :type EnvironmentName: str
        :param _Description: Environment description
        :type Description: str
        :param _Vpc: VPC name
        :type Vpc: str
        :param _SubnetIds: Subnets
        :type SubnetIds: list of str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        :param _EnvType: Environment type. Values: `test`, `pre`, `prod`
        :type EnvType: str
        """
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._Description = None
        self._Vpc = None
        self._SubnetIds = None
        self._SourceChannel = None
        self._EnvType = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Description = params.get("Description")
        self._Vpc = params.get("Vpc")
        self._SubnetIds = params.get("SubnetIds")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentResponse(AbstractModel):
    """ModifyEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Environment ID in case of success and `null` in case of failure
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyIngressRequest(AbstractModel):
    """ModifyIngress request structure.

    """

    def __init__(self):
        r"""
        :param _Ingress: Ingress rule configuration
        :type Ingress: :class:`tencentcloud.tem.v20210701.models.IngressInfo`
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._Ingress = None
        self._SourceChannel = None

    @property
    def Ingress(self):
        return self._Ingress

    @Ingress.setter
    def Ingress(self, Ingress):
        self._Ingress = Ingress

    @property
    def SourceChannel(self):
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
        :param _Result: Created successfully.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyLogConfigRequest(AbstractModel):
    """ModifyLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Configuration name
        :type Name: str
        :param _Data: Log collector configuration
        :type Data: :class:`tencentcloud.tem.v20210701.models.LogConfig`
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._Data = None
        self._ApplicationId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        if params.get("Data") is not None:
            self._Data = LogConfig()
            self._Data._deserialize(params.get("Data"))
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLogConfigResponse(AbstractModel):
    """ModifyLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of the modification
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class MountedSettingConf(AbstractModel):
    """Mounting configurations

    """

    def __init__(self):
        r"""
        :param _ConfigDataName: Configuration name
        :type ConfigDataName: str
        :param _MountedPath: Mount point path
        :type MountedPath: str
        :param _Data: Configuration content
        :type Data: list of Pair
        :param _SecretDataName: Encrypt configuration name
        :type SecretDataName: str
        """
        self._ConfigDataName = None
        self._MountedPath = None
        self._Data = None
        self._SecretDataName = None

    @property
    def ConfigDataName(self):
        return self._ConfigDataName

    @ConfigDataName.setter
    def ConfigDataName(self, ConfigDataName):
        self._ConfigDataName = ConfigDataName

    @property
    def MountedPath(self):
        return self._MountedPath

    @MountedPath.setter
    def MountedPath(self, MountedPath):
        self._MountedPath = MountedPath

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def SecretDataName(self):
        return self._SecretDataName

    @SecretDataName.setter
    def SecretDataName(self, SecretDataName):
        self._SecretDataName = SecretDataName


    def _deserialize(self, params):
        self._ConfigDataName = params.get("ConfigDataName")
        self._MountedPath = params.get("MountedPath")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Pair()
                obj._deserialize(item)
                self._Data.append(obj)
        self._SecretDataName = params.get("SecretDataName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfo(AbstractModel):
    """Basic information of the namespace

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: ID
        :type EnvironmentId: str
        :param _NamespaceName: (Disused) Name
        :type NamespaceName: str
        :param _Region: Region
        :type Region: str
        :param _VpcId: vpc id
        :type VpcId: str
        :param _SubnetIds: Array of subnet IDs
        :type SubnetIds: list of str
        :param _Description: Description
        :type Description: str
        :param _CreatedDate: Creation time
        :type CreatedDate: str
        :param _EnvironmentName: Environment name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param _ApmInstanceId: APM instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApmInstanceId: str
        :param _Locked: Whether the environment is locked. `1`: Locked, `0`: Not locked
Note: This field may return null, indicating that no valid values can be obtained.
        :type Locked: int
        :param _Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _EnvType: Environment type. Values: `test`, `pre`, `prod`
Note: This field may return `null`, indicating that no valid value was found.
        :type EnvType: str
        """
        self._EnvironmentId = None
        self._NamespaceName = None
        self._Region = None
        self._VpcId = None
        self._SubnetIds = None
        self._Description = None
        self._CreatedDate = None
        self._EnvironmentName = None
        self._ApmInstanceId = None
        self._Locked = None
        self._Tags = None
        self._EnvType = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedDate(self):
        return self._CreatedDate

    @CreatedDate.setter
    def CreatedDate(self, CreatedDate):
        self._CreatedDate = CreatedDate

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApmInstanceId(self):
        return self._ApmInstanceId

    @ApmInstanceId.setter
    def ApmInstanceId(self, ApmInstanceId):
        self._ApmInstanceId = ApmInstanceId

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._NamespaceName = params.get("NamespaceName")
        self._Region = params.get("Region")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._Description = params.get("Description")
        self._CreatedDate = params.get("CreatedDate")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApmInstanceId = params.get("ApmInstanceId")
        self._Locked = params.get("Locked")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespacePage(AbstractModel):
    """Namespace query result pagination

    """

    def __init__(self):
        r"""
        :param _Records: Details of the returned records
        :type Records: list of TemNamespaceInfo
        :param _Total: Total number of returned records
        :type Total: int
        :param _Size: Number of records per page
        :type Size: int
        :param _Pages: Total number of pages
        :type Pages: int
        :param _Current: Current entry
Note: This field may return null, indicating that no valid values can be obtained.
        :type Current: int
        """
        self._Records = None
        self._Total = None
        self._Size = None
        self._Pages = None
        self._Current = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Current(self):
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current


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
        self._Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceStatusInfo(AbstractModel):
    """Environment status

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: ID of the environment
        :type EnvironmentId: str
        :param _EnvironmentName: Environment name
        :type EnvironmentName: str
        :param _ClusterId: TCB envId | EKS clusterId
        :type ClusterId: str
        :param _ClusterStatus: Environment status
        :type ClusterStatus: str
        :param _EnvironmentStartingStatus: Whether the environment is being started. `null` is returned if it’s not being started.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentStartingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStartingStatus`
        :param _EnvironmentStoppingStatus: Whether the environment is being stopped. `null` is returned if it’s not being stopped.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentStoppingStatus: :class:`tencentcloud.tem.v20210701.models.TemEnvironmentStoppingStatus`
        """
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._ClusterId = None
        self._ClusterStatus = None
        self._EnvironmentStartingStatus = None
        self._EnvironmentStoppingStatus = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def EnvironmentStartingStatus(self):
        return self._EnvironmentStartingStatus

    @EnvironmentStartingStatus.setter
    def EnvironmentStartingStatus(self, EnvironmentStartingStatus):
        self._EnvironmentStartingStatus = EnvironmentStartingStatus

    @property
    def EnvironmentStoppingStatus(self):
        return self._EnvironmentStoppingStatus

    @EnvironmentStoppingStatus.setter
    def EnvironmentStoppingStatus(self, EnvironmentStoppingStatus):
        self._EnvironmentStoppingStatus = EnvironmentStoppingStatus


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ClusterId = params.get("ClusterId")
        self._ClusterStatus = params.get("ClusterStatus")
        if params.get("EnvironmentStartingStatus") is not None:
            self._EnvironmentStartingStatus = TemEnvironmentStartingStatus()
            self._EnvironmentStartingStatus._deserialize(params.get("EnvironmentStartingStatus"))
        if params.get("EnvironmentStoppingStatus") is not None:
            self._EnvironmentStoppingStatus = TemEnvironmentStoppingStatus()
            self._EnvironmentStoppingStatus._deserialize(params.get("EnvironmentStoppingStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInfo(AbstractModel):
    """Node information

    """

    def __init__(self):
        r"""
        :param _Name: Node name
        :type Name: str
        :param _Zone: Availability zone of the node
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Zone: str
        :param _SubnetId: Node subnet ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _AvailableIpCount: Number of available IPs
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AvailableIpCount: str
        :param _Cidr: CIDR block
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Cidr: str
        """
        self._Name = None
        self._Zone = None
        self._SubnetId = None
        self._AvailableIpCount = None
        self._Cidr = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AvailableIpCount(self):
        return self._AvailableIpCount

    @AvailableIpCount.setter
    def AvailableIpCount(self, AvailableIpCount):
        self._AvailableIpCount = AvailableIpCount

    @property
    def Cidr(self):
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Zone = params.get("Zone")
        self._SubnetId = params.get("SubnetId")
        self._AvailableIpCount = params.get("AvailableIpCount")
        self._Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Pair(AbstractModel):
    """Key value pair

    """

    def __init__(self):
        r"""
        :param _Key: Key
        :type Key: str
        :param _Value: Value
        :type Value: str
        :param _Type: `default``: Custom. `reserved`: System variable. `referenced`: Referenced configuration item.
Note: This field may return `null`, indicating that no valid value can be found.
        :type Type: str
        :param _Config: Configuration name
Note: This field may return `null`, indicating that no valid value can be found.
        :type Config: str
        :param _Secret: Encrypt configuration name
Note: This field may return `null`, indicating that no valid value was found.
        :type Secret: str
        """
        self._Key = None
        self._Value = None
        self._Type = None
        self._Config = None
        self._Secret = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        self._Config = params.get("Config")
        self._Secret = params.get("Secret")
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
        :param _TargetPort: Mapped port
        :type TargetPort: int
        :param _Protocol: TCP/UDP protocol stack.
        :type Protocol: str
        :param _ServiceName: K8s service name
        :type ServiceName: str
        """
        self._Port = None
        self._TargetPort = None
        self._Protocol = None
        self._ServiceName = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetPort(self):
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetPort = params.get("TargetPort")
        self._Protocol = params.get("Protocol")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """Filters for query

    """

    def __init__(self):
        r"""
        :param _Name: Name of the field to query
        :type Name: str
        :param _Value: Value of the field to query
        :type Value: list of str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class RestartApplicationPodRequest(AbstractModel):
    """RestartApplicationPod request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _PodName: Name
        :type PodName: str
        :param _Limit: Number of items per page
        :type Limit: int
        :param _Offset: Page offset
        :type Offset: int
        :param _Status: Pod status
        :type Status: str
        :param _SourceChannel: Source channel
        :type SourceChannel: int
        """
        self._EnvironmentId = None
        self._ApplicationId = None
        self._PodName = None
        self._Limit = None
        self._Offset = None
        self._Status = None
        self._SourceChannel = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def PodName(self):
        return self._PodName

    @PodName.setter
    def PodName(self, PodName):
        self._PodName = PodName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ApplicationId = params.get("ApplicationId")
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
        


class RestartApplicationPodResponse(AbstractModel):
    """RestartApplicationPod response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RestartApplicationRequest(AbstractModel):
    """RestartApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _SourceChannel: Retain as default
        :type SourceChannel: int
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartApplicationResponse(AbstractModel):
    """RestartApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RollingUpdateApplicationByVersionRequest(AbstractModel):
    """RollingUpdateApplicationByVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _DeployVersion: Update version. For image-based deployment, it is the value. For deployment with JAR/WAR files, it is `Version`.
        :type DeployVersion: str
        :param _PackageName: JAR/WAR package name. It’s only required for deployment with JAR/WAR files.
        :type PackageName: str
        :param _From: Request source. Options: `IntelliJ`, `Coding`
        :type From: str
        :param _DeployStrategyType: The deployment policy. Values: `AUTO` (automatically deploy), `BETA` (deploy a small batch first to test the result, and deploy the rest automatically) and `MANUAL` (manually deploy)
        :type DeployStrategyType: str
        :param _TotalBatchCount: Total number of batches
        :type TotalBatchCount: int
        :param _BatchInterval: Interval between the batches
        :type BatchInterval: int
        :param _BetaBatchNum: Number of instances in a beta batch
        :type BetaBatchNum: int
        :param _MinAvailable: Minimum number of available instances during the deployment
        :type MinAvailable: int
        :param _Force: Whether to enable force release
        :type Force: bool
        """
        self._ApplicationId = None
        self._EnvironmentId = None
        self._DeployVersion = None
        self._PackageName = None
        self._From = None
        self._DeployStrategyType = None
        self._TotalBatchCount = None
        self._BatchInterval = None
        self._BetaBatchNum = None
        self._MinAvailable = None
        self._Force = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PackageName(self):
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def DeployStrategyType(self):
        return self._DeployStrategyType

    @DeployStrategyType.setter
    def DeployStrategyType(self, DeployStrategyType):
        self._DeployStrategyType = DeployStrategyType

    @property
    def TotalBatchCount(self):
        return self._TotalBatchCount

    @TotalBatchCount.setter
    def TotalBatchCount(self, TotalBatchCount):
        self._TotalBatchCount = TotalBatchCount

    @property
    def BatchInterval(self):
        return self._BatchInterval

    @BatchInterval.setter
    def BatchInterval(self, BatchInterval):
        self._BatchInterval = BatchInterval

    @property
    def BetaBatchNum(self):
        return self._BetaBatchNum

    @BetaBatchNum.setter
    def BetaBatchNum(self, BetaBatchNum):
        self._BetaBatchNum = BetaBatchNum

    @property
    def MinAvailable(self):
        return self._MinAvailable

    @MinAvailable.setter
    def MinAvailable(self, MinAvailable):
        self._MinAvailable = MinAvailable

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._DeployVersion = params.get("DeployVersion")
        self._PackageName = params.get("PackageName")
        self._From = params.get("From")
        self._DeployStrategyType = params.get("DeployStrategyType")
        self._TotalBatchCount = params.get("TotalBatchCount")
        self._BatchInterval = params.get("BatchInterval")
        self._BetaBatchNum = params.get("BetaBatchNum")
        self._MinAvailable = params.get("MinAvailable")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollingUpdateApplicationByVersionResponse(AbstractModel):
    """RollingUpdateApplicationByVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Version ID
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RunVersionPod(AbstractModel):
    """Application pod

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
        :param _PodIp: Pod IP
        :type PodIp: str
        :param _Zone: Availability zone
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Zone: str
        :param _DeployVersion: Deployed version
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeployVersion: str
        :param _RestartCount: Number of restarts
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RestartCount: int
        :param _Ready: Whether the pod is ready
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ready: bool
        :param _ContainerState: Container status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ContainerState: str
        :param _NodeInfo: Information of the node whether the instance locates
Note: This field may return `null`, indicating that no valid value was found.
        :type NodeInfo: :class:`tencentcloud.tem.v20210701.models.NodeInfo`
        :param _StartTime: Start time
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type StartTime: str
        :param _Unhealthy: Whether the status is unhealthy or healthy
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Unhealthy: bool
        :param _UnhealthyWarningMsg: Warning message when the result is unhealthy
Note: This field may return `null`, indicating that no valid value was found.
        :type UnhealthyWarningMsg: str
        :param _VersionId: Version ID
Note: This field may return `null`, indicating that no valid value was found.
        :type VersionId: str
        :param _ApplicationName: Application name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        """
        self._Webshell = None
        self._PodId = None
        self._Status = None
        self._CreateTime = None
        self._PodIp = None
        self._Zone = None
        self._DeployVersion = None
        self._RestartCount = None
        self._Ready = None
        self._ContainerState = None
        self._NodeInfo = None
        self._StartTime = None
        self._Unhealthy = None
        self._UnhealthyWarningMsg = None
        self._VersionId = None
        self._ApplicationName = None

    @property
    def Webshell(self):
        return self._Webshell

    @Webshell.setter
    def Webshell(self, Webshell):
        self._Webshell = Webshell

    @property
    def PodId(self):
        return self._PodId

    @PodId.setter
    def PodId(self, PodId):
        self._PodId = PodId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PodIp(self):
        return self._PodIp

    @PodIp.setter
    def PodIp(self, PodIp):
        self._PodIp = PodIp

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def RestartCount(self):
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def Ready(self):
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def ContainerState(self):
        return self._ContainerState

    @ContainerState.setter
    def ContainerState(self, ContainerState):
        self._ContainerState = ContainerState

    @property
    def NodeInfo(self):
        return self._NodeInfo

    @NodeInfo.setter
    def NodeInfo(self, NodeInfo):
        self._NodeInfo = NodeInfo

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Unhealthy(self):
        return self._Unhealthy

    @Unhealthy.setter
    def Unhealthy(self, Unhealthy):
        self._Unhealthy = Unhealthy

    @property
    def UnhealthyWarningMsg(self):
        return self._UnhealthyWarningMsg

    @UnhealthyWarningMsg.setter
    def UnhealthyWarningMsg(self, UnhealthyWarningMsg):
        self._UnhealthyWarningMsg = UnhealthyWarningMsg

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName


    def _deserialize(self, params):
        self._Webshell = params.get("Webshell")
        self._PodId = params.get("PodId")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._PodIp = params.get("PodIp")
        self._Zone = params.get("Zone")
        self._DeployVersion = params.get("DeployVersion")
        self._RestartCount = params.get("RestartCount")
        self._Ready = params.get("Ready")
        self._ContainerState = params.get("ContainerState")
        if params.get("NodeInfo") is not None:
            self._NodeInfo = NodeInfo()
            self._NodeInfo._deserialize(params.get("NodeInfo"))
        self._StartTime = params.get("StartTime")
        self._Unhealthy = params.get("Unhealthy")
        self._UnhealthyWarningMsg = params.get("UnhealthyWarningMsg")
        self._VersionId = params.get("VersionId")
        self._ApplicationName = params.get("ApplicationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePage(AbstractModel):
    """List of returned applications

    """

    def __init__(self):
        r"""
        :param _Records: List of applications
        :type Records: list of TemService
        :param _Total: Total number of applications
        :type Total: int
        :param _Size: Number of applications per page
        :type Size: int
        :param _Pages: Total number of pages
        :type Pages: int
        :param _Current: Number of current entries
Note: This field may return `null`, indicating that no valid value was found.
        :type Current: int
        """
        self._Records = None
        self._Total = None
        self._Size = None
        self._Pages = None
        self._Current = None

    @property
    def Records(self):
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Pages(self):
        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        self._Pages = Pages

    @property
    def Current(self):
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = TemService()
                obj._deserialize(item)
                self._Records.append(obj)
        self._Total = params.get("Total")
        self._Size = params.get("Size")
        self._Pages = params.get("Pages")
        self._Current = params.get("Current")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMapping(AbstractModel):
    """Port mapping details

    """

    def __init__(self):
        r"""
        :param _Type: Specifies how a layer-4 proxy is created.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        :param _ServiceName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServiceName: str
        :param _ClusterIp: VIP for access within the environment
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterIp: str
        :param _ExternalIp: Cluster external IP
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExternalIp: str
        :param _SubnetId: Subnet ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _VpcId: VPC ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _LoadBalanceId: Load balancer ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LoadBalanceId: str
        :param _Yaml: YAML contents
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Yaml: str
        :param _Ports: List of exposed ports
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Ports: list of int
        :param _PortMappingItemList: Port mapping array 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PortMappingItemList: list of ServicePortMappingItem
        :param _ExternalDomain: CLB domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExternalDomain: str
        """
        self._Type = None
        self._ServiceName = None
        self._ClusterIp = None
        self._ExternalIp = None
        self._SubnetId = None
        self._VpcId = None
        self._LoadBalanceId = None
        self._Yaml = None
        self._Ports = None
        self._PortMappingItemList = None
        self._ExternalDomain = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ClusterIp(self):
        return self._ClusterIp

    @ClusterIp.setter
    def ClusterIp(self, ClusterIp):
        self._ClusterIp = ClusterIp

    @property
    def ExternalIp(self):
        return self._ExternalIp

    @ExternalIp.setter
    def ExternalIp(self, ExternalIp):
        self._ExternalIp = ExternalIp

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def LoadBalanceId(self):
        return self._LoadBalanceId

    @LoadBalanceId.setter
    def LoadBalanceId(self, LoadBalanceId):
        self._LoadBalanceId = LoadBalanceId

    @property
    def Yaml(self):
        return self._Yaml

    @Yaml.setter
    def Yaml(self, Yaml):
        self._Yaml = Yaml

    @property
    def Ports(self):
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def PortMappingItemList(self):
        return self._PortMappingItemList

    @PortMappingItemList.setter
    def PortMappingItemList(self, PortMappingItemList):
        self._PortMappingItemList = PortMappingItemList

    @property
    def ExternalDomain(self):
        return self._ExternalDomain

    @ExternalDomain.setter
    def ExternalDomain(self, ExternalDomain):
        self._ExternalDomain = ExternalDomain


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ServiceName = params.get("ServiceName")
        self._ClusterIp = params.get("ClusterIp")
        self._ExternalIp = params.get("ExternalIp")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._LoadBalanceId = params.get("LoadBalanceId")
        self._Yaml = params.get("Yaml")
        self._Ports = params.get("Ports")
        if params.get("PortMappingItemList") is not None:
            self._PortMappingItemList = []
            for item in params.get("PortMappingItemList"):
                obj = ServicePortMappingItem()
                obj._deserialize(item)
                self._PortMappingItemList.append(obj)
        self._ExternalDomain = params.get("ExternalDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePortMappingItem(AbstractModel):
    """Application port mapping

    """

    def __init__(self):
        r"""
        :param _Port: Application access port
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Port: int
        :param _TargetPort: Application listening port
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TargetPort: int
        :param _Protocol: Protocol type
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Protocol: str
        """
        self._Port = None
        self._TargetPort = None
        self._Protocol = None

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetPort(self):
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort

    @property
    def Protocol(self):
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
        


class ServiceVersionBrief(AbstractModel):
    """List of application versions

    """

    def __init__(self):
        r"""
        :param _VersionName: Version name
        :type VersionName: str
        :param _Status: Status of version
        :type Status: str
        :param _EnableEs: (Disused) Whether to enable elastic scaling
        :type EnableEs: int
        :param _CurrentInstances: Number of current instances
        :type CurrentInstances: int
        :param _VersionId: Version ID
        :type VersionId: str
        :param _LogOutputConf: (Disused) Log output configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param _ExpectedInstances: Expected number of instances
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExpectedInstances: int
        :param _DeployMode: Deployment mode
Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployMode: str
        :param _BuildTaskId: Task ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type BuildTaskId: str
        :param _EnvironmentId: Environment ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param _EnvironmentName: Environment name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param _ApplicationId: Application ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _ApplicationName: Application name
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _UnderDeploying: Whether the application is being deployed
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnderDeploying: bool
        :param _BatchDeployStatus: Status of batch deployment
Note: This field may return `null`, indicating that no valid value was found.
        :type BatchDeployStatus: str
        :param _Zones: Availability zones
Note: This field may return `null`, indicating that no valid value was found.
        :type Zones: list of str
        :param _NodeInfos: Node information
Note: This field may return `null`, indicating that no valid value was found.
        :type NodeInfos: list of NodeInfo
        :param _PodList: Pod information
Note: This field may return `null`, indicating that no valid value was found.
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param _WorkloadInfo: Workload information
Note: This field may return `null`, indicating that no valid value was found.
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param _CreateDate: Creation time
Note: This field may return `null`, indicating that no valid value was found.
        :type CreateDate: str
        :param _RegionId: Region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RegionId: str
        """
        self._VersionName = None
        self._Status = None
        self._EnableEs = None
        self._CurrentInstances = None
        self._VersionId = None
        self._LogOutputConf = None
        self._ExpectedInstances = None
        self._DeployMode = None
        self._BuildTaskId = None
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._UnderDeploying = None
        self._BatchDeployStatus = None
        self._Zones = None
        self._NodeInfos = None
        self._PodList = None
        self._WorkloadInfo = None
        self._CreateDate = None
        self._RegionId = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EnableEs(self):
        return self._EnableEs

    @EnableEs.setter
    def EnableEs(self, EnableEs):
        self._EnableEs = EnableEs

    @property
    def CurrentInstances(self):
        return self._CurrentInstances

    @CurrentInstances.setter
    def CurrentInstances(self, CurrentInstances):
        self._CurrentInstances = CurrentInstances

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def LogOutputConf(self):
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def ExpectedInstances(self):
        return self._ExpectedInstances

    @ExpectedInstances.setter
    def ExpectedInstances(self, ExpectedInstances):
        self._ExpectedInstances = ExpectedInstances

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def BuildTaskId(self):
        return self._BuildTaskId

    @BuildTaskId.setter
    def BuildTaskId(self, BuildTaskId):
        self._BuildTaskId = BuildTaskId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def UnderDeploying(self):
        return self._UnderDeploying

    @UnderDeploying.setter
    def UnderDeploying(self, UnderDeploying):
        self._UnderDeploying = UnderDeploying

    @property
    def BatchDeployStatus(self):
        return self._BatchDeployStatus

    @BatchDeployStatus.setter
    def BatchDeployStatus(self, BatchDeployStatus):
        self._BatchDeployStatus = BatchDeployStatus

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def NodeInfos(self):
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

    @property
    def PodList(self):
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList

    @property
    def WorkloadInfo(self):
        return self._WorkloadInfo

    @WorkloadInfo.setter
    def WorkloadInfo(self, WorkloadInfo):
        self._WorkloadInfo = WorkloadInfo

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._Status = params.get("Status")
        self._EnableEs = params.get("EnableEs")
        self._CurrentInstances = params.get("CurrentInstances")
        self._VersionId = params.get("VersionId")
        if params.get("LogOutputConf") is not None:
            self._LogOutputConf = LogOutputConf()
            self._LogOutputConf._deserialize(params.get("LogOutputConf"))
        self._ExpectedInstances = params.get("ExpectedInstances")
        self._DeployMode = params.get("DeployMode")
        self._BuildTaskId = params.get("BuildTaskId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._UnderDeploying = params.get("UnderDeploying")
        self._BatchDeployStatus = params.get("BatchDeployStatus")
        self._Zones = params.get("Zones")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        if params.get("PodList") is not None:
            self._PodList = DescribeRunPodPage()
            self._PodList._deserialize(params.get("PodList"))
        if params.get("WorkloadInfo") is not None:
            self._WorkloadInfo = WorkloadInfo()
            self._WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self._CreateDate = params.get("CreateDate")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortType(AbstractModel):
    """Query filter

    """

    def __init__(self):
        r"""
        :param _Key: Name of the sorting field
        :type Key: str
        :param _Type: `0`: Ascending; `1`: Descending 
        :type Type: int
        """
        self._Key = None
        self._Type = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationRequest(AbstractModel):
    """StopApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _SourceChannel: Retain as default
        :type SourceChannel: int
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self._ApplicationId = None
        self._SourceChannel = None
        self._EnvironmentId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def SourceChannel(self):
        return self._SourceChannel

    @SourceChannel.setter
    def SourceChannel(self, SourceChannel):
        self._SourceChannel = SourceChannel

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._SourceChannel = params.get("SourceChannel")
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopApplicationResponse(AbstractModel):
    """StopApplication response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned result
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


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
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageVolIp: str
        """
        self._StorageVolName = None
        self._StorageVolPath = None
        self._StorageVolIp = None

    @property
    def StorageVolName(self):
        return self._StorageVolName

    @StorageVolName.setter
    def StorageVolName(self, StorageVolName):
        self._StorageVolName = StorageVolName

    @property
    def StorageVolPath(self):
        return self._StorageVolPath

    @StorageVolPath.setter
    def StorageVolPath(self, StorageVolPath):
        self._StorageVolPath = StorageVolPath

    @property
    def StorageVolIp(self):
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
        return self._VolumeName

    @VolumeName.setter
    def VolumeName(self, VolumeName):
        self._VolumeName = VolumeName

    @property
    def MountPath(self):
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
        


class Tag(AbstractModel):
    """Information of tags

    """

    def __init__(self):
        r"""
        :param _TagKey: The tag key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: The tag value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStartingStatus(AbstractModel):
    """Environment startup processes (Only applications started by the environment startup)

    """

    def __init__(self):
        r"""
        :param _ApplicationNumNeedToStart: Number of applications to start
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationNumNeedToStart: int
        :param _StartedApplicationNum: Number of started applictions
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StartedApplicationNum: int
        :param _StartFailedApplicationNum: Number of applications failed to be started
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StartFailedApplicationNum: int
        """
        self._ApplicationNumNeedToStart = None
        self._StartedApplicationNum = None
        self._StartFailedApplicationNum = None

    @property
    def ApplicationNumNeedToStart(self):
        return self._ApplicationNumNeedToStart

    @ApplicationNumNeedToStart.setter
    def ApplicationNumNeedToStart(self, ApplicationNumNeedToStart):
        self._ApplicationNumNeedToStart = ApplicationNumNeedToStart

    @property
    def StartedApplicationNum(self):
        return self._StartedApplicationNum

    @StartedApplicationNum.setter
    def StartedApplicationNum(self, StartedApplicationNum):
        self._StartedApplicationNum = StartedApplicationNum

    @property
    def StartFailedApplicationNum(self):
        return self._StartFailedApplicationNum

    @StartFailedApplicationNum.setter
    def StartFailedApplicationNum(self, StartFailedApplicationNum):
        self._StartFailedApplicationNum = StartFailedApplicationNum


    def _deserialize(self, params):
        self._ApplicationNumNeedToStart = params.get("ApplicationNumNeedToStart")
        self._StartedApplicationNum = params.get("StartedApplicationNum")
        self._StartFailedApplicationNum = params.get("StartFailedApplicationNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemEnvironmentStoppingStatus(AbstractModel):
    """Processes stopped by the environment (Only applications stopped by the action of stopping the environment)

    """

    def __init__(self):
        r"""
        :param _ApplicationNumNeedToStop: Number of applications to stop
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationNumNeedToStop: int
        :param _StoppedApplicationNum: Number of stopped applications
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StoppedApplicationNum: int
        :param _StopFailedApplicationNum: Number of applications failed to be stopped
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StopFailedApplicationNum: int
        """
        self._ApplicationNumNeedToStop = None
        self._StoppedApplicationNum = None
        self._StopFailedApplicationNum = None

    @property
    def ApplicationNumNeedToStop(self):
        return self._ApplicationNumNeedToStop

    @ApplicationNumNeedToStop.setter
    def ApplicationNumNeedToStop(self, ApplicationNumNeedToStop):
        self._ApplicationNumNeedToStop = ApplicationNumNeedToStop

    @property
    def StoppedApplicationNum(self):
        return self._StoppedApplicationNum

    @StoppedApplicationNum.setter
    def StoppedApplicationNum(self, StoppedApplicationNum):
        self._StoppedApplicationNum = StoppedApplicationNum

    @property
    def StopFailedApplicationNum(self):
        return self._StopFailedApplicationNum

    @StopFailedApplicationNum.setter
    def StopFailedApplicationNum(self, StopFailedApplicationNum):
        self._StopFailedApplicationNum = StopFailedApplicationNum


    def _deserialize(self, params):
        self._ApplicationNumNeedToStop = params.get("ApplicationNumNeedToStop")
        self._StoppedApplicationNum = params.get("StoppedApplicationNum")
        self._StopFailedApplicationNum = params.get("StopFailedApplicationNum")
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
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Channel: Channel
        :type Channel: str
        :param _EnvironmentName: Environment name
        :type EnvironmentName: str
        :param _Region: Region name
        :type Region: str
        :param _Description: Environment description
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param _Status: Status. `1`: terminated; `0`: normal
        :type Status: int
        :param _Vpc: VPC network
        :type Vpc: str
        :param _CreateDate: Creation time
        :type CreateDate: str
        :param _ModifyDate: Modification time
        :type ModifyDate: str
        :param _Modifier: Modifier
        :type Modifier: str
        :param _Creator: Creator
        :type Creator: str
        :param _ApplicationNum: Number of applications
        :type ApplicationNum: int
        :param _RunInstancesNum: Number of running instances
        :type RunInstancesNum: int
        :param _SubnetId: Subnet
        :type SubnetId: str
        :param _ClusterStatus: Environment cluster status
        :type ClusterStatus: str
        :param _EnableTswTraceService: Whether to enable TSW
        :type EnableTswTraceService: bool
        :param _Locked: Whether the environment is locked. `1`: locked; `0`: not locked
        :type Locked: int
        :param _AppId: User AppId
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: str
        :param _Uin: User UIN
Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _SubAccountUin: The UIN of sub-account
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubAccountUin: str
        :param _ClusterId: Application ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _Tags: Tag.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _HasAuthority: Whether it’s authorized to access the resource
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasAuthority: bool
        :param _EnvType: Environment type. Values: `test`, `pre`, `prod`
Note: This field may return `null`, indicating that no valid value was found.
        :type EnvType: str
        :param _RegionId: Region code
Note: This field may return `null`, indicating that no valid value was found.
        :type RegionId: str
        """
        self._EnvironmentId = None
        self._Channel = None
        self._EnvironmentName = None
        self._Region = None
        self._Description = None
        self._Status = None
        self._Vpc = None
        self._CreateDate = None
        self._ModifyDate = None
        self._Modifier = None
        self._Creator = None
        self._ApplicationNum = None
        self._RunInstancesNum = None
        self._SubnetId = None
        self._ClusterStatus = None
        self._EnableTswTraceService = None
        self._Locked = None
        self._AppId = None
        self._Uin = None
        self._SubAccountUin = None
        self._ClusterId = None
        self._Tags = None
        self._HasAuthority = None
        self._EnvType = None
        self._RegionId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def Modifier(self):
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def ApplicationNum(self):
        return self._ApplicationNum

    @ApplicationNum.setter
    def ApplicationNum(self, ApplicationNum):
        self._ApplicationNum = ApplicationNum

    @property
    def RunInstancesNum(self):
        return self._RunInstancesNum

    @RunInstancesNum.setter
    def RunInstancesNum(self, RunInstancesNum):
        self._RunInstancesNum = RunInstancesNum

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def EnableTswTraceService(self):
        return self._EnableTswTraceService

    @EnableTswTraceService.setter
    def EnableTswTraceService(self, EnableTswTraceService):
        self._EnableTswTraceService = EnableTswTraceService

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HasAuthority(self):
        return self._HasAuthority

    @HasAuthority.setter
    def HasAuthority(self, HasAuthority):
        self._HasAuthority = HasAuthority

    @property
    def EnvType(self):
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Channel = params.get("Channel")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Region = params.get("Region")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Vpc = params.get("Vpc")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        self._ApplicationNum = params.get("ApplicationNum")
        self._RunInstancesNum = params.get("RunInstancesNum")
        self._SubnetId = params.get("SubnetId")
        self._ClusterStatus = params.get("ClusterStatus")
        self._EnableTswTraceService = params.get("EnableTswTraceService")
        self._Locked = params.get("Locked")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._SubAccountUin = params.get("SubAccountUin")
        self._ClusterId = params.get("ClusterId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HasAuthority = params.get("HasAuthority")
        self._EnvType = params.get("EnvType")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemService(AbstractModel):
    """Application details

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Version ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationId: str
        :param _ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _Description: Description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Description: str
        :param _EnvironmentId: ID of the environment
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param _CreateDate: Creation time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CreateDate: str
        :param _ModifyDate: Modification time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ModifyDate: str
        :param _Modifier: Modifier
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Modifier: str
        :param _Creator: Creator account
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Creator: str
        :param _RepoType: TCR Individual or TCR Enterprise
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoType: int
        :param _InstanceId: ID of the TCR Enterprise instance
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _RepoName: Name of the TCR instance
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoName: str
        :param _CodingLanguage: Programming Language
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CodingLanguage: str
        :param _DeployMode: Deployment mode
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DeployMode: str
        :param _EnvironmentName: Environment name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param _ActiveVersions: The instance information where the application is running
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ActiveVersions: list of ServiceVersionBrief
        :param _EnableTracing: Whether to enable link tracing
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableTracing: int
        :param _Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _HasAuthority: Whether it’s authorized to access the resource
Note: This field may return null, indicating that no valid values can be obtained.
        :type HasAuthority: bool
        """
        self._ApplicationId = None
        self._ApplicationName = None
        self._Description = None
        self._EnvironmentId = None
        self._CreateDate = None
        self._ModifyDate = None
        self._Modifier = None
        self._Creator = None
        self._RepoType = None
        self._InstanceId = None
        self._RepoName = None
        self._CodingLanguage = None
        self._DeployMode = None
        self._EnvironmentName = None
        self._ActiveVersions = None
        self._EnableTracing = None
        self._Tags = None
        self._HasAuthority = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def Modifier(self):
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RepoName(self):
        return self._RepoName

    @RepoName.setter
    def RepoName(self, RepoName):
        self._RepoName = RepoName

    @property
    def CodingLanguage(self):
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ActiveVersions(self):
        return self._ActiveVersions

    @ActiveVersions.setter
    def ActiveVersions(self, ActiveVersions):
        self._ActiveVersions = ActiveVersions

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HasAuthority(self):
        return self._HasAuthority

    @HasAuthority.setter
    def HasAuthority(self, HasAuthority):
        self._HasAuthority = HasAuthority


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._Description = params.get("Description")
        self._EnvironmentId = params.get("EnvironmentId")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        self._RepoType = params.get("RepoType")
        self._InstanceId = params.get("InstanceId")
        self._RepoName = params.get("RepoName")
        self._CodingLanguage = params.get("CodingLanguage")
        self._DeployMode = params.get("DeployMode")
        self._EnvironmentName = params.get("EnvironmentName")
        if params.get("ActiveVersions") is not None:
            self._ActiveVersions = []
            for item in params.get("ActiveVersions"):
                obj = ServiceVersionBrief()
                obj._deserialize(item)
                self._ActiveVersions.append(obj)
        self._EnableTracing = params.get("EnableTracing")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HasAuthority = params.get("HasAuthority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemServiceVersionInfo(AbstractModel):
    """Version information

    """

    def __init__(self):
        r"""
        :param _VersionId: Version ID
        :type VersionId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _DeployMode: Deployment mode
        :type DeployMode: str
        :param _JdkVersion: JDK version
        :type JdkVersion: str
        :param _Description: Description
        :type Description: str
        :param _DeployVersion: Deployed version
        :type DeployVersion: str
        :param _PublishMode: Publish mode
        :type PublishMode: str
        :param _JvmOpts: Launch parameter
        :type JvmOpts: str
        :param _InitPodNum: Number of initial pods
        :type InitPodNum: int
        :param _CpuSpec: CPU specification
        :type CpuSpec: float
        :param _MemorySpec: Memory specification
        :type MemorySpec: float
        :param _ImgRepo: Image path
        :type ImgRepo: str
        :param _ImgName: Image name
        :type ImgName: str
        :param _ImgVersion: Image version
        :type ImgVersion: str
        :param _EsInfo: Scaling configuration
Note: This field may return null, indicating that no valid values can be obtained.
        :type EsInfo: :class:`tencentcloud.tem.v20210701.models.EsInfo`
        :param _EnvConf: Environment configuration
        :type EnvConf: list of Pair
        :param _StorageConfs: Storage configuration
        :type StorageConfs: list of StorageConf
        :param _Status: Running status
        :type Status: str
        :param _Vpc: VPC
        :type Vpc: str
        :param _SubnetId: Subnets
        :type SubnetId: str
        :param _CreateDate: Creation time
        :type CreateDate: str
        :param _ModifyDate: Modification time
        :type ModifyDate: str
        :param _StorageMountConfs: Mounting configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StorageMountConfs: list of StorageMountConf
        :param _VersionName: Version name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VersionName: str
        :param _LogOutputConf: Log output configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogOutputConf: :class:`tencentcloud.tem.v20210701.models.LogOutputConf`
        :param _ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _ApplicationDescription: Application description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationDescription: str
        :param _EnvironmentName: Environment name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentName: str
        :param _EnvironmentId: Environment ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param _PublicDomain: Public network address
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PublicDomain: str
        :param _EnablePublicAccess: Whether to enable public network access
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnablePublicAccess: bool
        :param _CurrentInstances: Number of current instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CurrentInstances: int
        :param _ExpectedInstances: Number of expected instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExpectedInstances: int
        :param _CodingLanguage: Programming Language
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CodingLanguage: str
        :param _PkgName: Program package name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PkgName: str
        :param _EsEnable: Whether to enable auto scaling
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EsEnable: int
        :param _EsStrategy: Auto scaling policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EsStrategy: int
        :param _ImageTag: Image tag
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageTag: str
        :param _LogEnable: Whether to enable logging
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogEnable: int
        :param _MinAliveInstances: Minimum number of instances
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MinAliveInstances: str
        :param _SecurityGroupIds: Security group IDs
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroupIds: list of str
        :param _ImageCommand: Image command
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageCommand: str
        :param _ImageArgs: Image command parameters
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageArgs: list of str
        :param _UseRegistryDefaultConfig: Whether to use the default registry configurations
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UseRegistryDefaultConfig: bool
        :param _Service: EKS access configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Service: :class:`tencentcloud.tem.v20210701.models.EksService`
        :param _SettingConfs: Mounting configurations
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SettingConfs: list of MountedSettingConf
        :param _LogConfs: Log path information
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LogConfs: list of str
        :param _PostStart: The script to execute right after the startup
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PostStart: str
        :param _PreStop: The script to run before stop
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PreStop: str
        :param _Liveness: Configuration of aliveness probe
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Liveness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _Readiness: Configuration of readiness probe
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Readiness: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _HorizontalAutoscaler: Auto scaling policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HorizontalAutoscaler: list of HorizontalAutoscaler
        :param _CronHorizontalAutoscaler: Scheduled auto scaling policy
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CronHorizontalAutoscaler: list of CronHorizontalAutoscaler
        :param _Zones: Availability zone of the application
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Zones: list of str
        :param _LastDeployDate: The latest deployment time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastDeployDate: str
        :param _LastDeploySuccessDate: The latest successful deployment time
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastDeploySuccessDate: str
        :param _NodeInfos: Information of the node whether the application is deployed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type NodeInfos: list of NodeInfo
        :param _ImageType: Image type. Values: `0` (Demo image), `1` (Normal image)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ImageType: int
        :param _EnableTracing: Whether to 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type EnableTracing: int
        :param _EnableTracingReport: (Disused) Whether to enable linkage tracing and report. It only takes effect when EnableTracing = `1`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableTracingReport: int
        :param _RepoType: Image type. `0`: Individual image; `1`: Enterprise image; `2`: Public image
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoType: int
        :param _BatchDeployStatus: Status of batch deployment: `batch_updating`, `batch_updating_waiting_confirm`
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BatchDeployStatus: str
        :param _ApmInstanceId: APM instance ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApmInstanceId: str
        :param _WorkloadInfo: Workload information 
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type WorkloadInfo: :class:`tencentcloud.tem.v20210701.models.WorkloadInfo`
        :param _SpeedUp: Whether to enable application acceleration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SpeedUp: bool
        :param _StartupProbe: Configuration of the startup probe
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StartupProbe: :class:`tencentcloud.tem.v20210701.models.HealthCheckConfig`
        :param _OsFlavour: OS version. Values:
- ALPINE
- CENTOS
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OsFlavour: str
        :param _RepoServer: Image repository server
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RepoServer: str
        :param _UnderDeploying: Whether the application is being deployed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UnderDeploying: bool
        :param _EnablePrometheusConf: Whether to enable application metric monitoring 
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnablePrometheusConf: :class:`tencentcloud.tem.v20210701.models.EnablePrometheusConf`
        :param _StoppedManually: Whether it’s stopped manually
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StoppedManually: bool
        :param _TcrInstanceId: TCR instance ID
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TcrInstanceId: str
        :param _EnableMetrics: `1`: Automatically enable metrics collection (open-telemetry)
`0`: Disable metrics collection
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableMetrics: int
        :param _AppId: User AppId
Note: This field may return `null`, indicating that no valid value was found.
        :type AppId: str
        :param _SubAccountUin: Sub Account UIN
Note: This field may return `null`, indicating that no valid value was found.
        :type SubAccountUin: str
        :param _Uin: User UIN
Note: This field may return `null`, indicating that no valid value was found.
        :type Uin: str
        :param _Region: Region
Note: This field may return `null`, indicating that no valid value was found.
        :type Region: str
        :param _GroupId: Application group ID
Note: This field may return `null`, indicating that no valid value was found.
        :type GroupId: str
        :param _EnableRegistry: Whether to enable registry
Note: This field may return `null`, indicating that no valid value was found.
        :type EnableRegistry: int
        :param _AutoscalerList: Array of scaling rules
Note: This field may return `null`, indicating that no valid value was found.
        :type AutoscalerList: list of Autoscaler
        :param _Modifier: Modifier
Note: This field may return `null`, indicating that no valid value was found.
        :type Modifier: str
        :param _Creator: Creator
Note: This field may return `null`, indicating that no valid value was found.
        :type Creator: str
        :param _DeployStrategyConf: Deployment strategy
Note: This field may return `null`, indicating that no valid value was found.
        :type DeployStrategyConf: :class:`tencentcloud.tem.v20210701.models.DeployStrategyConf`
        :param _PodList: List of pods
Note: This field may return `null`, indicating that no valid value was found.
        :type PodList: :class:`tencentcloud.tem.v20210701.models.DescribeRunPodPage`
        :param _ConfEdited: Whether the configuration has been changed during deployment
Note: This field may return `null`, indicating that no valid value was found.
        :type ConfEdited: bool
        :param _Tags: Tag
Note: This field may return `null`, indicating that no valid value was found.
        :type Tags: list of Tag
        :param _PreStopEncoded: Whether to encode
Note: This field may return null, indicating that no valid values can be obtained.
        :type PreStopEncoded: str
        :param _PostStartEncoded: Whether to encode
Note: This field may return null, indicating that no valid values can be obtained.
        :type PostStartEncoded: str
        """
        self._VersionId = None
        self._ApplicationId = None
        self._DeployMode = None
        self._JdkVersion = None
        self._Description = None
        self._DeployVersion = None
        self._PublishMode = None
        self._JvmOpts = None
        self._InitPodNum = None
        self._CpuSpec = None
        self._MemorySpec = None
        self._ImgRepo = None
        self._ImgName = None
        self._ImgVersion = None
        self._EsInfo = None
        self._EnvConf = None
        self._StorageConfs = None
        self._Status = None
        self._Vpc = None
        self._SubnetId = None
        self._CreateDate = None
        self._ModifyDate = None
        self._StorageMountConfs = None
        self._VersionName = None
        self._LogOutputConf = None
        self._ApplicationName = None
        self._ApplicationDescription = None
        self._EnvironmentName = None
        self._EnvironmentId = None
        self._PublicDomain = None
        self._EnablePublicAccess = None
        self._CurrentInstances = None
        self._ExpectedInstances = None
        self._CodingLanguage = None
        self._PkgName = None
        self._EsEnable = None
        self._EsStrategy = None
        self._ImageTag = None
        self._LogEnable = None
        self._MinAliveInstances = None
        self._SecurityGroupIds = None
        self._ImageCommand = None
        self._ImageArgs = None
        self._UseRegistryDefaultConfig = None
        self._Service = None
        self._SettingConfs = None
        self._LogConfs = None
        self._PostStart = None
        self._PreStop = None
        self._Liveness = None
        self._Readiness = None
        self._HorizontalAutoscaler = None
        self._CronHorizontalAutoscaler = None
        self._Zones = None
        self._LastDeployDate = None
        self._LastDeploySuccessDate = None
        self._NodeInfos = None
        self._ImageType = None
        self._EnableTracing = None
        self._EnableTracingReport = None
        self._RepoType = None
        self._BatchDeployStatus = None
        self._ApmInstanceId = None
        self._WorkloadInfo = None
        self._SpeedUp = None
        self._StartupProbe = None
        self._OsFlavour = None
        self._RepoServer = None
        self._UnderDeploying = None
        self._EnablePrometheusConf = None
        self._StoppedManually = None
        self._TcrInstanceId = None
        self._EnableMetrics = None
        self._AppId = None
        self._SubAccountUin = None
        self._Uin = None
        self._Region = None
        self._GroupId = None
        self._EnableRegistry = None
        self._AutoscalerList = None
        self._Modifier = None
        self._Creator = None
        self._DeployStrategyConf = None
        self._PodList = None
        self._ConfEdited = None
        self._Tags = None
        self._PreStopEncoded = None
        self._PostStartEncoded = None

    @property
    def VersionId(self):
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def JdkVersion(self):
        return self._JdkVersion

    @JdkVersion.setter
    def JdkVersion(self, JdkVersion):
        self._JdkVersion = JdkVersion

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DeployVersion(self):
        return self._DeployVersion

    @DeployVersion.setter
    def DeployVersion(self, DeployVersion):
        self._DeployVersion = DeployVersion

    @property
    def PublishMode(self):
        return self._PublishMode

    @PublishMode.setter
    def PublishMode(self, PublishMode):
        self._PublishMode = PublishMode

    @property
    def JvmOpts(self):
        return self._JvmOpts

    @JvmOpts.setter
    def JvmOpts(self, JvmOpts):
        self._JvmOpts = JvmOpts

    @property
    def InitPodNum(self):
        return self._InitPodNum

    @InitPodNum.setter
    def InitPodNum(self, InitPodNum):
        self._InitPodNum = InitPodNum

    @property
    def CpuSpec(self):
        return self._CpuSpec

    @CpuSpec.setter
    def CpuSpec(self, CpuSpec):
        self._CpuSpec = CpuSpec

    @property
    def MemorySpec(self):
        return self._MemorySpec

    @MemorySpec.setter
    def MemorySpec(self, MemorySpec):
        self._MemorySpec = MemorySpec

    @property
    def ImgRepo(self):
        return self._ImgRepo

    @ImgRepo.setter
    def ImgRepo(self, ImgRepo):
        self._ImgRepo = ImgRepo

    @property
    def ImgName(self):
        return self._ImgName

    @ImgName.setter
    def ImgName(self, ImgName):
        self._ImgName = ImgName

    @property
    def ImgVersion(self):
        return self._ImgVersion

    @ImgVersion.setter
    def ImgVersion(self, ImgVersion):
        self._ImgVersion = ImgVersion

    @property
    def EsInfo(self):
        return self._EsInfo

    @EsInfo.setter
    def EsInfo(self, EsInfo):
        self._EsInfo = EsInfo

    @property
    def EnvConf(self):
        return self._EnvConf

    @EnvConf.setter
    def EnvConf(self, EnvConf):
        self._EnvConf = EnvConf

    @property
    def StorageConfs(self):
        return self._StorageConfs

    @StorageConfs.setter
    def StorageConfs(self, StorageConfs):
        self._StorageConfs = StorageConfs

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Vpc(self):
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def ModifyDate(self):
        return self._ModifyDate

    @ModifyDate.setter
    def ModifyDate(self, ModifyDate):
        self._ModifyDate = ModifyDate

    @property
    def StorageMountConfs(self):
        return self._StorageMountConfs

    @StorageMountConfs.setter
    def StorageMountConfs(self, StorageMountConfs):
        self._StorageMountConfs = StorageMountConfs

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def LogOutputConf(self):
        return self._LogOutputConf

    @LogOutputConf.setter
    def LogOutputConf(self, LogOutputConf):
        self._LogOutputConf = LogOutputConf

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationDescription(self):
        return self._ApplicationDescription

    @ApplicationDescription.setter
    def ApplicationDescription(self, ApplicationDescription):
        self._ApplicationDescription = ApplicationDescription

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def PublicDomain(self):
        return self._PublicDomain

    @PublicDomain.setter
    def PublicDomain(self, PublicDomain):
        self._PublicDomain = PublicDomain

    @property
    def EnablePublicAccess(self):
        return self._EnablePublicAccess

    @EnablePublicAccess.setter
    def EnablePublicAccess(self, EnablePublicAccess):
        self._EnablePublicAccess = EnablePublicAccess

    @property
    def CurrentInstances(self):
        return self._CurrentInstances

    @CurrentInstances.setter
    def CurrentInstances(self, CurrentInstances):
        self._CurrentInstances = CurrentInstances

    @property
    def ExpectedInstances(self):
        return self._ExpectedInstances

    @ExpectedInstances.setter
    def ExpectedInstances(self, ExpectedInstances):
        self._ExpectedInstances = ExpectedInstances

    @property
    def CodingLanguage(self):
        return self._CodingLanguage

    @CodingLanguage.setter
    def CodingLanguage(self, CodingLanguage):
        self._CodingLanguage = CodingLanguage

    @property
    def PkgName(self):
        return self._PkgName

    @PkgName.setter
    def PkgName(self, PkgName):
        self._PkgName = PkgName

    @property
    def EsEnable(self):
        return self._EsEnable

    @EsEnable.setter
    def EsEnable(self, EsEnable):
        self._EsEnable = EsEnable

    @property
    def EsStrategy(self):
        return self._EsStrategy

    @EsStrategy.setter
    def EsStrategy(self, EsStrategy):
        self._EsStrategy = EsStrategy

    @property
    def ImageTag(self):
        return self._ImageTag

    @ImageTag.setter
    def ImageTag(self, ImageTag):
        self._ImageTag = ImageTag

    @property
    def LogEnable(self):
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def MinAliveInstances(self):
        return self._MinAliveInstances

    @MinAliveInstances.setter
    def MinAliveInstances(self, MinAliveInstances):
        self._MinAliveInstances = MinAliveInstances

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ImageCommand(self):
        return self._ImageCommand

    @ImageCommand.setter
    def ImageCommand(self, ImageCommand):
        self._ImageCommand = ImageCommand

    @property
    def ImageArgs(self):
        return self._ImageArgs

    @ImageArgs.setter
    def ImageArgs(self, ImageArgs):
        self._ImageArgs = ImageArgs

    @property
    def UseRegistryDefaultConfig(self):
        return self._UseRegistryDefaultConfig

    @UseRegistryDefaultConfig.setter
    def UseRegistryDefaultConfig(self, UseRegistryDefaultConfig):
        self._UseRegistryDefaultConfig = UseRegistryDefaultConfig

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def SettingConfs(self):
        return self._SettingConfs

    @SettingConfs.setter
    def SettingConfs(self, SettingConfs):
        self._SettingConfs = SettingConfs

    @property
    def LogConfs(self):
        return self._LogConfs

    @LogConfs.setter
    def LogConfs(self, LogConfs):
        self._LogConfs = LogConfs

    @property
    def PostStart(self):
        return self._PostStart

    @PostStart.setter
    def PostStart(self, PostStart):
        self._PostStart = PostStart

    @property
    def PreStop(self):
        return self._PreStop

    @PreStop.setter
    def PreStop(self, PreStop):
        self._PreStop = PreStop

    @property
    def Liveness(self):
        return self._Liveness

    @Liveness.setter
    def Liveness(self, Liveness):
        self._Liveness = Liveness

    @property
    def Readiness(self):
        return self._Readiness

    @Readiness.setter
    def Readiness(self, Readiness):
        self._Readiness = Readiness

    @property
    def HorizontalAutoscaler(self):
        return self._HorizontalAutoscaler

    @HorizontalAutoscaler.setter
    def HorizontalAutoscaler(self, HorizontalAutoscaler):
        self._HorizontalAutoscaler = HorizontalAutoscaler

    @property
    def CronHorizontalAutoscaler(self):
        return self._CronHorizontalAutoscaler

    @CronHorizontalAutoscaler.setter
    def CronHorizontalAutoscaler(self, CronHorizontalAutoscaler):
        self._CronHorizontalAutoscaler = CronHorizontalAutoscaler

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def LastDeployDate(self):
        return self._LastDeployDate

    @LastDeployDate.setter
    def LastDeployDate(self, LastDeployDate):
        self._LastDeployDate = LastDeployDate

    @property
    def LastDeploySuccessDate(self):
        return self._LastDeploySuccessDate

    @LastDeploySuccessDate.setter
    def LastDeploySuccessDate(self, LastDeploySuccessDate):
        self._LastDeploySuccessDate = LastDeploySuccessDate

    @property
    def NodeInfos(self):
        return self._NodeInfos

    @NodeInfos.setter
    def NodeInfos(self, NodeInfos):
        self._NodeInfos = NodeInfos

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def EnableTracing(self):
        return self._EnableTracing

    @EnableTracing.setter
    def EnableTracing(self, EnableTracing):
        self._EnableTracing = EnableTracing

    @property
    def EnableTracingReport(self):
        return self._EnableTracingReport

    @EnableTracingReport.setter
    def EnableTracingReport(self, EnableTracingReport):
        self._EnableTracingReport = EnableTracingReport

    @property
    def RepoType(self):
        return self._RepoType

    @RepoType.setter
    def RepoType(self, RepoType):
        self._RepoType = RepoType

    @property
    def BatchDeployStatus(self):
        return self._BatchDeployStatus

    @BatchDeployStatus.setter
    def BatchDeployStatus(self, BatchDeployStatus):
        self._BatchDeployStatus = BatchDeployStatus

    @property
    def ApmInstanceId(self):
        return self._ApmInstanceId

    @ApmInstanceId.setter
    def ApmInstanceId(self, ApmInstanceId):
        self._ApmInstanceId = ApmInstanceId

    @property
    def WorkloadInfo(self):
        return self._WorkloadInfo

    @WorkloadInfo.setter
    def WorkloadInfo(self, WorkloadInfo):
        self._WorkloadInfo = WorkloadInfo

    @property
    def SpeedUp(self):
        return self._SpeedUp

    @SpeedUp.setter
    def SpeedUp(self, SpeedUp):
        self._SpeedUp = SpeedUp

    @property
    def StartupProbe(self):
        return self._StartupProbe

    @StartupProbe.setter
    def StartupProbe(self, StartupProbe):
        self._StartupProbe = StartupProbe

    @property
    def OsFlavour(self):
        return self._OsFlavour

    @OsFlavour.setter
    def OsFlavour(self, OsFlavour):
        self._OsFlavour = OsFlavour

    @property
    def RepoServer(self):
        return self._RepoServer

    @RepoServer.setter
    def RepoServer(self, RepoServer):
        self._RepoServer = RepoServer

    @property
    def UnderDeploying(self):
        return self._UnderDeploying

    @UnderDeploying.setter
    def UnderDeploying(self, UnderDeploying):
        self._UnderDeploying = UnderDeploying

    @property
    def EnablePrometheusConf(self):
        return self._EnablePrometheusConf

    @EnablePrometheusConf.setter
    def EnablePrometheusConf(self, EnablePrometheusConf):
        self._EnablePrometheusConf = EnablePrometheusConf

    @property
    def StoppedManually(self):
        return self._StoppedManually

    @StoppedManually.setter
    def StoppedManually(self, StoppedManually):
        self._StoppedManually = StoppedManually

    @property
    def TcrInstanceId(self):
        return self._TcrInstanceId

    @TcrInstanceId.setter
    def TcrInstanceId(self, TcrInstanceId):
        self._TcrInstanceId = TcrInstanceId

    @property
    def EnableMetrics(self):
        return self._EnableMetrics

    @EnableMetrics.setter
    def EnableMetrics(self, EnableMetrics):
        self._EnableMetrics = EnableMetrics

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def SubAccountUin(self):
        return self._SubAccountUin

    @SubAccountUin.setter
    def SubAccountUin(self, SubAccountUin):
        self._SubAccountUin = SubAccountUin

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def EnableRegistry(self):
        return self._EnableRegistry

    @EnableRegistry.setter
    def EnableRegistry(self, EnableRegistry):
        self._EnableRegistry = EnableRegistry

    @property
    def AutoscalerList(self):
        return self._AutoscalerList

    @AutoscalerList.setter
    def AutoscalerList(self, AutoscalerList):
        self._AutoscalerList = AutoscalerList

    @property
    def Modifier(self):
        return self._Modifier

    @Modifier.setter
    def Modifier(self, Modifier):
        self._Modifier = Modifier

    @property
    def Creator(self):
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def DeployStrategyConf(self):
        return self._DeployStrategyConf

    @DeployStrategyConf.setter
    def DeployStrategyConf(self, DeployStrategyConf):
        self._DeployStrategyConf = DeployStrategyConf

    @property
    def PodList(self):
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        self._PodList = PodList

    @property
    def ConfEdited(self):
        return self._ConfEdited

    @ConfEdited.setter
    def ConfEdited(self, ConfEdited):
        self._ConfEdited = ConfEdited

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PreStopEncoded(self):
        return self._PreStopEncoded

    @PreStopEncoded.setter
    def PreStopEncoded(self, PreStopEncoded):
        self._PreStopEncoded = PreStopEncoded

    @property
    def PostStartEncoded(self):
        return self._PostStartEncoded

    @PostStartEncoded.setter
    def PostStartEncoded(self, PostStartEncoded):
        self._PostStartEncoded = PostStartEncoded


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._ApplicationId = params.get("ApplicationId")
        self._DeployMode = params.get("DeployMode")
        self._JdkVersion = params.get("JdkVersion")
        self._Description = params.get("Description")
        self._DeployVersion = params.get("DeployVersion")
        self._PublishMode = params.get("PublishMode")
        self._JvmOpts = params.get("JvmOpts")
        self._InitPodNum = params.get("InitPodNum")
        self._CpuSpec = params.get("CpuSpec")
        self._MemorySpec = params.get("MemorySpec")
        self._ImgRepo = params.get("ImgRepo")
        self._ImgName = params.get("ImgName")
        self._ImgVersion = params.get("ImgVersion")
        if params.get("EsInfo") is not None:
            self._EsInfo = EsInfo()
            self._EsInfo._deserialize(params.get("EsInfo"))
        if params.get("EnvConf") is not None:
            self._EnvConf = []
            for item in params.get("EnvConf"):
                obj = Pair()
                obj._deserialize(item)
                self._EnvConf.append(obj)
        if params.get("StorageConfs") is not None:
            self._StorageConfs = []
            for item in params.get("StorageConfs"):
                obj = StorageConf()
                obj._deserialize(item)
                self._StorageConfs.append(obj)
        self._Status = params.get("Status")
        self._Vpc = params.get("Vpc")
        self._SubnetId = params.get("SubnetId")
        self._CreateDate = params.get("CreateDate")
        self._ModifyDate = params.get("ModifyDate")
        if params.get("StorageMountConfs") is not None:
            self._StorageMountConfs = []
            for item in params.get("StorageMountConfs"):
                obj = StorageMountConf()
                obj._deserialize(item)
                self._StorageMountConfs.append(obj)
        self._VersionName = params.get("VersionName")
        if params.get("LogOutputConf") is not None:
            self._LogOutputConf = LogOutputConf()
            self._LogOutputConf._deserialize(params.get("LogOutputConf"))
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationDescription = params.get("ApplicationDescription")
        self._EnvironmentName = params.get("EnvironmentName")
        self._EnvironmentId = params.get("EnvironmentId")
        self._PublicDomain = params.get("PublicDomain")
        self._EnablePublicAccess = params.get("EnablePublicAccess")
        self._CurrentInstances = params.get("CurrentInstances")
        self._ExpectedInstances = params.get("ExpectedInstances")
        self._CodingLanguage = params.get("CodingLanguage")
        self._PkgName = params.get("PkgName")
        self._EsEnable = params.get("EsEnable")
        self._EsStrategy = params.get("EsStrategy")
        self._ImageTag = params.get("ImageTag")
        self._LogEnable = params.get("LogEnable")
        self._MinAliveInstances = params.get("MinAliveInstances")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ImageCommand = params.get("ImageCommand")
        self._ImageArgs = params.get("ImageArgs")
        self._UseRegistryDefaultConfig = params.get("UseRegistryDefaultConfig")
        if params.get("Service") is not None:
            self._Service = EksService()
            self._Service._deserialize(params.get("Service"))
        if params.get("SettingConfs") is not None:
            self._SettingConfs = []
            for item in params.get("SettingConfs"):
                obj = MountedSettingConf()
                obj._deserialize(item)
                self._SettingConfs.append(obj)
        self._LogConfs = params.get("LogConfs")
        self._PostStart = params.get("PostStart")
        self._PreStop = params.get("PreStop")
        if params.get("Liveness") is not None:
            self._Liveness = HealthCheckConfig()
            self._Liveness._deserialize(params.get("Liveness"))
        if params.get("Readiness") is not None:
            self._Readiness = HealthCheckConfig()
            self._Readiness._deserialize(params.get("Readiness"))
        if params.get("HorizontalAutoscaler") is not None:
            self._HorizontalAutoscaler = []
            for item in params.get("HorizontalAutoscaler"):
                obj = HorizontalAutoscaler()
                obj._deserialize(item)
                self._HorizontalAutoscaler.append(obj)
        if params.get("CronHorizontalAutoscaler") is not None:
            self._CronHorizontalAutoscaler = []
            for item in params.get("CronHorizontalAutoscaler"):
                obj = CronHorizontalAutoscaler()
                obj._deserialize(item)
                self._CronHorizontalAutoscaler.append(obj)
        self._Zones = params.get("Zones")
        self._LastDeployDate = params.get("LastDeployDate")
        self._LastDeploySuccessDate = params.get("LastDeploySuccessDate")
        if params.get("NodeInfos") is not None:
            self._NodeInfos = []
            for item in params.get("NodeInfos"):
                obj = NodeInfo()
                obj._deserialize(item)
                self._NodeInfos.append(obj)
        self._ImageType = params.get("ImageType")
        self._EnableTracing = params.get("EnableTracing")
        self._EnableTracingReport = params.get("EnableTracingReport")
        self._RepoType = params.get("RepoType")
        self._BatchDeployStatus = params.get("BatchDeployStatus")
        self._ApmInstanceId = params.get("ApmInstanceId")
        if params.get("WorkloadInfo") is not None:
            self._WorkloadInfo = WorkloadInfo()
            self._WorkloadInfo._deserialize(params.get("WorkloadInfo"))
        self._SpeedUp = params.get("SpeedUp")
        if params.get("StartupProbe") is not None:
            self._StartupProbe = HealthCheckConfig()
            self._StartupProbe._deserialize(params.get("StartupProbe"))
        self._OsFlavour = params.get("OsFlavour")
        self._RepoServer = params.get("RepoServer")
        self._UnderDeploying = params.get("UnderDeploying")
        if params.get("EnablePrometheusConf") is not None:
            self._EnablePrometheusConf = EnablePrometheusConf()
            self._EnablePrometheusConf._deserialize(params.get("EnablePrometheusConf"))
        self._StoppedManually = params.get("StoppedManually")
        self._TcrInstanceId = params.get("TcrInstanceId")
        self._EnableMetrics = params.get("EnableMetrics")
        self._AppId = params.get("AppId")
        self._SubAccountUin = params.get("SubAccountUin")
        self._Uin = params.get("Uin")
        self._Region = params.get("Region")
        self._GroupId = params.get("GroupId")
        self._EnableRegistry = params.get("EnableRegistry")
        if params.get("AutoscalerList") is not None:
            self._AutoscalerList = []
            for item in params.get("AutoscalerList"):
                obj = Autoscaler()
                obj._deserialize(item)
                self._AutoscalerList.append(obj)
        self._Modifier = params.get("Modifier")
        self._Creator = params.get("Creator")
        if params.get("DeployStrategyConf") is not None:
            self._DeployStrategyConf = DeployStrategyConf()
            self._DeployStrategyConf._deserialize(params.get("DeployStrategyConf"))
        if params.get("PodList") is not None:
            self._PodList = DescribeRunPodPage()
            self._PodList._deserialize(params.get("PodList"))
        self._ConfEdited = params.get("ConfEdited")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PreStopEncoded = params.get("PreStopEncoded")
        self._PostStartEncoded = params.get("PostStartEncoded")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UseDefaultRepoParameters(AbstractModel):
    """Repository parameters

    """

    def __init__(self):
        r"""
        :param _EnterpriseInstanceName: TCR Enterprise instance name
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnterpriseInstanceName: str
        :param _EnterpriseInstanceChargeType: TCR Enterprise billing mode. `0`: Pay-as-you-go 
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnterpriseInstanceChargeType: int
        :param _EnterpriseInstanceType: Edition of the TCR Enterprise. Values: `basic`, `standard`, `premium` (Advanced edition)
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnterpriseInstanceType: str
        """
        self._EnterpriseInstanceName = None
        self._EnterpriseInstanceChargeType = None
        self._EnterpriseInstanceType = None

    @property
    def EnterpriseInstanceName(self):
        return self._EnterpriseInstanceName

    @EnterpriseInstanceName.setter
    def EnterpriseInstanceName(self, EnterpriseInstanceName):
        self._EnterpriseInstanceName = EnterpriseInstanceName

    @property
    def EnterpriseInstanceChargeType(self):
        return self._EnterpriseInstanceChargeType

    @EnterpriseInstanceChargeType.setter
    def EnterpriseInstanceChargeType(self, EnterpriseInstanceChargeType):
        self._EnterpriseInstanceChargeType = EnterpriseInstanceChargeType

    @property
    def EnterpriseInstanceType(self):
        return self._EnterpriseInstanceType

    @EnterpriseInstanceType.setter
    def EnterpriseInstanceType(self, EnterpriseInstanceType):
        self._EnterpriseInstanceType = EnterpriseInstanceType


    def _deserialize(self, params):
        self._EnterpriseInstanceName = params.get("EnterpriseInstanceName")
        self._EnterpriseInstanceChargeType = params.get("EnterpriseInstanceChargeType")
        self._EnterpriseInstanceType = params.get("EnterpriseInstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadInfo(AbstractModel):
    """Workload details

    """

    def __init__(self):
        r"""
        :param _ClusterId: The resource ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _ApplicationName: Application name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ApplicationName: str
        :param _VersionName: Version name
Note: This field may return `null`, indicating that no valid value was found.
        :type VersionName: str
        :param _ReadyReplicas: Number of ready replicas
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ReadyReplicas: int
        :param _Replicas: Number of replicas
Note: This field may return `null`, indicating that no valid value was found.
        :type Replicas: int
        :param _UpdatedReplicas: Number of updated replicas
Note: This field may return `null`, indicating that no valid value was found.
        :type UpdatedReplicas: int
        :param _UpdatedReadyReplicas: Number of replicas ready for update
Note: This field may return `null`, indicating that no valid value was found.
        :type UpdatedReadyReplicas: int
        :param _UpdateRevision: ## Version Updates
Note: This field may return `null`, indicating that no valid value was found.
        :type UpdateRevision: str
        :param _CurrentRevision: Current Version
Note: This field may return `null`, indicating that no valid value was found.
        :type CurrentRevision: str
        """
        self._ClusterId = None
        self._ApplicationName = None
        self._VersionName = None
        self._ReadyReplicas = None
        self._Replicas = None
        self._UpdatedReplicas = None
        self._UpdatedReadyReplicas = None
        self._UpdateRevision = None
        self._CurrentRevision = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ReadyReplicas(self):
        return self._ReadyReplicas

    @ReadyReplicas.setter
    def ReadyReplicas(self, ReadyReplicas):
        self._ReadyReplicas = ReadyReplicas

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def UpdatedReplicas(self):
        return self._UpdatedReplicas

    @UpdatedReplicas.setter
    def UpdatedReplicas(self, UpdatedReplicas):
        self._UpdatedReplicas = UpdatedReplicas

    @property
    def UpdatedReadyReplicas(self):
        return self._UpdatedReadyReplicas

    @UpdatedReadyReplicas.setter
    def UpdatedReadyReplicas(self, UpdatedReadyReplicas):
        self._UpdatedReadyReplicas = UpdatedReadyReplicas

    @property
    def UpdateRevision(self):
        return self._UpdateRevision

    @UpdateRevision.setter
    def UpdateRevision(self, UpdateRevision):
        self._UpdateRevision = UpdateRevision

    @property
    def CurrentRevision(self):
        return self._CurrentRevision

    @CurrentRevision.setter
    def CurrentRevision(self, CurrentRevision):
        self._CurrentRevision = CurrentRevision


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ApplicationName = params.get("ApplicationName")
        self._VersionName = params.get("VersionName")
        self._ReadyReplicas = params.get("ReadyReplicas")
        self._Replicas = params.get("Replicas")
        self._UpdatedReplicas = params.get("UpdatedReplicas")
        self._UpdatedReadyReplicas = params.get("UpdatedReadyReplicas")
        self._UpdateRevision = params.get("UpdateRevision")
        self._CurrentRevision = params.get("CurrentRevision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        