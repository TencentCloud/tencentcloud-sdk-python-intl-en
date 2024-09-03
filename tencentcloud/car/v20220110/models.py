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


class ApplicationBaseInfo(AbstractModel):
    """Application basic data.

    """

    def __init__(self):
        r"""
        :param _WindowUseType: Application window usage mode (ApplicationDesktop: Captures the entire desktop; ApplicationWindow: Captures only the application window).
        :type WindowUseType: str
        :param _WindowName: Application window name.
        :type WindowName: str
        :param _WindowClassName: Application window class name.
        :type WindowClassName: str
        :param _WindowCaptureMode: Application window capture mode (HOOK: default mode; DDA_CUT: compatible mode).
        :type WindowCaptureMode: str
        """
        self._WindowUseType = None
        self._WindowName = None
        self._WindowClassName = None
        self._WindowCaptureMode = None

    @property
    def WindowUseType(self):
        return self._WindowUseType

    @WindowUseType.setter
    def WindowUseType(self, WindowUseType):
        self._WindowUseType = WindowUseType

    @property
    def WindowName(self):
        return self._WindowName

    @WindowName.setter
    def WindowName(self, WindowName):
        self._WindowName = WindowName

    @property
    def WindowClassName(self):
        return self._WindowClassName

    @WindowClassName.setter
    def WindowClassName(self, WindowClassName):
        self._WindowClassName = WindowClassName

    @property
    def WindowCaptureMode(self):
        return self._WindowCaptureMode

    @WindowCaptureMode.setter
    def WindowCaptureMode(self, WindowCaptureMode):
        self._WindowCaptureMode = WindowCaptureMode


    def _deserialize(self, params):
        self._WindowUseType = params.get("WindowUseType")
        self._WindowName = params.get("WindowName")
        self._WindowClassName = params.get("WindowClassName")
        self._WindowCaptureMode = params.get("WindowCaptureMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConcurrentRequest(AbstractModel):
    """ApplyConcurrent request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Unique user ID, which is customized by you and is not parsed by CAR. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        :param _UserIp: Public IP address of the user's client, which is used for nearby scheduling.
        :type UserIp: str
        :param _ProjectId: Project ID.
        :type ProjectId: str
        :param _ApplicationVersionId: Application version ID. If the application of the current version is requested, you do not need to fill in this field. If the application of the other versions is requested, you need to specify the version through this field.
        :type ApplicationVersionId: str
        :param _ApplicationId: Application ID, which is used only by the multi-application project to specify applications. For a single-application project, this parameter is ignored, and the application bound to the project will be used.
        :type ApplicationId: str
        """
        self._UserId = None
        self._UserIp = None
        self._ProjectId = None
        self._ApplicationVersionId = None
        self._ApplicationId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ApplicationVersionId(self):
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserIp = params.get("UserIp")
        self._ProjectId = params.get("ProjectId")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConcurrentResponse(AbstractModel):
    """ApplyConcurrent response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateApplicationRequest(AbstractModel):
    """CreateApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationName: Application name.
        :type ApplicationName: str
        :param _ApplicationType: Application type (Application3D: cloud 3D; ApplicationXR: cloud XR; ApplicationAPK: cloud APK).
        :type ApplicationType: str
        """
        self._ApplicationName = None
        self._ApplicationType = None

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType


    def _deserialize(self, params):
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationType = params.get("ApplicationType")
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
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ApplicationId = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class CreateApplicationSnapshotRequest(AbstractModel):
    """CreateApplicationSnapshot request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationDownloadUrl: Application download address (if the version is created by file upload, this parameter is an empty string).
        :type ApplicationDownloadUrl: str
        """
        self._ApplicationId = None
        self._ApplicationDownloadUrl = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationDownloadUrl(self):
        return self._ApplicationDownloadUrl

    @ApplicationDownloadUrl.setter
    def ApplicationDownloadUrl(self, ApplicationDownloadUrl):
        self._ApplicationDownloadUrl = ApplicationDownloadUrl


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationDownloadUrl = params.get("ApplicationDownloadUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationSnapshotResponse(AbstractModel):
    """CreateApplicationSnapshot response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateApplicationVersionRequest(AbstractModel):
    """CreateApplicationVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationFileName: Application file name (desktop applications should be files in zip/rar/7z format, and mobile applications should be files in apk format).
        :type ApplicationFileName: str
        :param _ApplicationVersionRegions: Region for application version distribution.
        :type ApplicationVersionRegions: list of str
        :param _ApplicationVersionUpdateMode: Application update method.
        :type ApplicationVersionUpdateMode: str
        """
        self._ApplicationId = None
        self._ApplicationFileName = None
        self._ApplicationVersionRegions = None
        self._ApplicationVersionUpdateMode = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationFileName(self):
        return self._ApplicationFileName

    @ApplicationFileName.setter
    def ApplicationFileName(self, ApplicationFileName):
        self._ApplicationFileName = ApplicationFileName

    @property
    def ApplicationVersionRegions(self):
        return self._ApplicationVersionRegions

    @ApplicationVersionRegions.setter
    def ApplicationVersionRegions(self, ApplicationVersionRegions):
        self._ApplicationVersionRegions = ApplicationVersionRegions

    @property
    def ApplicationVersionUpdateMode(self):
        return self._ApplicationVersionUpdateMode

    @ApplicationVersionUpdateMode.setter
    def ApplicationVersionUpdateMode(self, ApplicationVersionUpdateMode):
        self._ApplicationVersionUpdateMode = ApplicationVersionUpdateMode


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationFileName = params.get("ApplicationFileName")
        self._ApplicationVersionRegions = params.get("ApplicationVersionRegions")
        self._ApplicationVersionUpdateMode = params.get("ApplicationVersionUpdateMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationVersionResponse(AbstractModel):
    """CreateApplicationVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Version: Application version data (new).
        :type Version: :class:`tencentcloud.car.v20220110.models.UserApplicationVersion`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Version") is not None:
            self._Version = UserApplicationVersion()
            self._Version._deserialize(params.get("Version"))
        self._RequestId = params.get("RequestId")


class CreateSessionRequest(AbstractModel):
    """CreateSession request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Unique user ID, which is customized by you and is not parsed by CAR. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        :param _UserIp: Public IP address of the user's client, which is used for nearby scheduling.
        :type UserIp: str
        :param _ClientSession: Client-side session information, which is obtained from the SDK. If `RunMode` is `RunWithoutClient`, this parameter can be empty.
        :type ClientSession: str
        :param _RunMode: On-cloud running mode.RunWithoutClient: Keeps the application running on the cloud even when there are no client connections.Empty string (default): Keeps the application running on the cloud only when there are client connections.
        :type RunMode: str
        :param _ApplicationParameters: Application startup parameters.This parameter is effective for multi-application projects.
This parameter is effective for single-application projects with prelaunch disabled.This parameter is ineffective for single-application projects with prelaunch enabled.
Note: When this parameter is effective, it will be appended to the startup parameters of application or project configuration in the console.
For example, for a single-application project with prelaunch disabled, if its startup parameter `bar` is `0` for project configuration in the console and the `ApplicationParameters` parameter `foo` is `1`, the actual application startup parameters will be `bar=0 and foo=1`.
        :type ApplicationParameters: str
        :param _HostUserId: [Multi-person Interaction] Homeowner's user ID, which is required in multi-person interaction mode.
If the user is the homeowner, HostUserID must be the same as UserID.
If the user is not the homeowner, HostUserID must be the homeowner's HostUserID.
        :type HostUserId: str
        :param _Role: [Multi-person Interaction] Role.
Player: a user who can operate the application via keyboard, mouse, etc.
Viewer: a user who can only watch the video in the room but cannot operate the application.
        :type Role: str
        """
        self._UserId = None
        self._UserIp = None
        self._ClientSession = None
        self._RunMode = None
        self._ApplicationParameters = None
        self._HostUserId = None
        self._Role = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserIp(self):
        return self._UserIp

    @UserIp.setter
    def UserIp(self, UserIp):
        self._UserIp = UserIp

    @property
    def ClientSession(self):
        return self._ClientSession

    @ClientSession.setter
    def ClientSession(self, ClientSession):
        self._ClientSession = ClientSession

    @property
    def RunMode(self):
        return self._RunMode

    @RunMode.setter
    def RunMode(self, RunMode):
        self._RunMode = RunMode

    @property
    def ApplicationParameters(self):
        return self._ApplicationParameters

    @ApplicationParameters.setter
    def ApplicationParameters(self, ApplicationParameters):
        self._ApplicationParameters = ApplicationParameters

    @property
    def HostUserId(self):
        return self._HostUserId

    @HostUserId.setter
    def HostUserId(self, HostUserId):
        self._HostUserId = HostUserId

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserIp = params.get("UserIp")
        self._ClientSession = params.get("ClientSession")
        self._RunMode = params.get("RunMode")
        self._ApplicationParameters = params.get("ApplicationParameters")
        self._HostUserId = params.get("HostUserId")
        self._Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSessionResponse(AbstractModel):
    """CreateSession response structure.

    """

    def __init__(self):
        r"""
        :param _ServerSession: Server-side session information, which is returned to the SDK.
        :type ServerSession: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ServerSession = None
        self._RequestId = None

    @property
    def ServerSession(self):
        return self._ServerSession

    @ServerSession.setter
    def ServerSession(self, ServerSession):
        self._ServerSession = ServerSession

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServerSession = params.get("ServerSession")
        self._RequestId = params.get("RequestId")


class DeleteApplicationRequest(AbstractModel):
    """DeleteApplication request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        """
        self._ApplicationId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteApplicationVersionRequest(AbstractModel):
    """DeleteApplicationVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationVersionId: Application version ID.
        :type ApplicationVersionId: str
        """
        self._ApplicationId = None
        self._ApplicationVersionId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationVersionId(self):
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationVersionResponse(AbstractModel):
    """DeleteApplicationVersion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeApplicationFileInfoRequest(AbstractModel):
    """DescribeApplicationFileInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _FilePathList: Application file path list.
        :type FilePathList: list of str
        """
        self._ApplicationId = None
        self._FilePathList = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def FilePathList(self):
        return self._FilePathList

    @FilePathList.setter
    def FilePathList(self, FilePathList):
        self._FilePathList = FilePathList


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._FilePathList = params.get("FilePathList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationFileInfoResponse(AbstractModel):
    """DescribeApplicationFileInfo response structure.

    """

    def __init__(self):
        r"""
        :param _FileInfoList: Application file data list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileInfoList: list of UserApplicationFileInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._FileInfoList = None
        self._RequestId = None

    @property
    def FileInfoList(self):
        return self._FileInfoList

    @FileInfoList.setter
    def FileInfoList(self, FileInfoList):
        self._FileInfoList = FileInfoList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FileInfoList") is not None:
            self._FileInfoList = []
            for item in params.get("FileInfoList"):
                obj = UserApplicationFileInfo()
                obj._deserialize(item)
                self._FileInfoList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationListRequest(AbstractModel):
    """DescribeApplicationList request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Application list offset.
        :type Offset: int
        :param _Limit: Application quantity limit.
        :type Limit: int
        :param _Filters: Filter criteria.
        :type Filters: list of Filter
        :param _ApplicationCategory: Application category (DESKTOP: desktop; MOBILE: mobile).
        :type ApplicationCategory: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ApplicationCategory = None

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
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ApplicationCategory(self):
        return self._ApplicationCategory

    @ApplicationCategory.setter
    def ApplicationCategory(self, ApplicationCategory):
        self._ApplicationCategory = ApplicationCategory


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ApplicationCategory = params.get("ApplicationCategory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationListResponse(AbstractModel):
    """DescribeApplicationList response structure.

    """

    def __init__(self):
        r"""
        :param _UserApplicationList: Application list information.
        :type UserApplicationList: list of UserApplicationInfo
        :param _ApplicationTotal: Total number of applications.
        :type ApplicationTotal: int
        :param _UserMobileApplicationList: Mobile application list information.
        :type UserMobileApplicationList: list of UserMobileApplicationInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UserApplicationList = None
        self._ApplicationTotal = None
        self._UserMobileApplicationList = None
        self._RequestId = None

    @property
    def UserApplicationList(self):
        return self._UserApplicationList

    @UserApplicationList.setter
    def UserApplicationList(self, UserApplicationList):
        self._UserApplicationList = UserApplicationList

    @property
    def ApplicationTotal(self):
        return self._ApplicationTotal

    @ApplicationTotal.setter
    def ApplicationTotal(self, ApplicationTotal):
        self._ApplicationTotal = ApplicationTotal

    @property
    def UserMobileApplicationList(self):
        return self._UserMobileApplicationList

    @UserMobileApplicationList.setter
    def UserMobileApplicationList(self, UserMobileApplicationList):
        self._UserMobileApplicationList = UserMobileApplicationList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UserApplicationList") is not None:
            self._UserApplicationList = []
            for item in params.get("UserApplicationList"):
                obj = UserApplicationInfo()
                obj._deserialize(item)
                self._UserApplicationList.append(obj)
        self._ApplicationTotal = params.get("ApplicationTotal")
        if params.get("UserMobileApplicationList") is not None:
            self._UserMobileApplicationList = []
            for item in params.get("UserMobileApplicationList"):
                obj = UserMobileApplicationInfo()
                obj._deserialize(item)
                self._UserMobileApplicationList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationPathListRequest(AbstractModel):
    """DescribeApplicationPathList request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Cloud application ID.
        :type ApplicationId: str
        :param _ApplicationVersionId: Cloud application version ID.
        :type ApplicationVersionId: str
        """
        self._ApplicationId = None
        self._ApplicationVersionId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationVersionId(self):
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationPathListResponse(AbstractModel):
    """DescribeApplicationPathList response structure.

    """

    def __init__(self):
        r"""
        :param _PathList: Application .exe file path list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PathList: list of str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PathList = None
        self._RequestId = None

    @property
    def PathList(self):
        return self._PathList

    @PathList.setter
    def PathList(self, PathList):
        self._PathList = PathList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PathList = params.get("PathList")
        self._RequestId = params.get("RequestId")


class DescribeApplicationStatusRequest(AbstractModel):
    """DescribeApplicationStatus request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationIdList: Application ID list.
        :type ApplicationIdList: list of str
        """
        self._ApplicationIdList = None

    @property
    def ApplicationIdList(self):
        return self._ApplicationIdList

    @ApplicationIdList.setter
    def ApplicationIdList(self, ApplicationIdList):
        self._ApplicationIdList = ApplicationIdList


    def _deserialize(self, params):
        self._ApplicationIdList = params.get("ApplicationIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationStatusResponse(AbstractModel):
    """DescribeApplicationStatus response structure.

    """

    def __init__(self):
        r"""
        :param _StatusList: Application status list.
        :type StatusList: list of UserApplicationStatus
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StatusList = None
        self._RequestId = None

    @property
    def StatusList(self):
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StatusList") is not None:
            self._StatusList = []
            for item in params.get("StatusList"):
                obj = UserApplicationStatus()
                obj._deserialize(item)
                self._StatusList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeApplicationVersionRequest(AbstractModel):
    """DescribeApplicationVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application version ID.
        :type ApplicationId: str
        """
        self._ApplicationId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationVersionResponse(AbstractModel):
    """DescribeApplicationVersion response structure.

    """

    def __init__(self):
        r"""
        :param _Versions: List of application versions.
        :type Versions: list of UserApplicationVersion
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Versions = None
        self._RequestId = None

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = UserApplicationVersion()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConcurrentCountRequest(AbstractModel):
    """DescribeConcurrentCount request structure.

    """

    def __init__(self):
        r"""
        :param _ProjectId: Project ID.
        :type ProjectId: str
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
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
        


class DescribeConcurrentCountResponse(AbstractModel):
    """DescribeConcurrentCount response structure.

    """

    def __init__(self):
        r"""
        :param _Total: Total number of concurrencies.
        :type Total: int
        :param _Running: The number of concurrent executions, including all non-idle concurrent executions such as those in prelaunch, connected, waiting for reconnection, and to be cleaned up or recovered. Therefore, refreshing projects or disconnecting user connections with concurrency packages will affect this value.
        :type Running: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._Running = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Running(self):
        return self._Running

    @Running.setter
    def Running(self, Running):
        self._Running = Running

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Running = params.get("Running")
        self._RequestId = params.get("RequestId")


class DescribeCosCredentialRequest(AbstractModel):
    """DescribeCosCredential request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationFileName: Application file name (the file must be a compressed package with a zip/rar/7z file name extension).
        :type ApplicationFileName: str
        """
        self._ApplicationId = None
        self._ApplicationFileName = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationFileName(self):
        return self._ApplicationFileName

    @ApplicationFileName.setter
    def ApplicationFileName(self, ApplicationFileName):
        self._ApplicationFileName = ApplicationFileName


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationFileName = params.get("ApplicationFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCosCredentialResponse(AbstractModel):
    """DescribeCosCredential response structure.

    """

    def __init__(self):
        r"""
        :param _SecretID: Cos SecretID
        :type SecretID: str
        :param _SecretKey: Cos SecretKey
        :type SecretKey: str
        :param _SessionToken: Cos SessionToken
        :type SessionToken: str
        :param _CosBucket: Cos Bucket
        :type CosBucket: str
        :param _CosRegion: Cos Region
        :type CosRegion: str
        :param _Path: COS operation path.
        :type Path: str
        :param _StartTime: Start time of the COS key.
        :type StartTime: int
        :param _ExpiredTime: Expiration time of the COS key.
        :type ExpiredTime: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SecretID = None
        self._SecretKey = None
        self._SessionToken = None
        self._CosBucket = None
        self._CosRegion = None
        self._Path = None
        self._StartTime = None
        self._ExpiredTime = None
        self._RequestId = None

    @property
    def SecretID(self):
        return self._SecretID

    @SecretID.setter
    def SecretID(self, SecretID):
        self._SecretID = SecretID

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SessionToken(self):
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

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
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SecretID = params.get("SecretID")
        self._SecretKey = params.get("SecretKey")
        self._SessionToken = params.get("SessionToken")
        self._CosBucket = params.get("CosBucket")
        self._CosRegion = params.get("CosRegion")
        self._Path = params.get("Path")
        self._StartTime = params.get("StartTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._RequestId = params.get("RequestId")


class DestroySessionRequest(AbstractModel):
    """DestroySession request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Unique user ID, which is customized by you and is not parsed by CAR. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroySessionResponse(AbstractModel):
    """DestroySession response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Query filter criteria.

    """

    def __init__(self):
        r"""
        :param _Name: Filter field name (ApplicationId: application ID; ApplicationName: application name; ApplicationRunStatus: running status; ApplicationUpdateStatus: update status).
        :type Name: str
        :param _Values: Filter value set (When the filter name is ApplicationRunStatus, the values can be [ApplicationDeleting: application deletion in progress; ApplicationCreateFail: application creation failed; ApplicationCreating: application creation in progress; ApplicationRunning: normal running; ApplicationNoConfigured: main execution program path not configured]. When the filter name is ApplicationUpdateStatus, the values can be [ApplicationUpdateCreating: version creation in progress; ApplicationUpdateCreateFail: version creation failed; ApplicationUpdateNoReleased: version to be released; ApplicationUpdateReleased: version release completed; ApplicationUpdateNormal: none]).
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
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
        


class ModifyApplicationBaseInfoRequest(AbstractModel):
    """ModifyApplicationBaseInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationExePath: Application program execution path.
        :type ApplicationExePath: str
        :param _ApplicationInterList: Application process list.
        :type ApplicationInterList: str
        :param _ApplicationBaseInfo: Application basic data.
        :type ApplicationBaseInfo: :class:`tencentcloud.car.v20220110.models.ApplicationBaseInfo`
        :param _ApplicationParams: Application startup parameters.
        :type ApplicationParams: str
        :param _ApplicationName: Application name.
        :type ApplicationName: str
        :param _ApplicationStores: Application repository information list.
        :type ApplicationStores: list of UserApplicationStore
        """
        self._ApplicationId = None
        self._ApplicationExePath = None
        self._ApplicationInterList = None
        self._ApplicationBaseInfo = None
        self._ApplicationParams = None
        self._ApplicationName = None
        self._ApplicationStores = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationExePath(self):
        return self._ApplicationExePath

    @ApplicationExePath.setter
    def ApplicationExePath(self, ApplicationExePath):
        self._ApplicationExePath = ApplicationExePath

    @property
    def ApplicationInterList(self):
        return self._ApplicationInterList

    @ApplicationInterList.setter
    def ApplicationInterList(self, ApplicationInterList):
        self._ApplicationInterList = ApplicationInterList

    @property
    def ApplicationBaseInfo(self):
        return self._ApplicationBaseInfo

    @ApplicationBaseInfo.setter
    def ApplicationBaseInfo(self, ApplicationBaseInfo):
        self._ApplicationBaseInfo = ApplicationBaseInfo

    @property
    def ApplicationParams(self):
        return self._ApplicationParams

    @ApplicationParams.setter
    def ApplicationParams(self, ApplicationParams):
        self._ApplicationParams = ApplicationParams

    @property
    def ApplicationName(self):
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationStores(self):
        return self._ApplicationStores

    @ApplicationStores.setter
    def ApplicationStores(self, ApplicationStores):
        self._ApplicationStores = ApplicationStores


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationExePath = params.get("ApplicationExePath")
        self._ApplicationInterList = params.get("ApplicationInterList")
        if params.get("ApplicationBaseInfo") is not None:
            self._ApplicationBaseInfo = ApplicationBaseInfo()
            self._ApplicationBaseInfo._deserialize(params.get("ApplicationBaseInfo"))
        self._ApplicationParams = params.get("ApplicationParams")
        self._ApplicationName = params.get("ApplicationName")
        if params.get("ApplicationStores") is not None:
            self._ApplicationStores = []
            for item in params.get("ApplicationStores"):
                obj = UserApplicationStore()
                obj._deserialize(item)
                self._ApplicationStores.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationBaseInfoResponse(AbstractModel):
    """ModifyApplicationBaseInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyApplicationVersionRequest(AbstractModel):
    """ModifyApplicationVersion request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationVersionId: Application version ID.
        :type ApplicationVersionId: str
        :param _ApplicationVersionName: Application version name.
        :type ApplicationVersionName: str
        """
        self._ApplicationId = None
        self._ApplicationVersionId = None
        self._ApplicationVersionName = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationVersionId(self):
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def ApplicationVersionName(self):
        return self._ApplicationVersionName

    @ApplicationVersionName.setter
    def ApplicationVersionName(self, ApplicationVersionName):
        self._ApplicationVersionName = ApplicationVersionName


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        self._ApplicationVersionName = params.get("ApplicationVersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationVersionResponse(AbstractModel):
    """ModifyApplicationVersion response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyMobileApplicationInfoRequest(AbstractModel):
    """ModifyMobileApplicationInfo request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationName: Application name.
        :type ApplicationName: str
        """
        self._ApplicationId = None
        self._ApplicationName = None

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


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMobileApplicationInfoResponse(AbstractModel):
    """ModifyMobileApplicationInfo response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class SetApplicationVersionOnlineRequest(AbstractModel):
    """SetApplicationVersionOnline request structure.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationVersionId: Application version ID.
        :type ApplicationVersionId: str
        """
        self._ApplicationId = None
        self._ApplicationVersionId = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationVersionId(self):
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetApplicationVersionOnlineResponse(AbstractModel):
    """SetApplicationVersionOnline response structure.

    """

    def __init__(self):
        r"""
        :param _Versions: List of application versions.
        :type Versions: list of UserApplicationVersion
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Versions = None
        self._RequestId = None

    @property
    def Versions(self):
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = UserApplicationVersion()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class StartPublishStreamRequest(AbstractModel):
    """StartPublishStream request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Unique user ID, which is customized by you and is not parsed by CAR. It will be used as the `StreamId` for streaming. For example, if the bound streaming domain is **abc.livepush.myqcloud.com**, the streaming address will be **rtmp://abc.livepush.myqcloud.com/live/UserId?txSecret=xxx&txTime=xxx**.
        :type UserId: str
        :param _PublishStreamArgs: Streaming parameter, which is a custom parameter carried during streaming.
        :type PublishStreamArgs: str
        """
        self._UserId = None
        self._PublishStreamArgs = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishStreamArgs(self):
        return self._PublishStreamArgs

    @PublishStreamArgs.setter
    def PublishStreamArgs(self, PublishStreamArgs):
        self._PublishStreamArgs = PublishStreamArgs


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PublishStreamArgs = params.get("PublishStreamArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamResponse(AbstractModel):
    """StartPublishStream response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartPublishStreamWithURLRequest(AbstractModel):
    """StartPublishStreamWithURL request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Unique user ID, which is customized by you and is not parsed by CAR.
        :type UserId: str
        :param _PublishStreamURL: Streaming address. Only RTMP is supported for streaming currently.
        :type PublishStreamURL: str
        """
        self._UserId = None
        self._PublishStreamURL = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PublishStreamURL(self):
        return self._PublishStreamURL

    @PublishStreamURL.setter
    def PublishStreamURL(self, PublishStreamURL):
        self._PublishStreamURL = PublishStreamURL


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._PublishStreamURL = params.get("PublishStreamURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishStreamWithURLResponse(AbstractModel):
    """StartPublishStreamWithURL response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopPublishStreamRequest(AbstractModel):
    """StopPublishStream request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: Unique user ID, which is customized by you and is not parsed by CAR. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        """
        self._UserId = None

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishStreamResponse(AbstractModel):
    """StopPublishStream response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UserApplicationFileInfo(AbstractModel):
    """Application file information.

    """

    def __init__(self):
        r"""
        :param _FilePath: Application file path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FilePath: str
        :param _FileState: File status. NO_EXIST: The file does not exist; EXIST: The file exists.
Note: This field may return null, indicating that no valid values can be obtained.
        :type FileState: str
        """
        self._FilePath = None
        self._FileState = None

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileState(self):
        return self._FileState

    @FileState.setter
    def FileState(self, FileState):
        self._FileState = FileState


    def _deserialize(self, params):
        self._FilePath = params.get("FilePath")
        self._FileState = params.get("FileState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserApplicationInfo(AbstractModel):
    """Application data information.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationName: Application name.
        :type ApplicationName: str
        :param _ApplicationType: Application type (cloud 3D: Application3D; cloud XR: ApplicationXR; cloud Web: ApplicationWeb).
        :type ApplicationType: str
        :param _ApplicationExePath: Application program execution path.
        :type ApplicationExePath: str
        :param _ApplicationInterList: Application process list.
        :type ApplicationInterList: str
        :param _ApplicationParams: Application startup parameters.
        :type ApplicationParams: str
        :param _ApplicationRunStatus: Application running status (ApplicationDeleting: application deletion in progress; ApplicationCreateFail: application creation failed; ApplicationCreating: application creation in progress; ApplicationRunning: normal running; ApplicationNoConfigured: main execution program path not configured).
        :type ApplicationRunStatus: str
        :param _ApplicationUpdateStatus: Application update status (ApplicationUpdateCreating: version creation in progress; ApplicationUpdateCreateFail: version creation failed; ApplicationUpdateNoReleased: version to be released; ApplicationUpdateReleased: version release completed; ApplicationUpdateNormal: none).
        :type ApplicationUpdateStatus: str
        :param _ApplicationCreateTime: Application creation time.
        :type ApplicationCreateTime: str
        :param _ApplicationVersions: List of application versions.
        :type ApplicationVersions: list of UserApplicationVersion
        :param _ApplicationBaseInfo: Application basic data.
        :type ApplicationBaseInfo: :class:`tencentcloud.car.v20220110.models.ApplicationBaseInfo`
        :param _ApplicationUpdateProgress: Application update progress.
        :type ApplicationUpdateProgress: int
        :param _ApplicationNature: Application nature (PUBLIC: public application; PRIVATE: user application).
        :type ApplicationNature: str
        :param _ApplicationStores: Application repository list.
        :type ApplicationStores: list of UserApplicationStore
        """
        self._ApplicationId = None
        self._ApplicationName = None
        self._ApplicationType = None
        self._ApplicationExePath = None
        self._ApplicationInterList = None
        self._ApplicationParams = None
        self._ApplicationRunStatus = None
        self._ApplicationUpdateStatus = None
        self._ApplicationCreateTime = None
        self._ApplicationVersions = None
        self._ApplicationBaseInfo = None
        self._ApplicationUpdateProgress = None
        self._ApplicationNature = None
        self._ApplicationStores = None

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
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationExePath(self):
        return self._ApplicationExePath

    @ApplicationExePath.setter
    def ApplicationExePath(self, ApplicationExePath):
        self._ApplicationExePath = ApplicationExePath

    @property
    def ApplicationInterList(self):
        return self._ApplicationInterList

    @ApplicationInterList.setter
    def ApplicationInterList(self, ApplicationInterList):
        self._ApplicationInterList = ApplicationInterList

    @property
    def ApplicationParams(self):
        return self._ApplicationParams

    @ApplicationParams.setter
    def ApplicationParams(self, ApplicationParams):
        self._ApplicationParams = ApplicationParams

    @property
    def ApplicationRunStatus(self):
        return self._ApplicationRunStatus

    @ApplicationRunStatus.setter
    def ApplicationRunStatus(self, ApplicationRunStatus):
        self._ApplicationRunStatus = ApplicationRunStatus

    @property
    def ApplicationUpdateStatus(self):
        return self._ApplicationUpdateStatus

    @ApplicationUpdateStatus.setter
    def ApplicationUpdateStatus(self, ApplicationUpdateStatus):
        self._ApplicationUpdateStatus = ApplicationUpdateStatus

    @property
    def ApplicationCreateTime(self):
        return self._ApplicationCreateTime

    @ApplicationCreateTime.setter
    def ApplicationCreateTime(self, ApplicationCreateTime):
        self._ApplicationCreateTime = ApplicationCreateTime

    @property
    def ApplicationVersions(self):
        return self._ApplicationVersions

    @ApplicationVersions.setter
    def ApplicationVersions(self, ApplicationVersions):
        self._ApplicationVersions = ApplicationVersions

    @property
    def ApplicationBaseInfo(self):
        return self._ApplicationBaseInfo

    @ApplicationBaseInfo.setter
    def ApplicationBaseInfo(self, ApplicationBaseInfo):
        self._ApplicationBaseInfo = ApplicationBaseInfo

    @property
    def ApplicationUpdateProgress(self):
        return self._ApplicationUpdateProgress

    @ApplicationUpdateProgress.setter
    def ApplicationUpdateProgress(self, ApplicationUpdateProgress):
        self._ApplicationUpdateProgress = ApplicationUpdateProgress

    @property
    def ApplicationNature(self):
        return self._ApplicationNature

    @ApplicationNature.setter
    def ApplicationNature(self, ApplicationNature):
        self._ApplicationNature = ApplicationNature

    @property
    def ApplicationStores(self):
        return self._ApplicationStores

    @ApplicationStores.setter
    def ApplicationStores(self, ApplicationStores):
        self._ApplicationStores = ApplicationStores


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationType = params.get("ApplicationType")
        self._ApplicationExePath = params.get("ApplicationExePath")
        self._ApplicationInterList = params.get("ApplicationInterList")
        self._ApplicationParams = params.get("ApplicationParams")
        self._ApplicationRunStatus = params.get("ApplicationRunStatus")
        self._ApplicationUpdateStatus = params.get("ApplicationUpdateStatus")
        self._ApplicationCreateTime = params.get("ApplicationCreateTime")
        if params.get("ApplicationVersions") is not None:
            self._ApplicationVersions = []
            for item in params.get("ApplicationVersions"):
                obj = UserApplicationVersion()
                obj._deserialize(item)
                self._ApplicationVersions.append(obj)
        if params.get("ApplicationBaseInfo") is not None:
            self._ApplicationBaseInfo = ApplicationBaseInfo()
            self._ApplicationBaseInfo._deserialize(params.get("ApplicationBaseInfo"))
        self._ApplicationUpdateProgress = params.get("ApplicationUpdateProgress")
        self._ApplicationNature = params.get("ApplicationNature")
        if params.get("ApplicationStores") is not None:
            self._ApplicationStores = []
            for item in params.get("ApplicationStores"):
                obj = UserApplicationStore()
                obj._deserialize(item)
                self._ApplicationStores.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserApplicationStatus(AbstractModel):
    """Application status information.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationRunStatus: Application running status (ApplicationDeleting: application deletion in progress; ApplicationCreateFail: application creation failed; ApplicationCreating: application creation in progress; ApplicationRunning: normal running; ApplicationNoConfigured: main execution program path not configured; ApplicationNoPackage: no available package).
        :type ApplicationRunStatus: str
        :param _ApplicationUpdateStatus: Application update status (ApplicationUpdateCreating: version creation in progress; ApplicationUpdateCreateFail: version creation failed; ApplicationUpdateNoReleased: version to be released; ApplicationUpdateReleased: version release completed; ApplicationUpdateNormal: none).
        :type ApplicationUpdateStatus: str
        :param _ApplicationUpdateProgress: Application update progress.
        :type ApplicationUpdateProgress: int
        """
        self._ApplicationId = None
        self._ApplicationRunStatus = None
        self._ApplicationUpdateStatus = None
        self._ApplicationUpdateProgress = None

    @property
    def ApplicationId(self):
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationRunStatus(self):
        return self._ApplicationRunStatus

    @ApplicationRunStatus.setter
    def ApplicationRunStatus(self, ApplicationRunStatus):
        self._ApplicationRunStatus = ApplicationRunStatus

    @property
    def ApplicationUpdateStatus(self):
        return self._ApplicationUpdateStatus

    @ApplicationUpdateStatus.setter
    def ApplicationUpdateStatus(self, ApplicationUpdateStatus):
        self._ApplicationUpdateStatus = ApplicationUpdateStatus

    @property
    def ApplicationUpdateProgress(self):
        return self._ApplicationUpdateProgress

    @ApplicationUpdateProgress.setter
    def ApplicationUpdateProgress(self, ApplicationUpdateProgress):
        self._ApplicationUpdateProgress = ApplicationUpdateProgress


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationRunStatus = params.get("ApplicationRunStatus")
        self._ApplicationUpdateStatus = params.get("ApplicationUpdateStatus")
        self._ApplicationUpdateProgress = params.get("ApplicationUpdateProgress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserApplicationStore(AbstractModel):
    """Application repository information.

    """

    def __init__(self):
        r"""
        :param _CosBucket: COS bucket name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosBucket: str
        :param _CosRegion: COS bucket region.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CosRegion: str
        :param _StoreType: Repository type. LOG: application logs; ARCHIVE: application archive.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StoreType: str
        :param _StoreState: Repository status. ON: enabled; OFF: disabled.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StoreState: str
        :param _StorePath: Repository path.
Note: This field may return null, indicating that no valid values can be obtained.
        :type StorePath: str
        """
        self._CosBucket = None
        self._CosRegion = None
        self._StoreType = None
        self._StoreState = None
        self._StorePath = None

    @property
    def CosBucket(self):
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosRegion(self):
        return self._CosRegion

    @CosRegion.setter
    def CosRegion(self, CosRegion):
        self._CosRegion = CosRegion

    @property
    def StoreType(self):
        return self._StoreType

    @StoreType.setter
    def StoreType(self, StoreType):
        self._StoreType = StoreType

    @property
    def StoreState(self):
        return self._StoreState

    @StoreState.setter
    def StoreState(self, StoreState):
        self._StoreState = StoreState

    @property
    def StorePath(self):
        return self._StorePath

    @StorePath.setter
    def StorePath(self, StorePath):
        self._StorePath = StorePath


    def _deserialize(self, params):
        self._CosBucket = params.get("CosBucket")
        self._CosRegion = params.get("CosRegion")
        self._StoreType = params.get("StoreType")
        self._StoreState = params.get("StoreState")
        self._StorePath = params.get("StorePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserApplicationVersion(AbstractModel):
    """Application version information.

    """

    def __init__(self):
        r"""
        :param _ApplicationVersionId: Application version ID.
        :type ApplicationVersionId: str
        :param _ApplicationVersionSize: Application version size.
        :type ApplicationVersionSize: int
        :param _ApplicationVersionStatus: Application version status (Uploading: uploading; Creating: in creation; CreateFailed: creation failed; Deleting: deleting; Inuse: current version; Normal: to be released; Usable: available).
        :type ApplicationVersionStatus: str
        :param _ApplicationVersionName: Application version name.
        :type ApplicationVersionName: str
        :param _CreateTime: Application version creation time.
        :type CreateTime: str
        :param _ApplicationVersionRegions: Region for application version distribution (
Standard zone:
ap-chinese-mainland: Chinese mainland
na-north-america: North America
eu-frankfurt: Frankfurt
ap-mumbai: Mumbai
ap-tokyo: Tokyo
ap-seoul: Seoul
ap-singapore: Singapore
ap-bangkok: Bangkok
ap-hongkong: Hong Kong (China)
Integration zone:
me-middle-east-fusion: Middle East
na-north-america-fusion: North America
sa-south-america-fusion: South America
ap-tokyo-fusion: Tokyo
ap-seoul-fusion: Seoul
eu-frankfurt-fusion: Frankfurt
ap-singapore-fusion: Singapore
ap-hongkong-fusion: Hong Kong (China)
).
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationVersionRegions: list of str
        :param _ApplicationVersionUpdateMode: Application version update method.
FULL: full update.
INCREMENT: incremental update.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ApplicationVersionUpdateMode: str
        """
        self._ApplicationVersionId = None
        self._ApplicationVersionSize = None
        self._ApplicationVersionStatus = None
        self._ApplicationVersionName = None
        self._CreateTime = None
        self._ApplicationVersionRegions = None
        self._ApplicationVersionUpdateMode = None

    @property
    def ApplicationVersionId(self):
        return self._ApplicationVersionId

    @ApplicationVersionId.setter
    def ApplicationVersionId(self, ApplicationVersionId):
        self._ApplicationVersionId = ApplicationVersionId

    @property
    def ApplicationVersionSize(self):
        return self._ApplicationVersionSize

    @ApplicationVersionSize.setter
    def ApplicationVersionSize(self, ApplicationVersionSize):
        self._ApplicationVersionSize = ApplicationVersionSize

    @property
    def ApplicationVersionStatus(self):
        return self._ApplicationVersionStatus

    @ApplicationVersionStatus.setter
    def ApplicationVersionStatus(self, ApplicationVersionStatus):
        self._ApplicationVersionStatus = ApplicationVersionStatus

    @property
    def ApplicationVersionName(self):
        return self._ApplicationVersionName

    @ApplicationVersionName.setter
    def ApplicationVersionName(self, ApplicationVersionName):
        self._ApplicationVersionName = ApplicationVersionName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ApplicationVersionRegions(self):
        return self._ApplicationVersionRegions

    @ApplicationVersionRegions.setter
    def ApplicationVersionRegions(self, ApplicationVersionRegions):
        self._ApplicationVersionRegions = ApplicationVersionRegions

    @property
    def ApplicationVersionUpdateMode(self):
        return self._ApplicationVersionUpdateMode

    @ApplicationVersionUpdateMode.setter
    def ApplicationVersionUpdateMode(self, ApplicationVersionUpdateMode):
        self._ApplicationVersionUpdateMode = ApplicationVersionUpdateMode


    def _deserialize(self, params):
        self._ApplicationVersionId = params.get("ApplicationVersionId")
        self._ApplicationVersionSize = params.get("ApplicationVersionSize")
        self._ApplicationVersionStatus = params.get("ApplicationVersionStatus")
        self._ApplicationVersionName = params.get("ApplicationVersionName")
        self._CreateTime = params.get("CreateTime")
        self._ApplicationVersionRegions = params.get("ApplicationVersionRegions")
        self._ApplicationVersionUpdateMode = params.get("ApplicationVersionUpdateMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserMobileApplicationInfo(AbstractModel):
    """Mobile application data information.

    """

    def __init__(self):
        r"""
        :param _ApplicationId: Application ID.
        :type ApplicationId: str
        :param _ApplicationName: Application name.
        :type ApplicationName: str
        :param _ApplicationType: Application type (cloud APK: application APK).
        :type ApplicationType: str
        :param _ApplicationRunStatus: Application running status (ApplicationRunning: normal running; ApplicationNoPackage: no available package).
        :type ApplicationRunStatus: str
        :param _ApplicationUpdateStatus: Application update status (ApplicationUpdateCreating: version creation in progress; ApplicationUpdateCreateFail: version creation failed; ApplicationUpdateNoReleased: version to be released; ApplicationUpdateReleased: version release completed; ApplicationUpdateNormal: none).
        :type ApplicationUpdateStatus: str
        :param _ApplicationCreateTime: Application creation time.
        :type ApplicationCreateTime: str
        :param _ApplicationVersions: List of application versions.
        :type ApplicationVersions: list of UserApplicationVersion
        :param _ApplicationNature: Application nature (PUBLIC: public application; PRIVATE: user application).
        :type ApplicationNature: str
        """
        self._ApplicationId = None
        self._ApplicationName = None
        self._ApplicationType = None
        self._ApplicationRunStatus = None
        self._ApplicationUpdateStatus = None
        self._ApplicationCreateTime = None
        self._ApplicationVersions = None
        self._ApplicationNature = None

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
    def ApplicationType(self):
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationRunStatus(self):
        return self._ApplicationRunStatus

    @ApplicationRunStatus.setter
    def ApplicationRunStatus(self, ApplicationRunStatus):
        self._ApplicationRunStatus = ApplicationRunStatus

    @property
    def ApplicationUpdateStatus(self):
        return self._ApplicationUpdateStatus

    @ApplicationUpdateStatus.setter
    def ApplicationUpdateStatus(self, ApplicationUpdateStatus):
        self._ApplicationUpdateStatus = ApplicationUpdateStatus

    @property
    def ApplicationCreateTime(self):
        return self._ApplicationCreateTime

    @ApplicationCreateTime.setter
    def ApplicationCreateTime(self, ApplicationCreateTime):
        self._ApplicationCreateTime = ApplicationCreateTime

    @property
    def ApplicationVersions(self):
        return self._ApplicationVersions

    @ApplicationVersions.setter
    def ApplicationVersions(self, ApplicationVersions):
        self._ApplicationVersions = ApplicationVersions

    @property
    def ApplicationNature(self):
        return self._ApplicationNature

    @ApplicationNature.setter
    def ApplicationNature(self, ApplicationNature):
        self._ApplicationNature = ApplicationNature


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationType = params.get("ApplicationType")
        self._ApplicationRunStatus = params.get("ApplicationRunStatus")
        self._ApplicationUpdateStatus = params.get("ApplicationUpdateStatus")
        self._ApplicationCreateTime = params.get("ApplicationCreateTime")
        if params.get("ApplicationVersions") is not None:
            self._ApplicationVersions = []
            for item in params.get("ApplicationVersions"):
                obj = UserApplicationVersion()
                obj._deserialize(item)
                self._ApplicationVersions.append(obj)
        self._ApplicationNature = params.get("ApplicationNature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        