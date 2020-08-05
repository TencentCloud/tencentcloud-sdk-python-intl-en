# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class ChannelInfo(AbstractModel):
    """Channel information.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param Name: Channel name.
        :type Name: str
        :param Protocol: Channel protocol.
        :type Protocol: str
        :param Points: Channel input and output.
        :type Points: :class:`tencentcloud.mdp.v20200527.models.PointInfo`
        """
        self.Id = None
        self.Name = None
        self.Protocol = None
        self.Points = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Protocol = params.get("Protocol")
        if params.get("Points") is not None:
            self.Points = PointInfo()
            self.Points._deserialize(params.get("Points"))


class CreateMediaPackageChannelEndpointRequest(AbstractModel):
    """CreateMediaPackageChannelEndpoint request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param Name: Channel name.
        :type Name: str
        :param AuthInfo: Authentication information.
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        self.Id = None
        self.Name = None
        self.AuthInfo = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("AuthInfo") is not None:
            self.AuthInfo = EndpointAuthInfo()
            self.AuthInfo._deserialize(params.get("AuthInfo"))


class CreateMediaPackageChannelEndpointResponse(AbstractModel):
    """CreateMediaPackageChannelEndpoint response structure.

    """

    def __init__(self):
        """
        :param Info: The information of the created channel endpoint.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.EndpointInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = EndpointInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class CreateMediaPackageChannelRequest(AbstractModel):
    """CreateMediaPackageChannel request structure.

    """

    def __init__(self):
        """
        :param Name: Channel name.
        :type Name: str
        :param Protocol: Channel protocol. Valid values: HLS, DASH.
        :type Protocol: str
        """
        self.Name = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Protocol = params.get("Protocol")


class CreateMediaPackageChannelResponse(AbstractModel):
    """CreateMediaPackageChannel response structure.

    """

    def __init__(self):
        """
        :param Info: Channel information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.ChannelInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = ChannelInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DeleteMediaPackageChannelEndpointsRequest(AbstractModel):
    """DeleteMediaPackageChannelEndpoints request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param Urls: The list of endpoint URLs.
        :type Urls: list of str
        """
        self.Id = None
        self.Urls = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Urls = params.get("Urls")


class DeleteMediaPackageChannelEndpointsResponse(AbstractModel):
    """DeleteMediaPackageChannelEndpoints response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaPackageChannelsRequest(AbstractModel):
    """DeleteMediaPackageChannels request structure.

    """

    def __init__(self):
        """
        :param Ids: The ID list of channels to be deleted.
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMediaPackageChannelsResponse(AbstractModel):
    """DeleteMediaPackageChannels response structure.

    """

    def __init__(self):
        """
        :param SuccessInfos: The information list of channels that have been deleted.
        :type SuccessInfos: list of ChannelInfo
        :param FailInfos: The information list of channels that failed to be deleted.
        :type FailInfos: list of ChannelInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SuccessInfos = None
        self.FailInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SuccessInfos") is not None:
            self.SuccessInfos = []
            for item in params.get("SuccessInfos"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self.SuccessInfos.append(obj)
        if params.get("FailInfos") is not None:
            self.FailInfos = []
            for item in params.get("FailInfos"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self.FailInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaPackageChannelRequest(AbstractModel):
    """DescribeMediaPackageChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DescribeMediaPackageChannelResponse(AbstractModel):
    """DescribeMediaPackageChannel response structure.

    """

    def __init__(self):
        """
        :param Info: Channel information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.ChannelInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = ChannelInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeMediaPackageChannelsRequest(AbstractModel):
    """DescribeMediaPackageChannels request structure.

    """

    def __init__(self):
        """
        :param PageNum: Page number. Value range: [1, 1000].
        :type PageNum: int
        :param PageSize: The size of each page. Value range: [1, 1000].
        :type PageSize: int
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeMediaPackageChannelsResponse(AbstractModel):
    """DescribeMediaPackageChannels response structure.

    """

    def __init__(self):
        """
        :param Infos: The list of channel outputs.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Infos: list of ChannelInfo
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: The size of each page.
        :type PageSize: int
        :param TotalNum: Total number.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class EndpointAuthInfo(AbstractModel):
    """The authentication information of channel endpoints.

    """

    def __init__(self):
        """
        :param WhiteIpList: The security group allowlist in CIDR format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type WhiteIpList: list of str
        :param BlackIpList: The security group blocklist in CIDR format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BlackIpList: list of str
        :param AuthKey: The authentication key. Its value is same as `X-TENCENT-PACKAGE` set in the HTTP request header.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthKey: str
        """
        self.WhiteIpList = None
        self.BlackIpList = None
        self.AuthKey = None


    def _deserialize(self, params):
        self.WhiteIpList = params.get("WhiteIpList")
        self.BlackIpList = params.get("BlackIpList")
        self.AuthKey = params.get("AuthKey")


class EndpointInfo(AbstractModel):
    """Channel endpoint information.

    """

    def __init__(self):
        """
        :param Name: Endpoint name.
        :type Name: str
        :param Url: Endpoint URL.
        :type Url: str
        :param AuthInfo: Endpoint authentication information.
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        self.Name = None
        self.Url = None
        self.AuthInfo = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Url = params.get("Url")
        if params.get("AuthInfo") is not None:
            self.AuthInfo = EndpointAuthInfo()
            self.AuthInfo._deserialize(params.get("AuthInfo"))


class InputAuthInfo(AbstractModel):
    """Channel input authentication information.

    """

    def __init__(self):
        """
        :param Username: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Username: str
        :param Password: Password.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Password: str
        """
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Password = params.get("Password")


class InputInfo(AbstractModel):
    """Channel input.

    """

    def __init__(self):
        """
        :param Url: Channel input URL.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param AuthInfo: Channel input authentication information.
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.InputAuthInfo`
        """
        self.Url = None
        self.AuthInfo = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("AuthInfo") is not None:
            self.AuthInfo = InputAuthInfo()
            self.AuthInfo._deserialize(params.get("AuthInfo"))


class ModifyMediaPackageChannelEndpointRequest(AbstractModel):
    """ModifyMediaPackageChannelEndpoint request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param Url: Channel endpoint URL.
        :type Url: str
        :param Name: The channel name after modification.
        :type Name: str
        :param AuthInfo: The channel authentication after modification.
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        self.Id = None
        self.Url = None
        self.Name = None
        self.AuthInfo = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        if params.get("AuthInfo") is not None:
            self.AuthInfo = EndpointAuthInfo()
            self.AuthInfo._deserialize(params.get("AuthInfo"))


class ModifyMediaPackageChannelEndpointResponse(AbstractModel):
    """ModifyMediaPackageChannelEndpoint response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaPackageChannelInputAuthInfoRequest(AbstractModel):
    """ModifyMediaPackageChannelInputAuthInfo request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param Url: Channel input URL.
        :type Url: str
        :param ActionType: Authentication configuration type. Valid values: CLOSE, UPDATE.
CLOSE: disable authentication.
UPDATE: update authentication.
        :type ActionType: str
        """
        self.Id = None
        self.Url = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Url = params.get("Url")
        self.ActionType = params.get("ActionType")


class ModifyMediaPackageChannelInputAuthInfoResponse(AbstractModel):
    """ModifyMediaPackageChannelInputAuthInfo response structure.

    """

    def __init__(self):
        """
        :param AuthInfo: Channel input authentication information.
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.InputAuthInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AuthInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuthInfo") is not None:
            self.AuthInfo = InputAuthInfo()
            self.AuthInfo._deserialize(params.get("AuthInfo"))
        self.RequestId = params.get("RequestId")


class ModifyMediaPackageChannelRequest(AbstractModel):
    """ModifyMediaPackageChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param Name: The channel name after modification.
        :type Name: str
        :param Protocol: The channel protocol after modification. Valid values: HLS, DASH.
        :type Protocol: str
        """
        self.Id = None
        self.Name = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Protocol = params.get("Protocol")


class ModifyMediaPackageChannelResponse(AbstractModel):
    """ModifyMediaPackageChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PointInfo(AbstractModel):
    """Channel input and output.

    """

    def __init__(self):
        """
        :param Inputs: Channel input list.
        :type Inputs: list of InputInfo
        :param Endpoints: Channel output list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Endpoints: list of EndpointInfo
        """
        self.Inputs = None
        self.Endpoints = None


    def _deserialize(self, params):
        if params.get("Inputs") is not None:
            self.Inputs = []
            for item in params.get("Inputs"):
                obj = InputInfo()
                obj._deserialize(item)
                self.Inputs.append(obj)
        if params.get("Endpoints") is not None:
            self.Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointInfo()
                obj._deserialize(item)
                self.Endpoints.append(obj)