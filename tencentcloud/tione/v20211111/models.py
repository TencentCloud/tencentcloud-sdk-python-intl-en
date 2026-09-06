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


class AuthToken(AbstractModel):
    r"""AuthToken data of an online service.

    """

    def __init__(self):
        r"""
        :param _Base: AuthToken basic information.
        :type Base: :class:`tencentcloud.tione.v20211111.models.AuthTokenBase`
        :param _Limits: AuthToken throttling array.
        :type Limits: list of AuthTokenLimit
        """
        self._Base = None
        self._Limits = None

    @property
    def Base(self):
        r"""AuthToken basic information.
        :rtype: :class:`tencentcloud.tione.v20211111.models.AuthTokenBase`
        """
        return self._Base

    @Base.setter
    def Base(self, Base):
        self._Base = Base

    @property
    def Limits(self):
        r"""AuthToken throttling array.
        :rtype: list of AuthTokenLimit
        """
        return self._Limits

    @Limits.setter
    def Limits(self, Limits):
        self._Limits = Limits


    def _deserialize(self, params):
        if params.get("Base") is not None:
            self._Base = AuthTokenBase()
            self._Base._deserialize(params.get("Base"))
        if params.get("Limits") is not None:
            self._Limits = []
            for item in params.get("Limits"):
                obj = AuthTokenLimit()
                obj._deserialize(item)
                self._Limits.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthTokenBase(AbstractModel):
    r"""AuthToken basic information.

    """

    def __init__(self):
        r"""
        :param _Value: Token value.
        :type Value: str
        :param _Name: Token alias.
        :type Name: str
        :param _Description: Token description.
        :type Description: str
        :param _CreateTime: Token creation time.
        :type CreateTime: str
        :param _Status: Token status.
        :type Status: str
        """
        self._Value = None
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._Status = None

    @property
    def Value(self):
        r"""Token value.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Name(self):
        r"""Token alias.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""Token description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""Token creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        r"""Token status.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Value = params.get("Value")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthTokenLimit(AbstractModel):
    r"""AuthToken throttling information.

    """

    def __init__(self):
        r"""
        :param _Strategy: Frequency limit policy. Valid values: PerMinute (frequency limit per minute) and PerDay (daily frequency limit).
        :type Strategy: str
        :param _Max: Upper limit.
        :type Max: int
        """
        self._Strategy = None
        self._Max = None

    @property
    def Strategy(self):
        r"""Frequency limit policy. Valid values: PerMinute (frequency limit per minute) and PerDay (daily frequency limit).
        :rtype: str
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Max(self):
        r"""Upper limit.
        :rtype: int
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Strategy = params.get("Strategy")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CBSConfig(AbstractModel):
    r"""CBS storage configuration.

    """

    def __init__(self):
        r"""
        :param _VolumeSizeInGB: Storage size.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VolumeSizeInGB: int
        """
        self._VolumeSizeInGB = None

    @property
    def VolumeSizeInGB(self):
        r"""Storage size.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._VolumeSizeInGB

    @VolumeSizeInGB.setter
    def VolumeSizeInGB(self, VolumeSizeInGB):
        self._VolumeSizeInGB = VolumeSizeInGB


    def _deserialize(self, params):
        self._VolumeSizeInGB = params.get("VolumeSizeInGB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSConfig(AbstractModel):
    r"""CFS storage configurations.

    """

    def __init__(self):
        r"""
        :param _Id: CFS instance ID.
        :type Id: str
        :param _Path: Storage path.
        :type Path: str
        :param _MountType: Mounting type of CFS. Valid values: STORAGE and SOURCE, which respectively indicate the storage expansion mode and the data source mode. The default value is STORAGE.Note: This field may return null, indicating that no valid values can be obtained.
        :type MountType: str
        :param _Protocol: Protocol. Valid values: NFS and TURBO.Note: This field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        """
        self._Id = None
        self._Path = None
        self._MountType = None
        self._Protocol = None

    @property
    def Id(self):
        r"""CFS instance ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Path(self):
        r"""Storage path.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def MountType(self):
        r"""Mounting type of CFS. Valid values: STORAGE and SOURCE, which respectively indicate the storage expansion mode and the data source mode. The default value is STORAGE.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MountType

    @MountType.setter
    def MountType(self, MountType):
        self._MountType = MountType

    @property
    def Protocol(self):
        r"""Protocol. Valid values: NFS and TURBO.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Path = params.get("Path")
        self._MountType = params.get("MountType")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSTurbo(AbstractModel):
    r"""Parameters for configuring CFSTurbo.

    """

    def __init__(self):
        r"""
        :param _Id: CFSTurbo instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _Path: CFSTurbo path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        """
        self._Id = None
        self._Path = None

    @property
    def Id(self):
        r"""CFSTurbo instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Path(self):
        r"""CFSTurbo path.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeRepoConfig(AbstractModel):
    r"""Code repository configuration.

    """

    def __init__(self):
        r"""
        :param _Id: Code repository ID.
        :type Id: str
        :param _TargetPath: Target address for the code repository download.
        :type TargetPath: str
        """
        self._Id = None
        self._TargetPath = None

    @property
    def Id(self):
        r"""Code repository ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TargetPath(self):
        r"""Target address for the code repository download.
        :rtype: str
        """
        return self._TargetPath

    @TargetPath.setter
    def TargetPath(self, TargetPath):
        self._TargetPath = TargetPath


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TargetPath = params.get("TargetPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Container(AbstractModel):
    r"""Container information.

    """

    def __init__(self):
        r"""
        :param _Name: Name.Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _ContainerId: id
Note: This field may return null, indicating that no valid values can be obtained.
        :type ContainerId: str
        :param _Image: Image address.Note: This field may return null, indicating that no valid values can be obtained.
        :type Image: str
        :param _Status: Container status.Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: :class:`tencentcloud.tione.v20211111.models.ContainerStatus`
        """
        self._Name = None
        self._ContainerId = None
        self._Image = None
        self._Status = None

    @property
    def Name(self):
        r"""Name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContainerId(self):
        r"""id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ContainerId

    @ContainerId.setter
    def ContainerId(self, ContainerId):
        self._ContainerId = ContainerId

    @property
    def Image(self):
        r"""Image address.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Status(self):
        r"""Container status.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ContainerStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContainerId = params.get("ContainerId")
        self._Image = params.get("Image")
        if params.get("Status") is not None:
            self._Status = ContainerStatus()
            self._Status._deserialize(params.get("Status"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerStatus(AbstractModel):
    r"""Container status.

    """

    def __init__(self):
        r"""
        :param _RestartCount: Number of restarts.Note: This field may return null, indicating that no valid values can be obtained.
        :type RestartCount: int
        :param _State: Status.Note: This field may return null, indicating that no valid values can be obtained.
        :type State: str
        :param _Ready: Whether it is ready.Note: This field may return null, indicating that no valid values can be obtained.
        :type Ready: bool
        :param _Reason: Status reason.Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param _Message: Container error message.Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self._RestartCount = None
        self._State = None
        self._Ready = None
        self._Reason = None
        self._Message = None

    @property
    def RestartCount(self):
        r"""Number of restarts.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RestartCount

    @RestartCount.setter
    def RestartCount(self, RestartCount):
        self._RestartCount = RestartCount

    @property
    def State(self):
        r"""Status.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Ready(self):
        r"""Whether it is ready.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Ready

    @Ready.setter
    def Ready(self, Ready):
        self._Ready = Ready

    @property
    def Reason(self):
        r"""Status reason.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Message(self):
        r"""Container error message.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._RestartCount = params.get("RestartCount")
        self._State = params.get("State")
        self._Ready = params.get("Ready")
        self._Reason = params.get("Reason")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosPathInfo(AbstractModel):
    r"""COS path information.

    """

    def __init__(self):
        r"""
        :param _Bucket: Bucket.Note: This field may return null, indicating that no valid values can be obtained.
        :type Bucket: str
        :param _Region: Region.Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Paths: Path list. Only one path is supported.Note: This field may return null, indicating that no valid values can be obtained.
        :type Paths: list of str
        """
        self._Bucket = None
        self._Region = None
        self._Paths = None

    @property
    def Bucket(self):
        r"""Bucket.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        r"""Region.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Paths(self):
        r"""Path list. Only one path is supported.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        self._Paths = params.get("Paths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingTaskRequest(AbstractModel):
    r"""CreateTrainingTask request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Training task name. The name cannot exceed 60 characters in length, and can contain only Chinese characters, letters, digits, underscores (_), and hyphens (-). It must start with a Chinese character, letter, or digit.
        :type Name: str
        :param _ChargeType: Billing mode. For example, PREPAID indicates yearly/monthly subscription (resource group).
POSTPAID_BY_HOUR indicates pay-as-you-go mode.
        :type ChargeType: str
        :param _ResourceConfigInfos: Resource configuration. Specify the CVM instance specification ID and number of nodes. The API for querying the CVM instance specification ID is DescribeBillingSpecsPrice. For example, [{"Role":"WORKER", "InstanceType": "TI.S.MEDIUM.POST", "InstanceNum": 1}].
        :type ResourceConfigInfos: list of ResourceConfigInfo
        :param _TiProjectId: TI Workspace ID. Used solely for the "Workspace" allowlist feature. To use this feature, please contact a TI administrator to enable allowlisting.
        :type TiProjectId: str
        :param _FrameworkName: Training framework name, which can be queried via the DescribeTrainingFrameworks API. For example, SPARK, PYSPARK, TENSORFLOW, and PYTORCH.
        :type FrameworkName: str
        :param _FrameworkVersion: Training framework version, which can be queried via the DescribeTrainingFrameworks API. For example, 1.15 and 1.9.
        :type FrameworkVersion: str
        :param _FrameworkEnvironment: Training framework environment, which can be queried via the DescribeTrainingFrameworks API. For example, tf1.15-py3.7-cpu and torch1.9-py3.8-cuda11.1-gpu.
        :type FrameworkEnvironment: str
        :param _ResourceGroupId: ID of the prepaid dedicated resource group, which can be queried via the DescribeBillingResourceGroups API.
        :type ResourceGroupId: str
        :param _Tags: Tag configuration.
        :type Tags: list of Tag
        :param _ImageInfo: Custom image information.
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _CodePackagePath: COS code package path.
        :type CodePackagePath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _StartCmdInfo: Task startup command. Specify this parameter based on the task training mode. If the configuration fails due to special characters, use the EncodedStartCmdInfo parameter instead.
        :type StartCmdInfo: :class:`tencentcloud.tione.v20211111.models.StartCmdInfo`
        :param _TrainingMode: Training mode, which can be queried via the DescribeTrainingFrameworks API. For example, PS_WORKER, DDP, MPI, and HOROVOD.
        :type TrainingMode: str
        :param _DataConfigs: Data configurations. This parameter depends on the DataSource field. The maximum number of configurations is 10.
        :type DataConfigs: list of DataConfig
        :param _VpcId: VPC Id
        :type VpcId: str
        :param _SubnetId: Subnet ID.
        :type SubnetId: str
        :param _Output: COS training output path.
        :type Output: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _LogConfig: CLS logging configuration.
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _TuningParameters: Tuning parameters. The value of this parameter cannot exceed 2048 characters in length.
        :type TuningParameters: str
        :param _LogEnable: Indicates whether to report logs.
        :type LogEnable: bool
        :param _Remark: Remarks. The value of this parameter cannot exceed 1024 characters.
        :type Remark: str
        :param _DataSource: Data source. For example, DATASET, COS, CFS, CFSTurbo, HDFS, and GooseFSx.
        :type DataSource: str
        :param _CallbackUrl: Callback URL. This parameter is used for the asynchronous callback to create, start, or stop training tasks. For the callback format and content, see [[TI-ONE API Callback Description]](https://www.tencentcloud.com/document/product/851/84292?from_cn_redirect=1).
        :type CallbackUrl: str
        :param _EncodedStartCmdInfo: Encoded task startup command. If StartCmdInfo is also configured, only this parameter takes effect.
        :type EncodedStartCmdInfo: :class:`tencentcloud.tione.v20211111.models.EncodedStartCmdInfo`
        :param _CodeRepos: Code repository configuration.
        :type CodeRepos: list of CodeRepoConfig
        :param _ExposeNetworkConfig: Network exposure configuration.
        :type ExposeNetworkConfig: :class:`tencentcloud.tione.v20211111.models.ExposeNetworkConfig`
        :param _Envs: Environment Variables.
        :type Envs: list of EnvVar
        :param _TrainToolConfig: Train tool configuration.
        :type TrainToolConfig: :class:`tencentcloud.tione.v20211111.models.TrainToolConfig`
        :param _ResourceSupplyAttribute: Training Diagnostic Tool Configuration.
        :type ResourceSupplyAttribute: :class:`tencentcloud.tione.v20211111.models.ResourceSupplyAttribute`
        :param _Queues: Queue ID.
        :type Queues: list of str
        """
        self._Name = None
        self._ChargeType = None
        self._ResourceConfigInfos = None
        self._TiProjectId = None
        self._FrameworkName = None
        self._FrameworkVersion = None
        self._FrameworkEnvironment = None
        self._ResourceGroupId = None
        self._Tags = None
        self._ImageInfo = None
        self._CodePackagePath = None
        self._StartCmdInfo = None
        self._TrainingMode = None
        self._DataConfigs = None
        self._VpcId = None
        self._SubnetId = None
        self._Output = None
        self._LogConfig = None
        self._TuningParameters = None
        self._LogEnable = None
        self._Remark = None
        self._DataSource = None
        self._CallbackUrl = None
        self._EncodedStartCmdInfo = None
        self._CodeRepos = None
        self._ExposeNetworkConfig = None
        self._Envs = None
        self._TrainToolConfig = None
        self._ResourceSupplyAttribute = None
        self._Queues = None

    @property
    def Name(self):
        r"""Training task name. The name cannot exceed 60 characters in length, and can contain only Chinese characters, letters, digits, underscores (_), and hyphens (-). It must start with a Chinese character, letter, or digit.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ChargeType(self):
        r"""Billing mode. For example, PREPAID indicates yearly/monthly subscription (resource group).
POSTPAID_BY_HOUR indicates pay-as-you-go mode.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceConfigInfos(self):
        r"""Resource configuration. Specify the CVM instance specification ID and number of nodes. The API for querying the CVM instance specification ID is DescribeBillingSpecsPrice. For example, [{"Role":"WORKER", "InstanceType": "TI.S.MEDIUM.POST", "InstanceNum": 1}].
        :rtype: list of ResourceConfigInfo
        """
        return self._ResourceConfigInfos

    @ResourceConfigInfos.setter
    def ResourceConfigInfos(self, ResourceConfigInfos):
        self._ResourceConfigInfos = ResourceConfigInfos

    @property
    def TiProjectId(self):
        r"""TI Workspace ID. Used solely for the "Workspace" allowlist feature. To use this feature, please contact a TI administrator to enable allowlisting.
        :rtype: str
        """
        return self._TiProjectId

    @TiProjectId.setter
    def TiProjectId(self, TiProjectId):
        self._TiProjectId = TiProjectId

    @property
    def FrameworkName(self):
        r"""Training framework name, which can be queried via the DescribeTrainingFrameworks API. For example, SPARK, PYSPARK, TENSORFLOW, and PYTORCH.
        :rtype: str
        """
        return self._FrameworkName

    @FrameworkName.setter
    def FrameworkName(self, FrameworkName):
        self._FrameworkName = FrameworkName

    @property
    def FrameworkVersion(self):
        r"""Training framework version, which can be queried via the DescribeTrainingFrameworks API. For example, 1.15 and 1.9.
        :rtype: str
        """
        return self._FrameworkVersion

    @FrameworkVersion.setter
    def FrameworkVersion(self, FrameworkVersion):
        self._FrameworkVersion = FrameworkVersion

    @property
    def FrameworkEnvironment(self):
        r"""Training framework environment, which can be queried via the DescribeTrainingFrameworks API. For example, tf1.15-py3.7-cpu and torch1.9-py3.8-cuda11.1-gpu.
        :rtype: str
        """
        return self._FrameworkEnvironment

    @FrameworkEnvironment.setter
    def FrameworkEnvironment(self, FrameworkEnvironment):
        self._FrameworkEnvironment = FrameworkEnvironment

    @property
    def ResourceGroupId(self):
        r"""ID of the prepaid dedicated resource group, which can be queried via the DescribeBillingResourceGroups API.
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Tags(self):
        r"""Tag configuration.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ImageInfo(self):
        r"""Custom image information.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        """
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def CodePackagePath(self):
        r"""COS code package path.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        return self._CodePackagePath

    @CodePackagePath.setter
    def CodePackagePath(self, CodePackagePath):
        self._CodePackagePath = CodePackagePath

    @property
    def StartCmdInfo(self):
        r"""Task startup command. Specify this parameter based on the task training mode. If the configuration fails due to special characters, use the EncodedStartCmdInfo parameter instead.
        :rtype: :class:`tencentcloud.tione.v20211111.models.StartCmdInfo`
        """
        return self._StartCmdInfo

    @StartCmdInfo.setter
    def StartCmdInfo(self, StartCmdInfo):
        self._StartCmdInfo = StartCmdInfo

    @property
    def TrainingMode(self):
        r"""Training mode, which can be queried via the DescribeTrainingFrameworks API. For example, PS_WORKER, DDP, MPI, and HOROVOD.
        :rtype: str
        """
        return self._TrainingMode

    @TrainingMode.setter
    def TrainingMode(self, TrainingMode):
        self._TrainingMode = TrainingMode

    @property
    def DataConfigs(self):
        r"""Data configurations. This parameter depends on the DataSource field. The maximum number of configurations is 10.
        :rtype: list of DataConfig
        """
        return self._DataConfigs

    @DataConfigs.setter
    def DataConfigs(self, DataConfigs):
        self._DataConfigs = DataConfigs

    @property
    def VpcId(self):
        r"""VPC Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""Subnet ID.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Output(self):
        r"""COS training output path.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def LogConfig(self):
        r"""CLS logging configuration.
        :rtype: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        """
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def TuningParameters(self):
        r"""Tuning parameters. The value of this parameter cannot exceed 2048 characters in length.
        :rtype: str
        """
        return self._TuningParameters

    @TuningParameters.setter
    def TuningParameters(self, TuningParameters):
        self._TuningParameters = TuningParameters

    @property
    def LogEnable(self):
        r"""Indicates whether to report logs.
        :rtype: bool
        """
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def Remark(self):
        r"""Remarks. The value of this parameter cannot exceed 1024 characters.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DataSource(self):
        r"""Data source. For example, DATASET, COS, CFS, CFSTurbo, HDFS, and GooseFSx.
        :rtype: str
        """
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def CallbackUrl(self):
        r"""Callback URL. This parameter is used for the asynchronous callback to create, start, or stop training tasks. For the callback format and content, see [[TI-ONE API Callback Description]](https://www.tencentcloud.com/document/product/851/84292?from_cn_redirect=1).
        :rtype: str
        """
        return self._CallbackUrl

    @CallbackUrl.setter
    def CallbackUrl(self, CallbackUrl):
        self._CallbackUrl = CallbackUrl

    @property
    def EncodedStartCmdInfo(self):
        r"""Encoded task startup command. If StartCmdInfo is also configured, only this parameter takes effect.
        :rtype: :class:`tencentcloud.tione.v20211111.models.EncodedStartCmdInfo`
        """
        return self._EncodedStartCmdInfo

    @EncodedStartCmdInfo.setter
    def EncodedStartCmdInfo(self, EncodedStartCmdInfo):
        self._EncodedStartCmdInfo = EncodedStartCmdInfo

    @property
    def CodeRepos(self):
        r"""Code repository configuration.
        :rtype: list of CodeRepoConfig
        """
        return self._CodeRepos

    @CodeRepos.setter
    def CodeRepos(self, CodeRepos):
        self._CodeRepos = CodeRepos

    @property
    def ExposeNetworkConfig(self):
        r"""Network exposure configuration.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ExposeNetworkConfig`
        """
        return self._ExposeNetworkConfig

    @ExposeNetworkConfig.setter
    def ExposeNetworkConfig(self, ExposeNetworkConfig):
        self._ExposeNetworkConfig = ExposeNetworkConfig

    @property
    def Envs(self):
        r"""Environment Variables.
        :rtype: list of EnvVar
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def TrainToolConfig(self):
        r"""Train tool configuration.
        :rtype: :class:`tencentcloud.tione.v20211111.models.TrainToolConfig`
        """
        return self._TrainToolConfig

    @TrainToolConfig.setter
    def TrainToolConfig(self, TrainToolConfig):
        self._TrainToolConfig = TrainToolConfig

    @property
    def ResourceSupplyAttribute(self):
        r"""Training Diagnostic Tool Configuration.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ResourceSupplyAttribute`
        """
        return self._ResourceSupplyAttribute

    @ResourceSupplyAttribute.setter
    def ResourceSupplyAttribute(self, ResourceSupplyAttribute):
        self._ResourceSupplyAttribute = ResourceSupplyAttribute

    @property
    def Queues(self):
        r"""Queue ID.
        :rtype: list of str
        """
        return self._Queues

    @Queues.setter
    def Queues(self, Queues):
        self._Queues = Queues


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ChargeType = params.get("ChargeType")
        if params.get("ResourceConfigInfos") is not None:
            self._ResourceConfigInfos = []
            for item in params.get("ResourceConfigInfos"):
                obj = ResourceConfigInfo()
                obj._deserialize(item)
                self._ResourceConfigInfos.append(obj)
        self._TiProjectId = params.get("TiProjectId")
        self._FrameworkName = params.get("FrameworkName")
        self._FrameworkVersion = params.get("FrameworkVersion")
        self._FrameworkEnvironment = params.get("FrameworkEnvironment")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("CodePackagePath") is not None:
            self._CodePackagePath = CosPathInfo()
            self._CodePackagePath._deserialize(params.get("CodePackagePath"))
        if params.get("StartCmdInfo") is not None:
            self._StartCmdInfo = StartCmdInfo()
            self._StartCmdInfo._deserialize(params.get("StartCmdInfo"))
        self._TrainingMode = params.get("TrainingMode")
        if params.get("DataConfigs") is not None:
            self._DataConfigs = []
            for item in params.get("DataConfigs"):
                obj = DataConfig()
                obj._deserialize(item)
                self._DataConfigs.append(obj)
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("Output") is not None:
            self._Output = CosPathInfo()
            self._Output._deserialize(params.get("Output"))
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._TuningParameters = params.get("TuningParameters")
        self._LogEnable = params.get("LogEnable")
        self._Remark = params.get("Remark")
        self._DataSource = params.get("DataSource")
        self._CallbackUrl = params.get("CallbackUrl")
        if params.get("EncodedStartCmdInfo") is not None:
            self._EncodedStartCmdInfo = EncodedStartCmdInfo()
            self._EncodedStartCmdInfo._deserialize(params.get("EncodedStartCmdInfo"))
        if params.get("CodeRepos") is not None:
            self._CodeRepos = []
            for item in params.get("CodeRepos"):
                obj = CodeRepoConfig()
                obj._deserialize(item)
                self._CodeRepos.append(obj)
        if params.get("ExposeNetworkConfig") is not None:
            self._ExposeNetworkConfig = ExposeNetworkConfig()
            self._ExposeNetworkConfig._deserialize(params.get("ExposeNetworkConfig"))
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = EnvVar()
                obj._deserialize(item)
                self._Envs.append(obj)
        if params.get("TrainToolConfig") is not None:
            self._TrainToolConfig = TrainToolConfig()
            self._TrainToolConfig._deserialize(params.get("TrainToolConfig"))
        if params.get("ResourceSupplyAttribute") is not None:
            self._ResourceSupplyAttribute = ResourceSupplyAttribute()
            self._ResourceSupplyAttribute._deserialize(params.get("ResourceSupplyAttribute"))
        self._Queues = params.get("Queues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTrainingTaskResponse(AbstractModel):
    r"""CreateTrainingTask response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Training task ID.
        :type Id: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""Training task ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CronScaleJob(AbstractModel):
    r"""Scheduled scaling task.

    """

    def __init__(self):
        r"""
        :param _Schedule: Cron expression, which identifies the task execution time, and is accurate to minutes.
        :type Schedule: str
        :param _Name: Scheduled task name.Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _TargetReplicas: Number of target instances.Note: This field may return null, indicating that no valid values can be obtained.
        :type TargetReplicas: int
        :param _MinReplicas: Minimum target.Note: This field may return null, indicating that no valid values can be obtained.
        :type MinReplicas: int
        :param _MaxReplicas: Maximum target.Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxReplicas: int
        :param _ExcludeDates: Exception periods, defined by Cron expressions, during which tasks are not executed. Up to 3 Cron expressions are supported.Note: This field may return null, indicating that no valid values can be obtained.
        :type ExcludeDates: list of str
        """
        self._Schedule = None
        self._Name = None
        self._TargetReplicas = None
        self._MinReplicas = None
        self._MaxReplicas = None
        self._ExcludeDates = None

    @property
    def Schedule(self):
        r"""Cron expression, which identifies the task execution time, and is accurate to minutes.
        :rtype: str
        """
        return self._Schedule

    @Schedule.setter
    def Schedule(self, Schedule):
        self._Schedule = Schedule

    @property
    def Name(self):
        r"""Scheduled task name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TargetReplicas(self):
        r"""Number of target instances.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TargetReplicas

    @TargetReplicas.setter
    def TargetReplicas(self, TargetReplicas):
        self._TargetReplicas = TargetReplicas

    @property
    def MinReplicas(self):
        r"""Minimum target.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        r"""Maximum target.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def ExcludeDates(self):
        r"""Exception periods, defined by Cron expressions, during which tasks are not executed. Up to 3 Cron expressions are supported.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._ExcludeDates

    @ExcludeDates.setter
    def ExcludeDates(self, ExcludeDates):
        self._ExcludeDates = ExcludeDates


    def _deserialize(self, params):
        self._Schedule = params.get("Schedule")
        self._Name = params.get("Name")
        self._TargetReplicas = params.get("TargetReplicas")
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._ExcludeDates = params.get("ExcludeDates")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CrossTenantENIInfo(AbstractModel):
    r"""Information about Pod calls involving ENIs across tenants.

    """

    def __init__(self):
        r"""
        :param _PrimaryIP: Pod IP address.Note: This field may return null, indicating that no valid values can be obtained.
        :type PrimaryIP: str
        :param _Port: Pod port.Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: str
        """
        self._PrimaryIP = None
        self._Port = None

    @property
    def PrimaryIP(self):
        r"""Pod IP address.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrimaryIP

    @PrimaryIP.setter
    def PrimaryIP(self, PrimaryIP):
        self._PrimaryIP = PrimaryIP

    @property
    def Port(self):
        r"""Pod port.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._PrimaryIP = params.get("PrimaryIP")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataConfig(AbstractModel):
    r"""Data configuration.

    """

    def __init__(self):
        r"""
        :param _MappingPath: Mapping path.
        :type MappingPath: str
        :param _DataSourceUsage: Storage purpose.
Valid values: BUILTIN_CODE, BUILTIN_DATA, BUILTIN_MODEL, USER_DATA, USER_CODE, USER_MODEL, OUTPUT, and OTHER.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataSourceUsage: str
        :param _DataSourceType: DATASET, COS, CFS, CFSTurbo, GooseFSx, HDFS, and WEDATA_HDFS
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataSourceType: str
        :param _DataSetSource: Data from the data set.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DataSetSource: :class:`tencentcloud.tione.v20211111.models.DataSetConfig`
        :param _COSSource: Data from COS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type COSSource: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _CFSSource: Data from CFS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFSSource: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _HDFSSource: Data from HDFS.
Note: This field may return null, indicating that no valid values can be obtained.
        :type HDFSSource: :class:`tencentcloud.tione.v20211111.models.HDFSConfig`
        :param _GooseFSSource: GooseFS data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GooseFSSource: :class:`tencentcloud.tione.v20211111.models.GooseFS`
        :param _CFSTurboSource: TurboFS data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CFSTurboSource: :class:`tencentcloud.tione.v20211111.models.CFSTurbo`
        :param _LocalDiskSource: Information from local disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocalDiskSource: :class:`tencentcloud.tione.v20211111.models.LocalDisk`
        :param _CBSSource: CBS configuration information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CBSSource: :class:`tencentcloud.tione.v20211111.models.CBSConfig`
        :param _HostPathSource: Host path information.
        :type HostPathSource: :class:`tencentcloud.tione.v20211111.models.HostPath`
        :param _PublicDataSource: 
        :type PublicDataSource: :class:`tencentcloud.tione.v20211111.models.PublicDataSourceFS`
        """
        self._MappingPath = None
        self._DataSourceUsage = None
        self._DataSourceType = None
        self._DataSetSource = None
        self._COSSource = None
        self._CFSSource = None
        self._HDFSSource = None
        self._GooseFSSource = None
        self._CFSTurboSource = None
        self._LocalDiskSource = None
        self._CBSSource = None
        self._HostPathSource = None
        self._PublicDataSource = None

    @property
    def MappingPath(self):
        r"""Mapping path.
        :rtype: str
        """
        return self._MappingPath

    @MappingPath.setter
    def MappingPath(self, MappingPath):
        self._MappingPath = MappingPath

    @property
    def DataSourceUsage(self):
        r"""Storage purpose.
Valid values: BUILTIN_CODE, BUILTIN_DATA, BUILTIN_MODEL, USER_DATA, USER_CODE, USER_MODEL, OUTPUT, and OTHER.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataSourceUsage

    @DataSourceUsage.setter
    def DataSourceUsage(self, DataSourceUsage):
        self._DataSourceUsage = DataSourceUsage

    @property
    def DataSourceType(self):
        r"""DATASET, COS, CFS, CFSTurbo, GooseFSx, HDFS, and WEDATA_HDFS
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def DataSetSource(self):
        r"""Data from the data set.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.DataSetConfig`
        """
        return self._DataSetSource

    @DataSetSource.setter
    def DataSetSource(self, DataSetSource):
        self._DataSetSource = DataSetSource

    @property
    def COSSource(self):
        r"""Data from COS.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        return self._COSSource

    @COSSource.setter
    def COSSource(self, COSSource):
        self._COSSource = COSSource

    @property
    def CFSSource(self):
        r"""Data from CFS.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        """
        return self._CFSSource

    @CFSSource.setter
    def CFSSource(self, CFSSource):
        self._CFSSource = CFSSource

    @property
    def HDFSSource(self):
        r"""Data from HDFS.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.HDFSConfig`
        """
        return self._HDFSSource

    @HDFSSource.setter
    def HDFSSource(self, HDFSSource):
        self._HDFSSource = HDFSSource

    @property
    def GooseFSSource(self):
        r"""GooseFS data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.GooseFS`
        """
        return self._GooseFSSource

    @GooseFSSource.setter
    def GooseFSSource(self, GooseFSSource):
        self._GooseFSSource = GooseFSSource

    @property
    def CFSTurboSource(self):
        r"""TurboFS data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CFSTurbo`
        """
        return self._CFSTurboSource

    @CFSTurboSource.setter
    def CFSTurboSource(self, CFSTurboSource):
        self._CFSTurboSource = CFSTurboSource

    @property
    def LocalDiskSource(self):
        r"""Information from local disks.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.LocalDisk`
        """
        return self._LocalDiskSource

    @LocalDiskSource.setter
    def LocalDiskSource(self, LocalDiskSource):
        self._LocalDiskSource = LocalDiskSource

    @property
    def CBSSource(self):
        r"""CBS configuration information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CBSConfig`
        """
        return self._CBSSource

    @CBSSource.setter
    def CBSSource(self, CBSSource):
        self._CBSSource = CBSSource

    @property
    def HostPathSource(self):
        r"""Host path information.
        :rtype: :class:`tencentcloud.tione.v20211111.models.HostPath`
        """
        return self._HostPathSource

    @HostPathSource.setter
    def HostPathSource(self, HostPathSource):
        self._HostPathSource = HostPathSource

    @property
    def PublicDataSource(self):
        r"""
        :rtype: :class:`tencentcloud.tione.v20211111.models.PublicDataSourceFS`
        """
        return self._PublicDataSource

    @PublicDataSource.setter
    def PublicDataSource(self, PublicDataSource):
        self._PublicDataSource = PublicDataSource


    def _deserialize(self, params):
        self._MappingPath = params.get("MappingPath")
        self._DataSourceUsage = params.get("DataSourceUsage")
        self._DataSourceType = params.get("DataSourceType")
        if params.get("DataSetSource") is not None:
            self._DataSetSource = DataSetConfig()
            self._DataSetSource._deserialize(params.get("DataSetSource"))
        if params.get("COSSource") is not None:
            self._COSSource = CosPathInfo()
            self._COSSource._deserialize(params.get("COSSource"))
        if params.get("CFSSource") is not None:
            self._CFSSource = CFSConfig()
            self._CFSSource._deserialize(params.get("CFSSource"))
        if params.get("HDFSSource") is not None:
            self._HDFSSource = HDFSConfig()
            self._HDFSSource._deserialize(params.get("HDFSSource"))
        if params.get("GooseFSSource") is not None:
            self._GooseFSSource = GooseFS()
            self._GooseFSSource._deserialize(params.get("GooseFSSource"))
        if params.get("CFSTurboSource") is not None:
            self._CFSTurboSource = CFSTurbo()
            self._CFSTurboSource._deserialize(params.get("CFSTurboSource"))
        if params.get("LocalDiskSource") is not None:
            self._LocalDiskSource = LocalDisk()
            self._LocalDiskSource._deserialize(params.get("LocalDiskSource"))
        if params.get("CBSSource") is not None:
            self._CBSSource = CBSConfig()
            self._CBSSource._deserialize(params.get("CBSSource"))
        if params.get("HostPathSource") is not None:
            self._HostPathSource = HostPath()
            self._HostPathSource._deserialize(params.get("HostPathSource"))
        if params.get("PublicDataSource") is not None:
            self._PublicDataSource = PublicDataSourceFS()
            self._PublicDataSource._deserialize(params.get("PublicDataSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSetConfig(AbstractModel):
    r"""Data set structure.

    """

    def __init__(self):
        r"""
        :param _Id: Data set ID.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        r"""Data set ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceGroupsRequest(AbstractModel):
    r"""DescribeModelServiceGroups request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of returned results. The default value is 20, and the maximum value is 100.
        :type Limit: int
        :param _Order: The sorting order of the output list. Valid values: ASC (ascending order) and DESC (descending order).
        :type Order: str
        :param _OrderField: Field to sort by. Valid values: CreateTime and UpdateTime.
        :type OrderField: str
        :param _Filters: Pagination parameters. Supported filterable field names include:["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId","Status","CreatedBy","ModelVersionId"]
        :type Filters: list of Filter
        :param _TagFilters: Tag filtering parameters.
        :type TagFilters: list of TagFilter
        :param _ServiceCategory: Service classification.
        :type ServiceCategory: str
        """
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._Filters = None
        self._TagFilters = None
        self._ServiceCategory = None

    @property
    def Offset(self):
        r"""Offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""Number of returned results. The default value is 20, and the maximum value is 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""The sorting order of the output list. Valid values: ASC (ascending order) and DESC (descending order).
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        r"""Field to sort by. Valid values: CreateTime and UpdateTime.
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Filters(self):
        r"""Pagination parameters. Supported filterable field names include:["ClusterId", "ServiceId", "ServiceGroupName", "ServiceGroupId","Status","CreatedBy","ModelVersionId"]
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagFilters(self):
        r"""Tag filtering parameters.
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def ServiceCategory(self):
        warnings.warn("parameter `ServiceCategory` is deprecated", DeprecationWarning) 

        r"""Service classification.
        :rtype: str
        """
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
        warnings.warn("parameter `ServiceCategory` is deprecated", DeprecationWarning) 

        self._ServiceCategory = ServiceCategory


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._ServiceCategory = params.get("ServiceCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelServiceGroupsResponse(AbstractModel):
    r"""DescribeModelServiceGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of inference service groups.Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _ServiceGroups: Service group information.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceGroups: list of ServiceGroup
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ServiceGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""Number of inference service groups.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceGroups(self):
        r"""Service group information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ServiceGroup
        """
        return self._ServiceGroups

    @ServiceGroups.setter
    def ServiceGroups(self, ServiceGroups):
        self._ServiceGroups = ServiceGroups

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
        if params.get("ServiceGroups") is not None:
            self._ServiceGroups = []
            for item in params.get("ServiceGroups"):
                obj = ServiceGroup()
                obj._deserialize(item)
                self._ServiceGroups.append(obj)
        self._RequestId = params.get("RequestId")


class EncodedStartCmdInfo(AbstractModel):
    r"""Encoded startup command information.

    """

    def __init__(self):
        r"""
        :param _StartCmdInfo: Startup command of the task, which is input in base64 format. Note that the complete input of {"StartCmd":"","PsStartCmd":"","WorkerStartCmd":""} is required for conversion.
        :type StartCmdInfo: str
        """
        self._StartCmdInfo = None

    @property
    def StartCmdInfo(self):
        r"""Startup command of the task, which is input in base64 format. Note that the complete input of {"StartCmd":"","PsStartCmd":"","WorkerStartCmd":""} is required for conversion.
        :rtype: str
        """
        return self._StartCmdInfo

    @StartCmdInfo.setter
    def StartCmdInfo(self, StartCmdInfo):
        self._StartCmdInfo = StartCmdInfo


    def _deserialize(self, params):
        self._StartCmdInfo = params.get("StartCmdInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvVar(AbstractModel):
    r"""Environment variables.

    """

    def __init__(self):
        r"""
        :param _Name: Environment variable key.Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Value: Environment variable value.Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""Environment variable key.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""Environment variable value.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        


class ExecAction(AbstractModel):
    r"""Probe check action for execution commands.

    """

    def __init__(self):
        r"""
        :param _Command: Execution command list.
        :type Command: list of str
        """
        self._Command = None

    @property
    def Command(self):
        r"""Execution command list.
        :rtype: list of str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command


    def _deserialize(self, params):
        self._Command = params.get("Command")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExposeNetworkConfig(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _SSHConfig: 
        :type SSHConfig: :class:`tencentcloud.tione.v20211111.models.SSHConfig`
        :param _ExposePortConfig: 
        :type ExposePortConfig: :class:`tencentcloud.tione.v20211111.models.ExposePortConfig`
        """
        self._SSHConfig = None
        self._ExposePortConfig = None

    @property
    def SSHConfig(self):
        r"""
        :rtype: :class:`tencentcloud.tione.v20211111.models.SSHConfig`
        """
        return self._SSHConfig

    @SSHConfig.setter
    def SSHConfig(self, SSHConfig):
        self._SSHConfig = SSHConfig

    @property
    def ExposePortConfig(self):
        r"""
        :rtype: :class:`tencentcloud.tione.v20211111.models.ExposePortConfig`
        """
        return self._ExposePortConfig

    @ExposePortConfig.setter
    def ExposePortConfig(self, ExposePortConfig):
        self._ExposePortConfig = ExposePortConfig


    def _deserialize(self, params):
        if params.get("SSHConfig") is not None:
            self._SSHConfig = SSHConfig()
            self._SSHConfig._deserialize(params.get("SSHConfig"))
        if params.get("ExposePortConfig") is not None:
            self._ExposePortConfig = ExposePortConfig()
            self._ExposePortConfig._deserialize(params.get("ExposePortConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExposePortConfig(AbstractModel):
    r"""Exposed port information.

    """

    def __init__(self):
        r"""
        :param _Enable: 
        :type Enable: bool
        :param _VpcId: 
        :type VpcId: str
        :param _ClbId: 
        :type ClbId: str
        :param _ClbHost: 
        :type ClbHost: str
        """
        self._Enable = None
        self._VpcId = None
        self._ClbId = None
        self._ClbHost = None

    @property
    def Enable(self):
        r"""
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def VpcId(self):
        r"""
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ClbId(self):
        r"""
        :rtype: str
        """
        return self._ClbId

    @ClbId.setter
    def ClbId(self, ClbId):
        self._ClbId = ClbId

    @property
    def ClbHost(self):
        r"""
        :rtype: str
        """
        return self._ClbHost

    @ClbHost.setter
    def ClbHost(self, ClbHost):
        self._ClbHost = ClbHost


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._VpcId = params.get("VpcId")
        self._ClbId = params.get("ClbId")
        self._ClbHost = params.get("ClbHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""Filter.

    """

    def __init__(self):
        r"""
        :param _Name: Filter field name.
        :type Name: str
        :param _Values: Filter field values.
        :type Values: list of str
        :param _Negative: Whether to enable reverse query.
        :type Negative: bool
        :param _Fuzzy: Whether to enable fuzzy matching.
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Negative = None
        self._Fuzzy = None

    @property
    def Name(self):
        r"""Filter field name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""Filter field values.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Negative(self):
        r"""Whether to enable reverse query.
        :rtype: bool
        """
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative

    @property
    def Fuzzy(self):
        r"""Whether to enable fuzzy matching.
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Negative = params.get("Negative")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFS(AbstractModel):
    r"""GooseFS configuration parameters.

    """

    def __init__(self):
        r"""
        :param _Id: GooseFS instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Id: str
        :param _Type: GooseFS type, including GooseFS and GooseFSx.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _Path: Path to mount the GooseFSx instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Path: str
        :param _NameSpace: GooseFS namespace.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NameSpace: str
        """
        self._Id = None
        self._Type = None
        self._Path = None
        self._NameSpace = None

    @property
    def Id(self):
        r"""GooseFS instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        r"""GooseFS type, including GooseFS and GooseFSx.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Path(self):
        r"""Path to mount the GooseFSx instance.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def NameSpace(self):
        r"""GooseFS namespace.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Path = params.get("Path")
        self._NameSpace = params.get("NameSpace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFSx(AbstractModel):
    r"""GooseFSx configurations.

    """

    def __init__(self):
        r"""
        :param _Id: GooseFSx instance ID.
        :type Id: str
        :param _Path: Path to mount the GooseFSx instance.
        :type Path: str
        """
        self._Id = None
        self._Path = None

    @property
    def Id(self):
        r"""GooseFSx instance ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Path(self):
        r"""Path to mount the GooseFSx instance.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GpuDetail(AbstractModel):
    r"""GPU details.

    """

    def __init__(self):
        r"""
        :param _Name: GPU card type. Enumeration values: V100, A100, T4.Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Value: GPU card quantity, in 1/100 cards. For example, 100 represents 1 card.Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: int
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""GPU card type. Enumeration values: V100, A100, T4.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""GPU card quantity, in 1/100 cards. For example, 100 represents 1 card.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
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
        


class HDFSConfig(AbstractModel):
    r"""HDFS parameter configuration.

    """

    def __init__(self):
        r"""
        :param _Id: Cluster instance ID, such as emr-xxxxxxxx.
        :type Id: str
        :param _Path: Path.
        :type Path: str
        """
        self._Id = None
        self._Path = None

    @property
    def Id(self):
        r"""Cluster instance ID, such as emr-xxxxxxxx.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Path(self):
        r"""Path.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPGetAction(AbstractModel):
    r"""HTTP GET action.

    """

    def __init__(self):
        r"""
        :param _Path: HTTP path.
        :type Path: str
        :param _Port: Called port.
        :type Port: int
        """
        self._Path = None
        self._Port = None

    @property
    def Path(self):
        r"""HTTP path.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Port(self):
        r"""Called port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthProbe(AbstractModel):
    r"""Health probe.

    """

    def __init__(self):
        r"""
        :param _LivenessProbe: Liveness probe.
        :type LivenessProbe: :class:`tencentcloud.tione.v20211111.models.Probe`
        :param _ReadinessProbe: Readiness probe.
        :type ReadinessProbe: :class:`tencentcloud.tione.v20211111.models.Probe`
        :param _StartupProbe: Startup probe.
        :type StartupProbe: :class:`tencentcloud.tione.v20211111.models.Probe`
        """
        self._LivenessProbe = None
        self._ReadinessProbe = None
        self._StartupProbe = None

    @property
    def LivenessProbe(self):
        r"""Liveness probe.
        :rtype: :class:`tencentcloud.tione.v20211111.models.Probe`
        """
        return self._LivenessProbe

    @LivenessProbe.setter
    def LivenessProbe(self, LivenessProbe):
        self._LivenessProbe = LivenessProbe

    @property
    def ReadinessProbe(self):
        r"""Readiness probe.
        :rtype: :class:`tencentcloud.tione.v20211111.models.Probe`
        """
        return self._ReadinessProbe

    @ReadinessProbe.setter
    def ReadinessProbe(self, ReadinessProbe):
        self._ReadinessProbe = ReadinessProbe

    @property
    def StartupProbe(self):
        r"""Startup probe.
        :rtype: :class:`tencentcloud.tione.v20211111.models.Probe`
        """
        return self._StartupProbe

    @StartupProbe.setter
    def StartupProbe(self, StartupProbe):
        self._StartupProbe = StartupProbe


    def _deserialize(self, params):
        if params.get("LivenessProbe") is not None:
            self._LivenessProbe = Probe()
            self._LivenessProbe._deserialize(params.get("LivenessProbe"))
        if params.get("ReadinessProbe") is not None:
            self._ReadinessProbe = Probe()
            self._ReadinessProbe._deserialize(params.get("ReadinessProbe"))
        if params.get("StartupProbe") is not None:
            self._StartupProbe = Probe()
            self._StartupProbe._deserialize(params.get("StartupProbe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalPodAutoscaler(AbstractModel):
    r"""HPA description.

    """

    def __init__(self):
        r"""
        :param _MinReplicas: Minimum number of instances.Note: This field may return null, indicating that no valid values can be obtained.
        :type MinReplicas: int
        :param _MaxReplicas: Maximum number of instances.Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxReplicas: int
        :param _HpaMetrics: Supported."gpu-util": GPU utilization; value range: 10-100. "cpu-util": CPU utilization; value range: 10-100. "memory-util": memory utilization; value range: 10-100. "service-qps": the QPS value of single instances; value range: 1-5000."concurrency-util": the number of concurrent requests of single instances. Value range: 1-100000.Note: This field may return null, indicating that no valid values can be obtained.
        :type HpaMetrics: list of Option
        :param _ScaleUpStabilizationWindowSeconds: Scale-out cooldown period, in seconds.
        :type ScaleUpStabilizationWindowSeconds: int
        :param _ScaleDownStabilizationWindowSeconds: Scale-in cooldown period, in seconds.
        :type ScaleDownStabilizationWindowSeconds: int
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._HpaMetrics = None
        self._ScaleUpStabilizationWindowSeconds = None
        self._ScaleDownStabilizationWindowSeconds = None

    @property
    def MinReplicas(self):
        r"""Minimum number of instances.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        r"""Maximum number of instances.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def HpaMetrics(self):
        r"""Supported."gpu-util": GPU utilization; value range: 10-100. "cpu-util": CPU utilization; value range: 10-100. "memory-util": memory utilization; value range: 10-100. "service-qps": the QPS value of single instances; value range: 1-5000."concurrency-util": the number of concurrent requests of single instances. Value range: 1-100000.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Option
        """
        return self._HpaMetrics

    @HpaMetrics.setter
    def HpaMetrics(self, HpaMetrics):
        self._HpaMetrics = HpaMetrics

    @property
    def ScaleUpStabilizationWindowSeconds(self):
        r"""Scale-out cooldown period, in seconds.
        :rtype: int
        """
        return self._ScaleUpStabilizationWindowSeconds

    @ScaleUpStabilizationWindowSeconds.setter
    def ScaleUpStabilizationWindowSeconds(self, ScaleUpStabilizationWindowSeconds):
        self._ScaleUpStabilizationWindowSeconds = ScaleUpStabilizationWindowSeconds

    @property
    def ScaleDownStabilizationWindowSeconds(self):
        r"""Scale-in cooldown period, in seconds.
        :rtype: int
        """
        return self._ScaleDownStabilizationWindowSeconds

    @ScaleDownStabilizationWindowSeconds.setter
    def ScaleDownStabilizationWindowSeconds(self, ScaleDownStabilizationWindowSeconds):
        self._ScaleDownStabilizationWindowSeconds = ScaleDownStabilizationWindowSeconds


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("HpaMetrics") is not None:
            self._HpaMetrics = []
            for item in params.get("HpaMetrics"):
                obj = Option()
                obj._deserialize(item)
                self._HpaMetrics.append(obj)
        self._ScaleUpStabilizationWindowSeconds = params.get("ScaleUpStabilizationWindowSeconds")
        self._ScaleDownStabilizationWindowSeconds = params.get("ScaleDownStabilizationWindowSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostPath(AbstractModel):
    r"""Host path mounting configuration.

    """

    def __init__(self):
        r"""
        :param _Path: Host path to be mounted.
        :type Path: str
        """
        self._Path = None

    @property
    def Path(self):
        r"""Host path to be mounted.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    r"""Image description information.

    """

    def __init__(self):
        r"""
        :param _ImageType: Image type. Valid values: TCR ( which indicates a Tencent Container Registry (TCR) image), CCR (which indicates a TCR Personal Edition image), PreSet (which indicates a platform preset image), and CUSTOM (which indicates a third-party custom image).
        :type ImageType: str
        :param _ImageUrl: Image address.
        :type ImageUrl: str
        :param _RegistryRegion: Region corresponding to the TCR image.Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistryRegion: str
        :param _RegistryId: Instance ID corresponding to the TCR image.Note: This field may return null, indicating that no valid values can be obtained.
        :type RegistryId: str
        :param _AllowSaveAllContent: Whether to allow exporting all content.Note: This field may return null, indicating that no valid values can be obtained.
        :type AllowSaveAllContent: bool
        :param _ImageName: Image name.Note: This field may return null, indicating that no valid values can be obtained.
        :type ImageName: str
        :param _SupportDataPipeline: Whether to support data generation.Note: This field may return null, indicating that no valid values can be obtained.
        :type SupportDataPipeline: bool
        :param _ImageSecret: 
        :type ImageSecret: :class:`tencentcloud.tione.v20211111.models.ImageSecret`
        """
        self._ImageType = None
        self._ImageUrl = None
        self._RegistryRegion = None
        self._RegistryId = None
        self._AllowSaveAllContent = None
        self._ImageName = None
        self._SupportDataPipeline = None
        self._ImageSecret = None

    @property
    def ImageType(self):
        r"""Image type. Valid values: TCR ( which indicates a Tencent Container Registry (TCR) image), CCR (which indicates a TCR Personal Edition image), PreSet (which indicates a platform preset image), and CUSTOM (which indicates a third-party custom image).
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageUrl(self):
        r"""Image address.
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def RegistryRegion(self):
        r"""Region corresponding to the TCR image.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegistryRegion

    @RegistryRegion.setter
    def RegistryRegion(self, RegistryRegion):
        self._RegistryRegion = RegistryRegion

    @property
    def RegistryId(self):
        r"""Instance ID corresponding to the TCR image.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def AllowSaveAllContent(self):
        r"""Whether to allow exporting all content.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._AllowSaveAllContent

    @AllowSaveAllContent.setter
    def AllowSaveAllContent(self, AllowSaveAllContent):
        self._AllowSaveAllContent = AllowSaveAllContent

    @property
    def ImageName(self):
        r"""Image name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def SupportDataPipeline(self):
        r"""Whether to support data generation.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._SupportDataPipeline

    @SupportDataPipeline.setter
    def SupportDataPipeline(self, SupportDataPipeline):
        self._SupportDataPipeline = SupportDataPipeline

    @property
    def ImageSecret(self):
        r"""
        :rtype: :class:`tencentcloud.tione.v20211111.models.ImageSecret`
        """
        return self._ImageSecret

    @ImageSecret.setter
    def ImageSecret(self, ImageSecret):
        self._ImageSecret = ImageSecret


    def _deserialize(self, params):
        self._ImageType = params.get("ImageType")
        self._ImageUrl = params.get("ImageUrl")
        self._RegistryRegion = params.get("RegistryRegion")
        self._RegistryId = params.get("RegistryId")
        self._AllowSaveAllContent = params.get("AllowSaveAllContent")
        self._ImageName = params.get("ImageName")
        self._SupportDataPipeline = params.get("SupportDataPipeline")
        if params.get("ImageSecret") is not None:
            self._ImageSecret = ImageSecret()
            self._ImageSecret._deserialize(params.get("ImageSecret"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSecret(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _KeyId: 
        :type KeyId: str
        :param _Username: 
        :type Username: str
        :param _Password: 
        :type Password: str
        :param _SecretId: 
        :type SecretId: str
        """
        self._KeyId = None
        self._Username = None
        self._Password = None
        self._SecretId = None

    @property
    def KeyId(self):
        r"""
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Username(self):
        r"""
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        r"""
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def SecretId(self):
        r"""
        :rtype: str
        """
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._SecretId = params.get("SecretId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InferCodeInfo(AbstractModel):
    r"""Inference code information.

    """

    def __init__(self):
        r"""
        :param _CosPathInfo: Details of Cloud Object Storage (COS) where the inference code is located.Note: This field may return null, indicating that no valid values can be obtained.
        :type CosPathInfo: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        self._CosPathInfo = None

    @property
    def CosPathInfo(self):
        r"""Details of Cloud Object Storage (COS) where the inference code is located.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        return self._CosPathInfo

    @CosPathInfo.setter
    def CosPathInfo(self, CosPathInfo):
        self._CosPathInfo = CosPathInfo


    def _deserialize(self, params):
        if params.get("CosPathInfo") is not None:
            self._CosPathInfo = CosPathInfo()
            self._CosPathInfo._deserialize(params.get("CosPathInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalDisk(AbstractModel):
    r"""Local disk information.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Node ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _LocalPath: Local path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LocalPath: str
        """
        self._InstanceId = None
        self._LocalPath = None

    @property
    def InstanceId(self):
        r"""Node ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def LocalPath(self):
        r"""Local path.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfig(AbstractModel):
    r"""Log configurations.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logs should be shipped to a Cloud Log Service (CLS) log set.Note: This field may return null, indicating that no valid values can be obtained.
        :type LogsetId: str
        :param _TopicId: Logs should be shipped to a CLS topic.Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        """
        self._LogsetId = None
        self._TopicId = None

    @property
    def LogsetId(self):
        r"""Logs should be shipped to a Cloud Log Service (CLS) log set.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        r"""Logs should be shipped to a CLS topic.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelInfo(AbstractModel):
    r"""Model description information.

    """

    def __init__(self):
        r"""
        :param _ModelVersionId: The model version ID is returned by the DescribeTrainingModelVersion API when querying the model.Enter the task ID of the Automated Machine Learning (AutoML) model.
        :type ModelVersionId: str
        :param _ModelId: Model ID.
        :type ModelId: str
        :param _ModelName: Model name.
        :type ModelName: str
        :param _ModelVersion: Model version.
        :type ModelVersion: str
        :param _ModelSource: Model source.
        :type ModelSource: str
        :param _CosPathInfo: COS path information.
        :type CosPathInfo: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        :param _GooseFSx: GooseFSx configuration. This parameter takes effect if ModelSource is GooseFSx.
Note: This field may return null, indicating that no valid values can be obtained.
        :type GooseFSx: :class:`tencentcloud.tione.v20211111.models.GooseFSx`
        :param _AlgorithmFramework: Algorithm framework corresponding to the model (reserved field).Note: This field may return null, indicating that no valid values can be obtained.
        :type AlgorithmFramework: str
        :param _ModelType: Default: NORMAL; accelerated model: ACCELERATE; automatic learning model: AUTO_ML.Note: This field may return null, indicating that no valid values can be obtained.
        :type ModelType: str
        :param _ModelFormat: Model format.Note: This field may return null, indicating that no valid values can be obtained.
        :type ModelFormat: str
        :param _IsPrivateModel: Whether it is a private LLM.Note: This field may return null, indicating that no valid values can be obtained.
        :type IsPrivateModel: bool
        :param _ModelCategory: Model category. Valid values: MultiModal (multi-modal) and LLM (text LLM).
        :type ModelCategory: str
        :param _PublicDataSource: Data source configurations.
        :type PublicDataSource: :class:`tencentcloud.tione.v20211111.models.PublicDataSourceFS`
        """
        self._ModelVersionId = None
        self._ModelId = None
        self._ModelName = None
        self._ModelVersion = None
        self._ModelSource = None
        self._CosPathInfo = None
        self._GooseFSx = None
        self._AlgorithmFramework = None
        self._ModelType = None
        self._ModelFormat = None
        self._IsPrivateModel = None
        self._ModelCategory = None
        self._PublicDataSource = None

    @property
    def ModelVersionId(self):
        r"""The model version ID is returned by the DescribeTrainingModelVersion API when querying the model.Enter the task ID of the Automated Machine Learning (AutoML) model.
        :rtype: str
        """
        return self._ModelVersionId

    @ModelVersionId.setter
    def ModelVersionId(self, ModelVersionId):
        self._ModelVersionId = ModelVersionId

    @property
    def ModelId(self):
        r"""Model ID.
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelName(self):
        r"""Model name.
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelVersion(self):
        r"""Model version.
        :rtype: str
        """
        return self._ModelVersion

    @ModelVersion.setter
    def ModelVersion(self, ModelVersion):
        self._ModelVersion = ModelVersion

    @property
    def ModelSource(self):
        r"""Model source.
        :rtype: str
        """
        return self._ModelSource

    @ModelSource.setter
    def ModelSource(self, ModelSource):
        self._ModelSource = ModelSource

    @property
    def CosPathInfo(self):
        r"""COS path information.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
        """
        return self._CosPathInfo

    @CosPathInfo.setter
    def CosPathInfo(self, CosPathInfo):
        self._CosPathInfo = CosPathInfo

    @property
    def GooseFSx(self):
        r"""GooseFSx configuration. This parameter takes effect if ModelSource is GooseFSx.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.GooseFSx`
        """
        return self._GooseFSx

    @GooseFSx.setter
    def GooseFSx(self, GooseFSx):
        self._GooseFSx = GooseFSx

    @property
    def AlgorithmFramework(self):
        r"""Algorithm framework corresponding to the model (reserved field).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AlgorithmFramework

    @AlgorithmFramework.setter
    def AlgorithmFramework(self, AlgorithmFramework):
        self._AlgorithmFramework = AlgorithmFramework

    @property
    def ModelType(self):
        r"""Default: NORMAL; accelerated model: ACCELERATE; automatic learning model: AUTO_ML.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def ModelFormat(self):
        r"""Model format.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ModelFormat

    @ModelFormat.setter
    def ModelFormat(self, ModelFormat):
        self._ModelFormat = ModelFormat

    @property
    def IsPrivateModel(self):
        r"""Whether it is a private LLM.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsPrivateModel

    @IsPrivateModel.setter
    def IsPrivateModel(self, IsPrivateModel):
        self._IsPrivateModel = IsPrivateModel

    @property
    def ModelCategory(self):
        r"""Model category. Valid values: MultiModal (multi-modal) and LLM (text LLM).
        :rtype: str
        """
        return self._ModelCategory

    @ModelCategory.setter
    def ModelCategory(self, ModelCategory):
        self._ModelCategory = ModelCategory

    @property
    def PublicDataSource(self):
        r"""Data source configurations.
        :rtype: :class:`tencentcloud.tione.v20211111.models.PublicDataSourceFS`
        """
        return self._PublicDataSource

    @PublicDataSource.setter
    def PublicDataSource(self, PublicDataSource):
        self._PublicDataSource = PublicDataSource


    def _deserialize(self, params):
        self._ModelVersionId = params.get("ModelVersionId")
        self._ModelId = params.get("ModelId")
        self._ModelName = params.get("ModelName")
        self._ModelVersion = params.get("ModelVersion")
        self._ModelSource = params.get("ModelSource")
        if params.get("CosPathInfo") is not None:
            self._CosPathInfo = CosPathInfo()
            self._CosPathInfo._deserialize(params.get("CosPathInfo"))
        if params.get("GooseFSx") is not None:
            self._GooseFSx = GooseFSx()
            self._GooseFSx._deserialize(params.get("GooseFSx"))
        self._AlgorithmFramework = params.get("AlgorithmFramework")
        self._ModelType = params.get("ModelType")
        self._ModelFormat = params.get("ModelFormat")
        self._IsPrivateModel = params.get("IsPrivateModel")
        self._ModelCategory = params.get("ModelCategory")
        if params.get("PublicDataSource") is not None:
            self._PublicDataSource = PublicDataSourceFS()
            self._PublicDataSource._deserialize(params.get("PublicDataSource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NumOrPercent(AbstractModel):
    r"""Percentage or quantity.

    """

    def __init__(self):
        r"""
        :param _Type: Valid values: Num and Percent, which indicate quantity and percentage respectively. The default value is Num.
        :type Type: str
        :param _Value: Numeric value.
        :type Value: int
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        r"""Valid values: Num and Percent, which indicate quantity and percentage respectively. The default value is Num.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""Numeric value.
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Option(AbstractModel):
    r"""Key-value pair.

    """

    def __init__(self):
        r"""
        :param _Name: Metric name.
        :type Name: str
        :param _Value: Metric value.
        :type Value: int
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""Metric name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""Metric value.
        :rtype: int
        """
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
        


class Pod(AbstractModel):
    r"""Pod information display.

    """

    def __init__(self):
        r"""
        :param _Name: Pod name.Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Uid: Unique ID of the Pod.Note: This field may return null, indicating that no valid values can be obtained.
        :type Uid: str
        :param _ChargeType: Service payment mode.Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _Phase: Pod status.Note: This field may return null, indicating that no valid values can be obtained.
        :type Phase: str
        :param _IP: Pod IP address.Note: This field may return null, indicating that no valid values can be obtained.
        :type IP: str
        :param _CreateTime: Pod creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _Containers: Container list.Note: This field may return null, indicating that no valid values can be obtained.
        :type Containers: :class:`tencentcloud.tione.v20211111.models.Container`
        :param _ContainerInfos: Container list.Note: This field may return null, indicating that no valid values can be obtained.
        :type ContainerInfos: list of Container
        :param _CrossTenantENIInfo: Container calling information.Note: This field may return null, indicating that no valid values can be obtained.
        :type CrossTenantENIInfo: :class:`tencentcloud.tione.v20211111.models.CrossTenantENIInfo`
        :param _Status: Instance status information.
        :type Status: str
        :param _StartScheduleTime: Instance scheduling start time.
        :type StartScheduleTime: str
        :param _Message: Supplemental instance status information.
        :type Message: str
        :param _NodeIP: Node IP address of the current instance.
        :type NodeIP: str
        :param _NodeId: Node ID of the current instance.
        :type NodeId: str
        :param _ResourceGroupId: Resource group ID to which the instance belonged.
        :type ResourceGroupId: str
        :param _ResourceGroupName: Resource group name.
        :type ResourceGroupName: str
        :param _ResourceInfo: Resource usage information of the instance.
        :type ResourceInfo: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        """
        self._Name = None
        self._Uid = None
        self._ChargeType = None
        self._Phase = None
        self._IP = None
        self._CreateTime = None
        self._Containers = None
        self._ContainerInfos = None
        self._CrossTenantENIInfo = None
        self._Status = None
        self._StartScheduleTime = None
        self._Message = None
        self._NodeIP = None
        self._NodeId = None
        self._ResourceGroupId = None
        self._ResourceGroupName = None
        self._ResourceInfo = None

    @property
    def Name(self):
        r"""Pod name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uid(self):
        r"""Unique ID of the Pod.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def ChargeType(self):
        r"""Service payment mode.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def Phase(self):
        r"""Pod status.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Phase

    @Phase.setter
    def Phase(self, Phase):
        self._Phase = Phase

    @property
    def IP(self):
        r"""Pod IP address.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def CreateTime(self):
        r"""Pod creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Containers(self):
        warnings.warn("parameter `Containers` is deprecated", DeprecationWarning) 

        r"""Container list.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.Container`
        """
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        warnings.warn("parameter `Containers` is deprecated", DeprecationWarning) 

        self._Containers = Containers

    @property
    def ContainerInfos(self):
        r"""Container list.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Container
        """
        return self._ContainerInfos

    @ContainerInfos.setter
    def ContainerInfos(self, ContainerInfos):
        self._ContainerInfos = ContainerInfos

    @property
    def CrossTenantENIInfo(self):
        r"""Container calling information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CrossTenantENIInfo`
        """
        return self._CrossTenantENIInfo

    @CrossTenantENIInfo.setter
    def CrossTenantENIInfo(self, CrossTenantENIInfo):
        self._CrossTenantENIInfo = CrossTenantENIInfo

    @property
    def Status(self):
        r"""Instance status information.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StartScheduleTime(self):
        r"""Instance scheduling start time.
        :rtype: str
        """
        return self._StartScheduleTime

    @StartScheduleTime.setter
    def StartScheduleTime(self, StartScheduleTime):
        self._StartScheduleTime = StartScheduleTime

    @property
    def Message(self):
        r"""Supplemental instance status information.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def NodeIP(self):
        r"""Node IP address of the current instance.
        :rtype: str
        """
        return self._NodeIP

    @NodeIP.setter
    def NodeIP(self, NodeIP):
        self._NodeIP = NodeIP

    @property
    def NodeId(self):
        r"""Node ID of the current instance.
        :rtype: str
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def ResourceGroupId(self):
        r"""Resource group ID to which the instance belonged.
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        r"""Resource group name.
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def ResourceInfo(self):
        r"""Resource usage information of the instance.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        """
        return self._ResourceInfo

    @ResourceInfo.setter
    def ResourceInfo(self, ResourceInfo):
        self._ResourceInfo = ResourceInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Uid = params.get("Uid")
        self._ChargeType = params.get("ChargeType")
        self._Phase = params.get("Phase")
        self._IP = params.get("IP")
        self._CreateTime = params.get("CreateTime")
        if params.get("Containers") is not None:
            self._Containers = Container()
            self._Containers._deserialize(params.get("Containers"))
        if params.get("ContainerInfos") is not None:
            self._ContainerInfos = []
            for item in params.get("ContainerInfos"):
                obj = Container()
                obj._deserialize(item)
                self._ContainerInfos.append(obj)
        if params.get("CrossTenantENIInfo") is not None:
            self._CrossTenantENIInfo = CrossTenantENIInfo()
            self._CrossTenantENIInfo._deserialize(params.get("CrossTenantENIInfo"))
        self._Status = params.get("Status")
        self._StartScheduleTime = params.get("StartScheduleTime")
        self._Message = params.get("Message")
        self._NodeIP = params.get("NodeIP")
        self._NodeId = params.get("NodeId")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        if params.get("ResourceInfo") is not None:
            self._ResourceInfo = ResourceInfo()
            self._ResourceInfo._deserialize(params.get("ResourceInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodSSHInfo(AbstractModel):
    r"""Information about Pod access over SSH.

    """

    def __init__(self):
        r"""
        :param _Host: IP address of the Pod.
        :type Host: str
        :param _Port: SSH port of the Pod.
        :type Port: int
        :param _LoginCommand: SSH access command.
        :type LoginCommand: str
        """
        self._Host = None
        self._Port = None
        self._LoginCommand = None

    @property
    def Host(self):
        r"""IP address of the Pod.
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        r"""SSH port of the Pod.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def LoginCommand(self):
        r"""SSH access command.
        :rtype: str
        """
        return self._LoginCommand

    @LoginCommand.setter
    def LoginCommand(self, LoginCommand):
        self._LoginCommand = LoginCommand


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._LoginCommand = params.get("LoginCommand")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Probe(AbstractModel):
    r"""Probe structure information.

    """

    def __init__(self):
        r"""
        :param _ProbeAction: Probe action.
        :type ProbeAction: :class:`tencentcloud.tione.v20211111.models.ProbeAction`
        :param _InitialDelaySeconds: Delay in waiting for a service startup.
        :type InitialDelaySeconds: int
        :param _PeriodSeconds: Polling check interval.
        :type PeriodSeconds: int
        :param _TimeoutSeconds: Check timeout duration.
        :type TimeoutSeconds: int
        :param _FailureThreshold: Number of acknowledged failed detections.
        :type FailureThreshold: int
        :param _SuccessThreshold: Number of acknowledged successful detections. The default values for readiness, liveness, and startup statuses are 3, 1, and 1.
        :type SuccessThreshold: int
        """
        self._ProbeAction = None
        self._InitialDelaySeconds = None
        self._PeriodSeconds = None
        self._TimeoutSeconds = None
        self._FailureThreshold = None
        self._SuccessThreshold = None

    @property
    def ProbeAction(self):
        r"""Probe action.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ProbeAction`
        """
        return self._ProbeAction

    @ProbeAction.setter
    def ProbeAction(self, ProbeAction):
        self._ProbeAction = ProbeAction

    @property
    def InitialDelaySeconds(self):
        r"""Delay in waiting for a service startup.
        :rtype: int
        """
        return self._InitialDelaySeconds

    @InitialDelaySeconds.setter
    def InitialDelaySeconds(self, InitialDelaySeconds):
        self._InitialDelaySeconds = InitialDelaySeconds

    @property
    def PeriodSeconds(self):
        r"""Polling check interval.
        :rtype: int
        """
        return self._PeriodSeconds

    @PeriodSeconds.setter
    def PeriodSeconds(self, PeriodSeconds):
        self._PeriodSeconds = PeriodSeconds

    @property
    def TimeoutSeconds(self):
        r"""Check timeout duration.
        :rtype: int
        """
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def FailureThreshold(self):
        r"""Number of acknowledged failed detections.
        :rtype: int
        """
        return self._FailureThreshold

    @FailureThreshold.setter
    def FailureThreshold(self, FailureThreshold):
        self._FailureThreshold = FailureThreshold

    @property
    def SuccessThreshold(self):
        r"""Number of acknowledged successful detections. The default values for readiness, liveness, and startup statuses are 3, 1, and 1.
        :rtype: int
        """
        return self._SuccessThreshold

    @SuccessThreshold.setter
    def SuccessThreshold(self, SuccessThreshold):
        self._SuccessThreshold = SuccessThreshold


    def _deserialize(self, params):
        if params.get("ProbeAction") is not None:
            self._ProbeAction = ProbeAction()
            self._ProbeAction._deserialize(params.get("ProbeAction"))
        self._InitialDelaySeconds = params.get("InitialDelaySeconds")
        self._PeriodSeconds = params.get("PeriodSeconds")
        self._TimeoutSeconds = params.get("TimeoutSeconds")
        self._FailureThreshold = params.get("FailureThreshold")
        self._SuccessThreshold = params.get("SuccessThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProbeAction(AbstractModel):
    r"""Probe action.

    """

    def __init__(self):
        r"""
        :param _HTTPGet: HTTP GET action.
        :type HTTPGet: :class:`tencentcloud.tione.v20211111.models.HTTPGetAction`
        :param _Exec: Executes check command action.
        :type Exec: :class:`tencentcloud.tione.v20211111.models.ExecAction`
        :param _TCPSocket: TCP Socket check action.
        :type TCPSocket: :class:`tencentcloud.tione.v20211111.models.TCPSocketAction`
        :param _ActionType: Probe type. The default value is HTTPGet. Valid values: HTTPGet, Exec, and TCPSocket.
        :type ActionType: str
        """
        self._HTTPGet = None
        self._Exec = None
        self._TCPSocket = None
        self._ActionType = None

    @property
    def HTTPGet(self):
        r"""HTTP GET action.
        :rtype: :class:`tencentcloud.tione.v20211111.models.HTTPGetAction`
        """
        return self._HTTPGet

    @HTTPGet.setter
    def HTTPGet(self, HTTPGet):
        self._HTTPGet = HTTPGet

    @property
    def Exec(self):
        r"""Executes check command action.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ExecAction`
        """
        return self._Exec

    @Exec.setter
    def Exec(self, Exec):
        self._Exec = Exec

    @property
    def TCPSocket(self):
        r"""TCP Socket check action.
        :rtype: :class:`tencentcloud.tione.v20211111.models.TCPSocketAction`
        """
        return self._TCPSocket

    @TCPSocket.setter
    def TCPSocket(self, TCPSocket):
        self._TCPSocket = TCPSocket

    @property
    def ActionType(self):
        r"""Probe type. The default value is HTTPGet. Valid values: HTTPGet, Exec, and TCPSocket.
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        if params.get("HTTPGet") is not None:
            self._HTTPGet = HTTPGetAction()
            self._HTTPGet._deserialize(params.get("HTTPGet"))
        if params.get("Exec") is not None:
            self._Exec = ExecAction()
            self._Exec._deserialize(params.get("Exec"))
        if params.get("TCPSocket") is not None:
            self._TCPSocket = TCPSocketAction()
            self._TCPSocket._deserialize(params.get("TCPSocket"))
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicDataSourceFS(AbstractModel):
    r"""Public cloud data source structure.

    """

    def __init__(self):
        r"""
        :param _DataSourceId: Data source ID.
        :type DataSourceId: str
        :param _SubPath: Relative subpath to the data source.
        :type SubPath: str
        """
        self._DataSourceId = None
        self._SubPath = None

    @property
    def DataSourceId(self):
        r"""Data source ID.
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId

    @property
    def SubPath(self):
        r"""Relative subpath to the data source.
        :rtype: str
        """
        return self._SubPath

    @SubPath.setter
    def SubPath(self, SubPath):
        self._SubPath = SubPath


    def _deserialize(self, params):
        self._DataSourceId = params.get("DataSourceId")
        self._SubPath = params.get("SubPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RDMAConfig(AbstractModel):
    r"""RDMA configuration.

    """

    def __init__(self):
        r"""
        :param _Enable: Whether to enable RDMA.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enable: bool
        """
        self._Enable = None

    @property
    def Enable(self):
        r"""Whether to enable RDMA.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceConfigInfo(AbstractModel):
    r"""Resource configuration.

    """

    def __init__(self):
        r"""
        :param _Role: Role. For example, PS, WORKER, DRIVER, and EXECUTOR.
        :type Role: str
        :param _Cpu: Number of CPU cores, which is required to be configured when resource groups are used. Unit: 1/1000, where 1000 represents 1 core.
        :type Cpu: int
        :param _Memory: Memory size, in MB. This parameter needs to be configured when resource groups are used.
        :type Memory: int
        :param _GpuType: GPU card type, which is required to be configured when resource groups are used.
        :type GpuType: str
        :param _Gpu: Number of GPU cards, which is required to be configured when resource groups are used. Unit: 1/100, where 100 represents 1 card.
        :type Gpu: int
        :param _InstanceType: CVM instance specification ID.
CVM instance specification (for postpaid billing). Valid values:
TI.S.LARGE.POST: 4C8G 
TI.S.2XLARGE16.POST:  8C16G 
TI.S.2XLARGE32.POST:  8C32G 
TI.S.4XLARGE32.POST:  16C32G
TI.S.4XLARGE64.POST:  16C64G
TI.S.6XLARGE48.POST:  24C48G
TI.S.6XLARGE96.POST:  24C96G
TI.S.8XLARGE64.POST:  32C64G
TI.S.8XLARGE128.POST : 32C128G
TI.GN10.2XLARGE40.POST: 8C40G V100*1 
TI.GN10.5XLARGE80.POST:  18C80G V100*2 
TI.GN10.10XLARGE160.POST :  32C160G V100*4
TI.GN10.20XLARGE320.POST :  72C320G V100*8
TI.GN7.8XLARGE128.POST: 32C128G T4*1 
TI.GN7.10XLARGE160.POST: 40C160G T4*2 
TI.GN7.20XLARGE320.POST: 80C32
        :type InstanceType: str
        :param _InstanceNum: Number of compute nodes.
        :type InstanceNum: int
        :param _InstanceTypeAlias: CVM instance specification name.
CVM instance specification (for postpaid billing). Valid values:
4C8G 
8C16G 
8C32G 
16C32G
6C64G
24C48G
24C96G
32C64G
32C128G
8C40G V100*1 
8C80G V100*2 
32C160G V100*4
72C320G V100*8
32C128G T4*1 
40C160G T4*2 
80C32
        :type InstanceTypeAlias: str
        :param _RDMAConfig: RDMA configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RDMAConfig: :class:`tencentcloud.tione.v20211111.models.RDMAConfig`
        """
        self._Role = None
        self._Cpu = None
        self._Memory = None
        self._GpuType = None
        self._Gpu = None
        self._InstanceType = None
        self._InstanceNum = None
        self._InstanceTypeAlias = None
        self._RDMAConfig = None

    @property
    def Role(self):
        r"""Role. For example, PS, WORKER, DRIVER, and EXECUTOR.
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Cpu(self):
        r"""Number of CPU cores, which is required to be configured when resource groups are used. Unit: 1/1000, where 1000 represents 1 core.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""Memory size, in MB. This parameter needs to be configured when resource groups are used.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def GpuType(self):
        r"""GPU card type, which is required to be configured when resource groups are used.
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def Gpu(self):
        r"""Number of GPU cards, which is required to be configured when resource groups are used. Unit: 1/100, where 100 represents 1 card.
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def InstanceType(self):
        r"""CVM instance specification ID.
CVM instance specification (for postpaid billing). Valid values:
TI.S.LARGE.POST: 4C8G 
TI.S.2XLARGE16.POST:  8C16G 
TI.S.2XLARGE32.POST:  8C32G 
TI.S.4XLARGE32.POST:  16C32G
TI.S.4XLARGE64.POST:  16C64G
TI.S.6XLARGE48.POST:  24C48G
TI.S.6XLARGE96.POST:  24C96G
TI.S.8XLARGE64.POST:  32C64G
TI.S.8XLARGE128.POST : 32C128G
TI.GN10.2XLARGE40.POST: 8C40G V100*1 
TI.GN10.5XLARGE80.POST:  18C80G V100*2 
TI.GN10.10XLARGE160.POST :  32C160G V100*4
TI.GN10.20XLARGE320.POST :  72C320G V100*8
TI.GN7.8XLARGE128.POST: 32C128G T4*1 
TI.GN7.10XLARGE160.POST: 40C160G T4*2 
TI.GN7.20XLARGE320.POST: 80C32
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceNum(self):
        r"""Number of compute nodes.
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def InstanceTypeAlias(self):
        r"""CVM instance specification name.
CVM instance specification (for postpaid billing). Valid values:
4C8G 
8C16G 
8C32G 
16C32G
6C64G
24C48G
24C96G
32C64G
32C128G
8C40G V100*1 
8C80G V100*2 
32C160G V100*4
72C320G V100*8
32C128G T4*1 
40C160G T4*2 
80C32
        :rtype: str
        """
        return self._InstanceTypeAlias

    @InstanceTypeAlias.setter
    def InstanceTypeAlias(self, InstanceTypeAlias):
        self._InstanceTypeAlias = InstanceTypeAlias

    @property
    def RDMAConfig(self):
        r"""RDMA configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.RDMAConfig`
        """
        return self._RDMAConfig

    @RDMAConfig.setter
    def RDMAConfig(self, RDMAConfig):
        self._RDMAConfig = RDMAConfig


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._GpuType = params.get("GpuType")
        self._Gpu = params.get("Gpu")
        self._InstanceType = params.get("InstanceType")
        self._InstanceNum = params.get("InstanceNum")
        self._InstanceTypeAlias = params.get("InstanceTypeAlias")
        if params.get("RDMAConfig") is not None:
            self._RDMAConfig = RDMAConfig()
            self._RDMAConfig._deserialize(params.get("RDMAConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceGroupInfo(AbstractModel):
    r"""Summarized information structure for the serviced resource group while an online service is provided.

    """

    def __init__(self):
        r"""
        :param _ResourceGroupId: Resource group ID.
        :type ResourceGroupId: str
        :param _ResourceGroupName: Resource group name.
        :type ResourceGroupName: str
        """
        self._ResourceGroupId = None
        self._ResourceGroupName = None

    @property
    def ResourceGroupId(self):
        r"""Resource group ID.
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        r"""Resource group name.
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName


    def _deserialize(self, params):
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInfo(AbstractModel):
    r"""Resource information description.

    """

    def __init__(self):
        r"""
        :param _Cpu: Processor resource, in 1/1000 cores.Note: This field may return null, indicating that no valid values can be obtained.
        :type Cpu: int
        :param _Memory: Memory resource, in MB.Note: This field may return null, indicating that no valid values can be obtained.
        :type Memory: int
        :param _Gpu: Number of GPU card resources, in 0.01 units of GpuType.Gpu=100 indicates the use of "1" GPU card. However, this "1" card could refer to a virtualized 1/4 card or a full physical card, depending on the instance type.Example 1: If the instance type includes 1 virtual GPU card, and each virtual GPU card corresponds to 1/4 of a physical T4 card, then GpuType=T4, Gpu=100, and RealGpu=25.Example 2: If the instance type includes 4 full GPU cards, and each card corresponds to 1 physical T4 card, then GpuType=T4, Gpu=400, and RealGpu=400.Note: This field may return null, indicating that no valid values can be obtained.
        :type Gpu: int
        :param _GpuType: GPU card model. Valid values: T4 and V100. It only displays the current GPU card model. If multiple types of cards are used simultaneously, see the value of RealGpuDetailSet.Note: This field may return null, indicating that no valid values can be obtained.
        :type GpuType: str
        :param _RealGpu: It is not required for creation or update operations. This field is used for display only.The actual GPU card resources for postpaid instances using fractional GPU cards. This value represents the total number of actual physical GPU cards consumed.RealGpu=100 indicates the consumption of 1 GPU card. Depending on the actual instance type, this may represent: 4 instances each using a 1/4 card, 2 instances each using a 1/2 card, or 1 instance using a full card.
        :type RealGpu: int
        :param _RealGpuDetailSet: It is not required for creation or update operations. This field is used for display only. It involves detailed GPU usage information.
        :type RealGpuDetailSet: list of GpuDetail
        :param _EnableRDMA: Indicates whether to enable RDMA.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableRDMA: bool
        :param _RootDisk: 
        :type RootDisk: int
        :param _DataDisk: 
        :type DataDisk: int
        """
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._GpuType = None
        self._RealGpu = None
        self._RealGpuDetailSet = None
        self._EnableRDMA = None
        self._RootDisk = None
        self._DataDisk = None

    @property
    def Cpu(self):
        r"""Processor resource, in 1/1000 cores.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        r"""Memory resource, in MB.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        r"""Number of GPU card resources, in 0.01 units of GpuType.Gpu=100 indicates the use of "1" GPU card. However, this "1" card could refer to a virtualized 1/4 card or a full physical card, depending on the instance type.Example 1: If the instance type includes 1 virtual GPU card, and each virtual GPU card corresponds to 1/4 of a physical T4 card, then GpuType=T4, Gpu=100, and RealGpu=25.Example 2: If the instance type includes 4 full GPU cards, and each card corresponds to 1 physical T4 card, then GpuType=T4, Gpu=400, and RealGpu=400.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuType(self):
        r"""GPU card model. Valid values: T4 and V100. It only displays the current GPU card model. If multiple types of cards are used simultaneously, see the value of RealGpuDetailSet.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def RealGpu(self):
        r"""It is not required for creation or update operations. This field is used for display only.The actual GPU card resources for postpaid instances using fractional GPU cards. This value represents the total number of actual physical GPU cards consumed.RealGpu=100 indicates the consumption of 1 GPU card. Depending on the actual instance type, this may represent: 4 instances each using a 1/4 card, 2 instances each using a 1/2 card, or 1 instance using a full card.
        :rtype: int
        """
        return self._RealGpu

    @RealGpu.setter
    def RealGpu(self, RealGpu):
        self._RealGpu = RealGpu

    @property
    def RealGpuDetailSet(self):
        r"""It is not required for creation or update operations. This field is used for display only. It involves detailed GPU usage information.
        :rtype: list of GpuDetail
        """
        return self._RealGpuDetailSet

    @RealGpuDetailSet.setter
    def RealGpuDetailSet(self, RealGpuDetailSet):
        self._RealGpuDetailSet = RealGpuDetailSet

    @property
    def EnableRDMA(self):
        r"""Indicates whether to enable RDMA.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableRDMA

    @EnableRDMA.setter
    def EnableRDMA(self, EnableRDMA):
        self._EnableRDMA = EnableRDMA

    @property
    def RootDisk(self):
        r"""
        :rtype: int
        """
        return self._RootDisk

    @RootDisk.setter
    def RootDisk(self, RootDisk):
        self._RootDisk = RootDisk

    @property
    def DataDisk(self):
        r"""
        :rtype: int
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk


    def _deserialize(self, params):
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._GpuType = params.get("GpuType")
        self._RealGpu = params.get("RealGpu")
        if params.get("RealGpuDetailSet") is not None:
            self._RealGpuDetailSet = []
            for item in params.get("RealGpuDetailSet"):
                obj = GpuDetail()
                obj._deserialize(item)
                self._RealGpuDetailSet.append(obj)
        self._EnableRDMA = params.get("EnableRDMA")
        self._RootDisk = params.get("RootDisk")
        self._DataDisk = params.get("DataDisk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceSupplyAttribute(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _SupplyType: 
        :type SupplyType: str
        :param _ClusterType: 
        :type ClusterType: str
        """
        self._SupplyType = None
        self._ClusterType = None

    @property
    def SupplyType(self):
        r"""
        :rtype: str
        """
        return self._SupplyType

    @SupplyType.setter
    def SupplyType(self, SupplyType):
        self._SupplyType = SupplyType

    @property
    def ClusterType(self):
        r"""
        :rtype: str
        """
        return self._ClusterType

    @ClusterType.setter
    def ClusterType(self, ClusterType):
        self._ClusterType = ClusterType


    def _deserialize(self, params):
        self._SupplyType = params.get("SupplyType")
        self._ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollingUpdate(AbstractModel):
    r"""Rolling update policy.

    """

    def __init__(self):
        r"""
        :param _MaxUnavailable: Maximum unavailability for rolling updates.
        :type MaxUnavailable: :class:`tencentcloud.tione.v20211111.models.NumOrPercent`
        :param _MaxSurge: Maximum number of new instances during rolling updates. 
        :type MaxSurge: :class:`tencentcloud.tione.v20211111.models.NumOrPercent`
        """
        self._MaxUnavailable = None
        self._MaxSurge = None

    @property
    def MaxUnavailable(self):
        r"""Maximum unavailability for rolling updates.
        :rtype: :class:`tencentcloud.tione.v20211111.models.NumOrPercent`
        """
        return self._MaxUnavailable

    @MaxUnavailable.setter
    def MaxUnavailable(self, MaxUnavailable):
        self._MaxUnavailable = MaxUnavailable

    @property
    def MaxSurge(self):
        r"""Maximum number of new instances during rolling updates. 
        :rtype: :class:`tencentcloud.tione.v20211111.models.NumOrPercent`
        """
        return self._MaxSurge

    @MaxSurge.setter
    def MaxSurge(self, MaxSurge):
        self._MaxSurge = MaxSurge


    def _deserialize(self, params):
        if params.get("MaxUnavailable") is not None:
            self._MaxUnavailable = NumOrPercent()
            self._MaxUnavailable._deserialize(params.get("MaxUnavailable"))
        if params.get("MaxSurge") is not None:
            self._MaxSurge = NumOrPercent()
            self._MaxSurge._deserialize(params.get("MaxSurge"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SSHConfig(AbstractModel):
    r"""Notebook SSH port configuration.

    """

    def __init__(self):
        r"""
        :param _Enable: Whether to enable SSH.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Enable: bool
        :param _PublicKey: Public key information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicKey: str
        :param _Port: Port number.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        :param _LoginCommand: Login command.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LoginCommand: str
        :param _IsAddressChanged: Whether to change the login address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsAddressChanged: bool
        :param _PodSSHInfo: Pod access information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PodSSHInfo: :class:`tencentcloud.tione.v20211111.models.PodSSHInfo`
        """
        self._Enable = None
        self._PublicKey = None
        self._Port = None
        self._LoginCommand = None
        self._IsAddressChanged = None
        self._PodSSHInfo = None

    @property
    def Enable(self):
        r"""Whether to enable SSH.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def PublicKey(self):
        r"""Public key information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Port(self):
        r"""Port number.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def LoginCommand(self):
        r"""Login command.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LoginCommand

    @LoginCommand.setter
    def LoginCommand(self, LoginCommand):
        self._LoginCommand = LoginCommand

    @property
    def IsAddressChanged(self):
        r"""Whether to change the login address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._IsAddressChanged

    @IsAddressChanged.setter
    def IsAddressChanged(self, IsAddressChanged):
        self._IsAddressChanged = IsAddressChanged

    @property
    def PodSSHInfo(self):
        r"""Pod access information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.PodSSHInfo`
        """
        return self._PodSSHInfo

    @PodSSHInfo.setter
    def PodSSHInfo(self, PodSSHInfo):
        self._PodSSHInfo = PodSSHInfo


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._PublicKey = params.get("PublicKey")
        self._Port = params.get("Port")
        self._LoginCommand = params.get("LoginCommand")
        self._IsAddressChanged = params.get("IsAddressChanged")
        if params.get("PodSSHInfo") is not None:
            self._PodSSHInfo = PodSSHInfo()
            self._PodSSHInfo._deserialize(params.get("PodSSHInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduledAction(AbstractModel):
    r"""Scheduled transactions and actions.

    """

    def __init__(self):
        r"""
        :param _ScheduleStop: Whether to stop the service on schedule. Valid values: true and false. If the value is true, ScheduleStopTime is required. If the value is false, ScheduleStopTime does not take effect.
        :type ScheduleStop: bool
        :param _ScheduleStopTime: Time to execute the scheduled stop. Format: "2022-01-26T19:46:22+08:00".
        :type ScheduleStopTime: str
        """
        self._ScheduleStop = None
        self._ScheduleStopTime = None

    @property
    def ScheduleStop(self):
        r"""Whether to stop the service on schedule. Valid values: true and false. If the value is true, ScheduleStopTime is required. If the value is false, ScheduleStopTime does not take effect.
        :rtype: bool
        """
        return self._ScheduleStop

    @ScheduleStop.setter
    def ScheduleStop(self, ScheduleStop):
        self._ScheduleStop = ScheduleStop

    @property
    def ScheduleStopTime(self):
        r"""Time to execute the scheduled stop. Format: "2022-01-26T19:46:22+08:00".
        :rtype: str
        """
        return self._ScheduleStopTime

    @ScheduleStopTime.setter
    def ScheduleStopTime(self, ScheduleStopTime):
        self._ScheduleStopTime = ScheduleStopTime


    def _deserialize(self, params):
        self._ScheduleStop = params.get("ScheduleStop")
        self._ScheduleStopTime = params.get("ScheduleStopTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingPolicy(AbstractModel):
    r"""Service scheduling policy configurations.

    """

    def __init__(self):
        r"""
        :param _CrossResourceGroupScheduling: Whether to enable cross-resource-group scheduling.
        :type CrossResourceGroupScheduling: bool
        """
        self._CrossResourceGroupScheduling = None

    @property
    def CrossResourceGroupScheduling(self):
        r"""Whether to enable cross-resource-group scheduling.
        :rtype: bool
        """
        return self._CrossResourceGroupScheduling

    @CrossResourceGroupScheduling.setter
    def CrossResourceGroupScheduling(self, CrossResourceGroupScheduling):
        self._CrossResourceGroupScheduling = CrossResourceGroupScheduling


    def _deserialize(self, params):
        self._CrossResourceGroupScheduling = params.get("CrossResourceGroupScheduling")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    r"""Online service description.

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: Service group ID.
        :type ServiceGroupId: str
        :param _ServiceId: Service ID.
        :type ServiceId: str
        :param _ServiceGroupName: Service group name.
        :type ServiceGroupName: str
        :param _ServiceDescription: Service description.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceDescription: str
        :param _ServiceInfo: Service details.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceInfo: :class:`tencentcloud.tione.v20211111.models.ServiceInfo`
        :param _ClusterId: Cluster ID.Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterId: str
        :param _Region: Region.Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Namespace: Namespace.Note: This field may return null, indicating that no valid values can be obtained.
        :type Namespace: str
        :param _ChargeType: Billing type.Note: This field may return null, indicating that no valid values can be obtained.
        :type ChargeType: str
        :param _ResourceGroupId: Resource group ID for yearly/monthly subscription services. The value is null for pay-as-you-go services.Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceGroupId: str
        :param _ResourceGroupName: Resource group name corresponding to the yearly/monthly subscription service.Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceGroupName: str
        :param _Tags: Tag of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _IngressName: Name of the ingress where the service is located.Note: This field may return null, indicating that no valid values can be obtained.
        :type IngressName: str
        :param _CreatedBy: Creator.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedBy: str
        :param _CreateTime: Creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time.Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _Uin: Root account.Note: This field may return null, indicating that no valid values can be obtained.
        :type Uin: str
        :param _SubUin: Sub-account.Note: This field may return null, indicating that no valid values can be obtained.
        :type SubUin: str
        :param _AppId: app_id
Note: This field may return null, indicating that no valid values can be obtained.
        :type AppId: int
        :param _BusinessStatus: Operational status of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessStatus: str
        :param _ServiceLimit: Deprecated. See the corresponding field in ServiceInfo.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param _ScheduledAction: Deprecated. See the corresponding field in ServiceInfo.Note: This field may return null, indicating that no valid values can be obtained.
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param _CreateFailedReason: Cause for service creation failure. The default value of this field is CREATE_SUCCEED upon successful creation.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateFailedReason: str
        :param _Status: Service status.CREATING: creating.CREATE_FAILED: creation failed.Normal: running.Stopped: stopped.Stopping: stopping.Abnormal: error.Pending: starting.Waiting: getting ready.Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _BillingInfo: Billing information.Note: This field may return null, indicating that no valid values can be obtained.
        :type BillingInfo: str
        :param _Weight: Model weight.Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _CreateSource: Creation source of the service.AUTO_ML: comes from one-click release of automatic learning.DEFAULT: other sources.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateSource: str
        :param _Version: Version number.Note: This field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _LatestVersion: The latest version number of services under a service group.Note: This field may return null, indicating that no valid values can be obtained.
        :type LatestVersion: str
        :param _ResourceGroupSWType: Resource group category. Valid values: NORMAL (hosting) and SW (half-hosting).Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceGroupSWType: str
        :param _ArchiveStatus: Archiving status of the service. Valid values: Waiting (pending archiving) and Archived (archived).Note: This field may return null, indicating that no valid values can be obtained.
        :type ArchiveStatus: str
        :param _DeployType: Deployment type of the service. Valid values: STANDARD (standard deployment) and DIST (multi-machine distributed deployment). The default value is STANDARD.Note: This field may return null, indicating that no valid values can be obtained.
        :type DeployType: str
        :param _InstancePerReplicas: Number of instances per replica. This parameter is valid only when the deployment type is DIST. Default value: 1.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstancePerReplicas: str
        :param _MonitorSource: Source for monitoring queries.Enumeration value. May differ from CreateSource in certain scenarios. This field is designed to be compatible.
        :type MonitorSource: str
        :param _SubUinName: Sub-account name of the service creator.
        :type SubUinName: str
        :param _SchedulingPolicy: Scheduling policy of the service.
        :type SchedulingPolicy: :class:`tencentcloud.tione.v20211111.models.SchedulingPolicy`
        :param _ExternalResourceGroups: External resource group information, indicating which resources are borrowed from resource groups.
        :type ExternalResourceGroups: list of ResourceGroupInfo
        """
        self._ServiceGroupId = None
        self._ServiceId = None
        self._ServiceGroupName = None
        self._ServiceDescription = None
        self._ServiceInfo = None
        self._ClusterId = None
        self._Region = None
        self._Namespace = None
        self._ChargeType = None
        self._ResourceGroupId = None
        self._ResourceGroupName = None
        self._Tags = None
        self._IngressName = None
        self._CreatedBy = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Uin = None
        self._SubUin = None
        self._AppId = None
        self._BusinessStatus = None
        self._ServiceLimit = None
        self._ScheduledAction = None
        self._CreateFailedReason = None
        self._Status = None
        self._BillingInfo = None
        self._Weight = None
        self._CreateSource = None
        self._Version = None
        self._LatestVersion = None
        self._ResourceGroupSWType = None
        self._ArchiveStatus = None
        self._DeployType = None
        self._InstancePerReplicas = None
        self._MonitorSource = None
        self._SubUinName = None
        self._SchedulingPolicy = None
        self._ExternalResourceGroups = None

    @property
    def ServiceGroupId(self):
        r"""Service group ID.
        :rtype: str
        """
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def ServiceId(self):
        r"""Service ID.
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceGroupName(self):
        r"""Service group name.
        :rtype: str
        """
        return self._ServiceGroupName

    @ServiceGroupName.setter
    def ServiceGroupName(self, ServiceGroupName):
        self._ServiceGroupName = ServiceGroupName

    @property
    def ServiceDescription(self):
        r"""Service description.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServiceDescription

    @ServiceDescription.setter
    def ServiceDescription(self, ServiceDescription):
        self._ServiceDescription = ServiceDescription

    @property
    def ServiceInfo(self):
        r"""Service details.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ServiceInfo`
        """
        return self._ServiceInfo

    @ServiceInfo.setter
    def ServiceInfo(self, ServiceInfo):
        self._ServiceInfo = ServiceInfo

    @property
    def ClusterId(self):
        r"""Cluster ID.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Region(self):
        r"""Region.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Namespace(self):
        r"""Namespace.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ChargeType(self):
        r"""Billing type.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceGroupId(self):
        r"""Resource group ID for yearly/monthly subscription services. The value is null for pay-as-you-go services.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def ResourceGroupName(self):
        r"""Resource group name corresponding to the yearly/monthly subscription service.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def Tags(self):
        r"""Tag of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IngressName(self):
        r"""Name of the ingress where the service is located.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def CreatedBy(self):
        r"""Creator.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreateTime(self):
        r"""Creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Update time.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Uin(self):
        r"""Root account.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""Sub-account.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def AppId(self):
        r"""app_id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def BusinessStatus(self):
        r"""Operational status of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BusinessStatus

    @BusinessStatus.setter
    def BusinessStatus(self, BusinessStatus):
        self._BusinessStatus = BusinessStatus

    @property
    def ServiceLimit(self):
        warnings.warn("parameter `ServiceLimit` is deprecated", DeprecationWarning) 

        r"""Deprecated. See the corresponding field in ServiceInfo.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        """
        return self._ServiceLimit

    @ServiceLimit.setter
    def ServiceLimit(self, ServiceLimit):
        warnings.warn("parameter `ServiceLimit` is deprecated", DeprecationWarning) 

        self._ServiceLimit = ServiceLimit

    @property
    def ScheduledAction(self):
        warnings.warn("parameter `ScheduledAction` is deprecated", DeprecationWarning) 

        r"""Deprecated. See the corresponding field in ServiceInfo.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        """
        return self._ScheduledAction

    @ScheduledAction.setter
    def ScheduledAction(self, ScheduledAction):
        warnings.warn("parameter `ScheduledAction` is deprecated", DeprecationWarning) 

        self._ScheduledAction = ScheduledAction

    @property
    def CreateFailedReason(self):
        r"""Cause for service creation failure. The default value of this field is CREATE_SUCCEED upon successful creation.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateFailedReason

    @CreateFailedReason.setter
    def CreateFailedReason(self, CreateFailedReason):
        self._CreateFailedReason = CreateFailedReason

    @property
    def Status(self):
        r"""Service status.CREATING: creating.CREATE_FAILED: creation failed.Normal: running.Stopped: stopped.Stopping: stopping.Abnormal: error.Pending: starting.Waiting: getting ready.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BillingInfo(self):
        r"""Billing information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo

    @property
    def Weight(self):
        r"""Model weight.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreateSource(self):
        r"""Creation source of the service.AUTO_ML: comes from one-click release of automatic learning.DEFAULT: other sources.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateSource

    @CreateSource.setter
    def CreateSource(self, CreateSource):
        self._CreateSource = CreateSource

    @property
    def Version(self):
        r"""Version number.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LatestVersion(self):
        r"""The latest version number of services under a service group.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LatestVersion

    @LatestVersion.setter
    def LatestVersion(self, LatestVersion):
        self._LatestVersion = LatestVersion

    @property
    def ResourceGroupSWType(self):
        r"""Resource group category. Valid values: NORMAL (hosting) and SW (half-hosting).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ResourceGroupSWType

    @ResourceGroupSWType.setter
    def ResourceGroupSWType(self, ResourceGroupSWType):
        self._ResourceGroupSWType = ResourceGroupSWType

    @property
    def ArchiveStatus(self):
        r"""Archiving status of the service. Valid values: Waiting (pending archiving) and Archived (archived).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ArchiveStatus

    @ArchiveStatus.setter
    def ArchiveStatus(self, ArchiveStatus):
        self._ArchiveStatus = ArchiveStatus

    @property
    def DeployType(self):
        r"""Deployment type of the service. Valid values: STANDARD (standard deployment) and DIST (multi-machine distributed deployment). The default value is STANDARD.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeployType

    @DeployType.setter
    def DeployType(self, DeployType):
        self._DeployType = DeployType

    @property
    def InstancePerReplicas(self):
        r"""Number of instances per replica. This parameter is valid only when the deployment type is DIST. Default value: 1.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstancePerReplicas

    @InstancePerReplicas.setter
    def InstancePerReplicas(self, InstancePerReplicas):
        self._InstancePerReplicas = InstancePerReplicas

    @property
    def MonitorSource(self):
        r"""Source for monitoring queries.Enumeration value. May differ from CreateSource in certain scenarios. This field is designed to be compatible.
        :rtype: str
        """
        return self._MonitorSource

    @MonitorSource.setter
    def MonitorSource(self, MonitorSource):
        self._MonitorSource = MonitorSource

    @property
    def SubUinName(self):
        r"""Sub-account name of the service creator.
        :rtype: str
        """
        return self._SubUinName

    @SubUinName.setter
    def SubUinName(self, SubUinName):
        self._SubUinName = SubUinName

    @property
    def SchedulingPolicy(self):
        r"""Scheduling policy of the service.
        :rtype: :class:`tencentcloud.tione.v20211111.models.SchedulingPolicy`
        """
        return self._SchedulingPolicy

    @SchedulingPolicy.setter
    def SchedulingPolicy(self, SchedulingPolicy):
        self._SchedulingPolicy = SchedulingPolicy

    @property
    def ExternalResourceGroups(self):
        r"""External resource group information, indicating which resources are borrowed from resource groups.
        :rtype: list of ResourceGroupInfo
        """
        return self._ExternalResourceGroups

    @ExternalResourceGroups.setter
    def ExternalResourceGroups(self, ExternalResourceGroups):
        self._ExternalResourceGroups = ExternalResourceGroups


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._ServiceId = params.get("ServiceId")
        self._ServiceGroupName = params.get("ServiceGroupName")
        self._ServiceDescription = params.get("ServiceDescription")
        if params.get("ServiceInfo") is not None:
            self._ServiceInfo = ServiceInfo()
            self._ServiceInfo._deserialize(params.get("ServiceInfo"))
        self._ClusterId = params.get("ClusterId")
        self._Region = params.get("Region")
        self._Namespace = params.get("Namespace")
        self._ChargeType = params.get("ChargeType")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._ResourceGroupName = params.get("ResourceGroupName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IngressName = params.get("IngressName")
        self._CreatedBy = params.get("CreatedBy")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._AppId = params.get("AppId")
        self._BusinessStatus = params.get("BusinessStatus")
        if params.get("ServiceLimit") is not None:
            self._ServiceLimit = ServiceLimit()
            self._ServiceLimit._deserialize(params.get("ServiceLimit"))
        if params.get("ScheduledAction") is not None:
            self._ScheduledAction = ScheduledAction()
            self._ScheduledAction._deserialize(params.get("ScheduledAction"))
        self._CreateFailedReason = params.get("CreateFailedReason")
        self._Status = params.get("Status")
        self._BillingInfo = params.get("BillingInfo")
        self._Weight = params.get("Weight")
        self._CreateSource = params.get("CreateSource")
        self._Version = params.get("Version")
        self._LatestVersion = params.get("LatestVersion")
        self._ResourceGroupSWType = params.get("ResourceGroupSWType")
        self._ArchiveStatus = params.get("ArchiveStatus")
        self._DeployType = params.get("DeployType")
        self._InstancePerReplicas = params.get("InstancePerReplicas")
        self._MonitorSource = params.get("MonitorSource")
        self._SubUinName = params.get("SubUinName")
        if params.get("SchedulingPolicy") is not None:
            self._SchedulingPolicy = SchedulingPolicy()
            self._SchedulingPolicy._deserialize(params.get("SchedulingPolicy"))
        if params.get("ExternalResourceGroups") is not None:
            self._ExternalResourceGroups = []
            for item in params.get("ExternalResourceGroups"):
                obj = ResourceGroupInfo()
                obj._deserialize(item)
                self._ExternalResourceGroups.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEIP(AbstractModel):
    r"""Service shared Elastic Network Interface (ENI) settings.

    """

    def __init__(self):
        r"""
        :param _EnableEIP: Whether to enable access from the TI-ONE private network to external resources.Note: This field may return null, indicating that no valid values can be obtained.
        :type EnableEIP: bool
        :param _VpcId: User VPC ID.Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: User subnet ID.Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        """
        self._EnableEIP = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def EnableEIP(self):
        r"""Whether to enable access from the TI-ONE private network to external resources.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._EnableEIP

    @EnableEIP.setter
    def EnableEIP(self, EnableEIP):
        self._EnableEIP = EnableEIP

    @property
    def VpcId(self):
        r"""User VPC ID.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""User subnet ID.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._EnableEIP = params.get("EnableEIP")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGroup(AbstractModel):
    r"""Information of a service group for an online service.

    """

    def __init__(self):
        r"""
        :param _ServiceGroupId: Service group ID.
        :type ServiceGroupId: str
        :param _ServiceGroupName: Service group name.
        :type ServiceGroupName: str
        :param _CreatedBy: Creator.
        :type CreatedBy: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        :param _Uin: Root account.
        :type Uin: str
        :param _ServiceCount: Total number of services in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceCount: int
        :param _RunningServiceCount: Number of running services in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :type RunningServiceCount: int
        :param _Services: Service description.Note: This field may return null, indicating that no valid values can be obtained.
        :type Services: list of Service
        :param _Status: Service group status, which aligns with service status.CREATING: creating.CREATE_FAILED: creation failed.Normal: running.Stopped: stopped.Stopping: stopping.Abnormal: error.Pending: starting.Waiting: getting ready.Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Tags: Service group tags.Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _LatestVersion: The latest version in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :type LatestVersion: str
        :param _BusinessStatus: Operational status of the service.CREATING: creating.CREATE_FAILED: creation failed.ARREARS_STOP: service suspended due to overdue payments.BILLING: billing.WHITELIST_USING: allowlist feature is in trial.WHITELIST_STOP: insufficient allowlist quota.Note: This field may return null, indicating that no valid values can be obtained.
        :type BusinessStatus: str
        :param _BillingInfo: Billing information of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :type BillingInfo: str
        :param _CreateSource: Creation source of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateSource: str
        :param _WeightUpdateStatus: Weight update status of the service group.UPDATING: updating.UPDATED: updated successfully.UPDATE FAILED: failed to update.Note: This field may return null, indicating that no valid values can be obtained.
        :type WeightUpdateStatus: str
        :param _ReplicasCount: Number of running Pods in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :type ReplicasCount: int
        :param _AvailableReplicasCount: Expected number of Pods under the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :type AvailableReplicasCount: int
        :param _SubUin: Service group's subuin.
        :type SubUin: str
        :param _AppId: Service group's app_id.
        :type AppId: int
        :param _AuthorizationEnable: Whether to enable authentication.
        :type AuthorizationEnable: bool
        :param _AuthTokens: List of throttling authentication tokens.
        :type AuthTokens: list of AuthToken
        :param _MonitorSource: Field for monitoring creation source.
        :type MonitorSource: str
        :param _SubUinName: Nickname of the sub-user.
        :type SubUinName: str
        """
        self._ServiceGroupId = None
        self._ServiceGroupName = None
        self._CreatedBy = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Uin = None
        self._ServiceCount = None
        self._RunningServiceCount = None
        self._Services = None
        self._Status = None
        self._Tags = None
        self._LatestVersion = None
        self._BusinessStatus = None
        self._BillingInfo = None
        self._CreateSource = None
        self._WeightUpdateStatus = None
        self._ReplicasCount = None
        self._AvailableReplicasCount = None
        self._SubUin = None
        self._AppId = None
        self._AuthorizationEnable = None
        self._AuthTokens = None
        self._MonitorSource = None
        self._SubUinName = None

    @property
    def ServiceGroupId(self):
        r"""Service group ID.
        :rtype: str
        """
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId

    @property
    def ServiceGroupName(self):
        r"""Service group name.
        :rtype: str
        """
        return self._ServiceGroupName

    @ServiceGroupName.setter
    def ServiceGroupName(self, ServiceGroupName):
        self._ServiceGroupName = ServiceGroupName

    @property
    def CreatedBy(self):
        r"""Creator.
        :rtype: str
        """
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreateTime(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""Update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Uin(self):
        r"""Root account.
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ServiceCount(self):
        r"""Total number of services in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def RunningServiceCount(self):
        r"""Number of running services in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RunningServiceCount

    @RunningServiceCount.setter
    def RunningServiceCount(self, RunningServiceCount):
        self._RunningServiceCount = RunningServiceCount

    @property
    def Services(self):
        r"""Service description.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Service
        """
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def Status(self):
        r"""Service group status, which aligns with service status.CREATING: creating.CREATE_FAILED: creation failed.Normal: running.Stopped: stopped.Stopping: stopping.Abnormal: error.Pending: starting.Waiting: getting ready.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""Service group tags.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def LatestVersion(self):
        r"""The latest version in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LatestVersion

    @LatestVersion.setter
    def LatestVersion(self, LatestVersion):
        self._LatestVersion = LatestVersion

    @property
    def BusinessStatus(self):
        r"""Operational status of the service.CREATING: creating.CREATE_FAILED: creation failed.ARREARS_STOP: service suspended due to overdue payments.BILLING: billing.WHITELIST_USING: allowlist feature is in trial.WHITELIST_STOP: insufficient allowlist quota.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BusinessStatus

    @BusinessStatus.setter
    def BusinessStatus(self, BusinessStatus):
        self._BusinessStatus = BusinessStatus

    @property
    def BillingInfo(self):
        r"""Billing information of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BillingInfo

    @BillingInfo.setter
    def BillingInfo(self, BillingInfo):
        self._BillingInfo = BillingInfo

    @property
    def CreateSource(self):
        r"""Creation source of the service.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateSource

    @CreateSource.setter
    def CreateSource(self, CreateSource):
        self._CreateSource = CreateSource

    @property
    def WeightUpdateStatus(self):
        r"""Weight update status of the service group.UPDATING: updating.UPDATED: updated successfully.UPDATE FAILED: failed to update.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._WeightUpdateStatus

    @WeightUpdateStatus.setter
    def WeightUpdateStatus(self, WeightUpdateStatus):
        self._WeightUpdateStatus = WeightUpdateStatus

    @property
    def ReplicasCount(self):
        r"""Number of running Pods in the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ReplicasCount

    @ReplicasCount.setter
    def ReplicasCount(self, ReplicasCount):
        self._ReplicasCount = ReplicasCount

    @property
    def AvailableReplicasCount(self):
        r"""Expected number of Pods under the service group.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AvailableReplicasCount

    @AvailableReplicasCount.setter
    def AvailableReplicasCount(self, AvailableReplicasCount):
        self._AvailableReplicasCount = AvailableReplicasCount

    @property
    def SubUin(self):
        r"""Service group's subuin.
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def AppId(self):
        r"""Service group's app_id.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AuthorizationEnable(self):
        r"""Whether to enable authentication.
        :rtype: bool
        """
        return self._AuthorizationEnable

    @AuthorizationEnable.setter
    def AuthorizationEnable(self, AuthorizationEnable):
        self._AuthorizationEnable = AuthorizationEnable

    @property
    def AuthTokens(self):
        r"""List of throttling authentication tokens.
        :rtype: list of AuthToken
        """
        return self._AuthTokens

    @AuthTokens.setter
    def AuthTokens(self, AuthTokens):
        self._AuthTokens = AuthTokens

    @property
    def MonitorSource(self):
        r"""Field for monitoring creation source.
        :rtype: str
        """
        return self._MonitorSource

    @MonitorSource.setter
    def MonitorSource(self, MonitorSource):
        self._MonitorSource = MonitorSource

    @property
    def SubUinName(self):
        r"""Nickname of the sub-user.
        :rtype: str
        """
        return self._SubUinName

    @SubUinName.setter
    def SubUinName(self, SubUinName):
        self._SubUinName = SubUinName


    def _deserialize(self, params):
        self._ServiceGroupId = params.get("ServiceGroupId")
        self._ServiceGroupName = params.get("ServiceGroupName")
        self._CreatedBy = params.get("CreatedBy")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Uin = params.get("Uin")
        self._ServiceCount = params.get("ServiceCount")
        self._RunningServiceCount = params.get("RunningServiceCount")
        if params.get("Services") is not None:
            self._Services = []
            for item in params.get("Services"):
                obj = Service()
                obj._deserialize(item)
                self._Services.append(obj)
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._LatestVersion = params.get("LatestVersion")
        self._BusinessStatus = params.get("BusinessStatus")
        self._BillingInfo = params.get("BillingInfo")
        self._CreateSource = params.get("CreateSource")
        self._WeightUpdateStatus = params.get("WeightUpdateStatus")
        self._ReplicasCount = params.get("ReplicasCount")
        self._AvailableReplicasCount = params.get("AvailableReplicasCount")
        self._SubUin = params.get("SubUin")
        self._AppId = params.get("AppId")
        self._AuthorizationEnable = params.get("AuthorizationEnable")
        if params.get("AuthTokens") is not None:
            self._AuthTokens = []
            for item in params.get("AuthTokens"):
                obj = AuthToken()
                obj._deserialize(item)
                self._AuthTokens.append(obj)
        self._MonitorSource = params.get("MonitorSource")
        self._SubUinName = params.get("SubUinName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceInfo(AbstractModel):
    r"""Information of the inference service in the cluster.

    """

    def __init__(self):
        r"""
        :param _Replicas: Expected number of running Pods. The instance is 0 when the stop status is reached.Corresponding relationships under different billing and scaling modes are as follows.PREPAID and POSTPAID_BY_HOUR:Corresponding number of instances in the manual scaling mode.Corresponding number of instances based on the default time-based policy in the auto-scaling mode.HYBRID_PAID:
Corresponding number of instances for postpaid instances in the manual scaling mode.Corresponding number of instances under the default time-based policy for postpaid instances in the auto-scaling mode.Note: This field may return null, indicating that no valid values can be obtained.
        :type Replicas: int
        :param _ImageInfo: Image information.Note: This field may return null, indicating that no valid values can be obtained.
        :type ImageInfo: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        :param _Env: Environment variables.Note: This field may return null, indicating that no valid values can be obtained.
        :type Env: list of EnvVar
        :param _Resources: Resource information.Note: This field may return null, indicating that no valid values can be obtained.
        :type Resources: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _InstanceType: Type specifications corresponding to the postpaid instance.Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param _ModelInfo: Model information.Note: This field may return null, indicating that no valid values can be obtained.
        :type ModelInfo: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        :param _LogEnable: Whether to enable logs.Note: This field may return null, indicating that no valid values can be obtained.
        :type LogEnable: bool
        :param _LogConfig: Log configurations.Note: This field may return null, indicating that no valid values can be obtained.
        :type LogConfig: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        :param _AuthorizationEnable: Whether to enable authentication.Note: This field may return null, indicating that no valid values can be obtained.
        :type AuthorizationEnable: bool
        :param _HorizontalPodAutoscaler: HPA configurations.Note: This field may return null, indicating that no valid values can be obtained.
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        :param _Status: Description of the service status.Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: :class:`tencentcloud.tione.v20211111.models.WorkloadStatus`
        :param _Weight: Weight.Note: This field may return null, indicating that no valid values can be obtained.
        :type Weight: int
        :param _ResourceTotal: Total resources.Note: This field may return null, indicating that no valid values can be obtained.
        :type ResourceTotal: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        :param _OldReplicas: Number of historical instances.Note: This field may return null, indicating that no valid values can be obtained.
        :type OldReplicas: int
        :param _HybridBillingPrepaidReplicas: This parameter is valid when the billing mode is HYBRID_PAID, and is used to identify the number of prepaid instances in the hybrid billing mode. The default value is 1 if this parameter is left unspecified.Note: This field may return null, indicating that no valid values can be obtained.
        :type HybridBillingPrepaidReplicas: int
        :param _OldHybridBillingPrepaidReplicas: Number of instances during the historical HYBRID_PAID period. The user restores services.Note: This field may return null, indicating that no valid values can be obtained.
        :type OldHybridBillingPrepaidReplicas: int
        :param _ModelHotUpdateEnable: Whether to enable hot update for the model. By default, hot update is disabled.Note: This field may return null, indicating that no valid values can be obtained.
        :type ModelHotUpdateEnable: bool
        :param _InstanceAlias: Service specification alias.
        :type InstanceAlias: str
        :param _ScaleMode: Instance quantity adjusting mode. Defaults to manual.Supported valid values: AUTO (automatic), MANUAL (manual).Note: This field may return null, indicating that no valid values can be obtained.
        :type ScaleMode: str
        :param _CronScaleJobs: Scheduled scaling task.Note: This field may return null, indicating that no valid values can be obtained.
        :type CronScaleJobs: list of CronScaleJob
        :param _ScaleStrategy: Scheduled scaling policy.Note: This field may return null, indicating that no valid values can be obtained.
        :type ScaleStrategy: str
        :param _ScheduledAction: Configurations of the scheduled stop.Note: This field may return null, indicating that no valid values can be obtained.
        :type ScheduledAction: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        :param _PodList: Instance list.Note: This field may return null, indicating that no valid values can be obtained.
        :type PodList: list of str
        :param _Pods: Pod list information.Note: This field may return null, indicating that no valid values can be obtained.
        :type Pods: :class:`tencentcloud.tione.v20211111.models.Pod`
        :param _PodInfos: Pod list information.Note: This field may return null, indicating that no valid values can be obtained.
        :type PodInfos: list of Pod
        :param _ServiceLimit: Configurations related to speed limit and throttling of services.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceLimit: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        :param _ModelTurboEnable: Whether to enable model acceleration, which is only valid for models in the StableDiffusion (dynamic acceleration) format.Note: This field may return null, indicating that no valid values can be obtained.
        :type ModelTurboEnable: bool
        :param _VolumeMount: Mounting.Note: This field may return null, indicating that no valid values can be obtained.
        :type VolumeMount: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        :param _InferCodeInfo: Inference code information.Note: This field may return null, indicating that no valid values can be obtained.
        :type InferCodeInfo: :class:`tencentcloud.tione.v20211111.models.InferCodeInfo`
        :param _Command: Service startup command.Note: This field may return null, indicating that no valid values can be obtained.
        :type Command: str
        :param _ServiceEIP: Settings of enabling the TI-ONE private network to access external resources.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServiceEIP: :class:`tencentcloud.tione.v20211111.models.ServiceEIP`
        :param _ServicePort: Service port, with the default value of 8501.Note: This field may return null, indicating that no valid values can be obtained.
        :type ServicePort: int
        :param _TerminationGracePeriodSeconds: Graceful exit time limit of the service, in seconds. Default value: 30. Minimum value: 1.
        :type TerminationGracePeriodSeconds: int
        :param _PreStopCommand: Command executed before the service instance stops. The instance ends after the command execution is completed or after the execution time exceeds the graceful exit time limit.
        :type PreStopCommand: list of str
        :param _GrpcEnable: Whether to enable the gRPC port.
        :type GrpcEnable: bool
        :param _HealthProbe: Health probe.
        :type HealthProbe: :class:`tencentcloud.tione.v20211111.models.HealthProbe`
        :param _RollingUpdate: Rolling update configurations.
        :type RollingUpdate: :class:`tencentcloud.tione.v20211111.models.RollingUpdate`
        :param _InstancePerReplicas: Number of instances per replica. This parameter is valid only when the deployment type is DIST or ROLE. Default value: 1.
        :type InstancePerReplicas: int
        :param _VolumeMounts: Batch data disk mounting configurations.
        :type VolumeMounts: list of VolumeMount
        """
        self._Replicas = None
        self._ImageInfo = None
        self._Env = None
        self._Resources = None
        self._InstanceType = None
        self._ModelInfo = None
        self._LogEnable = None
        self._LogConfig = None
        self._AuthorizationEnable = None
        self._HorizontalPodAutoscaler = None
        self._Status = None
        self._Weight = None
        self._ResourceTotal = None
        self._OldReplicas = None
        self._HybridBillingPrepaidReplicas = None
        self._OldHybridBillingPrepaidReplicas = None
        self._ModelHotUpdateEnable = None
        self._InstanceAlias = None
        self._ScaleMode = None
        self._CronScaleJobs = None
        self._ScaleStrategy = None
        self._ScheduledAction = None
        self._PodList = None
        self._Pods = None
        self._PodInfos = None
        self._ServiceLimit = None
        self._ModelTurboEnable = None
        self._VolumeMount = None
        self._InferCodeInfo = None
        self._Command = None
        self._ServiceEIP = None
        self._ServicePort = None
        self._TerminationGracePeriodSeconds = None
        self._PreStopCommand = None
        self._GrpcEnable = None
        self._HealthProbe = None
        self._RollingUpdate = None
        self._InstancePerReplicas = None
        self._VolumeMounts = None

    @property
    def Replicas(self):
        r"""Expected number of running Pods. The instance is 0 when the stop status is reached.Corresponding relationships under different billing and scaling modes are as follows.PREPAID and POSTPAID_BY_HOUR:Corresponding number of instances in the manual scaling mode.Corresponding number of instances based on the default time-based policy in the auto-scaling mode.HYBRID_PAID:
Corresponding number of instances for postpaid instances in the manual scaling mode.Corresponding number of instances under the default time-based policy for postpaid instances in the auto-scaling mode.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def ImageInfo(self):
        r"""Image information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ImageInfo`
        """
        return self._ImageInfo

    @ImageInfo.setter
    def ImageInfo(self, ImageInfo):
        self._ImageInfo = ImageInfo

    @property
    def Env(self):
        r"""Environment variables.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of EnvVar
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Resources(self):
        r"""Resource information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def InstanceType(self):
        r"""Type specifications corresponding to the postpaid instance.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ModelInfo(self):
        r"""Model information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ModelInfo`
        """
        return self._ModelInfo

    @ModelInfo.setter
    def ModelInfo(self, ModelInfo):
        self._ModelInfo = ModelInfo

    @property
    def LogEnable(self):
        r"""Whether to enable logs.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._LogEnable

    @LogEnable.setter
    def LogEnable(self, LogEnable):
        self._LogEnable = LogEnable

    @property
    def LogConfig(self):
        r"""Log configurations.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.LogConfig`
        """
        return self._LogConfig

    @LogConfig.setter
    def LogConfig(self, LogConfig):
        self._LogConfig = LogConfig

    @property
    def AuthorizationEnable(self):
        r"""Whether to enable authentication.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._AuthorizationEnable

    @AuthorizationEnable.setter
    def AuthorizationEnable(self, AuthorizationEnable):
        self._AuthorizationEnable = AuthorizationEnable

    @property
    def HorizontalPodAutoscaler(self):
        r"""HPA configurations.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.HorizontalPodAutoscaler`
        """
        return self._HorizontalPodAutoscaler

    @HorizontalPodAutoscaler.setter
    def HorizontalPodAutoscaler(self, HorizontalPodAutoscaler):
        self._HorizontalPodAutoscaler = HorizontalPodAutoscaler

    @property
    def Status(self):
        r"""Description of the service status.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.WorkloadStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        r"""Weight.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def ResourceTotal(self):
        r"""Total resources.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ResourceInfo`
        """
        return self._ResourceTotal

    @ResourceTotal.setter
    def ResourceTotal(self, ResourceTotal):
        self._ResourceTotal = ResourceTotal

    @property
    def OldReplicas(self):
        r"""Number of historical instances.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OldReplicas

    @OldReplicas.setter
    def OldReplicas(self, OldReplicas):
        self._OldReplicas = OldReplicas

    @property
    def HybridBillingPrepaidReplicas(self):
        r"""This parameter is valid when the billing mode is HYBRID_PAID, and is used to identify the number of prepaid instances in the hybrid billing mode. The default value is 1 if this parameter is left unspecified.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._HybridBillingPrepaidReplicas

    @HybridBillingPrepaidReplicas.setter
    def HybridBillingPrepaidReplicas(self, HybridBillingPrepaidReplicas):
        self._HybridBillingPrepaidReplicas = HybridBillingPrepaidReplicas

    @property
    def OldHybridBillingPrepaidReplicas(self):
        r"""Number of instances during the historical HYBRID_PAID period. The user restores services.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._OldHybridBillingPrepaidReplicas

    @OldHybridBillingPrepaidReplicas.setter
    def OldHybridBillingPrepaidReplicas(self, OldHybridBillingPrepaidReplicas):
        self._OldHybridBillingPrepaidReplicas = OldHybridBillingPrepaidReplicas

    @property
    def ModelHotUpdateEnable(self):
        r"""Whether to enable hot update for the model. By default, hot update is disabled.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ModelHotUpdateEnable

    @ModelHotUpdateEnable.setter
    def ModelHotUpdateEnable(self, ModelHotUpdateEnable):
        self._ModelHotUpdateEnable = ModelHotUpdateEnable

    @property
    def InstanceAlias(self):
        r"""Service specification alias.
        :rtype: str
        """
        return self._InstanceAlias

    @InstanceAlias.setter
    def InstanceAlias(self, InstanceAlias):
        self._InstanceAlias = InstanceAlias

    @property
    def ScaleMode(self):
        r"""Instance quantity adjusting mode. Defaults to manual.Supported valid values: AUTO (automatic), MANUAL (manual).Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ScaleMode

    @ScaleMode.setter
    def ScaleMode(self, ScaleMode):
        self._ScaleMode = ScaleMode

    @property
    def CronScaleJobs(self):
        r"""Scheduled scaling task.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of CronScaleJob
        """
        return self._CronScaleJobs

    @CronScaleJobs.setter
    def CronScaleJobs(self, CronScaleJobs):
        self._CronScaleJobs = CronScaleJobs

    @property
    def ScaleStrategy(self):
        r"""Scheduled scaling policy.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ScaleStrategy

    @ScaleStrategy.setter
    def ScaleStrategy(self, ScaleStrategy):
        self._ScaleStrategy = ScaleStrategy

    @property
    def ScheduledAction(self):
        r"""Configurations of the scheduled stop.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ScheduledAction`
        """
        return self._ScheduledAction

    @ScheduledAction.setter
    def ScheduledAction(self, ScheduledAction):
        self._ScheduledAction = ScheduledAction

    @property
    def PodList(self):
        warnings.warn("parameter `PodList` is deprecated", DeprecationWarning) 

        r"""Instance list.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._PodList

    @PodList.setter
    def PodList(self, PodList):
        warnings.warn("parameter `PodList` is deprecated", DeprecationWarning) 

        self._PodList = PodList

    @property
    def Pods(self):
        warnings.warn("parameter `Pods` is deprecated", DeprecationWarning) 

        r"""Pod list information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.Pod`
        """
        return self._Pods

    @Pods.setter
    def Pods(self, Pods):
        warnings.warn("parameter `Pods` is deprecated", DeprecationWarning) 

        self._Pods = Pods

    @property
    def PodInfos(self):
        r"""Pod list information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Pod
        """
        return self._PodInfos

    @PodInfos.setter
    def PodInfos(self, PodInfos):
        self._PodInfos = PodInfos

    @property
    def ServiceLimit(self):
        r"""Configurations related to speed limit and throttling of services.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ServiceLimit`
        """
        return self._ServiceLimit

    @ServiceLimit.setter
    def ServiceLimit(self, ServiceLimit):
        self._ServiceLimit = ServiceLimit

    @property
    def ModelTurboEnable(self):
        r"""Whether to enable model acceleration, which is only valid for models in the StableDiffusion (dynamic acceleration) format.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: bool
        """
        return self._ModelTurboEnable

    @ModelTurboEnable.setter
    def ModelTurboEnable(self, ModelTurboEnable):
        self._ModelTurboEnable = ModelTurboEnable

    @property
    def VolumeMount(self):
        r"""Mounting.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.VolumeMount`
        """
        return self._VolumeMount

    @VolumeMount.setter
    def VolumeMount(self, VolumeMount):
        self._VolumeMount = VolumeMount

    @property
    def InferCodeInfo(self):
        r"""Inference code information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.InferCodeInfo`
        """
        return self._InferCodeInfo

    @InferCodeInfo.setter
    def InferCodeInfo(self, InferCodeInfo):
        self._InferCodeInfo = InferCodeInfo

    @property
    def Command(self):
        r"""Service startup command.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ServiceEIP(self):
        r"""Settings of enabling the TI-ONE private network to access external resources.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.tione.v20211111.models.ServiceEIP`
        """
        return self._ServiceEIP

    @ServiceEIP.setter
    def ServiceEIP(self, ServiceEIP):
        self._ServiceEIP = ServiceEIP

    @property
    def ServicePort(self):
        r"""Service port, with the default value of 8501.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ServicePort

    @ServicePort.setter
    def ServicePort(self, ServicePort):
        self._ServicePort = ServicePort

    @property
    def TerminationGracePeriodSeconds(self):
        r"""Graceful exit time limit of the service, in seconds. Default value: 30. Minimum value: 1.
        :rtype: int
        """
        return self._TerminationGracePeriodSeconds

    @TerminationGracePeriodSeconds.setter
    def TerminationGracePeriodSeconds(self, TerminationGracePeriodSeconds):
        self._TerminationGracePeriodSeconds = TerminationGracePeriodSeconds

    @property
    def PreStopCommand(self):
        r"""Command executed before the service instance stops. The instance ends after the command execution is completed or after the execution time exceeds the graceful exit time limit.
        :rtype: list of str
        """
        return self._PreStopCommand

    @PreStopCommand.setter
    def PreStopCommand(self, PreStopCommand):
        self._PreStopCommand = PreStopCommand

    @property
    def GrpcEnable(self):
        r"""Whether to enable the gRPC port.
        :rtype: bool
        """
        return self._GrpcEnable

    @GrpcEnable.setter
    def GrpcEnable(self, GrpcEnable):
        self._GrpcEnable = GrpcEnable

    @property
    def HealthProbe(self):
        r"""Health probe.
        :rtype: :class:`tencentcloud.tione.v20211111.models.HealthProbe`
        """
        return self._HealthProbe

    @HealthProbe.setter
    def HealthProbe(self, HealthProbe):
        self._HealthProbe = HealthProbe

    @property
    def RollingUpdate(self):
        r"""Rolling update configurations.
        :rtype: :class:`tencentcloud.tione.v20211111.models.RollingUpdate`
        """
        return self._RollingUpdate

    @RollingUpdate.setter
    def RollingUpdate(self, RollingUpdate):
        self._RollingUpdate = RollingUpdate

    @property
    def InstancePerReplicas(self):
        r"""Number of instances per replica. This parameter is valid only when the deployment type is DIST or ROLE. Default value: 1.
        :rtype: int
        """
        return self._InstancePerReplicas

    @InstancePerReplicas.setter
    def InstancePerReplicas(self, InstancePerReplicas):
        self._InstancePerReplicas = InstancePerReplicas

    @property
    def VolumeMounts(self):
        r"""Batch data disk mounting configurations.
        :rtype: list of VolumeMount
        """
        return self._VolumeMounts

    @VolumeMounts.setter
    def VolumeMounts(self, VolumeMounts):
        self._VolumeMounts = VolumeMounts


    def _deserialize(self, params):
        self._Replicas = params.get("Replicas")
        if params.get("ImageInfo") is not None:
            self._ImageInfo = ImageInfo()
            self._ImageInfo._deserialize(params.get("ImageInfo"))
        if params.get("Env") is not None:
            self._Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self._Env.append(obj)
        if params.get("Resources") is not None:
            self._Resources = ResourceInfo()
            self._Resources._deserialize(params.get("Resources"))
        self._InstanceType = params.get("InstanceType")
        if params.get("ModelInfo") is not None:
            self._ModelInfo = ModelInfo()
            self._ModelInfo._deserialize(params.get("ModelInfo"))
        self._LogEnable = params.get("LogEnable")
        if params.get("LogConfig") is not None:
            self._LogConfig = LogConfig()
            self._LogConfig._deserialize(params.get("LogConfig"))
        self._AuthorizationEnable = params.get("AuthorizationEnable")
        if params.get("HorizontalPodAutoscaler") is not None:
            self._HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self._HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("Status") is not None:
            self._Status = WorkloadStatus()
            self._Status._deserialize(params.get("Status"))
        self._Weight = params.get("Weight")
        if params.get("ResourceTotal") is not None:
            self._ResourceTotal = ResourceInfo()
            self._ResourceTotal._deserialize(params.get("ResourceTotal"))
        self._OldReplicas = params.get("OldReplicas")
        self._HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
        self._OldHybridBillingPrepaidReplicas = params.get("OldHybridBillingPrepaidReplicas")
        self._ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
        self._InstanceAlias = params.get("InstanceAlias")
        self._ScaleMode = params.get("ScaleMode")
        if params.get("CronScaleJobs") is not None:
            self._CronScaleJobs = []
            for item in params.get("CronScaleJobs"):
                obj = CronScaleJob()
                obj._deserialize(item)
                self._CronScaleJobs.append(obj)
        self._ScaleStrategy = params.get("ScaleStrategy")
        if params.get("ScheduledAction") is not None:
            self._ScheduledAction = ScheduledAction()
            self._ScheduledAction._deserialize(params.get("ScheduledAction"))
        self._PodList = params.get("PodList")
        if params.get("Pods") is not None:
            self._Pods = Pod()
            self._Pods._deserialize(params.get("Pods"))
        if params.get("PodInfos") is not None:
            self._PodInfos = []
            for item in params.get("PodInfos"):
                obj = Pod()
                obj._deserialize(item)
                self._PodInfos.append(obj)
        if params.get("ServiceLimit") is not None:
            self._ServiceLimit = ServiceLimit()
            self._ServiceLimit._deserialize(params.get("ServiceLimit"))
        self._ModelTurboEnable = params.get("ModelTurboEnable")
        if params.get("VolumeMount") is not None:
            self._VolumeMount = VolumeMount()
            self._VolumeMount._deserialize(params.get("VolumeMount"))
        if params.get("InferCodeInfo") is not None:
            self._InferCodeInfo = InferCodeInfo()
            self._InferCodeInfo._deserialize(params.get("InferCodeInfo"))
        self._Command = params.get("Command")
        if params.get("ServiceEIP") is not None:
            self._ServiceEIP = ServiceEIP()
            self._ServiceEIP._deserialize(params.get("ServiceEIP"))
        self._ServicePort = params.get("ServicePort")
        self._TerminationGracePeriodSeconds = params.get("TerminationGracePeriodSeconds")
        self._PreStopCommand = params.get("PreStopCommand")
        self._GrpcEnable = params.get("GrpcEnable")
        if params.get("HealthProbe") is not None:
            self._HealthProbe = HealthProbe()
            self._HealthProbe._deserialize(params.get("HealthProbe"))
        if params.get("RollingUpdate") is not None:
            self._RollingUpdate = RollingUpdate()
            self._RollingUpdate._deserialize(params.get("RollingUpdate"))
        self._InstancePerReplicas = params.get("InstancePerReplicas")
        if params.get("VolumeMounts") is not None:
            self._VolumeMounts = []
            for item in params.get("VolumeMounts"):
                obj = VolumeMount()
                obj._deserialize(item)
                self._VolumeMounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceLimit(AbstractModel):
    r"""Configurations related to throttling and speed limit of services.

    """

    def __init__(self):
        r"""
        :param _EnableInstanceRpsLimit: Whether to enable throttling and speed limit at the instance level. Valid values: true and false. If the value is true, InstanceRpsLimit is required. If the value is false, InstanceRpsLimit does not take effect.
        :type EnableInstanceRpsLimit: bool
        :param _InstanceRpsLimit: Speed limit for the requests per second (RPS) of each service instance. 0 indicates no throttling.
        :type InstanceRpsLimit: int
        :param _EnableInstanceReqLimit: Whether to enable the maximum concurrency quantity limit for a single instance. Valid values: true and false. If the value is true, InstanceReqLimit is required. If the value is false, InstanceReqLimit does not take effect.
        :type EnableInstanceReqLimit: bool
        :param _InstanceReqLimit: Maximum concurrency for each service instance.
        :type InstanceReqLimit: int
        """
        self._EnableInstanceRpsLimit = None
        self._InstanceRpsLimit = None
        self._EnableInstanceReqLimit = None
        self._InstanceReqLimit = None

    @property
    def EnableInstanceRpsLimit(self):
        r"""Whether to enable throttling and speed limit at the instance level. Valid values: true and false. If the value is true, InstanceRpsLimit is required. If the value is false, InstanceRpsLimit does not take effect.
        :rtype: bool
        """
        return self._EnableInstanceRpsLimit

    @EnableInstanceRpsLimit.setter
    def EnableInstanceRpsLimit(self, EnableInstanceRpsLimit):
        self._EnableInstanceRpsLimit = EnableInstanceRpsLimit

    @property
    def InstanceRpsLimit(self):
        r"""Speed limit for the requests per second (RPS) of each service instance. 0 indicates no throttling.
        :rtype: int
        """
        return self._InstanceRpsLimit

    @InstanceRpsLimit.setter
    def InstanceRpsLimit(self, InstanceRpsLimit):
        self._InstanceRpsLimit = InstanceRpsLimit

    @property
    def EnableInstanceReqLimit(self):
        r"""Whether to enable the maximum concurrency quantity limit for a single instance. Valid values: true and false. If the value is true, InstanceReqLimit is required. If the value is false, InstanceReqLimit does not take effect.
        :rtype: bool
        """
        return self._EnableInstanceReqLimit

    @EnableInstanceReqLimit.setter
    def EnableInstanceReqLimit(self, EnableInstanceReqLimit):
        self._EnableInstanceReqLimit = EnableInstanceReqLimit

    @property
    def InstanceReqLimit(self):
        r"""Maximum concurrency for each service instance.
        :rtype: int
        """
        return self._InstanceReqLimit

    @InstanceReqLimit.setter
    def InstanceReqLimit(self, InstanceReqLimit):
        self._InstanceReqLimit = InstanceReqLimit


    def _deserialize(self, params):
        self._EnableInstanceRpsLimit = params.get("EnableInstanceRpsLimit")
        self._InstanceRpsLimit = params.get("InstanceRpsLimit")
        self._EnableInstanceReqLimit = params.get("EnableInstanceReqLimit")
        self._InstanceReqLimit = params.get("InstanceReqLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCmdInfo(AbstractModel):
    r"""Startup command information.

    """

    def __init__(self):
        r"""
        :param _StartCmd: Startup command.
        :type StartCmd: str
        :param _PsStartCmd: Startup command for ps nodes.
        :type PsStartCmd: str
        :param _WorkerStartCmd: Startup command for Worker nodes.
        :type WorkerStartCmd: str
        """
        self._StartCmd = None
        self._PsStartCmd = None
        self._WorkerStartCmd = None

    @property
    def StartCmd(self):
        r"""Startup command.
        :rtype: str
        """
        return self._StartCmd

    @StartCmd.setter
    def StartCmd(self, StartCmd):
        self._StartCmd = StartCmd

    @property
    def PsStartCmd(self):
        r"""Startup command for ps nodes.
        :rtype: str
        """
        return self._PsStartCmd

    @PsStartCmd.setter
    def PsStartCmd(self, PsStartCmd):
        self._PsStartCmd = PsStartCmd

    @property
    def WorkerStartCmd(self):
        r"""Startup command for Worker nodes.
        :rtype: str
        """
        return self._WorkerStartCmd

    @WorkerStartCmd.setter
    def WorkerStartCmd(self, WorkerStartCmd):
        self._WorkerStartCmd = WorkerStartCmd


    def _deserialize(self, params):
        self._StartCmd = params.get("StartCmd")
        self._PsStartCmd = params.get("PsStartCmd")
        self._WorkerStartCmd = params.get("WorkerStartCmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatefulSetCondition(AbstractModel):
    r"""Instance status.

    """

    def __init__(self):
        r"""
        :param _Message: Information.Note: This field may return null, indicating that no valid values can be obtained.
        :type Message: str
        :param _Reason: Reason.Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        :param _Status: Status of the condition, True, False or Unknown.Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param _Type: Type.Note: This field may return null, indicating that no valid values can be obtained.
        :type Type: str
        :param _LastTransitionTime: Last update time.Note: This field may return null, indicating that no valid values can be obtained.
        :type LastTransitionTime: str
        :param _LastUpdateTime: Last update time.Note: This field may return null, indicating that no valid values can be obtained.
        :type LastUpdateTime: str
        """
        self._Message = None
        self._Reason = None
        self._Status = None
        self._Type = None
        self._LastTransitionTime = None
        self._LastUpdateTime = None

    @property
    def Message(self):
        r"""Information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Reason(self):
        r"""Reason.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Status(self):
        r"""Status of the condition, True, False or Unknown.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""Type.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def LastTransitionTime(self):
        r"""Last update time.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastTransitionTime

    @LastTransitionTime.setter
    def LastTransitionTime(self, LastTransitionTime):
        self._LastTransitionTime = LastTransitionTime

    @property
    def LastUpdateTime(self):
        r"""Last update time.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Reason = params.get("Reason")
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._LastTransitionTime = params.get("LastTransitionTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCPSocketAction(AbstractModel):
    r"""Check action of a TCP Socket health probe.

    """

    def __init__(self):
        r"""
        :param _Port: Called port.
        :type Port: int
        """
        self._Port = None

    @property
    def Port(self):
        r"""Called port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""Tencent Cloud tag description.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.Note: This field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value.Note: This field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""Tag key.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""Tag value.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        


class TagFilter(AbstractModel):
    r"""Tag filtering parameters.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
        :type TagKey: str
        :param _TagValues: Multiple tag values.
        :type TagValues: list of str
        """
        self._TagKey = None
        self._TagValues = None

    @property
    def TagKey(self):
        r"""Tag key.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
        r"""Multiple tag values.
        :rtype: list of str
        """
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrainToolConfig(AbstractModel):
    r"""

    """

    def __init__(self):
        r"""
        :param _EnableHangMonitor: 
        :type EnableHangMonitor: bool
        :param _HangMonitorNodes: 
        :type HangMonitorNodes: list of str
        :param _LogHangTimeoutInMinute: 
        :type LogHangTimeoutInMinute: int
        """
        self._EnableHangMonitor = None
        self._HangMonitorNodes = None
        self._LogHangTimeoutInMinute = None

    @property
    def EnableHangMonitor(self):
        r"""
        :rtype: bool
        """
        return self._EnableHangMonitor

    @EnableHangMonitor.setter
    def EnableHangMonitor(self, EnableHangMonitor):
        self._EnableHangMonitor = EnableHangMonitor

    @property
    def HangMonitorNodes(self):
        r"""
        :rtype: list of str
        """
        return self._HangMonitorNodes

    @HangMonitorNodes.setter
    def HangMonitorNodes(self, HangMonitorNodes):
        self._HangMonitorNodes = HangMonitorNodes

    @property
    def LogHangTimeoutInMinute(self):
        r"""
        :rtype: int
        """
        return self._LogHangTimeoutInMinute

    @LogHangTimeoutInMinute.setter
    def LogHangTimeoutInMinute(self, LogHangTimeoutInMinute):
        self._LogHangTimeoutInMinute = LogHangTimeoutInMinute


    def _deserialize(self, params):
        self._EnableHangMonitor = params.get("EnableHangMonitor")
        self._HangMonitorNodes = params.get("HangMonitorNodes")
        self._LogHangTimeoutInMinute = params.get("LogHangTimeoutInMinute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeMount(AbstractModel):
    r"""External mounting information.

    """

    def __init__(self):
        r"""
        :param _CFSConfig: Cloud File Storage (CFS) configuration information.
        :type CFSConfig: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        :param _VolumeSourceType: Mounting source type. Valid values: CFS and COS. The default value is CFS.
        :type VolumeSourceType: str
        :param _MountPath: Mounting path in the custom container.Note: This field may return null, indicating that no valid values can be obtained.
        :type MountPath: str
        """
        self._CFSConfig = None
        self._VolumeSourceType = None
        self._MountPath = None

    @property
    def CFSConfig(self):
        r"""Cloud File Storage (CFS) configuration information.
        :rtype: :class:`tencentcloud.tione.v20211111.models.CFSConfig`
        """
        return self._CFSConfig

    @CFSConfig.setter
    def CFSConfig(self, CFSConfig):
        self._CFSConfig = CFSConfig

    @property
    def VolumeSourceType(self):
        r"""Mounting source type. Valid values: CFS and COS. The default value is CFS.
        :rtype: str
        """
        return self._VolumeSourceType

    @VolumeSourceType.setter
    def VolumeSourceType(self, VolumeSourceType):
        self._VolumeSourceType = VolumeSourceType

    @property
    def MountPath(self):
        r"""Mounting path in the custom container.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath


    def _deserialize(self, params):
        if params.get("CFSConfig") is not None:
            self._CFSConfig = CFSConfig()
            self._CFSConfig._deserialize(params.get("CFSConfig"))
        self._VolumeSourceType = params.get("VolumeSourceType")
        self._MountPath = params.get("MountPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadStatus(AbstractModel):
    r"""Workload status.

    """

    def __init__(self):
        r"""
        :param _Replicas: Number of current instances.
        :type Replicas: int
        :param _UpdatedReplicas: Number of updated instances.
        :type UpdatedReplicas: int
        :param _ReadyReplicas: Number of ready instances.
        :type ReadyReplicas: int
        :param _AvailableReplicas: Number of available instances.
        :type AvailableReplicas: int
        :param _UnavailableReplicas: Number of unavailable instances.
        :type UnavailableReplicas: int
        :param _Status: Normal: running.Abnormal: service abnormalities, such as container startup failure.Waiting: service waiting, such as container image pulling.Stopped: stopped.Pending: starting.Stopping: stopping.
        :type Status: str
        :param _StatefulSetCondition: Workload status information.
        :type StatefulSetCondition: list of StatefulSetCondition
        :param _Conditions: Status information of workload history.
        :type Conditions: list of StatefulSetCondition
        :param _Reason: Display the reason when the status is abnormal.Note: This field may return null, indicating that no valid values can be obtained.
        :type Reason: str
        """
        self._Replicas = None
        self._UpdatedReplicas = None
        self._ReadyReplicas = None
        self._AvailableReplicas = None
        self._UnavailableReplicas = None
        self._Status = None
        self._StatefulSetCondition = None
        self._Conditions = None
        self._Reason = None

    @property
    def Replicas(self):
        r"""Number of current instances.
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def UpdatedReplicas(self):
        r"""Number of updated instances.
        :rtype: int
        """
        return self._UpdatedReplicas

    @UpdatedReplicas.setter
    def UpdatedReplicas(self, UpdatedReplicas):
        self._UpdatedReplicas = UpdatedReplicas

    @property
    def ReadyReplicas(self):
        r"""Number of ready instances.
        :rtype: int
        """
        return self._ReadyReplicas

    @ReadyReplicas.setter
    def ReadyReplicas(self, ReadyReplicas):
        self._ReadyReplicas = ReadyReplicas

    @property
    def AvailableReplicas(self):
        r"""Number of available instances.
        :rtype: int
        """
        return self._AvailableReplicas

    @AvailableReplicas.setter
    def AvailableReplicas(self, AvailableReplicas):
        self._AvailableReplicas = AvailableReplicas

    @property
    def UnavailableReplicas(self):
        r"""Number of unavailable instances.
        :rtype: int
        """
        return self._UnavailableReplicas

    @UnavailableReplicas.setter
    def UnavailableReplicas(self, UnavailableReplicas):
        self._UnavailableReplicas = UnavailableReplicas

    @property
    def Status(self):
        r"""Normal: running.Abnormal: service abnormalities, such as container startup failure.Waiting: service waiting, such as container image pulling.Stopped: stopped.Pending: starting.Stopping: stopping.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatefulSetCondition(self):
        warnings.warn("parameter `StatefulSetCondition` is deprecated", DeprecationWarning) 

        r"""Workload status information.
        :rtype: list of StatefulSetCondition
        """
        return self._StatefulSetCondition

    @StatefulSetCondition.setter
    def StatefulSetCondition(self, StatefulSetCondition):
        warnings.warn("parameter `StatefulSetCondition` is deprecated", DeprecationWarning) 

        self._StatefulSetCondition = StatefulSetCondition

    @property
    def Conditions(self):
        r"""Status information of workload history.
        :rtype: list of StatefulSetCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Reason(self):
        r"""Display the reason when the status is abnormal.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Replicas = params.get("Replicas")
        self._UpdatedReplicas = params.get("UpdatedReplicas")
        self._ReadyReplicas = params.get("ReadyReplicas")
        self._AvailableReplicas = params.get("AvailableReplicas")
        self._UnavailableReplicas = params.get("UnavailableReplicas")
        self._Status = params.get("Status")
        if params.get("StatefulSetCondition") is not None:
            self._StatefulSetCondition = []
            for item in params.get("StatefulSetCondition"):
                obj = StatefulSetCondition()
                obj._deserialize(item)
                self._StatefulSetCondition.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = StatefulSetCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        