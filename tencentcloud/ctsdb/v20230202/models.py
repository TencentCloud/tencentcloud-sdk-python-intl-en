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


class Cluster(AbstractModel):
    """Instance-related information.

    """

    def __init__(self):
        r"""
        :param _AppID: User APP ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :type AppID: int
        :param _ClusterID: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterID: str
        :param _AccountID: Account ID.Note: This field may return null, indicating that no valid values can be obtained.
        :type AccountID: str
        :param _Name: Customizes the instance name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _Region: Region.Note: This field may return null, indicating that no valid values can be obtained.
        :type Region: str
        :param _Zones: Availability zone.Note: This field may return null, indicating that no valid values can be obtained.
        :type Zones: str
        :param _Networks: Network information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Networks: list of Network
        :param _Spec: Instance specification.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Spec: :class:`tencentcloud.ctsdb.v20230202.models.Spec`
        :param _Status: Instance status. 0: running; 1: creating; 16: adjusting configuration; 17: isolating; 18: to be terminated; 19: recovering; 20: shutting down; 21: terminating; 22: terminated.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _Period: Instance validity period.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Period: :class:`tencentcloud.ctsdb.v20230202.models.Period`
        :param _CreatedAt: Creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _UpdatedAt: Last modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        :param _Tenant: Internal features of the product.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tenant: :class:`tencentcloud.ctsdb.v20230202.models.Tenant`
        :param _Tags: Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Security: Security group information.Note: This field may return null, indicating that no valid values can be obtained.
        :type Security: list of str
        """
        self._AppID = None
        self._ClusterID = None
        self._AccountID = None
        self._Name = None
        self._Region = None
        self._Zones = None
        self._Networks = None
        self._Spec = None
        self._Status = None
        self._Period = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Tenant = None
        self._Tags = None
        self._Security = None

    @property
    def AppID(self):
        """User APP ID.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._AppID

    @AppID.setter
    def AppID(self, AppID):
        self._AppID = AppID

    @property
    def ClusterID(self):
        """Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def AccountID(self):
        """Account ID.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccountID

    @AccountID.setter
    def AccountID(self, AccountID):
        self._AccountID = AccountID

    @property
    def Name(self):
        """Customizes the instance name.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        """Region.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zones(self):
        """Availability zone.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def Networks(self):
        warnings.warn("parameter `Networks` is deprecated", DeprecationWarning) 

        """Network information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Network
        """
        return self._Networks

    @Networks.setter
    def Networks(self, Networks):
        warnings.warn("parameter `Networks` is deprecated", DeprecationWarning) 

        self._Networks = Networks

    @property
    def Spec(self):
        warnings.warn("parameter `Spec` is deprecated", DeprecationWarning) 

        """Instance specification.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Spec`
        """
        return self._Spec

    @Spec.setter
    def Spec(self, Spec):
        warnings.warn("parameter `Spec` is deprecated", DeprecationWarning) 

        self._Spec = Spec

    @property
    def Status(self):
        """Instance status. 0: running; 1: creating; 16: adjusting configuration; 17: isolating; 18: to be terminated; 19: recovering; 20: shutting down; 21: terminating; 22: terminated.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Period(self):
        """Instance validity period.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Period`
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def CreatedAt(self):
        """Creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        """Last modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Tenant(self):
        """Internal features of the product.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Tenant`
        """
        return self._Tenant

    @Tenant.setter
    def Tenant(self, Tenant):
        self._Tenant = Tenant

    @property
    def Tags(self):
        """Tag.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Security(self):
        """Security group information.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Security

    @Security.setter
    def Security(self, Security):
        self._Security = Security


    def _deserialize(self, params):
        self._AppID = params.get("AppID")
        self._ClusterID = params.get("ClusterID")
        self._AccountID = params.get("AccountID")
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        self._Zones = params.get("Zones")
        if params.get("Networks") is not None:
            self._Networks = []
            for item in params.get("Networks"):
                obj = Network()
                obj._deserialize(item)
                self._Networks.append(obj)
        if params.get("Spec") is not None:
            self._Spec = Spec()
            self._Spec._deserialize(params.get("Spec"))
        self._Status = params.get("Status")
        if params.get("Period") is not None:
            self._Period = Period()
            self._Period._deserialize(params.get("Period"))
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("Tenant") is not None:
            self._Tenant = Tenant()
            self._Tenant._deserialize(params.get("Tenant"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Security = params.get("Security")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Database(AbstractModel):
    """Database-related information.

    """

    def __init__(self):
        r"""
        :param _ClusterID: Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterID: str
        :param _Name: Database name.Note: This field may return null, indicating that no valid values can be obtained.
        :type Name: str
        :param _CoolDownInDays: Cold storage time (days).
Note: This field may return null, indicating that no valid values can be obtained.
        :type CoolDownInDays: int
        :param _RetentionInDays: Data retention time (days).
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetentionInDays: int
        :param _Remark: Remarks.Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _Status: Status. 0: initializing resources; 1: creating resources; 2: normal status; 3: deleting resources; 4: deleted resources; 5: disabling resources; 6: disabled resources; 7: abnormal resources, and manual operation is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _CreatedAt: Creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedAt: str
        :param _UpdatedAt: Last modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdatedAt: str
        """
        self._ClusterID = None
        self._Name = None
        self._CoolDownInDays = None
        self._RetentionInDays = None
        self._Remark = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def ClusterID(self):
        """Instance ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ClusterID

    @ClusterID.setter
    def ClusterID(self, ClusterID):
        self._ClusterID = ClusterID

    @property
    def Name(self):
        """Database name.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CoolDownInDays(self):
        """Cold storage time (days).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CoolDownInDays

    @CoolDownInDays.setter
    def CoolDownInDays(self, CoolDownInDays):
        self._CoolDownInDays = CoolDownInDays

    @property
    def RetentionInDays(self):
        """Data retention time (days).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RetentionInDays

    @RetentionInDays.setter
    def RetentionInDays(self, RetentionInDays):
        self._RetentionInDays = RetentionInDays

    @property
    def Remark(self):
        """Remarks.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Status(self):
        """Status. 0: initializing resources; 1: creating resources; 2: normal status; 3: deleting resources; 4: deleted resources; 5: disabling resources; 6: disabled resources; 7: abnormal resources, and manual operation is required.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        """Creation time.Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        """Last modification time.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._ClusterID = params.get("ClusterID")
        self._Name = params.get("Name")
        self._CoolDownInDays = params.get("CoolDownInDays")
        self._RetentionInDays = params.get("RetentionInDays")
        self._Remark = params.get("Remark")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Current page number.		
        :type PageNumber: int
        :param _PageSize: Page size.
        :type PageSize: int
        :param _Filters: Query parameter: Filtering and querying by instance ID (cluster_id) and instance name (name) are supported.
        :type Filters: list of Filter
        :param _Orders: Sorting parameter: Sorting by the creation time field (created_at) is supported. The value of Type can be set to DESC (descending order) or ASC (ascending order).
        :type Orders: list of Order
        """
        self._PageNumber = None
        self._PageSize = None
        self._Filters = None
        self._Orders = None

    @property
    def PageNumber(self):
        """Current page number.		
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """Page size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Filters(self):
        """Query parameter: Filtering and querying by instance ID (cluster_id) and instance name (name) are supported.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Orders(self):
        """Sorting parameter: Sorting by the creation time field (created_at) is supported. The value of Type can be set to DESC (descending order) or ASC (ascending order).
        :rtype: list of Order
        """
        return self._Orders

    @Orders.setter
    def Orders(self, Orders):
        self._Orders = Orders


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Orders") is not None:
            self._Orders = []
            for item in params.get("Orders"):
                obj = Order()
                obj._deserialize(item)
                self._Orders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of records under current conditions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param _Clusters: List of instances meeting the conditions.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Clusters: list of Cluster
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Clusters = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of records under current conditions.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Clusters(self):
        """List of instances meeting the conditions.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of Cluster
        """
        return self._Clusters

    @Clusters.setter
    def Clusters(self, Clusters):
        self._Clusters = Clusters

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
        if params.get("Clusters") is not None:
            self._Clusters = []
            for item in params.get("Clusters"):
                obj = Cluster()
                obj._deserialize(item)
                self._Clusters.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases request structure.

    """

    def __init__(self):
        r"""
        :param _Database: Database parameter.
        :type Database: :class:`tencentcloud.ctsdb.v20230202.models.Database`
        :param _PageSize: Pagination size.
        :type PageSize: int
        :param _PageNumber: Pagination page.
        :type PageNumber: int
        """
        self._Database = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Database(self):
        """Database parameter.
        :rtype: :class:`tencentcloud.ctsdb.v20230202.models.Database`
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def PageSize(self):
        """Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        """Pagination page.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        if params.get("Database") is not None:
            self._Database = Database()
            self._Database._deserialize(params.get("Database"))
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases response structure.

    """

    def __init__(self):
        r"""
        :param _Databases: Database list.
        :type Databases: list of Database
        :param _TotalCount: Quantity.
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Databases = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Databases(self):
        """Database list.
        :rtype: list of Database
        """
        return self._Databases

    @Databases.setter
    def Databases(self, Databases):
        self._Databases = Databases

    @property
    def TotalCount(self):
        """Quantity.
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
        if params.get("Databases") is not None:
            self._Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self._Databases.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Query filter.

    """

    def __init__(self):
        r"""
        :param _Name: Filter parameter.
        :type Name: str
        :param _Op: Filter expression.
        :type Op: str
        :param _Values: Value involved in filtering.
        :type Values: list of str
        """
        self._Name = None
        self._Op = None
        self._Values = None

    @property
    def Name(self):
        """Filter parameter.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Op(self):
        """Filter expression.
        :rtype: str
        """
        return self._Op

    @Op.setter
    def Op(self, Op):
        self._Op = Op

    @property
    def Values(self):
        """Value involved in filtering.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Op = params.get("Op")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Network(AbstractModel):
    """Instance network information (influxdb).

    """

    def __init__(self):
        r"""
        :param _VpcId: vpc id
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: vpc subnet id
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _VIP: VPC IP address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VIP: str
        :param _Port: VPC port address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Port: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._VIP = None
        self._Port = None

    @property
    def VpcId(self):
        """vpc id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """vpc subnet id
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VIP(self):
        """VPC IP address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VIP

    @VIP.setter
    def VIP(self, VIP):
        self._VIP = VIP

    @property
    def Port(self):
        """VPC port address.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._VIP = params.get("VIP")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Order(AbstractModel):
    """Sorting parameter, which is used for sorting the query results.

    """

    def __init__(self):
        r"""
        :param _Name: Sorting field.
        :type Name: str
        :param _Type: Sorting method.
        :type Type: str
        """
        self._Name = None
        self._Type = None

    @property
    def Name(self):
        """Sorting field.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Sorting method.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Period(AbstractModel):
    """Validity period.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type StartTime: str
        :param _EndTime: End time.

Note: This field may return null, indicating that no valid values can be obtained.
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """Start time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time.

Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Spec(AbstractModel):
    """Instance specification information (influxdb).

    """

    def __init__(self):
        r"""
        :param _PayMode: 1: yearly/monthly subscription; 2: bill by hour.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PayMode: int
        :param _RequestUnit: Request unit. 0 indicates following the resource configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RequestUnit: int
        :param _CpuLimit: Maximum number of CPU cores.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CpuLimit: float
        :param _MemoryLimit: Maximum memory size (Gi).
Note: This field may return null, indicating that no valid values can be obtained.
        :type MemoryLimit: float
        :param _DiskLimit: Maximum number of disks (Gi).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskLimit: int
        :param _Shards: Number of business shards.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Shards: int
        :param _Replicas: Number of business nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Replicas: int
        """
        self._PayMode = None
        self._RequestUnit = None
        self._CpuLimit = None
        self._MemoryLimit = None
        self._DiskLimit = None
        self._Shards = None
        self._Replicas = None

    @property
    def PayMode(self):
        """1: yearly/monthly subscription; 2: bill by hour.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def RequestUnit(self):
        """Request unit. 0 indicates following the resource configuration.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RequestUnit

    @RequestUnit.setter
    def RequestUnit(self, RequestUnit):
        self._RequestUnit = RequestUnit

    @property
    def CpuLimit(self):
        """Maximum number of CPU cores.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._CpuLimit

    @CpuLimit.setter
    def CpuLimit(self, CpuLimit):
        self._CpuLimit = CpuLimit

    @property
    def MemoryLimit(self):
        """Maximum memory size (Gi).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: float
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def DiskLimit(self):
        """Maximum number of disks (Gi).
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._DiskLimit

    @DiskLimit.setter
    def DiskLimit(self, DiskLimit):
        self._DiskLimit = DiskLimit

    @property
    def Shards(self):
        """Number of business shards.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Shards

    @Shards.setter
    def Shards(self, Shards):
        self._Shards = Shards

    @property
    def Replicas(self):
        """Number of business nodes.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas


    def _deserialize(self, params):
        self._PayMode = params.get("PayMode")
        self._RequestUnit = params.get("RequestUnit")
        self._CpuLimit = params.get("CpuLimit")
        self._MemoryLimit = params.get("MemoryLimit")
        self._DiskLimit = params.get("DiskLimit")
        self._Shards = params.get("Shards")
        self._Replicas = params.get("Replicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag.

    """

    def __init__(self):
        r"""
        :param _Key: Key.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Key: str
        :param _Value: Value.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Key.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Value.
Note: This field may return null, indicating that no valid values can be obtained.
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
        


class Tenant(AbstractModel):
    """Internal features of the product.

    """

    def __init__(self):
        r"""
        :param _IsPasswordEncrypted: Whether the password is encrypted.
        :type IsPasswordEncrypted: bool
        """
        self._IsPasswordEncrypted = None

    @property
    def IsPasswordEncrypted(self):
        """Whether the password is encrypted.
        :rtype: bool
        """
        return self._IsPasswordEncrypted

    @IsPasswordEncrypted.setter
    def IsPasswordEncrypted(self, IsPasswordEncrypted):
        self._IsPasswordEncrypted = IsPasswordEncrypted


    def _deserialize(self, params):
        self._IsPasswordEncrypted = params.get("IsPasswordEncrypted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        