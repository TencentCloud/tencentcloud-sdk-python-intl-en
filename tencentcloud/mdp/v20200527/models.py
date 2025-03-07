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


class AdBreakInfo(AbstractModel):
    """AdBreakInfo.

    """

    def __init__(self):
        r"""
        :param _SourceLocationId: SourceLocationId.
        :type SourceLocationId: str
        :param _VodSourceName: VodSourceName.
        :type VodSourceName: str
        :param _Offset: Offset.
        :type Offset: int
        :param _MessageType: MessageType, divided into SpliceInsert and TimeSignal.
        :type MessageType: str
        :param _TimeSignalConf: TimeSignalConf.
        :type TimeSignalConf: :class:`tencentcloud.mdp.v20200527.models.TimeSignalInfo`
        :param _SpliceInsertConf: SpliceInsertConf.
        :type SpliceInsertConf: :class:`tencentcloud.mdp.v20200527.models.SpliceInsertInfo`
        :param _Metadatas: Metadatas.
        :type Metadatas: list of Metadata
        :param _SourceLocationName: SourceLocationName.
        :type SourceLocationName: str
        """
        self._SourceLocationId = None
        self._VodSourceName = None
        self._Offset = None
        self._MessageType = None
        self._TimeSignalConf = None
        self._SpliceInsertConf = None
        self._Metadatas = None
        self._SourceLocationName = None

    @property
    def SourceLocationId(self):
        """SourceLocationId.
        :rtype: str
        """
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def VodSourceName(self):
        """VodSourceName.
        :rtype: str
        """
        return self._VodSourceName

    @VodSourceName.setter
    def VodSourceName(self, VodSourceName):
        self._VodSourceName = VodSourceName

    @property
    def Offset(self):
        """Offset.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def MessageType(self):
        """MessageType, divided into SpliceInsert and TimeSignal.
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def TimeSignalConf(self):
        """TimeSignalConf.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.TimeSignalInfo`
        """
        return self._TimeSignalConf

    @TimeSignalConf.setter
    def TimeSignalConf(self, TimeSignalConf):
        self._TimeSignalConf = TimeSignalConf

    @property
    def SpliceInsertConf(self):
        """SpliceInsertConf.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SpliceInsertInfo`
        """
        return self._SpliceInsertConf

    @SpliceInsertConf.setter
    def SpliceInsertConf(self, SpliceInsertConf):
        self._SpliceInsertConf = SpliceInsertConf

    @property
    def Metadatas(self):
        """Metadatas.
        :rtype: list of Metadata
        """
        return self._Metadatas

    @Metadatas.setter
    def Metadatas(self, Metadatas):
        self._Metadatas = Metadatas

    @property
    def SourceLocationName(self):
        """SourceLocationName.
        :rtype: str
        """
        return self._SourceLocationName

    @SourceLocationName.setter
    def SourceLocationName(self, SourceLocationName):
        self._SourceLocationName = SourceLocationName


    def _deserialize(self, params):
        self._SourceLocationId = params.get("SourceLocationId")
        self._VodSourceName = params.get("VodSourceName")
        self._Offset = params.get("Offset")
        self._MessageType = params.get("MessageType")
        if params.get("TimeSignalConf") is not None:
            self._TimeSignalConf = TimeSignalInfo()
            self._TimeSignalConf._deserialize(params.get("TimeSignalConf"))
        if params.get("SpliceInsertConf") is not None:
            self._SpliceInsertConf = SpliceInsertInfo()
            self._SpliceInsertConf._deserialize(params.get("SpliceInsertConf"))
        if params.get("Metadatas") is not None:
            self._Metadatas = []
            for item in params.get("Metadatas"):
                obj = Metadata()
                obj._deserialize(item)
                self._Metadatas.append(obj)
        self._SourceLocationName = params.get("SourceLocationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AliasValueConf(AbstractModel):
    """Alias-value configuration information.

    """

    def __init__(self):
        r"""
        :param _Alias: Alias.
        :type Alias: str
        :param _Value: Value.
        :type Value: str
        """
        self._Alias = None
        self._Value = None

    @property
    def Alias(self):
        """Alias.
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Value(self):
        """Value.
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindLinearAssemblyCDNDomainWithChannelRequest(AbstractModel):
    """BindLinearAssemblyCDNDomainWithChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel Id.
        :type ChannelId: str
        :param _CdnDomain: Cdn playback domain.
        :type CdnDomain: str
        """
        self._ChannelId = None
        self._CdnDomain = None

    @property
    def ChannelId(self):
        """Channel Id.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def CdnDomain(self):
        """Cdn playback domain.
        :rtype: str
        """
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
        


class BindLinearAssemblyCDNDomainWithChannelResponse(AbstractModel):
    """BindLinearAssemblyCDNDomainWithChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


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
        """Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def LVBDomain(self):
        """The LVB domain name to bind
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._LVBDomain = None
        self._RequestId = None

    @property
    def LVBDomain(self):
        """The LVB domain name bound successfully
        :rtype: str
        """
        return self._LVBDomain

    @LVBDomain.setter
    def LVBDomain(self, LVBDomain):
        self._LVBDomain = LVBDomain

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
        """List of timeout parameter configuration
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: list of CacheInfoInfo
        """
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
        """Timeout period (ms), which must be an integer multiple of 1000
.m3u8/.mpd: [1000, 60000]
.ts/.m4s/.mp4: [10000, 1800000]
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Ext(self):
        """File extension. Valid values: .m3u8, .ts, .mpd, .m4s, .mp4
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
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
        


class CdnDomainInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _TotalSize: 
        :type TotalSize: int
        :param _Records: 
        :type Records: list of DomainRecordInfo
        """
        self._TotalSize = None
        self._Records = None

    @property
    def TotalSize(self):
        """
        :rtype: int
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def Records(self):
        """
        :rtype: list of DomainRecordInfo
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records


    def _deserialize(self, params):
        self._TotalSize = params.get("TotalSize")
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = DomainRecordInfo()
                obj._deserialize(item)
                self._Records.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelAlertResp(AbstractModel):
    """Linear assembly channel alarm return information.

    """

    def __init__(self):
        r"""
        :param _ProgramAlertCounts: Program alarm aggregation information.
        :type ProgramAlertCounts: list of ProgramAlertCounts
        :param _ProgramAlertInfos: Program alarm details.
        :type ProgramAlertInfos: list of ProgramAlertInfos
        """
        self._ProgramAlertCounts = None
        self._ProgramAlertInfos = None

    @property
    def ProgramAlertCounts(self):
        """Program alarm aggregation information.
        :rtype: list of ProgramAlertCounts
        """
        return self._ProgramAlertCounts

    @ProgramAlertCounts.setter
    def ProgramAlertCounts(self, ProgramAlertCounts):
        self._ProgramAlertCounts = ProgramAlertCounts

    @property
    def ProgramAlertInfos(self):
        """Program alarm details.
        :rtype: list of ProgramAlertInfos
        """
        return self._ProgramAlertInfos

    @ProgramAlertInfos.setter
    def ProgramAlertInfos(self, ProgramAlertInfos):
        self._ProgramAlertInfos = ProgramAlertInfos


    def _deserialize(self, params):
        if params.get("ProgramAlertCounts") is not None:
            self._ProgramAlertCounts = []
            for item in params.get("ProgramAlertCounts"):
                obj = ProgramAlertCounts()
                obj._deserialize(item)
                self._ProgramAlertCounts.append(obj)
        if params.get("ProgramAlertInfos") is not None:
            self._ProgramAlertInfos = []
            for item in params.get("ProgramAlertInfos"):
                obj = ProgramAlertInfos()
                obj._deserialize(item)
                self._ProgramAlertInfos.append(obj)
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
        """Channel ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Channel name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        """Channel protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Points(self):
        """Channel input and output.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.PointInfo`
        """
        return self._Points

    @Points.setter
    def Points(self, Points):
        self._Points = Points

    @property
    def CacheInfo(self):
        """Cache configuration
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
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
        


class ClipRangeInfo(AbstractModel):
    """Spacer configuration.

    """

    def __init__(self):
        r"""
        :param _Type: The vod type is valid, the content is valid starting time, Entire and SpecifyTimeRange are optional.
        :type Type: str
        :param _Offset: Offset, valid when Type is SpecifyTimeRange.
        :type Offset: int
        """
        self._Type = None
        self._Offset = None

    @property
    def Type(self):
        """The vod type is valid, the content is valid starting time, Entire and SpecifyTimeRange are optional.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Offset(self):
        """Offset, valid when Type is SpecifyTimeRange.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigAliasesInfo(AbstractModel):
    """Parameter configuration.

    """

    def __init__(self):
        r"""
        :param _ParamName: parameter name.
        :type ParamName: str
        :param _AliasValueList: Alias-value configuration.
        :type AliasValueList: list of AliasValueConf
        """
        self._ParamName = None
        self._AliasValueList = None

    @property
    def ParamName(self):
        """parameter name.
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def AliasValueList(self):
        """Alias-value configuration.
        :rtype: list of AliasValueConf
        """
        return self._AliasValueList

    @AliasValueList.setter
    def AliasValueList(self, AliasValueList):
        self._AliasValueList = AliasValueList


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        if params.get("AliasValueList") is not None:
            self._AliasValueList = []
            for item in params.get("AliasValueList"):
                obj = AliasValueConf()
                obj._deserialize(item)
                self._AliasValueList.append(obj)
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
        :param _Protocol: Endpoint protocol type, supports HLS, DASH, CMAF (only HLS type input can create CMAF Endpoint).
        :type Protocol: str
        :param _Manifest: Mainifest name, default is main.
        :type Manifest: str
        :param _TimeShiftEnable: Whether to turn on the TimeShift function, true: on, false: off, the default is off.
        :type TimeShiftEnable: bool
        :param _TimeShiftDuration: The number of days to look back in TimeShift, up to 30 days is supported.
        :type TimeShiftDuration: int
        """
        self._Id = None
        self._Name = None
        self._AuthInfo = None
        self._Protocol = None
        self._Manifest = None
        self._TimeShiftEnable = None
        self._TimeShiftDuration = None

    @property
    def Id(self):
        """Channel ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Endpoint name, which must contain 1 to 32 characters and supports digits, letters, and underscores
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AuthInfo(self):
        """Authentication information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def Protocol(self):
        """Endpoint protocol type, supports HLS, DASH, CMAF (only HLS type input can create CMAF Endpoint).
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Manifest(self):
        """Mainifest name, default is main.
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def TimeShiftEnable(self):
        """Whether to turn on the TimeShift function, true: on, false: off, the default is off.
        :rtype: bool
        """
        return self._TimeShiftEnable

    @TimeShiftEnable.setter
    def TimeShiftEnable(self, TimeShiftEnable):
        self._TimeShiftEnable = TimeShiftEnable

    @property
    def TimeShiftDuration(self):
        """The number of days to look back in TimeShift, up to 30 days is supported.
        :rtype: int
        """
        return self._TimeShiftDuration

    @TimeShiftDuration.setter
    def TimeShiftDuration(self, TimeShiftDuration):
        self._TimeShiftDuration = TimeShiftDuration


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = EndpointAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        self._Protocol = params.get("Protocol")
        self._Manifest = params.get("Manifest")
        self._TimeShiftEnable = params.get("TimeShiftEnable")
        self._TimeShiftDuration = params.get("TimeShiftDuration")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Information of the created channel endpoint
        :rtype: :class:`tencentcloud.mdp.v20200527.models.EndpointInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = EndpointInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageChannelRequest(AbstractModel):
    """CreateStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Channel name.
        :type Name: str
        :param _Protocol: Channel protocol. Valid values: HLS, DASH, CMAF.
        :type Protocol: str
        :param _CacheInfo: Cache configuration.
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self._Name = None
        self._Protocol = None
        self._CacheInfo = None

    @property
    def Name(self):
        """Channel name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        """Channel protocol. Valid values: HLS, DASH, CMAF.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CacheInfo(self):
        """Cache configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Channel information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ChannelInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        """HarvestJob ID, a globally unique identifier.
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ChannelName(self):
        """The associated channel name.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def EndpointName(self):
        """The associated endpoint name.
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def TimeFormat(self):
        """Time format, supports the following types: 1. Epoch seconds 2. ISO-8601
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def StartTime(self):
        """Task start time supports two formats for TimeFormat input: 1. Epoch seconds: The input box is a numeric input box, and only positive integers can be entered. 2. ISO-8601: The supported format is ISO time, for example: 2023-08-01T10:00:00+08:00.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Task end time supports two formats for TimeFormat input: 1. Epoch seconds: The input box is a numeric input box, and only positive integers can be entered. 2. ISO-8601: The supported format is ISO time, for example: 2023-08-01T10:00:00+08:00.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Destination(self):
        """The path where the recording file is stored in Cos.
        :rtype: str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Manifest(self):
        """The file name of the recording file stored in Cos.
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """HarvestJob information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.HarvestJobResp`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = HarvestJobResp()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageLinearAssemblyChannelRequest(AbstractModel):
    """CreateStreamPackageLinearAssemblyChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Channel name.
        :type Name: str
        :param _Tier: Define the characteristics of the channel. Standard supports live broadcast and on-demand sources. Basic only supports on-demand source arrangement. Optional values: Standard and Basic.
        :type Tier: str
        :param _PlaybackMode: The source switching modes in the channel are divided into Linear and Loop. Basic only supports Linear, and Standatd supports both.
Optional values: Linear, Standatd.
        :type PlaybackMode: str
        :param _TimeShiftEnable: Time shift enable switch, only valid when Tier is Standard.
        :type TimeShiftEnable: bool
        :param _TimeShiftConf: Time shift configuration, effective when the time shift switch is turned on.
        :type TimeShiftConf: :class:`tencentcloud.mdp.v20200527.models.TimeShiftInfo`
        :param _SlateConf: Spacer configuration is only valid when PlaybackMode is Linear.
        :type SlateConf: :class:`tencentcloud.mdp.v20200527.models.SlateInfo`
        :param _Outputs: Output configuration.
        :type Outputs: list of OutputReq
        """
        self._Name = None
        self._Tier = None
        self._PlaybackMode = None
        self._TimeShiftEnable = None
        self._TimeShiftConf = None
        self._SlateConf = None
        self._Outputs = None

    @property
    def Name(self):
        """Channel name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tier(self):
        """Define the characteristics of the channel. Standard supports live broadcast and on-demand sources. Basic only supports on-demand source arrangement. Optional values: Standard and Basic.
        :rtype: str
        """
        return self._Tier

    @Tier.setter
    def Tier(self, Tier):
        self._Tier = Tier

    @property
    def PlaybackMode(self):
        """The source switching modes in the channel are divided into Linear and Loop. Basic only supports Linear, and Standatd supports both.
Optional values: Linear, Standatd.
        :rtype: str
        """
        return self._PlaybackMode

    @PlaybackMode.setter
    def PlaybackMode(self, PlaybackMode):
        self._PlaybackMode = PlaybackMode

    @property
    def TimeShiftEnable(self):
        """Time shift enable switch, only valid when Tier is Standard.
        :rtype: bool
        """
        return self._TimeShiftEnable

    @TimeShiftEnable.setter
    def TimeShiftEnable(self, TimeShiftEnable):
        self._TimeShiftEnable = TimeShiftEnable

    @property
    def TimeShiftConf(self):
        """Time shift configuration, effective when the time shift switch is turned on.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.TimeShiftInfo`
        """
        return self._TimeShiftConf

    @TimeShiftConf.setter
    def TimeShiftConf(self, TimeShiftConf):
        self._TimeShiftConf = TimeShiftConf

    @property
    def SlateConf(self):
        """Spacer configuration is only valid when PlaybackMode is Linear.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SlateInfo`
        """
        return self._SlateConf

    @SlateConf.setter
    def SlateConf(self, SlateConf):
        self._SlateConf = SlateConf

    @property
    def Outputs(self):
        """Output configuration.
        :rtype: list of OutputReq
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Tier = params.get("Tier")
        self._PlaybackMode = params.get("PlaybackMode")
        self._TimeShiftEnable = params.get("TimeShiftEnable")
        if params.get("TimeShiftConf") is not None:
            self._TimeShiftConf = TimeShiftInfo()
            self._TimeShiftConf._deserialize(params.get("TimeShiftConf"))
        if params.get("SlateConf") is not None:
            self._SlateConf = SlateInfo()
            self._SlateConf._deserialize(params.get("SlateConf"))
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = OutputReq()
                obj._deserialize(item)
                self._Outputs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageLinearAssemblyChannelResponse(AbstractModel):
    """CreateStreamPackageLinearAssemblyChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: channel information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyChannelInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """channel information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyChannelInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = LinearAssemblyChannelInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageLinearAssemblyProgramRequest(AbstractModel):
    """CreateStreamPackageLinearAssemblyProgram request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Program name.
        :type Name: str
        :param _AttachedChannel: The bound channel.
        :type AttachedChannel: str
        :param _SourceType: The type of arrangement target source is divided into live broadcast and on-demand VOD.
Optional values: Live, VOD.
        :type SourceType: str
        :param _SourceLocationId: The associated source location.
        :type SourceLocationId: str
        :param _SourceName: The associated live broadcast or on-demand broadcast, source name, and location are globally unique.
        :type SourceName: str
        :param _PlaybackConf: PlaybackConf.
        :type PlaybackConf: :class:`tencentcloud.mdp.v20200527.models.PlaybackInfoReq`
        :param _AdBreaks: AdBreaks is only valid when the source type is Vod.
        :type AdBreaks: list of AdBreakInfo
        """
        self._Name = None
        self._AttachedChannel = None
        self._SourceType = None
        self._SourceLocationId = None
        self._SourceName = None
        self._PlaybackConf = None
        self._AdBreaks = None

    @property
    def Name(self):
        """Program name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AttachedChannel(self):
        """The bound channel.
        :rtype: str
        """
        return self._AttachedChannel

    @AttachedChannel.setter
    def AttachedChannel(self, AttachedChannel):
        self._AttachedChannel = AttachedChannel

    @property
    def SourceType(self):
        """The type of arrangement target source is divided into live broadcast and on-demand VOD.
Optional values: Live, VOD.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceLocationId(self):
        """The associated source location.
        :rtype: str
        """
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def SourceName(self):
        """The associated live broadcast or on-demand broadcast, source name, and location are globally unique.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def PlaybackConf(self):
        """PlaybackConf.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.PlaybackInfoReq`
        """
        return self._PlaybackConf

    @PlaybackConf.setter
    def PlaybackConf(self, PlaybackConf):
        self._PlaybackConf = PlaybackConf

    @property
    def AdBreaks(self):
        """AdBreaks is only valid when the source type is Vod.
        :rtype: list of AdBreakInfo
        """
        return self._AdBreaks

    @AdBreaks.setter
    def AdBreaks(self, AdBreaks):
        self._AdBreaks = AdBreaks


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AttachedChannel = params.get("AttachedChannel")
        self._SourceType = params.get("SourceType")
        self._SourceLocationId = params.get("SourceLocationId")
        self._SourceName = params.get("SourceName")
        if params.get("PlaybackConf") is not None:
            self._PlaybackConf = PlaybackInfoReq()
            self._PlaybackConf._deserialize(params.get("PlaybackConf"))
        if params.get("AdBreaks") is not None:
            self._AdBreaks = []
            for item in params.get("AdBreaks"):
                obj = AdBreakInfo()
                obj._deserialize(item)
                self._AdBreaks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageLinearAssemblyProgramResponse(AbstractModel):
    """CreateStreamPackageLinearAssemblyProgram response structure.

    """

    def __init__(self):
        r"""
        :param _Info: channel information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyProgramInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """channel information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyProgramInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = LinearAssemblyProgramInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageSSAIChannelRequest(AbstractModel):
    """CreateStreamPackageSSAIChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Ad insertion configuration name, globally unique, cannot be repeated with other configurations
        :type Name: str
        :param _ContentSource: Source stream url prefix
        :type ContentSource: str
        :param _SSAIInfo: Ad insertion configuration information
        :type SSAIInfo: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        """
        self._Name = None
        self._ContentSource = None
        self._SSAIInfo = None

    @property
    def Name(self):
        """Ad insertion configuration name, globally unique, cannot be repeated with other configurations
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContentSource(self):
        """Source stream url prefix
        :rtype: str
        """
        return self._ContentSource

    @ContentSource.setter
    def ContentSource(self, ContentSource):
        self._ContentSource = ContentSource

    @property
    def SSAIInfo(self):
        """Ad insertion configuration information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        """
        return self._SSAIInfo

    @SSAIInfo.setter
    def SSAIInfo(self, SSAIInfo):
        self._SSAIInfo = SSAIInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContentSource = params.get("ContentSource")
        if params.get("SSAIInfo") is not None:
            self._SSAIInfo = SSAIConf()
            self._SSAIInfo._deserialize(params.get("SSAIInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageSSAIChannelResponse(AbstractModel):
    """CreateStreamPackageSSAIChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Ad insertion configuration information
        :type Info: :class:`tencentcloud.mdp.v20200527.models.SSAIChannelInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Ad insertion configuration information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SSAIChannelInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = SSAIChannelInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageSourceLocationRequest(AbstractModel):
    """CreateStreamPackageSourceLocation request structure.

    """

    def __init__(self):
        r"""
        :param _Name: SourceLocation name.
        :type Name: str
        :param _BaseUrl: BaseUrl.
        :type BaseUrl: str
        :param _SegmentDeliverEnable: Whether to enable patching.
        :type SegmentDeliverEnable: bool
        :param _SegmentDeliverConf: Patch configuration.
        :type SegmentDeliverConf: :class:`tencentcloud.mdp.v20200527.models.SegmentDeliverInfo`
        :param _SegmentDeliverUsePackageEnable: Whether to enable package distribution sharding, it is enabled by default.
        :type SegmentDeliverUsePackageEnable: bool
        """
        self._Name = None
        self._BaseUrl = None
        self._SegmentDeliverEnable = None
        self._SegmentDeliverConf = None
        self._SegmentDeliverUsePackageEnable = None

    @property
    def Name(self):
        """SourceLocation name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BaseUrl(self):
        """BaseUrl.
        :rtype: str
        """
        return self._BaseUrl

    @BaseUrl.setter
    def BaseUrl(self, BaseUrl):
        self._BaseUrl = BaseUrl

    @property
    def SegmentDeliverEnable(self):
        """Whether to enable patching.
        :rtype: bool
        """
        return self._SegmentDeliverEnable

    @SegmentDeliverEnable.setter
    def SegmentDeliverEnable(self, SegmentDeliverEnable):
        self._SegmentDeliverEnable = SegmentDeliverEnable

    @property
    def SegmentDeliverConf(self):
        """Patch configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SegmentDeliverInfo`
        """
        return self._SegmentDeliverConf

    @SegmentDeliverConf.setter
    def SegmentDeliverConf(self, SegmentDeliverConf):
        self._SegmentDeliverConf = SegmentDeliverConf

    @property
    def SegmentDeliverUsePackageEnable(self):
        """Whether to enable package distribution sharding, it is enabled by default.
        :rtype: bool
        """
        return self._SegmentDeliverUsePackageEnable

    @SegmentDeliverUsePackageEnable.setter
    def SegmentDeliverUsePackageEnable(self, SegmentDeliverUsePackageEnable):
        self._SegmentDeliverUsePackageEnable = SegmentDeliverUsePackageEnable


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._BaseUrl = params.get("BaseUrl")
        self._SegmentDeliverEnable = params.get("SegmentDeliverEnable")
        if params.get("SegmentDeliverConf") is not None:
            self._SegmentDeliverConf = SegmentDeliverInfo()
            self._SegmentDeliverConf._deserialize(params.get("SegmentDeliverConf"))
        self._SegmentDeliverUsePackageEnable = params.get("SegmentDeliverUsePackageEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageSourceLocationResponse(AbstractModel):
    """CreateStreamPackageSourceLocation response structure.

    """

    def __init__(self):
        r"""
        :param _Info: SourceLocation information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.SourceLocationInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """SourceLocation information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SourceLocationInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = SourceLocationInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamPackageSourceRequest(AbstractModel):
    """CreateStreamPackageSource request structure.

    """

    def __init__(self):
        r"""
        :param _AttachedLocation: The location id to which this source belongs is required and uniquely bound to one location.
        :type AttachedLocation: str
        :param _Name: Source name, globally unique under location.
        :type Name: str
        :param _Type: Distinguish between live broadcast and on-demand VOD source types. Optional values: Live, VOD.
        :type Type: str
        :param _PackageConfs: source specific configuration.
        :type PackageConfs: list of SourcePackageConf
        """
        self._AttachedLocation = None
        self._Name = None
        self._Type = None
        self._PackageConfs = None

    @property
    def AttachedLocation(self):
        """The location id to which this source belongs is required and uniquely bound to one location.
        :rtype: str
        """
        return self._AttachedLocation

    @AttachedLocation.setter
    def AttachedLocation(self, AttachedLocation):
        self._AttachedLocation = AttachedLocation

    @property
    def Name(self):
        """Source name, globally unique under location.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Distinguish between live broadcast and on-demand VOD source types. Optional values: Live, VOD.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PackageConfs(self):
        """source specific configuration.
        :rtype: list of SourcePackageConf
        """
        return self._PackageConfs

    @PackageConfs.setter
    def PackageConfs(self, PackageConfs):
        self._PackageConfs = PackageConfs


    def _deserialize(self, params):
        self._AttachedLocation = params.get("AttachedLocation")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("PackageConfs") is not None:
            self._PackageConfs = []
            for item in params.get("PackageConfs"):
                obj = SourcePackageConf()
                obj._deserialize(item)
                self._PackageConfs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamPackageSourceResponse(AbstractModel):
    """CreateStreamPackageSource response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Source information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.SourceInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Source information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SourceInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = SourceInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DRMInfo(AbstractModel):
    """DRM configure info.

    """

    def __init__(self):
        r"""
        :param _EncryptionMethod: Encryption method, optional values: `CBCS`, `CENC`.
        :type EncryptionMethod: str
        :param _DRMSystems: DRM system providers, when the encryption method is CBCS, the optional values are `PlayReady`, `Widevine`, `FairPlay`; when the encryption method is CENC, the oprional values are `PlayReady`, `Widevine`.
        :type DRMSystems: list of str
        :param _ResourceID: The resource ID sent to the key server. It can contain 1 to 128 characters, including numbers, letters, underscores (_), and hyphens (-).
        :type ResourceID: str
        :param _KeyServerUrl: Key server address; must start with https://.
        :type KeyServerUrl: str
        :param _VideoEncryptionPreset: Video encryption presets, options: 
`Preset Video 1` - Encrypts all video tracks with one key
`Preset Video 2` - Encrypts SD and HD video tracks with 2 different keys
`Preset Video 3` - Encrypts SD, HD and UHD video tracks with 3 different keys
`Preset Video 4` - Encrypts SD, HD, UHD1 and UHD2 video tracks with 4 different keys
`Preset Video 5` - Encrypts SD, HD1, HD2, UHD1 and UHD2 video tracks with 5 different keys
`Preset Video 6` - Encrypts SD, HD1, HD2, UHD video tracks with 4 different keys
`Preset Video 7` - Encrypts SD + HD1, HD2, UHD video tracks with 3 different keys
`Preset Video 8` - Encrypts SD + HD1, HD2, UHD1, UHD2 video tracks with 4 different keys
`Shared` - Encrypts all video and audio tracks with one key
`Unencrypted` - Does not encrypt any track
        :type VideoEncryptionPreset: str
        :param _AudioEncryptionPreset: Audio encryption presets, options:
`Preset Audio 1` - Encrypts all audio tracks with one key
`Preset Audio 2` - Encrypts STEREO and MULTICHANNEL audio tracks with 2 different keys
`Preset Audio 3` - Encrypts STEREO, MULTICHANNEL 3-6 and MULTICHANNEL 7 audio tracks with 3 different keys
`Shared` - Encrypts all video and audio tracks with one key
`Unencrypted` - Does not encrypt any track
        :type AudioEncryptionPreset: str
        :param _ConstantInitializationVector: Optional, used together with the key to encrypt the content; a 128-bit, 32-character, hexadecimal-encoded string.
        :type ConstantInitializationVector: str
        :param _KeyRotationInterval: Optional, specifies the rotation interval in seconds; empty, or an integer between 300-2592000.
        :type KeyRotationInterval: int
        """
        self._EncryptionMethod = None
        self._DRMSystems = None
        self._ResourceID = None
        self._KeyServerUrl = None
        self._VideoEncryptionPreset = None
        self._AudioEncryptionPreset = None
        self._ConstantInitializationVector = None
        self._KeyRotationInterval = None

    @property
    def EncryptionMethod(self):
        """Encryption method, optional values: `CBCS`, `CENC`.
        :rtype: str
        """
        return self._EncryptionMethod

    @EncryptionMethod.setter
    def EncryptionMethod(self, EncryptionMethod):
        self._EncryptionMethod = EncryptionMethod

    @property
    def DRMSystems(self):
        """DRM system providers, when the encryption method is CBCS, the optional values are `PlayReady`, `Widevine`, `FairPlay`; when the encryption method is CENC, the oprional values are `PlayReady`, `Widevine`.
        :rtype: list of str
        """
        return self._DRMSystems

    @DRMSystems.setter
    def DRMSystems(self, DRMSystems):
        self._DRMSystems = DRMSystems

    @property
    def ResourceID(self):
        """The resource ID sent to the key server. It can contain 1 to 128 characters, including numbers, letters, underscores (_), and hyphens (-).
        :rtype: str
        """
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID

    @property
    def KeyServerUrl(self):
        """Key server address; must start with https://.
        :rtype: str
        """
        return self._KeyServerUrl

    @KeyServerUrl.setter
    def KeyServerUrl(self, KeyServerUrl):
        self._KeyServerUrl = KeyServerUrl

    @property
    def VideoEncryptionPreset(self):
        """Video encryption presets, options: 
`Preset Video 1` - Encrypts all video tracks with one key
`Preset Video 2` - Encrypts SD and HD video tracks with 2 different keys
`Preset Video 3` - Encrypts SD, HD and UHD video tracks with 3 different keys
`Preset Video 4` - Encrypts SD, HD, UHD1 and UHD2 video tracks with 4 different keys
`Preset Video 5` - Encrypts SD, HD1, HD2, UHD1 and UHD2 video tracks with 5 different keys
`Preset Video 6` - Encrypts SD, HD1, HD2, UHD video tracks with 4 different keys
`Preset Video 7` - Encrypts SD + HD1, HD2, UHD video tracks with 3 different keys
`Preset Video 8` - Encrypts SD + HD1, HD2, UHD1, UHD2 video tracks with 4 different keys
`Shared` - Encrypts all video and audio tracks with one key
`Unencrypted` - Does not encrypt any track
        :rtype: str
        """
        return self._VideoEncryptionPreset

    @VideoEncryptionPreset.setter
    def VideoEncryptionPreset(self, VideoEncryptionPreset):
        self._VideoEncryptionPreset = VideoEncryptionPreset

    @property
    def AudioEncryptionPreset(self):
        """Audio encryption presets, options:
`Preset Audio 1` - Encrypts all audio tracks with one key
`Preset Audio 2` - Encrypts STEREO and MULTICHANNEL audio tracks with 2 different keys
`Preset Audio 3` - Encrypts STEREO, MULTICHANNEL 3-6 and MULTICHANNEL 7 audio tracks with 3 different keys
`Shared` - Encrypts all video and audio tracks with one key
`Unencrypted` - Does not encrypt any track
        :rtype: str
        """
        return self._AudioEncryptionPreset

    @AudioEncryptionPreset.setter
    def AudioEncryptionPreset(self, AudioEncryptionPreset):
        self._AudioEncryptionPreset = AudioEncryptionPreset

    @property
    def ConstantInitializationVector(self):
        """Optional, used together with the key to encrypt the content; a 128-bit, 32-character, hexadecimal-encoded string.
        :rtype: str
        """
        return self._ConstantInitializationVector

    @ConstantInitializationVector.setter
    def ConstantInitializationVector(self, ConstantInitializationVector):
        self._ConstantInitializationVector = ConstantInitializationVector

    @property
    def KeyRotationInterval(self):
        """Optional, specifies the rotation interval in seconds; empty, or an integer between 300-2592000.
        :rtype: int
        """
        return self._KeyRotationInterval

    @KeyRotationInterval.setter
    def KeyRotationInterval(self, KeyRotationInterval):
        self._KeyRotationInterval = KeyRotationInterval


    def _deserialize(self, params):
        self._EncryptionMethod = params.get("EncryptionMethod")
        self._DRMSystems = params.get("DRMSystems")
        self._ResourceID = params.get("ResourceID")
        self._KeyServerUrl = params.get("KeyServerUrl")
        self._VideoEncryptionPreset = params.get("VideoEncryptionPreset")
        self._AudioEncryptionPreset = params.get("AudioEncryptionPreset")
        self._ConstantInitializationVector = params.get("ConstantInitializationVector")
        self._KeyRotationInterval = params.get("KeyRotationInterval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DashManifestInfo(AbstractModel):
    """The manifest info used when Type is DASH.

    """

    def __init__(self):
        r"""
        :param _Windows: The total duration of each manifest in seconds. [30, 3600], type: integer, default value 60.
        :type Windows: int
        :param _MinBufferTime: The minimum cache time (in seconds) that the player keeps in the buffer. [2, 60], type: integer, default value 30.
        :type MinBufferTime: int
        :param _MinUpdatePeriod: The minimum time (in seconds) that the player should wait before requesting an update to the manifest. [2, 60], type: integer, default value 2.
        :type MinUpdatePeriod: int
        :param _SuggestedPresentationDelay: The time from the latest live broadcast time point when the player starts broadcasting is a rollback amount (in seconds). [2, 60], type: integer, default value 10.
        :type SuggestedPresentationDelay: int
        """
        self._Windows = None
        self._MinBufferTime = None
        self._MinUpdatePeriod = None
        self._SuggestedPresentationDelay = None

    @property
    def Windows(self):
        """The total duration of each manifest in seconds. [30, 3600], type: integer, default value 60.
        :rtype: int
        """
        return self._Windows

    @Windows.setter
    def Windows(self, Windows):
        self._Windows = Windows

    @property
    def MinBufferTime(self):
        """The minimum cache time (in seconds) that the player keeps in the buffer. [2, 60], type: integer, default value 30.
        :rtype: int
        """
        return self._MinBufferTime

    @MinBufferTime.setter
    def MinBufferTime(self, MinBufferTime):
        self._MinBufferTime = MinBufferTime

    @property
    def MinUpdatePeriod(self):
        """The minimum time (in seconds) that the player should wait before requesting an update to the manifest. [2, 60], type: integer, default value 2.
        :rtype: int
        """
        return self._MinUpdatePeriod

    @MinUpdatePeriod.setter
    def MinUpdatePeriod(self, MinUpdatePeriod):
        self._MinUpdatePeriod = MinUpdatePeriod

    @property
    def SuggestedPresentationDelay(self):
        """The time from the latest live broadcast time point when the player starts broadcasting is a rollback amount (in seconds). [2, 60], type: integer, default value 10.
        :rtype: int
        """
        return self._SuggestedPresentationDelay

    @SuggestedPresentationDelay.setter
    def SuggestedPresentationDelay(self, SuggestedPresentationDelay):
        self._SuggestedPresentationDelay = SuggestedPresentationDelay


    def _deserialize(self, params):
        self._Windows = params.get("Windows")
        self._MinBufferTime = params.get("MinBufferTime")
        self._MinUpdatePeriod = params.get("MinUpdatePeriod")
        self._SuggestedPresentationDelay = params.get("SuggestedPresentationDelay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """Channel ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Urls(self):
        """List of the URLs of the endpoints to delete
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        """List of the IDs of the channels to delete
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SuccessInfos = None
        self._FailInfos = None
        self._RequestId = None

    @property
    def SuccessInfos(self):
        """List of the information of successfully deleted channels
        :rtype: list of ChannelInfo
        """
        return self._SuccessInfos

    @SuccessInfos.setter
    def SuccessInfos(self, SuccessInfos):
        self._SuccessInfos = SuccessInfos

    @property
    def FailInfos(self):
        """List of the information of the channels that failed to be deleted
        :rtype: list of ChannelInfo
        """
        return self._FailInfos

    @FailInfos.setter
    def FailInfos(self, FailInfos):
        self._FailInfos = FailInfos

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
        """HarvestJob ID, a globally unique identifier.
        :rtype: str
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
        


class DeleteStreamPackageHarvestJobResponse(AbstractModel):
    """DeleteStreamPackageHarvestJob response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        """HarvestJob IDs, id is a globally unique identifier.
        :rtype: list of str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageLinearAssemblyChannelRequest(AbstractModel):
    """DeleteStreamPackageLinearAssemblyChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: channel id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """channel id.
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
        


class DeleteStreamPackageLinearAssemblyChannelResponse(AbstractModel):
    """DeleteStreamPackageLinearAssemblyChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageLinearAssemblyChannelsRequest(AbstractModel):
    """DeleteStreamPackageLinearAssemblyChannels request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: List of channel ids.
        :type Ids: list of str
        """
        self._Ids = None

    @property
    def Ids(self):
        """List of channel ids.
        :rtype: list of str
        """
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
        


class DeleteStreamPackageLinearAssemblyChannelsResponse(AbstractModel):
    """DeleteStreamPackageLinearAssemblyChannels response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageLinearAssemblyProgramRequest(AbstractModel):
    """DeleteStreamPackageLinearAssemblyProgram request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Program id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """Program id.
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
        


class DeleteStreamPackageLinearAssemblyProgramResponse(AbstractModel):
    """DeleteStreamPackageLinearAssemblyProgram response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageLinearAssemblyProgramsRequest(AbstractModel):
    """DeleteStreamPackageLinearAssemblyPrograms request structure.

    """

    def __init__(self):
        r"""
        :param _Ids: Program id list.
        :type Ids: list of str
        """
        self._Ids = None

    @property
    def Ids(self):
        """Program id list.
        :rtype: list of str
        """
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
        


class DeleteStreamPackageLinearAssemblyProgramsResponse(AbstractModel):
    """DeleteStreamPackageLinearAssemblyPrograms response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageSSAIChannelRequest(AbstractModel):
    """DeleteStreamPackageSSAIChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Ad insertion configuration ID that needs to be deleted
        :type ID: str
        """
        self._ID = None

    @property
    def ID(self):
        """Ad insertion configuration ID that needs to be deleted
        :rtype: str
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
        


class DeleteStreamPackageSSAIChannelResponse(AbstractModel):
    """DeleteStreamPackageSSAIChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageSourceLocationRequest(AbstractModel):
    """DeleteStreamPackageSourceLocation request structure.

    """

    def __init__(self):
        r"""
        :param _Id: SourceLocation Id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """SourceLocation Id.
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
        


class DeleteStreamPackageSourceLocationResponse(AbstractModel):
    """DeleteStreamPackageSourceLocation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteStreamPackageSourceRequest(AbstractModel):
    """DeleteStreamPackageSource request structure.

    """

    def __init__(self):
        r"""
        :param _Id: SourceLocation Id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """SourceLocation Id.
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
        


class DeleteStreamPackageSourceResponse(AbstractModel):
    """DeleteStreamPackageSource response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DescribeLinearAssemblyCDNDomainWithChannelRequest(AbstractModel):
    """DescribeLinearAssemblyCDNDomainWithChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel Id.
        :type ChannelId: str
        """
        self._ChannelId = None

    @property
    def ChannelId(self):
        """Channel Id.
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
        


class DescribeLinearAssemblyCDNDomainWithChannelResponse(AbstractModel):
    """DescribeLinearAssemblyCDNDomainWithChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The CDN domain name information associated with the channel.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.CdnDomainInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """The CDN domain name information associated with the channel.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CdnDomainInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = CdnDomainInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeLinearAssemblyCDNDomainWithChannelsRequest(AbstractModel):
    """DescribeLinearAssemblyCDNDomainWithChannels request structure.

    """


class DescribeLinearAssemblyCDNDomainWithChannelsResponse(AbstractModel):
    """DescribeLinearAssemblyCDNDomainWithChannels response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The CDN domain name information associated with the channel.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.CdnDomainInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """The CDN domain name information associated with the channel.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CdnDomainInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = CdnDomainInfo()
            self._Info._deserialize(params.get("Info"))
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
        """Channel ID
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
        


class DescribeStreamPackageChannelResponse(AbstractModel):
    """DescribeStreamPackageChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Channel information
        :type Info: :class:`tencentcloud.mdp.v20200527.models.ChannelInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Channel information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ChannelInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        """Page number. Value range: [1, 1000]
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Number of entries per page. Value range: [1, 1000]
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """List of channel information
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: list of ChannelInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
    def PageSize(self):
        """Number of entries per page
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """Total number of entries
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        """Total number of pages
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        """HarvestJob ID, a globally unique identifier.
        :rtype: str
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
        


class DescribeStreamPackageHarvestJobResponse(AbstractModel):
    """DescribeStreamPackageHarvestJob response structure.

    """

    def __init__(self):
        r"""
        :param _Info: HarvestJob information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.HarvestJobResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """HarvestJob information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.HarvestJobResp`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        """The bound channel name. If not passed, all channels will be queried by default.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def PageNum(self):
        """Page number.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """PageSize.
        :rtype: int
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def Infos(self):
        """HarvestJob information list.
        :rtype: list of HarvestJobResp
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """Page number.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """PageSize
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """TotalNum
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

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


class DescribeStreamPackageLinearAssemblyChannelAlertsRequest(AbstractModel):
    """DescribeStreamPackageLinearAssemblyChannelAlerts request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID.
        :type ChannelId: str
        :param _StartTime: Query start time, Unix timestamp, supports queries in the last seven days.
        :type StartTime: int
        :param _EndTime: Query end time, Unix timestamp, supports queries in the last seven days.
        :type EndTime: int
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ChannelId(self):
        """Channel ID.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        """Query start time, Unix timestamp, supports queries in the last seven days.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query end time, Unix timestamp, supports queries in the last seven days.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageLinearAssemblyChannelAlertsResponse(AbstractModel):
    """DescribeStreamPackageLinearAssemblyChannelAlerts response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Channel alarm information.
        :type Infos: :class:`tencentcloud.mdp.v20200527.models.ChannelAlertResp`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        """Channel alarm information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ChannelAlertResp`
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
        if params.get("Infos") is not None:
            self._Infos = ChannelAlertResp()
            self._Infos._deserialize(params.get("Infos"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageLinearAssemblyChannelRequest(AbstractModel):
    """DescribeStreamPackageLinearAssemblyChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: channel id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """channel id.
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
        


class DescribeStreamPackageLinearAssemblyChannelResponse(AbstractModel):
    """DescribeStreamPackageLinearAssemblyChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Channel information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyChannelInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Channel information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyChannelInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = LinearAssemblyChannelInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageLinearAssemblyChannelsRequest(AbstractModel):
    """DescribeStreamPackageLinearAssemblyChannels request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Paging query page number, the value range is [1, 1000].
        :type PageNum: int
        :param _PageSize: Paging query the size of each page, the value range is [1, 1000].
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        """Paging query page number, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Paging query the size of each page, the value range is [1, 1000].
        :rtype: int
        """
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
        


class DescribeStreamPackageLinearAssemblyChannelsResponse(AbstractModel):
    """DescribeStreamPackageLinearAssemblyChannels response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Channel list.
        :type Infos: list of LinearAssemblyChannelInfo
        :param _PageNum: Number of pages.
        :type PageNum: int
        :param _PageSize: Size per page.
        :type PageSize: int
        :param _TotalNum: The total amount.
        :type TotalNum: int
        :param _TotalPage: total pages.
        :type TotalPage: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Channel list.
        :rtype: list of LinearAssemblyChannelInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """Number of pages.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Size per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """The total amount.
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        """total pages.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = LinearAssemblyChannelInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageLinearAssemblyProgramRequest(AbstractModel):
    """DescribeStreamPackageLinearAssemblyProgram request structure.

    """

    def __init__(self):
        r"""
        :param _Id: program id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """program id.
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
        


class DescribeStreamPackageLinearAssemblyProgramResponse(AbstractModel):
    """DescribeStreamPackageLinearAssemblyProgram response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Program information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyProgramInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Program information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.LinearAssemblyProgramInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = LinearAssemblyProgramInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageLinearAssemblyProgramSchedulesRequest(AbstractModel):
    """DescribeStreamPackageLinearAssemblyProgramSchedules request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Query all Programs under a Channel.
        :type ChannelId: str
        :param _TimeWindow: Window duration information, in seconds.
        :type TimeWindow: int
        :param _PageNum: Paging query page number, the value range is [1, 1000].
        :type PageNum: int
        :param _PageSize: Paging query the size of each page, the value range is [1, 1000].
        :type PageSize: int
        """
        self._ChannelId = None
        self._TimeWindow = None
        self._PageNum = None
        self._PageSize = None

    @property
    def ChannelId(self):
        """Query all Programs under a Channel.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def TimeWindow(self):
        """Window duration information, in seconds.
        :rtype: int
        """
        return self._TimeWindow

    @TimeWindow.setter
    def TimeWindow(self, TimeWindow):
        self._TimeWindow = TimeWindow

    @property
    def PageNum(self):
        """Paging query page number, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Paging query the size of each page, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._TimeWindow = params.get("TimeWindow")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageLinearAssemblyProgramSchedulesResponse(AbstractModel):
    """DescribeStreamPackageLinearAssemblyProgramSchedules response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Program's scheduling list.
        :type Infos: list of LinearAssemblyProgramInfo
        :param _PageNum: Number of pages.
        :type PageNum: int
        :param _PageSize: Size per page.
        :type PageSize: int
        :param _TotalNum: The total amount.
        :type TotalNum: int
        :param _TotalPage: Total pages.
        :type TotalPage: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Program's scheduling list.
        :rtype: list of LinearAssemblyProgramInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """Number of pages.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Size per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """The total amount.
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        """Total pages.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = LinearAssemblyProgramInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageLinearAssemblyProgramsRequest(AbstractModel):
    """DescribeStreamPackageLinearAssemblyPrograms request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Paging query page number, the value range is [1, 1000].
        :type PageNum: int
        :param _PageSize: Paging query the size of each page, the value range is [1, 1000].
        :type PageSize: int
        :param _ChannelId: Query all Programs under a Channel.
        :type ChannelId: str
        """
        self._PageNum = None
        self._PageSize = None
        self._ChannelId = None

    @property
    def PageNum(self):
        """Paging query page number, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Paging query the size of each page, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def ChannelId(self):
        """Query all Programs under a Channel.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageLinearAssemblyProgramsResponse(AbstractModel):
    """DescribeStreamPackageLinearAssemblyPrograms response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Program list.
        :type Infos: list of LinearAssemblyProgramInfo
        :param _PageNum: Number of pages.
        :type PageNum: int
        :param _PageSize: Size per page.
        :type PageSize: int
        :param _TotalNum: The total amount.
        :type TotalNum: int
        :param _TotalPage: total pages.
        :type TotalPage: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Program list.
        :rtype: list of LinearAssemblyProgramInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """Number of pages.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Size per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """The total amount.
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        """total pages.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = LinearAssemblyProgramInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSSAIChannelRequest(AbstractModel):
    """DescribeStreamPackageSSAIChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ID: Ad insertion configuration ID
        :type ID: str
        """
        self._ID = None

    @property
    def ID(self):
        """Ad insertion configuration ID
        :rtype: str
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
        


class DescribeStreamPackageSSAIChannelResponse(AbstractModel):
    """DescribeStreamPackageSSAIChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Ad insertion configuration information
        :type Info: :class:`tencentcloud.mdp.v20200527.models.SSAIChannelInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Ad insertion configuration information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SSAIChannelInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = SSAIChannelInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSSAIChannelsRequest(AbstractModel):
    """DescribeStreamPackageSSAIChannels request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Page number, default is 1
        :type PageNum: int
        :param _PageSize: Page size, default is 10
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        """Page number, default is 1
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Page size, default is 10
        :rtype: int
        """
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
        


class DescribeStreamPackageSSAIChannelsResponse(AbstractModel):
    """DescribeStreamPackageSSAIChannels response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Ad insertion configuration information.
        :type Infos: list of SSAIChannelInfo
        :param _PageNum: Page number
        :type PageNum: int
        :param _PageSize: Page size
        :type PageSize: int
        :param _TotalNum: Total number
        :type TotalNum: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def Infos(self):
        """Ad insertion configuration information.
        :rtype: list of SSAIChannelInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
    def PageSize(self):
        """Page size
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """Total number
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = SSAIChannelInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSourceAlertsRequest(AbstractModel):
    """DescribeStreamPackageSourceAlerts request structure.

    """

    def __init__(self):
        r"""
        :param _SourceId: Source ID.
        :type SourceId: str
        :param _StartTime: Query start time, Unix timestamp, supports queries in the last seven days.
        :type StartTime: int
        :param _EndTime: Query end time, Unix timestamp, supports queries in the last seven days.
        :type EndTime: int
        """
        self._SourceId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SourceId(self):
        """Source ID.
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def StartTime(self):
        """Query start time, Unix timestamp, supports queries in the last seven days.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query end time, Unix timestamp, supports queries in the last seven days.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SourceId = params.get("SourceId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageSourceAlertsResponse(AbstractModel):
    """DescribeStreamPackageSourceAlerts response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Source alarm information.
        :type Infos: list of SourceAlert
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        """Source alarm information.
        :rtype: list of SourceAlert
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = SourceAlert()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSourceLocationAlertsRequest(AbstractModel):
    """DescribeStreamPackageSourceLocationAlerts request structure.

    """

    def __init__(self):
        r"""
        :param _LocationId: Location ID.
        :type LocationId: str
        """
        self._LocationId = None

    @property
    def LocationId(self):
        """Location ID.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageSourceLocationAlertsResponse(AbstractModel):
    """DescribeStreamPackageSourceLocationAlerts response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Location alarm information.
        :type Infos: list of LocationAlert
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        """Location alarm information.
        :rtype: list of LocationAlert
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = LocationAlert()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSourceLocationRequest(AbstractModel):
    """DescribeStreamPackageSourceLocation request structure.

    """

    def __init__(self):
        r"""
        :param _Id: SourceLocation Id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """SourceLocation Id.
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
        


class DescribeStreamPackageSourceLocationResponse(AbstractModel):
    """DescribeStreamPackageSourceLocation response structure.

    """

    def __init__(self):
        r"""
        :param _Info: SourceLocation information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.SourceLocationInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """SourceLocation information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SourceLocationInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = SourceLocationInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSourceLocationsRequest(AbstractModel):
    """DescribeStreamPackageSourceLocations request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Paging query page number, the value range is [1, 1000].
        :type PageNum: int
        :param _PageSize: Paging query the size of each page, the value range is [1, 1000].
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        """Paging query page number, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Paging query the size of each page, the value range is [1, 1000].
        :rtype: int
        """
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
        


class DescribeStreamPackageSourceLocationsResponse(AbstractModel):
    """DescribeStreamPackageSourceLocations response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: SourceLocation list.
        :type Infos: list of SourceLocationInfo
        :param _PageNum: Number of pages.
        :type PageNum: int
        :param _PageSize: Size per page.
        :type PageSize: int
        :param _TotalNum: The total amount.
        :type TotalNum: int
        :param _TotalPage: total pages.
        :type TotalPage: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """SourceLocation list.
        :rtype: list of SourceLocationInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """Number of pages.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Size per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """The total amount.
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        """total pages.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = SourceLocationInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSourceRequest(AbstractModel):
    """DescribeStreamPackageSource request structure.

    """

    def __init__(self):
        r"""
        :param _Id: SourceLocation Id.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """SourceLocation Id.
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
        


class DescribeStreamPackageSourceResponse(AbstractModel):
    """DescribeStreamPackageSource response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Source information.
        :type Info: :class:`tencentcloud.mdp.v20200527.models.SourceInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Source information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SourceInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = SourceInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamPackageSourcesRequest(AbstractModel):
    """DescribeStreamPackageSources request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Paging query page number, the value range is [1, 1000].
        :type PageNum: int
        :param _PageSize: Paging query the size of each page, the value range is [1, 1000].
        :type PageSize: int
        :param _LocationId: Location Id, query all sources under the location.
        :type LocationId: str
        :param _Type: The type of source is divided into live broadcast and on-demand VOD.
Optional values: Live, VOD.
        :type Type: str
        """
        self._PageNum = None
        self._PageSize = None
        self._LocationId = None
        self._Type = None

    @property
    def PageNum(self):
        """Paging query page number, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Paging query the size of each page, the value range is [1, 1000].
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def LocationId(self):
        """Location Id, query all sources under the location.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Type(self):
        """The type of source is divided into live broadcast and on-demand VOD.
Optional values: Live, VOD.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._LocationId = params.get("LocationId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPackageSourcesResponse(AbstractModel):
    """DescribeStreamPackageSources response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Source list.
        :type Infos: list of SourceInfo
        :param _PageNum: Number of pages.
        :type PageNum: int
        :param _PageSize: Size per page.
        :type PageSize: int
        :param _TotalNum: The total amount.
        :type TotalNum: int
        :param _TotalPage: total pages.
        :type TotalPage: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
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
        """Source list.
        :rtype: list of SourceInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """Number of pages.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Size per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """The total amount.
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        """total pages.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = SourceInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DomainRecordInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _CdnDomain: 
        :type CdnDomain: str
        :param _Region: 
        :type Region: str
        :param _ChannelId: 
        :type ChannelId: str
        :param _Id: 
        :type Id: str
        """
        self._CdnDomain = None
        self._Region = None
        self._ChannelId = None
        self._Id = None

    @property
    def CdnDomain(self):
        """
        :rtype: str
        """
        return self._CdnDomain

    @CdnDomain.setter
    def CdnDomain(self, CdnDomain):
        self._CdnDomain = CdnDomain

    @property
    def Region(self):
        """
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ChannelId(self):
        """
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Id(self):
        """
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._CdnDomain = params.get("CdnDomain")
        self._Region = params.get("Region")
        self._ChannelId = params.get("ChannelId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """The security group allowlist in CIDR format.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList

    @property
    def BlackIpList(self):
        """The security group blocklist in CIDR format.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def AuthKey(self):
        """The authentication key. Its value is same as `X-TENCENT-PACKAGE` set in the HTTP request header.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        :param _Protocol: Endpoint protocol, supports `HLS`, `CMAF`, `CMAF-HLS`.
        :type Protocol: str
        :param _Manifest: Manifest name, default is main.
        :type Manifest: str
        :param _TimeShiftEnable: Whether to turn on the time shift function, true: on, false: off, the default is off.
        :type TimeShiftEnable: bool
        :param _TimeShiftDuration: The number of days in the time shift window, up to 30 days. Valid when TimeShiftEnable is turned on.
        :type TimeShiftDuration: int
        :param _SSAIEnable: Advertising insertion function switch.
        :type SSAIEnable: bool
        :param _SSAIInfo: Ad insertion function configuration information.
        :type SSAIInfo: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        :param _CustomUrlParamIndex: The customer-defined url parameter is inserted into the subscript at the specified position of the Endpoint url. The optional range of the subscript is: [0,3].
        :type CustomUrlParamIndex: int
        :param _CustomUrlParam: Customer-defined url parameters are inserted into the specified position of the Endpoint url based on the CustomUrlParamIndex.
The parameters can only contain digits, letters, underscores (_), and hyphens (-), with a length of 1 to 64 chars.
        :type CustomUrlParam: str
        :param _DRMEnabled: DRM switch. If it is turned on, only CMAF will take effect.
        :type DRMEnabled: bool
        :param _DRMInfo: DRM configuration information.
        :type DRMInfo: :class:`tencentcloud.mdp.v20200527.models.DRMInfo`
        """
        self._Name = None
        self._Url = None
        self._AuthInfo = None
        self._Protocol = None
        self._Manifest = None
        self._TimeShiftEnable = None
        self._TimeShiftDuration = None
        self._SSAIEnable = None
        self._SSAIInfo = None
        self._CustomUrlParamIndex = None
        self._CustomUrlParam = None
        self._DRMEnabled = None
        self._DRMInfo = None

    @property
    def Name(self):
        """Endpoint name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        """Endpoint URL.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AuthInfo(self):
        """Endpoint authentication information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def Protocol(self):
        """Endpoint protocol, supports `HLS`, `CMAF`, `CMAF-HLS`.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Manifest(self):
        """Manifest name, default is main.
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def TimeShiftEnable(self):
        """Whether to turn on the time shift function, true: on, false: off, the default is off.
        :rtype: bool
        """
        return self._TimeShiftEnable

    @TimeShiftEnable.setter
    def TimeShiftEnable(self, TimeShiftEnable):
        self._TimeShiftEnable = TimeShiftEnable

    @property
    def TimeShiftDuration(self):
        """The number of days in the time shift window, up to 30 days. Valid when TimeShiftEnable is turned on.
        :rtype: int
        """
        return self._TimeShiftDuration

    @TimeShiftDuration.setter
    def TimeShiftDuration(self, TimeShiftDuration):
        self._TimeShiftDuration = TimeShiftDuration

    @property
    def SSAIEnable(self):
        """Advertising insertion function switch.
        :rtype: bool
        """
        return self._SSAIEnable

    @SSAIEnable.setter
    def SSAIEnable(self, SSAIEnable):
        self._SSAIEnable = SSAIEnable

    @property
    def SSAIInfo(self):
        """Ad insertion function configuration information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        """
        return self._SSAIInfo

    @SSAIInfo.setter
    def SSAIInfo(self, SSAIInfo):
        self._SSAIInfo = SSAIInfo

    @property
    def CustomUrlParamIndex(self):
        """The customer-defined url parameter is inserted into the subscript at the specified position of the Endpoint url. The optional range of the subscript is: [0,3].
        :rtype: int
        """
        return self._CustomUrlParamIndex

    @CustomUrlParamIndex.setter
    def CustomUrlParamIndex(self, CustomUrlParamIndex):
        self._CustomUrlParamIndex = CustomUrlParamIndex

    @property
    def CustomUrlParam(self):
        """Customer-defined url parameters are inserted into the specified position of the Endpoint url based on the CustomUrlParamIndex.
The parameters can only contain digits, letters, underscores (_), and hyphens (-), with a length of 1 to 64 chars.
        :rtype: str
        """
        return self._CustomUrlParam

    @CustomUrlParam.setter
    def CustomUrlParam(self, CustomUrlParam):
        self._CustomUrlParam = CustomUrlParam

    @property
    def DRMEnabled(self):
        """DRM switch. If it is turned on, only CMAF will take effect.
        :rtype: bool
        """
        return self._DRMEnabled

    @DRMEnabled.setter
    def DRMEnabled(self, DRMEnabled):
        self._DRMEnabled = DRMEnabled

    @property
    def DRMInfo(self):
        """DRM configuration information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DRMInfo`
        """
        return self._DRMInfo

    @DRMInfo.setter
    def DRMInfo(self, DRMInfo):
        self._DRMInfo = DRMInfo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = EndpointAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        self._Protocol = params.get("Protocol")
        self._Manifest = params.get("Manifest")
        self._TimeShiftEnable = params.get("TimeShiftEnable")
        self._TimeShiftDuration = params.get("TimeShiftDuration")
        self._SSAIEnable = params.get("SSAIEnable")
        if params.get("SSAIInfo") is not None:
            self._SSAIInfo = SSAIConf()
            self._SSAIInfo._deserialize(params.get("SSAIInfo"))
        self._CustomUrlParamIndex = params.get("CustomUrlParamIndex")
        self._CustomUrlParam = params.get("CustomUrlParam")
        self._DRMEnabled = params.get("DRMEnabled")
        if params.get("DRMInfo") is not None:
            self._DRMInfo = DRMInfo()
            self._DRMInfo._deserialize(params.get("DRMInfo"))
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
        """HarvestJob ID, a globally unique identifier.
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def ChannelName(self):
        """The associated channel name.
        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def EndpointName(self):
        """The associated endpoint name.
        :rtype: str
        """
        return self._EndpointName

    @EndpointName.setter
    def EndpointName(self, EndpointName):
        self._EndpointName = EndpointName

    @property
    def TimeFormat(self):
        """Time format, supports the following types: 1. Epoch seconds 2. ISO-8601
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def StartTime(self):
        """HarvestJob start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """HarvestJob end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Destination(self):
        """The path where the recording file is stored in COS.
        :rtype: str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Manifest(self):
        """The file name of the recording file stored in COS.
        :rtype: str
        """
        return self._Manifest

    @Manifest.setter
    def Manifest(self, Manifest):
        self._Manifest = Manifest

    @property
    def Status(self):
        """The task status is divided into running: Running, execution completed: Completed, and execution failure: Failed.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMessage(self):
        """HarvestJob error message.
        :rtype: str
        """
        return self._ErrMessage

    @ErrMessage.setter
    def ErrMessage(self, ErrMessage):
        self._ErrMessage = ErrMessage

    @property
    def CreateTime(self):
        """HarvestJob creation time, timestamp in seconds.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ChannelId(self):
        """The associated ChannelID.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Region(self):
        """The region corresponding to the harvest job.
        :rtype: str
        """
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
        """Username.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """Password.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        """Channel input URL.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def AuthInfo(self):
        """Channel input authentication information.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.InputAuthInfo`
        """
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
        


class LinearAssemblyChannelInfo(AbstractModel):
    """Linearly assembled channel information.

    """

    def __init__(self):
        r"""
        :param _Name: Linear assembly channel name.
        :type Name: str
        :param _Tier: Define the characteristics of the channel. Standard supports live broadcast and on-demand sources, while Basic only supports on-demand source arrangement.
        :type Tier: str
        :param _PlaybackMode: The source switching mode in the channel is divided into Linear and Loop. Live broadcast only supports Linear.
        :type PlaybackMode: str
        :param _TimeShiftConf: Time shift configuration, vod is valid.
        :type TimeShiftConf: :class:`tencentcloud.mdp.v20200527.models.TimeShiftInfo`
        :param _SlateConf: Spacer configuration.
        :type SlateConf: :class:`tencentcloud.mdp.v20200527.models.SlateInfo`
        :param _Outputs: output information.
        :type Outputs: list of OutputInfo
        :param _AttachedPrograms: List of programs bound to this channel.
        :type AttachedPrograms: list of str
        :param _ProgramSchedules: program information.
        :type ProgramSchedules: list of ProgramScheduleInfo
        :param _Id: ID.
        :type Id: str
        :param _Region: Region.
        :type Region: str
        :param _State: State.
        :type State: str
        :param _TimeShiftEnable: Time shift on switch.
        :type TimeShiftEnable: bool
        :param _CreateTime: Channel creation time, unix seconds timestamp.
        :type CreateTime: int
        """
        self._Name = None
        self._Tier = None
        self._PlaybackMode = None
        self._TimeShiftConf = None
        self._SlateConf = None
        self._Outputs = None
        self._AttachedPrograms = None
        self._ProgramSchedules = None
        self._Id = None
        self._Region = None
        self._State = None
        self._TimeShiftEnable = None
        self._CreateTime = None

    @property
    def Name(self):
        """Linear assembly channel name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tier(self):
        """Define the characteristics of the channel. Standard supports live broadcast and on-demand sources, while Basic only supports on-demand source arrangement.
        :rtype: str
        """
        return self._Tier

    @Tier.setter
    def Tier(self, Tier):
        self._Tier = Tier

    @property
    def PlaybackMode(self):
        """The source switching mode in the channel is divided into Linear and Loop. Live broadcast only supports Linear.
        :rtype: str
        """
        return self._PlaybackMode

    @PlaybackMode.setter
    def PlaybackMode(self, PlaybackMode):
        self._PlaybackMode = PlaybackMode

    @property
    def TimeShiftConf(self):
        """Time shift configuration, vod is valid.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.TimeShiftInfo`
        """
        return self._TimeShiftConf

    @TimeShiftConf.setter
    def TimeShiftConf(self, TimeShiftConf):
        self._TimeShiftConf = TimeShiftConf

    @property
    def SlateConf(self):
        """Spacer configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SlateInfo`
        """
        return self._SlateConf

    @SlateConf.setter
    def SlateConf(self, SlateConf):
        self._SlateConf = SlateConf

    @property
    def Outputs(self):
        """output information.
        :rtype: list of OutputInfo
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def AttachedPrograms(self):
        """List of programs bound to this channel.
        :rtype: list of str
        """
        return self._AttachedPrograms

    @AttachedPrograms.setter
    def AttachedPrograms(self, AttachedPrograms):
        self._AttachedPrograms = AttachedPrograms

    @property
    def ProgramSchedules(self):
        """program information.
        :rtype: list of ProgramScheduleInfo
        """
        return self._ProgramSchedules

    @ProgramSchedules.setter
    def ProgramSchedules(self, ProgramSchedules):
        self._ProgramSchedules = ProgramSchedules

    @property
    def Id(self):
        """ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Region(self):
        """Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def State(self):
        """State.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def TimeShiftEnable(self):
        """Time shift on switch.
        :rtype: bool
        """
        return self._TimeShiftEnable

    @TimeShiftEnable.setter
    def TimeShiftEnable(self, TimeShiftEnable):
        self._TimeShiftEnable = TimeShiftEnable

    @property
    def CreateTime(self):
        """Channel creation time, unix seconds timestamp.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Tier = params.get("Tier")
        self._PlaybackMode = params.get("PlaybackMode")
        if params.get("TimeShiftConf") is not None:
            self._TimeShiftConf = TimeShiftInfo()
            self._TimeShiftConf._deserialize(params.get("TimeShiftConf"))
        if params.get("SlateConf") is not None:
            self._SlateConf = SlateInfo()
            self._SlateConf._deserialize(params.get("SlateConf"))
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = OutputInfo()
                obj._deserialize(item)
                self._Outputs.append(obj)
        self._AttachedPrograms = params.get("AttachedPrograms")
        if params.get("ProgramSchedules") is not None:
            self._ProgramSchedules = []
            for item in params.get("ProgramSchedules"):
                obj = ProgramScheduleInfo()
                obj._deserialize(item)
                self._ProgramSchedules.append(obj)
        self._Id = params.get("Id")
        self._Region = params.get("Region")
        self._State = params.get("State")
        self._TimeShiftEnable = params.get("TimeShiftEnable")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LinearAssemblyProgramInfo(AbstractModel):
    """Channel linear assembly program information.

    """

    def __init__(self):
        r"""
        :param _Name: Channel linear assembly program information.
        :type Name: str
        :param _SourceType: The type of the arrangement target source, divided into live broadcast and on-demand.
        :type SourceType: str
        :param _SourceLocationId: The associated source location id.
        :type SourceLocationId: str
        :param _SourceId: SourceId, uniquely identifies a source.
        :type SourceId: str
        :param _SourceName: The associated live broadcast or on-demand broadcast, source name, and location are globally unique.
        :type SourceName: str
        :param _AttachedChannel: The bound channel.
        :type AttachedChannel: str
        :param _PlaybackConf: Play configuration.
        :type PlaybackConf: :class:`tencentcloud.mdp.v20200527.models.PlaybackInfo`
        :param _AdBreaks: AdBreaks.
        :type AdBreaks: list of AdBreakInfo
        :param _Id: ID.
        :type Id: str
        :param _Region: Region.
        :type Region: str
        :param _SourceLocationName: SourceLocation name.
        :type SourceLocationName: str
        """
        self._Name = None
        self._SourceType = None
        self._SourceLocationId = None
        self._SourceId = None
        self._SourceName = None
        self._AttachedChannel = None
        self._PlaybackConf = None
        self._AdBreaks = None
        self._Id = None
        self._Region = None
        self._SourceLocationName = None

    @property
    def Name(self):
        """Channel linear assembly program information.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceType(self):
        """The type of the arrangement target source, divided into live broadcast and on-demand.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceLocationId(self):
        """The associated source location id.
        :rtype: str
        """
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def SourceId(self):
        """SourceId, uniquely identifies a source.
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceName(self):
        """The associated live broadcast or on-demand broadcast, source name, and location are globally unique.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def AttachedChannel(self):
        """The bound channel.
        :rtype: str
        """
        return self._AttachedChannel

    @AttachedChannel.setter
    def AttachedChannel(self, AttachedChannel):
        self._AttachedChannel = AttachedChannel

    @property
    def PlaybackConf(self):
        """Play configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.PlaybackInfo`
        """
        return self._PlaybackConf

    @PlaybackConf.setter
    def PlaybackConf(self, PlaybackConf):
        self._PlaybackConf = PlaybackConf

    @property
    def AdBreaks(self):
        """AdBreaks.
        :rtype: list of AdBreakInfo
        """
        return self._AdBreaks

    @AdBreaks.setter
    def AdBreaks(self, AdBreaks):
        self._AdBreaks = AdBreaks

    @property
    def Id(self):
        """ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Region(self):
        """Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def SourceLocationName(self):
        """SourceLocation name.
        :rtype: str
        """
        return self._SourceLocationName

    @SourceLocationName.setter
    def SourceLocationName(self, SourceLocationName):
        self._SourceLocationName = SourceLocationName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._SourceType = params.get("SourceType")
        self._SourceLocationId = params.get("SourceLocationId")
        self._SourceId = params.get("SourceId")
        self._SourceName = params.get("SourceName")
        self._AttachedChannel = params.get("AttachedChannel")
        if params.get("PlaybackConf") is not None:
            self._PlaybackConf = PlaybackInfo()
            self._PlaybackConf._deserialize(params.get("PlaybackConf"))
        if params.get("AdBreaks") is not None:
            self._AdBreaks = []
            for item in params.get("AdBreaks"):
                obj = AdBreakInfo()
                obj._deserialize(item)
                self._AdBreaks.append(obj)
        self._Id = params.get("Id")
        self._Region = params.get("Region")
        self._SourceLocationName = params.get("SourceLocationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocationAlert(AbstractModel):
    """Channel Linear Assembly Location Alarm Information.

    """

    def __init__(self):
        r"""
        :param _LocationId: Location ID.
        :type LocationId: str
        :param _Code: Alarm event code.
        :type Code: int
        :param _Category: Alarm classification.
        :type Category: str
        :param _Message: Alarm message.
        :type Message: str
        :param _LastModifiedTime: Update time.
        :type LastModifiedTime: int
        :param _LocationName: Location name.
        :type LocationName: str
        """
        self._LocationId = None
        self._Code = None
        self._Category = None
        self._Message = None
        self._LastModifiedTime = None
        self._LocationName = None

    @property
    def LocationId(self):
        """Location ID.
        :rtype: str
        """
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Code(self):
        """Alarm event code.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Category(self):
        """Alarm classification.
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Message(self):
        """Alarm message.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def LastModifiedTime(self):
        """Update time.
        :rtype: int
        """
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime

    @property
    def LocationName(self):
        """Location name.
        :rtype: str
        """
        return self._LocationName

    @LocationName.setter
    def LocationName(self, LocationName):
        self._LocationName = LocationName


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Code = params.get("Code")
        self._Category = params.get("Category")
        self._Message = params.get("Message")
        self._LastModifiedTime = params.get("LastModifiedTime")
        self._LocationName = params.get("LocationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManifestInfo(AbstractModel):
    """Linear assembly channel configuration.

    """

    def __init__(self):
        r"""
        :param _Windows: Time window, in seconds.
        :type Windows: int
        :param _AdMarkupType: Enter the format of the output advertising tag. Optional values are: Date Range and Enhanced SCTE-35.
        :type AdMarkupType: str
        """
        self._Windows = None
        self._AdMarkupType = None

    @property
    def Windows(self):
        """Time window, in seconds.
        :rtype: int
        """
        return self._Windows

    @Windows.setter
    def Windows(self, Windows):
        self._Windows = Windows

    @property
    def AdMarkupType(self):
        """Enter the format of the output advertising tag. Optional values are: Date Range and Enhanced SCTE-35.
        :rtype: str
        """
        return self._AdMarkupType

    @AdMarkupType.setter
    def AdMarkupType(self, AdMarkupType):
        self._AdMarkupType = AdMarkupType


    def _deserialize(self, params):
        self._Windows = params.get("Windows")
        self._AdMarkupType = params.get("AdMarkupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Metadata(AbstractModel):
    """Metadata.

    """

    def __init__(self):
        r"""
        :param _Key: Key.
        :type Key: str
        :param _Value: Value.
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Key.
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Value.
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
        :param _Protocol: Endpoint protocol.
        :type Protocol: str
        :param _TimeShiftEnable: Whether to turn on the time shift function, true: on, false: off, the default is off.
        :type TimeShiftEnable: bool
        :param _TimeShiftDuration: The number of days in the time shift window, up to 30 days. Valid when TimeShiftEnable is turned on.
        :type TimeShiftDuration: int
        :param _SSAIEnable: Advertising insertion function switch.
        :type SSAIEnable: bool
        :param _SSAIInfo: Ad insertion function configuration information. Valid when SSAIEnable is turned on.
        :type SSAIInfo: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        :param _CustomUrlParamIndex: The customer-defined url parameter is inserted into the subscript at the specified position of the Endpoint url. 
Calculation starts from the first '/' in the url path, and the subscript starts from 0, the optional range of the subscript is: [0,3].
        :type CustomUrlParamIndex: int
        :param _CustomUrlParam: Customer-defined url parameters are inserted into the specified position of the Endpoint url based on the CustomUrlParamIndex.
The parameters can only contain digits, letters, underscores (_), and hyphens (-), with a length of 1 to 64 chars.
        :type CustomUrlParam: str
        """
        self._Id = None
        self._Url = None
        self._Name = None
        self._AuthInfo = None
        self._Protocol = None
        self._TimeShiftEnable = None
        self._TimeShiftDuration = None
        self._SSAIEnable = None
        self._SSAIInfo = None
        self._CustomUrlParamIndex = None
        self._CustomUrlParam = None

    @property
    def Id(self):
        """Channel ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        """Channel endpoint URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Name(self):
        """New endpoint name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AuthInfo(self):
        """New channel authentication information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.EndpointAuthInfo`
        """
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def Protocol(self):
        """Endpoint protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def TimeShiftEnable(self):
        """Whether to turn on the time shift function, true: on, false: off, the default is off.
        :rtype: bool
        """
        return self._TimeShiftEnable

    @TimeShiftEnable.setter
    def TimeShiftEnable(self, TimeShiftEnable):
        self._TimeShiftEnable = TimeShiftEnable

    @property
    def TimeShiftDuration(self):
        """The number of days in the time shift window, up to 30 days. Valid when TimeShiftEnable is turned on.
        :rtype: int
        """
        return self._TimeShiftDuration

    @TimeShiftDuration.setter
    def TimeShiftDuration(self, TimeShiftDuration):
        self._TimeShiftDuration = TimeShiftDuration

    @property
    def SSAIEnable(self):
        """Advertising insertion function switch.
        :rtype: bool
        """
        return self._SSAIEnable

    @SSAIEnable.setter
    def SSAIEnable(self, SSAIEnable):
        self._SSAIEnable = SSAIEnable

    @property
    def SSAIInfo(self):
        """Ad insertion function configuration information. Valid when SSAIEnable is turned on.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        """
        return self._SSAIInfo

    @SSAIInfo.setter
    def SSAIInfo(self, SSAIInfo):
        self._SSAIInfo = SSAIInfo

    @property
    def CustomUrlParamIndex(self):
        """The customer-defined url parameter is inserted into the subscript at the specified position of the Endpoint url. 
Calculation starts from the first '/' in the url path, and the subscript starts from 0, the optional range of the subscript is: [0,3].
        :rtype: int
        """
        return self._CustomUrlParamIndex

    @CustomUrlParamIndex.setter
    def CustomUrlParamIndex(self, CustomUrlParamIndex):
        self._CustomUrlParamIndex = CustomUrlParamIndex

    @property
    def CustomUrlParam(self):
        """Customer-defined url parameters are inserted into the specified position of the Endpoint url based on the CustomUrlParamIndex.
The parameters can only contain digits, letters, underscores (_), and hyphens (-), with a length of 1 to 64 chars.
        :rtype: str
        """
        return self._CustomUrlParam

    @CustomUrlParam.setter
    def CustomUrlParam(self, CustomUrlParam):
        self._CustomUrlParam = CustomUrlParam


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Url = params.get("Url")
        self._Name = params.get("Name")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = EndpointAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        self._Protocol = params.get("Protocol")
        self._TimeShiftEnable = params.get("TimeShiftEnable")
        self._TimeShiftDuration = params.get("TimeShiftDuration")
        self._SSAIEnable = params.get("SSAIEnable")
        if params.get("SSAIInfo") is not None:
            self._SSAIInfo = SSAIConf()
            self._SSAIInfo._deserialize(params.get("SSAIInfo"))
        self._CustomUrlParamIndex = params.get("CustomUrlParamIndex")
        self._CustomUrlParam = params.get("CustomUrlParam")
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        """Channel ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Url(self):
        """Channel input URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def ActionType(self):
        """Authentication configuration. Valid values: `CLOSE`, `UPDATE`
`CLOSE`: disable authentication
`UPDATE`: update authentication information
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AuthInfo = None
        self._RequestId = None

    @property
    def AuthInfo(self):
        """Channel input authentication information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.InputAuthInfo`
        """
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

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
        if params.get("AuthInfo") is not None:
            self._AuthInfo = InputAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        self._RequestId = params.get("RequestId")


class ModifyStreamPackageChannelRequest(AbstractModel):
    """ModifyStreamPackageChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID.
        :type Id: str
        :param _Name: New channel name.
        :type Name: str
        :param _Protocol: New channel protocol. Valid values: HLS, DASH, CMAF.
        :type Protocol: str
        :param _CacheInfo: Cache configuration.
        :type CacheInfo: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
        self._Id = None
        self._Name = None
        self._Protocol = None
        self._CacheInfo = None

    @property
    def Id(self):
        """Channel ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """New channel name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        """New channel protocol. Valid values: HLS, DASH, CMAF.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CacheInfo(self):
        """Cache configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.CacheInfo`
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyStreamPackageLinearAssemblyChannelRequest(AbstractModel):
    """ModifyStreamPackageLinearAssemblyChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID.
        :type Id: str
        :param _Name: Modified name.
        :type Name: str
        :param _Tier: Define the characteristics of the channel. Standard supports live broadcast and on-demand sources, while Basic only supports on-demand source arrangement.
        :type Tier: str
        :param _PlaybackMode: The source switching mode in the channel is divided into Linear and Loop. Live broadcast only supports Linear.
Optional values: Linear, Loop.
        :type PlaybackMode: str
        :param _TimeShiftEnable: Time shift on switch.
        :type TimeShiftEnable: bool
        :param _TimeShiftConf: Time shift configuration.
        :type TimeShiftConf: :class:`tencentcloud.mdp.v20200527.models.TimeShiftInfo`
        :param _SlateConf: padding configuration.
        :type SlateConf: :class:`tencentcloud.mdp.v20200527.models.SlateInfo`
        :param _Outputs: Output configuration.
        :type Outputs: list of OutputInfo
        """
        self._Id = None
        self._Name = None
        self._Tier = None
        self._PlaybackMode = None
        self._TimeShiftEnable = None
        self._TimeShiftConf = None
        self._SlateConf = None
        self._Outputs = None

    @property
    def Id(self):
        """Channel ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Modified name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tier(self):
        """Define the characteristics of the channel. Standard supports live broadcast and on-demand sources, while Basic only supports on-demand source arrangement.
        :rtype: str
        """
        return self._Tier

    @Tier.setter
    def Tier(self, Tier):
        self._Tier = Tier

    @property
    def PlaybackMode(self):
        """The source switching mode in the channel is divided into Linear and Loop. Live broadcast only supports Linear.
Optional values: Linear, Loop.
        :rtype: str
        """
        return self._PlaybackMode

    @PlaybackMode.setter
    def PlaybackMode(self, PlaybackMode):
        self._PlaybackMode = PlaybackMode

    @property
    def TimeShiftEnable(self):
        """Time shift on switch.
        :rtype: bool
        """
        return self._TimeShiftEnable

    @TimeShiftEnable.setter
    def TimeShiftEnable(self, TimeShiftEnable):
        self._TimeShiftEnable = TimeShiftEnable

    @property
    def TimeShiftConf(self):
        """Time shift configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.TimeShiftInfo`
        """
        return self._TimeShiftConf

    @TimeShiftConf.setter
    def TimeShiftConf(self, TimeShiftConf):
        self._TimeShiftConf = TimeShiftConf

    @property
    def SlateConf(self):
        """padding configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SlateInfo`
        """
        return self._SlateConf

    @SlateConf.setter
    def SlateConf(self, SlateConf):
        self._SlateConf = SlateConf

    @property
    def Outputs(self):
        """Output configuration.
        :rtype: list of OutputInfo
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Tier = params.get("Tier")
        self._PlaybackMode = params.get("PlaybackMode")
        self._TimeShiftEnable = params.get("TimeShiftEnable")
        if params.get("TimeShiftConf") is not None:
            self._TimeShiftConf = TimeShiftInfo()
            self._TimeShiftConf._deserialize(params.get("TimeShiftConf"))
        if params.get("SlateConf") is not None:
            self._SlateConf = SlateInfo()
            self._SlateConf._deserialize(params.get("SlateConf"))
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = OutputInfo()
                obj._deserialize(item)
                self._Outputs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageLinearAssemblyChannelResponse(AbstractModel):
    """ModifyStreamPackageLinearAssemblyChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyStreamPackageLinearAssemblyProgramRequest(AbstractModel):
    """ModifyStreamPackageLinearAssemblyProgram request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Program ID.
        :type Id: str
        :param _Name: Modified name.
        :type Name: str
        :param _SourceType: The type of the arrangement target source, divided into live broadcast and on-demand.
        :type SourceType: str
        :param _SourceLocationId: The associated source location.
        :type SourceLocationId: str
        :param _SourceName: The associated live broadcast or on-demand broadcast, source name, and location are globally unique.
        :type SourceName: str
        :param _PlaybackConf: PlaybackConf.
        :type PlaybackConf: :class:`tencentcloud.mdp.v20200527.models.PlaybackInfoReq`
        :param _AdBreaks: AdBreaks.
        :type AdBreaks: list of AdBreakInfo
        """
        self._Id = None
        self._Name = None
        self._SourceType = None
        self._SourceLocationId = None
        self._SourceName = None
        self._PlaybackConf = None
        self._AdBreaks = None

    @property
    def Id(self):
        """Program ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Modified name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SourceType(self):
        """The type of the arrangement target source, divided into live broadcast and on-demand.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceLocationId(self):
        """The associated source location.
        :rtype: str
        """
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def SourceName(self):
        """The associated live broadcast or on-demand broadcast, source name, and location are globally unique.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def PlaybackConf(self):
        """PlaybackConf.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.PlaybackInfoReq`
        """
        return self._PlaybackConf

    @PlaybackConf.setter
    def PlaybackConf(self, PlaybackConf):
        self._PlaybackConf = PlaybackConf

    @property
    def AdBreaks(self):
        """AdBreaks.
        :rtype: list of AdBreakInfo
        """
        return self._AdBreaks

    @AdBreaks.setter
    def AdBreaks(self, AdBreaks):
        self._AdBreaks = AdBreaks


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._SourceType = params.get("SourceType")
        self._SourceLocationId = params.get("SourceLocationId")
        self._SourceName = params.get("SourceName")
        if params.get("PlaybackConf") is not None:
            self._PlaybackConf = PlaybackInfoReq()
            self._PlaybackConf._deserialize(params.get("PlaybackConf"))
        if params.get("AdBreaks") is not None:
            self._AdBreaks = []
            for item in params.get("AdBreaks"):
                obj = AdBreakInfo()
                obj._deserialize(item)
                self._AdBreaks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageLinearAssemblyProgramResponse(AbstractModel):
    """ModifyStreamPackageLinearAssemblyProgram response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyStreamPackageSSAIChannelRequest(AbstractModel):
    """ModifyStreamPackageSSAIChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Ad insertion configuration name, globally unique, cannot be repeated.
        :type Name: str
        :param _ContentSource: Content source prefix.
        :type ContentSource: str
        :param _SSAIInfo: Ad insertion configuration information
        :type SSAIInfo: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        :param _ID: Ad insertion configuration ID
        :type ID: str
        """
        self._Name = None
        self._ContentSource = None
        self._SSAIInfo = None
        self._ID = None

    @property
    def Name(self):
        """Ad insertion configuration name, globally unique, cannot be repeated.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContentSource(self):
        """Content source prefix.
        :rtype: str
        """
        return self._ContentSource

    @ContentSource.setter
    def ContentSource(self, ContentSource):
        self._ContentSource = ContentSource

    @property
    def SSAIInfo(self):
        """Ad insertion configuration information
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        """
        return self._SSAIInfo

    @SSAIInfo.setter
    def SSAIInfo(self, SSAIInfo):
        self._SSAIInfo = SSAIInfo

    @property
    def ID(self):
        """Ad insertion configuration ID
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ContentSource = params.get("ContentSource")
        if params.get("SSAIInfo") is not None:
            self._SSAIInfo = SSAIConf()
            self._SSAIInfo._deserialize(params.get("SSAIInfo"))
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageSSAIChannelResponse(AbstractModel):
    """ModifyStreamPackageSSAIChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyStreamPackageSourceLocationRequest(AbstractModel):
    """ModifyStreamPackageSourceLocation request structure.

    """

    def __init__(self):
        r"""
        :param _Id: SourceLocation Id.
        :type Id: str
        :param _Name: Modified name.
        :type Name: str
        :param _BaseUrl: BaseUrl.
        :type BaseUrl: str
        :param _SegmentDeliverEnable: Whether to enable patching.
        :type SegmentDeliverEnable: bool
        :param _SegmentDeliverConf: Patch configuration.
        :type SegmentDeliverConf: :class:`tencentcloud.mdp.v20200527.models.SegmentDeliverInfo`
        :param _SegmentDeliverUsePackageEnable: Whether to enable package distribution sharding, it is enabled by default.
        :type SegmentDeliverUsePackageEnable: bool
        """
        self._Id = None
        self._Name = None
        self._BaseUrl = None
        self._SegmentDeliverEnable = None
        self._SegmentDeliverConf = None
        self._SegmentDeliverUsePackageEnable = None

    @property
    def Id(self):
        """SourceLocation Id.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Modified name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def BaseUrl(self):
        """BaseUrl.
        :rtype: str
        """
        return self._BaseUrl

    @BaseUrl.setter
    def BaseUrl(self, BaseUrl):
        self._BaseUrl = BaseUrl

    @property
    def SegmentDeliverEnable(self):
        """Whether to enable patching.
        :rtype: bool
        """
        return self._SegmentDeliverEnable

    @SegmentDeliverEnable.setter
    def SegmentDeliverEnable(self, SegmentDeliverEnable):
        self._SegmentDeliverEnable = SegmentDeliverEnable

    @property
    def SegmentDeliverConf(self):
        """Patch configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SegmentDeliverInfo`
        """
        return self._SegmentDeliverConf

    @SegmentDeliverConf.setter
    def SegmentDeliverConf(self, SegmentDeliverConf):
        self._SegmentDeliverConf = SegmentDeliverConf

    @property
    def SegmentDeliverUsePackageEnable(self):
        """Whether to enable package distribution sharding, it is enabled by default.
        :rtype: bool
        """
        return self._SegmentDeliverUsePackageEnable

    @SegmentDeliverUsePackageEnable.setter
    def SegmentDeliverUsePackageEnable(self, SegmentDeliverUsePackageEnable):
        self._SegmentDeliverUsePackageEnable = SegmentDeliverUsePackageEnable


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._BaseUrl = params.get("BaseUrl")
        self._SegmentDeliverEnable = params.get("SegmentDeliverEnable")
        if params.get("SegmentDeliverConf") is not None:
            self._SegmentDeliverConf = SegmentDeliverInfo()
            self._SegmentDeliverConf._deserialize(params.get("SegmentDeliverConf"))
        self._SegmentDeliverUsePackageEnable = params.get("SegmentDeliverUsePackageEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageSourceLocationResponse(AbstractModel):
    """ModifyStreamPackageSourceLocation response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyStreamPackageSourceRequest(AbstractModel):
    """ModifyStreamPackageSource request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Source Id.
        :type Id: str
        :param _Name: Modified name.
        :type Name: str
        :param _Type: Distinguish between live broadcast and on-demand VOD source types.
Optional values: Live, VOD (on demand)
        :type Type: str
        :param _PackageConfs: source configuration.
        :type PackageConfs: list of SourcePackageConf
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._PackageConfs = None

    @property
    def Id(self):
        """Source Id.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """Modified name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """Distinguish between live broadcast and on-demand VOD source types.
Optional values: Live, VOD (on demand)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PackageConfs(self):
        """source configuration.
        :rtype: list of SourcePackageConf
        """
        return self._PackageConfs

    @PackageConfs.setter
    def PackageConfs(self, PackageConfs):
        self._PackageConfs = PackageConfs


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("PackageConfs") is not None:
            self._PackageConfs = []
            for item in params.get("PackageConfs"):
                obj = SourcePackageConf()
                obj._deserialize(item)
                self._PackageConfs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamPackageSourceResponse(AbstractModel):
    """ModifyStreamPackageSource response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class NameServer(AbstractModel):
    """Custom server information.

    """

    def __init__(self):
        r"""
        :param _Name: name.
        :type Name: str
        :param _Url: address.
        :type Url: str
        """
        self._Name = None
        self._Url = None

    @property
    def Name(self):
        """name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        """address.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputInfo(AbstractModel):
    """Channel linear assembly output information.

    """

    def __init__(self):
        r"""
        :param _Type: HLS DASH.
        :type Type: str
        :param _GroupName: The output group name can be associated with the source group name.
        :type GroupName: str
        :param _ManifestName: The file name output by the channel program after scheduling.
        :type ManifestName: str
        :param _ManifestConf: The manifest info, used when Type is HLS.
        :type ManifestConf: :class:`tencentcloud.mdp.v20200527.models.ManifestInfo`
        :param _PlaybackURL: Playback address.
        :type PlaybackURL: str
        :param _DashManifestConf: The manifest info, used when Type is DASH.
        :type DashManifestConf: :class:`tencentcloud.mdp.v20200527.models.DashManifestInfo`
        """
        self._Type = None
        self._GroupName = None
        self._ManifestName = None
        self._ManifestConf = None
        self._PlaybackURL = None
        self._DashManifestConf = None

    @property
    def Type(self):
        """HLS DASH.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GroupName(self):
        """The output group name can be associated with the source group name.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ManifestName(self):
        """The file name output by the channel program after scheduling.
        :rtype: str
        """
        return self._ManifestName

    @ManifestName.setter
    def ManifestName(self, ManifestName):
        self._ManifestName = ManifestName

    @property
    def ManifestConf(self):
        """The manifest info, used when Type is HLS.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ManifestInfo`
        """
        return self._ManifestConf

    @ManifestConf.setter
    def ManifestConf(self, ManifestConf):
        self._ManifestConf = ManifestConf

    @property
    def PlaybackURL(self):
        """Playback address.
        :rtype: str
        """
        return self._PlaybackURL

    @PlaybackURL.setter
    def PlaybackURL(self, PlaybackURL):
        self._PlaybackURL = PlaybackURL

    @property
    def DashManifestConf(self):
        """The manifest info, used when Type is DASH.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DashManifestInfo`
        """
        return self._DashManifestConf

    @DashManifestConf.setter
    def DashManifestConf(self, DashManifestConf):
        self._DashManifestConf = DashManifestConf


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._GroupName = params.get("GroupName")
        self._ManifestName = params.get("ManifestName")
        if params.get("ManifestConf") is not None:
            self._ManifestConf = ManifestInfo()
            self._ManifestConf._deserialize(params.get("ManifestConf"))
        self._PlaybackURL = params.get("PlaybackURL")
        if params.get("DashManifestConf") is not None:
            self._DashManifestConf = DashManifestInfo()
            self._DashManifestConf._deserialize(params.get("DashManifestConf"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputReq(AbstractModel):
    """Channel linear assembly output information.

    """

    def __init__(self):
        r"""
        :param _Type: Output type, distinguish HLS DASH.
        :type Type: str
        :param _GroupName: The output group name can be associated with the source group name.
        :type GroupName: str
        :param _ManifestName: The file name output by the channel program after scheduling.
        :type ManifestName: str
        :param _ManifestConf: The manifest info, used when Type is HLS.
        :type ManifestConf: :class:`tencentcloud.mdp.v20200527.models.ManifestInfo`
        :param _DashManifestConf: The manifest info, used when Type is DASH.
        :type DashManifestConf: :class:`tencentcloud.mdp.v20200527.models.DashManifestInfo`
        """
        self._Type = None
        self._GroupName = None
        self._ManifestName = None
        self._ManifestConf = None
        self._DashManifestConf = None

    @property
    def Type(self):
        """Output type, distinguish HLS DASH.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GroupName(self):
        """The output group name can be associated with the source group name.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ManifestName(self):
        """The file name output by the channel program after scheduling.
        :rtype: str
        """
        return self._ManifestName

    @ManifestName.setter
    def ManifestName(self, ManifestName):
        self._ManifestName = ManifestName

    @property
    def ManifestConf(self):
        """The manifest info, used when Type is HLS.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ManifestInfo`
        """
        return self._ManifestConf

    @ManifestConf.setter
    def ManifestConf(self, ManifestConf):
        self._ManifestConf = ManifestConf

    @property
    def DashManifestConf(self):
        """The manifest info, used when Type is DASH.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.DashManifestInfo`
        """
        return self._DashManifestConf

    @DashManifestConf.setter
    def DashManifestConf(self, DashManifestConf):
        self._DashManifestConf = DashManifestConf


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._GroupName = params.get("GroupName")
        self._ManifestName = params.get("ManifestName")
        if params.get("ManifestConf") is not None:
            self._ManifestConf = ManifestInfo()
            self._ManifestConf._deserialize(params.get("ManifestConf"))
        if params.get("DashManifestConf") is not None:
            self._DashManifestConf = DashManifestInfo()
            self._DashManifestConf._deserialize(params.get("DashManifestConf"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlaybackInfo(AbstractModel):
    """program playback configuration.

    """

    def __init__(self):
        r"""
        :param _Duration: Program duration, in milliseconds, valid for live broadcast.
        :type Duration: int
        :param _TransitionType: Program startup method, live broadcast only supports Absolute, on-demand also supports Relative.
        :type TransitionType: str
        :param _StartTime: Unix timestamp, the start execution time of the program in the Absolute scenario.
        :type StartTime: int
        :param _RelativePosition: It is related to the insertion order of the selected program, divided into After and Before.
        :type RelativePosition: str
        :param _RelativeProgramId: The selected insertion reference program id.
        :type RelativeProgramId: str
        :param _ClipRangeConf: Spacer configuration.
        :type ClipRangeConf: :class:`tencentcloud.mdp.v20200527.models.ClipRangeInfo`
        :param _RelativeProgramName: RelativeProgramName.
        :type RelativeProgramName: str
        """
        self._Duration = None
        self._TransitionType = None
        self._StartTime = None
        self._RelativePosition = None
        self._RelativeProgramId = None
        self._ClipRangeConf = None
        self._RelativeProgramName = None

    @property
    def Duration(self):
        """Program duration, in milliseconds, valid for live broadcast.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def TransitionType(self):
        """Program startup method, live broadcast only supports Absolute, on-demand also supports Relative.
        :rtype: str
        """
        return self._TransitionType

    @TransitionType.setter
    def TransitionType(self, TransitionType):
        self._TransitionType = TransitionType

    @property
    def StartTime(self):
        """Unix timestamp, the start execution time of the program in the Absolute scenario.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def RelativePosition(self):
        """It is related to the insertion order of the selected program, divided into After and Before.
        :rtype: str
        """
        return self._RelativePosition

    @RelativePosition.setter
    def RelativePosition(self, RelativePosition):
        self._RelativePosition = RelativePosition

    @property
    def RelativeProgramId(self):
        """The selected insertion reference program id.
        :rtype: str
        """
        return self._RelativeProgramId

    @RelativeProgramId.setter
    def RelativeProgramId(self, RelativeProgramId):
        self._RelativeProgramId = RelativeProgramId

    @property
    def ClipRangeConf(self):
        """Spacer configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ClipRangeInfo`
        """
        return self._ClipRangeConf

    @ClipRangeConf.setter
    def ClipRangeConf(self, ClipRangeConf):
        self._ClipRangeConf = ClipRangeConf

    @property
    def RelativeProgramName(self):
        """RelativeProgramName.
        :rtype: str
        """
        return self._RelativeProgramName

    @RelativeProgramName.setter
    def RelativeProgramName(self, RelativeProgramName):
        self._RelativeProgramName = RelativeProgramName


    def _deserialize(self, params):
        self._Duration = params.get("Duration")
        self._TransitionType = params.get("TransitionType")
        self._StartTime = params.get("StartTime")
        self._RelativePosition = params.get("RelativePosition")
        self._RelativeProgramId = params.get("RelativeProgramId")
        if params.get("ClipRangeConf") is not None:
            self._ClipRangeConf = ClipRangeInfo()
            self._ClipRangeConf._deserialize(params.get("ClipRangeConf"))
        self._RelativeProgramName = params.get("RelativeProgramName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlaybackInfoReq(AbstractModel):
    """program playback configuration request.

    """

    def __init__(self):
        r"""
        :param _TransitionType: Program startup method, live broadcast only supports Absolute, on-demand also supports Relative.
Optional values: Absolute, Relative.
        :type TransitionType: str
        :param _StartTime: Unix timestamp, the start execution time of the program in absolute scenarios.
        :type StartTime: int
        :param _Duration: Program duration, in milliseconds, valid for live broadcast.
        :type Duration: int
        :param _RelativePosition: It is related to the insertion order of the selected program, divided into After and Before.
        :type RelativePosition: str
        :param _RelativeProgramId: The selected insertion reference program id.
        :type RelativeProgramId: str
        :param _ClipRangeConf: Spacer configuration.
        :type ClipRangeConf: :class:`tencentcloud.mdp.v20200527.models.ClipRangeInfo`
        """
        self._TransitionType = None
        self._StartTime = None
        self._Duration = None
        self._RelativePosition = None
        self._RelativeProgramId = None
        self._ClipRangeConf = None

    @property
    def TransitionType(self):
        """Program startup method, live broadcast only supports Absolute, on-demand also supports Relative.
Optional values: Absolute, Relative.
        :rtype: str
        """
        return self._TransitionType

    @TransitionType.setter
    def TransitionType(self, TransitionType):
        self._TransitionType = TransitionType

    @property
    def StartTime(self):
        """Unix timestamp, the start execution time of the program in absolute scenarios.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        """Program duration, in milliseconds, valid for live broadcast.
        :rtype: int
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def RelativePosition(self):
        """It is related to the insertion order of the selected program, divided into After and Before.
        :rtype: str
        """
        return self._RelativePosition

    @RelativePosition.setter
    def RelativePosition(self, RelativePosition):
        self._RelativePosition = RelativePosition

    @property
    def RelativeProgramId(self):
        """The selected insertion reference program id.
        :rtype: str
        """
        return self._RelativeProgramId

    @RelativeProgramId.setter
    def RelativeProgramId(self, RelativeProgramId):
        self._RelativeProgramId = RelativeProgramId

    @property
    def ClipRangeConf(self):
        """Spacer configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.ClipRangeInfo`
        """
        return self._ClipRangeConf

    @ClipRangeConf.setter
    def ClipRangeConf(self, ClipRangeConf):
        self._ClipRangeConf = ClipRangeConf


    def _deserialize(self, params):
        self._TransitionType = params.get("TransitionType")
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        self._RelativePosition = params.get("RelativePosition")
        self._RelativeProgramId = params.get("RelativeProgramId")
        if params.get("ClipRangeConf") is not None:
            self._ClipRangeConf = ClipRangeInfo()
            self._ClipRangeConf._deserialize(params.get("ClipRangeConf"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """Channel input list.
        :rtype: list of InputInfo
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def Endpoints(self):
        """Channel output list.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of EndpointInfo
        """
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
        


class ProgramAlertCounts(AbstractModel):
    """Channel Linear Assembly Program Aggregation Alarm Information

    """

    def __init__(self):
        r"""
        :param _ProgramId: Program ID.
        :type ProgramId: str
        :param _ProgramName: Program name.
        :type ProgramName: str
        :param _Category: Alarm classification.
        :type Category: str
        :param _Count: The number of occurrences
        :type Count: int
        :param _LastModifiedTime: Update time.
        :type LastModifiedTime: int
        """
        self._ProgramId = None
        self._ProgramName = None
        self._Category = None
        self._Count = None
        self._LastModifiedTime = None

    @property
    def ProgramId(self):
        """Program ID.
        :rtype: str
        """
        return self._ProgramId

    @ProgramId.setter
    def ProgramId(self, ProgramId):
        self._ProgramId = ProgramId

    @property
    def ProgramName(self):
        """Program name.
        :rtype: str
        """
        return self._ProgramName

    @ProgramName.setter
    def ProgramName(self, ProgramName):
        self._ProgramName = ProgramName

    @property
    def Category(self):
        """Alarm classification.
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Count(self):
        """The number of occurrences
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def LastModifiedTime(self):
        """Update time.
        :rtype: int
        """
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime


    def _deserialize(self, params):
        self._ProgramId = params.get("ProgramId")
        self._ProgramName = params.get("ProgramName")
        self._Category = params.get("Category")
        self._Count = params.get("Count")
        self._LastModifiedTime = params.get("LastModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramAlertInfos(AbstractModel):
    """Channel linear assembly program alarm information details.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID.
        :type ChannelId: str
        :param _ChannelName: Channel name.

        :type ChannelName: str
        :param _ProgramId: ProgramID.
        :type ProgramId: str
        :param _ProgramName: ProgramName.
        :type ProgramName: str
        :param _Code: Alarm event code.
        :type Code: int
        :param _Category: Alarm classification.
        :type Category: str
        :param _Message: Alarm message.
        :type Message: str
        :param _LastModifiedTime: Update time.
        :type LastModifiedTime: int
        """
        self._ChannelId = None
        self._ChannelName = None
        self._ProgramId = None
        self._ProgramName = None
        self._Code = None
        self._Category = None
        self._Message = None
        self._LastModifiedTime = None

    @property
    def ChannelId(self):
        """Channel ID.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def ChannelName(self):
        """Channel name.

        :rtype: str
        """
        return self._ChannelName

    @ChannelName.setter
    def ChannelName(self, ChannelName):
        self._ChannelName = ChannelName

    @property
    def ProgramId(self):
        """ProgramID.
        :rtype: str
        """
        return self._ProgramId

    @ProgramId.setter
    def ProgramId(self, ProgramId):
        self._ProgramId = ProgramId

    @property
    def ProgramName(self):
        """ProgramName.
        :rtype: str
        """
        return self._ProgramName

    @ProgramName.setter
    def ProgramName(self, ProgramName):
        self._ProgramName = ProgramName

    @property
    def Code(self):
        """Alarm event code.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Category(self):
        """Alarm classification.
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Message(self):
        """Alarm message.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def LastModifiedTime(self):
        """Update time.
        :rtype: int
        """
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._ChannelName = params.get("ChannelName")
        self._ProgramId = params.get("ProgramId")
        self._ProgramName = params.get("ProgramName")
        self._Code = params.get("Code")
        self._Category = params.get("Category")
        self._Message = params.get("Message")
        self._LastModifiedTime = params.get("LastModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProgramScheduleInfo(AbstractModel):
    """The scheduling information of the Program under this channel.

    """

    def __init__(self):
        r"""
        :param _ProgramName: program name.
        :type ProgramName: str
        :param _ProgramId: program id.
        :type ProgramId: str
        :param _SourceType: source type.
        :type SourceType: str
        :param _SourceId: source id.
        :type SourceId: str
        :param _SourceLocationId: The id of the source location.
        :type SourceLocationId: str
        :param _StartTime: Start timestamp.
        :type StartTime: int
        :param _Duration: Duration.
        :type Duration: str
        """
        self._ProgramName = None
        self._ProgramId = None
        self._SourceType = None
        self._SourceId = None
        self._SourceLocationId = None
        self._StartTime = None
        self._Duration = None

    @property
    def ProgramName(self):
        """program name.
        :rtype: str
        """
        return self._ProgramName

    @ProgramName.setter
    def ProgramName(self, ProgramName):
        self._ProgramName = ProgramName

    @property
    def ProgramId(self):
        """program id.
        :rtype: str
        """
        return self._ProgramId

    @ProgramId.setter
    def ProgramId(self, ProgramId):
        self._ProgramId = ProgramId

    @property
    def SourceType(self):
        """source type.
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceId(self):
        """source id.
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceLocationId(self):
        """The id of the source location.
        :rtype: str
        """
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def StartTime(self):
        """Start timestamp.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Duration(self):
        """Duration.
        :rtype: str
        """
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._ProgramName = params.get("ProgramName")
        self._ProgramId = params.get("ProgramId")
        self._SourceType = params.get("SourceType")
        self._SourceId = params.get("SourceId")
        self._SourceLocationId = params.get("SourceLocationId")
        self._StartTime = params.get("StartTime")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SSAIChannelInfo(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _ID: SSAI configuration ID, globally unique identifier
        :type ID: str
        :param _Name: Configuration name
        :type Name: str
        :param _ContentSource: Content source stream prefix
        :type ContentSource: str
        :param _PlaybackPrefix: Generated playback address prefix
        :type PlaybackPrefix: str
        :param _SSAIInfo: SSAI configuration info
        :type SSAIInfo: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        :param _Region: Region info
        :type Region: str
        """
        self._ID = None
        self._Name = None
        self._ContentSource = None
        self._PlaybackPrefix = None
        self._SSAIInfo = None
        self._Region = None

    @property
    def ID(self):
        """SSAI configuration ID, globally unique identifier
        :rtype: str
        """
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        """Configuration name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContentSource(self):
        """Content source stream prefix
        :rtype: str
        """
        return self._ContentSource

    @ContentSource.setter
    def ContentSource(self, ContentSource):
        self._ContentSource = ContentSource

    @property
    def PlaybackPrefix(self):
        """Generated playback address prefix
        :rtype: str
        """
        return self._PlaybackPrefix

    @PlaybackPrefix.setter
    def PlaybackPrefix(self, PlaybackPrefix):
        self._PlaybackPrefix = PlaybackPrefix

    @property
    def SSAIInfo(self):
        """SSAI configuration info
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SSAIConf`
        """
        return self._SSAIInfo

    @SSAIInfo.setter
    def SSAIInfo(self, SSAIInfo):
        self._SSAIInfo = SSAIInfo

    @property
    def Region(self):
        """Region info
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._ContentSource = params.get("ContentSource")
        self._PlaybackPrefix = params.get("PlaybackPrefix")
        if params.get("SSAIInfo") is not None:
            self._SSAIInfo = SSAIConf()
            self._SSAIInfo._deserialize(params.get("SSAIInfo"))
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SSAIConf(AbstractModel):
    """SSAI ad insertion configuration.

    """

    def __init__(self):
        r"""
        :param _AdsUrl: Advertising Decision Server URL (ADS).
        :type AdsUrl: str
        :param _ConfigAliases: Parameter configuration.
        :type ConfigAliases: list of ConfigAliasesInfo
        :param _AdMarkerPassthrough: Whether to enable transparent transmission of advertising tags.
        :type AdMarkerPassthrough: bool
        :param _SCTE35AdType: How to process tags in advertisements, optional values: [1,2] 
1: Process all SCTE-35 type tags - all (default) 
2: SCTE-35enhanced, parse some types.
        :type SCTE35AdType: int
        :param _SlateAd: Default advertising url.
        :type SlateAd: str
        :param _Threshold: Maximum unfilled duration, unit: seconds.
        :type Threshold: int
        :param _DashMPDLocation: Whether to enable mpd location, true corresponds to enable, false corresponds to disable.
        :type DashMPDLocation: bool
        :param _AdTriggers: The type of tag that is regarded as an advertisement, optional values: [1,8]
1. Splice insert 
2. Provider advertisement 
3. Distributor advertisement 
4. Provider placement opportunity 
5. Distributor placement opportunity 
6. Break 
7. Provider overlay placement opportunity 
8. Distributor overlay placement opportunity.
        :type AdTriggers: list of int non-negative
        :param _DeliveryRestrictions: The type of distribution restriction that is considered an advertisement, optional values: [1,4]
1:None 
2:Restricted (default) 
3:Unrestricted 
4.Both.
        :type DeliveryRestrictions: int
        :param _SourceCDNPrefix: Source CDN prefix, needs to start with http:// or https://
        :type SourceCDNPrefix: str
        :param _AdCDNPrefix: Advertising CDN prefix needs to start with http:// or https://
        :type AdCDNPrefix: str
        """
        self._AdsUrl = None
        self._ConfigAliases = None
        self._AdMarkerPassthrough = None
        self._SCTE35AdType = None
        self._SlateAd = None
        self._Threshold = None
        self._DashMPDLocation = None
        self._AdTriggers = None
        self._DeliveryRestrictions = None
        self._SourceCDNPrefix = None
        self._AdCDNPrefix = None

    @property
    def AdsUrl(self):
        """Advertising Decision Server URL (ADS).
        :rtype: str
        """
        return self._AdsUrl

    @AdsUrl.setter
    def AdsUrl(self, AdsUrl):
        self._AdsUrl = AdsUrl

    @property
    def ConfigAliases(self):
        """Parameter configuration.
        :rtype: list of ConfigAliasesInfo
        """
        return self._ConfigAliases

    @ConfigAliases.setter
    def ConfigAliases(self, ConfigAliases):
        self._ConfigAliases = ConfigAliases

    @property
    def AdMarkerPassthrough(self):
        """Whether to enable transparent transmission of advertising tags.
        :rtype: bool
        """
        return self._AdMarkerPassthrough

    @AdMarkerPassthrough.setter
    def AdMarkerPassthrough(self, AdMarkerPassthrough):
        self._AdMarkerPassthrough = AdMarkerPassthrough

    @property
    def SCTE35AdType(self):
        """How to process tags in advertisements, optional values: [1,2] 
1: Process all SCTE-35 type tags - all (default) 
2: SCTE-35enhanced, parse some types.
        :rtype: int
        """
        return self._SCTE35AdType

    @SCTE35AdType.setter
    def SCTE35AdType(self, SCTE35AdType):
        self._SCTE35AdType = SCTE35AdType

    @property
    def SlateAd(self):
        """Default advertising url.
        :rtype: str
        """
        return self._SlateAd

    @SlateAd.setter
    def SlateAd(self, SlateAd):
        self._SlateAd = SlateAd

    @property
    def Threshold(self):
        """Maximum unfilled duration, unit: seconds.
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def DashMPDLocation(self):
        """Whether to enable mpd location, true corresponds to enable, false corresponds to disable.
        :rtype: bool
        """
        return self._DashMPDLocation

    @DashMPDLocation.setter
    def DashMPDLocation(self, DashMPDLocation):
        self._DashMPDLocation = DashMPDLocation

    @property
    def AdTriggers(self):
        """The type of tag that is regarded as an advertisement, optional values: [1,8]
1. Splice insert 
2. Provider advertisement 
3. Distributor advertisement 
4. Provider placement opportunity 
5. Distributor placement opportunity 
6. Break 
7. Provider overlay placement opportunity 
8. Distributor overlay placement opportunity.
        :rtype: list of int non-negative
        """
        return self._AdTriggers

    @AdTriggers.setter
    def AdTriggers(self, AdTriggers):
        self._AdTriggers = AdTriggers

    @property
    def DeliveryRestrictions(self):
        """The type of distribution restriction that is considered an advertisement, optional values: [1,4]
1:None 
2:Restricted (default) 
3:Unrestricted 
4.Both.
        :rtype: int
        """
        return self._DeliveryRestrictions

    @DeliveryRestrictions.setter
    def DeliveryRestrictions(self, DeliveryRestrictions):
        self._DeliveryRestrictions = DeliveryRestrictions

    @property
    def SourceCDNPrefix(self):
        """Source CDN prefix, needs to start with http:// or https://
        :rtype: str
        """
        return self._SourceCDNPrefix

    @SourceCDNPrefix.setter
    def SourceCDNPrefix(self, SourceCDNPrefix):
        self._SourceCDNPrefix = SourceCDNPrefix

    @property
    def AdCDNPrefix(self):
        """Advertising CDN prefix needs to start with http:// or https://
        :rtype: str
        """
        return self._AdCDNPrefix

    @AdCDNPrefix.setter
    def AdCDNPrefix(self, AdCDNPrefix):
        self._AdCDNPrefix = AdCDNPrefix


    def _deserialize(self, params):
        self._AdsUrl = params.get("AdsUrl")
        if params.get("ConfigAliases") is not None:
            self._ConfigAliases = []
            for item in params.get("ConfigAliases"):
                obj = ConfigAliasesInfo()
                obj._deserialize(item)
                self._ConfigAliases.append(obj)
        self._AdMarkerPassthrough = params.get("AdMarkerPassthrough")
        self._SCTE35AdType = params.get("SCTE35AdType")
        self._SlateAd = params.get("SlateAd")
        self._Threshold = params.get("Threshold")
        self._DashMPDLocation = params.get("DashMPDLocation")
        self._AdTriggers = params.get("AdTriggers")
        self._DeliveryRestrictions = params.get("DeliveryRestrictions")
        self._SourceCDNPrefix = params.get("SourceCDNPrefix")
        self._AdCDNPrefix = params.get("AdCDNPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentDeliverInfo(AbstractModel):
    """SourceLocation shim configuration.

    """

    def __init__(self):
        r"""
        :param _DefaultSegmentUrl: Default content source address.
        :type DefaultSegmentUrl: str
        :param _NameServers: Custom server address.
        :type NameServers: list of NameServer
        """
        self._DefaultSegmentUrl = None
        self._NameServers = None

    @property
    def DefaultSegmentUrl(self):
        """Default content source address.
        :rtype: str
        """
        return self._DefaultSegmentUrl

    @DefaultSegmentUrl.setter
    def DefaultSegmentUrl(self, DefaultSegmentUrl):
        self._DefaultSegmentUrl = DefaultSegmentUrl

    @property
    def NameServers(self):
        """Custom server address.
        :rtype: list of NameServer
        """
        return self._NameServers

    @NameServers.setter
    def NameServers(self, NameServers):
        self._NameServers = NameServers


    def _deserialize(self, params):
        self._DefaultSegmentUrl = params.get("DefaultSegmentUrl")
        if params.get("NameServers") is not None:
            self._NameServers = []
            for item in params.get("NameServers"):
                obj = NameServer()
                obj._deserialize(item)
                self._NameServers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlateInfo(AbstractModel):
    """Channel linear assembly channel spacer configuration.

    """

    def __init__(self):
        r"""
        :param _SourceLocationId: The ID of the source location.
        :type SourceLocationId: str
        :param _VodSourceName: The corresponding vod shim content source name.
        :type VodSourceName: str
        """
        self._SourceLocationId = None
        self._VodSourceName = None

    @property
    def SourceLocationId(self):
        """The ID of the source location.
        :rtype: str
        """
        return self._SourceLocationId

    @SourceLocationId.setter
    def SourceLocationId(self, SourceLocationId):
        self._SourceLocationId = SourceLocationId

    @property
    def VodSourceName(self):
        """The corresponding vod shim content source name.
        :rtype: str
        """
        return self._VodSourceName

    @VodSourceName.setter
    def VodSourceName(self, VodSourceName):
        self._VodSourceName = VodSourceName


    def _deserialize(self, params):
        self._SourceLocationId = params.get("SourceLocationId")
        self._VodSourceName = params.get("VodSourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceAlert(AbstractModel):
    """Channel Linear Assembly Location Alarm Information

    """

    def __init__(self):
        r"""
        :param _SourceId: Source ID.
        :type SourceId: str
        :param _SourceName: Source name.
        :type SourceName: str
        :param _Code: Alarm event code.
        :type Code: int
        :param _Category: Alarm classification.
        :type Category: str
        :param _Message: Alarm message.
        :type Message: str
        :param _LastModifiedTime: Update time.
        :type LastModifiedTime: int
        """
        self._SourceId = None
        self._SourceName = None
        self._Code = None
        self._Category = None
        self._Message = None
        self._LastModifiedTime = None

    @property
    def SourceId(self):
        """Source ID.
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceName(self):
        """Source name.
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def Code(self):
        """Alarm event code.
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Category(self):
        """Alarm classification.
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Message(self):
        """Alarm message.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def LastModifiedTime(self):
        """Update time.
        :rtype: int
        """
        return self._LastModifiedTime

    @LastModifiedTime.setter
    def LastModifiedTime(self, LastModifiedTime):
        self._LastModifiedTime = LastModifiedTime


    def _deserialize(self, params):
        self._SourceId = params.get("SourceId")
        self._SourceName = params.get("SourceName")
        self._Code = params.get("Code")
        self._Category = params.get("Category")
        self._Message = params.get("Message")
        self._LastModifiedTime = params.get("LastModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceInfo(AbstractModel):
    """SourceInfo.

    """

    def __init__(self):
        r"""
        :param _Name: name.
        :type Name: str
        :param _Type: The source type distinguishes between live broadcast and on-demand Vod.
        :type Type: str
        :param _PackageConf: Source configuration.
        :type PackageConf: list of SourcePackageConf
        :param _Id: ID.
        :type Id: str
        :param _CreateTime: Create timestamp.
        :type CreateTime: int
        :param _UpdateTime: Update timestamp.
        :type UpdateTime: int
        :param _Region: Region.
        :type Region: str
        """
        self._Name = None
        self._Type = None
        self._PackageConf = None
        self._Id = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Region = None

    @property
    def Name(self):
        """name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """The source type distinguishes between live broadcast and on-demand Vod.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PackageConf(self):
        """Source configuration.
        :rtype: list of SourcePackageConf
        """
        return self._PackageConf

    @PackageConf.setter
    def PackageConf(self, PackageConf):
        self._PackageConf = PackageConf

    @property
    def Id(self):
        """ID.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CreateTime(self):
        """Create timestamp.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Update timestamp.
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Region(self):
        """Region.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("PackageConf") is not None:
            self._PackageConf = []
            for item in params.get("PackageConf"):
                obj = SourcePackageConf()
                obj._deserialize(item)
                self._PackageConf.append(obj)
        self._Id = params.get("Id")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceLocationInfo(AbstractModel):
    """SourceLocation configuration information.

    """

    def __init__(self):
        r"""
        :param _Id: ID, unique identification.
        :type Id: str
        :param _Name: SourceLocation name.
        :type Name: str
        :param _Region: area.
        :type Region: str
        :param _BaseUrl: BaseUrl information.
        :type BaseUrl: str
        :param _SegmentDeliverEnable: Whether to enable patching.
        :type SegmentDeliverEnable: bool
        :param _SegmentDeliverConf: Patch configuration.
        :type SegmentDeliverConf: :class:`tencentcloud.mdp.v20200527.models.SegmentDeliverInfo`
        :param _AttachedLiveSources: List of bound live broadcast source ids.
        :type AttachedLiveSources: list of str
        :param _AttachedVodSources: List of bound on-demand source ids.
        :type AttachedVodSources: list of str
        :param _CreateTime: Source location creation time, Unix timestamp.
        :type CreateTime: int
        :param _UpdateTime: Source location last modified time, Unix timestamp.
        :type UpdateTime: int
        :param _SegmentDeliverUsePackageEnable: Whether to enable package distribution sharding, it is enabled by default.
        :type SegmentDeliverUsePackageEnable: bool
        """
        self._Id = None
        self._Name = None
        self._Region = None
        self._BaseUrl = None
        self._SegmentDeliverEnable = None
        self._SegmentDeliverConf = None
        self._AttachedLiveSources = None
        self._AttachedVodSources = None
        self._CreateTime = None
        self._UpdateTime = None
        self._SegmentDeliverUsePackageEnable = None

    @property
    def Id(self):
        """ID, unique identification.
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """SourceLocation name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Region(self):
        """area.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def BaseUrl(self):
        """BaseUrl information.
        :rtype: str
        """
        return self._BaseUrl

    @BaseUrl.setter
    def BaseUrl(self, BaseUrl):
        self._BaseUrl = BaseUrl

    @property
    def SegmentDeliverEnable(self):
        """Whether to enable patching.
        :rtype: bool
        """
        return self._SegmentDeliverEnable

    @SegmentDeliverEnable.setter
    def SegmentDeliverEnable(self, SegmentDeliverEnable):
        self._SegmentDeliverEnable = SegmentDeliverEnable

    @property
    def SegmentDeliverConf(self):
        """Patch configuration.
        :rtype: :class:`tencentcloud.mdp.v20200527.models.SegmentDeliverInfo`
        """
        return self._SegmentDeliverConf

    @SegmentDeliverConf.setter
    def SegmentDeliverConf(self, SegmentDeliverConf):
        self._SegmentDeliverConf = SegmentDeliverConf

    @property
    def AttachedLiveSources(self):
        """List of bound live broadcast source ids.
        :rtype: list of str
        """
        return self._AttachedLiveSources

    @AttachedLiveSources.setter
    def AttachedLiveSources(self, AttachedLiveSources):
        self._AttachedLiveSources = AttachedLiveSources

    @property
    def AttachedVodSources(self):
        """List of bound on-demand source ids.
        :rtype: list of str
        """
        return self._AttachedVodSources

    @AttachedVodSources.setter
    def AttachedVodSources(self, AttachedVodSources):
        self._AttachedVodSources = AttachedVodSources

    @property
    def CreateTime(self):
        """Source location creation time, Unix timestamp.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Source location last modified time, Unix timestamp.
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def SegmentDeliverUsePackageEnable(self):
        """Whether to enable package distribution sharding, it is enabled by default.
        :rtype: bool
        """
        return self._SegmentDeliverUsePackageEnable

    @SegmentDeliverUsePackageEnable.setter
    def SegmentDeliverUsePackageEnable(self, SegmentDeliverUsePackageEnable):
        self._SegmentDeliverUsePackageEnable = SegmentDeliverUsePackageEnable


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Region = params.get("Region")
        self._BaseUrl = params.get("BaseUrl")
        self._SegmentDeliverEnable = params.get("SegmentDeliverEnable")
        if params.get("SegmentDeliverConf") is not None:
            self._SegmentDeliverConf = SegmentDeliverInfo()
            self._SegmentDeliverConf._deserialize(params.get("SegmentDeliverConf"))
        self._AttachedLiveSources = params.get("AttachedLiveSources")
        self._AttachedVodSources = params.get("AttachedVodSources")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._SegmentDeliverUsePackageEnable = params.get("SegmentDeliverUsePackageEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourcePackageConf(AbstractModel):
    """Source file information.

    """

    def __init__(self):
        r"""
        :param _GroupName: Group name. When the channel is in Linear mode and vod source is selected, the group name corresponds to the output group name of the channel output.
        :type GroupName: str
        :param _Type: Type, distinguish between HLS and DASH, optional values: HLS, DASH.
        :type Type: str
        :param _Path: access path.
        :type Path: str
        """
        self._GroupName = None
        self._Type = None
        self._Path = None

    @property
    def GroupName(self):
        """Group name. When the channel is in Linear mode and vod source is selected, the group name corresponds to the output group name of the channel output.
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Type(self):
        """Type, distinguish between HLS and DASH, optional values: HLS, DASH.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Path(self):
        """access path.
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Type = params.get("Type")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpliceInsertInfo(AbstractModel):
    """SpliceInsertInfo.

    """

    def __init__(self):
        r"""
        :param _EventID: EventID.
        :type EventID: str
        :param _AvailNum: AvailNum.
        :type AvailNum: str
        :param _AvailExpected: AvailExpected.
        :type AvailExpected: str
        :param _ProgramID: ProgramID.
        :type ProgramID: str
        """
        self._EventID = None
        self._AvailNum = None
        self._AvailExpected = None
        self._ProgramID = None

    @property
    def EventID(self):
        """EventID.
        :rtype: str
        """
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def AvailNum(self):
        """AvailNum.
        :rtype: str
        """
        return self._AvailNum

    @AvailNum.setter
    def AvailNum(self, AvailNum):
        self._AvailNum = AvailNum

    @property
    def AvailExpected(self):
        """AvailExpected.
        :rtype: str
        """
        return self._AvailExpected

    @AvailExpected.setter
    def AvailExpected(self, AvailExpected):
        self._AvailExpected = AvailExpected

    @property
    def ProgramID(self):
        """ProgramID.
        :rtype: str
        """
        return self._ProgramID

    @ProgramID.setter
    def ProgramID(self, ProgramID):
        self._ProgramID = ProgramID


    def _deserialize(self, params):
        self._EventID = params.get("EventID")
        self._AvailNum = params.get("AvailNum")
        self._AvailExpected = params.get("AvailExpected")
        self._ProgramID = params.get("ProgramID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamPackageLinearAssemblyChannelRequest(AbstractModel):
    """StartStreamPackageLinearAssemblyChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """Channel ID.
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
        


class StartStreamPackageLinearAssemblyChannelResponse(AbstractModel):
    """StartStreamPackageLinearAssemblyChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class StopStreamPackageLinearAssemblyChannelRequest(AbstractModel):
    """StopStreamPackageLinearAssemblyChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """Channel ID.
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
        


class StopStreamPackageLinearAssemblyChannelResponse(AbstractModel):
    """StopStreamPackageLinearAssemblyChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class TimeShiftInfo(AbstractModel):
    """Linearly assembled channel time-shift configuration information.

    """

    def __init__(self):
        r"""
        :param _TimeWindows: Lookback window, in seconds.
        :type TimeWindows: int
        """
        self._TimeWindows = None

    @property
    def TimeWindows(self):
        """Lookback window, in seconds.
        :rtype: int
        """
        return self._TimeWindows

    @TimeWindows.setter
    def TimeWindows(self, TimeWindows):
        self._TimeWindows = TimeWindows


    def _deserialize(self, params):
        self._TimeWindows = params.get("TimeWindows")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeSignalInfo(AbstractModel):
    """TimeSignalInfo.

    """

    def __init__(self):
        r"""
        :param _EventID: EventID.
        :type EventID: str
        :param _UPIDType: UPIDType.
        :type UPIDType: str
        :param _UPID: UPID.
        :type UPID: str
        :param _TypeID: TypeID.
        :type TypeID: str
        :param _Num: Num.
        :type Num: str
        :param _Expected: Expected.
        :type Expected: str
        :param _SubsegmentNum: SubsegmentNum.
        :type SubsegmentNum: str
        :param _SubsegmentsExpected: SubsegmentsExpected.
        :type SubsegmentsExpected: str
        """
        self._EventID = None
        self._UPIDType = None
        self._UPID = None
        self._TypeID = None
        self._Num = None
        self._Expected = None
        self._SubsegmentNum = None
        self._SubsegmentsExpected = None

    @property
    def EventID(self):
        """EventID.
        :rtype: str
        """
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def UPIDType(self):
        """UPIDType.
        :rtype: str
        """
        return self._UPIDType

    @UPIDType.setter
    def UPIDType(self, UPIDType):
        self._UPIDType = UPIDType

    @property
    def UPID(self):
        """UPID.
        :rtype: str
        """
        return self._UPID

    @UPID.setter
    def UPID(self, UPID):
        self._UPID = UPID

    @property
    def TypeID(self):
        """TypeID.
        :rtype: str
        """
        return self._TypeID

    @TypeID.setter
    def TypeID(self, TypeID):
        self._TypeID = TypeID

    @property
    def Num(self):
        """Num.
        :rtype: str
        """
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Expected(self):
        """Expected.
        :rtype: str
        """
        return self._Expected

    @Expected.setter
    def Expected(self, Expected):
        self._Expected = Expected

    @property
    def SubsegmentNum(self):
        """SubsegmentNum.
        :rtype: str
        """
        return self._SubsegmentNum

    @SubsegmentNum.setter
    def SubsegmentNum(self, SubsegmentNum):
        self._SubsegmentNum = SubsegmentNum

    @property
    def SubsegmentsExpected(self):
        """SubsegmentsExpected.
        :rtype: str
        """
        return self._SubsegmentsExpected

    @SubsegmentsExpected.setter
    def SubsegmentsExpected(self, SubsegmentsExpected):
        self._SubsegmentsExpected = SubsegmentsExpected


    def _deserialize(self, params):
        self._EventID = params.get("EventID")
        self._UPIDType = params.get("UPIDType")
        self._UPID = params.get("UPID")
        self._TypeID = params.get("TypeID")
        self._Num = params.get("Num")
        self._Expected = params.get("Expected")
        self._SubsegmentNum = params.get("SubsegmentNum")
        self._SubsegmentsExpected = params.get("SubsegmentsExpected")
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
        """Channel ID
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def CdnDomain(self):
        """CDN playback domain name
        :rtype: str
        """
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
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UnbindLinearAssemblyCDNDomainWithChannelRequest(AbstractModel):
    """UnbindLinearAssemblyCDNDomainWithChannel request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel Id.
        :type ChannelId: str
        :param _CdnDomain: Cdn playback domain.
        :type CdnDomain: str
        """
        self._ChannelId = None
        self._CdnDomain = None

    @property
    def ChannelId(self):
        """Channel Id.
        :rtype: str
        """
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def CdnDomain(self):
        """Cdn playback domain.
        :rtype: str
        """
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
        


class UnbindLinearAssemblyCDNDomainWithChannelResponse(AbstractModel):
    """UnbindLinearAssemblyCDNDomainWithChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")