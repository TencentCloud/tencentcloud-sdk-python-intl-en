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


class ApplyConcurrentRequest(AbstractModel):
    """ApplyConcurrent request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: The user’s unique ID. Tencent Cloud does not parse the ID. You need to manage your own user IDs. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        :param _UserIp: Public IP of user’s application client, which is used for nearby scheduling.
        :type UserIp: str
        :param _ProjectId: The project ID.
        :type ProjectId: str
        :param _ApplicationVersionId: The application version ID.
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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class CreateSessionRequest(AbstractModel):
    """CreateSession request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: The user’s unique ID. Tencent Cloud does not parse the ID. You need to manage your own user IDs. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        :param _UserIp: Public IP of user’s application client, which is used for nearby scheduling.
        :type UserIp: str
        :param _ClientSession: The client-side session data, which is obtained from the SDK. If `RunMode` is `RunWithoutClient`, this parameter can be null.
        :type ClientSession: str
        :param _RunMode: The on-cloud running mode.
`RunWithoutClient`: Keep the application running on the cloud even when there are no client connections.
Empty string (default): Keep the application running on the cloud only when there are client connections.
        :type RunMode: str
        :param _ApplicationParameters: Application startup parameter.
If the user requests a multi-application project or a prelaunch-disabled single-application project, this parameter takes effect.
If the user requests a prelaunch-enabled single-application project, this parameter is invalid.
        :type ApplicationParameters: str
        :param _HostUserId: The user ID of the host in **multi-person interaction** scenarios, which is required.
If the current user is the host, `HostUserId` must be the same as their `UserId`; otherwise, `HostUserId` should be the host's `UserId`.
        :type HostUserId: str
        :param _Role: The role in **multi-person interaction** scenarios. Valid values:
`Player`: A user who can operate an application by using a keyboard and mouse
`Viewer`: A user who can only watch the video in the room but cannot operate the application
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
        :param _ServerSession: The server-side session data, which is returned to the SDK.
        :type ServerSession: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class DestroySessionRequest(AbstractModel):
    """DestroySession request structure.

    """

    def __init__(self):
        r"""
        :param _UserId: The user’s unique ID. Tencent Cloud does not parse the ID. You need to manage your own user IDs. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
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
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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