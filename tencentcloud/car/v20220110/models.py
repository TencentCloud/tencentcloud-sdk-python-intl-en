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
        :param UserIp: The user’s IP address.
        :type UserIp: str
        :param ProjectId: The project ID.
        :type ProjectId: str
        :param ApplicationVersionId: The application version ID.
        :type ApplicationVersionId: str
        """
        self.UserId = None
        self.UserIp = None
        self.ProjectId = None
        self.ApplicationVersionId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserIp = params.get("UserIp")
        self.ProjectId = params.get("ProjectId")
        self.ApplicationVersionId = params.get("ApplicationVersionId")
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
        :param UserIp: The user’s IP address.
        :type UserIp: str
        :param ClientSession: The client-side session data, which is obtained from the SDK.
        :type ClientSession: str
        :param RunMode: The on-cloud running mode.
`RunWithoutClient`: Keep the application running on the cloud even when there are no client connections.
Empty string (default): Keep the application running on the cloud only when there are client connections.
        :type RunMode: str
        """
        self.UserId = None
        self.UserIp = None
        self.ClientSession = None
        self.RunMode = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserIp = params.get("UserIp")
        self.ClientSession = params.get("ClientSession")
        self.RunMode = params.get("RunMode")
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