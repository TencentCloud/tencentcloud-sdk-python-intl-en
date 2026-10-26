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


class AddDeviceData(AbstractModel):
    r"""Data returned by the add device API

    """

    def __init__(self):
        r"""
        :param _DeviceId: <p>Device iD</p>
        :type DeviceId: str
        :param _Code: <p>Device code (for national standard devices, it is the 20-digit National Standard Encoding we generated for the device; for rtmp devices, it is the 10-digit device code)</p>
        :type Code: str
        :param _Name: <p>Device name.</p>
        :type Name: str
        :param _AccessProtocol: <p>Device access protocol. 1: RTMP; 2: GB.</p><p>Enumeration values:</p><ul><li>1: RTMP</li><li>2: GB</li><li>6: ISUP</li></ul>
        :type AccessProtocol: int
        :param _Type: <p>Device type. 1: IPC. 2: NVR</p>
        :type Type: int
        :param _ClusterId: <p>Device access service node ID</p>
        :type ClusterId: str
        :param _ClusterName: <p>Device access service node name</p>
        :type ClusterName: str
        :param _TransportProtocol: <p>Device streaming protocol. 1: UDP, 2: TCP</p>
        :type TransportProtocol: int
        :param _Password: <p>Device password.</p>
        :type Password: str
        :param _Description: <p>Device description</p>
        :type Description: str
        :param _Status: <p>Device status. 0: unregistered, 1: online, 2: offline, 3: disabled</p>
        :type Status: int
        :param _OrganizationId: <p>Affiliated organization ID of the device</p>
        :type OrganizationId: int
        :param _GatewayId: <p>Device access gateway ID (deprecated, reserved for compatibility, can be ignored)</p>
        :type GatewayId: str
        :param _ProtocolType: <p>Gateway access protocol type (deprecated, reserved for compatibility, can be ignored)</p>
        :type ProtocolType: int
        :param _Ip: <p>Device access IP (deprecated, reserved for compatibility, can be ignored)</p>
        :type Ip: str
        :param _Port: <p>Device Port (deprecated, reserved for compatibility, can be ignored)</p>
        :type Port: int
        :param _Username: <p>Device username (deprecated, reserved for compatibility, can be ignored)</p>
        :type Username: str
        :param _AppId: <p>User ID</p>
        :type AppId: int
        """
        self._DeviceId = None
        self._Code = None
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._ClusterId = None
        self._ClusterName = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._Status = None
        self._OrganizationId = None
        self._GatewayId = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._AppId = None

    @property
    def DeviceId(self):
        r"""<p>Device iD</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        r"""<p>Device code (for national standard devices, it is the 20-digit National Standard Encoding we generated for the device; for rtmp devices, it is the 10-digit device code)</p>
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        r"""<p>Device name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        r"""<p>Device access protocol. 1: RTMP; 2: GB.</p><p>Enumeration values:</p><ul><li>1: RTMP</li><li>2: GB</li><li>6: ISUP</li></ul>
        :rtype: int
        """
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        r"""<p>Device type. 1: IPC. 2: NVR</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClusterId(self):
        r"""<p>Device access service node ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""<p>Device access service node name</p>
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TransportProtocol(self):
        r"""<p>Device streaming protocol. 1: UDP, 2: TCP</p>
        :rtype: int
        """
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        r"""<p>Device password.</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""<p>Device description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""<p>Device status. 0: unregistered, 1: online, 2: offline, 3: disabled</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrganizationId(self):
        r"""<p>Affiliated organization ID of the device</p>
        :rtype: int
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def GatewayId(self):
        r"""<p>Device access gateway ID (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ProtocolType(self):
        r"""<p>Gateway access protocol type (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: int
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        r"""<p>Device access IP (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""<p>Device Port (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        r"""<p>Device username (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def AppId(self):
        r"""<p>User ID</p>
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._OrganizationId = params.get("OrganizationId")
        self._GatewayId = params.get("GatewayId")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrgData(AbstractModel):
    r"""Add the return data of the organizational unit interface

    """

    def __init__(self):
        r"""
        :param _OrganizationId: Organization ID
        :type OrganizationId: str
        :param _Name: Organization name
        :type Name: str
        :param _ParentId: Organization parent node ID
        :type ParentId: str
        :param _Level: Organization hierarchy
        :type Level: int
        :param _AppId: User ID.
        :type AppId: int
        :param _ParentIds: Organizational structure
        :type ParentIds: str
        :param _Total: Total number of devices
        :type Total: int
        :param _Online: Number of devices online
        :type Online: int
        """
        self._OrganizationId = None
        self._Name = None
        self._ParentId = None
        self._Level = None
        self._AppId = None
        self._ParentIds = None
        self._Total = None
        self._Online = None

    @property
    def OrganizationId(self):
        r"""Organization ID
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        r"""Organization name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        r"""Organization parent node ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Level(self):
        r"""Organization hierarchy
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def AppId(self):
        r"""User ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ParentIds(self):
        r"""Organizational structure
        :rtype: str
        """
        return self._ParentIds

    @ParentIds.setter
    def ParentIds(self, ParentIds):
        self._ParentIds = ParentIds

    @property
    def Total(self):
        r"""Total number of devices
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Online(self):
        r"""Number of devices online
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._Level = params.get("Level")
        self._AppId = params.get("AppId")
        self._ParentIds = params.get("ParentIds")
        self._Total = params.get("Total")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationRequest(AbstractModel):
    r"""AddOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Organization name. Only Chinese, English, digits, spaces, Chinese and English parentheses, underscores (_), and hyphens (-) are supported. The length cannot exceed 64 characters, and the organization name must be unique.
        :type Name: str
        :param _ParentId: Organization parent node ID (obtain from the DescribeOrganization API; enter 0 for the root organization)
        :type ParentId: str
        """
        self._Name = None
        self._ParentId = None

    @property
    def Name(self):
        r"""Organization name. Only Chinese, English, digits, spaces, Chinese and English parentheses, underscores (_), and hyphens (-) are supported. The length cannot exceed 64 characters, and the organization name must be unique.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        r"""Organization parent node ID (obtain from the DescribeOrganization API; enter 0 for the root organization)
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationResponse(AbstractModel):
    r"""AddOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Interface return data for adding an organizational unit
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddOrgData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Interface return data for adding an organizational unit
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddOrgData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AddOrgData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordBackupPlanData(AbstractModel):
    r"""data for the newly-added recording cloud migration plan

    """

    def __init__(self):
        r"""
        :param _PlanId: Recording cloud migration plan ID
        :type PlanId: str
        :param _PlanName: Recording cloud migration plan name
        :type PlanName: str
        :param _TemplateId: Video cloud template ID
        :type TemplateId: str
        :param _Describe: Description of the recording cloud migration plan
        :type Describe: str
        :param _LifeCycle: Cloud file lifecycle
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: Recording cloud migration plan status. `1`: in normal use. `0`: deleting, unavailable.
        :type Status: int
        :param _ChannelCount: Number of channels
        :type ChannelCount: int
        :param _CreateAt: Creation time.
        :type CreateAt: str
        :param _UpdateAt: Modification time.
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        r"""Recording cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""Recording cloud migration plan name
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Video cloud template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Description of the recording cloud migration plan
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        r"""Cloud file lifecycle
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        r"""Recording cloud migration plan status. `1`: in normal use. `0`: deleting, unavailable.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        r"""Number of channels
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""Modification time.
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupPlanRequest(AbstractModel):
    r"""AddRecordBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Recording template ID (template ID associated with the recording schedule, obtained from the ListRecordBackupTemplates API for querying the video cloud template list)
        :type TemplateId: str
        :param _PlanName: Recording schedule name (supports Chinese, English, digits, _ and -. The length cannot exceed 32 characters. The plan name must be globally unique and cannot be empty or duplicated.)
        :type PlanName: str
        :param _Describe: Video recording plan description (only supports Chinese, English, digits, _, -, length not exceeding 128 characters)
        :type Describe: str
        :param _LifeCycle: Lifecycle (video recording file lifecycle settings, the time when cold and hot storage is managed for files)
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Channels: Channel and the device to which the channel belongs (channel information of the device to which a video recording is added. Add no more than 5,000 channels at a time, including the number of channels under the organizational unit directory).
        :type Channels: list of ChannelInfo
        :param _OrganizationId: Add all device channels under the organizational unit directory (Json array, can be empty, total number of channels no more than 5000, including the number of Channel fields)
        :type OrganizationId: list of str
        """
        self._TemplateId = None
        self._PlanName = None
        self._Describe = None
        self._LifeCycle = None
        self._Channels = None
        self._OrganizationId = None

    @property
    def TemplateId(self):
        r"""Recording template ID (template ID associated with the recording schedule, obtained from the ListRecordBackupTemplates API for querying the video cloud template list)
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def PlanName(self):
        r"""Recording schedule name (supports Chinese, English, digits, _ and -. The length cannot exceed 32 characters. The plan name must be globally unique and cannot be empty or duplicated.)
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def Describe(self):
        r"""Video recording plan description (only supports Chinese, English, digits, _, -, length not exceeding 128 characters)
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        r"""Lifecycle (video recording file lifecycle settings, the time when cold and hot storage is managed for files)
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Channels(self):
        r"""Channel and the device to which the channel belongs (channel information of the device to which a video recording is added. Add no more than 5,000 channels at a time, including the number of channels under the organizational unit directory).
        :rtype: list of ChannelInfo
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def OrganizationId(self):
        r"""Add all device channels under the organizational unit directory (Json array, can be empty, total number of channels no more than 5000, including the number of Channel fields)
        :rtype: list of str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._PlanName = params.get("PlanName")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupPlanResponse(AbstractModel):
    r"""AddRecordBackupPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupPlanData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupPlanData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AddRecordBackupPlanData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordBackupTemplateData(AbstractModel):
    r"""data for creating a video cloud template

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>Template ID</p>
        :type TemplateId: str
        :param _TemplateName: <p>Template name</p>
        :type TemplateName: str
        :param _TimeSections: <p>Cloud Upload Time Period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: <p>Recording time period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: <p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :type Scale: int
        :param _CreateAt: <p>Creation time.</p>
        :type CreateAt: str
        :param _UpdateAt: <p>Update time.</p>
        :type UpdateAt: str
        :param _DayOffset: <p>Cycle offset. Default value: 1, which means to pull yesterday's video recording from the device. 0 means to pull today's video recording from the device. 3 means to pull the video recording from the device from the day before yesterday.</p><p>Default value: 1</p>
        :type DayOffset: int
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None
        self._DayOffset = None

    @property
    def TemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""<p>Template name</p>
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""<p>Cloud Upload Time Period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        r"""<p>Recording time period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        r"""<p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DayOffset(self):
        r"""<p>Cycle offset. Default value: 1, which means to pull yesterday's video recording from the device. 0 means to pull today's video recording from the device. 3 means to pull the video recording from the device from the day before yesterday.</p><p>Default value: 1</p>
        :rtype: int
        """
        return self._DayOffset

    @DayOffset.setter
    def DayOffset(self, DayOffset):
        self._DayOffset = DayOffset


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._DayOffset = params.get("DayOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupTemplateRequest(AbstractModel):
    r"""AddRecordBackupTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateName: <p>Template name (supports only Chinese, English, number, _, -, length not exceeding 32 characters. Template name must be globally unique, cannot be empty, and must be unique)</p>
        :type TemplateName: str
        :param _TimeSections: <p>Cloud Upload Time Period (settings can be done by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: <p>Recording time period (settings can be done by week, support setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: <p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :type Scale: int
        :param _DayOffset: <p>Cycle offset. Default: 1. It means to pull yesterday's video recording to the device. 0 means to pull today's video recording to the device. 3 means to pull the video recording to the device from the day before yesterday.</p><p>Value range: [0, 90]</p><p>Default value: 1</p>
        :type DayOffset: int
        """
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._DayOffset = None

    @property
    def TemplateName(self):
        r"""<p>Template name (supports only Chinese, English, number, _, -, length not exceeding 32 characters. Template name must be globally unique, cannot be empty, and must be unique)</p>
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""<p>Cloud Upload Time Period (settings can be done by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        r"""<p>Recording time period (settings can be done by week, support setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        r"""<p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def DayOffset(self):
        r"""<p>Cycle offset. Default: 1. It means to pull yesterday's video recording to the device. 0 means to pull today's video recording to the device. 3 means to pull the video recording to the device from the day before yesterday.</p><p>Value range: [0, 90]</p><p>Default value: 1</p>
        :rtype: int
        """
        return self._DayOffset

    @DayOffset.setter
    def DayOffset(self, DayOffset):
        self._DayOffset = DayOffset


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._DayOffset = params.get("DayOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordBackupTemplateResponse(AbstractModel):
    r"""AddRecordBackupTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Response data.</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupTemplateData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Response data.</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordBackupTemplateData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AddRecordBackupTemplateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordPlanRequest(AbstractModel):
    r"""AddRecordPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanName: Real-time cloud migration plan name. It supports Chinese, English, digits, _, and -, with a length not exceeding 32 characters. The plan name must be globally unique and cannot be empty or repeated.
        :type PlanName: str
        :param _TemplateId: Real-time cloud template ID
        :type TemplateId: str
        :param _LifeCycle: Lifecycle
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Describe: Cloud plan description. Supports only Chinese, English, digits, _, and -. Length not exceeding 128 characters.
        :type Describe: str
        :param _StreamType: Stream type. default: The stream type is not specified, and the default push type of the device is used. main: Main stream. sub: Substream. Other values are customized based on the device capacity. If not specified, the default type is used. The length cannot exceed 32 bytes.
        :type StreamType: str
        :param _Channels: Channel information of the device to which video recording is added. You can add no more than 5000 channels only once, including the number of channels under the organizational unit directory.
        :type Channels: list of ChannelInfo
        :param _OrganizationId: Add all device channels under the organization. Json array, can be empty. The total number of channels cannot exceed 5,000 (including the number of Channel fields).
        :type OrganizationId: list of str
        :param _RepairMode: Video recording supplement mode (0: disabled, 1: enabled). If this field is not specified, it is not enabled by default.
        :type RepairMode: int
        """
        self._PlanName = None
        self._TemplateId = None
        self._LifeCycle = None
        self._Describe = None
        self._StreamType = None
        self._Channels = None
        self._OrganizationId = None
        self._RepairMode = None

    @property
    def PlanName(self):
        r"""Real-time cloud migration plan name. It supports Chinese, English, digits, _, and -, with a length not exceeding 32 characters. The plan name must be globally unique and cannot be empty or repeated.
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Real-time cloud template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def LifeCycle(self):
        r"""Lifecycle
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Describe(self):
        r"""Cloud plan description. Supports only Chinese, English, digits, _, and -. Length not exceeding 128 characters.
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def StreamType(self):
        r"""Stream type. default: The stream type is not specified, and the default push type of the device is used. main: Main stream. sub: Substream. Other values are customized based on the device capacity. If not specified, the default type is used. The length cannot exceed 32 bytes.
        :rtype: str
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Channels(self):
        r"""Channel information of the device to which video recording is added. You can add no more than 5000 channels only once, including the number of channels under the organizational unit directory.
        :rtype: list of ChannelInfo
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def OrganizationId(self):
        r"""Add all device channels under the organization. Json array, can be empty. The total number of channels cannot exceed 5,000 (including the number of Channel fields).
        :rtype: list of str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def RepairMode(self):
        r"""Video recording supplement mode (0: disabled, 1: enabled). If this field is not specified, it is not enabled by default.
        :rtype: int
        """
        return self._RepairMode

    @RepairMode.setter
    def RepairMode(self, RepairMode):
        self._RepairMode = RepairMode


    def _deserialize(self, params):
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Describe = params.get("Describe")
        self._StreamType = params.get("StreamType")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._OrganizationId = params.get("OrganizationId")
        self._RepairMode = params.get("RepairMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordPlanResponse(AbstractModel):
    r"""AddRecordPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlanOptData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.RecordPlanOptData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RecordPlanOptData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordRetrieveTaskData(AbstractModel):
    r"""data for querying retrieval task details

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _TaskName: Task name.
        :type TaskName: str
        :param _StartTime: Start time of video recording retrieval
        :type StartTime: int
        :param _EndTime: Retrieval end time of the video recording
        :type EndTime: int
        :param _Mode: Retrieval mode. 1: ultrafast mode. Others not supported currently.
        :type Mode: int
        :param _Expiration: Replica validity period
        :type Expiration: int
        :param _Status: Task status. 0: retrieved, 1: retrieving, 2: pending retrieval
        :type Status: int
        :param _Capacity: Retrieval capacity, in MB.
        :type Capacity: float
        :param _Describe: Task description
        :type Describe: str
        """
        self._TaskId = None
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Status = None
        self._Capacity = None
        self._Describe = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        r"""Start time of video recording retrieval
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Retrieval end time of the video recording
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        r"""Retrieval mode. 1: ultrafast mode. Others not supported currently.
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        r"""Replica validity period
        :rtype: int
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Status(self):
        r"""Task status. 0: retrieved, 1: retrieving, 2: pending retrieval
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Capacity(self):
        r"""Retrieval capacity, in MB.
        :rtype: float
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Describe(self):
        r"""Task description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        self._Status = params.get("Status")
        self._Capacity = params.get("Capacity")
        self._Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordRetrieveTaskRequest(AbstractModel):
    r"""AddRecordRetrieveTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskName: Task name. It supports Chinese, English, digits, _, and -, with a length not exceeding 32 characters. The name must be globally unique and cannot be empty or repeated.
        :type TaskName: str
        :param _StartTime: Start time for retrieving the video recording in UTC seconds, for example: 1662114146. The longest period between the start and end times is one day and cannot span multiple days.
        :type StartTime: int
        :param _EndTime: End time for retrieving the video recording, in UTC seconds, for example: 1662114146. The period between the start and end times can be up to one day and cannot span multiple days.
        :type EndTime: int
        :param _Mode: Retrieval mode. 1: ultrafast mode. Others not supported currently.
        :type Mode: int
        :param _Expiration: Retrieval replica validity period of the video recording. Minimum: 1 day. Maximum: 365 days.
        :type Expiration: int
        :param _Channels: Device channel. A task can contain up to 32 device channels.
        :type Channels: list of ChannelInfo
        :param _Describe: Retrieve the task description
        :type Describe: str
        """
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Channels = None
        self._Describe = None

    @property
    def TaskName(self):
        r"""Task name. It supports Chinese, English, digits, _, and -, with a length not exceeding 32 characters. The name must be globally unique and cannot be empty or repeated.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        r"""Start time for retrieving the video recording in UTC seconds, for example: 1662114146. The longest period between the start and end times is one day and cannot span multiple days.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time for retrieving the video recording, in UTC seconds, for example: 1662114146. The period between the start and end times can be up to one day and cannot span multiple days.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        r"""Retrieval mode. 1: ultrafast mode. Others not supported currently.
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        r"""Retrieval replica validity period of the video recording. Minimum: 1 day. Maximum: 365 days.
        :rtype: int
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Channels(self):
        r"""Device channel. A task can contain up to 32 device channels.
        :rtype: list of ChannelInfo
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def Describe(self):
        r"""Retrieve the task description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe


    def _deserialize(self, params):
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordRetrieveTaskResponse(AbstractModel):
    r"""AddRecordRetrieveTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned results
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddRecordRetrieveTaskData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned results
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddRecordRetrieveTaskData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AddRecordRetrieveTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddRecordTemplateRequest(AbstractModel):
    r"""AddRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name. It can contain only Chinese characters, letters, digits, underscores (_), and hyphens (-), with a length not exceeding 32 characters. The template name must be globally unique and cannot be empty or duplicated.
        :type TemplateName: str
        :param _TimeSections: Cloud upload time period. Settings can be done by week. Multiple time periods can be set for each day, with each time period not less than 10 minutes.
        :type TimeSections: list of RecordTemplateTimeSections
        """
        self._TemplateName = None
        self._TimeSections = None

    @property
    def TemplateName(self):
        r"""Template name. It can contain only Chinese characters, letters, digits, underscores (_), and hyphens (-), with a length not exceeding 32 characters. The template name must be globally unique and cannot be empty or duplicated.
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""Cloud upload time period. Settings can be done by week. Multiple time periods can be set for each day, with each time period not less than 10 minutes.
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRecordTemplateResponse(AbstractModel):
    r"""AddRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RecordTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddStreamAuthData(AbstractModel):
    r"""Data structure returned by push/pull stream authentication settings

    """

    def __init__(self):
        r"""
        :param _Id: Authentication configuration ID (uuid).
        :type Id: str
        :param _PullState: Whether to enable playback authentication. Valid values: `1`: enable, `0`: disable.
        :type PullState: int
        :param _PullSecret: Playback key (alphanumeric only, length: 0-10 characters)
        :type PullSecret: str
        :param _PullExpired: Playback expiration time (unit: minute)
        :type PullExpired: int
        :param _PushState: Whether to enable stream authentication (1: enable, 0: disable)
        :type PushState: int
        :param _PushSecret: Stream key (only alphanumeric characters are supported, with a length of 0-10 characters)
        :type PushSecret: str
        :param _PushExpired: Push expiration time (unit: minute)
        :type PushExpired: int
        :param _AppId: User ID.
        :type AppId: int
        """
        self._Id = None
        self._PullState = None
        self._PullSecret = None
        self._PullExpired = None
        self._PushState = None
        self._PushSecret = None
        self._PushExpired = None
        self._AppId = None

    @property
    def Id(self):
        r"""Authentication configuration ID (uuid).
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PullState(self):
        r"""Whether to enable playback authentication. Valid values: `1`: enable, `0`: disable.
        :rtype: int
        """
        return self._PullState

    @PullState.setter
    def PullState(self, PullState):
        self._PullState = PullState

    @property
    def PullSecret(self):
        r"""Playback key (alphanumeric only, length: 0-10 characters)
        :rtype: str
        """
        return self._PullSecret

    @PullSecret.setter
    def PullSecret(self, PullSecret):
        self._PullSecret = PullSecret

    @property
    def PullExpired(self):
        r"""Playback expiration time (unit: minute)
        :rtype: int
        """
        return self._PullExpired

    @PullExpired.setter
    def PullExpired(self, PullExpired):
        self._PullExpired = PullExpired

    @property
    def PushState(self):
        r"""Whether to enable stream authentication (1: enable, 0: disable)
        :rtype: int
        """
        return self._PushState

    @PushState.setter
    def PushState(self, PushState):
        self._PushState = PushState

    @property
    def PushSecret(self):
        r"""Stream key (only alphanumeric characters are supported, with a length of 0-10 characters)
        :rtype: str
        """
        return self._PushSecret

    @PushSecret.setter
    def PushSecret(self, PushSecret):
        self._PushSecret = PushSecret

    @property
    def PushExpired(self):
        r"""Push expiration time (unit: minute)
        :rtype: int
        """
        return self._PushExpired

    @PushExpired.setter
    def PushExpired(self, PushExpired):
        self._PushExpired = PushExpired

    @property
    def AppId(self):
        r"""User ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PullState = params.get("PullState")
        self._PullSecret = params.get("PullSecret")
        self._PullExpired = params.get("PullExpired")
        self._PushState = params.get("PushState")
        self._PushSecret = params.get("PushSecret")
        self._PushExpired = params.get("PushExpired")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddStreamAuthRequest(AbstractModel):
    r"""AddStreamAuth request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Authentication configuration ID (uuid).
        :type Id: str
        :param _PullState: Whether to enable playback authentication (1: enable, 0: disable)
        :type PullState: int
        :param _PullSecret: Playback key (only alphanumeric characters are supported, with a length of 0-10 characters)
        :type PullSecret: str
        :param _PullExpired: Playback expiration time (unit: minute)
        :type PullExpired: int
        :param _PushState: Whether to enable stream authentication (1: enable, 0: disable)
        :type PushState: int
        :param _PushSecret: Stream key (alphanumeric only, length 0-10 characters)
        :type PushSecret: str
        :param _PushExpired: Push expiration time (unit: minute)
        :type PushExpired: int
        """
        self._Id = None
        self._PullState = None
        self._PullSecret = None
        self._PullExpired = None
        self._PushState = None
        self._PushSecret = None
        self._PushExpired = None

    @property
    def Id(self):
        r"""Authentication configuration ID (uuid).
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PullState(self):
        r"""Whether to enable playback authentication (1: enable, 0: disable)
        :rtype: int
        """
        return self._PullState

    @PullState.setter
    def PullState(self, PullState):
        self._PullState = PullState

    @property
    def PullSecret(self):
        r"""Playback key (only alphanumeric characters are supported, with a length of 0-10 characters)
        :rtype: str
        """
        return self._PullSecret

    @PullSecret.setter
    def PullSecret(self, PullSecret):
        self._PullSecret = PullSecret

    @property
    def PullExpired(self):
        r"""Playback expiration time (unit: minute)
        :rtype: int
        """
        return self._PullExpired

    @PullExpired.setter
    def PullExpired(self, PullExpired):
        self._PullExpired = PullExpired

    @property
    def PushState(self):
        r"""Whether to enable stream authentication (1: enable, 0: disable)
        :rtype: int
        """
        return self._PushState

    @PushState.setter
    def PushState(self, PushState):
        self._PushState = PushState

    @property
    def PushSecret(self):
        r"""Stream key (alphanumeric only, length 0-10 characters)
        :rtype: str
        """
        return self._PushSecret

    @PushSecret.setter
    def PushSecret(self, PushSecret):
        self._PushSecret = PushSecret

    @property
    def PushExpired(self):
        r"""Push expiration time (unit: minute)
        :rtype: int
        """
        return self._PushExpired

    @PushExpired.setter
    def PushExpired(self, PushExpired):
        self._PushExpired = PushExpired


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PullState = params.get("PullState")
        self._PullSecret = params.get("PullSecret")
        self._PullExpired = params.get("PullExpired")
        self._PushState = params.get("PushState")
        self._PushSecret = params.get("PushSecret")
        self._PushExpired = params.get("PushExpired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddStreamAuthResponse(AbstractModel):
    r"""AddStreamAuth response structure.

    """

    def __init__(self):
        r"""
        :param _Data: data for setting push/pull stream authentication
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddStreamAuthData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""data for setting push/pull stream authentication
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddStreamAuthData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AddStreamAuthData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class AddUserDeviceRequest(AbstractModel):
    r"""AddUserDevice request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Device name, only supports Chinese, English, numbers, spaces, Chinese and English parentheses, _, -, length not exceeding 128 characters; (device name no need to be globally unique and can be duplicated)</p>
        :type Name: str
        :param _AccessProtocol: <p>Device access protocol (1: RTMP, 2: GB, 6: ISUP)</p><p>Enumeration values:</p><ul><li>1: RTMP</li><li>2: GB</li><li>6: ISUP</li></ul><p>Default value: 2</p>
        :type AccessProtocol: int
        :param _Type: <p>Device type. 1: IPC; 2: NVR. (If the device access protocol is RTMP, only select IPC as the device type.)</p><p>Enumeration values:</p><ul><li>1: IPC</li><li>2: NVR</li></ul>
        :type Type: int
        :param _OrganizationId: <p>ID of the organization to which the device belongs. Obtain from the organization query api DescribeOrganization.</p>
        :type OrganizationId: str
        :param _ClusterId: <p>Device access service node ID (Value field obtained from the DescribeRegionDomain API for querying available service nodes of a device)</p>
        :type ClusterId: str
        :param _TransportProtocol: <p>Device streaming protocol. 1: UDP, 2: TCP. (Valid for national standard devices. UDP by default if not specified)</p>
        :type TransportProtocol: int
        :param _Password: <p>Device password (required for national standard devices, length of 1-64 characters)</p>
        :type Password: str
        :param _Description: <p>Device description, length not exceeding 128 characters</p>
        :type Description: str
        :param _GatewayId: <p>Device access gateway ID (deprecated, reserved for compatibility, can be ignored)</p>
        :type GatewayId: str
        :param _ProtocolType: <p>Gateway access protocol type (deprecated, reserved for compatibility, can be ignored)</p>
        :type ProtocolType: int
        :param _Ip: <p>Device access IP (deprecated, reserved for compatibility, can be ignored)</p>
        :type Ip: str
        :param _Port: <p>Device port (deprecated, reserved for compatibility, can be ignored)</p><p>Value range: [1, 65535]</p><p>Unit: port</p>
        :type Port: int
        :param _Username: <p>Device username (deprecated, reserved for compatibility, can be ignored)</p>
        :type Username: str
        :param _SNCode: <p>Device SN (deprecated, reserved for compatibility, can be ignored)</p>
        :type SNCode: str
        :param _AppName: <p>Custom AppName for RTMP publishing address (required for RTMP only, support English, digits, _, -, ., length not exceeding 64 characters)</p>
        :type AppName: str
        :param _StreamName: <p>Custom StreamName for RTMP publishing address (required for RTMP only, supports English, digits, _, -, ., length not exceeding 64 characters)</p>
        :type StreamName: str
        """
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._OrganizationId = None
        self._ClusterId = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._GatewayId = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._SNCode = None
        self._AppName = None
        self._StreamName = None

    @property
    def Name(self):
        r"""<p>Device name, only supports Chinese, English, numbers, spaces, Chinese and English parentheses, _, -, length not exceeding 128 characters; (device name no need to be globally unique and can be duplicated)</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        r"""<p>Device access protocol (1: RTMP, 2: GB, 6: ISUP)</p><p>Enumeration values:</p><ul><li>1: RTMP</li><li>2: GB</li><li>6: ISUP</li></ul><p>Default value: 2</p>
        :rtype: int
        """
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        r"""<p>Device type. 1: IPC; 2: NVR. (If the device access protocol is RTMP, only select IPC as the device type.)</p><p>Enumeration values:</p><ul><li>1: IPC</li><li>2: NVR</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def OrganizationId(self):
        r"""<p>ID of the organization to which the device belongs. Obtain from the organization query api DescribeOrganization.</p>
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def ClusterId(self):
        r"""<p>Device access service node ID (Value field obtained from the DescribeRegionDomain API for querying available service nodes of a device)</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def TransportProtocol(self):
        r"""<p>Device streaming protocol. 1: UDP, 2: TCP. (Valid for national standard devices. UDP by default if not specified)</p>
        :rtype: int
        """
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        r"""<p>Device password (required for national standard devices, length of 1-64 characters)</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""<p>Device description, length not exceeding 128 characters</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GatewayId(self):
        r"""<p>Device access gateway ID (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ProtocolType(self):
        r"""<p>Gateway access protocol type (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: int
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        r"""<p>Device access IP (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""<p>Device port (deprecated, reserved for compatibility, can be ignored)</p><p>Value range: [1, 65535]</p><p>Unit: port</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        r"""<p>Device username (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def SNCode(self):
        r"""<p>Device SN (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._SNCode

    @SNCode.setter
    def SNCode(self, SNCode):
        self._SNCode = SNCode

    @property
    def AppName(self):
        r"""<p>Custom AppName for RTMP publishing address (required for RTMP only, support English, digits, _, -, ., length not exceeding 64 characters)</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        r"""<p>Custom StreamName for RTMP publishing address (required for RTMP only, supports English, digits, _, -, ., length not exceeding 64 characters)</p>
        :rtype: str
        """
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._OrganizationId = params.get("OrganizationId")
        self._ClusterId = params.get("ClusterId")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._GatewayId = params.get("GatewayId")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._SNCode = params.get("SNCode")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserDeviceResponse(AbstractModel):
    r"""AddUserDevice response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Add device response data.</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.AddDeviceData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Add device response data.</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.AddDeviceData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = AddDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class BatchAddVideoSnapshotConfigChannelRequest(AbstractModel):
    r"""BatchAddVideoSnapshotConfigChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: <p>Screenshot configuration Id</p>
        :type ConfigId: str
        :param _Channels: <p>Channel Id list</p>
        :type Channels: list of str
        """
        self._ConfigId = None
        self._Channels = None

    @property
    def ConfigId(self):
        r"""<p>Screenshot configuration Id</p>
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Channels(self):
        r"""<p>Channel Id list</p>
        :rtype: list of str
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Channels = params.get("Channels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAddVideoSnapshotConfigChannelResponse(AbstractModel):
    r"""BatchAddVideoSnapshotConfigChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class BatchAssignVLPlanChannelsRequest(AbstractModel):
    r"""BatchAssignVLPlanChannels request structure.

    """

    def __init__(self):
        r"""
        :param _VLPlanId: <p>Plan ID</p>
        :type VLPlanId: str
        :param _Cmd: <p>Operation command: 1=associate, 2=unbind</p>
        :type Cmd: int
        :param _ChannelIds: <p>Channel ID list, up to 500; pass at least one of this parameter and OrganizationIds (when Cmd=1)</p>
        :type ChannelIds: list of str
        :param _OrganizationIds: <p>List of organization IDs (valid only when Cmd=1; does not allow input when Cmd=2); unfold all channels under the organization to participate in association, and take the union with ChannelIds and remove duplicates</p>
        :type OrganizationIds: list of str
        """
        self._VLPlanId = None
        self._Cmd = None
        self._ChannelIds = None
        self._OrganizationIds = None

    @property
    def VLPlanId(self):
        r"""<p>Plan ID</p>
        :rtype: str
        """
        return self._VLPlanId

    @VLPlanId.setter
    def VLPlanId(self, VLPlanId):
        self._VLPlanId = VLPlanId

    @property
    def Cmd(self):
        r"""<p>Operation command: 1=associate, 2=unbind</p>
        :rtype: int
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def ChannelIds(self):
        r"""<p>Channel ID list, up to 500; pass at least one of this parameter and OrganizationIds (when Cmd=1)</p>
        :rtype: list of str
        """
        return self._ChannelIds

    @ChannelIds.setter
    def ChannelIds(self, ChannelIds):
        self._ChannelIds = ChannelIds

    @property
    def OrganizationIds(self):
        r"""<p>List of organization IDs (valid only when Cmd=1; does not allow input when Cmd=2); unfold all channels under the organization to participate in association, and take the union with ChannelIds and remove duplicates</p>
        :rtype: list of str
        """
        return self._OrganizationIds

    @OrganizationIds.setter
    def OrganizationIds(self, OrganizationIds):
        self._OrganizationIds = OrganizationIds


    def _deserialize(self, params):
        self._VLPlanId = params.get("VLPlanId")
        self._Cmd = params.get("Cmd")
        self._ChannelIds = params.get("ChannelIds")
        self._OrganizationIds = params.get("OrganizationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchAssignVLPlanChannelsResponse(AbstractModel):
    r"""BatchAssignVLPlanChannels response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class BatchDeleteVideoDownloadTaskRequest(AbstractModel):
    r"""BatchDeleteVideoDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _DownloadTaskIds: List of local recording download task IDs
        :type DownloadTaskIds: list of str
        """
        self._DownloadTaskIds = None

    @property
    def DownloadTaskIds(self):
        r"""List of local recording download task IDs
        :rtype: list of str
        """
        return self._DownloadTaskIds

    @DownloadTaskIds.setter
    def DownloadTaskIds(self, DownloadTaskIds):
        self._DownloadTaskIds = DownloadTaskIds


    def _deserialize(self, params):
        self._DownloadTaskIds = params.get("DownloadTaskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeleteVideoDownloadTaskResponse(AbstractModel):
    r"""BatchDeleteVideoDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class BatchGetVLPlanSourceFileURLRequest(AbstractModel):
    r"""BatchGetVLPlanSourceFileURL request structure.

    """

    def __init__(self):
        r"""
        :param _VLPlanResultIds: <p>Analysis result ID list. Up to 200.</p>
        :type VLPlanResultIds: list of str
        :param _Expire: <p>URL validity period (in seconds). Value range: [60, 86400]. Default: 600</p>
        :type Expire: int
        """
        self._VLPlanResultIds = None
        self._Expire = None

    @property
    def VLPlanResultIds(self):
        r"""<p>Analysis result ID list. Up to 200.</p>
        :rtype: list of str
        """
        return self._VLPlanResultIds

    @VLPlanResultIds.setter
    def VLPlanResultIds(self, VLPlanResultIds):
        self._VLPlanResultIds = VLPlanResultIds

    @property
    def Expire(self):
        r"""<p>URL validity period (in seconds). Value range: [60, 86400]. Default: 600</p>
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire


    def _deserialize(self, params):
        self._VLPlanResultIds = params.get("VLPlanResultIds")
        self._Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchGetVLPlanSourceFileURLResponse(AbstractModel):
    r"""BatchGetVLPlanSourceFileURL response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>URL list</p>
        :type Data: list of VLPlanResultSnapshotImageUrlInfo
        :param _TotalCount: <p>Total quantity.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>URL list</p>
        :rtype: list of VLPlanResultSnapshotImageUrlInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""<p>Total quantity.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VLPlanResultSnapshotImageUrlInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class BatchGetVideoSnapshotImageUrlData(AbstractModel):
    r"""Batch obtain the screenshot image URL information list

    """

    def __init__(self):
        r"""
        :param _Images: <p>Image Url information</p>
        :type Images: list of ImageUrlInfo
        :param _ImageUrlExpires: <p>Valid period of the image Url</p><p>Unit: seconds</p><p>Default value: 600</p>
        :type ImageUrlExpires: int
        """
        self._Images = None
        self._ImageUrlExpires = None

    @property
    def Images(self):
        r"""<p>Image Url information</p>
        :rtype: list of ImageUrlInfo
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def ImageUrlExpires(self):
        r"""<p>Valid period of the image Url</p><p>Unit: seconds</p><p>Default value: 600</p>
        :rtype: int
        """
        return self._ImageUrlExpires

    @ImageUrlExpires.setter
    def ImageUrlExpires(self, ImageUrlExpires):
        self._ImageUrlExpires = ImageUrlExpires


    def _deserialize(self, params):
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = ImageUrlInfo()
                obj._deserialize(item)
                self._Images.append(obj)
        self._ImageUrlExpires = params.get("ImageUrlExpires")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchGetVideoSnapshotImageUrlRequest(AbstractModel):
    r"""BatchGetVideoSnapshotImageUrl request structure.

    """

    def __init__(self):
        r"""
        :param _ImageIds: <p>Image Id</p>
        :type ImageIds: list of str
        :param _ImageUrlExpires: <p>Valid period of the image URL, unit: seconds</p><p>Value range: [60, 86400]</p><p>Default value: 600</p>
        :type ImageUrlExpires: int
        """
        self._ImageIds = None
        self._ImageUrlExpires = None

    @property
    def ImageIds(self):
        r"""<p>Image Id</p>
        :rtype: list of str
        """
        return self._ImageIds

    @ImageIds.setter
    def ImageIds(self, ImageIds):
        self._ImageIds = ImageIds

    @property
    def ImageUrlExpires(self):
        r"""<p>Valid period of the image URL, unit: seconds</p><p>Value range: [60, 86400]</p><p>Default value: 600</p>
        :rtype: int
        """
        return self._ImageUrlExpires

    @ImageUrlExpires.setter
    def ImageUrlExpires(self, ImageUrlExpires):
        self._ImageUrlExpires = ImageUrlExpires


    def _deserialize(self, params):
        self._ImageIds = params.get("ImageIds")
        self._ImageUrlExpires = params.get("ImageUrlExpires")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchGetVideoSnapshotImageUrlResponse(AbstractModel):
    r"""BatchGetVideoSnapshotImageUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>List of screenshot image URL results</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.BatchGetVideoSnapshotImageUrlData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>List of screenshot image URL results</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchGetVideoSnapshotImageUrlData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = BatchGetVideoSnapshotImageUrlData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class BatchOperateDeviceData(AbstractModel):
    r"""Result returned by the batch operation device

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID (used to query task progress in the ListSubTasks API for querying the subtask list of a job)
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Task ID (used to query task progress in the ListSubTasks API for querying the subtask list of a job)
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchOperateDeviceRequest(AbstractModel):
    r"""BatchOperateDevice request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceIds: <p>Device ID array (obtain from the device list API ListDevices)</p><p>For parameter values, see <a href="https://www.tencentcloud.com/document/api/1344/95871?from_cn_redirect=1">ListDevices</a></p>
        :type DeviceIds: list of str
        :param _Cmd: <p>Operation command</p><p>Enumeration values:</p><ul><li>enable: Enable</li><li>disable: Disable</li><li>delete: Delete</li><li>sync: Synchronize device channel</li></ul>
        :type Cmd: str
        """
        self._DeviceIds = None
        self._Cmd = None

    @property
    def DeviceIds(self):
        r"""<p>Device ID array (obtain from the device list API ListDevices)</p><p>For parameter values, see <a href="https://www.tencentcloud.com/document/api/1344/95871?from_cn_redirect=1">ListDevices</a></p>
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds

    @property
    def Cmd(self):
        r"""<p>Operation command</p><p>Enumeration values:</p><ul><li>enable: Enable</li><li>disable: Disable</li><li>delete: Delete</li><li>sync: Synchronize device channel</li></ul>
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        self._Cmd = params.get("Cmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchOperateDeviceResponse(AbstractModel):
    r"""BatchOperateDevice response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Returned results.</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.BatchOperateDeviceData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Returned results.</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.BatchOperateDeviceData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = BatchOperateDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class BitRateInfo(AbstractModel):
    r"""Video channel bitrate returned results

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel Id
        :type ChannelId: str
        :param _Bitrate: Bitrate, in kbps.
        :type Bitrate: float
        """
        self._ChannelId = None
        self._Bitrate = None

    @property
    def ChannelId(self):
        r"""Channel Id
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Bitrate(self):
        r"""Bitrate, in kbps.
        :rtype: float
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Bitrate = params.get("Bitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallISAPIRequest(AbstractModel):
    r"""CallISAPI request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID
        :type DeviceId: str
        :param _Url: url resource
        :type Url: str
        :param _InputData: Input parameter
        :type InputData: str
        """
        self._DeviceId = None
        self._Url = None
        self._InputData = None

    @property
    def DeviceId(self):
        r"""Device ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Url(self):
        r"""url resource
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def InputData(self):
        r"""Input parameter
        :rtype: str
        """
        return self._InputData

    @InputData.setter
    def InputData(self, InputData):
        self._InputData = InputData


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Url = params.get("Url")
        self._InputData = params.get("InputData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallISAPIResponse(AbstractModel):
    r"""CallISAPI response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.ISAPIOutputData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.ISAPIOutputData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ISAPIOutputData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CallbackURL(AbstractModel):
    r"""Callback address configuration for screenshots

    """

    def __init__(self):
        r"""
        :param _Url: <p>Image callback URL</p>
        :type Url: str
        :param _Token: <p>Token</p>
        :type Token: str
        :param _Enable: 
        :type Enable: bool
        """
        self._Url = None
        self._Token = None
        self._Enable = None

    @property
    def Url(self):
        r"""<p>Image callback URL</p>
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Token(self):
        r"""<p>Token</p>
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Enable(self):
        r"""
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Token = params.get("Token")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelAttrInfo(AbstractModel):
    r"""Channel property information

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID to which the device channel belongs
        :type DeviceId: str
        :param _DeviceName: Device name of the device channel
        :type DeviceName: str
        :param _ChannelId: Device channel ID
        :type ChannelId: str
        :param _ChannelName: Device channel name
        :type ChannelName: str
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None

    @property
    def DeviceId(self):
        r"""Device ID to which the device channel belongs
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""Device name of the device channel
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        r"""Device channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""Device channel name
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelInfo(AbstractModel):
    r"""Channel and device information of the channel

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID to which the channel belongs
        :type DeviceId: str
        :param _ChannelId: Device channel ID. A device channel can only be added to one cloud connection plan.
        :type ChannelId: str
        """
        self._DeviceId = None
        self._ChannelId = None

    @property
    def DeviceId(self):
        r"""Device ID to which the channel belongs
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        r"""Device channel ID. A device channel can only be added to one cloud connection plan.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDevicePTZRequest(AbstractModel):
    r"""ControlDevicePTZ request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :type ChannelId: str
        :param _Type: Command type (up, down, left, right).
Upper left: leftup, upper right: rightup, lower left: leftdown, lower right: rightdown
Zoom in: zoom in, zoom out: zoom out
Focus far: focusfar, focus near: focusnear
Iris in: enlarge aperture, iris out: shrink aperture)
        :type Type: str
        :param _Speed: Command description (speed range: 1-8)
        :type Speed: int
        """
        self._ChannelId = None
        self._Type = None
        self._Speed = None

    @property
    def ChannelId(self):
        r"""Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Type(self):
        r"""Command type (up, down, left, right).
Upper left: leftup, upper right: rightup, lower left: leftdown, lower right: rightdown
Zoom in: zoom in, zoom out: zoom out
Focus far: focusfar, focus near: focusnear
Iris in: enlarge aperture, iris out: shrink aperture)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Speed(self):
        r"""Command description (speed range: 1-8)
        :rtype: int
        """
        return self._Speed

    @Speed.setter
    def Speed(self, Speed):
        self._Speed = Speed


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Type = params.get("Type")
        self._Speed = params.get("Speed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDevicePTZResponse(AbstractModel):
    r"""ControlDevicePTZ response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ControlDevicePresetRequest(AbstractModel):
    r"""ControlDevicePreset request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :type ChannelId: str
        :param _Cmd: Command (goto: preset position call;
Set: preset position settings
del: Delete preset position)
        :type Cmd: str
        :param _Index: Preset position index (supports only index positions 1-10; an error is reported if exceeded)
        :type Index: int
        """
        self._ChannelId = None
        self._Cmd = None
        self._Index = None

    @property
    def ChannelId(self):
        r"""Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Cmd(self):
        r"""Command (goto: preset position call;
Set: preset position settings
del: Delete preset position)
        :rtype: str
        """
        return self._Cmd

    @Cmd.setter
    def Cmd(self, Cmd):
        self._Cmd = Cmd

    @property
    def Index(self):
        r"""Preset position index (supports only index positions 1-10; an error is reported if exceeded)
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Cmd = params.get("Cmd")
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDevicePresetResponse(AbstractModel):
    r"""ControlDevicePreset response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ControlDeviceSnapshotRequest(AbstractModel):
    r"""ControlDeviceSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _SnapNum: Number of burst shots. Range of optional values: 1–10.
        :type SnapNum: int
        :param _Interval: Snapshot interval. Range of optional values: 1–1800
        :type Interval: int
        :param _Expire: Image storage period. Default value: 7 days. Only supports 7, 15, 30, 60, 90, 180, or 365 days.
        :type Expire: int
        """
        self._ChannelId = None
        self._SnapNum = None
        self._Interval = None
        self._Expire = None

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def SnapNum(self):
        r"""Number of burst shots. Range of optional values: 1–10.
        :rtype: int
        """
        return self._SnapNum

    @SnapNum.setter
    def SnapNum(self, SnapNum):
        self._SnapNum = SnapNum

    @property
    def Interval(self):
        r"""Snapshot interval. Range of optional values: 1–1800
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Expire(self):
        r"""Image storage period. Default value: 7 days. Only supports 7, 15, 30, 60, 90, 180, or 365 days.
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._SnapNum = params.get("SnapNum")
        self._Interval = params.get("Interval")
        self._Expire = params.get("Expire")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceSnapshotResponse(AbstractModel):
    r"""ControlDeviceSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ControlDeviceStreamData(AbstractModel):
    r"""Returned data of the streaming address.

    """

    def __init__(self):
        r"""
        :param _Flv: flv stream address.
        :type Flv: str
        :param _Hls: hls stream address.
        :type Hls: str
        :param _Rtmp: rtmp stream address.
        :type Rtmp: str
        """
        self._Flv = None
        self._Hls = None
        self._Rtmp = None

    @property
    def Flv(self):
        r"""flv stream address.
        :rtype: str
        """
        return self._Flv

    @Flv.setter
    def Flv(self, Flv):
        self._Flv = Flv

    @property
    def Hls(self):
        r"""hls stream address.
        :rtype: str
        """
        return self._Hls

    @Hls.setter
    def Hls(self, Hls):
        self._Hls = Hls

    @property
    def Rtmp(self):
        r"""rtmp stream address.
        :rtype: str
        """
        return self._Rtmp

    @Rtmp.setter
    def Rtmp(self, Rtmp):
        self._Rtmp = Rtmp


    def _deserialize(self, params):
        self._Flv = params.get("Flv")
        self._Hls = params.get("Hls")
        self._Rtmp = params.get("Rtmp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceStreamRequest(AbstractModel):
    r"""ControlDeviceStream request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :type ChannelId: str
        :param _StreamType: Stream type (1: main stream;
2: Substream (not allowed to be delivered at the same time as Resolution)
        :type StreamType: str
        :param _Resolution: Resolution (1: QCIF;
2:CIF;
3:4CIF;
4:D1;
5:720P;
6:1080P/I;
Custom 1920*1080, etc. (device support required) (not allowed to be sent at the same time as StreamType)
        :type Resolution: str
        :param _IsInternal: Whether it is a private network
        :type IsInternal: bool
        """
        self._ChannelId = None
        self._StreamType = None
        self._Resolution = None
        self._IsInternal = None

    @property
    def ChannelId(self):
        r"""Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StreamType(self):
        r"""Stream type (1: main stream;
2: Substream (not allowed to be delivered at the same time as Resolution)
        :rtype: str
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Resolution(self):
        r"""Resolution (1: QCIF;
2:CIF;
3:4CIF;
4:D1;
5:720P;
6:1080P/I;
Custom 1920*1080, etc. (device support required) (not allowed to be sent at the same time as StreamType)
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def IsInternal(self):
        r"""Whether it is a private network
        :rtype: bool
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StreamType = params.get("StreamType")
        self._Resolution = params.get("Resolution")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlDeviceStreamResponse(AbstractModel):
    r"""ControlDeviceStream response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.ControlDeviceStreamData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.ControlDeviceStreamData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ControlDeviceStreamData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ControlRecordTimelineRequest(AbstractModel):
    r"""ControlRecordTimeline request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :type ChannelId: str
        :param _Start: Start time.
        :type Start: int
        :param _End: End time.
        :type End: int
        """
        self._ChannelId = None
        self._Start = None
        self._End = None

    @property
    def ChannelId(self):
        r"""Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Start(self):
        r"""Start time.
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        r"""End time.
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlRecordTimelineResponse(AbstractModel):
    r"""ControlRecordTimeline response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: list of Timeline
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: list of Timeline
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = Timeline()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class CreateVLPlanRequest(AbstractModel):
    r"""CreateVLPlan request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Plan name. Supports Chinese, English, digits, _ and -. Up to 32 characters.</p>
        :type Name: str
        :param _VLTemplateId: <p>ID of the associated visual understanding template</p>
        :type VLTemplateId: str
        :param _Describe: <p>Plan description. Up to 256 characters.</p>
        :type Describe: str
        :param _FileExpires: <p>Number of days to store screenshot files. Value range: [7, 1080]. Required in image mode. Do not pass this parameter in video mode.</p>
        :type FileExpires: int
        :param _Callback: <p>Callback notification configuration</p>
        :type Callback: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        self._Name = None
        self._VLTemplateId = None
        self._Describe = None
        self._FileExpires = None
        self._Callback = None

    @property
    def Name(self):
        r"""<p>Plan name. Supports Chinese, English, digits, _ and -. Up to 32 characters.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VLTemplateId(self):
        r"""<p>ID of the associated visual understanding template</p>
        :rtype: str
        """
        return self._VLTemplateId

    @VLTemplateId.setter
    def VLTemplateId(self, VLTemplateId):
        self._VLTemplateId = VLTemplateId

    @property
    def Describe(self):
        r"""<p>Plan description. Up to 256 characters.</p>
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def FileExpires(self):
        r"""<p>Number of days to store screenshot files. Value range: [7, 1080]. Required in image mode. Do not pass this parameter in video mode.</p>
        :rtype: int
        """
        return self._FileExpires

    @FileExpires.setter
    def FileExpires(self, FileExpires):
        self._FileExpires = FileExpires

    @property
    def Callback(self):
        r"""<p>Callback notification configuration</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._VLTemplateId = params.get("VLTemplateId")
        self._Describe = params.get("Describe")
        self._FileExpires = params.get("FileExpires")
        if params.get("Callback") is not None:
            self._Callback = CallbackURL()
            self._Callback._deserialize(params.get("Callback"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVLPlanResponse(AbstractModel):
    r"""CreateVLPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Visual understanding plan information</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VLPlanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Visual understanding plan information</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VLPlanInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VLPlanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateVLTemplateRequest(AbstractModel):
    r"""CreateVLTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _AIModel: <p>AI model</p><p>Enumeration values:</p><ul><li>ivc-vl-1.0: View large model</li></ul>
        :type AIModel: str
        :param _Name: <p>Template name. Supports only Chinese, English, digits, _, and -, with a maximum length of 32 characters.</p>
        :type Name: str
        :param _Prompt: <p>Prompt content, maximum 2MB</p>
        :type Prompt: str
        :param _AnalysisMode: <p>Analysis mode</p><p>Enumeration values:</p><ul><li>image: image mode</li><li>video: video mode</li></ul>
        :type AnalysisMode: str
        :param _Times: <p>List of effective periods, up to 100 entries</p>
        :type Times: list of EffectiveTime
        :param _Describe: <p>Template description. Maximum length: 256 characters.</p>
        :type Describe: str
        :param _ImageConfig: <p>Image scenario configuration (required when AnalysisMode=image)</p>
        :type ImageConfig: :class:`tencentcloud.iss.v20230517.models.ImageSceneInfo`
        """
        self._AIModel = None
        self._Name = None
        self._Prompt = None
        self._AnalysisMode = None
        self._Times = None
        self._Describe = None
        self._ImageConfig = None

    @property
    def AIModel(self):
        r"""<p>AI model</p><p>Enumeration values:</p><ul><li>ivc-vl-1.0: View large model</li></ul>
        :rtype: str
        """
        return self._AIModel

    @AIModel.setter
    def AIModel(self, AIModel):
        self._AIModel = AIModel

    @property
    def Name(self):
        r"""<p>Template name. Supports only Chinese, English, digits, _, and -, with a maximum length of 32 characters.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Prompt(self):
        r"""<p>Prompt content, maximum 2MB</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def AnalysisMode(self):
        r"""<p>Analysis mode</p><p>Enumeration values:</p><ul><li>image: image mode</li><li>video: video mode</li></ul>
        :rtype: str
        """
        return self._AnalysisMode

    @AnalysisMode.setter
    def AnalysisMode(self, AnalysisMode):
        self._AnalysisMode = AnalysisMode

    @property
    def Times(self):
        r"""<p>List of effective periods, up to 100 entries</p>
        :rtype: list of EffectiveTime
        """
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times

    @property
    def Describe(self):
        r"""<p>Template description. Maximum length: 256 characters.</p>
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ImageConfig(self):
        r"""<p>Image scenario configuration (required when AnalysisMode=image)</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.ImageSceneInfo`
        """
        return self._ImageConfig

    @ImageConfig.setter
    def ImageConfig(self, ImageConfig):
        self._ImageConfig = ImageConfig


    def _deserialize(self, params):
        self._AIModel = params.get("AIModel")
        self._Name = params.get("Name")
        self._Prompt = params.get("Prompt")
        self._AnalysisMode = params.get("AnalysisMode")
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = EffectiveTime()
                obj._deserialize(item)
                self._Times.append(obj)
        self._Describe = params.get("Describe")
        if params.get("ImageConfig") is not None:
            self._ImageConfig = ImageSceneInfo()
            self._ImageConfig._deserialize(params.get("ImageConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVLTemplateResponse(AbstractModel):
    r"""CreateVLTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Visual understanding template information</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VLTemplateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Visual understanding template information</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VLTemplateInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VLTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateVideoDownloadTaskRequest(AbstractModel):
    r"""CreateVideoDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _BeginTime: Start time.
        :type BeginTime: int
        :param _EndTime: End time.
        :type EndTime: int
        :param _Scale: Default: 1x. Supports 1x, 2x, 4x, and 8x playback speeds.
        :type Scale: int
        :param _Expire: Expiration time of the transcoded mp4 file (7, 15, 30, 60, 90, 180, and 365 are supported)
        :type Expire: int
        :param _FileType: Download file format. Currently only supports (1: mp4)
        :type FileType: int
        :param _CompletionPolicy: Completion policy (0: The task fails and no MP4 is generated if the stream pull fails but the video recording is incomplete. 1: The task succeeds and an MP4 is generated if the stream pull fails but the video recording is incomplete.)
        :type CompletionPolicy: int
        """
        self._ChannelId = None
        self._BeginTime = None
        self._EndTime = None
        self._Scale = None
        self._Expire = None
        self._FileType = None
        self._CompletionPolicy = None

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def BeginTime(self):
        r"""Start time.
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Scale(self):
        r"""Default: 1x. Supports 1x, 2x, 4x, and 8x playback speeds.
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def Expire(self):
        r"""Expiration time of the transcoded mp4 file (7, 15, 30, 60, 90, 180, and 365 are supported)
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def FileType(self):
        r"""Download file format. Currently only supports (1: mp4)
        :rtype: int
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def CompletionPolicy(self):
        r"""Completion policy (0: The task fails and no MP4 is generated if the stream pull fails but the video recording is incomplete. 1: The task succeeds and an MP4 is generated if the stream pull fails but the video recording is incomplete.)
        :rtype: int
        """
        return self._CompletionPolicy

    @CompletionPolicy.setter
    def CompletionPolicy(self, CompletionPolicy):
        self._CompletionPolicy = CompletionPolicy


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._Scale = params.get("Scale")
        self._Expire = params.get("Expire")
        self._FileType = params.get("FileType")
        self._CompletionPolicy = params.get("CompletionPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoDownloadTaskResponse(AbstractModel):
    r"""CreateVideoDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned results of the download task
        :type Data: :class:`tencentcloud.iss.v20230517.models.VideoDownloadTaskData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned results of the download task
        :rtype: :class:`tencentcloud.iss.v20230517.models.VideoDownloadTaskData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VideoDownloadTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateVideoSnapshotConfigRequest(AbstractModel):
    r"""CreateVideoSnapshotConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Screenshot configuration name</p><p>Input parameter limits: Chinese, English, digits, "-", "_", length not exceeding 128 characters</p>
        :type Name: str
        :param _TemplateId: <p>Screenshot template Id</p>
        :type TemplateId: str
        :param _FileExpires: <p>Hot storage days for image files</p><p>Enumeration values:</p><ul><li>7: 7 days</li><li>15: 15 days</li><li>30: 30 days</li><li>60: 60 days</li><li>90: 90 days</li><li>180: 180 days</li><li>270: 270 days</li><li>360: 360 days</li><li>540: 540 days</li><li>720: 720 days</li><li>900: 900 days</li><li>1080: 1080 days</li></ul>
        :type FileExpires: int
        :param _Callback: <p>Screenshot result callback URL</p>
        :type Callback: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        self._Name = None
        self._TemplateId = None
        self._FileExpires = None
        self._Callback = None

    @property
    def Name(self):
        r"""<p>Screenshot configuration name</p><p>Input parameter limits: Chinese, English, digits, "-", "_", length not exceeding 128 characters</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TemplateId(self):
        r"""<p>Screenshot template Id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def FileExpires(self):
        r"""<p>Hot storage days for image files</p><p>Enumeration values:</p><ul><li>7: 7 days</li><li>15: 15 days</li><li>30: 30 days</li><li>60: 60 days</li><li>90: 90 days</li><li>180: 180 days</li><li>270: 270 days</li><li>360: 360 days</li><li>540: 540 days</li><li>720: 720 days</li><li>900: 900 days</li><li>1080: 1080 days</li></ul>
        :rtype: int
        """
        return self._FileExpires

    @FileExpires.setter
    def FileExpires(self, FileExpires):
        self._FileExpires = FileExpires

    @property
    def Callback(self):
        r"""<p>Screenshot result callback URL</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._TemplateId = params.get("TemplateId")
        self._FileExpires = params.get("FileExpires")
        if params.get("Callback") is not None:
            self._Callback = CallbackURL()
            self._Callback._deserialize(params.get("Callback"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoSnapshotConfigResponse(AbstractModel):
    r"""CreateVideoSnapshotConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Screenshot configuration message</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotConfigInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Screenshot configuration message</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotConfigInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VideoSnapshotConfigInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateVideoSnapshotTemplateRequest(AbstractModel):
    r"""CreateVideoSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Template name: Chinese, English, digits, "-", "_", with a length not exceeding 128 characters</p>
        :type Name: str
        :param _Type: <p>Screenshot type: 1-Real-time frame capture 2-Low frequency frame capture<br>Note: Real-time frame capture pulls the real-time stream throughout the effective period. Low frequency frame capture pulls the real-time stream as needed during the effective period, with a minimum duration of not less than 1 minute each time.</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :type Type: int
        :param _Interval: <p>Frame capturing frequency: When Type = 1, the value range is [5, 180] seconds; when Type = 2, the value range is [30, 36000] seconds</p>
        :type Interval: int
        :param _Times: <p>Effective period. Note: The array size is no more than 100, and each time period is not less than 1 minute.</p>
        :type Times: list of EffectiveTime
        :param _MultiMode: <p>Multiple mode</p>
        :type MultiMode: :class:`tencentcloud.iss.v20230517.models.MultiVideoSnapshotMode`
        """
        self._Name = None
        self._Type = None
        self._Interval = None
        self._Times = None
        self._MultiMode = None

    @property
    def Name(self):
        r"""<p>Template name: Chinese, English, digits, "-", "_", with a length not exceeding 128 characters</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>Screenshot type: 1-Real-time frame capture 2-Low frequency frame capture<br>Note: Real-time frame capture pulls the real-time stream throughout the effective period. Low frequency frame capture pulls the real-time stream as needed during the effective period, with a minimum duration of not less than 1 minute each time.</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        r"""<p>Frame capturing frequency: When Type = 1, the value range is [5, 180] seconds; when Type = 2, the value range is [30, 36000] seconds</p>
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Times(self):
        r"""<p>Effective period. Note: The array size is no more than 100, and each time period is not less than 1 minute.</p>
        :rtype: list of EffectiveTime
        """
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times

    @property
    def MultiMode(self):
        r"""<p>Multiple mode</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.MultiVideoSnapshotMode`
        """
        return self._MultiMode

    @MultiMode.setter
    def MultiMode(self, MultiMode):
        self._MultiMode = MultiMode


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = EffectiveTime()
                obj._deserialize(item)
                self._Times.append(obj)
        if params.get("MultiMode") is not None:
            self._MultiMode = MultiVideoSnapshotMode()
            self._MultiMode._deserialize(params.get("MultiMode"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoSnapshotTemplateResponse(AbstractModel):
    r"""CreateVideoSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Screenshot template information</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotTemplateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Screenshot template information</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotTemplateInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VideoSnapshotTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    r"""DeleteDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Domain name ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        r"""Domain name ID
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
        


class DeleteDomainResponse(AbstractModel):
    r"""DeleteDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrganizationRequest(AbstractModel):
    r"""DeleteOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _OrganizationId: Organization ID (obtain from the DescribeOrganization API for querying organizations)
        :type OrganizationId: str
        """
        self._OrganizationId = None

    @property
    def OrganizationId(self):
        r"""Organization ID (obtain from the DescribeOrganization API for querying organizations)
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationResponse(AbstractModel):
    r"""DeleteOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRecordBackupPlanRequest(AbstractModel):
    r"""DeleteRecordBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Recording cloud migration plan ID (obtain from the ListRecordBackupPlans API for querying the recording cloud migration plan list)
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        r"""Recording cloud migration plan ID (obtain from the ListRecordBackupPlans API for querying the recording cloud migration plan list)
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordBackupPlanResponse(AbstractModel):
    r"""DeleteRecordBackupPlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRecordBackupTemplateRequest(AbstractModel):
    r"""DeleteRecordBackupTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID (obtain from the ListRecordBackupTemplates API for querying the video recording cloud template list)
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""Template ID (obtain from the ListRecordBackupTemplates API for querying the video recording cloud template list)
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordBackupTemplateResponse(AbstractModel):
    r"""DeleteRecordBackupTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRecordPlanRequest(AbstractModel):
    r"""DeleteRecordPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Cloud migration plan ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        r"""Cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordPlanResponse(AbstractModel):
    r"""DeleteRecordPlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRecordRetrieveTaskRequest(AbstractModel):
    r"""DeleteRecordRetrieveTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Retrieval task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Retrieval task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordRetrieveTaskResponse(AbstractModel):
    r"""DeleteRecordRetrieveTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRecordTemplateRequest(AbstractModel):
    r"""DeleteRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID.
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""Template ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordTemplateResponse(AbstractModel):
    r"""DeleteRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteTaskRequest(AbstractModel):
    r"""DeleteTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTaskResponse(AbstractModel):
    r"""DeleteTask response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteUserDeviceRequest(AbstractModel):
    r"""DeleteUserDevice request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID (obtain from the ListDevices API for getting the device list)
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        r"""Device ID (obtain from the ListDevices API for getting the device list)
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserDeviceResponse(AbstractModel):
    r"""DeleteUserDevice response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteVLPlanRequest(AbstractModel):
    r"""DeleteVLPlan request structure.

    """

    def __init__(self):
        r"""
        :param _VLPlanId: <p>Plan ID</p>
        :type VLPlanId: str
        """
        self._VLPlanId = None

    @property
    def VLPlanId(self):
        r"""<p>Plan ID</p>
        :rtype: str
        """
        return self._VLPlanId

    @VLPlanId.setter
    def VLPlanId(self, VLPlanId):
        self._VLPlanId = VLPlanId


    def _deserialize(self, params):
        self._VLPlanId = params.get("VLPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVLPlanResponse(AbstractModel):
    r"""DeleteVLPlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteVLTemplateRequest(AbstractModel):
    r"""DeleteVLTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _VLTemplateId: <p>Template ID</p>
        :type VLTemplateId: str
        """
        self._VLTemplateId = None

    @property
    def VLTemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._VLTemplateId

    @VLTemplateId.setter
    def VLTemplateId(self, VLTemplateId):
        self._VLTemplateId = VLTemplateId


    def _deserialize(self, params):
        self._VLTemplateId = params.get("VLTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVLTemplateResponse(AbstractModel):
    r"""DeleteVLTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteVideoSnapshotConfigRequest(AbstractModel):
    r"""DeleteVideoSnapshotConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: <p>Screenshot configuration Id</p>
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        r"""<p>Screenshot configuration Id</p>
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVideoSnapshotConfigResponse(AbstractModel):
    r"""DeleteVideoSnapshotConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteVideoSnapshotTemplateRequest(AbstractModel):
    r"""DeleteVideoSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>Screenshot template Id</p>
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""<p>Screenshot template Id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVideoSnapshotTemplateResponse(AbstractModel):
    r"""DeleteVideoSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeCNAMERequest(AbstractModel):
    r"""DescribeCNAME request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Service node ID (obtain from the DescribeDomainRegion API for querying domain name bindable service nodes)
        :type ClusterId: str
        :param _DomainType: Domain type. 0: pull streaming domain name. 1: streaming domain.
        :type DomainType: int
        """
        self._ClusterId = None
        self._DomainType = None

    @property
    def ClusterId(self):
        r"""Service node ID (obtain from the DescribeDomainRegion API for querying domain name bindable service nodes)
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def DomainType(self):
        r"""Domain type. 0: pull streaming domain name. 1: streaming domain.
        :rtype: int
        """
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._DomainType = params.get("DomainType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCNAMEResponse(AbstractModel):
    r"""DescribeCNAME response structure.

    """

    def __init__(self):
        r"""
        :param _Data: CNAME record value
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""CNAME record value
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeDeviceAddrList(AbstractModel):
    r"""Query the list of national standard device addresses

    """

    def __init__(self):
        r"""
        :param _RemoteAddrs: List of device addresses
        :type RemoteAddrs: list of RemoteAddrInfo
        """
        self._RemoteAddrs = None

    @property
    def RemoteAddrs(self):
        r"""List of device addresses
        :rtype: list of RemoteAddrInfo
        """
        return self._RemoteAddrs

    @RemoteAddrs.setter
    def RemoteAddrs(self, RemoteAddrs):
        self._RemoteAddrs = RemoteAddrs


    def _deserialize(self, params):
        if params.get("RemoteAddrs") is not None:
            self._RemoteAddrs = []
            for item in params.get("RemoteAddrs"):
                obj = RemoteAddrInfo()
                obj._deserialize(item)
                self._RemoteAddrs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceChannelData(AbstractModel):
    r"""Returned results of querying device channel information

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID
        :type DeviceId: str
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _ChannelCode: Channel encoding
        :type ChannelCode: str
        :param _Name: Channel name
        :type Name: str
        :param _Status: Stream status (0: not transmitted, 1: in transit)
        :type Status: int
        :param _PTZType: Whether Ptz is controllable (0: no, 1: yes)
        :type PTZType: int
        :param _Manufacturer: Channel manufacturer
        :type Manufacturer: str
        :param _Resolution: Channel supports resolution (resolution list separated by '/', National Standard Protocol example (6/3), custom example (12800960/640480))
        :type Resolution: str
        :param _State: Channel offline status (0: offline, 1: online)
        :type State: int
        :param _Region: Region
        :type Region: str
        """
        self._DeviceId = None
        self._ChannelId = None
        self._ChannelCode = None
        self._Name = None
        self._Status = None
        self._PTZType = None
        self._Manufacturer = None
        self._Resolution = None
        self._State = None
        self._Region = None

    @property
    def DeviceId(self):
        r"""Device ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelCode(self):
        r"""Channel encoding
        :rtype: str
        """
        return self._ChannelCode

    @ChannelCode.setter
    def ChannelCode(self, ChannelCode):
        self._ChannelCode = ChannelCode

    @property
    def Name(self):
        r"""Channel name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""Stream status (0: not transmitted, 1: in transit)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PTZType(self):
        r"""Whether Ptz is controllable (0: no, 1: yes)
        :rtype: int
        """
        return self._PTZType

    @PTZType.setter
    def PTZType(self, PTZType):
        self._PTZType = PTZType

    @property
    def Manufacturer(self):
        r"""Channel manufacturer
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def Resolution(self):
        r"""Channel supports resolution (resolution list separated by '/', National Standard Protocol example (6/3), custom example (12800960/640480))
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def State(self):
        r"""Channel offline status (0: offline, 1: online)
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Region(self):
        r"""Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._ChannelCode = params.get("ChannelCode")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._PTZType = params.get("PTZType")
        self._Manufacturer = params.get("Manufacturer")
        self._Resolution = params.get("Resolution")
        self._State = params.get("State")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceChannelRequest(AbstractModel):
    r"""DescribeDeviceChannel request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID (obtain from the ListDevices API for getting the device list)
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        r"""Device ID (obtain from the ListDevices API for getting the device list)
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceChannelResponse(AbstractModel):
    r"""DescribeDeviceChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: list of DescribeDeviceChannelData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: list of DescribeDeviceChannelData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDeviceChannelData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceData(AbstractModel):
    r"""Data returned by the device query API

    """

    def __init__(self):
        r"""
        :param _DeviceId: <p>Device ID</p>
        :type DeviceId: str
        :param _Code: <p>Device code (for national standard devices, it is the 20-digit National Standard Encoding we generated for the device; for rtmp devices, it is the 10-digit device code)</p>
        :type Code: str
        :param _Name: <p>Device name</p>
        :type Name: str
        :param _AccessProtocol: <p>Device access protocol. 1: RTMP, 2: GB, 3: GW</p>
        :type AccessProtocol: int
        :param _Type: <p>Device type. 1: IPC. 2: NVR.</p>
        :type Type: int
        :param _ClusterId: <p>Device access service node id</p>
        :type ClusterId: str
        :param _ClusterName: <p>Device access service node name</p>
        :type ClusterName: str
        :param _TransportProtocol: <p>Device streaming protocol. 1: UDP; 2: TCP</p>
        :type TransportProtocol: int
        :param _Password: <p>Device password</p>
        :type Password: str
        :param _Description: <p>Device description</p>
        :type Description: str
        :param _SipId: <p>sip service ID</p>
        :type SipId: str
        :param _SipDomain: <p>sip Service Domain</p>
        :type SipDomain: str
        :param _SipIp: <p>sip service IP address</p>
        :type SipIp: str
        :param _SipPort: <p>sip server port</p>
        :type SipPort: int
        :param _PushStreamUrl: <p>Rtmp device streaming address (valid only for Rtmp devices)</p>
        :type PushStreamUrl: str
        :param _Status: <p>Device status. 0: unregistered, 1: online, 2: offline, 3: disabled</p>
        :type Status: int
        :param _OrganizationId: <p>Organization ID of the device</p>
        :type OrganizationId: str
        :param _GatewayId: <p>Device gateway ID, obtained from the query gateway list API (required for gateway access only)</p>
        :type GatewayId: str
        :param _GatewayName: <p>Gateway name of the device ownership</p>
        :type GatewayName: str
        :param _ProtocolTypeName: <p>Device gateway protocol name</p>
        :type ProtocolTypeName: str
        :param _ProtocolType: <p>Gateway access protocol type. 1. Hikvision SDK, 2. Dahua SDK, 3. Uniview SDK, 4. Onvif (required for gateway access only)</p>
        :type ProtocolType: int
        :param _Ip: <p>Device connectivity IP</p>
        :type Ip: str
        :param _Port: <p>Device Port</p>
        :type Port: int
        :param _Username: <p>Device username</p>
        :type Username: str
        :param _Region: <p>Device region</p>
        :type Region: str
        :param _Manufacturer: <p>Device vendor</p>
        :type Manufacturer: str
        :param _AudioSwitch: <p>Audio on/off (0: off; 1: on). Audio is dropped when turned off.</p>
        :type AudioSwitch: int
        :param _SubscribeSwitch: <p>Subscription switch (0: off; 1: on), enabled by default. When enabled, it subscribes to device channel adjustments. Valid only for national standard NVR devices</p>
        :type SubscribeSwitch: int
        :param _AppName: <p>Custom appName for RTMP publishing address</p>
        :type AppName: str
        :param _StreamName: <p>Custom streamName for RTMP publishing address</p>
        :type StreamName: str
        :param _SilentFrameSwitch: <p>Whether to enable silent frames (0: disabled; 1: enabled)</p>
        :type SilentFrameSwitch: int
        :param _PushStreamSecureUrl: <p>Rtmp device secure authentication streaming address (valid only for Rtmp devices)</p>
        :type PushStreamSecureUrl: str
        """
        self._DeviceId = None
        self._Code = None
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._ClusterId = None
        self._ClusterName = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._SipId = None
        self._SipDomain = None
        self._SipIp = None
        self._SipPort = None
        self._PushStreamUrl = None
        self._Status = None
        self._OrganizationId = None
        self._GatewayId = None
        self._GatewayName = None
        self._ProtocolTypeName = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._Region = None
        self._Manufacturer = None
        self._AudioSwitch = None
        self._SubscribeSwitch = None
        self._AppName = None
        self._StreamName = None
        self._SilentFrameSwitch = None
        self._PushStreamSecureUrl = None

    @property
    def DeviceId(self):
        r"""<p>Device ID</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        r"""<p>Device code (for national standard devices, it is the 20-digit National Standard Encoding we generated for the device; for rtmp devices, it is the 10-digit device code)</p>
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        r"""<p>Device name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        r"""<p>Device access protocol. 1: RTMP, 2: GB, 3: GW</p>
        :rtype: int
        """
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        r"""<p>Device type. 1: IPC. 2: NVR.</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClusterId(self):
        r"""<p>Device access service node id</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""<p>Device access service node name</p>
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TransportProtocol(self):
        r"""<p>Device streaming protocol. 1: UDP; 2: TCP</p>
        :rtype: int
        """
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        r"""<p>Device password</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""<p>Device description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SipId(self):
        r"""<p>sip service ID</p>
        :rtype: str
        """
        return self._SipId

    @SipId.setter
    def SipId(self, SipId):
        self._SipId = SipId

    @property
    def SipDomain(self):
        r"""<p>sip Service Domain</p>
        :rtype: str
        """
        return self._SipDomain

    @SipDomain.setter
    def SipDomain(self, SipDomain):
        self._SipDomain = SipDomain

    @property
    def SipIp(self):
        r"""<p>sip service IP address</p>
        :rtype: str
        """
        return self._SipIp

    @SipIp.setter
    def SipIp(self, SipIp):
        self._SipIp = SipIp

    @property
    def SipPort(self):
        r"""<p>sip server port</p>
        :rtype: int
        """
        return self._SipPort

    @SipPort.setter
    def SipPort(self, SipPort):
        self._SipPort = SipPort

    @property
    def PushStreamUrl(self):
        r"""<p>Rtmp device streaming address (valid only for Rtmp devices)</p>
        :rtype: str
        """
        return self._PushStreamUrl

    @PushStreamUrl.setter
    def PushStreamUrl(self, PushStreamUrl):
        self._PushStreamUrl = PushStreamUrl

    @property
    def Status(self):
        r"""<p>Device status. 0: unregistered, 1: online, 2: offline, 3: disabled</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrganizationId(self):
        r"""<p>Organization ID of the device</p>
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def GatewayId(self):
        r"""<p>Device gateway ID, obtained from the query gateway list API (required for gateway access only)</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayName(self):
        r"""<p>Gateway name of the device ownership</p>
        :rtype: str
        """
        return self._GatewayName

    @GatewayName.setter
    def GatewayName(self, GatewayName):
        self._GatewayName = GatewayName

    @property
    def ProtocolTypeName(self):
        r"""<p>Device gateway protocol name</p>
        :rtype: str
        """
        return self._ProtocolTypeName

    @ProtocolTypeName.setter
    def ProtocolTypeName(self, ProtocolTypeName):
        self._ProtocolTypeName = ProtocolTypeName

    @property
    def ProtocolType(self):
        r"""<p>Gateway access protocol type. 1. Hikvision SDK, 2. Dahua SDK, 3. Uniview SDK, 4. Onvif (required for gateway access only)</p>
        :rtype: int
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        r"""<p>Device connectivity IP</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""<p>Device Port</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        r"""<p>Device username</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Region(self):
        r"""<p>Device region</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Manufacturer(self):
        r"""<p>Device vendor</p>
        :rtype: str
        """
        return self._Manufacturer

    @Manufacturer.setter
    def Manufacturer(self, Manufacturer):
        self._Manufacturer = Manufacturer

    @property
    def AudioSwitch(self):
        r"""<p>Audio on/off (0: off; 1: on). Audio is dropped when turned off.</p>
        :rtype: int
        """
        return self._AudioSwitch

    @AudioSwitch.setter
    def AudioSwitch(self, AudioSwitch):
        self._AudioSwitch = AudioSwitch

    @property
    def SubscribeSwitch(self):
        r"""<p>Subscription switch (0: off; 1: on), enabled by default. When enabled, it subscribes to device channel adjustments. Valid only for national standard NVR devices</p>
        :rtype: int
        """
        return self._SubscribeSwitch

    @SubscribeSwitch.setter
    def SubscribeSwitch(self, SubscribeSwitch):
        self._SubscribeSwitch = SubscribeSwitch

    @property
    def AppName(self):
        r"""<p>Custom appName for RTMP publishing address</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        r"""<p>Custom streamName for RTMP publishing address</p>
        :rtype: str
        """
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def SilentFrameSwitch(self):
        r"""<p>Whether to enable silent frames (0: disabled; 1: enabled)</p>
        :rtype: int
        """
        return self._SilentFrameSwitch

    @SilentFrameSwitch.setter
    def SilentFrameSwitch(self, SilentFrameSwitch):
        self._SilentFrameSwitch = SilentFrameSwitch

    @property
    def PushStreamSecureUrl(self):
        r"""<p>Rtmp device secure authentication streaming address (valid only for Rtmp devices)</p>
        :rtype: str
        """
        return self._PushStreamSecureUrl

    @PushStreamSecureUrl.setter
    def PushStreamSecureUrl(self, PushStreamSecureUrl):
        self._PushStreamSecureUrl = PushStreamSecureUrl


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._SipId = params.get("SipId")
        self._SipDomain = params.get("SipDomain")
        self._SipIp = params.get("SipIp")
        self._SipPort = params.get("SipPort")
        self._PushStreamUrl = params.get("PushStreamUrl")
        self._Status = params.get("Status")
        self._OrganizationId = params.get("OrganizationId")
        self._GatewayId = params.get("GatewayId")
        self._GatewayName = params.get("GatewayName")
        self._ProtocolTypeName = params.get("ProtocolTypeName")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._Region = params.get("Region")
        self._Manufacturer = params.get("Manufacturer")
        self._AudioSwitch = params.get("AudioSwitch")
        self._SubscribeSwitch = params.get("SubscribeSwitch")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._SilentFrameSwitch = params.get("SilentFrameSwitch")
        self._PushStreamSecureUrl = params.get("PushStreamSecureUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceListData(AbstractModel):
    r"""Data returned by the batch query device API

    """

    def __init__(self):
        r"""
        :param _List: Device detail list
        :type List: list of DescribeDeviceData
        """
        self._List = None

    @property
    def List(self):
        r"""Device detail list
        :rtype: list of DescribeDeviceData
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DescribeDeviceData()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePresetData(AbstractModel):
    r"""data for querying device preset positions

    """

    def __init__(self):
        r"""
        :param _Index: Preset position index. Supports only indexes 1-10.
        :type Index: int
        :param _Name: Preset position name
        :type Name: str
        """
        self._Index = None
        self._Name = None

    @property
    def Index(self):
        r"""Preset position index. Supports only indexes 1-10.
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Name(self):
        r"""Preset position name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePresetRequest(AbstractModel):
    r"""DescribeDevicePreset request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :type ChannelId: str
        """
        self._ChannelId = None

    @property
    def ChannelId(self):
        r"""Channel ID (obtain from the channel query API DescribeDeviceChannel)
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicePresetResponse(AbstractModel):
    r"""DescribeDevicePreset response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: list of DescribeDevicePresetData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: list of DescribeDevicePresetData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDevicePresetData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainData(AbstractModel):
    r"""Query domain detail data

    """

    def __init__(self):
        r"""
        :param _Id: Domain ID
        :type Id: str
        :param _PlayDomain: Playback domain
        :type PlayDomain: str
        :param _InternalDomain: CNAME record value
        :type InternalDomain: str
        :param _HaveCert: Whether to upload a certificate (0: No, 1: Yes)
        :type HaveCert: int
        :param _ClusterId: Service node ID
        :type ClusterId: str
        :param _ClusterName: Service node name
        :type ClusterName: str
        :param _AppId: User ID.
        :type AppId: int
        :param _CertId: Certificate ID
        :type CertId: str
        :param _DomainType: Domain type. 0: Pull streaming domain name; 1: Streaming domain
        :type DomainType: int
        """
        self._Id = None
        self._PlayDomain = None
        self._InternalDomain = None
        self._HaveCert = None
        self._ClusterId = None
        self._ClusterName = None
        self._AppId = None
        self._CertId = None
        self._DomainType = None

    @property
    def Id(self):
        r"""Domain ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PlayDomain(self):
        r"""Playback domain
        :rtype: str
        """
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def InternalDomain(self):
        r"""CNAME record value
        :rtype: str
        """
        return self._InternalDomain

    @InternalDomain.setter
    def InternalDomain(self, InternalDomain):
        self._InternalDomain = InternalDomain

    @property
    def HaveCert(self):
        r"""Whether to upload a certificate (0: No, 1: Yes)
        :rtype: int
        """
        return self._HaveCert

    @HaveCert.setter
    def HaveCert(self, HaveCert):
        self._HaveCert = HaveCert

    @property
    def ClusterId(self):
        r"""Service node ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""Service node name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AppId(self):
        r"""User ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CertId(self):
        r"""Certificate ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DomainType(self):
        r"""Domain type. 0: Pull streaming domain name; 1: Streaming domain
        :rtype: int
        """
        return self._DomainType

    @DomainType.setter
    def DomainType(self, DomainType):
        self._DomainType = DomainType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PlayDomain = params.get("PlayDomain")
        self._InternalDomain = params.get("InternalDomain")
        self._HaveCert = params.get("HaveCert")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._AppId = params.get("AppId")
        self._CertId = params.get("CertId")
        self._DomainType = params.get("DomainType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainRegionData(AbstractModel):
    r"""Query domain name data that can be bound to clusters

    """

    def __init__(self):
        r"""
        :param _Label: Service node description
        :type Label: str
        :param _Value: Service node ID (the ClusterId required in other APIs)
        :type Value: str
        :param _Region: Region information
        :type Region: str
        """
        self._Label = None
        self._Value = None
        self._Region = None

    @property
    def Label(self):
        r"""Service node description
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Value(self):
        r"""Service node ID (the ClusterId required in other APIs)
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Region(self):
        r"""Region information
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Value = params.get("Value")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainRegionRequest(AbstractModel):
    r"""DescribeDomainRegion request structure.

    """


class DescribeDomainRegionResponse(AbstractModel):
    r"""DescribeDomainRegion response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: list of DescribeDomainRegionData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: list of DescribeDomainRegionData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDomainRegionData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainRequest(AbstractModel):
    r"""DescribeDomain request structure.

    """


class DescribeDomainResponse(AbstractModel):
    r"""DescribeDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: list of DescribeDomainData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: list of DescribeDomainData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeDomainData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGBDeviceAddrRequest(AbstractModel):
    r"""DescribeGBDeviceAddr request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceIds: Device ID list
        :type DeviceIds: list of str
        """
        self._DeviceIds = None

    @property
    def DeviceIds(self):
        r"""Device ID list
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGBDeviceAddrResponse(AbstractModel):
    r"""DescribeGBDeviceAddr response structure.

    """

    def __init__(self):
        r"""
        :param _Data: None.
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceAddrList`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""None.
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceAddrList`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeDeviceAddrList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeOrganizationData(AbstractModel):
    r"""Query the returned result of organizational data

    """

    def __init__(self):
        r"""
        :param _OrganizationId: Organization ID
        :type OrganizationId: str
        :param _Name: Organization name
        :type Name: str
        :param _ParentId: Parent node ID of the organizational unit
        :type ParentId: str
        :param _Level: Organizational hierarchy
        :type Level: int
        :param _AppId: User ID
        :type AppId: int
        :param _ParentIds: Organizational structure
        :type ParentIds: str
        :param _Total: Total number of devices
        :type Total: int
        :param _Online: Number of devices online
        :type Online: int
        """
        self._OrganizationId = None
        self._Name = None
        self._ParentId = None
        self._Level = None
        self._AppId = None
        self._ParentIds = None
        self._Total = None
        self._Online = None

    @property
    def OrganizationId(self):
        r"""Organization ID
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        r"""Organization name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        r"""Parent node ID of the organizational unit
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Level(self):
        r"""Organizational hierarchy
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def AppId(self):
        r"""User ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ParentIds(self):
        r"""Organizational structure
        :rtype: str
        """
        return self._ParentIds

    @ParentIds.setter
    def ParentIds(self, ParentIds):
        self._ParentIds = ParentIds

    @property
    def Total(self):
        r"""Total number of devices
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Online(self):
        r"""Number of devices online
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._Level = params.get("Level")
        self._AppId = params.get("AppId")
        self._ParentIds = params.get("ParentIds")
        self._Total = params.get("Total")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationRequest(AbstractModel):
    r"""DescribeOrganization request structure.

    """


class DescribeOrganizationResponse(AbstractModel):
    r"""DescribeOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: list of DescribeOrganizationData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: list of DescribeOrganizationData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DescribeOrganizationData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordBackupPlanData(AbstractModel):
    r"""data for querying the recording cloud migration plan

    """

    def __init__(self):
        r"""
        :param _PlanId: Recording cloud migration plan ID
        :type PlanId: str
        :param _PlanName: Recording cloud migration plan name
        :type PlanName: str
        :param _TemplateId: Video cloud template ID
        :type TemplateId: str
        :param _Describe: Description of the recording cloud migration plan
        :type Describe: str
        :param _LifeCycle: Cloud file lifecycle
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: Recording cloud migration plan status. 1: In normal use. 0: Deleting, cannot be used.
        :type Status: int
        :param _ChannelCount: Number of channels
        :type ChannelCount: int
        :param _CreateAt: Creation time.
        :type CreateAt: str
        :param _UpdateAt: Modification time.
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        r"""Recording cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""Recording cloud migration plan name
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Video cloud template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Description of the recording cloud migration plan
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        r"""Cloud file lifecycle
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        r"""Recording cloud migration plan status. 1: In normal use. 0: Deleting, cannot be used.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        r"""Number of channels
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""Modification time.
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordBackupPlanRequest(AbstractModel):
    r"""DescribeRecordBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Recording cloud migration plan ID (obtain from the ListRecordBackupPlans API for querying the recording cloud migration plan list)
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        r"""Recording cloud migration plan ID (obtain from the ListRecordBackupPlans API for querying the recording cloud migration plan list)
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordBackupPlanResponse(AbstractModel):
    r"""DescribeRecordBackupPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupPlanData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupPlanData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeRecordBackupPlanData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordBackupTemplateData(AbstractModel):
    r"""data for querying video recording cloud templates

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>Template ID</p>
        :type TemplateId: str
        :param _TemplateName: <p>Template name</p>
        :type TemplateName: str
        :param _TimeSections: <p>Cloud Upload Time Period (settings can be done by week, support setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: <p>Recording time period (settings can be done by week. You can set multiple time periods each day, each not less than 10 minutes)</p>
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: <p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :type Scale: int
        :param _CreateAt: <p>Creation time.</p>
        :type CreateAt: str
        :param _UpdateAt: <p>Update time.</p>
        :type UpdateAt: str
        :param _DayOffset: <p>Cycle offset. Default value: 1. It means to pull yesterday's video recording from the device. 0 means to pull today's video recording from the device. 3 means to pull the video recording from the day before yesterday from the device.</p>
        :type DayOffset: int
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None
        self._DayOffset = None

    @property
    def TemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""<p>Template name</p>
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""<p>Cloud Upload Time Period (settings can be done by week, support setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        r"""<p>Recording time period (settings can be done by week. You can set multiple time periods each day, each not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        r"""<p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DayOffset(self):
        r"""<p>Cycle offset. Default value: 1. It means to pull yesterday's video recording from the device. 0 means to pull today's video recording from the device. 3 means to pull the video recording from the day before yesterday from the device.</p>
        :rtype: int
        """
        return self._DayOffset

    @DayOffset.setter
    def DayOffset(self, DayOffset):
        self._DayOffset = DayOffset


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._DayOffset = params.get("DayOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordBackupTemplateRequest(AbstractModel):
    r"""DescribeRecordBackupTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID (obtain from the ListRecordBackupTemplates API used to query the video recording cloud template list)
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""Template ID (obtain from the ListRecordBackupTemplates API used to query the video recording cloud template list)
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordBackupTemplateResponse(AbstractModel):
    r"""DescribeRecordBackupTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupTemplateData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordBackupTemplateData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeRecordBackupTemplateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordFileData(AbstractModel):
    r"""data used for querying the recording timeline information of the device cloud

    """

    def __init__(self):
        r"""
        :param _Tips: Notification type. 0: No archived video recording within the period. 1: Archived video recording within the period.
        :type Tips: int
        :param _List: Exists in array format. If it does not exist, the field content is empty.
        :type List: list of RecordTimeLine
        """
        self._Tips = None
        self._List = None

    @property
    def Tips(self):
        r"""Notification type. 0: No archived video recording within the period. 1: Archived video recording within the period.
        :rtype: int
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def List(self):
        r"""Exists in array format. If it does not exist, the field content is empty.
        :rtype: list of RecordTimeLine
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._Tips = params.get("Tips")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RecordTimeLine()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordFileRequest(AbstractModel):
    r"""DescribeRecordFile request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID to which the channel belongs
        :type DeviceId: str
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _StartTime: Search start time in UTC seconds, for example: 1662114146. The longest period between the start and end times is one day and cannot span multiple days.
        :type StartTime: int
        :param _EndTime: Search end time, UTC seconds. Example: 1662114246. The longest period between the start and end times is one day, and cannot span multiple days.
        :type EndTime: int
        :param _WithUrl: Whether to carry the playback url for each time period
        :type WithUrl: bool
        """
        self._DeviceId = None
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None
        self._WithUrl = None

    @property
    def DeviceId(self):
        r"""Device ID to which the channel belongs
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        r"""Search start time in UTC seconds, for example: 1662114146. The longest period between the start and end times is one day and cannot span multiple days.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Search end time, UTC seconds. Example: 1662114246. The longest period between the start and end times is one day, and cannot span multiple days.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def WithUrl(self):
        r"""Whether to carry the playback url for each time period
        :rtype: bool
        """
        return self._WithUrl

    @WithUrl.setter
    def WithUrl(self, WithUrl):
        self._WithUrl = WithUrl


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._WithUrl = params.get("WithUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordFileResponse(AbstractModel):
    r"""DescribeRecordFile response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordFileData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordFileData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeRecordFileData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordPlanRequest(AbstractModel):
    r"""DescribeRecordPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Real-time cloud plan ID
        :type PlanId: str
        """
        self._PlanId = None

    @property
    def PlanId(self):
        r"""Real-time cloud plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordPlanResponse(AbstractModel):
    r"""DescribeRecordPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Output result
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlanBaseInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Output result
        :rtype: :class:`tencentcloud.iss.v20230517.models.RecordPlanBaseInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RecordPlanBaseInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordPlaybackUrlRequest(AbstractModel):
    r"""DescribeRecordPlaybackUrl request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Device channel ID
        :type ChannelId: str
        :param _StartTime: Replay start time in UTC seconds, for example: 1662114146. The longest period between the start and end times is one day and cannot span multiple days.
        :type StartTime: int
        :param _EndTime: Replay end time in UTC seconds, for example: 1662114246. The longest period between the start and end times is one day, and cannot span multiple days.
        :type EndTime: int
        :param _IsInternal: Whether to obtain the intranet address
        :type IsInternal: bool
        :param _CorrectTimestamp: Whether to enable timestamp correction during cloud video playback. This primarily addresses issues such as timestamp reversal or rollback that cause playback failure.
        :type CorrectTimestamp: bool
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None
        self._IsInternal = None
        self._CorrectTimestamp = None

    @property
    def ChannelId(self):
        r"""Device channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        r"""Replay start time in UTC seconds, for example: 1662114146. The longest period between the start and end times is one day and cannot span multiple days.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Replay end time in UTC seconds, for example: 1662114246. The longest period between the start and end times is one day, and cannot span multiple days.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IsInternal(self):
        r"""Whether to obtain the intranet address
        :rtype: bool
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal

    @property
    def CorrectTimestamp(self):
        r"""Whether to enable timestamp correction during cloud video playback. This primarily addresses issues such as timestamp reversal or rollback that cause playback failure.
        :rtype: bool
        """
        return self._CorrectTimestamp

    @CorrectTimestamp.setter
    def CorrectTimestamp(self, CorrectTimestamp):
        self._CorrectTimestamp = CorrectTimestamp


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._IsInternal = params.get("IsInternal")
        self._CorrectTimestamp = params.get("CorrectTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordPlaybackUrlResponse(AbstractModel):
    r"""DescribeRecordPlaybackUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned results.
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlaybackUrl`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned results.
        :rtype: :class:`tencentcloud.iss.v20230517.models.RecordPlaybackUrl`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RecordPlaybackUrl()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordRetrieveTaskData(AbstractModel):
    r"""data for querying the details of a cloud recording retrieval task

    """

    def __init__(self):
        r"""
        :param _TaskId: Retrieval task ID
        :type TaskId: str
        :param _TaskName: Task name for retrieval
        :type TaskName: str
        :param _StartTime: Start time of video recording retrieval
        :type StartTime: int
        :param _EndTime: Retrieval end time of the video recording
        :type EndTime: int
        :param _Mode: Retrieval mode. 1: speed mode. Others not supported currently.
        :type Mode: int
        :param _Expiration: Replica validity period
        :type Expiration: int
        :param _Status: Task status. 0: Retrieved, 1: Retrieving, 2: To be retrieved
        :type Status: int
        :param _Capacity: Retrieval capacity, in MB.
        :type Capacity: float
        :param _Channels: Task device channel id
        :type Channels: list of RecordRetrieveTaskChannelInfo
        :param _Describe: Task description
        :type Describe: str
        :param _ChannelCount: Number of task channels
        :type ChannelCount: int
        """
        self._TaskId = None
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Status = None
        self._Capacity = None
        self._Channels = None
        self._Describe = None
        self._ChannelCount = None

    @property
    def TaskId(self):
        r"""Retrieval task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name for retrieval
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        r"""Start time of video recording retrieval
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Retrieval end time of the video recording
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        r"""Retrieval mode. 1: speed mode. Others not supported currently.
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        r"""Replica validity period
        :rtype: int
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Status(self):
        r"""Task status. 0: Retrieved, 1: Retrieving, 2: To be retrieved
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Capacity(self):
        r"""Retrieval capacity, in MB.
        :rtype: float
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Channels(self):
        r"""Task device channel id
        :rtype: list of RecordRetrieveTaskChannelInfo
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def Describe(self):
        r"""Task description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ChannelCount(self):
        r"""Number of task channels
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        self._Status = params.get("Status")
        self._Capacity = params.get("Capacity")
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = RecordRetrieveTaskChannelInfo()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._Describe = params.get("Describe")
        self._ChannelCount = params.get("ChannelCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordRetrieveTaskRequest(AbstractModel):
    r"""DescribeRecordRetrieveTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Cloud recording retrieval task ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""Cloud recording retrieval task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordRetrieveTaskResponse(AbstractModel):
    r"""DescribeRecordRetrieveTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeRecordRetrieveTaskData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeRecordRetrieveTaskData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeRecordRetrieveTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRecordTemplateRequest(AbstractModel):
    r"""DescribeRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID.
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""Template ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordTemplateResponse(AbstractModel):
    r"""DescribeRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned results
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned results
        :rtype: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RecordTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeStreamAuthData(AbstractModel):
    r"""Data structure returned by push/pull stream authentication query

    """

    def __init__(self):
        r"""
        :param _Id: Authentication configuration ID (uuid).
        :type Id: str
        :param _PullState: Whether to enable playback authentication. Valid values: `1`: enable, `0`: disable.
        :type PullState: int
        :param _PullSecret: Playback key (alphanumeric only, length: 0-10 characters)
        :type PullSecret: str
        :param _PullExpired: Playback expiration time (unit: minute)
        :type PullExpired: int
        :param _PushState: Whether to enable stream authentication (1: enable, 0: disable)
        :type PushState: int
        :param _PushSecret: Stream key (alphanumeric only, length 0-10 characters)
        :type PushSecret: str
        :param _PushExpired: Push expiration time (unit: minute)
        :type PushExpired: int
        :param _AppId: User ID.
        :type AppId: int
        """
        self._Id = None
        self._PullState = None
        self._PullSecret = None
        self._PullExpired = None
        self._PushState = None
        self._PushSecret = None
        self._PushExpired = None
        self._AppId = None

    @property
    def Id(self):
        r"""Authentication configuration ID (uuid).
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PullState(self):
        r"""Whether to enable playback authentication. Valid values: `1`: enable, `0`: disable.
        :rtype: int
        """
        return self._PullState

    @PullState.setter
    def PullState(self, PullState):
        self._PullState = PullState

    @property
    def PullSecret(self):
        r"""Playback key (alphanumeric only, length: 0-10 characters)
        :rtype: str
        """
        return self._PullSecret

    @PullSecret.setter
    def PullSecret(self, PullSecret):
        self._PullSecret = PullSecret

    @property
    def PullExpired(self):
        r"""Playback expiration time (unit: minute)
        :rtype: int
        """
        return self._PullExpired

    @PullExpired.setter
    def PullExpired(self, PullExpired):
        self._PullExpired = PullExpired

    @property
    def PushState(self):
        r"""Whether to enable stream authentication (1: enable, 0: disable)
        :rtype: int
        """
        return self._PushState

    @PushState.setter
    def PushState(self, PushState):
        self._PushState = PushState

    @property
    def PushSecret(self):
        r"""Stream key (alphanumeric only, length 0-10 characters)
        :rtype: str
        """
        return self._PushSecret

    @PushSecret.setter
    def PushSecret(self, PushSecret):
        self._PushSecret = PushSecret

    @property
    def PushExpired(self):
        r"""Push expiration time (unit: minute)
        :rtype: int
        """
        return self._PushExpired

    @PushExpired.setter
    def PushExpired(self, PushExpired):
        self._PushExpired = PushExpired

    @property
    def AppId(self):
        r"""User ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._PullState = params.get("PullState")
        self._PullSecret = params.get("PullSecret")
        self._PullExpired = params.get("PullExpired")
        self._PushState = params.get("PushState")
        self._PushSecret = params.get("PushSecret")
        self._PushExpired = params.get("PushExpired")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamAuthRequest(AbstractModel):
    r"""DescribeStreamAuth request structure.

    """


class DescribeStreamAuthResponse(AbstractModel):
    r"""DescribeStreamAuth response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeStreamAuthData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeStreamAuthData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeStreamAuthData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    r"""DescribeTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of a simple or complex task
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""ID of a simple or complex task
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResponse(AbstractModel):
    r"""DescribeTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Task details.
        :type Data: :class:`tencentcloud.iss.v20230517.models.TaskData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Task details.
        :rtype: :class:`tencentcloud.iss.v20230517.models.TaskData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeUserDeviceListRequest(AbstractModel):
    r"""DescribeUserDeviceList request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceIds: Device Id list
        :type DeviceIds: list of str
        """
        self._DeviceIds = None

    @property
    def DeviceIds(self):
        r"""Device Id list
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserDeviceListResponse(AbstractModel):
    r"""DescribeUserDeviceList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceListData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceListData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeDeviceListData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeUserDeviceRequest(AbstractModel):
    r"""DescribeUserDevice request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID (obtain from the ListDevices api)
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        r"""Device ID (obtain from the ListDevices api)
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserDeviceResponse(AbstractModel):
    r"""DescribeUserDevice response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeDeviceData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVLPlanRequest(AbstractModel):
    r"""DescribeVLPlan request structure.

    """

    def __init__(self):
        r"""
        :param _VLPlanId: <p>Plan ID</p>
        :type VLPlanId: str
        """
        self._VLPlanId = None

    @property
    def VLPlanId(self):
        r"""<p>Plan ID</p>
        :rtype: str
        """
        return self._VLPlanId

    @VLPlanId.setter
    def VLPlanId(self, VLPlanId):
        self._VLPlanId = VLPlanId


    def _deserialize(self, params):
        self._VLPlanId = params.get("VLPlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVLPlanResponse(AbstractModel):
    r"""DescribeVLPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Visual understanding plan information</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VLPlanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Visual understanding plan information</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VLPlanInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VLPlanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVLPlanResultRequest(AbstractModel):
    r"""DescribeVLPlanResult request structure.

    """

    def __init__(self):
        r"""
        :param _VLPlanResultId: <p>Analysis result ID</p>
        :type VLPlanResultId: str
        """
        self._VLPlanResultId = None

    @property
    def VLPlanResultId(self):
        r"""<p>Analysis result ID</p>
        :rtype: str
        """
        return self._VLPlanResultId

    @VLPlanResultId.setter
    def VLPlanResultId(self, VLPlanResultId):
        self._VLPlanResultId = VLPlanResultId


    def _deserialize(self, params):
        self._VLPlanResultId = params.get("VLPlanResultId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVLPlanResultResponse(AbstractModel):
    r"""DescribeVLPlanResult response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Analysis result details</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VLPlanResultDetailInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Analysis result details</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VLPlanResultDetailInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VLPlanResultDetailInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVLTemplateRequest(AbstractModel):
    r"""DescribeVLTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _VLTemplateId: <p>Template ID</p>
        :type VLTemplateId: str
        """
        self._VLTemplateId = None

    @property
    def VLTemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._VLTemplateId

    @VLTemplateId.setter
    def VLTemplateId(self, VLTemplateId):
        self._VLTemplateId = VLTemplateId


    def _deserialize(self, params):
        self._VLTemplateId = params.get("VLTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVLTemplateResponse(AbstractModel):
    r"""DescribeVLTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Visual understanding template information</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VLTemplateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Visual understanding template information</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VLTemplateInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VLTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVideoBitRateList(AbstractModel):
    r"""Result list returned from querying the bitrate of a video channel

    """

    def __init__(self):
        r"""
        :param _BitRates: List of channel bitrates
        :type BitRates: list of BitRateInfo
        """
        self._BitRates = None

    @property
    def BitRates(self):
        r"""List of channel bitrates
        :rtype: list of BitRateInfo
        """
        return self._BitRates

    @BitRates.setter
    def BitRates(self, BitRates):
        self._BitRates = BitRates


    def _deserialize(self, params):
        if params.get("BitRates") is not None:
            self._BitRates = []
            for item in params.get("BitRates"):
                obj = BitRateInfo()
                obj._deserialize(item)
                self._BitRates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoBitRateRequest(AbstractModel):
    r"""DescribeVideoBitRate request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelIds: Channel ID list
        :type ChannelIds: list of str
        """
        self._ChannelIds = None

    @property
    def ChannelIds(self):
        r"""Channel ID list
        :rtype: list of str
        """
        return self._ChannelIds

    @ChannelIds.setter
    def ChannelIds(self, ChannelIds):
        self._ChannelIds = ChannelIds


    def _deserialize(self, params):
        self._ChannelIds = params.get("ChannelIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoBitRateResponse(AbstractModel):
    r"""DescribeVideoBitRate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: None.
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeVideoBitRateList`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""None.
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoBitRateList`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeVideoBitRateList()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVideoDownloadUrlData(AbstractModel):
    r"""Returned data for obtaining the cloud recording download URL

    """

    def __init__(self):
        r"""
        :param _Url: Video recording file download URL
Note:
The URL is valid for 10 minutes. Access will be denied after expiry. Obtain a new one if needed. 
Video file download uses chunked transfer encoding, and the response header is Transfer-Encoding: chunked. 
The naming format of the downloaded file is {ChannelId}-{BeginTime}-{EndTime}.{FileType}
        :type Url: str
        :param _ActualBeginTime: Actual download start time of the video recording
Note: This field is returned only when the IsRespActualTime parameter is set to true in the request.
        :type ActualBeginTime: str
        :param _ActualEndTime: Actual download end time of the video recording
Note: This field is returned only when the IsRespActualTime parameter is set to true in the request.
        :type ActualEndTime: str
        """
        self._Url = None
        self._ActualBeginTime = None
        self._ActualEndTime = None

    @property
    def Url(self):
        r"""Video recording file download URL
Note:
The URL is valid for 10 minutes. Access will be denied after expiry. Obtain a new one if needed. 
Video file download uses chunked transfer encoding, and the response header is Transfer-Encoding: chunked. 
The naming format of the downloaded file is {ChannelId}-{BeginTime}-{EndTime}.{FileType}
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ActualBeginTime(self):
        r"""Actual download start time of the video recording
Note: This field is returned only when the IsRespActualTime parameter is set to true in the request.
        :rtype: str
        """
        return self._ActualBeginTime

    @ActualBeginTime.setter
    def ActualBeginTime(self, ActualBeginTime):
        self._ActualBeginTime = ActualBeginTime

    @property
    def ActualEndTime(self):
        r"""Actual download end time of the video recording
Note: This field is returned only when the IsRespActualTime parameter is set to true in the request.
        :rtype: str
        """
        return self._ActualEndTime

    @ActualEndTime.setter
    def ActualEndTime(self, ActualEndTime):
        self._ActualEndTime = ActualEndTime


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._ActualBeginTime = params.get("ActualBeginTime")
        self._ActualEndTime = params.get("ActualEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoDownloadUrlRequest(AbstractModel):
    r"""DescribeVideoDownloadUrl request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _BeginTime: Download start time in UTC seconds. The longest period between the start and end times is 60 minutes and cannot span across days.
Note: The actual downloaded file duration may be longer than this period. You can obtain the actual download start time and end time by specifying the IsRespActualTime parameter. This is because downloads are aligned by TS segments to ensure data integrity and include the entire specified period.
        :type BeginTime: str
        :param _EndTime: Download end time in UTC seconds. The longest period between the start and end times is 60 minutes and cannot span across days.
Note: The actual downloaded file duration may be longer than this period. You can obtain the actual download start time and end time by specifying the IsRespActualTime parameter. This is because downloads are aligned by TS segments to ensure data integrity and include the entire specified period.
        :type EndTime: str
        :param _FileType: File format. "mp4": MP4 format. "ts": TS file format.
        :type FileType: str
        :param _IsRespActualTime: data carries the actual download video recording start time and end time required or not
        :type IsRespActualTime: bool
        :param _IsInternal: Whether to return the private network download URL. Default false: the public network download URL is returned. If true, the private network download URL is returned.
        :type IsInternal: bool
        :param _Expires: Set the valid period of the URL. The minimum value is 1 second and the maximum value is 86400 seconds. If not set, the default is 600 seconds.
        :type Expires: int
        :param _IsSupportG711: Whether the downloaded MP4 file supports G711 audio encoding. 
Note: If the audio encoding in cloud recording is AAC, then the downloaded MP4 supports AAC encoding by default.
If the audio encoding in the cloud recording is G711 and IsSupportG711 is set to true, the downloaded MP4 supports G711 audio encoding.
If the audio encoding in the cloud recording is G711 and IsSupportG711 is set to false, the downloaded MP4 does not support G711 audio encoding.
This parameter is valid only when FileType is mp4. If left unset, it defaults to false.
        :type IsSupportG711: bool
        """
        self._ChannelId = None
        self._BeginTime = None
        self._EndTime = None
        self._FileType = None
        self._IsRespActualTime = None
        self._IsInternal = None
        self._Expires = None
        self._IsSupportG711 = None

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def BeginTime(self):
        r"""Download start time in UTC seconds. The longest period between the start and end times is 60 minutes and cannot span across days.
Note: The actual downloaded file duration may be longer than this period. You can obtain the actual download start time and end time by specifying the IsRespActualTime parameter. This is because downloads are aligned by TS segments to ensure data integrity and include the entire specified period.
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""Download end time in UTC seconds. The longest period between the start and end times is 60 minutes and cannot span across days.
Note: The actual downloaded file duration may be longer than this period. You can obtain the actual download start time and end time by specifying the IsRespActualTime parameter. This is because downloads are aligned by TS segments to ensure data integrity and include the entire specified period.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileType(self):
        r"""File format. "mp4": MP4 format. "ts": TS file format.
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def IsRespActualTime(self):
        r"""data carries the actual download video recording start time and end time required or not
        :rtype: bool
        """
        return self._IsRespActualTime

    @IsRespActualTime.setter
    def IsRespActualTime(self, IsRespActualTime):
        self._IsRespActualTime = IsRespActualTime

    @property
    def IsInternal(self):
        r"""Whether to return the private network download URL. Default false: the public network download URL is returned. If true, the private network download URL is returned.
        :rtype: bool
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal

    @property
    def Expires(self):
        r"""Set the valid period of the URL. The minimum value is 1 second and the maximum value is 86400 seconds. If not set, the default is 600 seconds.
        :rtype: int
        """
        return self._Expires

    @Expires.setter
    def Expires(self, Expires):
        self._Expires = Expires

    @property
    def IsSupportG711(self):
        r"""Whether the downloaded MP4 file supports G711 audio encoding. 
Note: If the audio encoding in cloud recording is AAC, then the downloaded MP4 supports AAC encoding by default.
If the audio encoding in the cloud recording is G711 and IsSupportG711 is set to true, the downloaded MP4 supports G711 audio encoding.
If the audio encoding in the cloud recording is G711 and IsSupportG711 is set to false, the downloaded MP4 does not support G711 audio encoding.
This parameter is valid only when FileType is mp4. If left unset, it defaults to false.
        :rtype: bool
        """
        return self._IsSupportG711

    @IsSupportG711.setter
    def IsSupportG711(self, IsSupportG711):
        self._IsSupportG711 = IsSupportG711


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._FileType = params.get("FileType")
        self._IsRespActualTime = params.get("IsRespActualTime")
        self._IsInternal = params.get("IsInternal")
        self._Expires = params.get("Expires")
        self._IsSupportG711 = params.get("IsSupportG711")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoDownloadUrlResponse(AbstractModel):
    r"""DescribeVideoDownloadUrl response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data structure
        :type Data: :class:`tencentcloud.iss.v20230517.models.DescribeVideoDownloadUrlData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data structure
        :rtype: :class:`tencentcloud.iss.v20230517.models.DescribeVideoDownloadUrlData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeVideoDownloadUrlData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVideoSnapshotConfigRequest(AbstractModel):
    r"""DescribeVideoSnapshotConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: <p>Screenshot configuration Id</p>
        :type ConfigId: str
        """
        self._ConfigId = None

    @property
    def ConfigId(self):
        r"""<p>Screenshot configuration Id</p>
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoSnapshotConfigResponse(AbstractModel):
    r"""DescribeVideoSnapshotConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Screenshot configuration details</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotConfigInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Screenshot configuration details</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotConfigInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VideoSnapshotConfigInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeVideoSnapshotTemplateRequest(AbstractModel):
    r"""DescribeVideoSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>Screenshot template Id</p>
        :type TemplateId: str
        """
        self._TemplateId = None

    @property
    def TemplateId(self):
        r"""<p>Screenshot template Id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVideoSnapshotTemplateResponse(AbstractModel):
    r"""DescribeVideoSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Screenshot template description</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotTemplateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Screenshot template description</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotTemplateInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VideoSnapshotTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class EffectiveTime(AbstractModel):
    r"""Effective period

    """

    def __init__(self):
        r"""
        :param _BeginTime: <p>Start time</p><p>Parameter format: hh:mm:ss</p>
        :type BeginTime: str
        :param _EndTime: <p>End time</p><p>Parameter format: hh:mm:ss</p>
        :type EndTime: str
        :param _WeekDay: <p>Repetition cycle: 1-Monday 2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday 7-Sunday</p><p>Value range: [1, 7]</p>
        :type WeekDay: int
        """
        self._BeginTime = None
        self._EndTime = None
        self._WeekDay = None

    @property
    def BeginTime(self):
        r"""<p>Start time</p><p>Parameter format: hh:mm:ss</p>
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""<p>End time</p><p>Parameter format: hh:mm:ss</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def WeekDay(self):
        r"""<p>Repetition cycle: 1-Monday 2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday 7-Sunday</p><p>Value range: [1, 7]</p>
        :rtype: int
        """
        return self._WeekDay

    @WeekDay.setter
    def WeekDay(self, WeekDay):
        self._WeekDay = WeekDay


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._WeekDay = params.get("WeekDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GBDeviceSnapInfo(AbstractModel):
    r"""Snapshot information

    """

    def __init__(self):
        r"""
        :param _FileName: File name
        :type FileName: str
        :param _DownloadUrl: Download link. Empty value means the stored image expires.
        :type DownloadUrl: str
        :param _ImageSize: Image size in Unit B.
        :type ImageSize: int
        :param _CreatedTime: Creation time of the file.
        :type CreatedTime: str
        :param _ReceivedTime: Reception time of the image
        :type ReceivedTime: str
        :param _PreviewUrl: Preview link. Empty value means the stored image expires.
        :type PreviewUrl: str
        :param _SessionId: National standard signaling session ID, corresponding to the request_id returned by the ControlDeviceSnapshot API.
        :type SessionId: str
        """
        self._FileName = None
        self._DownloadUrl = None
        self._ImageSize = None
        self._CreatedTime = None
        self._ReceivedTime = None
        self._PreviewUrl = None
        self._SessionId = None

    @property
    def FileName(self):
        r"""File name
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def DownloadUrl(self):
        r"""Download link. Empty value means the stored image expires.
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def ImageSize(self):
        r"""Image size in Unit B.
        :rtype: int
        """
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def CreatedTime(self):
        r"""Creation time of the file.
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ReceivedTime(self):
        r"""Reception time of the image
        :rtype: str
        """
        return self._ReceivedTime

    @ReceivedTime.setter
    def ReceivedTime(self, ReceivedTime):
        self._ReceivedTime = ReceivedTime

    @property
    def PreviewUrl(self):
        r"""Preview link. Empty value means the stored image expires.
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl

    @property
    def SessionId(self):
        r"""National standard signaling session ID, corresponding to the request_id returned by the ControlDeviceSnapshot API.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._DownloadUrl = params.get("DownloadUrl")
        self._ImageSize = params.get("ImageSize")
        self._CreatedTime = params.get("CreatedTime")
        self._ReceivedTime = params.get("ReceivedTime")
        self._PreviewUrl = params.get("PreviewUrl")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISAPIOutputData(AbstractModel):
    r"""Returned data of the ISUP intelligent secure access API

    """

    def __init__(self):
        r"""
        :param _OutputData: Output parameter
        :type OutputData: str
        """
        self._OutputData = None

    @property
    def OutputData(self):
        r"""Output parameter
        :rtype: str
        """
        return self._OutputData

    @OutputData.setter
    def OutputData(self, OutputData):
        self._OutputData = OutputData


    def _deserialize(self, params):
        self._OutputData = params.get("OutputData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSceneInfo(AbstractModel):
    r"""Image scenario configuration

    """

    def __init__(self):
        r"""
        :param _Type: <p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :type Type: int
        :param _Interval: <p>Frame capturing frequency</p><p>When Type=1, the value range is [5, 180] seconds; when Type=2, the value range is [30, 36000] seconds</p>
        :type Interval: int
        :param _MultiMode: <p>Multiple screenshots mode</p>
        :type MultiMode: :class:`tencentcloud.iss.v20230517.models.MultiSnapshotMode`
        """
        self._Type = None
        self._Interval = None
        self._MultiMode = None

    @property
    def Type(self):
        r"""<p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        r"""<p>Frame capturing frequency</p><p>When Type=1, the value range is [5, 180] seconds; when Type=2, the value range is [30, 36000] seconds</p>
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MultiMode(self):
        r"""<p>Multiple screenshots mode</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.MultiSnapshotMode`
        """
        return self._MultiMode

    @MultiMode.setter
    def MultiMode(self, MultiMode):
        self._MultiMode = MultiMode


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        if params.get("MultiMode") is not None:
            self._MultiMode = MultiSnapshotMode()
            self._MultiMode._deserialize(params.get("MultiMode"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageUrlInfo(AbstractModel):
    r"""Image download URL information

    """

    def __init__(self):
        r"""
        :param _ImageId: <p>Image Id</p>
        :type ImageId: str
        :param _ImageUrl: <p>Image Url</p>
        :type ImageUrl: str
        :param _ErrorMessage: <p>Error information</p><p>Reason for failure to get the image url</p>
        :type ErrorMessage: str
        """
        self._ImageId = None
        self._ImageUrl = None
        self._ErrorMessage = None

    @property
    def ImageId(self):
        r"""<p>Image Id</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageUrl(self):
        r"""<p>Image Url</p>
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ErrorMessage(self):
        r"""<p>Error information</p><p>Reason for failure to get the image url</p>
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageUrl = params.get("ImageUrl")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifeCycleData(AbstractModel):
    r"""Lifecycle, cloud file lifecycle settings, the time when cold and hot storage is managed for files

    """

    def __init__(self):
        r"""
        :param _Transition: Hot storage duration of cloud files in days. Minimum value: 1. Maximum value: 3650.
        :type Transition: int
        :param _Expiration: Cold storage duration of cloud files in days. 0 means leave unset. The minimum is 60 days when set. The sum of the Expiration and Transition fields is no more than 3650 days.
        :type Expiration: int
        """
        self._Transition = None
        self._Expiration = None

    @property
    def Transition(self):
        r"""Hot storage duration of cloud files in days. Minimum value: 1. Maximum value: 3650.
        :rtype: int
        """
        return self._Transition

    @Transition.setter
    def Transition(self, Transition):
        self._Transition = Transition

    @property
    def Expiration(self):
        r"""Cold storage duration of cloud files in days. 0 means leave unset. The minimum is 60 days when set. The sum of the Expiration and Transition fields is no more than 3650 days.
        :rtype: int
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration


    def _deserialize(self, params):
        self._Transition = params.get("Transition")
        self._Expiration = params.get("Expiration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDeviceInfo(AbstractModel):
    r"""to the get device list request

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID
        :type DeviceId: str
        :param _Code: Device code
        :type Code: str
        :param _Status: Device status. 0: unregistered; 1: online; 2: offline; 3: disabled
        :type Status: int
        :param _TransportProtocol: Device streaming protocol. 1: UDP, 2: TCP
        :type TransportProtocol: int
        :param _Name: Device name.
        :type Name: str
        :param _Type: Device type. 1: IPC. 2: NVR
        :type Type: int
        :param _Password: Device password
        :type Password: str
        :param _Description: Description
        :type Description: str
        :param _ClusterId: Node ID of the device access service
        :type ClusterId: str
        :param _ClusterName: Service node name
        :type ClusterName: str
        :param _AccessProtocol: Access protocol. 1: RTMP, 2: GB, 3: GW
        :type AccessProtocol: int
        :param _OrganizationId: Organization ID of the device
        :type OrganizationId: str
        :param _ChannelNum: Number of channels
        :type ChannelNum: int
        """
        self._DeviceId = None
        self._Code = None
        self._Status = None
        self._TransportProtocol = None
        self._Name = None
        self._Type = None
        self._Password = None
        self._Description = None
        self._ClusterId = None
        self._ClusterName = None
        self._AccessProtocol = None
        self._OrganizationId = None
        self._ChannelNum = None

    @property
    def DeviceId(self):
        r"""Device ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        r"""Device code
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Status(self):
        r"""Device status. 0: unregistered; 1: online; 2: offline; 3: disabled
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TransportProtocol(self):
        r"""Device streaming protocol. 1: UDP, 2: TCP
        :rtype: int
        """
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Name(self):
        r"""Device name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""Device type. 1: IPC. 2: NVR
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Password(self):
        r"""Device password
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""Description
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClusterId(self):
        r"""Node ID of the device access service
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""Service node name
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def AccessProtocol(self):
        r"""Access protocol. 1: RTMP, 2: GB, 3: GW
        :rtype: int
        """
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def OrganizationId(self):
        r"""Organization ID of the device
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def ChannelNum(self):
        r"""Number of channels
        :rtype: int
        """
        return self._ChannelNum

    @ChannelNum.setter
    def ChannelNum(self, ChannelNum):
        self._ChannelNum = ChannelNum


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Status = params.get("Status")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._AccessProtocol = params.get("AccessProtocol")
        self._OrganizationId = params.get("OrganizationId")
        self._ChannelNum = params.get("ChannelNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDeviceSnapshotsRequest(AbstractModel):
    r"""ListDeviceSnapshots request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _DeviceId: Device ID (this field is not effective yet)
        :type DeviceId: str
        :param _Start: Query start time. Default query: on the day.
        :type Start: int
        :param _End: Query end time. Default query: on the day.
        :type End: int
        :param _PageNumber: Page number, which is 1 by default.
        :type PageNumber: int
        :param _PageSize: Pagination size. Default: 200. Maximum: 2000
        :type PageSize: int
        """
        self._ChannelId = None
        self._DeviceId = None
        self._Start = None
        self._End = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def DeviceId(self):
        r"""Device ID (this field is not effective yet)
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Start(self):
        r"""Query start time. Default query: on the day.
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        r"""Query end time. Default query: on the day.
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def PageNumber(self):
        r"""Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size. Default: 200. Maximum: 2000
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._DeviceId = params.get("DeviceId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDeviceSnapshotsResponse(AbstractModel):
    r"""ListDeviceSnapshots response structure.

    """

    def __init__(self):
        r"""
        :param _Data: List of snapshot information
        :type Data: list of GBDeviceSnapInfo
        :param _TotalCount: Total snapshot results
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        r"""List of snapshot information
        :rtype: list of GBDeviceSnapInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total snapshot results
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = GBDeviceSnapInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListDevicesRequest(AbstractModel):
    r"""ListDevices request structure.

    """

    def __init__(self):
        r"""
        :param _OrganizationId: Organization ID
        :type OrganizationId: str
        :param _IsContainSubLevel: Whether to obtain the device list of the current level and sub-levels. Default value: false.
        :type IsContainSubLevel: bool
        :param _IsContainUser: Whether the devices already associated with the current user are included. Default value: false.
        :type IsContainUser: bool
        :param _AccessProtocol: Device access protocol. 1: RTMP, 2: GB, 3: GW, 4: IVCP (private protocol)
        :type AccessProtocol: int
        :param _Type: Device type. 1: IPC, 2: NVR
        :type Type: int
        :param _Status: Device status. 0: unregistered; 1: online; 2: offline; 3: disabled.	
        :type Status: int
        :param _ClusterId: Service node ID
        :type ClusterId: str
        :param _Keyword: Keyword for fuzzy search of devices
        :type Keyword: str
        :param _CurrentUin: Uin of the current user
        :type CurrentUin: int
        :param _PageNumber: Page number. Default value: 1.
        :type PageNumber: int
        :param _PageSize: Number of items per page. Default value: 20. Maximum: 10000 per page.
        :type PageSize: int
        """
        self._OrganizationId = None
        self._IsContainSubLevel = None
        self._IsContainUser = None
        self._AccessProtocol = None
        self._Type = None
        self._Status = None
        self._ClusterId = None
        self._Keyword = None
        self._CurrentUin = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def OrganizationId(self):
        r"""Organization ID
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def IsContainSubLevel(self):
        r"""Whether to obtain the device list of the current level and sub-levels. Default value: false.
        :rtype: bool
        """
        return self._IsContainSubLevel

    @IsContainSubLevel.setter
    def IsContainSubLevel(self, IsContainSubLevel):
        self._IsContainSubLevel = IsContainSubLevel

    @property
    def IsContainUser(self):
        r"""Whether the devices already associated with the current user are included. Default value: false.
        :rtype: bool
        """
        return self._IsContainUser

    @IsContainUser.setter
    def IsContainUser(self, IsContainUser):
        self._IsContainUser = IsContainUser

    @property
    def AccessProtocol(self):
        r"""Device access protocol. 1: RTMP, 2: GB, 3: GW, 4: IVCP (private protocol)
        :rtype: int
        """
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        r"""Device type. 1: IPC, 2: NVR
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""Device status. 0: unregistered; 1: online; 2: offline; 3: disabled.	
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ClusterId(self):
        r"""Service node ID
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Keyword(self):
        r"""Keyword for fuzzy search of devices
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def CurrentUin(self):
        r"""Uin of the current user
        :rtype: int
        """
        return self._CurrentUin

    @CurrentUin.setter
    def CurrentUin(self, CurrentUin):
        self._CurrentUin = CurrentUin

    @property
    def PageNumber(self):
        r"""Page number. Default value: 1.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of items per page. Default value: 20. Maximum: 10000 per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._IsContainSubLevel = params.get("IsContainSubLevel")
        self._IsContainUser = params.get("IsContainUser")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._ClusterId = params.get("ClusterId")
        self._Keyword = params.get("Keyword")
        self._CurrentUin = params.get("CurrentUin")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDevicesResponse(AbstractModel):
    r"""ListDevices response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Device list details
        :type Data: list of ListDeviceInfo
        :param _TotalCount: Total number of devices
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Device list details
        :rtype: list of ListDeviceInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""Total number of devices
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ListDeviceInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListForbidplayChannelsData(AbstractModel):
    r"""data of the channel list where streaming is forbidden for the user

    """

    def __init__(self):
        r"""
        :param _PageNumber: Which page.
        :type PageNumber: int
        :param _PageSize: Number of devices on the current page
        :type PageSize: int
        :param _TotalCount: Total number of device channels in this query
        :type TotalCount: int
        :param _List: Device channel information list
        :type List: list of ChannelAttrInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._List = None

    @property
    def PageNumber(self):
        r"""Which page.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of devices on the current page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of device channels in this query
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""Device channel information list
        :rtype: list of ChannelAttrInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ChannelAttrInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationChannelsData(AbstractModel):
    r"""data of the channel list query under the organizational unit directory

    """

    def __init__(self):
        r"""
        :param _PageNumber: Which page.
        :type PageNumber: int
        :param _PageSize: Number of devices on the current page
        :type PageSize: int
        :param _TotalCount: Total number of device channels in this query
        :type TotalCount: int
        :param _List: List of device channel information
        :type List: list of OrganizationChannelInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._List = None

    @property
    def PageNumber(self):
        r"""Which page.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of devices on the current page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of device channels in this query
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""List of device channel information
        :rtype: list of OrganizationChannelInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = OrganizationChannelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationChannelsRequest(AbstractModel):
    r"""ListOrganizationChannels request structure.

    """

    def __init__(self):
        r"""
        :param _OrganizationId: Organization ID
        :type OrganizationId: str
        :param _PageSize: Maximum number of items per page
        :type PageSize: int
        :param _PageNumber: Which page. 
        :type PageNumber: int
        :param _DeviceName: Query condition. Query by device name.
Only one query condition can take effect at a time. Length not exceeding 32 bytes.
        :type DeviceName: str
        :param _ChannelName: Query condition. Proceed to query by channel name.
Only one query condition can take effect at a time. Length not exceeding 32 bytes.
        :type ChannelName: str
        """
        self._OrganizationId = None
        self._PageSize = None
        self._PageNumber = None
        self._DeviceName = None
        self._ChannelName = None

    @property
    def OrganizationId(self):
        r"""Organization ID
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def PageSize(self):
        r"""Maximum number of items per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Which page. 
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def DeviceName(self):
        r"""Query condition. Query by device name.
Only one query condition can take effect at a time. Length not exceeding 32 bytes.
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelName(self):
        r"""Query condition. Proceed to query by channel name.
Only one query condition can take effect at a time. Length not exceeding 32 bytes.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._DeviceName = params.get("DeviceName")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationChannelsResponse(AbstractModel):
    r"""ListOrganizationChannels response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelsData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListOrganizationChannelsData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListOrganizationChannelsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListRecordBackupPlanData(AbstractModel):
    r"""data for querying the recording cloud migration plan list

    """

    def __init__(self):
        r"""
        :param _PlanId: Recording cloud migration plan ID
        :type PlanId: str
        :param _PlanName: Recording cloud migration plan name
        :type PlanName: str
        :param _TemplateId: Video cloud template ID
        :type TemplateId: str
        :param _Describe: Description of the recording cloud migration plan
        :type Describe: str
        :param _LifeCycle: Cloud file lifecycle
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: Recording cloud migration plan status. `1`: in normal use. `0`: deleting, unavailable.
        :type Status: int
        :param _ChannelCount: Number of channels
        :type ChannelCount: int
        :param _CreateAt: Creation time.
        :type CreateAt: str
        :param _UpdateAt: Modification time.
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        r"""Recording cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""Recording cloud migration plan name
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Video cloud template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Description of the recording cloud migration plan
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        r"""Cloud file lifecycle
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        r"""Recording cloud migration plan status. `1`: in normal use. `0`: deleting, unavailable.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        r"""Number of channels
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""Modification time.
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupPlanDevicesData(AbstractModel):
    r"""data of the query for the associated tunnel of the recording cloud migration plan

    """

    def __init__(self):
        r"""
        :param _PageNumber: Which page.
        :type PageNumber: int
        :param _PageSize: Number of devices on the current page
        :type PageSize: int
        :param _TotalCount: Total number of device channels in this query
        :type TotalCount: int
        :param _List: List of device channel information
        :type List: list of RecordPlanChannelInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._List = None

    @property
    def PageNumber(self):
        r"""Which page.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of devices on the current page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of device channels in this query
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""List of device channel information
        :rtype: list of RecordPlanChannelInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RecordPlanChannelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupPlanDevicesRequest(AbstractModel):
    r"""ListRecordBackupPlanDevices request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Recording schedule ID (obtain from the ListRecordBackupPlans API for querying the recording cloud migration plan list)
        :type PlanId: str
        :param _DeviceName: Query by device name (if empty, this parameter is not used for reference)
        :type DeviceName: str
        :param _ChannelName: Query by channel name (if empty, ignore this parameter)
        :type ChannelName: str
        :param _OrganizationName: Query by organization name (if empty, this parameter is not used for reference)
        :type OrganizationName: str
        :param _PageSize: Maximum number of items per page
        :type PageSize: int
        :param _PageNumber: Page number
        :type PageNumber: int
        """
        self._PlanId = None
        self._DeviceName = None
        self._ChannelName = None
        self._OrganizationName = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def PlanId(self):
        r"""Recording schedule ID (obtain from the ListRecordBackupPlans API for querying the recording cloud migration plan list)
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def DeviceName(self):
        r"""Query by device name (if empty, this parameter is not used for reference)
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelName(self):
        r"""Query by channel name (if empty, ignore this parameter)
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def OrganizationName(self):
        r"""Query by organization name (if empty, this parameter is not used for reference)
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def PageSize(self):
        r"""Maximum number of items per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelName = params.get("ChannelName")
        self._OrganizationName = params.get("OrganizationName")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupPlanDevicesResponse(AbstractModel):
    r"""ListRecordBackupPlanDevices response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlanDevicesData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordBackupPlanDevicesData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListRecordBackupPlanDevicesData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListRecordBackupPlansRequest(AbstractModel):
    r"""ListRecordBackupPlans request structure.

    """


class ListRecordBackupPlansResponse(AbstractModel):
    r"""ListRecordBackupPlans response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: list of ListRecordBackupPlanData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: list of ListRecordBackupPlanData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ListRecordBackupPlanData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordBackupTemplatesData(AbstractModel):
    r"""List returned for querying cloud templates for video recording

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>Template ID</p>
        :type TemplateId: str
        :param _TemplateName: <p>Template name</p>
        :type TemplateName: str
        :param _TimeSections: <p>Cloud Upload Time Period (settings can be done by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: <p>Recording time period (settings can be done by week, supports setting multiple time periods per day, each time period greater than or equal to 10 minutes)</p>
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: <p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :type Scale: int
        :param _CreateAt: <p>Creation time.</p>
        :type CreateAt: str
        :param _UpdateAt: <p>Update time.</p>
        :type UpdateAt: str
        :param _DayOffset: <p>Cycle offset. Default: 1, which means pulling yesterday's data. 0 means pulling today's data. 3 means pulling the day before yesterday's data.</p>
        :type DayOffset: int
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None
        self._DayOffset = None

    @property
    def TemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""<p>Template name</p>
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""<p>Cloud Upload Time Period (settings can be done by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        r"""<p>Recording time period (settings can be done by week, supports setting multiple time periods per day, each time period greater than or equal to 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        r"""<p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DayOffset(self):
        r"""<p>Cycle offset. Default: 1, which means pulling yesterday's data. 0 means pulling today's data. 3 means pulling the day before yesterday's data.</p>
        :rtype: int
        """
        return self._DayOffset

    @DayOffset.setter
    def DayOffset(self, DayOffset):
        self._DayOffset = DayOffset


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._DayOffset = params.get("DayOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordBackupTemplatesRequest(AbstractModel):
    r"""ListRecordBackupTemplates request structure.

    """


class ListRecordBackupTemplatesResponse(AbstractModel):
    r"""ListRecordBackupTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: list of ListRecordBackupTemplatesData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: list of ListRecordBackupTemplatesData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ListRecordBackupTemplatesData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordPlanDevicesData(AbstractModel):
    r"""List returned data of device channels under the cloud plan

    """

    def __init__(self):
        r"""
        :param _PageNumber: Which page.
        :type PageNumber: int
        :param _PageSize: Number of devices on the current page
        :type PageSize: int
        :param _TotalCount: Total number of device channels in this query
        :type TotalCount: int
        :param _List: List of device channel information
        :type List: list of RecordPlanChannelInfo
        """
        self._PageNumber = None
        self._PageSize = None
        self._TotalCount = None
        self._List = None

    @property
    def PageNumber(self):
        r"""Which page.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of devices on the current page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalCount(self):
        r"""Total number of device channels in this query
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        r"""List of device channel information
        :rtype: list of RecordPlanChannelInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = RecordPlanChannelInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordPlanDevicesRequest(AbstractModel):
    r"""ListRecordPlanDevices request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Cloud migration plan ID
        :type PlanId: str
        :param _PageSize: Maximum number of items per page.
        :type PageSize: int
        :param _PageNumber: Which page.
        :type PageNumber: int
        :param _DeviceName: Query by device name. If it is empty, ignore this parameter.
Only one of the channel name, device name, and organization name is valid at the same time. If multiple fields have values at the same time, query by the priority order of channel name, device name, and organization name. If all are empty, perform a full query. The length cannot exceed 32 bytes.
        :type DeviceName: str
        :param _ChannelName: Query by channel name. If it is empty, ignore this parameter.
Only one of the channel name, device name, and organization name is valid at the same time. If multiple fields have values at the same time, query by the priority order of channel name, device name, and organization name. If all are empty, perform a full query. The length cannot exceed 32 bytes.
        :type ChannelName: str
        :param _OrganizationName: Query by organization name. If it is empty, ignore this parameter.
Only one of the channel name, device name, and organization name is valid at the same time. If multiple fields have values at the same time, query by the priority order of channel name, device name, and organization name. If all are empty, perform a full query. The length cannot exceed 32 bytes.
        :type OrganizationName: str
        """
        self._PlanId = None
        self._PageSize = None
        self._PageNumber = None
        self._DeviceName = None
        self._ChannelName = None
        self._OrganizationName = None

    @property
    def PlanId(self):
        r"""Cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PageSize(self):
        r"""Maximum number of items per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Which page.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def DeviceName(self):
        r"""Query by device name. If it is empty, ignore this parameter.
Only one of the channel name, device name, and organization name is valid at the same time. If multiple fields have values at the same time, query by the priority order of channel name, device name, and organization name. If all are empty, perform a full query. The length cannot exceed 32 bytes.
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelName(self):
        r"""Query by channel name. If it is empty, ignore this parameter.
Only one of the channel name, device name, and organization name is valid at the same time. If multiple fields have values at the same time, query by the priority order of channel name, device name, and organization name. If all are empty, perform a full query. The length cannot exceed 32 bytes.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def OrganizationName(self):
        r"""Query by organization name. If it is empty, ignore this parameter.
Only one of the channel name, device name, and organization name is valid at the same time. If multiple fields have values at the same time, query by the priority order of channel name, device name, and organization name. If all are empty, perform a full query. The length cannot exceed 32 bytes.
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        self._DeviceName = params.get("DeviceName")
        self._ChannelName = params.get("ChannelName")
        self._OrganizationName = params.get("OrganizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRecordPlanDevicesResponse(AbstractModel):
    r"""ListRecordPlanDevices response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Output result
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanDevicesData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Output result
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListRecordPlanDevicesData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListRecordPlanDevicesData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListRecordPlansRequest(AbstractModel):
    r"""ListRecordPlans request structure.

    """


class ListRecordPlansResponse(AbstractModel):
    r"""ListRecordPlans response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned results. If a plan exists, the results are in a Json array format. If no plan exists, the field data is empty.
        :type Data: list of RecordPlanBaseInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned results. If a plan exists, the results are in a Json array format. If no plan exists, the field data is empty.
        :rtype: list of RecordPlanBaseInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RecordPlanBaseInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordRetrieveTasksRequest(AbstractModel):
    r"""ListRecordRetrieveTasks request structure.

    """


class ListRecordRetrieveTasksResponse(AbstractModel):
    r"""ListRecordRetrieveTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned results
        :type Data: list of RecordRetrieveTaskDetailsInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned results
        :rtype: list of RecordRetrieveTaskDetailsInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RecordRetrieveTaskDetailsInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListRecordTemplatesRequest(AbstractModel):
    r"""ListRecordTemplates request structure.

    """


class ListRecordTemplatesResponse(AbstractModel):
    r"""ListRecordTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Output result. If a template exists, it is in Json array format. If no template exists, the field data is empty.
        :type Data: list of RecordTemplateInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Output result. If a template exists, it is in Json array format. If no template exists, the field data is empty.
        :rtype: list of RecordTemplateInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RecordTemplateInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListSubTasksData(AbstractModel):
    r"""List the subtask list

    """

    def __init__(self):
        r"""
        :param _List: Subtask List
        :type List: list of SubTaskData
        :param _TotalCount: Subtask quantity
        :type TotalCount: int
        """
        self._List = None
        self._TotalCount = None

    @property
    def List(self):
        r"""Subtask List
        :rtype: list of SubTaskData
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        r"""Subtask quantity
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = SubTaskData()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSubTasksRequest(AbstractModel):
    r"""ListSubTasks request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Complex task ID
        :type TaskId: str
        :param _PageNumber: Page number, which is 1 by default.
        :type PageNumber: int
        :param _PageSize: Number of items per page. Default: 10.
        :type PageSize: int
        :param _Status: Default: no filtering on this field. Otherwise, filter by task status. Status code: 1-NEW, 2-RUNNING, 3-COMPLETED, 4-FAILED.
        :type Status: int
        """
        self._TaskId = None
        self._PageNumber = None
        self._PageSize = None
        self._Status = None

    @property
    def TaskId(self):
        r"""Complex task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def PageNumber(self):
        r"""Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of items per page. Default: 10.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Status(self):
        r"""Default: no filtering on this field. Otherwise, filter by task status. Status code: 1-NEW, 2-RUNNING, 3-COMPLETED, 4-FAILED.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSubTasksResponse(AbstractModel):
    r"""ListSubTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListSubTasksData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListSubTasksData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListSubTasksData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListTasksData(AbstractModel):
    r"""This API is used to query the task list.

    """

    def __init__(self):
        r"""
        :param _List: Task list
        :type List: list of TaskData
        :param _TotalCount: Number of Tasks
        :type TotalCount: int
        """
        self._List = None
        self._TotalCount = None

    @property
    def List(self):
        r"""Task list
        :rtype: list of TaskData
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        r"""Number of Tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = TaskData()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTasksRequest(AbstractModel):
    r"""ListTasks request structure.

    """

    def __init__(self):
        r"""
        :param _PageNumber: Page number, which is 1 by default.
        :type PageNumber: int
        :param _PageSize: Number of items per page. The default value is 20.
        :type PageSize: int
        :param _Operation: Default: do not filter by this field. Otherwise, filter by device operation type. Current values: BatchDeleteUserDevice, BatchDisableDevice, BatchEnableDevice.
BatchUpgradeDevice,
BatchResetDevice,
BatchRebootDevice,
BatchRefreshDeviceChannel
        :type Operation: str
        :param _Status: By default, filtering is not based on this field. Otherwise, filter by task status. Status code: 1 - Pending, 2 - Executing, 3 - Completed, 4 - Cancelled.
        :type Status: int
        :param _BeginTime: Start time.
        :type BeginTime: int
        :param _EndTime: End time.
        :type EndTime: int
        """
        self._PageNumber = None
        self._PageSize = None
        self._Operation = None
        self._Status = None
        self._BeginTime = None
        self._EndTime = None

    @property
    def PageNumber(self):
        r"""Page number, which is 1 by default.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Number of items per page. The default value is 20.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Operation(self):
        r"""Default: do not filter by this field. Otherwise, filter by device operation type. Current values: BatchDeleteUserDevice, BatchDisableDevice, BatchEnableDevice.
BatchUpgradeDevice,
BatchResetDevice,
BatchRebootDevice,
BatchRefreshDeviceChannel
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Status(self):
        r"""By default, filtering is not based on this field. Otherwise, filter by task status. Status code: 1 - Pending, 2 - Executing, 3 - Completed, 4 - Cancelled.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BeginTime(self):
        r"""Start time.
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        r"""End time.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Operation = params.get("Operation")
        self._Status = params.get("Status")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTasksResponse(AbstractModel):
    r"""ListTasks response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListTasksData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListTasksData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListTasksData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListVLPlansRequest(AbstractModel):
    r"""ListVLPlans request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Plan name, exact match</p>
        :type Name: str
        :param _PageNumber: <p>Page number. Default value: 1.</p>
        :type PageNumber: int
        :param _PageSize: <p>Number of items per page. Default: 20. Maximum: 200.</p>
        :type PageSize: int
        """
        self._Name = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Name(self):
        r"""<p>Plan name, exact match</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PageNumber(self):
        r"""<p>Page number. Default value: 1.</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>Number of items per page. Default: 20. Maximum: 200.</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVLPlansResponse(AbstractModel):
    r"""ListVLPlans response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Plan list</p>
        :type Data: list of VLPlanInfo
        :param _TotalCount: <p>Total quantity.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Plan list</p>
        :rtype: list of VLPlanInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""<p>Total quantity.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VLPlanInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListVLTemplatesRequest(AbstractModel):
    r"""ListVLTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Template name, exact match</p>
        :type Name: str
        :param _AnalysisMode: <p>Analysis mode filter, image / video</p>
        :type AnalysisMode: str
        :param _CaptureType: <p>Screenshot type filter (this parameter is valid only when AnalysisMode=image): realtime/low</p>
        :type CaptureType: str
        :param _PageNumber: <p>Page number, which is 1 by default.</p>
        :type PageNumber: int
        :param _PageSize: <p>Number of items per page. Default value: 20. Maximum value: 200.</p>
        :type PageSize: int
        """
        self._Name = None
        self._AnalysisMode = None
        self._CaptureType = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Name(self):
        r"""<p>Template name, exact match</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AnalysisMode(self):
        r"""<p>Analysis mode filter, image / video</p>
        :rtype: str
        """
        return self._AnalysisMode

    @AnalysisMode.setter
    def AnalysisMode(self, AnalysisMode):
        self._AnalysisMode = AnalysisMode

    @property
    def CaptureType(self):
        r"""<p>Screenshot type filter (this parameter is valid only when AnalysisMode=image): realtime/low</p>
        :rtype: str
        """
        return self._CaptureType

    @CaptureType.setter
    def CaptureType(self, CaptureType):
        self._CaptureType = CaptureType

    @property
    def PageNumber(self):
        r"""<p>Page number, which is 1 by default.</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>Number of items per page. Default value: 20. Maximum value: 200.</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AnalysisMode = params.get("AnalysisMode")
        self._CaptureType = params.get("CaptureType")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVLTemplatesResponse(AbstractModel):
    r"""ListVLTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Template list</p>
        :type Data: list of VLTemplateInfo
        :param _TotalCount: <p>Total quantity.</p>
        :type TotalCount: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Template list</p>
        :rtype: list of VLTemplateInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        r"""<p>Total quantity.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = VLTemplateInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListVideoDownloadTaskData(AbstractModel):
    r"""Local recording download task list

    """

    def __init__(self):
        r"""
        :param _List: Task list
        :type List: list of VideoDownloadTask
        :param _TotalCount: Total number of tasks
        :type TotalCount: int
        """
        self._List = None
        self._TotalCount = None

    @property
    def List(self):
        r"""Task list
        :rtype: list of VideoDownloadTask
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        r"""Total number of tasks
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = VideoDownloadTask()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVideoDownloadTaskRequest(AbstractModel):
    r"""ListVideoDownloadTask request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceName: Device name. Fuzzy search supported.
        :type DeviceName: str
        :param _ChannelName: Channel name, used for fuzzy search
        :type ChannelName: str
        :param _Status: Task status (0: preparing, 1: executing, 2: completed, 3: failure)
        :type Status: int
        :param _SortRule: Sorting rule (only StartTime is supported. A hyphen (-) indicates descending order, e.g., -StartTime)
        :type SortRule: str
        :param _WithPreviewUrl: Whether the response carries the preview address (0: without; 1: carry)
        :type WithPreviewUrl: int
        :param _PageNumber: Page number
        :type PageNumber: int
        :param _PageSize: Pagination size.
        :type PageSize: int
        :param _DownloadTaskId: Download task ID
        :type DownloadTaskId: str
        :param _UrlExpires: URL expiration time (in seconds), with a maximum value of 86400 seconds (1 day).
        :type UrlExpires: int
        :param _Date: Task date. Defaults to the current day.
        :type Date: str
        """
        self._DeviceName = None
        self._ChannelName = None
        self._Status = None
        self._SortRule = None
        self._WithPreviewUrl = None
        self._PageNumber = None
        self._PageSize = None
        self._DownloadTaskId = None
        self._UrlExpires = None
        self._Date = None

    @property
    def DeviceName(self):
        r"""Device name. Fuzzy search supported.
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelName(self):
        r"""Channel name, used for fuzzy search
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Status(self):
        r"""Task status (0: preparing, 1: executing, 2: completed, 3: failure)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SortRule(self):
        r"""Sorting rule (only StartTime is supported. A hyphen (-) indicates descending order, e.g., -StartTime)
        :rtype: str
        """
        return self._SortRule

    @SortRule.setter
    def SortRule(self, SortRule):
        self._SortRule = SortRule

    @property
    def WithPreviewUrl(self):
        r"""Whether the response carries the preview address (0: without; 1: carry)
        :rtype: int
        """
        return self._WithPreviewUrl

    @WithPreviewUrl.setter
    def WithPreviewUrl(self, WithPreviewUrl):
        self._WithPreviewUrl = WithPreviewUrl

    @property
    def PageNumber(self):
        r"""Page number
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""Pagination size.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def DownloadTaskId(self):
        r"""Download task ID
        :rtype: str
        """
        return self._DownloadTaskId

    @DownloadTaskId.setter
    def DownloadTaskId(self, DownloadTaskId):
        self._DownloadTaskId = DownloadTaskId

    @property
    def UrlExpires(self):
        r"""URL expiration time (in seconds), with a maximum value of 86400 seconds (1 day).
        :rtype: int
        """
        return self._UrlExpires

    @UrlExpires.setter
    def UrlExpires(self, UrlExpires):
        self._UrlExpires = UrlExpires

    @property
    def Date(self):
        r"""Task date. Defaults to the current day.
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._DeviceName = params.get("DeviceName")
        self._ChannelName = params.get("ChannelName")
        self._Status = params.get("Status")
        self._SortRule = params.get("SortRule")
        self._WithPreviewUrl = params.get("WithPreviewUrl")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._DownloadTaskId = params.get("DownloadTaskId")
        self._UrlExpires = params.get("UrlExpires")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVideoDownloadTaskResponse(AbstractModel):
    r"""ListVideoDownloadTask response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Local recording download task list
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListVideoDownloadTaskData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Local recording download task list
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListVideoDownloadTaskData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListVideoDownloadTaskData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ListVideoSnapshotTemplateData(AbstractModel):
    r"""Query the screenshot template detail list

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>Total.</p>
        :type TotalCount: int
        :param _Sort: <p>Sorting parameter</p>
        :type Sort: str
        :param _Order: <p>Sort order</p>
        :type Order: str
        :param _PageNumber: <p>Page number.</p>
        :type PageNumber: int
        :param _PageSize: <p>Number of items per page.</p>
        :type PageSize: int
        :param _List: <p>Screenshot template list</p>
        :type List: list of VideoSnapshotTemplateInfo
        """
        self._TotalCount = None
        self._Sort = None
        self._Order = None
        self._PageNumber = None
        self._PageSize = None
        self._List = None

    @property
    def TotalCount(self):
        r"""<p>Total.</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Sort(self):
        r"""<p>Sorting parameter</p>
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Order(self):
        r"""<p>Sort order</p>
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def PageNumber(self):
        r"""<p>Page number.</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>Number of items per page.</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def List(self):
        r"""<p>Screenshot template list</p>
        :rtype: list of VideoSnapshotTemplateInfo
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Sort = params.get("Sort")
        self._Order = params.get("Order")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = VideoSnapshotTemplateInfo()
                obj._deserialize(item)
                self._List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVideoSnapshotTemplateRequest(AbstractModel):
    r"""ListVideoSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Template name</p>
        :type Name: str
        :param _Type: <p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :type Type: int
        :param _Sort: <p>Sorting parameter</p><p>Default value: update_time</p>
        :type Sort: str
        :param _Order: <p>Sort order</p><p>Enumeration values:</p><ul><li>desc: in descending order</li><li>asc: in ascending order</li></ul><p>Default value: desc</p>
        :type Order: str
        :param _PageNumber: <p>Page number</p><p>Default value: 1</p>
        :type PageNumber: int
        :param _PageSize: <p>Number of items per page</p><p>Default value: 20</p>
        :type PageSize: int
        """
        self._Name = None
        self._Type = None
        self._Sort = None
        self._Order = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def Name(self):
        r"""<p>Template name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Sort(self):
        r"""<p>Sorting parameter</p><p>Default value: update_time</p>
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Order(self):
        r"""<p>Sort order</p><p>Enumeration values:</p><ul><li>desc: in descending order</li><li>asc: in ascending order</li></ul><p>Default value: desc</p>
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def PageNumber(self):
        r"""<p>Page number</p><p>Default value: 1</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>Number of items per page</p><p>Default value: 20</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Sort = params.get("Sort")
        self._Order = params.get("Order")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListVideoSnapshotTemplateResponse(AbstractModel):
    r"""ListVideoSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Screenshot template result list</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListVideoSnapshotTemplateData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Screenshot template result list</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListVideoSnapshotTemplateData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListVideoSnapshotTemplateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyVLPlanRequest(AbstractModel):
    r"""ModifyVLPlan request structure.

    """

    def __init__(self):
        r"""
        :param _VLPlanId: <p>Plan ID</p>
        :type VLPlanId: str
        :param _Name: <p>New plan name</p>
        :type Name: str
        :param _Describe: <p>New plan description.</p>
        :type Describe: str
        :param _VLTemplateId: <p>ID of the newly associated visual understanding template</p>
        :type VLTemplateId: str
        :param _FileExpires: <p>New storage days, range [7, 1080]. 0 means no modification</p>
        :type FileExpires: int
        :param _Callback: <p>New callback configuration</p>
        :type Callback: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        self._VLPlanId = None
        self._Name = None
        self._Describe = None
        self._VLTemplateId = None
        self._FileExpires = None
        self._Callback = None

    @property
    def VLPlanId(self):
        r"""<p>Plan ID</p>
        :rtype: str
        """
        return self._VLPlanId

    @VLPlanId.setter
    def VLPlanId(self, VLPlanId):
        self._VLPlanId = VLPlanId

    @property
    def Name(self):
        r"""<p>New plan name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Describe(self):
        r"""<p>New plan description.</p>
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def VLTemplateId(self):
        r"""<p>ID of the newly associated visual understanding template</p>
        :rtype: str
        """
        return self._VLTemplateId

    @VLTemplateId.setter
    def VLTemplateId(self, VLTemplateId):
        self._VLTemplateId = VLTemplateId

    @property
    def FileExpires(self):
        r"""<p>New storage days, range [7, 1080]. 0 means no modification</p>
        :rtype: int
        """
        return self._FileExpires

    @FileExpires.setter
    def FileExpires(self, FileExpires):
        self._FileExpires = FileExpires

    @property
    def Callback(self):
        r"""<p>New callback configuration</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._VLPlanId = params.get("VLPlanId")
        self._Name = params.get("Name")
        self._Describe = params.get("Describe")
        self._VLTemplateId = params.get("VLTemplateId")
        self._FileExpires = params.get("FileExpires")
        if params.get("Callback") is not None:
            self._Callback = CallbackURL()
            self._Callback._deserialize(params.get("Callback"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVLPlanResponse(AbstractModel):
    r"""ModifyVLPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Visual understanding plan information</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VLPlanInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Visual understanding plan information</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VLPlanInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VLPlanInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyVideoSnapshotConfigRequest(AbstractModel):
    r"""ModifyVideoSnapshotConfig request structure.

    """

    def __init__(self):
        r"""
        :param _ConfigId: <p>Screenshot configuration Id</p>
        :type ConfigId: str
        :param _Name: <p>Screenshot configuration name</p><p>Input parameter limits: Chinese, English, digits, "-", "_", length not exceeding 128 characters</p>
        :type Name: str
        :param _TemplateId: <p>Screenshot template Id</p>
        :type TemplateId: str
        :param _FileExpires: <p>Hot storage days of image files</p><p>Enumeration values:</p><ul><li>7: 7 days</li><li>15: 15 days</li><li>30: 30 days</li><li>60: 60 days</li><li>90: 90 days</li><li>180: 180 days</li><li>270: 270 days</li><li>360: 360 days</li><li>540: 540 days</li><li>720: 720 days</li><li>900: 900 days</li><li>1080: 1080 days</li></ul>
        :type FileExpires: int
        :param _Callback: <p>Callback configuration</p>
        :type Callback: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        self._ConfigId = None
        self._Name = None
        self._TemplateId = None
        self._FileExpires = None
        self._Callback = None

    @property
    def ConfigId(self):
        r"""<p>Screenshot configuration Id</p>
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Name(self):
        r"""<p>Screenshot configuration name</p><p>Input parameter limits: Chinese, English, digits, "-", "_", length not exceeding 128 characters</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TemplateId(self):
        r"""<p>Screenshot template Id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def FileExpires(self):
        r"""<p>Hot storage days of image files</p><p>Enumeration values:</p><ul><li>7: 7 days</li><li>15: 15 days</li><li>30: 30 days</li><li>60: 60 days</li><li>90: 90 days</li><li>180: 180 days</li><li>270: 270 days</li><li>360: 360 days</li><li>540: 540 days</li><li>720: 720 days</li><li>900: 900 days</li><li>1080: 1080 days</li></ul>
        :rtype: int
        """
        return self._FileExpires

    @FileExpires.setter
    def FileExpires(self, FileExpires):
        self._FileExpires = FileExpires

    @property
    def Callback(self):
        r"""<p>Callback configuration</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._Name = params.get("Name")
        self._TemplateId = params.get("TemplateId")
        self._FileExpires = params.get("FileExpires")
        if params.get("Callback") is not None:
            self._Callback = CallbackURL()
            self._Callback._deserialize(params.get("Callback"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVideoSnapshotConfigResponse(AbstractModel):
    r"""ModifyVideoSnapshotConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Screenshot configuration message</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotConfigInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Screenshot configuration message</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VideoSnapshotConfigInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = VideoSnapshotConfigInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class MultiSnapshotMode(AbstractModel):
    r"""Multiple screenshots mode

    """

    def __init__(self):
        r"""
        :param _Enable: <p>Whether to enable multiple image mode</p><p>When set to false, single image mode is used, and the Interval and Total parameters are ignored</p><p>Default value: false</p>
        :type Enable: bool
        :param _Interval: <p>Frame interception interval</p><p>Value range: [10, 600]</p><p>Unit: second</p>
        :type Interval: int
        :param _Total: <p>Number of captured frames</p><p>Value range: [1, 10]</p>
        :type Total: int
        """
        self._Enable = None
        self._Interval = None
        self._Total = None

    @property
    def Enable(self):
        r"""<p>Whether to enable multiple image mode</p><p>When set to false, single image mode is used, and the Interval and Total parameters are ignored</p><p>Default value: false</p>
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Interval(self):
        r"""<p>Frame interception interval</p><p>Value range: [10, 600]</p><p>Unit: second</p>
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Total(self):
        r"""<p>Number of captured frames</p><p>Value range: [1, 10]</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Interval = params.get("Interval")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiVideoSnapshotMode(AbstractModel):
    r"""Parameter of the multiple mode

    """

    def __init__(self):
        r"""
        :param _Enable: <p>Whether to enable multiple mode. When set to false, single image mode is used, and the Interval and Total parameters are ignored.</p><p>Default value: false</p>
        :type Enable: bool
        :param _Interval: <p>Frame interception interval</p><p>Value range: [10, 600]</p><p>Unit: seconds</p>
        :type Interval: int
        :param _Total: <p>Number of captured frames</p><p>Value range: [1, 10]</p>
        :type Total: int
        """
        self._Enable = None
        self._Interval = None
        self._Total = None

    @property
    def Enable(self):
        r"""<p>Whether to enable multiple mode. When set to false, single image mode is used, and the Interval and Total parameters are ignored.</p><p>Default value: false</p>
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Interval(self):
        r"""<p>Frame interception interval</p><p>Value range: [10, 600]</p><p>Unit: seconds</p>
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Total(self):
        r"""<p>Number of captured frames</p><p>Value range: [1, 10]</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Interval = params.get("Interval")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationChannelInfo(AbstractModel):
    r"""Channel information under the organization directory

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID of the device channel
        :type DeviceId: str
        :param _DeviceName: Device name of the device channel
        :type DeviceName: str
        :param _ChannelId: Device channel ID
        :type ChannelId: str
        :param _ChannelName: Device channel name.
        :type ChannelName: str
        :param _InPlan: Whether the channel is in a cloud migration plan. If so, it cannot be added to another cloud migration plan | true: in a cloud migration plan, false: not in a cloud migration plan
        :type InPlan: bool
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None
        self._InPlan = None

    @property
    def DeviceId(self):
        r"""Device ID of the device channel
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""Device name of the device channel
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        r"""Device channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""Device channel name.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def InPlan(self):
        r"""Whether the channel is in a cloud migration plan. If so, it cannot be added to another cloud migration plan | true: in a cloud migration plan, false: not in a cloud migration plan
        :rtype: bool
        """
        return self._InPlan

    @InPlan.setter
    def InPlan(self, InPlan):
        self._InPlan = InPlan


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._InPlan = params.get("InPlan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayRecordData(AbstractModel):
    r"""Local recording playback url data structure

    """

    def __init__(self):
        r"""
        :param _Flv: Video playback address
        :type Flv: str
        """
        self._Flv = None

    @property
    def Flv(self):
        r"""Video playback address
        :rtype: str
        """
        return self._Flv

    @Flv.setter
    def Flv(self, Flv):
        self._Flv = Flv


    def _deserialize(self, params):
        self._Flv = params.get("Flv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayRecordRequest(AbstractModel):
    r"""PlayRecord request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID (obtain from the DescribeDeviceChannel API)
        :type ChannelId: str
        :param _Start: Start time.
        :type Start: int
        :param _End:  End time.
        :type End: int
        :param _StreamType: Stream type (1: main stream; 2: sub-stream (not allowed to be delivered at the same time as Resolution))
        :type StreamType: int
        :param _Resolution: Resolution (1: QCIF; 2: CIF; 3: 4CIF; 4: D1; 5: 720P; 6: 1080P/I; custom 19201080, etc. (device support required) (not allowed to be delivered at the same time as StreamType))
        :type Resolution: str
        :param _IsInternal: Whether it is a private network
        :type IsInternal: bool
        """
        self._ChannelId = None
        self._Start = None
        self._End = None
        self._StreamType = None
        self._Resolution = None
        self._IsInternal = None

    @property
    def ChannelId(self):
        r"""Channel ID (obtain from the DescribeDeviceChannel API)
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Start(self):
        r"""Start time.
        :rtype: int
        """
        return self._Start

    @Start.setter
    def Start(self, Start):
        self._Start = Start

    @property
    def End(self):
        r""" End time.
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def StreamType(self):
        r"""Stream type (1: main stream; 2: sub-stream (not allowed to be delivered at the same time as Resolution))
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def Resolution(self):
        r"""Resolution (1: QCIF; 2: CIF; 3: 4CIF; 4: D1; 5: 720P; 6: 1080P/I; custom 19201080, etc. (device support required) (not allowed to be delivered at the same time as StreamType))
        :rtype: str
        """
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def IsInternal(self):
        r"""Whether it is a private network
        :rtype: bool
        """
        return self._IsInternal

    @IsInternal.setter
    def IsInternal(self, IsInternal):
        self._IsInternal = IsInternal


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Start = params.get("Start")
        self._End = params.get("End")
        self._StreamType = params.get("StreamType")
        self._Resolution = params.get("Resolution")
        self._IsInternal = params.get("IsInternal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayRecordResponse(AbstractModel):
    r"""PlayRecord response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.PlayRecordData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.PlayRecordData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = PlayRecordData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class QueryForbidPlayChannelListRequest(AbstractModel):
    r"""QueryForbidPlayChannelList request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Sub-user uin, which can also be the root user uin.
        :type UserId: str
        :param _PageSize: Maximum number of items per page. Maximum value: 200. If the number of items exceeds 200, 200 items are returned.
        :type PageSize: int
        :param _PageNumber: Which page.
        :type PageNumber: int
        """
        self._UserId = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def UserId(self):
        r"""Sub-user uin, which can also be the root user uin.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PageSize(self):
        r"""Maximum number of items per page. Maximum value: 200. If the number of items exceeds 200, 200 items are returned.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""Which page.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryForbidPlayChannelListResponse(AbstractModel):
    r"""QueryForbidPlayChannelList response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.ListForbidplayChannelsData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.ListForbidplayChannelsData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = ListForbidplayChannelsData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class RecordPlanBaseInfo(AbstractModel):
    r"""Basic information of the real-time cloud migration plan

    """

    def __init__(self):
        r"""
        :param _PlanId: Cloud migration plan ID
        :type PlanId: str
        :param _PlanName: Cloud migration plan name
        :type PlanName: str
        :param _TemplateId: Cloud template ID
        :type TemplateId: str
        :param _Describe: Cloud migration plan description
        :type Describe: str
        :param _StreamType: Stream type. default: default stream type of the device. main: main stream. sub: substream. Other stream types can be customized based on the device capacity.
        :type StreamType: str
        :param _LifeCycle: Cloud file lifecycle
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: Recording schedule status. 1: In normal use. 0: Deleting, cannot be used.
        :type Status: int
        :param _ChannelCount: Total number of channels
        :type ChannelCount: int
        :param _RepairMode: Video recording supplement mode (0: not enabled, 1: enabled)
        :type RepairMode: int
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._StreamType = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._RepairMode = None

    @property
    def PlanId(self):
        r"""Cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""Cloud migration plan name
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Cloud template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Cloud migration plan description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def StreamType(self):
        r"""Stream type. default: default stream type of the device. main: main stream. sub: substream. Other stream types can be customized based on the device capacity.
        :rtype: str
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def LifeCycle(self):
        r"""Cloud file lifecycle
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        r"""Recording schedule status. 1: In normal use. 0: Deleting, cannot be used.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        r"""Total number of channels
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def RepairMode(self):
        r"""Video recording supplement mode (0: not enabled, 1: enabled)
        :rtype: int
        """
        return self._RepairMode

    @RepairMode.setter
    def RepairMode(self, RepairMode):
        self._RepairMode = RepairMode


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        self._StreamType = params.get("StreamType")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._RepairMode = params.get("RepairMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanChannelInfo(AbstractModel):
    r"""Channel information of the device under the plan

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID to which the device channel belongs
        :type DeviceId: str
        :param _DeviceName: Device name of the device channel
        :type DeviceName: str
        :param _ChannelId: Device channel ID
        :type ChannelId: str
        :param _ChannelName: Device channel name
        :type ChannelName: str
        :param _OrganizationName: Affiliated organization name
        :type OrganizationName: str
        :param _AccessProtocol: Access protocol type of the device to which the channel belongs
        :type AccessProtocol: int
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None
        self._OrganizationName = None
        self._AccessProtocol = None

    @property
    def DeviceId(self):
        r"""Device ID to which the device channel belongs
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""Device name of the device channel
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        r"""Device channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""Device channel name
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def OrganizationName(self):
        r"""Affiliated organization name
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def AccessProtocol(self):
        r"""Access protocol type of the device to which the channel belongs
        :rtype: int
        """
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._OrganizationName = params.get("OrganizationName")
        self._AccessProtocol = params.get("AccessProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlanOptData(AbstractModel):
    r"""data for adding and modifying a real-time cloud migration plan

    """

    def __init__(self):
        r"""
        :param _PlanId: Cloud migration plan ID
        :type PlanId: str
        :param _PlanName: Cloud migration plan name
        :type PlanName: str
        :param _TemplateId: Cloud template ID
        :type TemplateId: str
        :param _Describe: Cloud migration plan description
        :type Describe: str
        :param _LifeCycle: Cloud file lifecycle
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _StreamType: Stream type. default: The default stream type of the device. main: Main stream. sub: Substream. Other values are customized based on the device capacity.
        :type StreamType: str
        :param _RepairMode: Video recording supplement mode (0: disabled, 1: enabled)
        :type RepairMode: int
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._StreamType = None
        self._RepairMode = None

    @property
    def PlanId(self):
        r"""Cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""Cloud migration plan name
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Cloud template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Cloud migration plan description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        r"""Cloud file lifecycle
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def StreamType(self):
        r"""Stream type. default: The default stream type of the device. main: Main stream. sub: Substream. Other values are customized based on the device capacity.
        :rtype: str
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def RepairMode(self):
        r"""Video recording supplement mode (0: disabled, 1: enabled)
        :rtype: int
        """
        return self._RepairMode

    @RepairMode.setter
    def RepairMode(self, RepairMode):
        self._RepairMode = RepairMode


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._StreamType = params.get("StreamType")
        self._RepairMode = params.get("RepairMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordPlaybackUrl(AbstractModel):
    r"""Cloud video playback url

    """

    def __init__(self):
        r"""
        :param _Hls: hls replay url
        :type Hls: str
        """
        self._Hls = None

    @property
    def Hls(self):
        r"""hls replay url
        :rtype: str
        """
        return self._Hls

    @Hls.setter
    def Hls(self, Hls):
        self._Hls = Hls


    def _deserialize(self, params):
        self._Hls = params.get("Hls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordRetrieveTaskChannelInfo(AbstractModel):
    r"""Retrieve the task channel information

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID to which the device channel belongs
        :type DeviceId: str
        :param _DeviceName: Device name of the device channel
        :type DeviceName: str
        :param _ChannelId: Device channel ID
        :type ChannelId: str
        :param _ChannelName: Device channel name
        :type ChannelName: str
        :param _Status: Task status. 0: Retrieved, 1: Retrieving, 2: Pending retrieval, 3: No archived video recording
        :type Status: int
        """
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None
        self._Status = None

    @property
    def DeviceId(self):
        r"""Device ID to which the device channel belongs
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""Device name of the device channel
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        r"""Device channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""Device channel name
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def Status(self):
        r"""Task status. 0: Retrieved, 1: Retrieving, 2: Pending retrieval, 3: No archived video recording
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordRetrieveTaskDetailsInfo(AbstractModel):
    r"""Basic information of the recording retrieval task

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _TaskName: Task name.
        :type TaskName: str
        :param _StartTime: Start time of video recording retrieval
        :type StartTime: int
        :param _EndTime: Retrieval end time of the video recording
        :type EndTime: int
        :param _Mode: Retrieval mode. 1: ultrafast mode. Others not supported currently.
        :type Mode: int
        :param _Expiration: Replica validity period
        :type Expiration: int
        :param _Status: Task status. 0: Retrieved, 1: Retrieving, 2: Pending retrieval
        :type Status: int
        :param _Capacity: Retrieval capacity, in MB.
        :type Capacity: int
        :param _Describe: Task description
        :type Describe: str
        :param _ChannelCount: Number of task channels
        :type ChannelCount: int
        """
        self._TaskId = None
        self._TaskName = None
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Expiration = None
        self._Status = None
        self._Capacity = None
        self._Describe = None
        self._ChannelCount = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskName(self):
        r"""Task name.
        :rtype: str
        """
        return self._TaskName

    @TaskName.setter
    def TaskName(self, TaskName):
        self._TaskName = TaskName

    @property
    def StartTime(self):
        r"""Start time of video recording retrieval
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Retrieval end time of the video recording
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        r"""Retrieval mode. 1: ultrafast mode. Others not supported currently.
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Expiration(self):
        r"""Replica validity period
        :rtype: int
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration

    @property
    def Status(self):
        r"""Task status. 0: Retrieved, 1: Retrieving, 2: Pending retrieval
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Capacity(self):
        r"""Retrieval capacity, in MB.
        :rtype: int
        """
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity

    @property
    def Describe(self):
        r"""Task description
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def ChannelCount(self):
        r"""Number of task channels
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TaskName = params.get("TaskName")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Expiration = params.get("Expiration")
        self._Status = params.get("Status")
        self._Capacity = params.get("Capacity")
        self._Describe = params.get("Describe")
        self._ChannelCount = params.get("ChannelCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTemplateInfo(AbstractModel):
    r"""Real-time cloud template information data

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID.
        :type TemplateId: str
        :param _TemplateName: Template name
        :type TemplateName: str
        :param _TimeSections: Cloud upload time period. Settings can be done by week. Multiple time periods can be set for each day, with each time period greater than or equal to 10 minutes.
        :type TimeSections: list of RecordTemplateTimeSections
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None

    @property
    def TemplateId(self):
        r"""Template ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""Template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""Cloud upload time period. Settings can be done by week. Multiple time periods can be set for each day, with each time period greater than or equal to 10 minutes.
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTemplateTimeSections(AbstractModel):
    r"""Data format of the time segment in the cloud template

    """

    def __init__(self):
        r"""
        :param _DayOfWeek: Day of the week. Value range: 1–7 (corresponding to Monday–Sunday)
        :type DayOfWeek: int
        :param _StartTime: Start time. Format: HH:MM:SS. Range: [00:00:00–23:59:59]
        :type StartTime: str
        :param _EndTime: End time. Format: HH:MM:SS. Range: [00:00:00–23:59:59]
        :type EndTime: str
        """
        self._DayOfWeek = None
        self._StartTime = None
        self._EndTime = None

    @property
    def DayOfWeek(self):
        r"""Day of the week. Value range: 1–7 (corresponding to Monday–Sunday)
        :rtype: int
        """
        return self._DayOfWeek

    @DayOfWeek.setter
    def DayOfWeek(self, DayOfWeek):
        self._DayOfWeek = DayOfWeek

    @property
    def StartTime(self):
        r"""Start time. Format: HH:MM:SS. Range: [00:00:00–23:59:59]
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time. Format: HH:MM:SS. Range: [00:00:00–23:59:59]
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._DayOfWeek = params.get("DayOfWeek")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTimeLine(AbstractModel):
    r"""Cloud Recording time segment

    """

    def __init__(self):
        r"""
        :param _Begin: Segment start time in UTC seconds, for example: 1662114146
        :type Begin: int
        :param _End: Segment end time in UTC seconds, for example: 1662114146
        :type End: int
        :param _HlsUrl: Playback url of the corresponding recording clip
        :type HlsUrl: str
        """
        self._Begin = None
        self._End = None
        self._HlsUrl = None

    @property
    def Begin(self):
        r"""Segment start time in UTC seconds, for example: 1662114146
        :rtype: int
        """
        return self._Begin

    @Begin.setter
    def Begin(self, Begin):
        self._Begin = Begin

    @property
    def End(self):
        r"""Segment end time in UTC seconds, for example: 1662114146
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End

    @property
    def HlsUrl(self):
        r"""Playback url of the corresponding recording clip
        :rtype: str
        """
        return self._HlsUrl

    @HlsUrl.setter
    def HlsUrl(self, HlsUrl):
        self._HlsUrl = HlsUrl


    def _deserialize(self, params):
        self._Begin = params.get("Begin")
        self._End = params.get("End")
        self._HlsUrl = params.get("HlsUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshDeviceChannelRequest(AbstractModel):
    r"""RefreshDeviceChannel request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID (obtain from the ListDevices API for getting device list)
        :type DeviceId: str
        """
        self._DeviceId = None

    @property
    def DeviceId(self):
        r"""Device ID (obtain from the ListDevices API for getting device list)
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefreshDeviceChannelResponse(AbstractModel):
    r"""RefreshDeviceChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RemoteAddrInfo(AbstractModel):
    r"""Device address return result

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device Id
        :type DeviceId: str
        :param _Addr: IP address
        :type Addr: str
        """
        self._DeviceId = None
        self._Addr = None

    @property
    def DeviceId(self):
        r"""Device Id
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Addr(self):
        r"""IP address
        :rtype: str
        """
        return self._Addr

    @Addr.setter
    def Addr(self, Addr):
        self._Addr = Addr


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Addr = params.get("Addr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetForbidPlayChannelsRequest(AbstractModel):
    r"""SetForbidPlayChannels request structure.

    """

    def __init__(self):
        r"""
        :param _Channels: Channel parameters to be disabled. Up to 200 channels can be set at a time.
        :type Channels: list of SetForbidplayChannelParam
        :param _UserId: User uin, which can be the uin of a sub-user or a root user
        :type UserId: str
        """
        self._Channels = None
        self._UserId = None

    @property
    def Channels(self):
        r"""Channel parameters to be disabled. Up to 200 channels can be set at a time.
        :rtype: list of SetForbidplayChannelParam
        """
        return self._Channels

    @Channels.setter
    def Channels(self, Channels):
        self._Channels = Channels

    @property
    def UserId(self):
        r"""User uin, which can be the uin of a sub-user or a root user
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        if params.get("Channels") is not None:
            self._Channels = []
            for item in params.get("Channels"):
                obj = SetForbidplayChannelParam()
                obj._deserialize(item)
                self._Channels.append(obj)
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetForbidPlayChannelsResponse(AbstractModel):
    r"""SetForbidPlayChannels response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class SetForbidplayChannelParam(AbstractModel):
    r"""Set the channel to forbid stream publishing. It has the Channel Id and enable fields.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel Id
        :type ChannelId: str
        :param _Enable: Whether to forbid stream pushing over the channel
        :type Enable: bool
        """
        self._ChannelId = None
        self._Enable = None

    @property
    def ChannelId(self):
        r"""Channel Id
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Enable(self):
        r"""Whether to forbid stream pushing over the channel
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubTaskData(AbstractModel):
    r"""Subtask details

    """

    def __init__(self):
        r"""
        :param _SubTaskId: Subtask ID
        :type SubTaskId: str
        :param _Status: Task status. 1: NEW, 2: RUNNING, 3: COMPLETED, 4: FAILED
        :type Status: int
        :param _FailReason: Cause of the task failure.
        :type FailReason: str
        :param _Progress: Task progress
        :type Progress: float
        :param _Action: Operation type.
        :type Action: str
        :param _ActionZhDesc: Operation type Chinese description
        :type ActionZhDesc: str
        :param _ResourceId: Resource ID
        :type ResourceId: str
        :param _StartedAt: Task start time
        :type StartedAt: str
        :param _CreatedAt: Task creation time
        :type CreatedAt: str
        :param _UpdatedAt: Task update time
        :type UpdatedAt: str
        :param _Runtime: Task running time in milliseconds
        :type Runtime: int
        :param _DeviceId: Device ID
        :type DeviceId: str
        :param _DeviceName: Device name.
        :type DeviceName: str
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _ChannelName: Channel name
        :type ChannelName: str
        """
        self._SubTaskId = None
        self._Status = None
        self._FailReason = None
        self._Progress = None
        self._Action = None
        self._ActionZhDesc = None
        self._ResourceId = None
        self._StartedAt = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Runtime = None
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None

    @property
    def SubTaskId(self):
        r"""Subtask ID
        :rtype: str
        """
        return self._SubTaskId

    @SubTaskId.setter
    def SubTaskId(self, SubTaskId):
        self._SubTaskId = SubTaskId

    @property
    def Status(self):
        r"""Task status. 1: NEW, 2: RUNNING, 3: COMPLETED, 4: FAILED
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailReason(self):
        r"""Cause of the task failure.
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Progress(self):
        r"""Task progress
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Action(self):
        r"""Operation type.
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionZhDesc(self):
        r"""Operation type Chinese description
        :rtype: str
        """
        return self._ActionZhDesc

    @ActionZhDesc.setter
    def ActionZhDesc(self, ActionZhDesc):
        self._ActionZhDesc = ActionZhDesc

    @property
    def ResourceId(self):
        r"""Resource ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def StartedAt(self):
        r"""Task start time
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def CreatedAt(self):
        r"""Task creation time
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""Task update time
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Runtime(self):
        r"""Task running time in milliseconds
        :rtype: int
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def DeviceId(self):
        r"""Device ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""Device name.
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""Channel name
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._SubTaskId = params.get("SubTaskId")
        self._Status = params.get("Status")
        self._FailReason = params.get("FailReason")
        self._Progress = params.get("Progress")
        self._Action = params.get("Action")
        self._ActionZhDesc = params.get("ActionZhDesc")
        self._ResourceId = params.get("ResourceId")
        self._StartedAt = params.get("StartedAt")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Runtime = params.get("Runtime")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskData(AbstractModel):
    r"""Returned results of querying complex task details

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID.
        :type TaskId: str
        :param _Status: Task status. 1: NEW, 2: RUNNING, 3: COMPLETED, 4: FAILED
        :type Status: int
        :param _FailReason: Reason for failure
        :type FailReason: str
        :param _Progress: Progress (0-1)
        :type Progress: float
        :param _Action: Task operation type. A batch task type starts with "Batch".
        :type Action: str
        :param _ActionZhDesc: Operation type Chinese description
        :type ActionZhDesc: str
        :param _TaskType: Task type. 1. Simple 2. Complex 3. Subtask
        :type TaskType: int
        :param _ResourceId: Task resource ID (invalid for complex tasks)
        :type ResourceId: str
        :param _Total: Total number of tasks (valid only for complex tasks)
        :type Total: int
        :param _SuccessCount: Successful Tasks (valid only for complex tasks)
        :type SuccessCount: int
        :param _FailCount: Number of failed tasks (valid only for complex tasks)
        :type FailCount: int
        :param _RunningCount: Number of running tasks (valid only for complex tasks)
        :type RunningCount: int
        :param _StartedAt: Task start time.
        :type StartedAt: str
        :param _CreatedAt: Task creation time
        :type CreatedAt: str
        :param _UpdatedAt: Update task time.
        :type UpdatedAt: str
        :param _Runtime: Task running time in milliseconds.
        :type Runtime: int
        :param _DeviceId: Device ID
        :type DeviceId: str
        :param _DeviceName: Device name.
        :type DeviceName: str
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _ChannelName: Channel name
        :type ChannelName: str
        """
        self._TaskId = None
        self._Status = None
        self._FailReason = None
        self._Progress = None
        self._Action = None
        self._ActionZhDesc = None
        self._TaskType = None
        self._ResourceId = None
        self._Total = None
        self._SuccessCount = None
        self._FailCount = None
        self._RunningCount = None
        self._StartedAt = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Runtime = None
        self._DeviceId = None
        self._DeviceName = None
        self._ChannelId = None
        self._ChannelName = None

    @property
    def TaskId(self):
        r"""Task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        r"""Task status. 1: NEW, 2: RUNNING, 3: COMPLETED, 4: FAILED
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailReason(self):
        r"""Reason for failure
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def Progress(self):
        r"""Progress (0-1)
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Action(self):
        r"""Task operation type. A batch task type starts with "Batch".
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionZhDesc(self):
        r"""Operation type Chinese description
        :rtype: str
        """
        return self._ActionZhDesc

    @ActionZhDesc.setter
    def ActionZhDesc(self, ActionZhDesc):
        self._ActionZhDesc = ActionZhDesc

    @property
    def TaskType(self):
        r"""Task type. 1. Simple 2. Complex 3. Subtask
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ResourceId(self):
        r"""Task resource ID (invalid for complex tasks)
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Total(self):
        r"""Total number of tasks (valid only for complex tasks)
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def SuccessCount(self):
        r"""Successful Tasks (valid only for complex tasks)
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def FailCount(self):
        r"""Number of failed tasks (valid only for complex tasks)
        :rtype: int
        """
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount

    @property
    def RunningCount(self):
        r"""Number of running tasks (valid only for complex tasks)
        :rtype: int
        """
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def StartedAt(self):
        r"""Task start time.
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def CreatedAt(self):
        r"""Task creation time
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""Update task time.
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Runtime(self):
        r"""Task running time in milliseconds.
        :rtype: int
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def DeviceId(self):
        r"""Device ID
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""Device name.
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""Channel name
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        self._FailReason = params.get("FailReason")
        self._Progress = params.get("Progress")
        self._Action = params.get("Action")
        self._ActionZhDesc = params.get("ActionZhDesc")
        self._TaskType = params.get("TaskType")
        self._ResourceId = params.get("ResourceId")
        self._Total = params.get("Total")
        self._SuccessCount = params.get("SuccessCount")
        self._FailCount = params.get("FailCount")
        self._RunningCount = params.get("RunningCount")
        self._StartedAt = params.get("StartedAt")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Runtime = params.get("Runtime")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Timeline(AbstractModel):
    r"""Time segment structure

    """

    def __init__(self):
        r"""
        :param _Begin: Fragment start time
        :type Begin: int
        :param _End: Shard end time
        :type End: int
        """
        self._Begin = None
        self._End = None

    @property
    def Begin(self):
        r"""Fragment start time
        :rtype: int
        """
        return self._Begin

    @Begin.setter
    def Begin(self, Begin):
        self._Begin = Begin

    @property
    def End(self):
        r"""Shard end time
        :rtype: int
        """
        return self._End

    @End.setter
    def End(self, End):
        self._End = End


    def _deserialize(self, params):
        self._Begin = params.get("Begin")
        self._End = params.get("End")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceData(AbstractModel):
    r"""Modify the device interface return data

    """

    def __init__(self):
        r"""
        :param _DeviceId: <p>Device ID</p>
        :type DeviceId: str
        :param _Code: <p>Device code (for national standard devices, it is the 20-digit National Standard Encoding we generated for the device; for rtmp devices, it is the 10-digit device code)</p>
        :type Code: str
        :param _Name: <p>Device name.</p>
        :type Name: str
        :param _AccessProtocol: <p>Device access protocol. 1: RTMP; 2: GB.</p><p>Enumeration values:</p><ul><li>1: RTMP</li><li>2: GB</li></ul>
        :type AccessProtocol: int
        :param _Type: <p>Device type. 1: IPC. 2: NVR</p>
        :type Type: int
        :param _ClusterId: <p>Device access service node ID</p>
        :type ClusterId: str
        :param _ClusterName: <p>Device access service node name</p>
        :type ClusterName: str
        :param _TransportProtocol: <p>Device streaming protocol. 1: UDP, 2: TCP</p>
        :type TransportProtocol: int
        :param _Password: <p>Device password.</p>
        :type Password: str
        :param _Description: <p>Device description</p>
        :type Description: str
        :param _Status: <p>Device status. 0: unregistered, 1: online, 2: offline, 3: disabled</p>
        :type Status: int
        :param _OrganizationId: <p>Affiliated organization ID of the device</p>
        :type OrganizationId: int
        :param _GatewayId: <p>Device access gateway ID (deprecated, reserved for compatibility, can be ignored)</p>
        :type GatewayId: str
        :param _ProtocolType: <p>Gateway access protocol type (deprecated, reserved for compatibility, can be ignored)</p>
        :type ProtocolType: int
        :param _Ip: <p>Device access IP</p>
        :type Ip: str
        :param _Port: <p>Device Port</p>
        :type Port: int
        :param _Username: <p>Device username</p>
        :type Username: str
        :param _AppId: <p>User Id</p>
        :type AppId: int
        """
        self._DeviceId = None
        self._Code = None
        self._Name = None
        self._AccessProtocol = None
        self._Type = None
        self._ClusterId = None
        self._ClusterName = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._Status = None
        self._OrganizationId = None
        self._GatewayId = None
        self._ProtocolType = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._AppId = None

    @property
    def DeviceId(self):
        r"""<p>Device ID</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Code(self):
        r"""<p>Device code (for national standard devices, it is the 20-digit National Standard Encoding we generated for the device; for rtmp devices, it is the 10-digit device code)</p>
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Name(self):
        r"""<p>Device name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AccessProtocol(self):
        r"""<p>Device access protocol. 1: RTMP; 2: GB.</p><p>Enumeration values:</p><ul><li>1: RTMP</li><li>2: GB</li></ul>
        :rtype: int
        """
        return self._AccessProtocol

    @AccessProtocol.setter
    def AccessProtocol(self, AccessProtocol):
        self._AccessProtocol = AccessProtocol

    @property
    def Type(self):
        r"""<p>Device type. 1: IPC. 2: NVR</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClusterId(self):
        r"""<p>Device access service node ID</p>
        :rtype: str
        """
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        r"""<p>Device access service node name</p>
        :rtype: str
        """
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def TransportProtocol(self):
        r"""<p>Device streaming protocol. 1: UDP, 2: TCP</p>
        :rtype: int
        """
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        r"""<p>Device password.</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""<p>Device description</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""<p>Device status. 0: unregistered, 1: online, 2: offline, 3: disabled</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrganizationId(self):
        r"""<p>Affiliated organization ID of the device</p>
        :rtype: int
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def GatewayId(self):
        r"""<p>Device access gateway ID (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ProtocolType(self):
        r"""<p>Gateway access protocol type (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: int
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def Ip(self):
        r"""<p>Device access IP</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""<p>Device Port</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        r"""<p>Device username</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def AppId(self):
        r"""<p>User Id</p>
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Code = params.get("Code")
        self._Name = params.get("Name")
        self._AccessProtocol = params.get("AccessProtocol")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._OrganizationId = params.get("OrganizationId")
        self._GatewayId = params.get("GatewayId")
        self._ProtocolType = params.get("ProtocolType")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceOrganizationRequest(AbstractModel):
    r"""UpdateDeviceOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceIds: Device ID array (obtain from the ListDevices API for getting device list)
        :type DeviceIds: list of str
        :param _OrganizationId: Organization ID (obtain from the DescribeOrganization API)
        :type OrganizationId: str
        """
        self._DeviceIds = None
        self._OrganizationId = None

    @property
    def DeviceIds(self):
        r"""Device ID array (obtain from the ListDevices API for getting device list)
        :rtype: list of str
        """
        return self._DeviceIds

    @DeviceIds.setter
    def DeviceIds(self, DeviceIds):
        self._DeviceIds = DeviceIds

    @property
    def OrganizationId(self):
        r"""Organization ID (obtain from the DescribeOrganization API)
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._DeviceIds = params.get("DeviceIds")
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceOrganizationResponse(AbstractModel):
    r"""UpdateDeviceOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateDeviceStatusRequest(AbstractModel):
    r"""UpdateDeviceStatus request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: Device ID (obtain from the ListDevices API for getting device list)
        :type DeviceId: str
        :param _Status: Disable enable status code (2: enable, 3: disable)
        :type Status: int
        """
        self._DeviceId = None
        self._Status = None

    @property
    def DeviceId(self):
        r"""Device ID (obtain from the ListDevices API for getting device list)
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Status(self):
        r"""Disable enable status code (2: enable, 3: disable)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDeviceStatusResponse(AbstractModel):
    r"""UpdateDeviceStatus response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateOrgData(AbstractModel):
    r"""Modify the interface return data of an organizational unit

    """

    def __init__(self):
        r"""
        :param _OrganizationId: Organization ID
        :type OrganizationId: str
        :param _Name: Organization name
        :type Name: str
        :param _ParentId: Organizational parent node ID
        :type ParentId: str
        :param _Level: Organization hierarchy
        :type Level: int
        :param _AppId: User ID.
        :type AppId: int
        :param _ParentIds: Organizational structure
        :type ParentIds: str
        :param _Total: Total number of devices
        :type Total: int
        :param _Online: Number of devices online
        :type Online: int
        """
        self._OrganizationId = None
        self._Name = None
        self._ParentId = None
        self._Level = None
        self._AppId = None
        self._ParentIds = None
        self._Total = None
        self._Online = None

    @property
    def OrganizationId(self):
        r"""Organization ID
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        r"""Organization name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentId(self):
        r"""Organizational parent node ID
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId

    @property
    def Level(self):
        r"""Organization hierarchy
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def AppId(self):
        r"""User ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ParentIds(self):
        r"""Organizational structure
        :rtype: str
        """
        return self._ParentIds

    @ParentIds.setter
    def ParentIds(self, ParentIds):
        self._ParentIds = ParentIds

    @property
    def Total(self):
        r"""Total number of devices
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Online(self):
        r"""Number of devices online
        :rtype: int
        """
        return self._Online

    @Online.setter
    def Online(self, Online):
        self._Online = Online


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        self._ParentId = params.get("ParentId")
        self._Level = params.get("Level")
        self._AppId = params.get("AppId")
        self._ParentIds = params.get("ParentIds")
        self._Total = params.get("Total")
        self._Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationRequest(AbstractModel):
    r"""UpdateOrganization request structure.

    """

    def __init__(self):
        r"""
        :param _OrganizationId: Organization ID (obtain from the DescribeOrganization API for querying organizations)
        :type OrganizationId: str
        :param _Name: Organization name. Chinese, English, digits, spaces, Chinese and English parentheses, underscores (_), and hyphens (-) are supported. The length cannot exceed 64 characters, and the organization name must be unique.
        :type Name: str
        """
        self._OrganizationId = None
        self._Name = None

    @property
    def OrganizationId(self):
        r"""Organization ID (obtain from the DescribeOrganization API for querying organizations)
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Name(self):
        r"""Organization name. Chinese, English, digits, spaces, Chinese and English parentheses, underscores (_), and hyphens (-) are supported. The length cannot exceed 64 characters, and the organization name must be unique.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationResponse(AbstractModel):
    r"""UpdateOrganization response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateOrgData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateOrgData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateOrgData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordBackupPlanData(AbstractModel):
    r"""data for modifying the recording cloud migration plan

    """

    def __init__(self):
        r"""
        :param _PlanId: Recording cloud migration plan ID
        :type PlanId: str
        :param _PlanName: Recording cloud migration plan name
        :type PlanName: str
        :param _TemplateId: Video cloud template ID
        :type TemplateId: str
        :param _Describe: Description of the recording cloud migration plan
        :type Describe: str
        :param _LifeCycle: Cloud file lifecycle
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Status: Recording cloud migration plan status. `1`: in normal use. `0`: deleting, unavailable.
        :type Status: int
        :param _ChannelCount: Number of channels
        :type ChannelCount: int
        :param _CreateAt: Creation time.
        :type CreateAt: str
        :param _UpdateAt: Modification time.
        :type UpdateAt: str
        """
        self._PlanId = None
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Status = None
        self._ChannelCount = None
        self._CreateAt = None
        self._UpdateAt = None

    @property
    def PlanId(self):
        r"""Recording cloud migration plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def PlanName(self):
        r"""Recording cloud migration plan name
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Video cloud template ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Description of the recording cloud migration plan
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        r"""Cloud file lifecycle
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Status(self):
        r"""Recording cloud migration plan status. `1`: in normal use. `0`: deleting, unavailable.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ChannelCount(self):
        r"""Number of channels
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreateAt(self):
        r"""Creation time.
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""Modification time.
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        self._Status = params.get("Status")
        self._ChannelCount = params.get("ChannelCount")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupPlanModify(AbstractModel):
    r"""Modify the data structure of the recording cloud migration plan

    """

    def __init__(self):
        r"""
        :param _PlanName: Recording cloud migration plan name (supports only Chinese, English, digits, _, and -, length not exceeding 32 characters. The plan name must be globally unique and cannot be empty or repeated. This field is not required if the name is not modified.)
        :type PlanName: str
        :param _TemplateId: Recording template ID (obtain from the ListRecordBackupTemplates API for querying the video recording upload template list. This field is not required if the template ID is not modified)
        :type TemplateId: str
        :param _Describe: Recording cloud migration plan description (only supports Chinese, English, numbers, _, -, length not exceeding 128 characters. This field is not required if the description is not modified)
        :type Describe: str
        :param _LifeCycle: Lifecycle (lifecycle settings for video recording files, managing the time when files are in cold or hot storage. This field is not required if you do not modify the lifecycle)
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Add: Device channels to be added (Json array; not required when no channels are added; the total number of channels added at once cannot exceed 5000, including the number of channels under the organizational directory)
        :type Add: list of ChannelInfo
        :param _Del: Device channel to delete (Json array containing the IDs of device channels to delete. Not required if no device channel is deleted)
        :type Del: list of str
        :param _OrganizationId: Add the channels of all devices under the organizational unit (Json array, can be empty, and the total number of channels no more than 5000, including the number of channels in the Add field)
        :type OrganizationId: list of str
        """
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._LifeCycle = None
        self._Add = None
        self._Del = None
        self._OrganizationId = None

    @property
    def PlanName(self):
        r"""Recording cloud migration plan name (supports only Chinese, English, digits, _, and -, length not exceeding 32 characters. The plan name must be globally unique and cannot be empty or repeated. This field is not required if the name is not modified.)
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Recording template ID (obtain from the ListRecordBackupTemplates API for querying the video recording upload template list. This field is not required if the template ID is not modified)
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Recording cloud migration plan description (only supports Chinese, English, numbers, _, -, length not exceeding 128 characters. This field is not required if the description is not modified)
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def LifeCycle(self):
        r"""Lifecycle (lifecycle settings for video recording files, managing the time when files are in cold or hot storage. This field is not required if you do not modify the lifecycle)
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Add(self):
        r"""Device channels to be added (Json array; not required when no channels are added; the total number of channels added at once cannot exceed 5000, including the number of channels under the organizational directory)
        :rtype: list of ChannelInfo
        """
        return self._Add

    @Add.setter
    def Add(self, Add):
        self._Add = Add

    @property
    def Del(self):
        r"""Device channel to delete (Json array containing the IDs of device channels to delete. Not required if no device channel is deleted)
        :rtype: list of str
        """
        return self._Del

    @Del.setter
    def Del(self, Del):
        self._Del = Del

    @property
    def OrganizationId(self):
        r"""Add the channels of all devices under the organizational unit (Json array, can be empty, and the total number of channels no more than 5000, including the number of channels in the Add field)
        :rtype: list of str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId


    def _deserialize(self, params):
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        if params.get("Add") is not None:
            self._Add = []
            for item in params.get("Add"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Add.append(obj)
        self._Del = params.get("Del")
        self._OrganizationId = params.get("OrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupPlanRequest(AbstractModel):
    r"""UpdateRecordBackupPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID
        :type PlanId: str
        :param _Mod: Modified Content
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanModify`
        """
        self._PlanId = None
        self._Mod = None

    @property
    def PlanId(self):
        r"""Plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Mod(self):
        r"""Modified Content
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanModify`
        """
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordBackupPlanModify()
            self._Mod._deserialize(params.get("Mod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupPlanResponse(AbstractModel):
    r"""UpdateRecordBackupPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupPlanData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateRecordBackupPlanData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordBackupTemplateData(AbstractModel):
    r"""data for modifying a video cloud template

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>Template ID</p>
        :type TemplateId: str
        :param _TemplateName: <p>Template name</p>
        :type TemplateName: str
        :param _TimeSections: <p>Cloud Upload Time Period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: <p>Recording time period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: <p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :type Scale: int
        :param _CreateAt: <p>Creation time.</p>
        :type CreateAt: str
        :param _UpdateAt: <p>Update time.</p>
        :type UpdateAt: str
        :param _DayOffset: <p>Cycle offset. Default value: 1, which means to pull yesterday's video recording from the device. 0 means to pull today's video recording from the device. 3 means to pull the video recording from the device from the day before yesterday.</p>
        :type DayOffset: int
        """
        self._TemplateId = None
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None
        self._CreateAt = None
        self._UpdateAt = None
        self._DayOffset = None

    @property
    def TemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def TemplateName(self):
        r"""<p>Template name</p>
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""<p>Cloud Upload Time Period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        r"""<p>Recording time period (set by week, supports setting multiple time periods per day, each time period not less than 10 minutes)</p>
        :rtype: list of RecordTemplateTimeSections
        """
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        r"""<p>Speed multiplication for cloud migration (supports 1x, 2x, and 4x)</p>
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def CreateAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateAt

    @CreateAt.setter
    def CreateAt(self, CreateAt):
        self._CreateAt = CreateAt

    @property
    def UpdateAt(self):
        r"""<p>Update time.</p>
        :rtype: str
        """
        return self._UpdateAt

    @UpdateAt.setter
    def UpdateAt(self, UpdateAt):
        self._UpdateAt = UpdateAt

    @property
    def DayOffset(self):
        r"""<p>Cycle offset. Default value: 1, which means to pull yesterday's video recording from the device. 0 means to pull today's video recording from the device. 3 means to pull the video recording from the device from the day before yesterday.</p>
        :rtype: int
        """
        return self._DayOffset

    @DayOffset.setter
    def DayOffset(self, DayOffset):
        self._DayOffset = DayOffset


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        self._CreateAt = params.get("CreateAt")
        self._UpdateAt = params.get("UpdateAt")
        self._DayOffset = params.get("DayOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupTemplateModify(AbstractModel):
    r"""Modify the video cloud template data structure

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name (not required if you do not rename)
        :type TemplateName: str
        :param _TimeSections: Cloud upload time period (settings can be done by week. Multiple time periods can be set for each day, with each time period not less than 10 minutes)
        :type TimeSections: list of RecordTemplateTimeSections
        :param _DevTimeSections: Recording time period (set by week. Multiple time periods can be set each day, each not less than 10 minutes)
        :type DevTimeSections: list of RecordTemplateTimeSections
        :param _Scale: Cloud speed multiplication (supports 1x, 2x, and 4x).
        :type Scale: int
        """
        self._TemplateName = None
        self._TimeSections = None
        self._DevTimeSections = None
        self._Scale = None

    @property
    def TemplateName(self):
        r"""Template name (not required if you do not rename)
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""Cloud upload time period (settings can be done by week. Multiple time periods can be set for each day, with each time period not less than 10 minutes)
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections

    @property
    def DevTimeSections(self):
        r"""Recording time period (set by week. Multiple time periods can be set each day, each not less than 10 minutes)
        :rtype: list of RecordTemplateTimeSections
        """
        return self._DevTimeSections

    @DevTimeSections.setter
    def DevTimeSections(self, DevTimeSections):
        self._DevTimeSections = DevTimeSections

    @property
    def Scale(self):
        r"""Cloud speed multiplication (supports 1x, 2x, and 4x).
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        if params.get("DevTimeSections") is not None:
            self._DevTimeSections = []
            for item in params.get("DevTimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._DevTimeSections.append(obj)
        self._Scale = params.get("Scale")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupTemplateRequest(AbstractModel):
    r"""UpdateRecordBackupTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID (obtain from the ListRecordBackupTemplates API for querying the video recording cloud template list)
        :type TemplateId: str
        :param _Mod: Modify the template data for video recording upload to cloud
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateModify`
        """
        self._TemplateId = None
        self._Mod = None

    @property
    def TemplateId(self):
        r"""Template ID (obtain from the ListRecordBackupTemplates API for querying the video recording cloud template list)
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Mod(self):
        r"""Modify the template data for video recording upload to cloud
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateModify`
        """
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordBackupTemplateModify()
            self._Mod._deserialize(params.get("Mod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordBackupTemplateResponse(AbstractModel):
    r"""UpdateRecordBackupTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data.
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned data.
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordBackupTemplateData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateRecordBackupTemplateData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordPlanData(AbstractModel):
    r"""Modify the data of the real-time Cloud Recording plan

    """

    def __init__(self):
        r"""
        :param _PlanName: Cloud migration plan name, supporting only Chinese, English, digits, _, -, with a length not exceeding 32 characters. The plan name must be globally unique and cannot be empty or duplicated. This field is not required if the name is not modified.
        :type PlanName: str
        :param _TemplateId: Cloud template ID. This field is not required if the template ID is not modified.
        :type TemplateId: str
        :param _Describe: Usage plan description. It can contain only Chinese characters, English letters, digits, underscores (_), and hyphens (-), with a length not exceeding 128 characters. This field is not required if you do not modify the description.
        :type Describe: str
        :param _StreamType: Stream type. default: The stream type is not specified, and the default push type of the device is used. main: main stream. sub: substream. Other: custom based on the device capability set. The length cannot exceed 32 bytes.
        :type StreamType: str
        :param _LifeCycle: Lifecycle, file lifecycle settings, the time when cold and hot storage of files is managed. This field is not required if lifecycle is not modified.
        :type LifeCycle: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        :param _Add: Device channels to be added. Json array. This field is not required when no channels are added. The total number of channels added at once cannot exceed 5,000, including the number of channels under the organization directory.
        :type Add: list of ChannelInfo
        :param _Del: Device channels to delete. Json array. The content is the IDs of the device channels to delete. This field is not required if no device channel is deleted.
        :type Del: list of str
        :param _OrganizationId: Organizational directory ID. Add all device channels under the organizational directory. Json array. Can be empty. And the total number of channels is no more than 5,000 (including the number of channels added in the Add field).
        :type OrganizationId: list of str
        :param _RepairMode: Video recording supplement mode (0: not enabled, 1: enabled)
        :type RepairMode: int
        """
        self._PlanName = None
        self._TemplateId = None
        self._Describe = None
        self._StreamType = None
        self._LifeCycle = None
        self._Add = None
        self._Del = None
        self._OrganizationId = None
        self._RepairMode = None

    @property
    def PlanName(self):
        r"""Cloud migration plan name, supporting only Chinese, English, digits, _, -, with a length not exceeding 32 characters. The plan name must be globally unique and cannot be empty or duplicated. This field is not required if the name is not modified.
        :rtype: str
        """
        return self._PlanName

    @PlanName.setter
    def PlanName(self, PlanName):
        self._PlanName = PlanName

    @property
    def TemplateId(self):
        r"""Cloud template ID. This field is not required if the template ID is not modified.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Describe(self):
        r"""Usage plan description. It can contain only Chinese characters, English letters, digits, underscores (_), and hyphens (-), with a length not exceeding 128 characters. This field is not required if you do not modify the description.
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def StreamType(self):
        r"""Stream type. default: The stream type is not specified, and the default push type of the device is used. main: main stream. sub: substream. Other: custom based on the device capability set. The length cannot exceed 32 bytes.
        :rtype: str
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def LifeCycle(self):
        r"""Lifecycle, file lifecycle settings, the time when cold and hot storage of files is managed. This field is not required if lifecycle is not modified.
        :rtype: :class:`tencentcloud.iss.v20230517.models.LifeCycleData`
        """
        return self._LifeCycle

    @LifeCycle.setter
    def LifeCycle(self, LifeCycle):
        self._LifeCycle = LifeCycle

    @property
    def Add(self):
        r"""Device channels to be added. Json array. This field is not required when no channels are added. The total number of channels added at once cannot exceed 5,000, including the number of channels under the organization directory.
        :rtype: list of ChannelInfo
        """
        return self._Add

    @Add.setter
    def Add(self, Add):
        self._Add = Add

    @property
    def Del(self):
        r"""Device channels to delete. Json array. The content is the IDs of the device channels to delete. This field is not required if no device channel is deleted.
        :rtype: list of str
        """
        return self._Del

    @Del.setter
    def Del(self, Del):
        self._Del = Del

    @property
    def OrganizationId(self):
        r"""Organizational directory ID. Add all device channels under the organizational directory. Json array. Can be empty. And the total number of channels is no more than 5,000 (including the number of channels added in the Add field).
        :rtype: list of str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def RepairMode(self):
        r"""Video recording supplement mode (0: not enabled, 1: enabled)
        :rtype: int
        """
        return self._RepairMode

    @RepairMode.setter
    def RepairMode(self, RepairMode):
        self._RepairMode = RepairMode


    def _deserialize(self, params):
        self._PlanName = params.get("PlanName")
        self._TemplateId = params.get("TemplateId")
        self._Describe = params.get("Describe")
        self._StreamType = params.get("StreamType")
        if params.get("LifeCycle") is not None:
            self._LifeCycle = LifeCycleData()
            self._LifeCycle._deserialize(params.get("LifeCycle"))
        if params.get("Add") is not None:
            self._Add = []
            for item in params.get("Add"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Add.append(obj)
        self._Del = params.get("Del")
        self._OrganizationId = params.get("OrganizationId")
        self._RepairMode = params.get("RepairMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordPlanRequest(AbstractModel):
    r"""UpdateRecordPlan request structure.

    """

    def __init__(self):
        r"""
        :param _PlanId: Plan ID
        :type PlanId: str
        :param _Mod: Modify the content of the plan
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordPlanData`
        """
        self._PlanId = None
        self._Mod = None

    @property
    def PlanId(self):
        r"""Plan ID
        :rtype: str
        """
        return self._PlanId

    @PlanId.setter
    def PlanId(self, PlanId):
        self._PlanId = PlanId

    @property
    def Mod(self):
        r"""Modify the content of the plan
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordPlanData`
        """
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._PlanId = params.get("PlanId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordPlanData()
            self._Mod._deserialize(params.get("Mod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordPlanResponse(AbstractModel):
    r"""UpdateRecordPlan response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordPlanOptData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.RecordPlanOptData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RecordPlanOptData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateRecordTemplateData(AbstractModel):
    r"""Request data structure for modifying a real-time cloud template

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name. If you do not modify the name, you do not need to include this field.
        :type TemplateName: str
        :param _TimeSections: Cloud upload time period. If you do not modify the name, you do not need to include this field.
        :type TimeSections: list of RecordTemplateTimeSections
        """
        self._TemplateName = None
        self._TimeSections = None

    @property
    def TemplateName(self):
        r"""Template name. If you do not modify the name, you do not need to include this field.
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TimeSections(self):
        r"""Cloud upload time period. If you do not modify the name, you do not need to include this field.
        :rtype: list of RecordTemplateTimeSections
        """
        return self._TimeSections

    @TimeSections.setter
    def TimeSections(self, TimeSections):
        self._TimeSections = TimeSections


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TimeSections") is not None:
            self._TimeSections = []
            for item in params.get("TimeSections"):
                obj = RecordTemplateTimeSections()
                obj._deserialize(item)
                self._TimeSections.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordTemplateRequest(AbstractModel):
    r"""UpdateRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateId: Template ID.
        :type TemplateId: str
        :param _Mod: Modify Content
        :type Mod: :class:`tencentcloud.iss.v20230517.models.UpdateRecordTemplateData`
        """
        self._TemplateId = None
        self._Mod = None

    @property
    def TemplateId(self):
        r"""Template ID.
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Mod(self):
        r"""Modify Content
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateRecordTemplateData`
        """
        return self._Mod

    @Mod.setter
    def Mod(self, Mod):
        self._Mod = Mod


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        if params.get("Mod") is not None:
            self._Mod = UpdateRecordTemplateData()
            self._Mod._deserialize(params.get("Mod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordTemplateResponse(AbstractModel):
    r"""UpdateRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned result
        :type Data: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""Returned result
        :rtype: :class:`tencentcloud.iss.v20230517.models.RecordTemplateInfo`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RecordTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UpdateUserDeviceRequest(AbstractModel):
    r"""UpdateUserDevice request structure.

    """

    def __init__(self):
        r"""
        :param _DeviceId: <p>Device ID (obtain from the device list API ListDevices)</p><p>For parameter values, see <a href="https://www.tencentcloud.com/document/api/1344/95871?from_cn_redirect=1">ListDevices</a></p>
        :type DeviceId: str
        :param _Name: <p>Device name (only supports Chinese, English, numbers, spaces, Chinese and English parentheses, _, -, length not exceeding 128 characters)</p>
        :type Name: str
        :param _TransportProtocol: <p>Device streaming protocol. Only valid for national standard devices. Fill in 0 to make no change (1: UDP, 2: TCP)</p>
        :type TransportProtocol: int
        :param _Password: <p>Device password (only supported for national standard devices, length not exceeding 64 characters)</p>
        :type Password: str
        :param _Description: <p>Device description (length not exceeding 128 characters)</p>
        :type Description: str
        :param _Ip: <p>Device access IP (deprecated, reserved for compatibility, can be ignored)</p>
        :type Ip: str
        :param _Port: <p>Device Port (deprecated, reserved for compatibility, can be ignored)</p>
        :type Port: int
        :param _Username: <p>Device username (deprecated, reserved for compatibility, can be ignored)</p>
        :type Username: str
        :param _ProtocolType: <p>Gateway device access protocol (deprecated, reserved for compatibility, can be ignored)</p>
        :type ProtocolType: int
        :param _AudioSwitch: <p>Audio on/off (0: off; 1: on), enabled by default. Audio is dropped when turned off.</p>
        :type AudioSwitch: int
        :param _SubscribeSwitch: <p>Subscription switch (0: off; 1: on). Default On. When enabled, it subscribes to device channel transitions. Valid only for national standard NVR devices.</p>
        :type SubscribeSwitch: int
        :param _SilentFrameSwitch: <p>Whether to enable silent frame (0: disabled; 1: enabled)</p>
        :type SilentFrameSwitch: int
        :param _TimeSyncSwitch: <p>Clock sync switch (only effective for national standard devices)</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul><p>Default value: 1</p>
        :type TimeSyncSwitch: int
        """
        self._DeviceId = None
        self._Name = None
        self._TransportProtocol = None
        self._Password = None
        self._Description = None
        self._Ip = None
        self._Port = None
        self._Username = None
        self._ProtocolType = None
        self._AudioSwitch = None
        self._SubscribeSwitch = None
        self._SilentFrameSwitch = None
        self._TimeSyncSwitch = None

    @property
    def DeviceId(self):
        r"""<p>Device ID (obtain from the device list API ListDevices)</p><p>For parameter values, see <a href="https://www.tencentcloud.com/document/api/1344/95871?from_cn_redirect=1">ListDevices</a></p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def Name(self):
        r"""<p>Device name (only supports Chinese, English, numbers, spaces, Chinese and English parentheses, _, -, length not exceeding 128 characters)</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TransportProtocol(self):
        r"""<p>Device streaming protocol. Only valid for national standard devices. Fill in 0 to make no change (1: UDP, 2: TCP)</p>
        :rtype: int
        """
        return self._TransportProtocol

    @TransportProtocol.setter
    def TransportProtocol(self, TransportProtocol):
        self._TransportProtocol = TransportProtocol

    @property
    def Password(self):
        r"""<p>Device password (only supported for national standard devices, length not exceeding 64 characters)</p>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Description(self):
        r"""<p>Device description (length not exceeding 128 characters)</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Ip(self):
        r"""<p>Device access IP (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""<p>Device Port (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Username(self):
        r"""<p>Device username (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def ProtocolType(self):
        r"""<p>Gateway device access protocol (deprecated, reserved for compatibility, can be ignored)</p>
        :rtype: int
        """
        return self._ProtocolType

    @ProtocolType.setter
    def ProtocolType(self, ProtocolType):
        self._ProtocolType = ProtocolType

    @property
    def AudioSwitch(self):
        r"""<p>Audio on/off (0: off; 1: on), enabled by default. Audio is dropped when turned off.</p>
        :rtype: int
        """
        return self._AudioSwitch

    @AudioSwitch.setter
    def AudioSwitch(self, AudioSwitch):
        self._AudioSwitch = AudioSwitch

    @property
    def SubscribeSwitch(self):
        r"""<p>Subscription switch (0: off; 1: on). Default On. When enabled, it subscribes to device channel transitions. Valid only for national standard NVR devices.</p>
        :rtype: int
        """
        return self._SubscribeSwitch

    @SubscribeSwitch.setter
    def SubscribeSwitch(self, SubscribeSwitch):
        self._SubscribeSwitch = SubscribeSwitch

    @property
    def SilentFrameSwitch(self):
        r"""<p>Whether to enable silent frame (0: disabled; 1: enabled)</p>
        :rtype: int
        """
        return self._SilentFrameSwitch

    @SilentFrameSwitch.setter
    def SilentFrameSwitch(self, SilentFrameSwitch):
        self._SilentFrameSwitch = SilentFrameSwitch

    @property
    def TimeSyncSwitch(self):
        r"""<p>Clock sync switch (only effective for national standard devices)</p><p>Enumeration values:</p><ul><li>0: Off</li><li>1: On</li></ul><p>Default value: 1</p>
        :rtype: int
        """
        return self._TimeSyncSwitch

    @TimeSyncSwitch.setter
    def TimeSyncSwitch(self, TimeSyncSwitch):
        self._TimeSyncSwitch = TimeSyncSwitch


    def _deserialize(self, params):
        self._DeviceId = params.get("DeviceId")
        self._Name = params.get("Name")
        self._TransportProtocol = params.get("TransportProtocol")
        self._Password = params.get("Password")
        self._Description = params.get("Description")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Username = params.get("Username")
        self._ProtocolType = params.get("ProtocolType")
        self._AudioSwitch = params.get("AudioSwitch")
        self._SubscribeSwitch = params.get("SubscribeSwitch")
        self._SilentFrameSwitch = params.get("SilentFrameSwitch")
        self._TimeSyncSwitch = params.get("TimeSyncSwitch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserDeviceResponse(AbstractModel):
    r"""UpdateUserDevice response structure.

    """

    def __init__(self):
        r"""
        :param _Data: <p>Response data.</p>
        :type Data: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceData`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""<p>Response data.</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.UpdateDeviceData`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UpdateDeviceData()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class VLPlanInfo(AbstractModel):
    r"""Visual understanding plan information

    """

    def __init__(self):
        r"""
        :param _VLPlanId: <p>Plan ID</p>
        :type VLPlanId: str
        :param _Name: <p>Plan name.</p>
        :type Name: str
        :param _Describe: <p>Plan description.</p>
        :type Describe: str
        :param _VLTemplateId: <p>ID of the visual understanding template</p>
        :type VLTemplateId: str
        :param _Callback: <p>Callback notification configuration</p>
        :type Callback: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        :param _FileExpires: <p>File expiration time (seconds)</p>
        :type FileExpires: int
        :param _ChannelCount: <p>Number of channels included in the plan</p>
        :type ChannelCount: int
        :param _CreatedAt: <p>Creation time.</p>
        :type CreatedAt: str
        :param _UpdatedAt: <p>Last update time</p>
        :type UpdatedAt: str
        """
        self._VLPlanId = None
        self._Name = None
        self._Describe = None
        self._VLTemplateId = None
        self._Callback = None
        self._FileExpires = None
        self._ChannelCount = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def VLPlanId(self):
        r"""<p>Plan ID</p>
        :rtype: str
        """
        return self._VLPlanId

    @VLPlanId.setter
    def VLPlanId(self, VLPlanId):
        self._VLPlanId = VLPlanId

    @property
    def Name(self):
        r"""<p>Plan name.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Describe(self):
        r"""<p>Plan description.</p>
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def VLTemplateId(self):
        r"""<p>ID of the visual understanding template</p>
        :rtype: str
        """
        return self._VLTemplateId

    @VLTemplateId.setter
    def VLTemplateId(self, VLTemplateId):
        self._VLTemplateId = VLTemplateId

    @property
    def Callback(self):
        r"""<p>Callback notification configuration</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def FileExpires(self):
        r"""<p>File expiration time (seconds)</p>
        :rtype: int
        """
        return self._FileExpires

    @FileExpires.setter
    def FileExpires(self, FileExpires):
        self._FileExpires = FileExpires

    @property
    def ChannelCount(self):
        r"""<p>Number of channels included in the plan</p>
        :rtype: int
        """
        return self._ChannelCount

    @ChannelCount.setter
    def ChannelCount(self, ChannelCount):
        self._ChannelCount = ChannelCount

    @property
    def CreatedAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>Last update time</p>
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._VLPlanId = params.get("VLPlanId")
        self._Name = params.get("Name")
        self._Describe = params.get("Describe")
        self._VLTemplateId = params.get("VLTemplateId")
        if params.get("Callback") is not None:
            self._Callback = CallbackURL()
            self._Callback._deserialize(params.get("Callback"))
        self._FileExpires = params.get("FileExpires")
        self._ChannelCount = params.get("ChannelCount")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VLPlanResultDetailInfo(AbstractModel):
    r"""Visual understanding plan result details

    """

    def __init__(self):
        r"""
        :param _VLPlanResultId: <p>Analysis result ID</p>
        :type VLPlanResultId: str
        :param _MediaType: <p>Media type. The current fixed value is image</p>
        :type MediaType: str
        :param _VLPlanId: <p>ID of the associated analysis plan</p>
        :type VLPlanId: str
        :param _VLPlanName: <p>Plan name</p>
        :type VLPlanName: str
        :param _ChannelId: <p>Channel ID</p>
        :type ChannelId: str
        :param _ChannelName: <p>Channel name</p>
        :type ChannelName: str
        :param _DeviceId: <p>Device ID</p>
        :type DeviceId: str
        :param _DeviceName: <p>Device name</p>
        :type DeviceName: str
        :param _OrganizationId: <p>Affiliated organization ID</p>
        :type OrganizationId: str
        :param _OrganizationName: <p>Affiliated organization name</p>
        :type OrganizationName: str
        :param _VLResultTimestamp: <p>Analysis timestamp (seconds)</p>
        :type VLResultTimestamp: int
        :param _SnapshotTimestamp: <p>Image mode screenshot timestamp (seconds)</p>
        :type SnapshotTimestamp: int
        :param _VideoStartTimestamp: <p>Video clip start timestamp (seconds)</p>
        :type VideoStartTimestamp: int
        :param _VideoEndTimestamp: <p>Video segment end timestamp (seconds)</p>
        :type VideoEndTimestamp: int
        :param _BilledFrameCount: <p>Billing method for the number of frames in video mode</p>
        :type BilledFrameCount: int
        :param _Content: <p>AI analysis result content (JSON string)</p>
        :type Content: str
        :param _ImageUrl: <p>Temporary screenshot download URL (valid for 300 seconds)</p>
        :type ImageUrl: str
        :param _ImageUrlExpire: <p>Screenshot URL validity period (seconds)</p>
        :type ImageUrlExpire: int
        :param _CreatedAt: <p>Creation time, format: 2006-01-02 15:04:05</p>
        :type CreatedAt: str
        :param _UpdatedAt: <p>Update time, format 2006-01-02 15:04:05</p>
        :type UpdatedAt: str
        """
        self._VLPlanResultId = None
        self._MediaType = None
        self._VLPlanId = None
        self._VLPlanName = None
        self._ChannelId = None
        self._ChannelName = None
        self._DeviceId = None
        self._DeviceName = None
        self._OrganizationId = None
        self._OrganizationName = None
        self._VLResultTimestamp = None
        self._SnapshotTimestamp = None
        self._VideoStartTimestamp = None
        self._VideoEndTimestamp = None
        self._BilledFrameCount = None
        self._Content = None
        self._ImageUrl = None
        self._ImageUrlExpire = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def VLPlanResultId(self):
        r"""<p>Analysis result ID</p>
        :rtype: str
        """
        return self._VLPlanResultId

    @VLPlanResultId.setter
    def VLPlanResultId(self, VLPlanResultId):
        self._VLPlanResultId = VLPlanResultId

    @property
    def MediaType(self):
        r"""<p>Media type. The current fixed value is image</p>
        :rtype: str
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def VLPlanId(self):
        r"""<p>ID of the associated analysis plan</p>
        :rtype: str
        """
        return self._VLPlanId

    @VLPlanId.setter
    def VLPlanId(self, VLPlanId):
        self._VLPlanId = VLPlanId

    @property
    def VLPlanName(self):
        r"""<p>Plan name</p>
        :rtype: str
        """
        return self._VLPlanName

    @VLPlanName.setter
    def VLPlanName(self, VLPlanName):
        self._VLPlanName = VLPlanName

    @property
    def ChannelId(self):
        r"""<p>Channel ID</p>
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""<p>Channel name</p>
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def DeviceId(self):
        r"""<p>Device ID</p>
        :rtype: str
        """
        return self._DeviceId

    @DeviceId.setter
    def DeviceId(self, DeviceId):
        self._DeviceId = DeviceId

    @property
    def DeviceName(self):
        r"""<p>Device name</p>
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def OrganizationId(self):
        r"""<p>Affiliated organization ID</p>
        :rtype: str
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def OrganizationName(self):
        r"""<p>Affiliated organization name</p>
        :rtype: str
        """
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def VLResultTimestamp(self):
        r"""<p>Analysis timestamp (seconds)</p>
        :rtype: int
        """
        return self._VLResultTimestamp

    @VLResultTimestamp.setter
    def VLResultTimestamp(self, VLResultTimestamp):
        self._VLResultTimestamp = VLResultTimestamp

    @property
    def SnapshotTimestamp(self):
        r"""<p>Image mode screenshot timestamp (seconds)</p>
        :rtype: int
        """
        return self._SnapshotTimestamp

    @SnapshotTimestamp.setter
    def SnapshotTimestamp(self, SnapshotTimestamp):
        self._SnapshotTimestamp = SnapshotTimestamp

    @property
    def VideoStartTimestamp(self):
        r"""<p>Video clip start timestamp (seconds)</p>
        :rtype: int
        """
        return self._VideoStartTimestamp

    @VideoStartTimestamp.setter
    def VideoStartTimestamp(self, VideoStartTimestamp):
        self._VideoStartTimestamp = VideoStartTimestamp

    @property
    def VideoEndTimestamp(self):
        r"""<p>Video segment end timestamp (seconds)</p>
        :rtype: int
        """
        return self._VideoEndTimestamp

    @VideoEndTimestamp.setter
    def VideoEndTimestamp(self, VideoEndTimestamp):
        self._VideoEndTimestamp = VideoEndTimestamp

    @property
    def BilledFrameCount(self):
        r"""<p>Billing method for the number of frames in video mode</p>
        :rtype: int
        """
        return self._BilledFrameCount

    @BilledFrameCount.setter
    def BilledFrameCount(self, BilledFrameCount):
        self._BilledFrameCount = BilledFrameCount

    @property
    def Content(self):
        r"""<p>AI analysis result content (JSON string)</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ImageUrl(self):
        r"""<p>Temporary screenshot download URL (valid for 300 seconds)</p>
        :rtype: str
        """
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl

    @property
    def ImageUrlExpire(self):
        r"""<p>Screenshot URL validity period (seconds)</p>
        :rtype: int
        """
        return self._ImageUrlExpire

    @ImageUrlExpire.setter
    def ImageUrlExpire(self, ImageUrlExpire):
        self._ImageUrlExpire = ImageUrlExpire

    @property
    def CreatedAt(self):
        r"""<p>Creation time, format: 2006-01-02 15:04:05</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>Update time, format 2006-01-02 15:04:05</p>
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._VLPlanResultId = params.get("VLPlanResultId")
        self._MediaType = params.get("MediaType")
        self._VLPlanId = params.get("VLPlanId")
        self._VLPlanName = params.get("VLPlanName")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._DeviceId = params.get("DeviceId")
        self._DeviceName = params.get("DeviceName")
        self._OrganizationId = params.get("OrganizationId")
        self._OrganizationName = params.get("OrganizationName")
        self._VLResultTimestamp = params.get("VLResultTimestamp")
        self._SnapshotTimestamp = params.get("SnapshotTimestamp")
        self._VideoStartTimestamp = params.get("VideoStartTimestamp")
        self._VideoEndTimestamp = params.get("VideoEndTimestamp")
        self._BilledFrameCount = params.get("BilledFrameCount")
        self._Content = params.get("Content")
        self._ImageUrl = params.get("ImageUrl")
        self._ImageUrlExpire = params.get("ImageUrlExpire")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VLPlanResultSnapshotImageUrlInfo(AbstractModel):
    r"""Visual understanding plan source material URL information

    """

    def __init__(self):
        r"""
        :param _VLPlanResultId: <p>Analysis result ID</p>
        :type VLPlanResultId: str
        :param _SourceFileURL: <p>Source material download URL (empty if unsuccessful)</p>
        :type SourceFileURL: str
        :param _Expire: <p>URL validity period (seconds; 0 on failure)</p>
        :type Expire: int
        :param _ErrMsg: <p>Error information (has a value on failure)</p>
        :type ErrMsg: str
        """
        self._VLPlanResultId = None
        self._SourceFileURL = None
        self._Expire = None
        self._ErrMsg = None

    @property
    def VLPlanResultId(self):
        r"""<p>Analysis result ID</p>
        :rtype: str
        """
        return self._VLPlanResultId

    @VLPlanResultId.setter
    def VLPlanResultId(self, VLPlanResultId):
        self._VLPlanResultId = VLPlanResultId

    @property
    def SourceFileURL(self):
        r"""<p>Source material download URL (empty if unsuccessful)</p>
        :rtype: str
        """
        return self._SourceFileURL

    @SourceFileURL.setter
    def SourceFileURL(self, SourceFileURL):
        self._SourceFileURL = SourceFileURL

    @property
    def Expire(self):
        r"""<p>URL validity period (seconds; 0 on failure)</p>
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def ErrMsg(self):
        r"""<p>Error information (has a value on failure)</p>
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._VLPlanResultId = params.get("VLPlanResultId")
        self._SourceFileURL = params.get("SourceFileURL")
        self._Expire = params.get("Expire")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VLTemplateInfo(AbstractModel):
    r"""Visual understanding template information

    """

    def __init__(self):
        r"""
        :param _VLTemplateId: <p>Template ID</p>
        :type VLTemplateId: str
        :param _AIModel: <p>AI model</p><p>Enumeration values:</p><ul><li>IVC-G: Default large model for view</li></ul>
        :type AIModel: str
        :param _Name: <p>AI scenario name</p>
        :type Name: str
        :param _Describe: <p>AI scenario description</p>
        :type Describe: str
        :param _Prompt: <p>Prompt content</p>
        :type Prompt: str
        :param _AnalysisMode: <p>Analysis mode</p><p>Enumeration values:</p><ul><li>image: Image mode</li><li>video: Video mode</li></ul>
        :type AnalysisMode: str
        :param _ImageConfig: <p>Image scenario configuration</p>
        :type ImageConfig: :class:`tencentcloud.iss.v20230517.models.ImageSceneInfo`
        :param _Times: <p>Effective period list</p>
        :type Times: list of EffectiveTime
        :param _CreatedAt: <p>Creation time.</p>
        :type CreatedAt: str
        :param _UpdatedAt: <p>Last update time</p>
        :type UpdatedAt: str
        :param _IsUsed: <p>Whether associated with a visual understanding plan</p>
        :type IsUsed: bool
        :param _VideoConfig: <p>Video scene configuration</p>
        :type VideoConfig: :class:`tencentcloud.iss.v20230517.models.VideoSceneInfo`
        """
        self._VLTemplateId = None
        self._AIModel = None
        self._Name = None
        self._Describe = None
        self._Prompt = None
        self._AnalysisMode = None
        self._ImageConfig = None
        self._Times = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._IsUsed = None
        self._VideoConfig = None

    @property
    def VLTemplateId(self):
        r"""<p>Template ID</p>
        :rtype: str
        """
        return self._VLTemplateId

    @VLTemplateId.setter
    def VLTemplateId(self, VLTemplateId):
        self._VLTemplateId = VLTemplateId

    @property
    def AIModel(self):
        r"""<p>AI model</p><p>Enumeration values:</p><ul><li>IVC-G: Default large model for view</li></ul>
        :rtype: str
        """
        return self._AIModel

    @AIModel.setter
    def AIModel(self, AIModel):
        self._AIModel = AIModel

    @property
    def Name(self):
        r"""<p>AI scenario name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Describe(self):
        r"""<p>AI scenario description</p>
        :rtype: str
        """
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Prompt(self):
        r"""<p>Prompt content</p>
        :rtype: str
        """
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def AnalysisMode(self):
        r"""<p>Analysis mode</p><p>Enumeration values:</p><ul><li>image: Image mode</li><li>video: Video mode</li></ul>
        :rtype: str
        """
        return self._AnalysisMode

    @AnalysisMode.setter
    def AnalysisMode(self, AnalysisMode):
        self._AnalysisMode = AnalysisMode

    @property
    def ImageConfig(self):
        r"""<p>Image scenario configuration</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.ImageSceneInfo`
        """
        return self._ImageConfig

    @ImageConfig.setter
    def ImageConfig(self, ImageConfig):
        self._ImageConfig = ImageConfig

    @property
    def Times(self):
        r"""<p>Effective period list</p>
        :rtype: list of EffectiveTime
        """
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times

    @property
    def CreatedAt(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""<p>Last update time</p>
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def IsUsed(self):
        r"""<p>Whether associated with a visual understanding plan</p>
        :rtype: bool
        """
        return self._IsUsed

    @IsUsed.setter
    def IsUsed(self, IsUsed):
        self._IsUsed = IsUsed

    @property
    def VideoConfig(self):
        r"""<p>Video scene configuration</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.VideoSceneInfo`
        """
        return self._VideoConfig

    @VideoConfig.setter
    def VideoConfig(self, VideoConfig):
        self._VideoConfig = VideoConfig


    def _deserialize(self, params):
        self._VLTemplateId = params.get("VLTemplateId")
        self._AIModel = params.get("AIModel")
        self._Name = params.get("Name")
        self._Describe = params.get("Describe")
        self._Prompt = params.get("Prompt")
        self._AnalysisMode = params.get("AnalysisMode")
        if params.get("ImageConfig") is not None:
            self._ImageConfig = ImageSceneInfo()
            self._ImageConfig._deserialize(params.get("ImageConfig"))
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = EffectiveTime()
                obj._deserialize(item)
                self._Times.append(obj)
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._IsUsed = params.get("IsUsed")
        if params.get("VideoConfig") is not None:
            self._VideoConfig = VideoSceneInfo()
            self._VideoConfig._deserialize(params.get("VideoConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoDownloadTask(AbstractModel):
    r"""Local recording download task

    """

    def __init__(self):
        r"""
        :param _DownloadTaskId: Download task ID
        :type DownloadTaskId: str
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _ChannelName: Channel name
        :type ChannelName: str
        :param _ChannelCode: Channel encoding
        :type ChannelCode: str
        :param _DeviceName: Device name.
        :type DeviceName: str
        :param _DeviceCode: Device code
        :type DeviceCode: str
        :param _Status: Task status (0: pending; 1: executing; 2: task complete;
3: Task failure)
        :type Status: int
        :param _VideoTimeSection: Download the recording time period
        :type VideoTimeSection: str
        :param _Scale: Playback speed
        :type Scale: int
        :param _DownloadTime: Download duration.
        :type DownloadTime: int
        :param _VideoSize: Video recording size
        :type VideoSize: int
        :param _StartTime: Task start time
        :type StartTime: str
        :param _EndTime: Task end time
        :type EndTime: str
        :param _FileDownloadUrl: File download address
        :type FileDownloadUrl: str
        :param _FailedReason: Reason for failure
        :type FailedReason: str
        :param _Expire: Lifecycle rule, number of days in hot storage
        :type Expire: int
        :param _PreviewUrl: mp4 preview address
        :type PreviewUrl: str
        """
        self._DownloadTaskId = None
        self._ChannelId = None
        self._ChannelName = None
        self._ChannelCode = None
        self._DeviceName = None
        self._DeviceCode = None
        self._Status = None
        self._VideoTimeSection = None
        self._Scale = None
        self._DownloadTime = None
        self._VideoSize = None
        self._StartTime = None
        self._EndTime = None
        self._FileDownloadUrl = None
        self._FailedReason = None
        self._Expire = None
        self._PreviewUrl = None

    @property
    def DownloadTaskId(self):
        r"""Download task ID
        :rtype: str
        """
        return self._DownloadTaskId

    @DownloadTaskId.setter
    def DownloadTaskId(self, DownloadTaskId):
        self._DownloadTaskId = DownloadTaskId

    @property
    def ChannelId(self):
        r"""Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        r"""Channel name
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ChannelCode(self):
        r"""Channel encoding
        :rtype: str
        """
        return self._ChannelCode

    @ChannelCode.setter
    def ChannelCode(self, ChannelCode):
        self._ChannelCode = ChannelCode

    @property
    def DeviceName(self):
        r"""Device name.
        :rtype: str
        """
        return self._DeviceName

    @DeviceName.setter
    def DeviceName(self, DeviceName):
        self._DeviceName = DeviceName

    @property
    def DeviceCode(self):
        r"""Device code
        :rtype: str
        """
        return self._DeviceCode

    @DeviceCode.setter
    def DeviceCode(self, DeviceCode):
        self._DeviceCode = DeviceCode

    @property
    def Status(self):
        r"""Task status (0: pending; 1: executing; 2: task complete;
3: Task failure)
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VideoTimeSection(self):
        r"""Download the recording time period
        :rtype: str
        """
        return self._VideoTimeSection

    @VideoTimeSection.setter
    def VideoTimeSection(self, VideoTimeSection):
        self._VideoTimeSection = VideoTimeSection

    @property
    def Scale(self):
        r"""Playback speed
        :rtype: int
        """
        return self._Scale

    @Scale.setter
    def Scale(self, Scale):
        self._Scale = Scale

    @property
    def DownloadTime(self):
        r"""Download duration.
        :rtype: int
        """
        return self._DownloadTime

    @DownloadTime.setter
    def DownloadTime(self, DownloadTime):
        self._DownloadTime = DownloadTime

    @property
    def VideoSize(self):
        r"""Video recording size
        :rtype: int
        """
        return self._VideoSize

    @VideoSize.setter
    def VideoSize(self, VideoSize):
        self._VideoSize = VideoSize

    @property
    def StartTime(self):
        r"""Task start time
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""Task end time
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FileDownloadUrl(self):
        r"""File download address
        :rtype: str
        """
        return self._FileDownloadUrl

    @FileDownloadUrl.setter
    def FileDownloadUrl(self, FileDownloadUrl):
        self._FileDownloadUrl = FileDownloadUrl

    @property
    def FailedReason(self):
        r"""Reason for failure
        :rtype: str
        """
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def Expire(self):
        r"""Lifecycle rule, number of days in hot storage
        :rtype: int
        """
        return self._Expire

    @Expire.setter
    def Expire(self, Expire):
        self._Expire = Expire

    @property
    def PreviewUrl(self):
        r"""mp4 preview address
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl


    def _deserialize(self, params):
        self._DownloadTaskId = params.get("DownloadTaskId")
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._ChannelCode = params.get("ChannelCode")
        self._DeviceName = params.get("DeviceName")
        self._DeviceCode = params.get("DeviceCode")
        self._Status = params.get("Status")
        self._VideoTimeSection = params.get("VideoTimeSection")
        self._Scale = params.get("Scale")
        self._DownloadTime = params.get("DownloadTime")
        self._VideoSize = params.get("VideoSize")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._FileDownloadUrl = params.get("FileDownloadUrl")
        self._FailedReason = params.get("FailedReason")
        self._Expire = params.get("Expire")
        self._PreviewUrl = params.get("PreviewUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoDownloadTaskData(AbstractModel):
    r"""Recording download task data structure

    """

    def __init__(self):
        r"""
        :param _DownloadTaskId: Download task ID
        :type DownloadTaskId: str
        """
        self._DownloadTaskId = None

    @property
    def DownloadTaskId(self):
        r"""Download task ID
        :rtype: str
        """
        return self._DownloadTaskId

    @DownloadTaskId.setter
    def DownloadTaskId(self, DownloadTaskId):
        self._DownloadTaskId = DownloadTaskId


    def _deserialize(self, params):
        self._DownloadTaskId = params.get("DownloadTaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSceneInfo(AbstractModel):
    r"""Video scene configuration (reservation)

    """

    def __init__(self):
        r"""
        :param _Interval: <p>Analysis interval (seconds): trigger an analysis every few seconds (sliding step length)</p>
        :type Interval: int
        :param _Duration: <p>Analysis segment duration (seconds): length of the video window fed into the model at a time, range [5, 12800]</p>
        :type Duration: int
        :param _Fps: <p>Frame sampling rate. Default value: 1. Value range: [0.1, 1]. One frame is sampled every 1/Fps seconds and sent to the model.</p>
        :type Fps: float
        """
        self._Interval = None
        self._Duration = None
        self._Fps = None

    @property
    def Interval(self):
        r"""<p>Analysis interval (seconds): trigger an analysis every few seconds (sliding step length)</p>
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Duration(self):
        r"""<p>Analysis segment duration (seconds): length of the video window fed into the model at a time, range [5, 12800]</p>
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def Fps(self):
        r"""<p>Frame sampling rate. Default value: 1. Value range: [0.1, 1]. One frame is sampled every 1/Fps seconds and sent to the model.</p>
        :rtype: float
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        self._Duration = params.get("Duration")
        self._Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSnapshotConfigInfo(AbstractModel):
    r"""Screenshot configuration message

    """

    def __init__(self):
        r"""
        :param _ConfigId: <p>Screenshot configuration Id</p>
        :type ConfigId: str
        :param _TemplateId: <p>Screenshot template Id</p>
        :type TemplateId: str
        :param _Name: <p>Screenshot configuration name</p>
        :type Name: str
        :param _Type: <p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :type Type: int
        :param _FileExpires: <p>Image storage days</p><p>Unit: days</p>
        :type FileExpires: int
        :param _Callback: <p>Callback configuration</p>
        :type Callback: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        :param _CreateTime: <p>Creation time.</p>
        :type CreateTime: str
        :param _UpdateTime: <p>Last update time</p>
        :type UpdateTime: str
        """
        self._ConfigId = None
        self._TemplateId = None
        self._Name = None
        self._Type = None
        self._FileExpires = None
        self._Callback = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ConfigId(self):
        r"""<p>Screenshot configuration Id</p>
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def TemplateId(self):
        r"""<p>Screenshot template Id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        r"""<p>Screenshot configuration name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FileExpires(self):
        r"""<p>Image storage days</p><p>Unit: days</p>
        :rtype: int
        """
        return self._FileExpires

    @FileExpires.setter
    def FileExpires(self, FileExpires):
        self._FileExpires = FileExpires

    @property
    def Callback(self):
        r"""<p>Callback configuration</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.CallbackURL`
        """
        return self._Callback

    @Callback.setter
    def Callback(self, Callback):
        self._Callback = Callback

    @property
    def CreateTime(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>Last update time</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ConfigId = params.get("ConfigId")
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._FileExpires = params.get("FileExpires")
        if params.get("Callback") is not None:
            self._Callback = CallbackURL()
            self._Callback._deserialize(params.get("Callback"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSnapshotTemplateInfo(AbstractModel):
    r"""Screenshot template information

    """

    def __init__(self):
        r"""
        :param _TemplateId: <p>Screenshot template Id</p>
        :type TemplateId: str
        :param _Name: <p>Screenshot template name</p>
        :type Name: str
        :param _Type: <p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :type Type: int
        :param _Interval: <p>Frame capturing frequency</p>
        :type Interval: int
        :param _MultiMode: <p>Multiple mode</p>
        :type MultiMode: :class:`tencentcloud.iss.v20230517.models.MultiVideoSnapshotMode`
        :param _Times: <p>Effective period</p>
        :type Times: list of EffectiveTime
        :param _RelatedConfigCount: <p>Number of configurations associated with the template</p>
        :type RelatedConfigCount: int
        :param _CreateTime: <p>Creation time.</p>
        :type CreateTime: str
        :param _UpdateTime: <p>Last update time</p>
        :type UpdateTime: str
        """
        self._TemplateId = None
        self._Name = None
        self._Type = None
        self._Interval = None
        self._MultiMode = None
        self._Times = None
        self._RelatedConfigCount = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def TemplateId(self):
        r"""<p>Screenshot template Id</p>
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        r"""<p>Screenshot template name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>Screenshot type</p><p>Enumeration values:</p><ul><li>1: Real-time frame capture</li><li>2: Low frequency frame capture</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Interval(self):
        r"""<p>Frame capturing frequency</p>
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def MultiMode(self):
        r"""<p>Multiple mode</p>
        :rtype: :class:`tencentcloud.iss.v20230517.models.MultiVideoSnapshotMode`
        """
        return self._MultiMode

    @MultiMode.setter
    def MultiMode(self, MultiMode):
        self._MultiMode = MultiMode

    @property
    def Times(self):
        r"""<p>Effective period</p>
        :rtype: list of EffectiveTime
        """
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times

    @property
    def RelatedConfigCount(self):
        r"""<p>Number of configurations associated with the template</p>
        :rtype: int
        """
        return self._RelatedConfigCount

    @RelatedConfigCount.setter
    def RelatedConfigCount(self, RelatedConfigCount):
        self._RelatedConfigCount = RelatedConfigCount

    @property
    def CreateTime(self):
        r"""<p>Creation time.</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>Last update time</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Interval = params.get("Interval")
        if params.get("MultiMode") is not None:
            self._MultiMode = MultiVideoSnapshotMode()
            self._MultiMode._deserialize(params.get("MultiMode"))
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = EffectiveTime()
                obj._deserialize(item)
                self._Times.append(obj)
        self._RelatedConfigCount = params.get("RelatedConfigCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        