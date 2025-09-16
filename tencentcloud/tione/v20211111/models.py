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
        r"""Service classification.
        :rtype: str
        """
        return self._ServiceCategory

    @ServiceCategory.setter
    def ServiceCategory(self, ServiceCategory):
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
        """
        self._ImageType = None
        self._ImageUrl = None
        self._RegistryRegion = None
        self._RegistryId = None
        self._AllowSaveAllContent = None
        self._ImageName = None
        self._SupportDataPipeline = None

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


    def _deserialize(self, params):
        self._ImageType = params.get("ImageType")
        self._ImageUrl = params.get("ImageUrl")
        self._RegistryRegion = params.get("RegistryRegion")
        self._RegistryId = params.get("RegistryId")
        self._AllowSaveAllContent = params.get("AllowSaveAllContent")
        self._ImageName = params.get("ImageName")
        self._SupportDataPipeline = params.get("SupportDataPipeline")
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
        :param _GooseFSx: GooseFSx configurations, and is valid when ModelSource is GooseFSx.
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
        r"""GooseFSx configurations, and is valid when ModelSource is GooseFSx.
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
        """
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._GpuType = None
        self._RealGpu = None
        self._RealGpuDetailSet = None

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
        