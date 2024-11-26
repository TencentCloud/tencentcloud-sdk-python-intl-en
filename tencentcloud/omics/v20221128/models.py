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


class ApplicationVersion(AbstractModel):
    """Application version

    """

    def __init__(self):
        r"""
        :param _Type: Version type
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _ApplicationVersionId: Version ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationVersionId: str
        :param _Name: Release name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Description: Release description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Entrypoint: Entry file
Note: This field may return null, indicating that no valid values can be obtained.
        :type Entrypoint: str
        :param _CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _CreatorName: Creator name
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatorName: str
        :param _CreatorId: Creator ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatorId: str
        :param _GitInfo: Git information
Note: This field may return null, indicating that no valid values can be obtained.
        :type GitInfo: str
        """
        self._Type = None
        self._ApplicationVersionId = None
        self._Name = None
        self._Description = None
        self._Entrypoint = None
        self._CreateTime = None
        self._CreatorName = None
        self._CreatorId = None
        self._GitInfo = None

    @property
    def Type(self):
        """Version type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ApplicationVersionId(self):
        """Version ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def Name(self):
        """Release name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Release description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Entrypoint(self):
        """Entry file
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Entrypoint

    @Entrypoint.setter
    def Entrypoint(self, Entrypoint):
        self._Entrypoint = Entrypoint

    @property
    def CreateTime(self):
        """Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreatorName(self):
        """Creator name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatorName

    @CreatorName.setter
    def CreatorName(self, CreatorName):
        self._CreatorName = CreatorName

    @property
    def CreatorId(self):
        """Creator ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def GitInfo(self):
        warnings.warn("parameter `GitInfo` is deprecated", DeprecationWarning) 

        """Git information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GitInfo

    @GitInfo.setter
    def GitInfo(self, GitInfo):
        warnings.warn("parameter `GitInfo` is deprecated", DeprecationWarning) 

        self._GitInfo = GitInfo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Entrypoint = params.get("Entrypoint")
        self._CreateTime = params.get("CreateTime")
        self._CreatorName = params.get("CreatorName")
        self._CreatorId = params.get("CreatorId")
        self._GitInfo = params.get("GitInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CVMOption(AbstractModel):
    """CVM configuration

    """

    def __init__(self):
        r"""
        :param _Zone: CVM availability zone
        :type Zone: str
        :param _InstanceType: CVM instance specifications
        :type InstanceType: str
        """
        self._Zone = None
        self._InstanceType = None

    @property
    def Zone(self):
        """CVM availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        """CVM instance specifications
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheInfo(AbstractModel):
    """Cache information

    """

    def __init__(self):
        r"""
        :param _CacheClearDelay: Cache cleanup time (hours)
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheClearDelay: int
        :param _CacheClearTime: Cache cleanup schedule time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheClearTime: str
        :param _CacheCleared: Whether the cache has been cleaned up
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheCleared: bool
        """
        self._CacheClearDelay = None
        self._CacheClearTime = None
        self._CacheCleared = None

    @property
    def CacheClearDelay(self):
        """Cache cleanup time (hours)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CacheClearDelay

    @CacheClearDelay.setter
    def CacheClearDelay(self, CacheClearDelay):
        self._CacheClearDelay = CacheClearDelay

    @property
    def CacheClearTime(self):
        """Cache cleanup schedule time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CacheClearTime

    @CacheClearTime.setter
    def CacheClearTime(self, CacheClearTime):
        self._CacheClearTime = CacheClearTime

    @property
    def CacheCleared(self):
        """Whether the cache has been cleaned up
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._CacheCleared

    @CacheCleared.setter
    def CacheCleared(self, CacheCleared):
        self._CacheCleared = CacheCleared


    def _deserialize(self, params):
        self._CacheClearDelay = params.get("CacheClearDelay")
        self._CacheClearTime = params.get("CacheClearTime")
        self._CacheCleared = params.get("CacheCleared")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterOption(AbstractModel):
    """Computing cluster configuration

    """

    def __init__(self):
        r"""
        :param _Zone: Computing cluster availability zone
        :type Zone: str
        :param _Type: Computing cluster type. Valid values:
- KUBERNETES
        :type Type: str
        :param _ServiceCidr: Computing cluster Service CIDR. It must not overlap with the VPC IP range.
        :type ServiceCidr: str
        :param _ResourceQuota: Resource quota
        :type ResourceQuota: :class:`tencentcloud.omics.v20221128.models.ResourceQuota`
        :param _LimitRange: Limit scope
        :type LimitRange: :class:`tencentcloud.omics.v20221128.models.LimitRange`
        """
        self._Zone = None
        self._Type = None
        self._ServiceCidr = None
        self._ResourceQuota = None
        self._LimitRange = None

    @property
    def Zone(self):
        """Computing cluster availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Type(self):
        """Computing cluster type. Valid values:
- KUBERNETES
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ServiceCidr(self):
        """Computing cluster Service CIDR. It must not overlap with the VPC IP range.
        :rtype: str
        """
        return self._ServiceCidr

    @ServiceCidr.setter
    def ServiceCidr(self, ServiceCidr):
        self._ServiceCidr = ServiceCidr

    @property
    def ResourceQuota(self):
        """Resource quota
        :rtype: :class:`tencentcloud.omics.v20221128.models.ResourceQuota`
        """
        return self._ResourceQuota

    @ResourceQuota.setter
    def ResourceQuota(self, ResourceQuota):
        self._ResourceQuota = ResourceQuota

    @property
    def LimitRange(self):
        """Limit scope
        :rtype: :class:`tencentcloud.omics.v20221128.models.LimitRange`
        """
        return self._LimitRange

    @LimitRange.setter
    def LimitRange(self, LimitRange):
        self._LimitRange = LimitRange


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._Type = params.get("Type")
        self._ServiceCidr = params.get("ServiceCidr")
        if params.get("ResourceQuota") is not None:
            self._ResourceQuota = ResourceQuota()
            self._ResourceQuota._deserialize(params.get("ResourceQuota"))
        if params.get("LimitRange") is not None:
            self._LimitRange = LimitRange()
            self._LimitRange._deserialize(params.get("LimitRange"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Environment name
        :type Name: str
        :param _Config: Environment configuration information
        :type Config: :class:`tencentcloud.omics.v20221128.models.EnvironmentConfig`
        :param _Description: Environment description
        :type Description: str
        :param _IsDefault: Whether it is the default environment.
        :type IsDefault: bool
        """
        self._Name = None
        self._Config = None
        self._Description = None
        self._IsDefault = None

    @property
    def Name(self):
        """Environment name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Config(self):
        """Environment configuration information
        :rtype: :class:`tencentcloud.omics.v20221128.models.EnvironmentConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Description(self):
        """Environment description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsDefault(self):
        """Whether it is the default environment.
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Config") is not None:
            self._Config = EnvironmentConfig()
            self._Config._deserialize(params.get("Config"))
        self._Description = params.get("Description")
        self._IsDefault = params.get("IsDefault")
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
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _WorkflowUuid: Workflow UUID
        :type WorkflowUuid: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._WorkflowUuid = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        """Environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def WorkflowUuid(self):
        """Workflow UUID
        :rtype: str
        """
        return self._WorkflowUuid

    @WorkflowUuid.setter
    def WorkflowUuid(self, WorkflowUuid):
        self._WorkflowUuid = WorkflowUuid

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
        self._EnvironmentId = params.get("EnvironmentId")
        self._WorkflowUuid = params.get("WorkflowUuid")
        self._RequestId = params.get("RequestId")


class CreateVolumeRequest(AbstractModel):
    """CreateVolume request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Name
        :type Name: str
        :param _Type: Volume type. Valid values:
* SHARED: Multi-point mount shared storage
        :type Type: str
        :param _Spec: Volume specifications. Valid values:

- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
        :type Spec: str
        :param _Description: Description
        :type Description: str
        :param _Capacity: Volume size (GB), which is required to be specified for the Turbo series.
        :type Capacity: int
        """
        self._EnvironmentId = None
        self._Name = None
        self._Type = None
        self._Spec = None
        self._Description = None
        self._Capacity = None

    @property
    def EnvironmentId(self):
        """Environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Volume type. Valid values:
* SHARED: Multi-point mount shared storage
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Spec(self):
        """Volume specifications. Valid values:

- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

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
    def Capacity(self):
        """Volume size (GB), which is required to be specified for the Turbo series.
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Spec = params.get("Spec")
        self._Description = params.get("Description")
        self._Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVolumeResponse(AbstractModel):
    """CreateVolume response structure.

    """

    def __init__(self):
        r"""
        :param _VolumeId: Volume ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VolumeId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._VolumeId = None
        self._RequestId = None

    @property
    def VolumeId(self):
        """Volume ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

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
        self._VolumeId = params.get("VolumeId")
        self._RequestId = params.get("RequestId")


class DatabaseOption(AbstractModel):
    """Database configuration

    """

    def __init__(self):
        r"""
        :param _Zone: Database availability zone
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        """Database availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRequest(AbstractModel):
    """DeleteEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        """
        self._EnvironmentId = None

    @property
    def EnvironmentId(self):
        """Environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentResponse(AbstractModel):
    """DeleteEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _WorkflowUuid: Workflow UUID
        :type WorkflowUuid: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WorkflowUuid = None
        self._RequestId = None

    @property
    def WorkflowUuid(self):
        """Workflow UUID
        :rtype: str
        """
        return self._WorkflowUuid

    @WorkflowUuid.setter
    def WorkflowUuid(self, WorkflowUuid):
        self._WorkflowUuid = WorkflowUuid

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
        self._WorkflowUuid = params.get("WorkflowUuid")
        self._RequestId = params.get("RequestId")


class DeleteVolumeDataRequest(AbstractModel):
    """DeleteVolumeData request structure.

    """

    def __init__(self):
        r"""
        :param _VolumeId: Volume ID
        :type VolumeId: str
        :param _Path: Path to be deleted
        :type Path: str
        """
        self._VolumeId = None
        self._Path = None

    @property
    def VolumeId(self):
        """Volume ID
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def Path(self):
        """Path to be deleted
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVolumeDataResponse(AbstractModel):
    """DeleteVolumeData response structure.

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


class DeleteVolumeRequest(AbstractModel):
    """DeleteVolume request structure.

    """

    def __init__(self):
        r"""
        :param _VolumeId: Volume ID
        :type VolumeId: str
        """
        self._VolumeId = None

    @property
    def VolumeId(self):
        """Volume ID
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVolumeResponse(AbstractModel):
    """DeleteVolume response structure.

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


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset, which defaults to 0.
        :type Offset: int
        :param _Limit: Quantity of returns. It is 20 by default, and the maximum value is 100.
        :type Limit: int
        :param _Filters: Filter, which supports filtering fields:
- EnvironmentId: Environment ID
- Name: Name
- Status: Environmental status
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """Offset, which defaults to 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Quantity of returns. It is 20 by default, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Filter, which supports filtering fields:
- EnvironmentId: Environment ID
- Name: Name
- Status: Environmental status
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
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
        :param _TotalCount: Number of qualified items
        :type TotalCount: int
        :param _Environments: List of Environment details
        :type Environments: list of Environment
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Environments = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of qualified items
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Environments(self):
        """List of Environment details
        :rtype: list of Environment
        """
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

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
        if params.get("Environments") is not None:
            self._Environments = []
            for item in params.get("Environments"):
                obj = Environment()
                obj._deserialize(item)
                self._Environments.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunGroupsRequest(AbstractModel):
    """DescribeRunGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        :param _Limit: Quantity of returns. It is 10 by default, and the maximum value is 100.
        :type Limit: int
        :param _Offset: Offset, which defaults to 0.
        :type Offset: int
        :param _Filters: Filter, which supports filtering fields:
- Name: Run group name
- RunGroupId: Run group ID
- Status: Run group status
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Limit(self):
        """Quantity of returns. It is 10 by default, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset, which defaults to 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter, which supports filtering fields:
- Name: Run group name
- RunGroupId: Run group ID
- Status: Run group status
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunGroupsResponse(AbstractModel):
    """DescribeRunGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of qualified items
        :type TotalCount: int
        :param _RunGroups: Run group list
        :type RunGroups: list of RunGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RunGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of qualified items
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RunGroups(self):
        """Run group list
        :rtype: list of RunGroup
        """
        return self._RunGroups

    @RunGroups.setter
    def RunGroups(self, RunGroups):
        self._RunGroups = RunGroups

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
        if params.get("RunGroups") is not None:
            self._RunGroups = []
            for item in params.get("RunGroups"):
                obj = RunGroup()
                obj._deserialize(item)
                self._RunGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRunsRequest(AbstractModel):
    """DescribeRuns request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        :param _Limit: Quantity of returns. It is 10 by default, and the maximum value is 100.
        :type Limit: int
        :param _Offset: Offset, which defaults to 0.
        :type Offset: int
        :param _Filters: Filter, which supports filtering fields:
- RunGroupId: run group ID
- Status: run status
- RunUuid: run UUID
- UserDefinedId: user-defined ID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Limit(self):
        """Quantity of returns. It is 10 by default, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset, which defaults to 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter, which supports filtering fields:
- RunGroupId: run group ID
- Status: run status
- RunUuid: run UUID
- UserDefinedId: user-defined ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRunsResponse(AbstractModel):
    """DescribeRuns response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of qualified items
        :type TotalCount: int
        :param _Runs: Run list
        :type Runs: list of Run
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Runs = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Number of qualified items
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Runs(self):
        """Run list
        :rtype: list of Run
        """
        return self._Runs

    @Runs.setter
    def Runs(self, Runs):
        self._Runs = Runs

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
        if params.get("Runs") is not None:
            self._Runs = []
            for item in params.get("Runs"):
                obj = Run()
                obj._deserialize(item)
                self._Runs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _Limit: Quantity of returns. It is 10 by default, and the maximum value is 100.
        :type Limit: int
        :param _Offset: Offset, which defaults to 0
        :type Offset: int
        :param _Filters: Filter, which supports filtering fields:
- Name: Table name
- TableId: Table ID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Limit(self):
        """Quantity of returns. It is 10 by default, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset, which defaults to 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter, which supports filtering fields:
- Name: Table name
- TableId: Table ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesResponse(AbstractModel):
    """DescribeTables response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Tables: Table list
        :type Tables: list of Table
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Tables = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Tables(self):
        """Table list
        :rtype: list of Table
        """
        return self._Tables

    @Tables.setter
    def Tables(self, Tables):
        self._Tables = Tables

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
        if params.get("Tables") is not None:
            self._Tables = []
            for item in params.get("Tables"):
                obj = Table()
                obj._deserialize(item)
                self._Tables.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTablesRowsRequest(AbstractModel):
    """DescribeTablesRows request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _TableId: Table ID
        :type TableId: str
        :param _Limit: Quantity of returns. It is 10 by default, and the maximum value is 100.
        :type Limit: int
        :param _Offset: Offset, which defaults to 0.
        :type Offset: int
        :param _Filters: Filter, which supports filtering fields:
- Tr: Table data, which supports fuzzy query.
- TableRowUuid: table row UUID
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._TableId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TableId(self):
        """Table ID
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def Limit(self):
        """Quantity of returns. It is 10 by default, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset, which defaults to 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter, which supports filtering fields:
- Tr: Table data, which supports fuzzy query.
- TableRowUuid: table row UUID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._TableId = params.get("TableId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTablesRowsResponse(AbstractModel):
    """DescribeTablesRows response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of results
        :type TotalCount: int
        :param _Rows: Table row list
        :type Rows: list of TableRow
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rows(self):
        """Table row list
        :rtype: list of TableRow
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

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
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TableRow()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVolumesRequest(AbstractModel):
    """DescribeVolumes request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Limit: Quantity of returns. It is 20 by default, and the maximum value is 100.
        :type Limit: int
        :param _Offset: Offset, defaults to 0
        :type Offset: int
        :param _Filters: Filter, supports filtering fields:
- Name: Name
- IsDefault: Whether it is the default.
        :type Filters: list of Filter
        """
        self._EnvironmentId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def EnvironmentId(self):
        """Environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Limit(self):
        """Quantity of returns. It is 20 by default, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Offset, defaults to 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter, supports filtering fields:
- Name: Name
- IsDefault: Whether it is the default.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVolumesResponse(AbstractModel):
    """DescribeVolumes response structure.

    """

    def __init__(self):
        r"""
        :param _Volumes: Volume
Note: This field may return null, indicating that no valid values can be obtained.
        :type Volumes: list of Volume
        :param _TotalCount: Number of qualified items
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Volumes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Volumes(self):
        """Volume
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Volume
        """
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        self._Volumes = Volumes

    @property
    def TotalCount(self):
        """Number of qualified items
Note: This field may return null, indicating that no valid values can be obtained.
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
        if params.get("Volumes") is not None:
            self._Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self._Volumes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """Tencent Healthcare Omics Platform environment details

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _Name: Environment name
        :type Name: str
        :param _Description: Environment description information
        :type Description: str
        :param _Region: Environment region
        :type Region: str
        :param _Type: Environment type. Valid values:
- KUBERNETES: Kubernetes container cluster
- HPC:HPC HCC 
        :type Type: str
        :param _Status: Environment status. Valid values:
- INITIALIZING: Creating
- INITIALIZATION_ERROR: Creation failed
- RUNNING: Running
- ERROR: Exceptional
- DELETING: Deleting
- DELETE_ERROR: Deletion failed.
        :type Status: str
        :param _Available: Whether the environment is available. The environment needs to be available before computing runs can be delivered.
        :type Available: bool
        :param _IsDefault: Whether the environment is the default environment.
        :type IsDefault: bool
        :param _IsManaged: Whether the environment is a managed environment.
        :type IsManaged: bool
        :param _Message: Environment information
        :type Message: str
        :param _ResourceIds: Cloud resource ID
        :type ResourceIds: :class:`tencentcloud.omics.v20221128.models.ResourceIds`
        :param _LastWorkflowUuid: The UUID of the previous workflow
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastWorkflowUuid: str
        :param _CreationTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreationTime: str
        """
        self._EnvironmentId = None
        self._Name = None
        self._Description = None
        self._Region = None
        self._Type = None
        self._Status = None
        self._Available = None
        self._IsDefault = None
        self._IsManaged = None
        self._Message = None
        self._ResourceIds = None
        self._LastWorkflowUuid = None
        self._CreationTime = None

    @property
    def EnvironmentId(self):
        """Environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Name(self):
        """Environment name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Environment description information
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Region(self):
        """Environment region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Type(self):
        """Environment type. Valid values:
- KUBERNETES: Kubernetes container cluster
- HPC:HPC HCC 
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """Environment status. Valid values:
- INITIALIZING: Creating
- INITIALIZATION_ERROR: Creation failed
- RUNNING: Running
- ERROR: Exceptional
- DELETING: Deleting
- DELETE_ERROR: Deletion failed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Available(self):
        """Whether the environment is available. The environment needs to be available before computing runs can be delivered.
        :rtype: bool
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def IsDefault(self):
        """Whether the environment is the default environment.
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def IsManaged(self):
        """Whether the environment is a managed environment.
        :rtype: bool
        """
        return self._IsManaged

    @IsManaged.setter
    def IsManaged(self, IsManaged):
        self._IsManaged = IsManaged

    @property
    def Message(self):
        """Environment information
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ResourceIds(self):
        """Cloud resource ID
        :rtype: :class:`tencentcloud.omics.v20221128.models.ResourceIds`
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def LastWorkflowUuid(self):
        """The UUID of the previous workflow
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastWorkflowUuid

    @LastWorkflowUuid.setter
    def LastWorkflowUuid(self, LastWorkflowUuid):
        self._LastWorkflowUuid = LastWorkflowUuid

    @property
    def CreationTime(self):
        """Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreationTime

    @CreationTime.setter
    def CreationTime(self, CreationTime):
        self._CreationTime = CreationTime


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Region = params.get("Region")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._Available = params.get("Available")
        self._IsDefault = params.get("IsDefault")
        self._IsManaged = params.get("IsManaged")
        self._Message = params.get("Message")
        if params.get("ResourceIds") is not None:
            self._ResourceIds = ResourceIds()
            self._ResourceIds._deserialize(params.get("ResourceIds"))
        self._LastWorkflowUuid = params.get("LastWorkflowUuid")
        self._CreationTime = params.get("CreationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentConfig(AbstractModel):
    """Environment configuration

    """

    def __init__(self):
        r"""
        :param _VPCOption: VPC configuration
        :type VPCOption: :class:`tencentcloud.omics.v20221128.models.VPCOption`
        :param _ClusterOption: Computing cluster configuration
        :type ClusterOption: :class:`tencentcloud.omics.v20221128.models.ClusterOption`
        :param _DatabaseOption: Database configuration
        :type DatabaseOption: :class:`tencentcloud.omics.v20221128.models.DatabaseOption`
        :param _StorageOption: Storage configuration
        :type StorageOption: :class:`tencentcloud.omics.v20221128.models.StorageOption`
        :param _CVMOption: CVM configuration
        :type CVMOption: :class:`tencentcloud.omics.v20221128.models.CVMOption`
        :param _SecurityGroupOption: Security group configuration
        :type SecurityGroupOption: :class:`tencentcloud.omics.v20221128.models.SecurityGroupOption`
        """
        self._VPCOption = None
        self._ClusterOption = None
        self._DatabaseOption = None
        self._StorageOption = None
        self._CVMOption = None
        self._SecurityGroupOption = None

    @property
    def VPCOption(self):
        """VPC configuration
        :rtype: :class:`tencentcloud.omics.v20221128.models.VPCOption`
        """
        return self._VPCOption

    @VPCOption.setter
    def VPCOption(self, VPCOption):
        self._VPCOption = VPCOption

    @property
    def ClusterOption(self):
        """Computing cluster configuration
        :rtype: :class:`tencentcloud.omics.v20221128.models.ClusterOption`
        """
        return self._ClusterOption

    @ClusterOption.setter
    def ClusterOption(self, ClusterOption):
        self._ClusterOption = ClusterOption

    @property
    def DatabaseOption(self):
        """Database configuration
        :rtype: :class:`tencentcloud.omics.v20221128.models.DatabaseOption`
        """
        return self._DatabaseOption

    @DatabaseOption.setter
    def DatabaseOption(self, DatabaseOption):
        self._DatabaseOption = DatabaseOption

    @property
    def StorageOption(self):
        """Storage configuration
        :rtype: :class:`tencentcloud.omics.v20221128.models.StorageOption`
        """
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def CVMOption(self):
        """CVM configuration
        :rtype: :class:`tencentcloud.omics.v20221128.models.CVMOption`
        """
        return self._CVMOption

    @CVMOption.setter
    def CVMOption(self, CVMOption):
        self._CVMOption = CVMOption

    @property
    def SecurityGroupOption(self):
        """Security group configuration
        :rtype: :class:`tencentcloud.omics.v20221128.models.SecurityGroupOption`
        """
        return self._SecurityGroupOption

    @SecurityGroupOption.setter
    def SecurityGroupOption(self, SecurityGroupOption):
        self._SecurityGroupOption = SecurityGroupOption


    def _deserialize(self, params):
        if params.get("VPCOption") is not None:
            self._VPCOption = VPCOption()
            self._VPCOption._deserialize(params.get("VPCOption"))
        if params.get("ClusterOption") is not None:
            self._ClusterOption = ClusterOption()
            self._ClusterOption._deserialize(params.get("ClusterOption"))
        if params.get("DatabaseOption") is not None:
            self._DatabaseOption = DatabaseOption()
            self._DatabaseOption._deserialize(params.get("DatabaseOption"))
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOption()
            self._StorageOption._deserialize(params.get("StorageOption"))
        if params.get("CVMOption") is not None:
            self._CVMOption = CVMOption()
            self._CVMOption._deserialize(params.get("CVMOption"))
        if params.get("SecurityGroupOption") is not None:
            self._SecurityGroupOption = SecurityGroupOption()
            self._SecurityGroupOption._deserialize(params.get("SecurityGroupOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecutionTime(AbstractModel):
    """Execution time

    """

    def __init__(self):
        r"""
        :param _SubmitTime: Submission time
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubmitTime: str
        :param _StartTime: Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self._SubmitTime = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SubmitTime(self):
        """Submission time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubmitTime

    @SubmitTime.setter
    def SubmitTime(self, SubmitTime):
        self._SubmitTime = SubmitTime

    @property
    def StartTime(self):
        """Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SubmitTime = params.get("SubmitTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Description key-value pair filter, which is used for conditional filtering queries.

    - If there are multiple Filters, the logical relationship between them is AND.

    - If there are multiple Values in the same Filter, the logical relationship between the Values under the same Filter is OR.

    """

    def __init__(self):
        r"""
        :param _Name: Filtering fields
        :type Name: str
        :param _Values: Filtering field values
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """Filtering fields
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """Filtering field values
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
        


class GetRunCallsRequest(AbstractModel):
    """GetRunCalls request structure.

    """

    def __init__(self):
        r"""
        :param _RunUuid: Run UUID
        :type RunUuid: str
        :param _Path: Job path
        :type Path: str
        :param _ProjectId: Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        """
        self._RunUuid = None
        self._Path = None
        self._ProjectId = None

    @property
    def RunUuid(self):
        """Run UUID
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def Path(self):
        """Job path
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ProjectId(self):
        """Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._Path = params.get("Path")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunCallsResponse(AbstractModel):
    """GetRunCalls response structure.

    """

    def __init__(self):
        r"""
        :param _Calls: Job details
        :type Calls: list of RunMetadata
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Calls = None
        self._RequestId = None

    @property
    def Calls(self):
        """Job details
        :rtype: list of RunMetadata
        """
        return self._Calls

    @Calls.setter
    def Calls(self, Calls):
        self._Calls = Calls

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
        if params.get("Calls") is not None:
            self._Calls = []
            for item in params.get("Calls"):
                obj = RunMetadata()
                obj._deserialize(item)
                self._Calls.append(obj)
        self._RequestId = params.get("RequestId")


class GetRunMetadataFileRequest(AbstractModel):
    """GetRunMetadataFile request structure.

    """

    def __init__(self):
        r"""
        :param _RunUuid: Run UUID
        :type RunUuid: str
        :param _ProjectId: Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        :param _Key: File names to be get

The following files are supported by default:
- nextflow.log

When report is specified as true in NFOption during submission, the following files are additionally supported:
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :type Key: str
        :param _Keys: File names to be get in batch

The following files are supported by default:
- nextflow.log

When report is specified as true in NFOption during submission, the following files are additionally supported:
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :type Keys: list of str
        """
        self._RunUuid = None
        self._ProjectId = None
        self._Key = None
        self._Keys = None

    @property
    def RunUuid(self):
        """Run UUID
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        """Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Key(self):
        """File names to be get

The following files are supported by default:
- nextflow.log

When report is specified as true in NFOption during submission, the following files are additionally supported:
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Keys(self):
        """File names to be get in batch

The following files are supported by default:
- nextflow.log

When report is specified as true in NFOption during submission, the following files are additionally supported:
- execution_report.html
- execution_timeline.html
- execution_trace.txt
- pipeline_dag.html
        :rtype: list of str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        self._Key = params.get("Key")
        self._Keys = params.get("Keys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunMetadataFileResponse(AbstractModel):
    """GetRunMetadataFile response structure.

    """

    def __init__(self):
        r"""
        :param _CosSignedUrl: Document pre-signed link that works in a minute
        :type CosSignedUrl: str
        :param _CosSignedUrls: Batch document pre-signed link that works in a minute
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosSignedUrls: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CosSignedUrl = None
        self._CosSignedUrls = None
        self._RequestId = None

    @property
    def CosSignedUrl(self):
        """Document pre-signed link that works in a minute
        :rtype: str
        """
        return self._CosSignedUrl

    @CosSignedUrl.setter
    def CosSignedUrl(self, CosSignedUrl):
        self._CosSignedUrl = CosSignedUrl

    @property
    def CosSignedUrls(self):
        """Batch document pre-signed link that works in a minute
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._CosSignedUrls

    @CosSignedUrls.setter
    def CosSignedUrls(self, CosSignedUrls):
        self._CosSignedUrls = CosSignedUrls

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
        self._CosSignedUrl = params.get("CosSignedUrl")
        self._CosSignedUrls = params.get("CosSignedUrls")
        self._RequestId = params.get("RequestId")


class GetRunStatusRequest(AbstractModel):
    """GetRunStatus request structure.

    """

    def __init__(self):
        r"""
        :param _RunUuid: Run UUID
        :type RunUuid: str
        :param _ProjectId: Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        """
        self._RunUuid = None
        self._ProjectId = None

    @property
    def RunUuid(self):
        """Run UUID
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        """Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRunStatusResponse(AbstractModel):
    """GetRunStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Metadata: Job details
        :type Metadata: :class:`tencentcloud.omics.v20221128.models.RunMetadata`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Metadata = None
        self._RequestId = None

    @property
    def Metadata(self):
        """Job details
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunMetadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

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
        if params.get("Metadata") is not None:
            self._Metadata = RunMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        self._RequestId = params.get("RequestId")


class GitInfo(AbstractModel):
    """Git information

    """

    def __init__(self):
        r"""
        :param _GitHttpPath: Git URL
        :type GitHttpPath: str
        :param _GitUserName: Git username .
        :type GitUserName: str
        :param _GitTokenOrPassword: Git password or Token
        :type GitTokenOrPassword: str
        :param _Branch: Branch
        :type Branch: str
        :param _Tag: Tag
        :type Tag: str
        """
        self._GitHttpPath = None
        self._GitUserName = None
        self._GitTokenOrPassword = None
        self._Branch = None
        self._Tag = None

    @property
    def GitHttpPath(self):
        """Git URL
        :rtype: str
        """
        return self._GitHttpPath

    @GitHttpPath.setter
    def GitHttpPath(self, GitHttpPath):
        self._GitHttpPath = GitHttpPath

    @property
    def GitUserName(self):
        """Git username .
        :rtype: str
        """
        return self._GitUserName

    @GitUserName.setter
    def GitUserName(self, GitUserName):
        self._GitUserName = GitUserName

    @property
    def GitTokenOrPassword(self):
        """Git password or Token
        :rtype: str
        """
        return self._GitTokenOrPassword

    @GitTokenOrPassword.setter
    def GitTokenOrPassword(self, GitTokenOrPassword):
        self._GitTokenOrPassword = GitTokenOrPassword

    @property
    def Branch(self):
        """Branch
        :rtype: str
        """
        return self._Branch

    @Branch.setter
    def Branch(self, Branch):
        self._Branch = Branch

    @property
    def Tag(self):
        """Tag
        :rtype: str
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._GitHttpPath = params.get("GitHttpPath")
        self._GitUserName = params.get("GitUserName")
        self._GitTokenOrPassword = params.get("GitTokenOrPassword")
        self._Branch = params.get("Branch")
        self._Tag = params.get("Tag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportTableFileRequest(AbstractModel):
    """ImportTableFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID associated with the table
        :type ProjectId: str
        :param _Name: Table name: Up to 200 characters in length is supported.
        :type Name: str
        :param _CosUri: Table file COS object path
        :type CosUri: str
        :param _DataType: Data type of each column in the table file. Supported types include Int, Float, String, File, Boolean, Array[Int], Array[Float], Array[String], Array[File], and Array[Boolean].
        :type DataType: list of str
        :param _Description: Table description: Up to 500 characters in length is supported.
        :type Description: str
        """
        self._ProjectId = None
        self._Name = None
        self._CosUri = None
        self._DataType = None
        self._Description = None

    @property
    def ProjectId(self):
        """Project ID associated with the table
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        """Table name: Up to 200 characters in length is supported.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CosUri(self):
        """Table file COS object path
        :rtype: str
        """
        return self._CosUri

    @CosUri.setter
    def CosUri(self, CosUri):
        self._CosUri = CosUri

    @property
    def DataType(self):
        """Data type of each column in the table file. Supported types include Int, Float, String, File, Boolean, Array[Int], Array[Float], Array[String], Array[File], and Array[Boolean].
        :rtype: list of str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def Description(self):
        """Table description: Up to 500 characters in length is supported.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._CosUri = params.get("CosUri")
        self._DataType = params.get("DataType")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportTableFileResponse(AbstractModel):
    """ImportTableFile response structure.

    """

    def __init__(self):
        r"""
        :param _TableId: Table ID
        :type TableId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TableId = None
        self._RequestId = None

    @property
    def TableId(self):
        """Table ID
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

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
        self._TableId = params.get("TableId")
        self._RequestId = params.get("RequestId")


class LimitRange(AbstractModel):
    """Resource limit scope

    """

    def __init__(self):
        r"""
        :param _MaxCPU: Maximum CPU setting
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxCPU: str
        :param _MaxMemory: Maximum memory setting (unit: Mi, Gi, Ti, M, G, and T)
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxMemory: str
        """
        self._MaxCPU = None
        self._MaxMemory = None

    @property
    def MaxCPU(self):
        """Maximum CPU setting
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MaxCPU

    @MaxCPU.setter
    def MaxCPU(self, MaxCPU):
        self._MaxCPU = MaxCPU

    @property
    def MaxMemory(self):
        """Maximum memory setting (unit: Mi, Gi, Ti, M, G, and T)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MaxMemory

    @MaxMemory.setter
    def MaxMemory(self, MaxMemory):
        self._MaxMemory = MaxMemory


    def _deserialize(self, params):
        self._MaxCPU = params.get("MaxCPU")
        self._MaxMemory = params.get("MaxMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVolumeRequest(AbstractModel):
    """ModifyVolume request structure.

    """

    def __init__(self):
        r"""
        :param _VolumeId: Volume ID
        :type VolumeId: str
        :param _Name: Name
        :type Name: str
        :param _Description: Description
        :type Description: str
        """
        self._VolumeId = None
        self._Name = None
        self._Description = None

    @property
    def VolumeId(self):
        """Volume ID
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def Name(self):
        """Name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVolumeResponse(AbstractModel):
    """ModifyVolume response structure.

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


class NFOption(AbstractModel):
    """Nextflow option

    """

    def __init__(self):
        r"""
        :param _Config: Config.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Config: str
        :param _Profile: Profile.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Profile: str
        :param _Report: Report.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Report: bool
        :param _Resume: Resume.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Resume: bool
        :param _NFVersion: Nextflow engine version. Valid values:
- 22.10.4
- 22.10.8 
- 23.10.1
Note: This field may return null, indicating that no valid values can be obtained.
        :type NFVersion: str
        """
        self._Config = None
        self._Profile = None
        self._Report = None
        self._Resume = None
        self._NFVersion = None

    @property
    def Config(self):
        """Config.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Profile(self):
        """Profile.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Report(self):
        """Report.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Report

    @Report.setter
    def Report(self, Report):
        self._Report = Report

    @property
    def Resume(self):
        """Resume.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Resume

    @Resume.setter
    def Resume(self, Resume):
        self._Resume = Resume

    @property
    def NFVersion(self):
        """Nextflow engine version. Valid values:
- 22.10.4
- 22.10.8 
- 23.10.1
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NFVersion

    @NFVersion.setter
    def NFVersion(self, NFVersion):
        self._NFVersion = NFVersion


    def _deserialize(self, params):
        self._Config = params.get("Config")
        self._Profile = params.get("Profile")
        self._Report = params.get("Report")
        self._Resume = params.get("Resume")
        self._NFVersion = params.get("NFVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIds(AbstractModel):
    """Cloud resource ID

    """

    def __init__(self):
        r"""
        :param _VPCId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VPCId: str
        :param _SubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _SecurityGroupId: Security group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SecurityGroupId: str
        :param _TDSQLCId: TDSQL-C for MySQL database ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TDSQLCId: str
        :param _CFSId:  CFS ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFSId: str
        :param _CFSStorageType: CFS type. Valid values:
- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFSStorageType: str
        :param _CVMId:  Cloud Virtual Machine ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CVMId: str
        :param _EKSId: Elastic container cluster ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EKSId: str
        """
        self._VPCId = None
        self._SubnetId = None
        self._SecurityGroupId = None
        self._TDSQLCId = None
        self._CFSId = None
        self._CFSStorageType = None
        self._CVMId = None
        self._EKSId = None

    @property
    def VPCId(self):
        """VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VPCId

    @VPCId.setter
    def VPCId(self, VPCId):
        self._VPCId = VPCId

    @property
    def SubnetId(self):
        """Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SecurityGroupId(self):
        """Security group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def TDSQLCId(self):
        """TDSQL-C for MySQL database ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TDSQLCId

    @TDSQLCId.setter
    def TDSQLCId(self, TDSQLCId):
        self._TDSQLCId = TDSQLCId

    @property
    def CFSId(self):
        """ CFS ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFSId

    @CFSId.setter
    def CFSId(self, CFSId):
        self._CFSId = CFSId

    @property
    def CFSStorageType(self):
        """CFS type. Valid values:
- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CFSStorageType

    @CFSStorageType.setter
    def CFSStorageType(self, CFSStorageType):
        self._CFSStorageType = CFSStorageType

    @property
    def CVMId(self):
        """ Cloud Virtual Machine ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CVMId

    @CVMId.setter
    def CVMId(self, CVMId):
        self._CVMId = CVMId

    @property
    def EKSId(self):
        """Elastic container cluster ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EKSId

    @EKSId.setter
    def EKSId(self, EKSId):
        self._EKSId = EKSId


    def _deserialize(self, params):
        self._VPCId = params.get("VPCId")
        self._SubnetId = params.get("SubnetId")
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._TDSQLCId = params.get("TDSQLCId")
        self._CFSId = params.get("CFSId")
        self._CFSStorageType = params.get("CFSStorageType")
        self._CVMId = params.get("CVMId")
        self._EKSId = params.get("EKSId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceQuota(AbstractModel):
    """Resource quota

    """

    def __init__(self):
        r"""
        :param _CPULimit: CPU limit setting
Note: This field may return null, indicating that no valid values can be obtained.
        :type CPULimit: str
        :param _MemoryLimit: Memory limit setting (Unit: Mi, Gi, Ti, M, G, and T)
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryLimit: str
        :param _Pods: Pod quantity setting
Note: This field may return null, indicating that no valid values can be obtained.
        :type Pods: str
        """
        self._CPULimit = None
        self._MemoryLimit = None
        self._Pods = None

    @property
    def CPULimit(self):
        """CPU limit setting
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CPULimit

    @CPULimit.setter
    def CPULimit(self, CPULimit):
        self._CPULimit = CPULimit

    @property
    def MemoryLimit(self):
        """Memory limit setting (Unit: Mi, Gi, Ti, M, G, and T)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def Pods(self):
        """Pod quantity setting
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Pods

    @Pods.setter
    def Pods(self, Pods):
        self._Pods = Pods


    def _deserialize(self, params):
        self._CPULimit = params.get("CPULimit")
        self._MemoryLimit = params.get("MemoryLimit")
        self._Pods = params.get("Pods")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsRequest(AbstractModel):
    """RetryRuns request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID. (If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        :param _RunGroupId: The run group ID that needs to be retried
        :type RunGroupId: str
        :param _RunUuids: The run UUID that needs to be retried
        :type RunUuids: list of str
        :param _WDLOption: WDL running option. If you leave it blank, the retried run group running option will be used.
        :type WDLOption: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _NFOption: Nextflow running option. If you leave it blank, the retried run group running option will be used.
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        self._ProjectId = None
        self._RunGroupId = None
        self._RunUuids = None
        self._WDLOption = None
        self._NFOption = None

    @property
    def ProjectId(self):
        """Project ID. (If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RunGroupId(self):
        """The run group ID that needs to be retried
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def RunUuids(self):
        """The run UUID that needs to be retried
        :rtype: list of str
        """
        return self._RunUuids

    @RunUuids.setter
    def RunUuids(self, RunUuids):
        self._RunUuids = RunUuids

    @property
    def WDLOption(self):
        """WDL running option. If you leave it blank, the retried run group running option will be used.
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._WDLOption

    @WDLOption.setter
    def WDLOption(self, WDLOption):
        self._WDLOption = WDLOption

    @property
    def NFOption(self):
        """Nextflow running option. If you leave it blank, the retried run group running option will be used.
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RunGroupId = params.get("RunGroupId")
        self._RunUuids = params.get("RunUuids")
        if params.get("WDLOption") is not None:
            self._WDLOption = RunOption()
            self._WDLOption._deserialize(params.get("WDLOption"))
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryRunsResponse(AbstractModel):
    """RetryRuns response structure.

    """

    def __init__(self):
        r"""
        :param _RunGroupId: New run group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RunGroupId = None
        self._RequestId = None

    @property
    def RunGroupId(self):
        """New run group ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

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
        self._RunGroupId = params.get("RunGroupId")
        self._RequestId = params.get("RequestId")


class Run(AbstractModel):
    """Run

    """

    def __init__(self):
        r"""
        :param _RunUuid: Run UUID
        :type RunUuid: str
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _RunGroupId: Run group ID
        :type RunGroupId: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _UserDefinedId: User-defined ID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserDefinedId: str
        :param _TableId: Table ID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableId: str
        :param _TableRowUuid: Table row UUID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableRowUuid: str
        :param _Status: Run status
        :type Status: str
        :param _Input: Run input
        :type Input: str
        :param _Option: Running option
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _ExecutionTime: Execution time
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param _Cache: Cache information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.omics.v20221128.models.CacheInfo`
        :param _ErrorMessage: Error message
        :type ErrorMessage: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        """
        self._RunUuid = None
        self._ProjectId = None
        self._ApplicationId = None
        self._RunGroupId = None
        self._EnvironmentId = None
        self._UserDefinedId = None
        self._TableId = None
        self._TableRowUuid = None
        self._Status = None
        self._Input = None
        self._Option = None
        self._ExecutionTime = None
        self._Cache = None
        self._ErrorMessage = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def RunUuid(self):
        """Run UUID
        :rtype: str
        """
        return self._RunUuid

    @RunUuid.setter
    def RunUuid(self, RunUuid):
        self._RunUuid = RunUuid

    @property
    def ProjectId(self):
        """Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ApplicationId(self):
        """Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RunGroupId(self):
        """Run group ID
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def EnvironmentId(self):
        """Environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def UserDefinedId(self):
        """User-defined ID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserDefinedId

    @UserDefinedId.setter
    def UserDefinedId(self, UserDefinedId):
        self._UserDefinedId = UserDefinedId

    @property
    def TableId(self):
        """Table ID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableRowUuid(self):
        """Table row UUID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableRowUuid

    @TableRowUuid.setter
    def TableRowUuid(self, TableRowUuid):
        self._TableRowUuid = TableRowUuid

    @property
    def Status(self):
        """Run status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        """Run input
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Option(self):
        warnings.warn("parameter `Option` is deprecated", DeprecationWarning) 

        """Running option
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._Option

    @Option.setter
    def Option(self, Option):
        warnings.warn("parameter `Option` is deprecated", DeprecationWarning) 

        self._Option = Option

    @property
    def ExecutionTime(self):
        """Execution time
        :rtype: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        """
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def Cache(self):
        """Cache information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.omics.v20221128.models.CacheInfo`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def ErrorMessage(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._RunUuid = params.get("RunUuid")
        self._ProjectId = params.get("ProjectId")
        self._ApplicationId = params.get("ApplicationId")
        self._RunGroupId = params.get("RunGroupId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._UserDefinedId = params.get("UserDefinedId")
        self._TableId = params.get("TableId")
        self._TableRowUuid = params.get("TableRowUuid")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        if params.get("ExecutionTime") is not None:
            self._ExecutionTime = ExecutionTime()
            self._ExecutionTime._deserialize(params.get("ExecutionTime"))
        if params.get("Cache") is not None:
            self._Cache = CacheInfo()
            self._Cache._deserialize(params.get("Cache"))
        self._ErrorMessage = params.get("ErrorMessage")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationRequest(AbstractModel):
    """RunApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _Name: Run group name
        :type Name: str
        :param _EnvironmentId: Delivery environment ID
        :type EnvironmentId: str
        :param _ProjectId: Project ID. (If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        :param _Description: Run group description
        :type Description: str
        :param _InputCosUri: Run input COS path. (Either InputBase64 or InputCosUri must be selected.)
        :type InputCosUri: str
        :param _InputBase64: Run input JSON. Base64 encoding is required. (Either InputBase64 or InputCosUri must be selected.)
        :type InputBase64: str
        :param _TableId: Batch deliver table ID. Leaving it blank indicates delivery in singleton mode.
        :type TableId: str
        :param _TableRowUuids: Batch deliver table row UUID. Leaving it blank indicates all rows of the table.
        :type TableRowUuids: list of str
        :param _CacheClearDelay: Run cache cleanup time (hours). Leaving it blank or entering 0 indicates no cleanup.
        :type CacheClearDelay: int
        :param _ApplicationVersionId: Application version ID. Leaving it blank indicates that the latest version is used.
        :type ApplicationVersionId: str
        :param _Option: WDL running option
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _NFOption: Nextflow running option
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        :param _WorkDir: Working directory. You can fill in the absolute path in the specified volume. If you leave it blank, the default path in the default volume will be used. Currently, only Nextflow is supported.
        :type WorkDir: str
        :param _AccessMode: Access mode. Leaving it blank indicates it is private by default. Valid values:
- PRIVATE: Private application
- PUBLIC: Public application
        :type AccessMode: str
        :param _VolumeIds: Volume ID. If you leave it blank, the default volume will be used. Currently, only Nextflow is supported.
        :type VolumeIds: list of str
        """
        self._ApplicationId = None
        self._Name = None
        self._EnvironmentId = None
        self._ProjectId = None
        self._Description = None
        self._InputCosUri = None
        self._InputBase64 = None
        self._TableId = None
        self._TableRowUuids = None
        self._CacheClearDelay = None
        self._ApplicationVersionId = None
        self._Option = None
        self._NFOption = None
        self._WorkDir = None
        self._AccessMode = None
        self._VolumeIds = None

    @property
    def ApplicationId(self):
        """Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def Name(self):
        """Run group name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnvironmentId(self):
        """Delivery environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ProjectId(self):
        """Project ID. (If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """Run group description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InputCosUri(self):
        """Run input COS path. (Either InputBase64 or InputCosUri must be selected.)
        :rtype: str
        """
        return self._InputCosUri

    @InputCosUri.setter
    def InputCosUri(self, InputCosUri):
        self._InputCosUri = InputCosUri

    @property
    def InputBase64(self):
        """Run input JSON. Base64 encoding is required. (Either InputBase64 or InputCosUri must be selected.)
        :rtype: str
        """
        return self._InputBase64

    @InputBase64.setter
    def InputBase64(self, InputBase64):
        self._InputBase64 = InputBase64

    @property
    def TableId(self):
        """Batch deliver table ID. Leaving it blank indicates delivery in singleton mode.
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def TableRowUuids(self):
        """Batch deliver table row UUID. Leaving it blank indicates all rows of the table.
        :rtype: list of str
        """
        return self._TableRowUuids

    @TableRowUuids.setter
    def TableRowUuids(self, TableRowUuids):
        self._TableRowUuids = TableRowUuids

    @property
    def CacheClearDelay(self):
        """Run cache cleanup time (hours). Leaving it blank or entering 0 indicates no cleanup.
        :rtype: int
        """
        return self._CacheClearDelay

    @CacheClearDelay.setter
    def CacheClearDelay(self, CacheClearDelay):
        self._CacheClearDelay = CacheClearDelay

    @property
    def ApplicationVersionId(self):
        """Application version ID. Leaving it blank indicates that the latest version is used.
        :rtype: str
        """
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def Option(self):
        """WDL running option
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def NFOption(self):
        """Nextflow running option
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption

    @property
    def WorkDir(self):
        """Working directory. You can fill in the absolute path in the specified volume. If you leave it blank, the default path in the default volume will be used. Currently, only Nextflow is supported.
        :rtype: str
        """
        return self._WorkDir

    @WorkDir.setter
    def WorkDir(self, WorkDir):
        self._WorkDir = WorkDir

    @property
    def AccessMode(self):
        """Access mode. Leaving it blank indicates it is private by default. Valid values:
- PRIVATE: Private application
- PUBLIC: Public application
        :rtype: str
        """
        return self._AccessMode

    @AccessMode.setter
    def AccessMode(self, AccessMode):
        self._AccessMode = AccessMode

    @property
    def VolumeIds(self):
        """Volume ID. If you leave it blank, the default volume will be used. Currently, only Nextflow is supported.
        :rtype: list of str
        """
        return self._VolumeIds

    @VolumeIds.setter
    def VolumeIds(self, VolumeIds):
        self._VolumeIds = VolumeIds


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._Name = params.get("Name")
        self._EnvironmentId = params.get("EnvironmentId")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._InputCosUri = params.get("InputCosUri")
        self._InputBase64 = params.get("InputBase64")
        self._TableId = params.get("TableId")
        self._TableRowUuids = params.get("TableRowUuids")
        self._CacheClearDelay = params.get("CacheClearDelay")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        self._WorkDir = params.get("WorkDir")
        self._AccessMode = params.get("AccessMode")
        self._VolumeIds = params.get("VolumeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunApplicationResponse(AbstractModel):
    """RunApplication response structure.

    """

    def __init__(self):
        r"""
        :param _RunGroupId: Run group ID
        :type RunGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RunGroupId = None
        self._RequestId = None

    @property
    def RunGroupId(self):
        """Run group ID
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

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
        self._RunGroupId = params.get("RunGroupId")
        self._RequestId = params.get("RequestId")


class RunGroup(AbstractModel):
    """Run

    """

    def __init__(self):
        r"""
        :param _RunGroupId: Run group ID
        :type RunGroupId: str
        :param _ProjectId: Project ID
        :type ProjectId: str
        :param _ProjectName: Project name
        :type ProjectName: str
        :param _ApplicationId: Application ID
        :type ApplicationId: str
        :param _ApplicationName: Application name
        :type ApplicationName: str
        :param _ApplicationType: Application type
        :type ApplicationType: str
        :param _EnvironmentId: Environment ID
        :type EnvironmentId: str
        :param _EnvironmentName: Environment name
        :type EnvironmentName: str
        :param _TableId: Table ID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableId: str
        :param _Name: Run name
        :type Name: str
        :param _Description: Run description
        :type Description: str
        :param _Status: Run status
        :type Status: str
        :param _Input: Run input
        :type Input: str
        :param _Option: WDL running option
        :type Option: :class:`tencentcloud.omics.v20221128.models.RunOption`
        :param _NFOption: Nextflow running option
Note: This field may return null, indicating that no valid values can be obtained.
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        :param _TotalRun: Total number of runs
        :type TotalRun: int
        :param _RunStatusCounts: Number of runs in various status
        :type RunStatusCounts: list of RunStatusCount
        :param _ExecutionTime: Execution time
        :type ExecutionTime: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        :param _ErrorMessage: Error message
        :type ErrorMessage: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        :param _Creator: Creator
Note: This field may return null, indicating that no valid values can be obtained.
        :type Creator: str
        :param _CreatorId: Creator ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatorId: str
        :param _ResultNotify: Running result notification method
Note: This field may return null, indicating that no valid values can be obtained.
        :type ResultNotify: str
        :param _ApplicationVersion: Application version
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationVersion: :class:`tencentcloud.omics.v20221128.models.ApplicationVersion`
        """
        self._RunGroupId = None
        self._ProjectId = None
        self._ProjectName = None
        self._ApplicationId = None
        self._ApplicationName = None
        self._ApplicationType = None
        self._EnvironmentId = None
        self._EnvironmentName = None
        self._TableId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Input = None
        self._Option = None
        self._NFOption = None
        self._TotalRun = None
        self._RunStatusCounts = None
        self._ExecutionTime = None
        self._ErrorMessage = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Creator = None
        self._CreatorId = None
        self._ResultNotify = None
        self._ApplicationVersion = None

    @property
    def RunGroupId(self):
        """Run group ID
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def ProjectId(self):
        """Project ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        """Project name
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ApplicationId(self):
        """Application ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        """Application name
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationType(self):
        """Application type
        :rtype: str
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def EnvironmentId(self):
        """Environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def EnvironmentName(self):
        """Environment name
        :rtype: str
        """
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def TableId(self):
        """Table ID. Null for running in singleton mode.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def Name(self):
        """Run name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Run description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """Run status
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Input(self):
        """Run input
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Option(self):
        """WDL running option
        :rtype: :class:`tencentcloud.omics.v20221128.models.RunOption`
        """
        return self._Option

    @Option.setter
    def Option(self, Option):
        self._Option = Option

    @property
    def NFOption(self):
        """Nextflow running option
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption

    @property
    def TotalRun(self):
        """Total number of runs
        :rtype: int
        """
        return self._TotalRun

    @TotalRun.setter
    def TotalRun(self, TotalRun):
        self._TotalRun = TotalRun

    @property
    def RunStatusCounts(self):
        """Number of runs in various status
        :rtype: list of RunStatusCount
        """
        return self._RunStatusCounts

    @RunStatusCounts.setter
    def RunStatusCounts(self, RunStatusCounts):
        self._RunStatusCounts = RunStatusCounts

    @property
    def ExecutionTime(self):
        """Execution time
        :rtype: :class:`tencentcloud.omics.v20221128.models.ExecutionTime`
        """
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def ErrorMessage(self):
        """Error message
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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
    def UpdateTime(self):
        """Update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Creator(self):
        """Creator
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatorId(self):
        """Creator ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def ResultNotify(self):
        """Running result notification method
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResultNotify

    @ResultNotify.setter
    def ResultNotify(self, ResultNotify):
        self._ResultNotify = ResultNotify

    @property
    def ApplicationVersion(self):
        """Application version
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.omics.v20221128.models.ApplicationVersion`
        """
        return self._ApplicationVersion

    @ApplicationVersion.setter
    def ApplicationVersion(self, ApplicationVersion):
        self._ApplicationVersion = ApplicationVersion


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationType = params.get("ApplicationType")
        self._EnvironmentId = params.get("EnvironmentId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._TableId = params.get("TableId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Input = params.get("Input")
        if params.get("Option") is not None:
            self._Option = RunOption()
            self._Option._deserialize(params.get("Option"))
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        self._TotalRun = params.get("TotalRun")
        if params.get("RunStatusCounts") is not None:
            self._RunStatusCounts = []
            for item in params.get("RunStatusCounts"):
                obj = RunStatusCount()
                obj._deserialize(item)
                self._RunStatusCounts.append(obj)
        if params.get("ExecutionTime") is not None:
            self._ExecutionTime = ExecutionTime()
            self._ExecutionTime._deserialize(params.get("ExecutionTime"))
        self._ErrorMessage = params.get("ErrorMessage")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Creator = params.get("Creator")
        self._CreatorId = params.get("CreatorId")
        self._ResultNotify = params.get("ResultNotify")
        if params.get("ApplicationVersion") is not None:
            self._ApplicationVersion = ApplicationVersion()
            self._ApplicationVersion._deserialize(params.get("ApplicationVersion"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMetadata(AbstractModel):
    """Run job details

    """

    def __init__(self):
        r"""
        :param _RunType: Run type
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunType: str
        :param _RunId: Run ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type RunId: str
        :param _ParentId: Parent layer ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ParentId: str
        :param _JobId: Job ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type JobId: str
        :param _CallName: Job name
Note: This field may return null, indicating that no valid values can be obtained.
        :type CallName: str
        :param _ScatterIndex: Scatter index
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScatterIndex: str
        :param _Input: Input
Note: This field may return null, indicating that no valid values can be obtained.
        :type Input: str
        :param _Output: Output
Note: This field may return null, indicating that no valid values can be obtained.
        :type Output: str
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _ErrorMessage: Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param _StartTime: Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _SubmitTime: Submission time
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubmitTime: str
        :param _EndTime: End time
Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        :param _Command: Command Line
Note: This field may return null, indicating that no valid values can be obtained.
        :type Command: str
        :param _Runtime: Runtime
Note: This field may return null, indicating that no valid values can be obtained.
        :type Runtime: str
        :param _Preprocess: Preprocessing
Note: This field may return null, indicating that no valid values can be obtained.
        :type Preprocess: bool
        :param _PostProcess: Post-processing
Note: This field may return null, indicating that no valid values can be obtained.
        :type PostProcess: bool
        :param _CallCached: Cache hit
Note: This field may return null, indicating that no valid values can be obtained.
        :type CallCached: bool
        :param _Stdout: Standard output
Note: This field may return null, indicating that no valid values can be obtained.
        :type Stdout: str
        :param _Stderr: Error output
Note: This field may return null, indicating that no valid values can be obtained.
        :type Stderr: str
        :param _Meta: Other information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Meta: str
        """
        self._RunType = None
        self._RunId = None
        self._ParentId = None
        self._JobId = None
        self._CallName = None
        self._ScatterIndex = None
        self._Input = None
        self._Output = None
        self._Status = None
        self._ErrorMessage = None
        self._StartTime = None
        self._SubmitTime = None
        self._EndTime = None
        self._Command = None
        self._Runtime = None
        self._Preprocess = None
        self._PostProcess = None
        self._CallCached = None
        self._Stdout = None
        self._Stderr = None
        self._Meta = None

    @property
    def RunType(self):
        """Run type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunType

    @RunType.setter
    def RunType(self, RunType):
        self._RunType = RunType

    @property
    def RunId(self):
        """Run ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def ParentId(self):
        """Parent layer ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def JobId(self):
        """Job ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def CallName(self):
        """Job name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CallName

    @CallName.setter
    def CallName(self, CallName):
        self._CallName = CallName

    @property
    def ScatterIndex(self):
        """Scatter index
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ScatterIndex

    @ScatterIndex.setter
    def ScatterIndex(self, ScatterIndex):
        self._ScatterIndex = ScatterIndex

    @property
    def Input(self):
        """Input
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Output(self):
        """Output
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def Status(self):
        """Status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMessage(self):
        """Error message
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def StartTime(self):
        """Start time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SubmitTime(self):
        """Submission time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubmitTime

    @SubmitTime.setter
    def SubmitTime(self, SubmitTime):
        self._SubmitTime = SubmitTime

    @property
    def EndTime(self):
        """End time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Command(self):
        """Command Line
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Runtime(self):
        """Runtime
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Preprocess(self):
        """Preprocessing
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Preprocess

    @Preprocess.setter
    def Preprocess(self, Preprocess):
        self._Preprocess = Preprocess

    @property
    def PostProcess(self):
        """Post-processing
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._PostProcess

    @PostProcess.setter
    def PostProcess(self, PostProcess):
        self._PostProcess = PostProcess

    @property
    def CallCached(self):
        """Cache hit
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._CallCached

    @CallCached.setter
    def CallCached(self, CallCached):
        self._CallCached = CallCached

    @property
    def Stdout(self):
        """Standard output
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Stdout

    @Stdout.setter
    def Stdout(self, Stdout):
        self._Stdout = Stdout

    @property
    def Stderr(self):
        """Error output
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Stderr

    @Stderr.setter
    def Stderr(self, Stderr):
        self._Stderr = Stderr

    @property
    def Meta(self):
        """Other information
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta


    def _deserialize(self, params):
        self._RunType = params.get("RunType")
        self._RunId = params.get("RunId")
        self._ParentId = params.get("ParentId")
        self._JobId = params.get("JobId")
        self._CallName = params.get("CallName")
        self._ScatterIndex = params.get("ScatterIndex")
        self._Input = params.get("Input")
        self._Output = params.get("Output")
        self._Status = params.get("Status")
        self._ErrorMessage = params.get("ErrorMessage")
        self._StartTime = params.get("StartTime")
        self._SubmitTime = params.get("SubmitTime")
        self._EndTime = params.get("EndTime")
        self._Command = params.get("Command")
        self._Runtime = params.get("Runtime")
        self._Preprocess = params.get("Preprocess")
        self._PostProcess = params.get("PostProcess")
        self._CallCached = params.get("CallCached")
        self._Stdout = params.get("Stdout")
        self._Stderr = params.get("Stderr")
        self._Meta = params.get("Meta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunOption(AbstractModel):
    """Application running option

    """

    def __init__(self):
        r"""
        :param _FailureMode: Operation failure mode. Valid values:
- ContinueWhilePossible
- NoNewCalls
        :type FailureMode: str
        :param _UseCallCache: Whether to use the Call-Caching feature.
        :type UseCallCache: bool
        :param _UseErrorOnHold: Whether to use the error suspension feature.
        :type UseErrorOnHold: bool
        :param _FinalWorkflowOutputsDir: Output archive COS path
Note: This field may return null, indicating that no valid values can be obtained.
        :type FinalWorkflowOutputsDir: str
        :param _UseRelativeOutputPaths: Whether to use the relative directory archive output.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UseRelativeOutputPaths: bool
        """
        self._FailureMode = None
        self._UseCallCache = None
        self._UseErrorOnHold = None
        self._FinalWorkflowOutputsDir = None
        self._UseRelativeOutputPaths = None

    @property
    def FailureMode(self):
        """Operation failure mode. Valid values:
- ContinueWhilePossible
- NoNewCalls
        :rtype: str
        """
        return self._FailureMode

    @FailureMode.setter
    def FailureMode(self, FailureMode):
        self._FailureMode = FailureMode

    @property
    def UseCallCache(self):
        """Whether to use the Call-Caching feature.
        :rtype: bool
        """
        return self._UseCallCache

    @UseCallCache.setter
    def UseCallCache(self, UseCallCache):
        self._UseCallCache = UseCallCache

    @property
    def UseErrorOnHold(self):
        """Whether to use the error suspension feature.
        :rtype: bool
        """
        return self._UseErrorOnHold

    @UseErrorOnHold.setter
    def UseErrorOnHold(self, UseErrorOnHold):
        self._UseErrorOnHold = UseErrorOnHold

    @property
    def FinalWorkflowOutputsDir(self):
        """Output archive COS path
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FinalWorkflowOutputsDir

    @FinalWorkflowOutputsDir.setter
    def FinalWorkflowOutputsDir(self, FinalWorkflowOutputsDir):
        self._FinalWorkflowOutputsDir = FinalWorkflowOutputsDir

    @property
    def UseRelativeOutputPaths(self):
        """Whether to use the relative directory archive output.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._UseRelativeOutputPaths

    @UseRelativeOutputPaths.setter
    def UseRelativeOutputPaths(self, UseRelativeOutputPaths):
        self._UseRelativeOutputPaths = UseRelativeOutputPaths


    def _deserialize(self, params):
        self._FailureMode = params.get("FailureMode")
        self._UseCallCache = params.get("UseCallCache")
        self._UseErrorOnHold = params.get("UseErrorOnHold")
        self._FinalWorkflowOutputsDir = params.get("FinalWorkflowOutputsDir")
        self._UseRelativeOutputPaths = params.get("UseRelativeOutputPaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunStatusCount(AbstractModel):
    """Run running status

    """

    def __init__(self):
        r"""
        :param _Status: Status
        :type Status: str
        :param _Count: Quantity
        :type Count: int
        """
        self._Status = None
        self._Count = None

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
    def Count(self):
        """Quantity
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkflowRequest(AbstractModel):
    """RunWorkflow request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Run group name
        :type Name: str
        :param _EnvironmentId: Delivery environment ID
        :type EnvironmentId: str
        :param _GitSource: Workflow Git repository information
        :type GitSource: :class:`tencentcloud.omics.v20221128.models.GitInfo`
        :param _Type: Workflow type

Supported type:
- NEXTFLOW
        :type Type: str
        :param _NFOption: Nextflow option
        :type NFOption: :class:`tencentcloud.omics.v20221128.models.NFOption`
        :param _ProjectId: Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        :param _Description: Run group description
        :type Description: str
        :param _InputBase64: Run input JSON. Base64 encoding is required.
(Either InputBase64 or InputCosUri must be selected.)
        :type InputBase64: str
        :param _InputCosUri: Run input COS path
(Either InputBase64 or InputCosUri must be selected.)
        :type InputCosUri: str
        :param _CacheClearDelay: Run cache cleanup time (hours). Leaving it blank or entering 0 indicates no cleanup.
        :type CacheClearDelay: int
        :param _WorkDir: Working directory. You can fill in the absolute path in the specified volume. If you leave it blank, the default path in the default volume will be used. Currently, only Nextflow is supported.
        :type WorkDir: str
        :param _VolumeIds: Volume ID. If you leave it blank, the default volume will be used. Currently, only Nextflow is supported.
        :type VolumeIds: list of str
        """
        self._Name = None
        self._EnvironmentId = None
        self._GitSource = None
        self._Type = None
        self._NFOption = None
        self._ProjectId = None
        self._Description = None
        self._InputBase64 = None
        self._InputCosUri = None
        self._CacheClearDelay = None
        self._WorkDir = None
        self._VolumeIds = None

    @property
    def Name(self):
        """Run group name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EnvironmentId(self):
        """Delivery environment ID
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def GitSource(self):
        """Workflow Git repository information
        :rtype: :class:`tencentcloud.omics.v20221128.models.GitInfo`
        """
        return self._GitSource

    @GitSource.setter
    def GitSource(self, GitSource):
        self._GitSource = GitSource

    @property
    def Type(self):
        """Workflow type

Supported type:
- NEXTFLOW
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NFOption(self):
        """Nextflow option
        :rtype: :class:`tencentcloud.omics.v20221128.models.NFOption`
        """
        return self._NFOption

    @NFOption.setter
    def NFOption(self, NFOption):
        self._NFOption = NFOption

    @property
    def ProjectId(self):
        """Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """Run group description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InputBase64(self):
        """Run input JSON. Base64 encoding is required.
(Either InputBase64 or InputCosUri must be selected.)
        :rtype: str
        """
        return self._InputBase64

    @InputBase64.setter
    def InputBase64(self, InputBase64):
        self._InputBase64 = InputBase64

    @property
    def InputCosUri(self):
        """Run input COS path
(Either InputBase64 or InputCosUri must be selected.)
        :rtype: str
        """
        return self._InputCosUri

    @InputCosUri.setter
    def InputCosUri(self, InputCosUri):
        self._InputCosUri = InputCosUri

    @property
    def CacheClearDelay(self):
        """Run cache cleanup time (hours). Leaving it blank or entering 0 indicates no cleanup.
        :rtype: int
        """
        return self._CacheClearDelay

    @CacheClearDelay.setter
    def CacheClearDelay(self, CacheClearDelay):
        self._CacheClearDelay = CacheClearDelay

    @property
    def WorkDir(self):
        """Working directory. You can fill in the absolute path in the specified volume. If you leave it blank, the default path in the default volume will be used. Currently, only Nextflow is supported.
        :rtype: str
        """
        return self._WorkDir

    @WorkDir.setter
    def WorkDir(self, WorkDir):
        self._WorkDir = WorkDir

    @property
    def VolumeIds(self):
        """Volume ID. If you leave it blank, the default volume will be used. Currently, only Nextflow is supported.
        :rtype: list of str
        """
        return self._VolumeIds

    @VolumeIds.setter
    def VolumeIds(self, VolumeIds):
        self._VolumeIds = VolumeIds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EnvironmentId = params.get("EnvironmentId")
        if params.get("GitSource") is not None:
            self._GitSource = GitInfo()
            self._GitSource._deserialize(params.get("GitSource"))
        self._Type = params.get("Type")
        if params.get("NFOption") is not None:
            self._NFOption = NFOption()
            self._NFOption._deserialize(params.get("NFOption"))
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._InputBase64 = params.get("InputBase64")
        self._InputCosUri = params.get("InputCosUri")
        self._CacheClearDelay = params.get("CacheClearDelay")
        self._WorkDir = params.get("WorkDir")
        self._VolumeIds = params.get("VolumeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkflowResponse(AbstractModel):
    """RunWorkflow response structure.

    """

    def __init__(self):
        r"""
        :param _RunGroupId: Run group ID
        :type RunGroupId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RunGroupId = None
        self._RequestId = None

    @property
    def RunGroupId(self):
        """Run group ID
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

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
        self._RunGroupId = params.get("RunGroupId")
        self._RequestId = params.get("RequestId")


class SecurityGroupOption(AbstractModel):
    """Security group configuration

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: Security group ID
        :type SecurityGroupId: str
        """
        self._SecurityGroupId = None

    @property
    def SecurityGroupId(self):
        """Security group ID
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOption(AbstractModel):
    """CFS configuration

    """

    def __init__(self):
        r"""
        :param _StorageType: CFS type. Valid values:
- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
        :type StorageType: str
        :param _Zone: CFS availability zone
        :type Zone: str
        :param _Capacity: CFS capacity in GiB, required for the Turbo series
- Standard Turbo has a minimum capacity of 40 TiB, or 40,960 GiB; the capacity expansion step is 20 TiB, or 20,480 GiB.
- High-performance Turbo has a minimum capacity of 20 TiB, or 20,480 GiB; the capacity expansion step is 10 TiB, or 10,240 GiB.
        :type Capacity: int
        """
        self._StorageType = None
        self._Zone = None
        self._Capacity = None

    @property
    def StorageType(self):
        """CFS type. Valid values:
- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def Zone(self):
        """CFS availability zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Capacity(self):
        """CFS capacity in GiB, required for the Turbo series
- Standard Turbo has a minimum capacity of 40 TiB, or 40,960 GiB; the capacity expansion step is 20 TiB, or 20,480 GiB.
- High-performance Turbo has a minimum capacity of 20 TiB, or 20,480 GiB; the capacity expansion step is 10 TiB, or 10,240 GiB.
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity


    def _deserialize(self, params):
        self._StorageType = params.get("StorageType")
        self._Zone = params.get("Zone")
        self._Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Table(AbstractModel):
    """Table

    """

    def __init__(self):
        r"""
        :param _TableId: Table ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableId: str
        :param _ProjectId: Associated project ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProjectId: str
        :param _Name: Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Description: Table description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Columns: Table column
Note: This field may return null, indicating that no valid values can be obtained.
        :type Columns: list of TableColumn
        :param _CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _Creator: Creator
Note: This field may return null, indicating that no valid values can be obtained.
        :type Creator: str
        """
        self._TableId = None
        self._ProjectId = None
        self._Name = None
        self._Description = None
        self._Columns = None
        self._CreateTime = None
        self._Creator = None

    @property
    def TableId(self):
        """Table ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableId

    @TableId.setter
    def TableId(self, TableId):
        self._TableId = TableId

    @property
    def ProjectId(self):
        """Associated project ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Name(self):
        """Table name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Table description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Columns(self):
        """Table column
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of TableColumn
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def CreateTime(self):
        """Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Creator(self):
        """Creator
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator


    def _deserialize(self, params):
        self._TableId = params.get("TableId")
        self._ProjectId = params.get("ProjectId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Columns") is not None:
            self._Columns = []
            for item in params.get("Columns"):
                obj = TableColumn()
                obj._deserialize(item)
                self._Columns.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableColumn(AbstractModel):
    """Table column

    """

    def __init__(self):
        r"""
        :param _Header: Column name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Header: str
        :param _DataType: Column data type
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataType: str
        """
        self._Header = None
        self._DataType = None

    @property
    def Header(self):
        """Column name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def DataType(self):
        """Column data type
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        self._Header = params.get("Header")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TableRow(AbstractModel):
    """Table row

    """

    def __init__(self):
        r"""
        :param _TableRowUuid: Table row UUID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TableRowUuid: str
        :param _Content: Table row content
Note: This field may return null, indicating that no valid values can be obtained.
        :type Content: list of str
        """
        self._TableRowUuid = None
        self._Content = None

    @property
    def TableRowUuid(self):
        """Table row UUID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TableRowUuid

    @TableRowUuid.setter
    def TableRowUuid(self, TableRowUuid):
        self._TableRowUuid = TableRowUuid

    @property
    def Content(self):
        """Table row content
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._TableRowUuid = params.get("TableRowUuid")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateRunGroupRequest(AbstractModel):
    """TerminateRunGroup request structure.

    """

    def __init__(self):
        r"""
        :param _RunGroupId: Run group ID
        :type RunGroupId: str
        :param _ProjectId: Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :type ProjectId: str
        """
        self._RunGroupId = None
        self._ProjectId = None

    @property
    def RunGroupId(self):
        """Run group ID
        :rtype: str
        """
        return self._RunGroupId

    @RunGroupId.setter
    def RunGroupId(self, RunGroupId):
        self._RunGroupId = RunGroupId

    @property
    def ProjectId(self):
        """Project ID
(If you leave it blank, the default item in the specified region will be used.)
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._RunGroupId = params.get("RunGroupId")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateRunGroupResponse(AbstractModel):
    """TerminateRunGroup response structure.

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


class VPCOption(AbstractModel):
    """VPC configuration

    """

    def __init__(self):
        r"""
        :param _VPCId: VPC ID (Either VPCId or VPCCIDRBlock must be selected. If VPCId is selected, the existing VPCs will be used; if VPCCIDRBlock is selected, a new VPC will be created.)
        :type VPCId: str
        :param _SubnetId: Subnet ID (Either SubnetId or SubnetZone&SubnetCIDRBlock must be selected. If SubnetId is selected, the existing subnet will be used; if SubnetZone&SubnetCIDRBlock is selected, a new subnet will be created.)
        :type SubnetId: str
        :param _SubnetZone: Subnet availability zone
        :type SubnetZone: str
        :param _VPCCIDRBlock:  VPC CIDR.
        :type VPCCIDRBlock: str
        :param _SubnetCIDRBlock: Subnet CIDR
        :type SubnetCIDRBlock: str
        """
        self._VPCId = None
        self._SubnetId = None
        self._SubnetZone = None
        self._VPCCIDRBlock = None
        self._SubnetCIDRBlock = None

    @property
    def VPCId(self):
        """VPC ID (Either VPCId or VPCCIDRBlock must be selected. If VPCId is selected, the existing VPCs will be used; if VPCCIDRBlock is selected, a new VPC will be created.)
        :rtype: str
        """
        return self._VPCId

    @VPCId.setter
    def VPCId(self, VPCId):
        self._VPCId = VPCId

    @property
    def SubnetId(self):
        """Subnet ID (Either SubnetId or SubnetZone&SubnetCIDRBlock must be selected. If SubnetId is selected, the existing subnet will be used; if SubnetZone&SubnetCIDRBlock is selected, a new subnet will be created.)
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetZone(self):
        """Subnet availability zone
        :rtype: str
        """
        return self._SubnetZone

    @SubnetZone.setter
    def SubnetZone(self, SubnetZone):
        self._SubnetZone = SubnetZone

    @property
    def VPCCIDRBlock(self):
        """ VPC CIDR.
        :rtype: str
        """
        return self._VPCCIDRBlock

    @VPCCIDRBlock.setter
    def VPCCIDRBlock(self, VPCCIDRBlock):
        self._VPCCIDRBlock = VPCCIDRBlock

    @property
    def SubnetCIDRBlock(self):
        """Subnet CIDR
        :rtype: str
        """
        return self._SubnetCIDRBlock

    @SubnetCIDRBlock.setter
    def SubnetCIDRBlock(self, SubnetCIDRBlock):
        self._SubnetCIDRBlock = SubnetCIDRBlock


    def _deserialize(self, params):
        self._VPCId = params.get("VPCId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetZone = params.get("SubnetZone")
        self._VPCCIDRBlock = params.get("VPCCIDRBlock")
        self._SubnetCIDRBlock = params.get("SubnetCIDRBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Volume(AbstractModel):
    """Volume

    """

    def __init__(self):
        r"""
        :param _VolumeId: Volume ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VolumeId: str
        :param _Name: Name
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Description: Description
Note: This field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _EnvironmentId: Environment ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param _Type: Volume type. Valid values:
* SHARED: Multi-point mount shared storage
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Spec: Volume specifications. Valid values:

- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
Note: This field may return null, indicating that no valid values can be obtained.
        :type Spec: str
        :param _Capacity: Volume size (GB)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Capacity: int
        :param _Usage: Volume usage (Byte)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Usage: int
        :param _BandwidthLimit: Volume throughput upper limit (MiB/s)
Note: This field may return null, indicating that no valid values can be obtained.
        :type BandwidthLimit: float
        :param _DefaultMountPath: Default mount path
Note: This field may return null, indicating that no valid values can be obtained.
        :type DefaultMountPath: str
        :param _IsDefault: Whether it is the default volume.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsDefault: bool
        :param _Status: Status
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        """
        self._VolumeId = None
        self._Name = None
        self._Description = None
        self._EnvironmentId = None
        self._Type = None
        self._Spec = None
        self._Capacity = None
        self._Usage = None
        self._BandwidthLimit = None
        self._DefaultMountPath = None
        self._IsDefault = None
        self._Status = None

    @property
    def VolumeId(self):
        """Volume ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VolumeId

    @VolumeId.setter
    def VolumeId(self, VolumeId):
        self._VolumeId = VolumeId

    @property
    def Name(self):
        """Name
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """Description
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnvironmentId(self):
        """Environment ID
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Type(self):
        """Volume type. Valid values:
* SHARED: Multi-point mount shared storage
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Spec(self):
        """Volume specifications. Valid values:

- SD: standard
- HP: high-performance
- TB: standard Turbo
- TP: high-performance Turbo
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        self._Spec = Spec

    @property
    def Capacity(self):
        """Volume size (GB)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Usage(self):
        """Volume usage (Byte)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def BandwidthLimit(self):
        """Volume throughput upper limit (MiB/s)
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._BandwidthLimit

    @BandwidthLimit.setter
    def BandwidthLimit(self, BandwidthLimit):
        self._BandwidthLimit = BandwidthLimit

    @property
    def DefaultMountPath(self):
        """Default mount path
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DefaultMountPath

    @DefaultMountPath.setter
    def DefaultMountPath(self, DefaultMountPath):
        self._DefaultMountPath = DefaultMountPath

    @property
    def IsDefault(self):
        """Whether it is the default volume.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Status(self):
        """Status
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._VolumeId = params.get("VolumeId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Type = params.get("Type")
        self._Spec = params.get("Spec")
        self._Capacity = params.get("Capacity")
        self._Usage = params.get("Usage")
        self._BandwidthLimit = params.get("BandwidthLimit")
        self._DefaultMountPath = params.get("DefaultMountPath")
        self._IsDefault = params.get("IsDefault")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        