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


class BindNewLVBDomainWithChannelRequest(AbstractModel):
    """BindNewLVBDomainWithChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _LVBDomain: The LVB domain name to bind
        :type LVBDomain: str
        """
        self._ChannelId = None
        self._LVBDomain = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def LVBDomain(self):
        return self._LVBDomain

    @LVBDomain.setter
    def LVBDomain(self, LVBDomain):
        self._LVBDomain = LVBDomain


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._LVBDomain = params.get("LVBDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindNewLVBDomainWithChannelResponse(AbstractModel):
    """BindNewLVBDomainWithChannel response structure.

    """

    def __init__(self):
        r"""
        :param _LVBDomain: The LVB domain name bound successfully
        :type LVBDomain: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LVBDomain = None
        self._RequestId = None

    @property
    def LVBDomain(self):
        return self._LVBDomain

    @LVBDomain.setter
    def LVBDomain(self, LVBDomain):
        self._LVBDomain = LVBDomain

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._LVBDomain = params.get("LVBDomain")
        self._RequestId = params.get("RequestId")


class CacheInfo(AbstractModel):
    """Cache configuration

    """

    def __init__(self):
        r"""
        :param _Info: List of timeout parameter configuration
Note: this field may return `null`, indicating that no valid value was found.
        :type Info: list of CacheInfoInfo
        """
        self._Info = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = CacheInfoInfo()
                obj._deserialize(item)
                self._Info.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheInfoInfo(AbstractModel):
    """Timeout information for cache configuration

    """

    def __init__(self):
        r"""
        :param _Timeout: Timeout period (ms), which must be an integer multiple of 1000
.m3u8/.mpd: [1000, 60000]
.ts/.m4s/.mp4: [10000, 1800000]
        :type Timeout: int
        :param _Ext: File extension. Valid values: .m3u8, .ts, .mpd, .m4s, .mp4
Note: this field may return `null`, indicating that no valid value was found.
        :type Ext: str
        """
        self._Timeout = None
        self._Ext = None

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Ext(self):
        return self._Ext

    @Ext.setter
    def Ext(self, Ext):
        self._Ext = Ext


    def _deserialize(self, params):
        self._Timeout = params.get("Timeout")
        self._Ext = params.get("Ext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelInfo(AbstractModel):
    """Channel information.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID.
        :type Id: str
        :param _Name: Channel name.
        :type Name: str
        :param _Protocol: Channel protocol.
        :type Protocol: str
        :param _Points: Channel input and output.
        :type Points: :class:`tencentcloud.mdp.v20200527.models.PointInfo`
        :param _CacheInfo: Cache configuration
Note: this field may return `null`, indicating that no valid value was found.
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self._Id = None
        self._Name = None
        self._Protocol = None
        self._Points = None
        self._CacheInfo = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points

    @property
    def CacheInfo(self):
        return self._CacheInfo

    @CacheInfo.setter
    def CacheInfo(self, CacheInfo):
        self._CacheInfo = CacheInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        if params.get("Points") is not None:
            self._Points = PointInfo()
            self._Points._deserialize(params.get("Points"))
        if params.get("CacheInfo") is not None:
            self._CacheInfo = CacheInfo()
            self._CacheInfo._deserialize(params.get("CacheInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageChannelEndpointRequest(AbstractModel):
    """CreateStreamPackageChannelEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _Name: Endpoint name, which must contain 1 to 32 characters and supports digits, letters, and underscores
        :type Name: str
        :param _AuthInfo: Authentication information
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        self._Id = None
        self._Name = None
        self._AuthInfo = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AuthInfo(self):
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = EndpointAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageChannelEndpointResponse(AbstractModel):
    """CreateStreamPackageChannelEndpoint response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Information of the created channel endpoint
        :type Info: :class:`tencentcloud.mdp.v20200527.models.EndpointInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = EndpointInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageChannelRequest(AbstractModel):
    """CreateStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Channel name
        :type Name: str
        :param _Protocol: Channel protocol. Valid values: HLS, DASH
        :type Protocol: str
        :param _CacheInfo: Cache configuration
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self._Name = None
        self._Protocol = None
        self._CacheInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CacheInfo(self):
        return self._CacheInfo

    @CacheInfo.setter
    def CacheInfo(self, CacheInfo):
        self._CacheInfo = CacheInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        if params.get("CacheInfo") is not None:
            self._CacheInfo = CacheInfo()
            self._CacheInfo._deserialize(params.get("CacheInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageChannelResponse(AbstractModel):
    """CreateStreamPackageChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Channel information
        :type Info: :class:`tencentcloud.mdp.v20200527.models.ChannelInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = ChannelInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageHarvestJobRequest(AbstractModel):
    """CreateStreamPackageHarvestJob request structure.

    """

    def __init__(self):
        r"""
        :param _ID: HarvestJob ID, a globally unique identifier.
        :type ID: str
        :param _ChannelName: The associated channel name.
        :type ChannelName: str
        :param _EndpointName: The associated endpoint name.
        :type EndpointName: str
        :param _TimeFormat: Time format, supports the following types: 1. Epoch seconds 2. ISO-8601
        :type TimeFormat: str
        :param _StartTime: Task start time supports two formats for TimeFormat input: 1. Epoch seconds: The input box is a numeric input box, and only positive integers can be entered. 2. ISO-8601: The supported format is ISO time, for example: 2023-08-01T10:00:00+08:00.
        :type StartTime: str
        :param _EndTime: Task end time supports two formats for TimeFormat input: 1. Epoch seconds: The input box is a numeric input box, and only positive integers can be entered. 2. ISO-8601: The supported format is ISO time, for example: 2023-08-01T10:00:00+08:00.
        :type EndTime: str
        :param _Destination: The path where the recording file is stored in Cos.
        :type Destination: str
        :param _Manifest: The file name of the recording file stored in Cos.
        :type Manifest: str
        """
        self._ID = None
        self._ChannelName = None
        self._EndpointName = None
        self._TimeFormat = None
        self._StartTime = None
        self._EndTime = None
        self._Destination = None
        self._Manifest = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def EndpointName(self):
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Destination(self):
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Manifest(self):
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ChannelName = params.get("ChannelName")
        self._EndpointName = params.get("EndpointName")
        self._TimeFormat = params.get("TimeFormat")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Destination = params.get("Destination")
        self._Manifest = params.get("Manifest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageHarvestJobResponse(AbstractModel):
    """CreateStreamPackageHarvestJob response structure.

    """

    def __init__(self):
        r"""
        :param _Info: HarvestJob information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.HarvestJobResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = HarvestJobResp()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageChannelEndpointsRequest(AbstractModel):
    """DeleteStreamPackageChannelEndpoints request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _Urls: List of the URLs of the endpoints to delete
        :type Urls: list of str
        """
        self._Id = None
        self._Urls = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamPackageChannelEndpointsResponse(AbstractModel):
    """DeleteStreamPackageChannelEndpoints response structure.

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


class DeleteStreamPackageChannelsRequest(AbstractModel):
    """DeleteStreamPackageChannels request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: List of the IDs of the channels to delete
        :type Ids: list of str
        """
        self._Ids = None

    @property
    def Ids(self):
        return self._Ids

    @Ids.setter
    def Ids(self, Ids):
        self._Ids = Ids


    def _deserialize(self, params):
        self._Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamPackageChannelsResponse(AbstractModel):
    """DeleteStreamPackageChannels response structure.

    """

    def __init__(self):
        r"""
        :param _SuccessInfos: List of the information of successfully deleted channels
        :type SuccessInfos: list of ChannelInfo
        :param _FailInfos: List of the information of the channels that failed to be deleted
        :type FailInfos: list of ChannelInfo
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInfos = None
        self._FailInfos = None
        self._RequestId = None

    @property
    def SuccessInfos(self):
        return self._SuccessInfos

    @SuccessInfos.setter
    def SuccessInfos(self, SuccessInfos):
        self._SuccessInfos = SuccessInfos

    @property
    def FailInfos(self):
        return self._FailInfos

    @FailInfos.setter
    def FailInfos(self, FailInfos):
        self._FailInfos = FailInfos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SuccessInfos") is not None:
            self._SuccessInfos = []
            for item in params.get("SuccessInfos"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._SuccessInfos.append(obj)
        if params.get("FailInfos") is not None:
            self._FailInfos = []
            for item in params.get("FailInfos"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._FailInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageHarvestJobRequest(AbstractModel):
    """DeleteStreamPackageHarvestJob request structure.

    """

    def __init__(self):
        r"""
        :param _ID: HarvestJob ID, a globally unique identifier.
        :type ID: str
        """
        self._ID = None

    @property
    def ID(self):
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
        


class DeleteStreamPackageHarvestJobResponse(AbstractModel):
    """DeleteStreamPackageHarvestJob response structure.

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


class DeleteStreamPackageHarvestJobsRequest(AbstractModel):
    """DeleteStreamPackageHarvestJobs request structure.

    """

    def __init__(self):
        r"""
        :param _IDs: HarvestJob IDs, id is a globally unique identifier.
        :type IDs: list of str
        """
        self._IDs = None

    @property
    def IDs(self):
        return self._IDs

    @IDs.setter
    def IDs(self, IDs):
        self._IDs = IDs


    def _deserialize(self, params):
        self._IDs = params.get("IDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamPackageHarvestJobsResponse(AbstractModel):
    """DeleteStreamPackageHarvestJobs response structure.

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


class DescribeStreamPackageChannelRequest(AbstractModel):
    """DescribeStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
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
        


class DescribeStreamPackageChannelResponse(AbstractModel):
    """DescribeStreamPackageChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Channel information
        :type Info: :class:`tencentcloud.mdp.v20200527.models.ChannelInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = ChannelInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageChannelsRequest(AbstractModel):
    """DescribeStreamPackageChannels request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Page number. Value range: [1, 1000]
        :type PageNum: int
        :param _PageSize: Number of entries per page. Value range: [1, 1000]
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageChannelsResponse(AbstractModel):
    """DescribeStreamPackageChannels response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of channel information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of ChannelInfo
        :param _PageNum: Page number
        :type PageNum: int
        :param _PageSize: Number of entries per page
        :type PageSize: int
        :param _TotalNum: Total number of entries
        :type TotalNum: int
        :param _TotalPage: Total number of pages
        :type TotalPage: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageHarvestJobRequest(AbstractModel):
    """DescribeStreamPackageHarvestJob request structure.

    """

    def __init__(self):
        r"""
        :param _ID: HarvestJob ID, a globally unique identifier.
        :type ID: str
        """
        self._ID = None

    @property
    def ID(self):
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
        


class DescribeStreamPackageHarvestJobResponse(AbstractModel):
    """DescribeStreamPackageHarvestJob response structure.

    """

    def __init__(self):
        r"""
        :param _Info: HarvestJob information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.HarvestJobResp`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = HarvestJobResp()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageHarvestJobsRequest(AbstractModel):
    """DescribeStreamPackageHarvestJobs request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelName: The bound channel name. If not passed, all channels will be queried by default.
        :type ChannelName: str
        :param _PageNum: Page number.
        :type PageNum: int
        :param _PageSize: PageSize.
        :type PageSize: int
        """
        self._ChannelName = None
        self._PageNum = None
        self._PageSize = None

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ChannelName = params.get("ChannelName")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageHarvestJobsResponse(AbstractModel):
    """DescribeStreamPackageHarvestJobs response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: HarvestJob information list.
        :type Infos: list of HarvestJobResp
        :param _PageNum: Page number.
        :type PageNum: int
        :param _PageSize: PageSize
        :type PageSize: int
        :param _TotalNum: TotalNum
        :type TotalNum: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = HarvestJobResp()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class EndpointAuthInfo(AbstractModel):
    """The authentication information of channel endpoints.

    """

    def __init__(self):
        r"""
        :param _WhiteIpList: The security group allowlist in CIDR format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type WhiteIpList: list of str
        :param _BlackIpList: The security group blocklist in CIDR format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BlackIpList: list of str
        :param _AuthKey: The authentication key. Its value is same as `X-TENCENT-PACKAGE` set in the HTTP request header.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthKey: str
        """
        self._WhiteIpList = None
        self._BlackIpList = None
        self._AuthKey = None

    @property
    def WhiteIpList(self):
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList

    @property
    def BlackIpList(self):
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def AuthKey(self):
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey


    def _deserialize(self, params):
        self._WhiteIpList = params.get("WhiteIpList")
        self._BlackIpList = params.get("BlackIpList")
        self._AuthKey = params.get("AuthKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointInfo(AbstractModel):
    """Channel endpoint information.

    """

    def __init__(self):
        r"""
        :param _Name: Endpoint name.
        :type Name: str
        :param _Url: Endpoint URL.
        :type Url: str
        :param _AuthInfo: Endpoint authentication information.
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        self._Name = None
        self._Url = None
        self._AuthInfo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AuthInfo(self):
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = EndpointAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HarvestJobResp(AbstractModel):
    """HarvestJob response info.

    """

    def __init__(self):
        r"""
        :param _ID: HarvestJob ID, a globally unique identifier.
        :type ID: str
        :param _ChannelName: The associated channel name.
        :type ChannelName: str
        :param _EndpointName: The associated endpoint name.
        :type EndpointName: str
        :param _TimeFormat: Time format, supports the following types: 1. Epoch seconds 2. ISO-8601
        :type TimeFormat: str
        :param _StartTime: HarvestJob start time.
        :type StartTime: str
        :param _EndTime: HarvestJob end time.
        :type EndTime: str
        :param _Destination: The path where the recording file is stored in COS.
        :type Destination: str
        :param _Manifest: The file name of the recording file stored in COS.
        :type Manifest: str
        :param _Status: The task status is divided into running: Running, execution completed: Completed, and execution failure: Failed.
        :type Status: str
        :param _ErrMessage: HarvestJob error message.
        :type ErrMessage: str
        :param _CreateTime: HarvestJob creation time, timestamp in seconds.
        :type CreateTime: int
        :param _ChannelId: The associated ChannelID.
        :type ChannelId: str
        :param _Region: The region corresponding to the harvest job.
        :type Region: str
        """
        self._ID = None
        self._ChannelName = None
        self._EndpointName = None
        self._TimeFormat = None
        self._StartTime = None
        self._EndTime = None
        self._Destination = None
        self._Manifest = None
        self._Status = None
        self._ErrMessage = None
        self._CreateTime = None
        self._ChannelId = None
        self._Region = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ChannelName(self):
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def EndpointName(self):
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Destination(self):
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Manifest(self):
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMessage(self):
        return self._ErrMessage

    @ErrMessage.setter
    def ErrMessage(self, ErrMessage):
        self._ErrMessage = ErrMessage

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._ChannelName = params.get("ChannelName")
        self._EndpointName = params.get("EndpointName")
        self._TimeFormat = params.get("TimeFormat")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Destination = params.get("Destination")
        self._Manifest = params.get("Manifest")
        self._Status = params.get("Status")
        self._ErrMessage = params.get("ErrMessage")
        self._CreateTime = params.get("CreateTime")
        self._ChannelId = params.get("ChannelId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputAuthInfo(AbstractModel):
    """Channel input authentication information.

    """

    def __init__(self):
        r"""
        :param _Username: Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Username: str
        :param _Password: Password.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Password: str
        """
        self._Username = None
        self._Password = None

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """Channel input.

    """

    def __init__(self):
        r"""
        :param _Url: Channel input URL.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Url: str
        :param _AuthInfo: Channel input authentication information.
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.InputAuthInfo`
        """
        self._Url = None
        self._AuthInfo = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AuthInfo(self):
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo


    def _deserialize(self, params):
        self._Url = params.get("Url")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = InputAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelEndpointRequest(AbstractModel):
    """ModifyStreamPackageChannelEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _Url: Channel endpoint URL
        :type Url: str
        :param _Name: New endpoint name
        :type Name: str
        :param _AuthInfo: New channel authentication information
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        self._Id = None
        self._Url = None
        self._Name = None
        self._AuthInfo = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AuthInfo(self):
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._Name = params.get("Name")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = EndpointAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelEndpointResponse(AbstractModel):
    """ModifyStreamPackageChannelEndpoint response structure.

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


class ModifyStreamPackageChannelInputAuthInfoRequest(AbstractModel):
    """ModifyStreamPackageChannelInputAuthInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _Url: Channel input URL
        :type Url: str
        :param _ActionType: Authentication configuration. Valid values: `CLOSE`, `UPDATE`
`CLOSE`: disable authentication
`UPDATE`: update authentication information
        :type ActionType: str
        """
        self._Id = None
        self._Url = None
        self._ActionType = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ActionType(self):
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._ActionType = params.get("ActionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelInputAuthInfoResponse(AbstractModel):
    """ModifyStreamPackageChannelInputAuthInfo response structure.

    """

    def __init__(self):
        r"""
        :param _AuthInfo: Channel input authentication information
        :type AuthInfo: :class:`tencentcloud.mdp.v20200527.models.InputAuthInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AuthInfo = None
        self._RequestId = None

    @property
    def AuthInfo(self):
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AuthInfo") is not None:
            self._AuthInfo = InputAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        self._RequestId = params.get("RequestId")


class ModifyStreamPackageChannelRequest(AbstractModel):
    """ModifyStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _Name: New channel name
        :type Name: str
        :param _Protocol: New channel protocol. Valid values: HLS, DASH
        :type Protocol: str
        :param _CacheInfo: Cache configuration
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self._Id = None
        self._Name = None
        self._Protocol = None
        self._CacheInfo = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CacheInfo(self):
        return self._CacheInfo

    @CacheInfo.setter
    def CacheInfo(self, CacheInfo):
        self._CacheInfo = CacheInfo


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        if params.get("CacheInfo") is not None:
            self._CacheInfo = CacheInfo()
            self._CacheInfo._deserialize(params.get("CacheInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageChannelResponse(AbstractModel):
    """ModifyStreamPackageChannel response structure.

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


class PointInfo(AbstractModel):
    """Channel input and output.

    """

    def __init__(self):
        r"""
        :param _Inputs: Channel input list.
        :type Inputs: list of InputInfo
        :param _Endpoints: Channel output list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Endpoints: list of EndpointInfo
        """
        self._Inputs = None
        self._Endpoints = None

    @property
    def Inputs(self):
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def Endpoints(self):
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints


    def _deserialize(self, params):
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = InputInfo()
                obj._deserialize(item)
                self._Inputs.append(obj)
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = EndpointInfo()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCdnDomainWithChannelRequest(AbstractModel):
    """UnbindCdnDomainWithChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _CdnDomain: CDN playback domain name
        :type CdnDomain: str
        """
        self._ChannelId = None
        self._CdnDomain = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def CdnDomain(self):
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._CdnDomain = params.get("CdnDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCdnDomainWithChannelResponse(AbstractModel):
    """UnbindCdnDomainWithChannel response structure.

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