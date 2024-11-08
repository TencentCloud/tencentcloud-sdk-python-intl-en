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


class CreateLogExportRequest(AbstractModel):
    """CreateLogExport request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Project ID
        :type ID: int
        :param _StartTime: Log export start time
        :type StartTime: str
        :param _EndTime: Log export end time
        :type EndTime: str
        :param _Query: Log export search statement
        :type Query: str
        :param _Count: Number of logs to be exported. Maximum value: 10 million
        :type Count: int
        :param _Order: Exported log sorting order by time. Valid values: asc: ascending; desc: descending. Default value: desc
        :type Order: str
        :param _Format: Exported log data format. Valid values: json, csv. Default value: json
        :type Format: str
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None
        self._Query = None
        self._Count = None
        self._Order = None
        self._Format = None

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        """Log export start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Log export end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Query(self):
        """Log export search statement
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Count(self):
        """Number of logs to be exported. Maximum value: 10 million
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Order(self):
        """Exported log sorting order by time. Valid values: asc: ascending; desc: descending. Default value: desc
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Format(self):
        """Exported log data format. Valid values: json, csv. Default value: json
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Query = params.get("Query")
        self._Count = params.get("Count")
        self._Order = params.get("Order")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLogExportResponse(AbstractModel):
    """CreateLogExport response structure.

    """

    def __init__(self):
        r"""
        :param _ExportID: Log export ID
        :type ExportID: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ExportID = None
        self._RequestId = None

    @property
    def ExportID(self):
        """Log export ID
        :rtype: str
        """
        return self._ExportID

    @ExportID.setter
    def ExportID(self, ExportID):
        self._ExportID = ExportID

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
        self._ExportID = params.get("ExportID")
        self._RequestId = params.get("RequestId")


class CreateOfflineLogConfigRequest(AbstractModel):
    """CreateOfflineLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param _UniqueID: Unique identifier of the user to be listened on (`aid` or `uin`)
        :type UniqueID: str
        """
        self._ProjectKey = None
        self._UniqueID = None

    @property
    def ProjectKey(self):
        """Unique project key for reporting
        :rtype: str
        """
        return self._ProjectKey

    @ProjectKey.setter
    def ProjectKey(self, ProjectKey):
        self._ProjectKey = ProjectKey

    @property
    def UniqueID(self):
        """Unique identifier of the user to be listened on (`aid` or `uin`)
        :rtype: str
        """
        return self._UniqueID

    @UniqueID.setter
    def UniqueID(self, UniqueID):
        self._UniqueID = UniqueID


    def _deserialize(self, params):
        self._ProjectKey = params.get("ProjectKey")
        self._UniqueID = params.get("UniqueID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOfflineLogConfigResponse(AbstractModel):
    """CreateOfflineLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: API response information
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """API response information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Name of the created project (required and up to 200 characters)
        :type Name: str
        :param _InstanceID: Business system ID
        :type InstanceID: str
        :param _Rate: Project sampling rate (greater than or equal to 0)
        :type Rate: str
        :param _EnableURLGroup: Whether to enable aggregation
        :type EnableURLGroup: int
        :param _Type: Project type (valid values: "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param _Repo: Repository address of the project (optional and up to 256 characters)
        :type Repo: str
        :param _URL: Webpage address of the project (optional and up to 256 characters)
        :type URL: str
        :param _Desc: Description of the created project (optional and up to 1,000 characters)
        :type Desc: str
        """
        self._Name = None
        self._InstanceID = None
        self._Rate = None
        self._EnableURLGroup = None
        self._Type = None
        self._Repo = None
        self._URL = None
        self._Desc = None

    @property
    def Name(self):
        """Name of the created project (required and up to 200 characters)
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstanceID(self):
        """Business system ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Rate(self):
        """Project sampling rate (greater than or equal to 0)
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def EnableURLGroup(self):
        """Whether to enable aggregation
        :rtype: int
        """
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def Type(self):
        """Project type (valid values: "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Repo(self):
        """Repository address of the project (optional and up to 256 characters)
        :rtype: str
        """
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def URL(self):
        """Webpage address of the project (optional and up to 256 characters)
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Desc(self):
        """Description of the created project (optional and up to 1,000 characters)
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InstanceID = params.get("InstanceID")
        self._Rate = params.get("Rate")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._Type = params.get("Type")
        self._Repo = params.get("Repo")
        self._URL = params.get("URL")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProjectResponse(AbstractModel):
    """CreateProject response structure.

    """

    def __init__(self):
        r"""
        :param _ID: Project ID
        :type ID: int
        :param _Key: Unique project key
        :type Key: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ID = None
        self._Key = None
        self._RequestId = None

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Key(self):
        """Unique project key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

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
        self._ID = params.get("ID")
        self._Key = params.get("Key")
        self._RequestId = params.get("RequestId")


class CreateReleaseFileRequest(AbstractModel):
    """CreateReleaseFile request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectID: Project ID
        :type ProjectID: int
        :param _Files: File information list
        :type Files: list of ReleaseFile
        """
        self._ProjectID = None
        self._Files = None

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def Files(self):
        """File information list
        :rtype: list of ReleaseFile
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self._Files.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseFileResponse(AbstractModel):
    """CreateReleaseFile response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Call result
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """Call result
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateStarProjectRequest(AbstractModel):
    """CreateStarProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Instance ID, such as taw-123
        :type InstanceID: str
        :param _ID: Project ID
        :type ID: int
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        """Instance ID, such as taw-123
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStarProjectResponse(AbstractModel):
    """CreateStarProject response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: API response information
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """API response information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class CreateTawInstanceRequest(AbstractModel):
    """CreateTawInstance request structure.

    """

    def __init__(self):
        r"""
        :param _AreaId: Region ID (at least greater than 0)
        :type AreaId: int
        :param _ChargeType: Billing type (1: Pay-as-you-go).
        :type ChargeType: int
        :param _DataRetentionDays: Data retention period (at least greater than 0)
        :type DataRetentionDays: int
        :param _InstanceName: Instance name (up to 255 bytes)
        :type InstanceName: str
        :param _Tags: Tag list
        :type Tags: list of Tag
        :param _InstanceDesc: Instance description (up to 1,024 bytes)
        :type InstanceDesc: str
        :param _CountNum: Number of data entries reported per day
        :type CountNum: str
        :param _PeriodRetain: Billing for data storage
        :type PeriodRetain: str
        :param _BuyingChannel: Instance purchase channel. Valid value: `cdn`.
        :type BuyingChannel: str
        :param _ResourcePackageType: Type of prepaid resource pack (only required for prepaid mode)
        :type ResourcePackageType: int
        :param _ResourcePackageNum: The number of prepaid resource packs (only required for prepaid mode)
        :type ResourcePackageNum: int
        :param _InstanceType: Instance type. `1`: Web; `2`: Application
        :type InstanceType: int
        """
        self._AreaId = None
        self._ChargeType = None
        self._DataRetentionDays = None
        self._InstanceName = None
        self._Tags = None
        self._InstanceDesc = None
        self._CountNum = None
        self._PeriodRetain = None
        self._BuyingChannel = None
        self._ResourcePackageType = None
        self._ResourcePackageNum = None
        self._InstanceType = None

    @property
    def AreaId(self):
        """Region ID (at least greater than 0)
        :rtype: int
        """
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def ChargeType(self):
        """Billing type (1: Pay-as-you-go).
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def DataRetentionDays(self):
        """Data retention period (at least greater than 0)
        :rtype: int
        """
        return self._DataRetentionDays

    @DataRetentionDays.setter
    def DataRetentionDays(self, DataRetentionDays):
        self._DataRetentionDays = DataRetentionDays

    @property
    def InstanceName(self):
        """Instance name (up to 255 bytes)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Tags(self):
        """Tag list
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceDesc(self):
        """Instance description (up to 1,024 bytes)
        :rtype: str
        """
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc

    @property
    def CountNum(self):
        """Number of data entries reported per day
        :rtype: str
        """
        return self._CountNum

    @CountNum.setter
    def CountNum(self, CountNum):
        self._CountNum = CountNum

    @property
    def PeriodRetain(self):
        """Billing for data storage
        :rtype: str
        """
        return self._PeriodRetain

    @PeriodRetain.setter
    def PeriodRetain(self, PeriodRetain):
        self._PeriodRetain = PeriodRetain

    @property
    def BuyingChannel(self):
        """Instance purchase channel. Valid value: `cdn`.
        :rtype: str
        """
        return self._BuyingChannel

    @BuyingChannel.setter
    def BuyingChannel(self, BuyingChannel):
        self._BuyingChannel = BuyingChannel

    @property
    def ResourcePackageType(self):
        """Type of prepaid resource pack (only required for prepaid mode)
        :rtype: int
        """
        return self._ResourcePackageType

    @ResourcePackageType.setter
    def ResourcePackageType(self, ResourcePackageType):
        self._ResourcePackageType = ResourcePackageType

    @property
    def ResourcePackageNum(self):
        """The number of prepaid resource packs (only required for prepaid mode)
        :rtype: int
        """
        return self._ResourcePackageNum

    @ResourcePackageNum.setter
    def ResourcePackageNum(self, ResourcePackageNum):
        self._ResourcePackageNum = ResourcePackageNum

    @property
    def InstanceType(self):
        """Instance type. `1`: Web; `2`: Application
        :rtype: int
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        self._AreaId = params.get("AreaId")
        self._ChargeType = params.get("ChargeType")
        self._DataRetentionDays = params.get("DataRetentionDays")
        self._InstanceName = params.get("InstanceName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceDesc = params.get("InstanceDesc")
        self._CountNum = params.get("CountNum")
        self._PeriodRetain = params.get("PeriodRetain")
        self._BuyingChannel = params.get("BuyingChannel")
        self._ResourcePackageType = params.get("ResourcePackageType")
        self._ResourcePackageNum = params.get("ResourcePackageNum")
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTawInstanceResponse(AbstractModel):
    """CreateTawInstance response structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _DealName: ID of prepaid order
Note: This field may return null, indicating that no valid values can be obtained.
        :type DealName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._InstanceId = None
        self._DealName = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DealName(self):
        """ID of prepaid order
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

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
        self._InstanceId = params.get("InstanceId")
        self._DealName = params.get("DealName")
        self._RequestId = params.get("RequestId")


class CreateWhitelistRequest(AbstractModel):
    """CreateWhitelist request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Instance ID, such as taw-123
        :type InstanceID: str
        :param _Remark: Remarks
        :type Remark: str
        :param _WhitelistUin: uin: business identifier
        :type WhitelistUin: str
        :param _Aid: Business identifier
        :type Aid: str
        """
        self._InstanceID = None
        self._Remark = None
        self._WhitelistUin = None
        self._Aid = None

    @property
    def InstanceID(self):
        """Instance ID, such as taw-123
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def WhitelistUin(self):
        """uin: business identifier
        :rtype: str
        """
        return self._WhitelistUin

    @WhitelistUin.setter
    def WhitelistUin(self, WhitelistUin):
        self._WhitelistUin = WhitelistUin

    @property
    def Aid(self):
        """Business identifier
        :rtype: str
        """
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._Remark = params.get("Remark")
        self._WhitelistUin = params.get("WhitelistUin")
        self._Aid = params.get("Aid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhitelistResponse(AbstractModel):
    """CreateWhitelist response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Message
        :type Msg: str
        :param _ID: Allowlist ID
        :type ID: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._ID = None
        self._RequestId = None

    @property
    def Msg(self):
        """Message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def ID(self):
        """Allowlist ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

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
        self._Msg = params.get("Msg")
        self._ID = params.get("ID")
        self._RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be deleted
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ID of the instance to be deleted
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteLogExportRequest(AbstractModel):
    """DeleteLogExport request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Project ID
        :type ID: int
        :param _ExportID: Log export ID
        :type ExportID: str
        """
        self._ID = None
        self._ExportID = None

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExportID(self):
        """Log export ID
        :rtype: str
        """
        return self._ExportID

    @ExportID.setter
    def ExportID(self, ExportID):
        self._ExportID = ExportID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ExportID = params.get("ExportID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLogExportResponse(AbstractModel):
    """DeleteLogExport response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Whether it is successful. If so, `success` will be returned; otherwise, `Error` rather than this parameter will be returned
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """Whether it is successful. If so, `success` will be returned; otherwise, `Error` rather than this parameter will be returned
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteOfflineLogConfigRequest(AbstractModel):
    """DeleteOfflineLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param _UniqueID: Unique user identifier (uin or aid)
        :type UniqueID: str
        """
        self._ProjectKey = None
        self._UniqueID = None

    @property
    def ProjectKey(self):
        """Unique project key for reporting
        :rtype: str
        """
        return self._ProjectKey

    @ProjectKey.setter
    def ProjectKey(self, ProjectKey):
        self._ProjectKey = ProjectKey

    @property
    def UniqueID(self):
        """Unique user identifier (uin or aid)
        :rtype: str
        """
        return self._UniqueID

    @UniqueID.setter
    def UniqueID(self, UniqueID):
        self._UniqueID = UniqueID


    def _deserialize(self, params):
        self._ProjectKey = params.get("ProjectKey")
        self._UniqueID = params.get("UniqueID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOfflineLogConfigResponse(AbstractModel):
    """DeleteOfflineLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: API call information
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """API call information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteOfflineLogRecordRequest(AbstractModel):
    """DeleteOfflineLogRecord request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param _FileID: Offline log file ID
        :type FileID: str
        """
        self._ProjectKey = None
        self._FileID = None

    @property
    def ProjectKey(self):
        """Unique project key for reporting
        :rtype: str
        """
        return self._ProjectKey

    @ProjectKey.setter
    def ProjectKey(self, ProjectKey):
        self._ProjectKey = ProjectKey

    @property
    def FileID(self):
        """Offline log file ID
        :rtype: str
        """
        return self._FileID

    @FileID.setter
    def FileID(self, FileID):
        self._FileID = FileID


    def _deserialize(self, params):
        self._ProjectKey = params.get("ProjectKey")
        self._FileID = params.get("FileID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOfflineLogRecordResponse(AbstractModel):
    """DeleteOfflineLogRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: API call information
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """API call information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject request structure.

    """

    def __init__(self):
        r"""
        :param _ID: ID of the project to be deleted
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        """ID of the project to be deleted
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProjectResponse(AbstractModel):
    """DeleteProject response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Operation information
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """Operation information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteReleaseFileRequest(AbstractModel):
    """DeleteReleaseFile request structure.

    """

    def __init__(self):
        r"""
        :param _ID: File ID
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        """File ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReleaseFileResponse(AbstractModel):
    """DeleteReleaseFile response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Response string of the API request
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """Response string of the API request
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteStarProjectRequest(AbstractModel):
    """DeleteStarProject request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Instance ID, such as taw-123
        :type InstanceID: str
        :param _ID: Project ID
        :type ID: int
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        """Instance ID, such as taw-123
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStarProjectResponse(AbstractModel):
    """DeleteStarProject response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Response message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """Response message
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DeleteWhitelistRequest(AbstractModel):
    """DeleteWhitelist request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Instance ID
        :type InstanceID: str
        :param _ID: List ID
        :type ID: str
        """
        self._InstanceID = None
        self._ID = None

    @property
    def InstanceID(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def ID(self):
        """List ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhitelistResponse(AbstractModel):
    """DeleteWhitelist response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Success message
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """Success message
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class DescribeDataCustomUrlRequest(AbstractModel):
    """DescribeDataCustomUrl request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `top`: top resources view; `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `pagepv`: PV view; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation method
        :type CostType: str
        :param _Url: Key value of the custom speed test
        :type Url: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`top`: top resources view; `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `pagepv`: PV view; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation method
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        """Key value of the custom speed test
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataCustomUrlResponse(AbstractModel):
    """DescribeDataCustomUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataEventUrlRequest(AbstractModel):
    """DescribeDataEventUrl request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `ckuv`: UV trend; `ckpv`: PV trend; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _Name: Filter
        :type Name: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Name = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`allcount`: performance view; `day`: 14-day data; `condition`: condition list; `ckuv`: UV trend; `ckpv`: PV trend; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Name(self):
        """Filter
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Name = params.get("Name")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataEventUrlResponse(AbstractModel):
    """DescribeDataEventUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataFetchProjectRequest(AbstractModel):
    """DescribeDataFetchProject request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation method
        :type CostType: str
        :param _Url: Source
        :type Url: str
        :param _Env: Environment
        :type Env: str
        :param _Status: HTTP status code.
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._Status = None
        self._Ret = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`allcount`: performance view; `day`: 14-day data; `condition`: condition list; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation method
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        """Source
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        """HTTP status code.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        """retcode
        :rtype: str
        """
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchProjectResponse(AbstractModel):
    """DescribeDataFetchProject response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataFetchUrlInfoRequest(AbstractModel):
    """DescribeDataFetchUrlInfo request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: Type
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation method
        :type CostType: str
        :param _Url: Source
        :type Url: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """Type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation method
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        """Source
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlInfoResponse(AbstractModel):
    """DescribeDataFetchUrlInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataFetchUrlRequest(AbstractModel):
    """DescribeDataFetchUrl request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `allcount`: performance view; `day`: 14-day data; `count40x`: HTTP status codes 40X view; `count50x`: HTTP status codes 50X view; `count5xand4x`: HTTP status codes 40X∑50X view; `top`: top resources view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation method
        :type CostType: str
        :param _Url: Source
        :type Url: str
        :param _Env: Environment
        :type Env: str
        :param _Status: HTTP status code.
        :type Status: str
        :param _Ret: retcode
        :type Ret: str
        :param _NetStatus: Network status
        :type NetStatus: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None
        self._Status = None
        self._Ret = None
        self._NetStatus = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`allcount`: performance view; `day`: 14-day data; `count40x`: HTTP status codes 40X view; `count50x`: HTTP status codes 50X view; `count5xand4x`: HTTP status codes 40X∑50X view; `top`: top resources view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation method
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        """Source
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        """HTTP status code.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ret(self):
        """retcode
        :rtype: str
        """
        return self._Ret

    @Ret.setter
    def Ret(self, Ret):
        self._Ret = Ret

    @property
    def NetStatus(self):
        """Network status
        :rtype: str
        """
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._Ret = params.get("Ret")
        self._NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataFetchUrlResponse(AbstractModel):
    """DescribeDataFetchUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataLogUrlInfoRequest(AbstractModel):
    """DescribeDataLogUrlInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Project ID
        :type ID: int
        :param _StartTime: Timestamp
        :type StartTime: int
        :param _EndTime: Timestamp
        :type EndTime: int
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        """Timestamp
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Timestamp
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlInfoResponse(AbstractModel):
    """DescribeDataLogUrlInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeDataLogUrlStatisticsRequest(AbstractModel):
    """DescribeDataLogUrlStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `analysis`: exception analysis; `compare`: exception list comparison; `allcount`: performance view; `condition`: condition list; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`analysis`: exception analysis; `compare`: exception list comparison; `allcount`: performance view; `condition`: condition list; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataLogUrlStatisticsResponse(AbstractModel):
    """DescribeDataLogUrlStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataPerformancePageRequest(AbstractModel):
    """DescribeDataPerformancePage request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Project ID
        :type ID: int
        :param _StartTime: Start time
        :type StartTime: int
        :param _EndTime: End time
        :type EndTime: int
        :param _Type: `pagepv`: PV view; `allcount`: performance view; `falls`: page loading waterfall plot; `samp`: FMP, `day`: 14-day data, `nettype`: network/platform view; `performance`: top underperformed pages view; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :type Type: str
        :param _Level: Log level
        :type Level: str
        :param _Isp: ISP
        :type Isp: str
        :param _Area: Region
        :type Area: str
        :param _NetType: Network type
        :type NetType: str
        :param _Platform: Platform
        :type Platform: str
        :param _Device: Model
        :type Device: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Browser: Browser
        :type Browser: str
        :param _Os: OS
        :type Os: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Brand: Brand
        :type Brand: str
        :param _From: Source page
        :type From: str
        :param _CostType: Duration calculation method
        :type CostType: str
        :param _Env: Environment variable
        :type Env: str
        :param _NetStatus: Network status
        :type NetStatus: str
        """
        self._ID = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Level = None
        self._Isp = None
        self._Area = None
        self._NetType = None
        self._Platform = None
        self._Device = None
        self._VersionNum = None
        self._ExtFirst = None
        self._ExtSecond = None
        self._ExtThird = None
        self._IsAbroad = None
        self._Browser = None
        self._Os = None
        self._Engine = None
        self._Brand = None
        self._From = None
        self._CostType = None
        self._Env = None
        self._NetStatus = None

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        """`pagepv`: PV view; `allcount`: performance view; `falls`: page loading waterfall plot; `samp`: FMP, `day`: 14-day data, `nettype`: network/platform view; `performance`: top underperformed pages view; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CostType(self):
        """Duration calculation method
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        """Environment variable
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def NetStatus(self):
        """Network status
        :rtype: str
        """
        return self._NetStatus

    @NetStatus.setter
    def NetStatus(self, NetStatus):
        self._NetStatus = NetStatus


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Level = params.get("Level")
        self._Isp = params.get("Isp")
        self._Area = params.get("Area")
        self._NetType = params.get("NetType")
        self._Platform = params.get("Platform")
        self._Device = params.get("Device")
        self._VersionNum = params.get("VersionNum")
        self._ExtFirst = params.get("ExtFirst")
        self._ExtSecond = params.get("ExtSecond")
        self._ExtThird = params.get("ExtThird")
        self._IsAbroad = params.get("IsAbroad")
        self._Browser = params.get("Browser")
        self._Os = params.get("Os")
        self._Engine = params.get("Engine")
        self._Brand = params.get("Brand")
        self._From = params.get("From")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._NetStatus = params.get("NetStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformancePageResponse(AbstractModel):
    """DescribeDataPerformancePage response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataPerformanceProjectRequest(AbstractModel):
    """DescribeDataPerformanceProject request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `allcount`; performance view; `falls`: page loading waterfall plot; `samp`: FMP, `day`: 14-day data, `nettype`: network/platform view; `performance`: top underperformed pages view; `condition`: condition list; `area`: request speed distribution; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation
        :type CostType: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`allcount`; performance view; `falls`: page loading waterfall plot; `samp`: FMP, `day`: 14-day data, `nettype`: network/platform view; `performance`: top underperformed pages view; `condition`: condition list; `area`: request speed distribution; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPerformanceProjectResponse(AbstractModel):
    """DescribeDataPerformanceProject response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataPvUrlInfoRequest(AbstractModel):
    """DescribeDataPvUrlInfo request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: Type
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """Type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlInfoResponse(AbstractModel):
    """DescribeDataPvUrlInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataPvUrlStatisticsRequest(AbstractModel):
    """DescribeDataPvUrlStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `allcount`; performance view; `day`: 14-day data, `vp`: performance; `ckuv`: UV; `ckpv`: PV; `condition`: condition list; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`allcount`; performance view; `day`: 14-day data, `vp`: performance; `ckuv`: UV; `ckpv`: PV; `condition`: condition list; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataPvUrlStatisticsResponse(AbstractModel):
    """DescribeDataPvUrlStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataReportCountRequest(AbstractModel):
    """DescribeDataReportCount request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ReportType: Reporting type
        :type ReportType: str
        :param _InstanceID: Instance ID
        :type InstanceID: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ReportType = None
        self._InstanceID = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ReportType(self):
        """Reporting type
        :rtype: str
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def InstanceID(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ReportType = params.get("ReportType")
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataReportCountResponse(AbstractModel):
    """DescribeDataReportCount response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataRequest(AbstractModel):
    """DescribeData request structure.

    """

    def __init__(self):
        r"""
        :param _Query: Query string
        :type Query: str
        :param _ID: Project ID
        :type ID: int
        """
        self._Query = None
        self._ID = None

    @property
    def Query(self):
        """Query string
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataResponse(AbstractModel):
    """DescribeData response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeDataSetUrlStatisticsRequest(AbstractModel):
    """DescribeDataSetUrlStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `allcount`: performance view; `data`: mini program; `component`: mini program-related components; `day`: 14-day data; `nettype`: network/platform view; `performance`: top underperformed pages view; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation
        :type CostType: str
        :param _Env: Environment
        :type Env: str
        :param _PackageType: The obtained package.
        :type PackageType: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None
        self._PackageType = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`allcount`: performance view; `data`: mini program; `component`: mini program-related components; `day`: 14-day data; `nettype`: network/platform view; `performance`: top underperformed pages view; `version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: version view; device view; ISP view; region view; browser view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def PackageType(self):
        """The obtained package.
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSetUrlStatisticsResponse(AbstractModel):
    """DescribeDataSetUrlStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataStaticProjectRequest(AbstractModel):
    """DescribeDataStaticProject request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `allcount`: performance view; `day`: 14-day data; `condition`: condition list; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation
        :type CostType: str
        :param _Url: Source
        :type Url: list of str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`allcount`: performance view; `day`: 14-day data; `condition`: condition list; `area`: request speed distribution; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        """Source
        :rtype: list of str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticProjectResponse(AbstractModel):
    """DescribeDataStaticProject response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataStaticResourceRequest(AbstractModel):
    """DescribeDataStaticResource request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `top`: top resources view; `count40x`: HTTP status codes 40X view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation method
        :type CostType: str
        :param _Url: Source
        :type Url: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`top`: top resources view; `count40x`: HTTP status codes 40X view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation method
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        """Source
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticResourceResponse(AbstractModel):
    """DescribeDataStaticResource response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataStaticUrlRequest(AbstractModel):
    """DescribeDataStaticUrl request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _Type: `pagepv`: page view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :type Type: str
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation method
        :type CostType: str
        :param _Url: Source
        :type Url: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._Type = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Url = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Type(self):
        """`pagepv`: page view; `nettype`/`version`/`platform`/`isp`/`region`/`device`/`browser`/`ext1`/`ext2`/`ext3`/`ret`/`status`/`from`/`url`/`env`: network/platform view; version view; device view; ISP view; region view; browser view; custom view, and so on.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation method
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Url(self):
        """Source
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Type = params.get("Type")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Url = params.get("Url")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataStaticUrlResponse(AbstractModel):
    """DescribeDataStaticUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeDataWebVitalsPageRequest(AbstractModel):
    """DescribeDataWebVitalsPage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time
        :type StartTime: int
        :param _EndTime: End time
        :type EndTime: int
        :param _ID: Project ID
        :type ID: int
        :param _ExtSecond: Custom 2
        :type ExtSecond: str
        :param _Engine: Browser engine
        :type Engine: str
        :param _Isp: ISP
        :type Isp: str
        :param _From: Source page
        :type From: str
        :param _Level: Log level
        :type Level: str
        :param _Type: No type yet
        :type Type: str
        :param _Brand: Brand
        :type Brand: str
        :param _Area: Region
        :type Area: str
        :param _VersionNum: Version
        :type VersionNum: str
        :param _Platform: Platform
        :type Platform: str
        :param _ExtThird: Custom 3
        :type ExtThird: str
        :param _ExtFirst: Custom 1
        :type ExtFirst: str
        :param _NetType: Network type
        :type NetType: str
        :param _Device: Model
        :type Device: str
        :param _IsAbroad: Whether it is outside the Chinese mainland
        :type IsAbroad: str
        :param _Os: OS
        :type Os: str
        :param _Browser: Browser
        :type Browser: str
        :param _CostType: Duration calculation
        :type CostType: str
        :param _Env: Environment
        :type Env: str
        """
        self._StartTime = None
        self._EndTime = None
        self._ID = None
        self._ExtSecond = None
        self._Engine = None
        self._Isp = None
        self._From = None
        self._Level = None
        self._Type = None
        self._Brand = None
        self._Area = None
        self._VersionNum = None
        self._Platform = None
        self._ExtThird = None
        self._ExtFirst = None
        self._NetType = None
        self._Device = None
        self._IsAbroad = None
        self._Os = None
        self._Browser = None
        self._CostType = None
        self._Env = None

    @property
    def StartTime(self):
        """Start time
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ExtSecond(self):
        """Custom 2
        :rtype: str
        """
        return self._ExtSecond

    @ExtSecond.setter
    def ExtSecond(self, ExtSecond):
        self._ExtSecond = ExtSecond

    @property
    def Engine(self):
        """Browser engine
        :rtype: str
        """
        return self._Engine

    @Engine.setter
    def Engine(self, Engine):
        self._Engine = Engine

    @property
    def Isp(self):
        """ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def From(self):
        """Source page
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Level(self):
        """Log level
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Type(self):
        """No type yet
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Brand(self):
        """Brand
        :rtype: str
        """
        return self._Brand

    @Brand.setter
    def Brand(self, Brand):
        self._Brand = Brand

    @property
    def Area(self):
        """Region
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def VersionNum(self):
        """Version
        :rtype: str
        """
        return self._VersionNum

    @VersionNum.setter
    def VersionNum(self, VersionNum):
        self._VersionNum = VersionNum

    @property
    def Platform(self):
        """Platform
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ExtThird(self):
        """Custom 3
        :rtype: str
        """
        return self._ExtThird

    @ExtThird.setter
    def ExtThird(self, ExtThird):
        self._ExtThird = ExtThird

    @property
    def ExtFirst(self):
        """Custom 1
        :rtype: str
        """
        return self._ExtFirst

    @ExtFirst.setter
    def ExtFirst(self, ExtFirst):
        self._ExtFirst = ExtFirst

    @property
    def NetType(self):
        """Network type
        :rtype: str
        """
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def Device(self):
        """Model
        :rtype: str
        """
        return self._Device

    @Device.setter
    def Device(self, Device):
        self._Device = Device

    @property
    def IsAbroad(self):
        """Whether it is outside the Chinese mainland
        :rtype: str
        """
        return self._IsAbroad

    @IsAbroad.setter
    def IsAbroad(self, IsAbroad):
        self._IsAbroad = IsAbroad

    @property
    def Os(self):
        """OS
        :rtype: str
        """
        return self._Os

    @Os.setter
    def Os(self, Os):
        self._Os = Os

    @property
    def Browser(self):
        """Browser
        :rtype: str
        """
        return self._Browser

    @Browser.setter
    def Browser(self, Browser):
        self._Browser = Browser

    @property
    def CostType(self):
        """Duration calculation
        :rtype: str
        """
        return self._CostType

    @CostType.setter
    def CostType(self, CostType):
        self._CostType = CostType

    @property
    def Env(self):
        """Environment
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._ExtSecond = params.get("ExtSecond")
        self._Engine = params.get("Engine")
        self._Isp = params.get("Isp")
        self._From = params.get("From")
        self._Level = params.get("Level")
        self._Type = params.get("Type")
        self._Brand = params.get("Brand")
        self._Area = params.get("Area")
        self._VersionNum = params.get("VersionNum")
        self._Platform = params.get("Platform")
        self._ExtThird = params.get("ExtThird")
        self._ExtFirst = params.get("ExtFirst")
        self._NetType = params.get("NetType")
        self._Device = params.get("Device")
        self._IsAbroad = params.get("IsAbroad")
        self._Os = params.get("Os")
        self._Browser = params.get("Browser")
        self._CostType = params.get("CostType")
        self._Env = params.get("Env")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataWebVitalsPageResponse(AbstractModel):
    """DescribeDataWebVitalsPage response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Returned value
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Returned value
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


class DescribeErrorRequest(AbstractModel):
    """DescribeError request structure.

    """

    def __init__(self):
        r"""
        :param _Date: Date
        :type Date: str
        :param _ID: Project ID
        :type ID: int
        """
        self._Date = None
        self._ID = None

    @property
    def Date(self):
        """Date
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeErrorResponse(AbstractModel):
    """DescribeError response structure.

    """

    def __init__(self):
        r"""
        :param _Content: Content
        :type Content: str
        :param _ID: Project ID
        :type ID: int
        :param _CreateTime: Time
        :type CreateTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Content = None
        self._ID = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Content(self):
        """Content
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def CreateTime(self):
        """Time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
        self._Content = params.get("Content")
        self._ID = params.get("ID")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class DescribeLogExportsRequest(AbstractModel):
    """DescribeLogExports request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Project ID
        :type ID: int
        """
        self._ID = None

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogExportsResponse(AbstractModel):
    """DescribeLogExports response structure.

    """

    def __init__(self):
        r"""
        :param _LogExportSet: List of log export records
        :type LogExportSet: list of LogExport
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LogExportSet = None
        self._RequestId = None

    @property
    def LogExportSet(self):
        """List of log export records
        :rtype: list of LogExport
        """
        return self._LogExportSet

    @LogExportSet.setter
    def LogExportSet(self, LogExportSet):
        self._LogExportSet = LogExportSet

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
        if params.get("LogExportSet") is not None:
            self._LogExportSet = []
            for item in params.get("LogExportSet"):
                obj = LogExport()
                obj._deserialize(item)
                self._LogExportSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeLogListRequest(AbstractModel):
    """DescribeLogList request structure.

    """

    def __init__(self):
        r"""
        :param _Sort: Sorting order (required). Valid values: `desc`, `asc`.
        :type Sort: str
        :param _ActionType: This parameter is required. Valid values: `searchlog`, `histogram`.
        :type ActionType: str
        :param _ID: Project ID (required)
        :type ID: int
        :param _StartTime: Start time (required)
        :type StartTime: str
        :param _Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: 100.
        :type Limit: int
        :param _Context: Context, which is used to load more logs. Pass through the last `Context` value returned to get more log content (up to 10,000 raw logs). It will expire after 1 hour
        :type Context: str
        :param _Query: Query statement, which is required and can contain up to 4,096 characters, such as "id:120001 AND type:\"log\"".
        :type Query: str
        :param _EndTime: End time (required)
        :type EndTime: str
        """
        self._Sort = None
        self._ActionType = None
        self._ID = None
        self._StartTime = None
        self._Limit = None
        self._Context = None
        self._Query = None
        self._EndTime = None

    @property
    def Sort(self):
        """Sorting order (required). Valid values: `desc`, `asc`.
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def ActionType(self):
        """This parameter is required. Valid values: `searchlog`, `histogram`.
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ID(self):
        """Project ID (required)
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def StartTime(self):
        """Start time (required)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        """The number of raw logs returned for a single query. This parameter is required. Maximum value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        """Context, which is used to load more logs. Pass through the last `Context` value returned to get more log content (up to 10,000 raw logs). It will expire after 1 hour
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Query(self):
        """Query statement, which is required and can contain up to 4,096 characters, such as "id:120001 AND type:\"log\"".
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        """End time (required)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Sort = params.get("Sort")
        self._ActionType = params.get("ActionType")
        self._ID = params.get("ID")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogListResponse(AbstractModel):
    """DescribeLogList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeOfflineLogConfigsRequest(AbstractModel):
    """DescribeOfflineLogConfigs request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        """
        self._ProjectKey = None

    @property
    def ProjectKey(self):
        """Unique project key for reporting
        :rtype: str
        """
        return self._ProjectKey

    @ProjectKey.setter
    def ProjectKey(self, ProjectKey):
        self._ProjectKey = ProjectKey


    def _deserialize(self, params):
        self._ProjectKey = params.get("ProjectKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogConfigsResponse(AbstractModel):
    """DescribeOfflineLogConfigs response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: API call information
        :type Msg: str
        :param _UniqueIDSet: Array of unique user identifiers
        :type UniqueIDSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._UniqueIDSet = None
        self._RequestId = None

    @property
    def Msg(self):
        """API call information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def UniqueIDSet(self):
        """Array of unique user identifiers
        :rtype: list of str
        """
        return self._UniqueIDSet

    @UniqueIDSet.setter
    def UniqueIDSet(self, UniqueIDSet):
        self._UniqueIDSet = UniqueIDSet

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
        self._Msg = params.get("Msg")
        self._UniqueIDSet = params.get("UniqueIDSet")
        self._RequestId = params.get("RequestId")


class DescribeOfflineLogRecordsRequest(AbstractModel):
    """DescribeOfflineLogRecords request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        """
        self._ProjectKey = None

    @property
    def ProjectKey(self):
        """Unique project key for reporting
        :rtype: str
        """
        return self._ProjectKey

    @ProjectKey.setter
    def ProjectKey(self, ProjectKey):
        self._ProjectKey = ProjectKey


    def _deserialize(self, params):
        self._ProjectKey = params.get("ProjectKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogRecordsResponse(AbstractModel):
    """DescribeOfflineLogRecords response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: API call information
        :type Msg: str
        :param _RecordSet: Array of record IDs
        :type RecordSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RecordSet = None
        self._RequestId = None

    @property
    def Msg(self):
        """API call information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def RecordSet(self):
        """Array of record IDs
        :rtype: list of str
        """
        return self._RecordSet

    @RecordSet.setter
    def RecordSet(self, RecordSet):
        self._RecordSet = RecordSet

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
        self._Msg = params.get("Msg")
        self._RecordSet = params.get("RecordSet")
        self._RequestId = params.get("RequestId")


class DescribeOfflineLogsRequest(AbstractModel):
    """DescribeOfflineLogs request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectKey: Unique project key for reporting
        :type ProjectKey: str
        :param _FileIDs: List of offline log file IDs
        :type FileIDs: list of str
        """
        self._ProjectKey = None
        self._FileIDs = None

    @property
    def ProjectKey(self):
        """Unique project key for reporting
        :rtype: str
        """
        return self._ProjectKey

    @ProjectKey.setter
    def ProjectKey(self, ProjectKey):
        self._ProjectKey = ProjectKey

    @property
    def FileIDs(self):
        """List of offline log file IDs
        :rtype: list of str
        """
        return self._FileIDs

    @FileIDs.setter
    def FileIDs(self, FileIDs):
        self._FileIDs = FileIDs


    def _deserialize(self, params):
        self._ProjectKey = params.get("ProjectKey")
        self._FileIDs = params.get("FileIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfflineLogsResponse(AbstractModel):
    """DescribeOfflineLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: API call response
        :type Msg: str
        :param _LogSet: Log list
        :type LogSet: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._LogSet = None
        self._RequestId = None

    @property
    def Msg(self):
        """API call response
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def LogSet(self):
        """Log list
        :rtype: list of str
        """
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

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
        self._Msg = params.get("Msg")
        self._LogSet = params.get("LogSet")
        self._RequestId = params.get("RequestId")


class DescribeProjectLimitsRequest(AbstractModel):
    """DescribeProjectLimits request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectID: Project ID
        :type ProjectID: int
        """
        self._ProjectID = None

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectLimitsResponse(AbstractModel):
    """DescribeProjectLimits response structure.

    """

    def __init__(self):
        r"""
        :param _ProjectLimitSet: Array of reporting rates
        :type ProjectLimitSet: list of ProjectLimit
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProjectLimitSet = None
        self._RequestId = None

    @property
    def ProjectLimitSet(self):
        """Array of reporting rates
        :rtype: list of ProjectLimit
        """
        return self._ProjectLimitSet

    @ProjectLimitSet.setter
    def ProjectLimitSet(self, ProjectLimitSet):
        self._ProjectLimitSet = ProjectLimitSet

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
        if params.get("ProjectLimitSet") is not None:
            self._ProjectLimitSet = []
            for item in params.get("ProjectLimitSet"):
                obj = ProjectLimit()
                obj._deserialize(item)
                self._ProjectLimitSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of items per page (integer)
        :type Limit: int
        :param _Offset: Page number (integer)
        :type Offset: int
        :param _Filters: Filter parameter. Pass in {"Name": "IsDemo", "Values":["1"]} for the demo mode.
        :type Filters: list of Filter
        :param _IsDemo: This parameter has been disused. You need to indicate whether the demo mode is used in `Filters`.
        :type IsDemo: int
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._IsDemo = None

    @property
    def Limit(self):
        """Number of items per page (integer)
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Page number (integer)
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """Filter parameter. Pass in {"Name": "IsDemo", "Values":["1"]} for the demo mode.
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def IsDemo(self):
        """This parameter has been disused. You need to indicate whether the demo mode is used in `Filters`.
        :rtype: int
        """
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        self._IsDemo = IsDemo


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of items in the list
        :type TotalCount: int
        :param _ProjectSet: Project list
        :type ProjectSet: list of RumProject
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProjectSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of items in the list
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProjectSet(self):
        """Project list
        :rtype: list of RumProject
        """
        return self._ProjectSet

    @ProjectSet.setter
    def ProjectSet(self, ProjectSet):
        self._ProjectSet = ProjectSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("ProjectSet") is not None:
            self._ProjectSet = []
            for item in params.get("ProjectSet"):
                obj = RumProject()
                obj._deserialize(item)
                self._ProjectSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePvListRequest(AbstractModel):
    """DescribePvList request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: ID
        :type ProjectId: int
        :param _EndTime: End time
        :type EndTime: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _Dimension: Get day:d (leave this parameter empty if to get min)
        :type Dimension: str
        """
        self._ProjectId = None
        self._EndTime = None
        self._StartTime = None
        self._Dimension = None

    @property
    def ProjectId(self):
        """ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Dimension(self):
        """Get day:d (leave this parameter empty if to get min)
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePvListResponse(AbstractModel):
    """DescribePvList response structure.

    """

    def __init__(self):
        r"""
        :param _ProjectPvSet: PV list
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectPvSet: list of RumPvInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProjectPvSet = None
        self._RequestId = None

    @property
    def ProjectPvSet(self):
        """PV list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of RumPvInfo
        """
        return self._ProjectPvSet

    @ProjectPvSet.setter
    def ProjectPvSet(self, ProjectPvSet):
        self._ProjectPvSet = ProjectPvSet

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
        if params.get("ProjectPvSet") is not None:
            self._ProjectPvSet = []
            for item in params.get("ProjectPvSet"):
                obj = RumPvInfo()
                obj._deserialize(item)
                self._ProjectPvSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeReleaseFileSignRequest(AbstractModel):
    """DescribeReleaseFileSign request structure.

    """

    def __init__(self):
        r"""
        :param _Timeout: Timeout period. If it is not set, it will be 5 minutes by default
        :type Timeout: int
        :param _FileType: Bucket type. Valid values: `1`: (Web, which is the default value), `2` (Application).
        :type FileType: int
        """
        self._Timeout = None
        self._FileType = None

    @property
    def Timeout(self):
        """Timeout period. If it is not set, it will be 5 minutes by default
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def FileType(self):
        """Bucket type. Valid values: `1`: (Web, which is the default value), `2` (Application).
        :rtype: int
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._Timeout = params.get("Timeout")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFileSignResponse(AbstractModel):
    """DescribeReleaseFileSign response structure.

    """

    def __init__(self):
        r"""
        :param _SecretKey: Temporary key
        :type SecretKey: str
        :param _SecretID: Temporary key ID
        :type SecretID: str
        :param _SessionToken: Temporary key token
        :type SessionToken: str
        :param _StartTime: Start timestamp
        :type StartTime: int
        :param _ExpiredTime: Expiration timestamp
        :type ExpiredTime: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretKey = None
        self._SecretID = None
        self._SessionToken = None
        self._StartTime = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def SecretKey(self):
        """Temporary key
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SecretID(self):
        """Temporary key ID
        :rtype: str
        """
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def SessionToken(self):
        """Temporary key token
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def StartTime(self):
        """Start timestamp
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpiredTime(self):
        """Expiration timestamp
        :rtype: int
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

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
        self._SecretKey = params.get("SecretKey")
        self._SecretID = params.get("SecretID")
        self._SessionToken = params.get("SessionToken")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class DescribeReleaseFilesRequest(AbstractModel):
    """DescribeReleaseFiles request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectID: Project ID
        :type ProjectID: int
        :param _FileVersion: File version
        :type FileVersion: str
        """
        self._ProjectID = None
        self._FileVersion = None

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def FileVersion(self):
        """File version
        :rtype: str
        """
        return self._FileVersion

    @FileVersion.setter
    def FileVersion(self, FileVersion):
        self._FileVersion = FileVersion


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._FileVersion = params.get("FileVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseFilesResponse(AbstractModel):
    """DescribeReleaseFiles response structure.

    """

    def __init__(self):
        r"""
        :param _Files: File information list
        :type Files: list of ReleaseFile
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Files = None
        self._RequestId = None

    @property
    def Files(self):
        """File information list
        :rtype: list of ReleaseFile
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files

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
        if params.get("Files") is not None:
            self._Files = []
            for item in params.get("Files"):
                obj = ReleaseFile()
                obj._deserialize(item)
                self._Files.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRumGroupLogRequest(AbstractModel):
    """DescribeRumGroupLog request structure.

    """

    def __init__(self):
        r"""
        :param _OrderBy: Sorting order (required). Valid values: `desc`, `asc`.
        :type OrderBy: str
        :param _StartTime: Start time (required)
        :type StartTime: str
        :param _Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :type Limit: int
        :param _Page: Page number
        :type Page: int
        :param _Query: Query statement, which is required and can contain up to 4,096 characters.
        :type Query: str
        :param _EndTime: End time (required)
        :type EndTime: str
        :param _ID: Project ID (required)
        :type ID: int
        :param _GroupField: Aggregate field
        :type GroupField: str
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Page = None
        self._Query = None
        self._EndTime = None
        self._ID = None
        self._GroupField = None

    @property
    def OrderBy(self):
        """Sorting order (required). Valid values: `desc`, `asc`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        """Start time (required)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        """The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        """Page number
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Query(self):
        """Query statement, which is required and can contain up to 4,096 characters.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        """End time (required)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID (required)
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def GroupField(self):
        """Aggregate field
        :rtype: str
        """
        return self._GroupField

    @GroupField.setter
    def GroupField(self, GroupField):
        self._GroupField = GroupField


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._GroupField = params.get("GroupField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumGroupLogResponse(AbstractModel):
    """DescribeRumGroupLog response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeRumLogExportRequest(AbstractModel):
    """DescribeRumLogExport request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Export identifier name
        :type Name: str
        :param _StartTime: Start time (required)
        :type StartTime: str
        :param _Query: Query statement, which is required and can contain up to 4,096 characters.
        :type Query: str
        :param _EndTime: End time (required)
        :type EndTime: str
        :param _ID: Project ID (required)
        :type ID: int
        :param _Fields: Filter field
        :type Fields: list of str
        """
        self._Name = None
        self._StartTime = None
        self._Query = None
        self._EndTime = None
        self._ID = None
        self._Fields = None

    @property
    def Name(self):
        """Export identifier name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StartTime(self):
        """Start time (required)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Query(self):
        """Query statement, which is required and can contain up to 4,096 characters.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        """End time (required)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID (required)
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Fields(self):
        """Filter field
        :rtype: list of str
        """
        return self._Fields

    @Fields.setter
    def Fields(self, Fields):
        self._Fields = Fields


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._StartTime = params.get("StartTime")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        self._Fields = params.get("Fields")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportResponse(AbstractModel):
    """DescribeRumLogExport response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeRumLogExportsRequest(AbstractModel):
    """DescribeRumLogExports request structure.

    """

    def __init__(self):
        r"""
        :param _PageSize: Page size
        :type PageSize: int
        :param _PageNum: Page number
        :type PageNum: int
        :param _ID: Project ID (required)
        :type ID: int
        """
        self._PageSize = None
        self._PageNum = None
        self._ID = None

    @property
    def PageSize(self):
        """Page size
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        """Page number
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def ID(self):
        """Project ID (required)
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogExportsResponse(AbstractModel):
    """DescribeRumLogExports response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeRumLogListRequest(AbstractModel):
    """DescribeRumLogList request structure.

    """

    def __init__(self):
        r"""
        :param _OrderBy: Sorting order (required). Valid values: `desc`, `asc`.
        :type OrderBy: str
        :param _StartTime: Start time in milliseconds. It is in timestamp format and is required.
        :type StartTime: str
        :param _Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :type Limit: int
        :param _Page: Page number
        :type Page: int
        :param _Query: Query statement, which is required and can contain up to 4,096 characters.
        :type Query: str
        :param _EndTime: End time in milliseconds. It is in timestamp format and is required.
        :type EndTime: str
        :param _ID: Project ID (required)
        :type ID: int
        """
        self._OrderBy = None
        self._StartTime = None
        self._Limit = None
        self._Page = None
        self._Query = None
        self._EndTime = None
        self._ID = None

    @property
    def OrderBy(self):
        """Sorting order (required). Valid values: `desc`, `asc`.
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def StartTime(self):
        """Start time in milliseconds. It is in timestamp format and is required.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        """The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        """Page number
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Query(self):
        """Query statement, which is required and can contain up to 4,096 characters.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        """End time in milliseconds. It is in timestamp format and is required.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID (required)
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumLogListResponse(AbstractModel):
    """DescribeRumLogList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeRumStatsLogListRequest(AbstractModel):
    """DescribeRumStatsLogList request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time (required)
        :type StartTime: str
        :param _Limit: The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :type Limit: int
        :param _Query: Query statement, which is required and can contain up to 4,096 characters.
        :type Query: str
        :param _EndTime: End time (required)
        :type EndTime: str
        :param _ID: Project ID (required)
        :type ID: int
        """
        self._StartTime = None
        self._Limit = None
        self._Query = None
        self._EndTime = None
        self._ID = None

    @property
    def StartTime(self):
        """Start time (required)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Limit(self):
        """The number of raw logs returned for a single query. This parameter is required. Maximum value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Query(self):
        """Query statement, which is required and can contain up to 4,096 characters.
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def EndTime(self):
        """End time (required)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ID(self):
        """Project ID (required)
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._Limit = params.get("Limit")
        self._Query = params.get("Query")
        self._EndTime = params.get("EndTime")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRumStatsLogListResponse(AbstractModel):
    """DescribeRumStatsLogList response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Response string
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """Response string
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


class DescribeScoresRequest(AbstractModel):
    """DescribeScores request structure.

    """

    def __init__(self):
        r"""
        :param _EndTime: End time
        :type EndTime: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _ID: Project ID
        :type ID: int
        :param _IsDemo: This parameter has been disused.
        :type IsDemo: int
        """
        self._EndTime = None
        self._StartTime = None
        self._ID = None
        self._IsDemo = None

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def IsDemo(self):
        """This parameter has been disused.
        :rtype: int
        """
        return self._IsDemo

    @IsDemo.setter
    def IsDemo(self, IsDemo):
        self._IsDemo = IsDemo


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._ID = params.get("ID")
        self._IsDemo = params.get("IsDemo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScoresResponse(AbstractModel):
    """DescribeScores response structure.

    """

    def __init__(self):
        r"""
        :param _ScoreSet: Array
        :type ScoreSet: list of ScoreInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ScoreSet = None
        self._RequestId = None

    @property
    def ScoreSet(self):
        """Array
        :rtype: list of ScoreInfo
        """
        return self._ScoreSet

    @ScoreSet.setter
    def ScoreSet(self, ScoreSet):
        self._ScoreSet = ScoreSet

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
        if params.get("ScoreSet") is not None:
            self._ScoreSet = []
            for item in params.get("ScoreSet"):
                obj = ScoreInfo()
                obj._deserialize(item)
                self._ScoreSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTawAreasRequest(AbstractModel):
    """DescribeTawAreas request structure.

    """

    def __init__(self):
        r"""
        :param _AreaIds: Region ID
        :type AreaIds: list of int
        :param _AreaKeys: Region key
        :type AreaKeys: list of str
        :param _Limit: Pagination limit
        :type Limit: int
        :param _AreaStatuses: Region status (1: valid; 2: invalid)
        :type AreaStatuses: list of int
        :param _Offset: Pagination offset
        :type Offset: int
        """
        self._AreaIds = None
        self._AreaKeys = None
        self._Limit = None
        self._AreaStatuses = None
        self._Offset = None

    @property
    def AreaIds(self):
        """Region ID
        :rtype: list of int
        """
        return self._AreaIds

    @AreaIds.setter
    def AreaIds(self, AreaIds):
        self._AreaIds = AreaIds

    @property
    def AreaKeys(self):
        """Region key
        :rtype: list of str
        """
        return self._AreaKeys

    @AreaKeys.setter
    def AreaKeys(self, AreaKeys):
        self._AreaKeys = AreaKeys

    @property
    def Limit(self):
        """Pagination limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AreaStatuses(self):
        """Region status (1: valid; 2: invalid)
        :rtype: list of int
        """
        return self._AreaStatuses

    @AreaStatuses.setter
    def AreaStatuses(self, AreaStatuses):
        self._AreaStatuses = AreaStatuses

    @property
    def Offset(self):
        """Pagination offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._AreaIds = params.get("AreaIds")
        self._AreaKeys = params.get("AreaKeys")
        self._Limit = params.get("Limit")
        self._AreaStatuses = params.get("AreaStatuses")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTawAreasResponse(AbstractModel):
    """DescribeTawAreas response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of regions
        :type TotalCount: int
        :param _AreaSet: Region list
        :type AreaSet: list of RumAreaInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._AreaSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number of regions
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AreaSet(self):
        """Region list
        :rtype: list of RumAreaInfo
        """
        return self._AreaSet

    @AreaSet.setter
    def AreaSet(self, AreaSet):
        self._AreaSet = AreaSet

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
        self._TotalCount = params.get("TotalCount")
        if params.get("AreaSet") is not None:
            self._AreaSet = []
            for item in params.get("AreaSet"):
                obj = RumAreaInfo()
                obj._deserialize(item)
                self._AreaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUvListRequest(AbstractModel):
    """DescribeUvList request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: ID
        :type ProjectId: int
        :param _EndTime: End time
        :type EndTime: str
        :param _StartTime: Start time
        :type StartTime: str
        :param _Dimension: Get day:d min:m
        :type Dimension: str
        """
        self._ProjectId = None
        self._EndTime = None
        self._StartTime = None
        self._Dimension = None

    @property
    def ProjectId(self):
        """ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def EndTime(self):
        """End time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        """Start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Dimension(self):
        """Get day:d min:m
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        self._Dimension = params.get("Dimension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUvListResponse(AbstractModel):
    """DescribeUvList response structure.

    """

    def __init__(self):
        r"""
        :param _ProjectUvSet: UV list
        :type ProjectUvSet: list of RumUvInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ProjectUvSet = None
        self._RequestId = None

    @property
    def ProjectUvSet(self):
        """UV list
        :rtype: list of RumUvInfo
        """
        return self._ProjectUvSet

    @ProjectUvSet.setter
    def ProjectUvSet(self, ProjectUvSet):
        self._ProjectUvSet = ProjectUvSet

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
        if params.get("ProjectUvSet") is not None:
            self._ProjectUvSet = []
            for item in params.get("ProjectUvSet"):
                obj = RumUvInfo()
                obj._deserialize(item)
                self._ProjectUvSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhitelistsRequest(AbstractModel):
    """DescribeWhitelists request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceID: Instance ID
        :type InstanceID: str
        """
        self._InstanceID = None

    @property
    def InstanceID(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID


    def _deserialize(self, params):
        self._InstanceID = params.get("InstanceID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhitelistsResponse(AbstractModel):
    """DescribeWhitelists response structure.

    """

    def __init__(self):
        r"""
        :param _WhitelistSet: Allowlist list
        :type WhitelistSet: list of Whitelist
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._WhitelistSet = None
        self._RequestId = None

    @property
    def WhitelistSet(self):
        """Allowlist list
        :rtype: list of Whitelist
        """
        return self._WhitelistSet

    @WhitelistSet.setter
    def WhitelistSet(self, WhitelistSet):
        self._WhitelistSet = WhitelistSet

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
        if params.get("WhitelistSet") is not None:
            self._WhitelistSet = []
            for item in params.get("WhitelistSet"):
                obj = Whitelist()
                obj._deserialize(item)
                self._WhitelistSet.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Key-Value pair filter for conditional filtering queries, such as filtering ID, name, status, etc.

    · If more than one filter exists, the logical relationship between these filters is `AND`.
    · If multiple values exist in one filter, the logical relationship between these values is `OR`.

    """

    def __init__(self):
        r"""
        :param _Values: One or more filter values.
        :type Values: list of str
        :param _Name: Filter name.
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        """One or more filter values.
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        """Filter name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogExport(AbstractModel):
    """Log export record

    """

    def __init__(self):
        r"""
        :param _CosPath: Log export path
        :type CosPath: str
        :param _Count: Number of logs to be exported
        :type Count: int
        :param _CreateTime: Log export task creation time
        :type CreateTime: str
        :param _ExportID: Log export task ID
        :type ExportID: str
        :param _FileName: Log export filename
        :type FileName: str
        :param _FileSize: Log file size
        :type FileSize: int
        :param _Format: Log export format
        :type Format: str
        :param _Order: Log export time sorting
        :type Order: str
        :param _Query: Log export query statement
        :type Query: str
        :param _StartTime: Log export start time
        :type StartTime: str
        :param _EndTime: Log export end time
        :type EndTime: str
        :param _Status: Log download status. Valid values: Queuing: queuing; Processing: exporting; Complete: completed; Failed: failed; Expired: expired (3-day validity period).
        :type Status: str
        """
        self._CosPath = None
        self._Count = None
        self._CreateTime = None
        self._ExportID = None
        self._FileName = None
        self._FileSize = None
        self._Format = None
        self._Order = None
        self._Query = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None

    @property
    def CosPath(self):
        """Log export path
        :rtype: str
        """
        return self._CosPath

    @CosPath.setter
    def CosPath(self, CosPath):
        self._CosPath = CosPath

    @property
    def Count(self):
        """Number of logs to be exported
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def CreateTime(self):
        """Log export task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExportID(self):
        """Log export task ID
        :rtype: str
        """
        return self._ExportID

    @ExportID.setter
    def ExportID(self, ExportID):
        self._ExportID = ExportID

    @property
    def FileName(self):
        """Log export filename
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileSize(self):
        """Log file size
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def Format(self):
        """Log export format
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Order(self):
        """Log export time sorting
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Query(self):
        """Log export query statement
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def StartTime(self):
        """Log export start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Log export end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """Log download status. Valid values: Queuing: queuing; Processing: exporting; Complete: completed; Failed: failed; Expired: expired (3-day validity period).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CosPath = params.get("CosPath")
        self._Count = params.get("Count")
        self._CreateTime = params.get("CreateTime")
        self._ExportID = params.get("ExportID")
        self._FileName = params.get("FileName")
        self._FileSize = params.get("FileSize")
        self._Format = params.get("Format")
        self._Order = params.get("Order")
        self._Query = params.get("Query")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be modified
        :type InstanceId: str
        :param _InstanceName: New instance name (up to 255 characters)
        :type InstanceName: str
        :param _InstanceDesc: New instance description (up to 1,024 characters)
        :type InstanceDesc: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceDesc = None

    @property
    def InstanceId(self):
        """ID of the instance to be modified
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """New instance name (up to 255 characters)
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceDesc(self):
        """New instance description (up to 1,024 characters)
        :rtype: str
        """
        return self._InstanceDesc

    @InstanceDesc.setter
    def InstanceDesc(self, InstanceDesc):
        self._InstanceDesc = InstanceDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceDesc = params.get("InstanceDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyProjectLimitRequest(AbstractModel):
    """ModifyProjectLimit request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectID: Project ID
        :type ProjectID: int
        :param _ProjectInterface: Project API
        :type ProjectInterface: str
        :param _ReportRate: Reporting rate. 10 means 10%
        :type ReportRate: int
        :param _ReportType: Reporting type. 1: rate; 2: number of reported data entries
        :type ReportType: int
        :param _ID: Primary key ID
        :type ID: int
        """
        self._ProjectID = None
        self._ProjectInterface = None
        self._ReportRate = None
        self._ReportType = None
        self._ID = None

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ProjectInterface(self):
        """Project API
        :rtype: str
        """
        return self._ProjectInterface

    @ProjectInterface.setter
    def ProjectInterface(self, ProjectInterface):
        self._ProjectInterface = ProjectInterface

    @property
    def ReportRate(self):
        """Reporting rate. 10 means 10%
        :rtype: int
        """
        return self._ReportRate

    @ReportRate.setter
    def ReportRate(self, ReportRate):
        self._ReportRate = ReportRate

    @property
    def ReportType(self):
        """Reporting type. 1: rate; 2: number of reported data entries
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def ID(self):
        """Primary key ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._ProjectID = params.get("ProjectID")
        self._ProjectInterface = params.get("ProjectInterface")
        self._ReportRate = params.get("ReportRate")
        self._ReportType = params.get("ReportType")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectLimitResponse(AbstractModel):
    """ModifyProjectLimit response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Returned message
Note: this field may return null, indicating that no valid values can be obtained.
        :type Msg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._RequestId = None

    @property
    def Msg(self):
        """Returned message
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Project ID
        :type ID: int
        :param _Name: Project name (optional, not empty, and up to 200 characters)
        :type Name: str
        :param _URL: Project webpage URL (optional and up to 256 characters)
        :type URL: str
        :param _Repo: Project repository address (optional and up to 256 characters)
        :type Repo: str
        :param _InstanceID: ID of the instance to which to move the project (optional)
        :type InstanceID: str
        :param _Rate: Project sample rate (optional)
        :type Rate: str
        :param _EnableURLGroup: Whether to enable aggregation (optional)
        :type EnableURLGroup: int
        :param _Type: Project type (valid values: "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :type Type: str
        :param _Desc: Project description (optional and up to 1,000 characters)
        :type Desc: str
        """
        self._ID = None
        self._Name = None
        self._URL = None
        self._Repo = None
        self._InstanceID = None
        self._Rate = None
        self._EnableURLGroup = None
        self._Type = None
        self._Desc = None

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        """Project name (optional, not empty, and up to 200 characters)
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def URL(self):
        """Project webpage URL (optional and up to 256 characters)
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Repo(self):
        """Project repository address (optional and up to 256 characters)
        :rtype: str
        """
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def InstanceID(self):
        """ID of the instance to which to move the project (optional)
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Rate(self):
        """Project sample rate (optional)
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def EnableURLGroup(self):
        """Whether to enable aggregation (optional)
        :rtype: int
        """
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def Type(self):
        """Project type (valid values: "web", "mp", "android", "ios", "node", "hippy", "weex", "viola", "rn")
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Desc(self):
        """Project description (optional and up to 1,000 characters)
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._URL = params.get("URL")
        self._Repo = params.get("Repo")
        self._InstanceID = params.get("InstanceID")
        self._Rate = params.get("Rate")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._Type = params.get("Type")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProjectResponse(AbstractModel):
    """ModifyProject response structure.

    """

    def __init__(self):
        r"""
        :param _Msg: Operation information
        :type Msg: str
        :param _ID: Project ID
        :type ID: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Msg = None
        self._ID = None
        self._RequestId = None

    @property
    def Msg(self):
        """Operation information
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

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
        self._Msg = params.get("Msg")
        self._ID = params.get("ID")
        self._RequestId = params.get("RequestId")


class ProjectLimit(AbstractModel):
    """Project API restriction type

    """

    def __init__(self):
        r"""
        :param _ID: Primary key ID
        :type ID: int
        :param _ProjectID: Project ID
        :type ProjectID: int
        :param _ProjectInterface: API
        :type ProjectInterface: str
        :param _ReportRate: Reporting rate
        :type ReportRate: int
        :param _ReportType: Reporting type. 1: reporting rate; 2: reporting count limit
        :type ReportType: int
        """
        self._ID = None
        self._ProjectID = None
        self._ProjectInterface = None
        self._ReportRate = None
        self._ReportType = None

    @property
    def ID(self):
        """Primary key ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def ProjectInterface(self):
        """API
        :rtype: str
        """
        return self._ProjectInterface

    @ProjectInterface.setter
    def ProjectInterface(self, ProjectInterface):
        self._ProjectInterface = ProjectInterface

    @property
    def ReportRate(self):
        """Reporting rate
        :rtype: int
        """
        return self._ReportRate

    @ReportRate.setter
    def ReportRate(self, ReportRate):
        self._ReportRate = ReportRate

    @property
    def ReportType(self):
        """Reporting type. 1: reporting rate; 2: reporting count limit
        :rtype: int
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ProjectID = params.get("ProjectID")
        self._ProjectInterface = params.get("ProjectInterface")
        self._ReportRate = params.get("ReportRate")
        self._ReportType = params.get("ReportType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseFile(AbstractModel):
    """Release file list (sourcemap)

    """

    def __init__(self):
        r"""
        :param _Version: File version
        :type Version: str
        :param _FileKey: Unique file key
        :type FileKey: str
        :param _FileName: Filename
        :type FileName: str
        :param _FileHash: File hash
        :type FileHash: str
        :param _ID: File ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ID: int
        """
        self._Version = None
        self._FileKey = None
        self._FileName = None
        self._FileHash = None
        self._ID = None

    @property
    def Version(self):
        """File version
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def FileKey(self):
        """Unique file key
        :rtype: str
        """
        return self._FileKey

    @FileKey.setter
    def FileKey(self, FileKey):
        self._FileKey = FileKey

    @property
    def FileName(self):
        """Filename
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileHash(self):
        """File hash
        :rtype: str
        """
        return self._FileHash

    @FileHash.setter
    def FileHash(self, FileHash):
        self._FileHash = FileHash

    @property
    def ID(self):
        """File ID
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._FileKey = params.get("FileKey")
        self._FileName = params.get("FileName")
        self._FileHash = params.get("FileHash")
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceRequest(AbstractModel):
    """ResumeInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be resumed
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ID of the instance to be resumed
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeInstanceResponse(AbstractModel):
    """ResumeInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ResumeProjectRequest(AbstractModel):
    """ResumeProject request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeProjectResponse(AbstractModel):
    """ResumeProject response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RumAreaInfo(AbstractModel):
    """RUM region information

    """

    def __init__(self):
        r"""
        :param _AreaId: Region ID
        :type AreaId: int
        :param _AreaStatus: Region status (1: valid; 2: invalid)
        :type AreaStatus: int
        :param _AreaName: Region name
        :type AreaName: str
        :param _AreaKey: Region key
        :type AreaKey: str
        :param _AreaRegionID: Region ID.
        :type AreaRegionID: str
        :param _AreaRegionCode: Region code, such as “ap-xxx” (xxx is the region name).
        :type AreaRegionCode: str
        :param _AreaAbbr: Region abbreviation.
        :type AreaAbbr: str
        """
        self._AreaId = None
        self._AreaStatus = None
        self._AreaName = None
        self._AreaKey = None
        self._AreaRegionID = None
        self._AreaRegionCode = None
        self._AreaAbbr = None

    @property
    def AreaId(self):
        """Region ID
        :rtype: int
        """
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def AreaStatus(self):
        """Region status (1: valid; 2: invalid)
        :rtype: int
        """
        return self._AreaStatus

    @AreaStatus.setter
    def AreaStatus(self, AreaStatus):
        self._AreaStatus = AreaStatus

    @property
    def AreaName(self):
        """Region name
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def AreaKey(self):
        """Region key
        :rtype: str
        """
        return self._AreaKey

    @AreaKey.setter
    def AreaKey(self, AreaKey):
        self._AreaKey = AreaKey

    @property
    def AreaRegionID(self):
        """Region ID.
        :rtype: str
        """
        return self._AreaRegionID

    @AreaRegionID.setter
    def AreaRegionID(self, AreaRegionID):
        self._AreaRegionID = AreaRegionID

    @property
    def AreaRegionCode(self):
        """Region code, such as “ap-xxx” (xxx is the region name).
        :rtype: str
        """
        return self._AreaRegionCode

    @AreaRegionCode.setter
    def AreaRegionCode(self, AreaRegionCode):
        self._AreaRegionCode = AreaRegionCode

    @property
    def AreaAbbr(self):
        """Region abbreviation.
        :rtype: str
        """
        return self._AreaAbbr

    @AreaAbbr.setter
    def AreaAbbr(self, AreaAbbr):
        self._AreaAbbr = AreaAbbr


    def _deserialize(self, params):
        self._AreaId = params.get("AreaId")
        self._AreaStatus = params.get("AreaStatus")
        self._AreaName = params.get("AreaName")
        self._AreaKey = params.get("AreaKey")
        self._AreaRegionID = params.get("AreaRegionID")
        self._AreaRegionCode = params.get("AreaRegionCode")
        self._AreaAbbr = params.get("AreaAbbr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumProject(AbstractModel):
    """RUM project information

    """

    def __init__(self):
        r"""
        :param _Name: Project name
        :type Name: str
        :param _Creator: Creator ID
        :type Creator: str
        :param _InstanceID: Instance ID
        :type InstanceID: str
        :param _Type: Project type
        :type Type: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Repo: Project repository address
Note: this field may return null, indicating that no valid values can be obtained.
        :type Repo: str
        :param _URL: Project URL
Note: this field may return null, indicating that no valid values can be obtained.
        :type URL: str
        :param _Rate: Project sample rate
        :type Rate: str
        :param _Key: Unique project key (12 characters)
        :type Key: str
        :param _EnableURLGroup: Whether to enable URL aggregation
        :type EnableURLGroup: int
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _ID: Project ID
        :type ID: int
        :param _InstanceKey: Instance key
        :type InstanceKey: str
        :param _Desc: Project description
Note: this field may return null, indicating that no valid values can be obtained.
        :type Desc: str
        :param _IsStar: Starred status. 1: yes; 0: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsStar: int
        :param _ProjectStatus: Project status (`1`: Creating; `2`: Running; `3`: Abnormal; `4`: Restarting; `5`: Stopping; `6`: Stopped; `7`: Terminating; `8`: Terminated)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProjectStatus: int
        :param _AccessPoint: Log access point, which can be ignored. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :type AccessPoint: str
        """
        self._Name = None
        self._Creator = None
        self._InstanceID = None
        self._Type = None
        self._CreateTime = None
        self._Repo = None
        self._URL = None
        self._Rate = None
        self._Key = None
        self._EnableURLGroup = None
        self._InstanceName = None
        self._ID = None
        self._InstanceKey = None
        self._Desc = None
        self._IsStar = None
        self._ProjectStatus = None
        self._AccessPoint = None

    @property
    def Name(self):
        """Project name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Creator(self):
        """Creator ID
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def InstanceID(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Type(self):
        """Project type
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
    def Repo(self):
        """Project repository address
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Repo

    @Repo.setter
    def Repo(self, Repo):
        self._Repo = Repo

    @property
    def URL(self):
        """Project URL
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._URL

    @URL.setter
    def URL(self, URL):
        self._URL = URL

    @property
    def Rate(self):
        """Project sample rate
        :rtype: str
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Key(self):
        """Unique project key (12 characters)
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def EnableURLGroup(self):
        """Whether to enable URL aggregation
        :rtype: int
        """
        return self._EnableURLGroup

    @EnableURLGroup.setter
    def EnableURLGroup(self, EnableURLGroup):
        self._EnableURLGroup = EnableURLGroup

    @property
    def InstanceName(self):
        """Instance name
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ID(self):
        """Project ID
        :rtype: int
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def InstanceKey(self):
        """Instance key
        :rtype: str
        """
        return self._InstanceKey

    @InstanceKey.setter
    def InstanceKey(self, InstanceKey):
        self._InstanceKey = InstanceKey

    @property
    def Desc(self):
        """Project description
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def IsStar(self):
        """Starred status. 1: yes; 0: no
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IsStar

    @IsStar.setter
    def IsStar(self, IsStar):
        self._IsStar = IsStar

    @property
    def ProjectStatus(self):
        """Project status (`1`: Creating; `2`: Running; `3`: Abnormal; `4`: Restarting; `5`: Stopping; `6`: Stopped; `7`: Terminating; `8`: Terminated)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ProjectStatus

    @ProjectStatus.setter
    def ProjectStatus(self, ProjectStatus):
        self._ProjectStatus = ProjectStatus

    @property
    def AccessPoint(self):
        """Log access point, which can be ignored. 
Note:  This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._AccessPoint

    @AccessPoint.setter
    def AccessPoint(self, AccessPoint):
        self._AccessPoint = AccessPoint


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Creator = params.get("Creator")
        self._InstanceID = params.get("InstanceID")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._Repo = params.get("Repo")
        self._URL = params.get("URL")
        self._Rate = params.get("Rate")
        self._Key = params.get("Key")
        self._EnableURLGroup = params.get("EnableURLGroup")
        self._InstanceName = params.get("InstanceName")
        self._ID = params.get("ID")
        self._InstanceKey = params.get("InstanceKey")
        self._Desc = params.get("Desc")
        self._IsStar = params.get("IsStar")
        self._ProjectStatus = params.get("ProjectStatus")
        self._AccessPoint = params.get("AccessPoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumPvInfo(AbstractModel):
    """RUM log object

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Pv: Number of PVs
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pv: str
        :param _CreateTime: Time
        :type CreateTime: str
        """
        self._ProjectId = None
        self._Pv = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Pv(self):
        """Number of PVs
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Pv

    @Pv.setter
    def Pv(self, Pv):
        self._Pv = Pv

    @property
    def CreateTime(self):
        """Time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Pv = params.get("Pv")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RumUvInfo(AbstractModel):
    """Number of RUM UVs

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Uv: Number of UVs
        :type Uv: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        """
        self._ProjectId = None
        self._Uv = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Uv(self):
        """Number of UVs
        :rtype: str
        """
        return self._Uv

    @Uv.setter
    def Uv(self, Uv):
        self._Uv = Uv

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Uv = params.get("Uv")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScoreInfo(AbstractModel):
    """Project score entity

    """

    def __init__(self):
        r"""
        :param _StaticDuration: duration
        :type StaticDuration: str
        :param _PagePv: pv
        :type PagePv: str
        :param _ApiFail: Failure
        :type ApiFail: str
        :param _ApiNum: Request
        :type ApiNum: str
        :param _StaticFail: fail
        :type StaticFail: str
        :param _ProjectID: Project ID
        :type ProjectID: int
        :param _PageUv: uv
        :type PageUv: str
        :param _ApiDuration: Number of requests
        :type ApiDuration: str
        :param _Score: Score
        :type Score: str
        :param _PageError: error
        :type PageError: str
        :param _StaticNum: num
        :type StaticNum: str
        :param _RecordNum: num
        :type RecordNum: int
        :param _PageDuration: Duration
        :type PageDuration: str
        :param _CreateTime: Time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        """
        self._StaticDuration = None
        self._PagePv = None
        self._ApiFail = None
        self._ApiNum = None
        self._StaticFail = None
        self._ProjectID = None
        self._PageUv = None
        self._ApiDuration = None
        self._Score = None
        self._PageError = None
        self._StaticNum = None
        self._RecordNum = None
        self._PageDuration = None
        self._CreateTime = None

    @property
    def StaticDuration(self):
        """duration
        :rtype: str
        """
        return self._StaticDuration

    @StaticDuration.setter
    def StaticDuration(self, StaticDuration):
        self._StaticDuration = StaticDuration

    @property
    def PagePv(self):
        """pv
        :rtype: str
        """
        return self._PagePv

    @PagePv.setter
    def PagePv(self, PagePv):
        self._PagePv = PagePv

    @property
    def ApiFail(self):
        """Failure
        :rtype: str
        """
        return self._ApiFail

    @ApiFail.setter
    def ApiFail(self, ApiFail):
        self._ApiFail = ApiFail

    @property
    def ApiNum(self):
        """Request
        :rtype: str
        """
        return self._ApiNum

    @ApiNum.setter
    def ApiNum(self, ApiNum):
        self._ApiNum = ApiNum

    @property
    def StaticFail(self):
        """fail
        :rtype: str
        """
        return self._StaticFail

    @StaticFail.setter
    def StaticFail(self, StaticFail):
        self._StaticFail = StaticFail

    @property
    def ProjectID(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def PageUv(self):
        """uv
        :rtype: str
        """
        return self._PageUv

    @PageUv.setter
    def PageUv(self, PageUv):
        self._PageUv = PageUv

    @property
    def ApiDuration(self):
        """Number of requests
        :rtype: str
        """
        return self._ApiDuration

    @ApiDuration.setter
    def ApiDuration(self, ApiDuration):
        self._ApiDuration = ApiDuration

    @property
    def Score(self):
        """Score
        :rtype: str
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def PageError(self):
        """error
        :rtype: str
        """
        return self._PageError

    @PageError.setter
    def PageError(self, PageError):
        self._PageError = PageError

    @property
    def StaticNum(self):
        """num
        :rtype: str
        """
        return self._StaticNum

    @StaticNum.setter
    def StaticNum(self, StaticNum):
        self._StaticNum = StaticNum

    @property
    def RecordNum(self):
        """num
        :rtype: int
        """
        return self._RecordNum

    @RecordNum.setter
    def RecordNum(self, RecordNum):
        self._RecordNum = RecordNum

    @property
    def PageDuration(self):
        """Duration
        :rtype: str
        """
        return self._PageDuration

    @PageDuration.setter
    def PageDuration(self, PageDuration):
        self._PageDuration = PageDuration

    @property
    def CreateTime(self):
        """Time
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._StaticDuration = params.get("StaticDuration")
        self._PagePv = params.get("PagePv")
        self._ApiFail = params.get("ApiFail")
        self._ApiNum = params.get("ApiNum")
        self._StaticFail = params.get("StaticFail")
        self._ProjectID = params.get("ProjectID")
        self._PageUv = params.get("PageUv")
        self._ApiDuration = params.get("ApiDuration")
        self._Score = params.get("Score")
        self._PageError = params.get("PageError")
        self._StaticNum = params.get("StaticNum")
        self._RecordNum = params.get("RecordNum")
        self._PageDuration = params.get("PageDuration")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceRequest(AbstractModel):
    """StopInstance request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: ID of the instance to be stopped
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """ID of the instance to be stopped
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceResponse(AbstractModel):
    """StopInstance response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopProjectRequest(AbstractModel):
    """StopProject request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        """Project ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopProjectResponse(AbstractModel):
    """StopProject response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _Key: Tag key
        :type Key: str
        :param _Value: Tag value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Tag key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Tag value
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
        


class Whitelist(AbstractModel):
    """Allowlist

    """

    def __init__(self):
        r"""
        :param _Remark: Remarks
        :type Remark: str
        :param _InstanceID: Instance ID
        :type InstanceID: str
        :param _Ttl: End time
        :type Ttl: str
        :param _ID: Auto-Increment allowlist ID
        :type ID: str
        :param _WhitelistUin: Unique business identifier
        :type WhitelistUin: str
        :param _CreateUser: Creator ID
        :type CreateUser: str
        :param _Aid: aid
        :type Aid: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        """
        self._Remark = None
        self._InstanceID = None
        self._Ttl = None
        self._ID = None
        self._WhitelistUin = None
        self._CreateUser = None
        self._Aid = None
        self._CreateTime = None

    @property
    def Remark(self):
        """Remarks
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceID(self):
        """Instance ID
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Ttl(self):
        """End time
        :rtype: str
        """
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def ID(self):
        """Auto-Increment allowlist ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def WhitelistUin(self):
        """Unique business identifier
        :rtype: str
        """
        return self._WhitelistUin

    @WhitelistUin.setter
    def WhitelistUin(self, WhitelistUin):
        self._WhitelistUin = WhitelistUin

    @property
    def CreateUser(self):
        """Creator ID
        :rtype: str
        """
        return self._CreateUser

    @CreateUser.setter
    def CreateUser(self, CreateUser):
        self._CreateUser = CreateUser

    @property
    def Aid(self):
        """aid
        :rtype: str
        """
        return self._Aid

    @Aid.setter
    def Aid(self, Aid):
        self._Aid = Aid

    @property
    def CreateTime(self):
        """Creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Remark = params.get("Remark")
        self._InstanceID = params.get("InstanceID")
        self._Ttl = params.get("Ttl")
        self._ID = params.get("ID")
        self._WhitelistUin = params.get("WhitelistUin")
        self._CreateUser = params.get("CreateUser")
        self._Aid = params.get("Aid")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        