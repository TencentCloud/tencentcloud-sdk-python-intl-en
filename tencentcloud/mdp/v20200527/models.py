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


class CacheInfo(AbstractModel):
    """Cache configuration

    """

    def __init__(self):
        r"""
        :param Info: List of timeout parameter configuration
Note: this field may return `null`, indicating that no valid value was found.
        :type Info: list of CacheInfoInfo
        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = CacheInfoInfo()
                obj._deserialize(item)
                self.Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheInfoInfo(AbstractModel):
    """Timeout information for cache configuration

    """

    def __init__(self):
        r"""
        :param Timeout: Timeout period (ms), which must be an integer multiple of 1000
.m3u8/.mpd: [1000, 60000]
.ts/.m4s/.mp4: [10000, 1800000]
        :type Timeout: int
        :param Ext: File extension. Valid values: .m3u8, .ts, .mpd, .m4s, .mp4
Note: this field may return `null`, indicating that no valid value was found.
        :type Ext: str
        """
        self.Timeout = None
        self.Ext = None


    def _deserialize(self, params):
        self.Timeout = params.get("Timeout")
        self.Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelInfo(AbstractModel):
    """Channel information.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID.
        :type Id: str
        :param Name: Channel name.
        :type Name: str
        :param Protocol: Channel protocol.
        :type Protocol: str
        :param Points: Channel input and output.
        :type Points: :class:`tencentcloud.mdp.v20200527.models.PointInfo`
        :param CacheInfo: Cache configuration
Note: this field may return `null`, indicating that no valid value was found.
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self.Id = None
        self.Name = None
        self.Protocol = None
        self.Points = None
        self.CacheInfo = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Protocol = params.get("Protocol")
        if params.get("Points") is not None:
            self.Points = PointInfo()
            self.Points._deserialize(params.get("Points"))
        if params.get("CacheInfo") is not None:
            self.CacheInfo = CacheInfo()
            self.CacheInfo._deserialize(params.get("CacheInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageChannelEndpointRequest(AbstractModel):
    """CreateStreamPackageChannelEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param Name: Channel name
        :type Name: str
        :param AuthInfo: Authentication information
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageChannelEndpointResponse(AbstractModel):
    """CreateStreamPackageChannelEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param Info: Information of the created channel endpoint
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


class CreateStreamPackageChannelRequest(AbstractModel):
    """CreateStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param Name: Channel name
        :type Name: str
        :param Protocol: Channel protocol. Valid values: HLS, DASH
        :type Protocol: str
        :param CacheInfo: Cache configuration
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self.Name = None
        self.Protocol = None
        self.CacheInfo = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Protocol = params.get("Protocol")
        if params.get("CacheInfo") is not None:
            self.CacheInfo = CacheInfo()
            self.CacheInfo._deserialize(params.get("CacheInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageChannelResponse(AbstractModel):
    """CreateStreamPackageChannel response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStreamPackageChannelEndpointsRequest(AbstractModel):
    """DeleteStreamPackageChannelEndpoints request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param Urls: List of the URLs of the endpoints to delete
        :type Urls: list of str
        """
        self.Id = None
        self.Urls = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamPackageChannelEndpointsResponse(AbstractModel):
    """DeleteStreamPackageChannelEndpoints response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStreamPackageChannelsRequest(AbstractModel):
    """DeleteStreamPackageChannels request structure.

    """

    def __init__(self):
        r"""
        :param Ids: List of the IDs of the channels to delete
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamPackageChannelsResponse(AbstractModel):
    """DeleteStreamPackageChannels response structure.

    """

    def __init__(self):
        r"""
        :param SuccessInfos: List of the information of successfully deleted channels
        :type SuccessInfos: list of ChannelInfo
        :param FailInfos: List of the information of the channels that failed to be deleted
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


class DescribeStreamPackageChannelRequest(AbstractModel):
    """DescribeStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageChannelResponse(AbstractModel):
    """DescribeStreamPackageChannel response structure.

    """

    def __init__(self):
        r"""
        :param Info: Channel information
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


class DescribeStreamPackageChannelsRequest(AbstractModel):
    """DescribeStreamPackageChannels request structure.

    """

    def __init__(self):
        r"""
        :param PageNum: Page number. Value range: [1, 1000]
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [1, 1000]
        :type PageSize: int
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageChannelsResponse(AbstractModel):
    """DescribeStreamPackageChannels response structure.

    """

    def __init__(self):
        r"""
        :param Infos: List of channel information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of ChannelInfo
        :param PageNum: Page number
        :type PageNum: int
        :param PageSize: Number of entries per page
        :type PageSize: int
        :param TotalNum: Total number of entries
        :type TotalNum: int
        :param TotalPage: Total number of pages
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointInfo(AbstractModel):
    """Channel endpoint information.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputAuthInfo(AbstractModel):
    """Channel input authentication information.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """Channel input.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelEndpointRequest(AbstractModel):
    """ModifyStreamPackageChannelEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param Url: Channel endpoint URL
        :type Url: str
        :param Name: New endpoint name
        :type Name: str
        :param AuthInfo: New channel authentication information
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelEndpointResponse(AbstractModel):
    """ModifyStreamPackageChannelEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyStreamPackageChannelInputAuthInfoRequest(AbstractModel):
    """ModifyStreamPackageChannelInputAuthInfo request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param Url: Channel input URL
        :type Url: str
        :param ActionType: Authentication configuration. Valid values: `CLOSE`, `UPDATE`
`CLOSE`: disable authentication
`UPDATE`: update authentication information
        :type ActionType: str
        """
        self.Id = None
        self.Url = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Url = params.get("Url")
        self.ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelInputAuthInfoResponse(AbstractModel):
    """ModifyStreamPackageChannelInputAuthInfo response structure.

    """

    def __init__(self):
        r"""
        :param AuthInfo: Channel input authentication information
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


class ModifyStreamPackageChannelRequest(AbstractModel):
    """ModifyStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param Id: Channel ID
        :type Id: str
        :param Name: New channel name
        :type Name: str
        :param Protocol: New channel protocol. Valid values: HLS, DASH
        :type Protocol: str
        :param CacheInfo: Cache configuration
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self.Id = None
        self.Name = None
        self.Protocol = None
        self.CacheInfo = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Protocol = params.get("Protocol")
        if params.get("CacheInfo") is not None:
            self.CacheInfo = CacheInfo()
            self.CacheInfo._deserialize(params.get("CacheInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelResponse(AbstractModel):
    """ModifyStreamPackageChannel response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        