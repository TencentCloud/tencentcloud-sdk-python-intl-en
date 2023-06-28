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
        :param UserId: The user’s unique ID. Tencent Cloud does not parse the ID. You need to manage your own user IDs. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        :param UserIp: Public IP of user’s application client, which is used for nearby scheduling.
        :type UserIp: str
        :param ProjectId: The project ID.
        :type ProjectId: str
        :param ApplicationVersionId: The application version ID.
        :type ApplicationVersionId: str
        :param ApplicationId: Application ID, which is used only by the multi-application project to specify applications. For a single-application project, this parameter is ignored, and the application bound to the project will be used.
        :type ApplicationId: str
        """
        self.UserId = None
        self.UserIp = None
        self.ProjectId = None
        self.ApplicationVersionId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserIp = params.get("UserIp")
        self.ProjectId = params.get("ProjectId")
        self.ApplicationVersionId = params.get("ApplicationVersionId")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyConcurrentResponse(AbstractModel):
    """ApplyConcurrent response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSessionRequest(AbstractModel):
    """CreateSession request structure.

    """

    def __init__(self):
        r"""
        :param UserId: The user’s unique ID. Tencent Cloud does not parse the ID. You need to manage your own user IDs. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        :param UserIp: Public IP of user’s application client, which is used for nearby scheduling.
        :type UserIp: str
        :param ClientSession: The client-side session data, which is obtained from the SDK. If `RunMode` is `RunWithoutClient`, this parameter can be null.
        :type ClientSession: str
        :param RunMode: The on-cloud running mode.
`RunWithoutClient`: Keep the application running on the cloud even when there are no client connections.
Empty string (default): Keep the application running on the cloud only when there are client connections.
        :type RunMode: str
        :param ApplicationParameters: Application startup parameter.
If the user requests a multi-application project or a prelaunch-disabled single-application project, this parameter takes effect.
If the user requests a prelaunch-enabled single-application project, this parameter is invalid.
        :type ApplicationParameters: str
        :param HostUserId: The user ID of the host in **multi-person interaction** scenarios, which is required.
If the current user is the host, `HostUserId` must be the same as their `UserId`; otherwise, `HostUserId` should be the host's `UserId`.
        :type HostUserId: str
        :param Role: The role in **multi-person interaction** scenarios. Valid values:
`Player`: A user who can operate an application by using a keyboard and mouse
`Viewer`: A user who can only watch the video in the room but cannot operate the application
        :type Role: str
        """
        self.UserId = None
        self.UserIp = None
        self.ClientSession = None
        self.RunMode = None
        self.ApplicationParameters = None
        self.HostUserId = None
        self.Role = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserIp = params.get("UserIp")
        self.ClientSession = params.get("ClientSession")
        self.RunMode = params.get("RunMode")
        self.ApplicationParameters = params.get("ApplicationParameters")
        self.HostUserId = params.get("HostUserId")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSessionResponse(AbstractModel):
    """CreateSession response structure.

    """

    def __init__(self):
        r"""
        :param ServerSession: The server-side session data, which is returned to the SDK.
        :type ServerSession: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServerSession = params.get("ServerSession")
        self.RequestId = params.get("RequestId")


class DestroySessionRequest(AbstractModel):
    """DestroySession request structure.

    """

    def __init__(self):
        r"""
        :param UserId: The user’s unique ID. Tencent Cloud does not parse the ID. You need to manage your own user IDs. Based on your needs, you can either define unique IDs for users or use timestamps to generate random IDs. Make sure the same ID is used when a user reconnects to your application.
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroySessionResponse(AbstractModel):
    """DestroySession response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")