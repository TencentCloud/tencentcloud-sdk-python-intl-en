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


class CreateInput(AbstractModel):
    r"""Create input configuration message.

    """

    def __init__(self):
        r"""
        :param _InputName: Enter a name. It can contain uppercase letters, lowercase letters, digits, and underscores. Length: [1, 32].
        :type InputName: str
        :param _Protocol: Input protocol. Selectable: [SRT|RTP|RTMP|RTMP_PULL|RTSP_PULL|RIST].
        :type Protocol: str
        :param _Description: Enter description. Length: [0, 255].
        :type Description: str
        :param _AllowIpList: Input IP allowlist in CIDR format.
        :type AllowIpList: list of str
        :param _SRTSettings: SRT configuration information of the input.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param _RTPSettings: Input RTP configuration message.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param _FailOver: Primary/replica switch input. Selectable values: `OPEN` and `CLOSE`. Default value: `CLOSE`.
        :type FailOver: str
        :param _RTMPPullSettings: Input RTMP_PULL configuration message.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        :param _RTSPPullSettings: Input RTSP_PULL configuration message.
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        :param _HLSPullSettings: Input HLS_PULL configuration message.
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        :param _ResilientStream: Configuration message for smooth streaming during delayed broadcasting.
        :type ResilientStream: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        :param _SecurityGroupIds: Bound input security group ID.
        :type SecurityGroupIds: list of str
        :param _Zones: Availability zone. This parameter is optional. If disaster recovery is enabled, two different availability zones must be input. Otherwise, only one availability zone can be input.
        :type Zones: list of str
        :param _RISTSettings: Input RIST configuration message.
        :type RISTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRISTSettings`
        :param _InputRegion: Region of the input node
        :type InputRegion: str
        :param _FailOverOption: Hot/cold backup
        :type FailOverOption: :class:`tencentcloud.mdc.v20200828.models.FailOverOption`
        """
        self._InputName = None
        self._Protocol = None
        self._Description = None
        self._AllowIpList = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._FailOver = None
        self._RTMPPullSettings = None
        self._RTSPPullSettings = None
        self._HLSPullSettings = None
        self._ResilientStream = None
        self._SecurityGroupIds = None
        self._Zones = None
        self._RISTSettings = None
        self._InputRegion = None
        self._FailOverOption = None

    @property
    def InputName(self):
        r"""Enter a name. It can contain uppercase letters, lowercase letters, digits, and underscores. Length: [1, 32].
        :rtype: str
        """
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Protocol(self):
        r"""Input protocol. Selectable: [SRT|RTP|RTMP|RTMP_PULL|RTSP_PULL|RIST].
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Description(self):
        r"""Enter description. Length: [0, 255].
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AllowIpList(self):
        r"""Input IP allowlist in CIDR format.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        r"""SRT configuration information of the input.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        r"""Input RTP configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def FailOver(self):
        r"""Primary/replica switch input. Selectable values: `OPEN` and `CLOSE`. Default value: `CLOSE`.
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def RTMPPullSettings(self):
        r"""Input RTMP_PULL configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def RTSPPullSettings(self):
        r"""Input RTSP_PULL configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        r"""Input HLS_PULL configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def ResilientStream(self):
        r"""Configuration message for smooth streaming during delayed broadcasting.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        """
        return self._ResilientStream

    @ResilientStream.setter
    def ResilientStream(self, ResilientStream):
        self._ResilientStream = ResilientStream

    @property
    def SecurityGroupIds(self):
        r"""Bound input security group ID.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        r"""Availability zone. This parameter is optional. If disaster recovery is enabled, two different availability zones must be input. Otherwise, only one availability zone can be input.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RISTSettings(self):
        r"""Input RIST configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRISTSettings`
        """
        return self._RISTSettings

    @RISTSettings.setter
    def RISTSettings(self, RISTSettings):
        self._RISTSettings = RISTSettings

    @property
    def InputRegion(self):
        r"""Region of the input node
        :rtype: str
        """
        return self._InputRegion

    @InputRegion.setter
    def InputRegion(self, InputRegion):
        self._InputRegion = InputRegion

    @property
    def FailOverOption(self):
        r"""Hot/cold backup
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FailOverOption`
        """
        return self._FailOverOption

    @FailOverOption.setter
    def FailOverOption(self, FailOverOption):
        self._FailOverOption = FailOverOption


    def _deserialize(self, params):
        self._InputName = params.get("InputName")
        self._Protocol = params.get("Protocol")
        self._Description = params.get("Description")
        self._AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateInputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateInputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._FailOver = params.get("FailOver")
        if params.get("RTMPPullSettings") is not None:
            self._RTMPPullSettings = CreateInputRTMPPullSettings()
            self._RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        if params.get("RTSPPullSettings") is not None:
            self._RTSPPullSettings = CreateInputRTSPPullSettings()
            self._RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self._HLSPullSettings = CreateInputHLSPullSettings()
            self._HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        if params.get("ResilientStream") is not None:
            self._ResilientStream = ResilientStreamConf()
            self._ResilientStream._deserialize(params.get("ResilientStream"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zones = params.get("Zones")
        if params.get("RISTSettings") is not None:
            self._RISTSettings = CreateInputRISTSettings()
            self._RISTSettings._deserialize(params.get("RISTSettings"))
        self._InputRegion = params.get("InputRegion")
        if params.get("FailOverOption") is not None:
            self._FailOverOption = FailOverOption()
            self._FailOverOption._deserialize(params.get("FailOverOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputHLSPullSettings(AbstractModel):
    r"""Configuration message of the created input HLS pull.

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: HLS origin server address. Only one is allowed.
        :type SourceAddresses: list of HLSPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        r"""HLS origin server address. Only one is allowed.
        :rtype: list of HLSPullSourceAddress
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = HLSPullSourceAddress()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRISTSettings(AbstractModel):
    r"""Input RIST configuration message created.

    """

    def __init__(self):
        r"""
        :param _Mode: RIST mode. Valid value: `LISTENER`. Default value: `LISTENER`.
        :type Mode: str
        :param _Profile: RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :type Profile: str
        :param _Buffer: RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120.
        :type Buffer: int
        """
        self._Mode = None
        self._Profile = None
        self._Buffer = None

    @property
    def Mode(self):
        r"""RIST mode. Valid value: `LISTENER`. Default value: `LISTENER`.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Profile(self):
        r"""RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :rtype: str
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Buffer(self):
        r"""RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120.
        :rtype: int
        """
        return self._Buffer

    @Buffer.setter
    def Buffer(self, Buffer):
        self._Buffer = Buffer


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Profile = params.get("Profile")
        self._Buffer = params.get("Buffer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTMPPullSettings(AbstractModel):
    r"""Configuration message of the created input RTMP pull.

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: RTMP origin server address. Only one is allowed.
        :type SourceAddresses: list of RTMPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        r"""RTMP origin server address. Only one is allowed.
        :rtype: list of RTMPPullSourceAddress
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = RTMPPullSourceAddress()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTPSettings(AbstractModel):
    r"""Configuration message for creating an input RTP.

    """

    def __init__(self):
        r"""
        :param _FEC: Default value: "none". Available value: ['none'].
        :type FEC: str
        :param _IdleTimeout: Idle timeout. Default value: 5000 ms. Range: [1000, 10000].
        :type IdleTimeout: int
        """
        self._FEC = None
        self._IdleTimeout = None

    @property
    def FEC(self):
        r"""Default value: "none". Available value: ['none'].
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        r"""Idle timeout. Default value: 5000 ms. Range: [1000, 10000].
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTSPPullSettings(AbstractModel):
    r"""Configuration message of the created input RTSP pull stream.

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: Origin server address of the RTSP origin server. Only one is allowed.
        :type SourceAddresses: list of RTSPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        r"""Origin server address of the RTSP origin server. Only one is allowed.
        :rtype: list of RTSPPullSourceAddress
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = RTSPPullSourceAddress()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputSRTSettings(AbstractModel):
    r"""Configuration message of the created input SRT.

    """

    def __init__(self):
        r"""
        :param _Mode: SRT mode. Options: [LISTENER|CALLER]. Default value: LISTENER.
        :type Mode: str
        :param _StreamId: Stream Id. It can contain upper- and lower-case letters, digits, and special characters (.#!:&,=_-), with a length of 0 to 512. For the specific format, see: https://github.com/Haivision/srt/blob/master/docs/features/access-control.md#standard-keys.	
        :type StreamId: str
        :param _Latency: Delay. Default value: 0. Unit: ms. Range: [0, 3000].
        :type Latency: int
        :param _RecvLatency: Receive latency. Default value: 120. Unit: ms. Range: [0, 3000].
        :type RecvLatency: int
        :param _PeerLatency: Peer delay. Default value: 0. Unit: ms. Range: [0, 3000].
        :type PeerLatency: int
        :param _PeerIdleTimeout: Peer timeout. Default value: 5000 ms. Range: [1000, 10000].
        :type PeerIdleTimeout: int
        :param _Passphrase: Decryption key. Empty by default, which means not encrypted. Only ascii characters are supported. Length range: [10, 79].
        :type Passphrase: str
        :param _PbKeyLen: Key length. Default value: 0. Options: [0|16|24|32].
        :type PbKeyLen: int
        :param _SourceAddresses: SRT peer address. Required when Mode is CALLER, and can only contain 1 group.
        :type SourceAddresses: list of SRTSourceAddressReq
        :param _FEC: SRT FEC settings
        :type FEC: :class:`tencentcloud.mdc.v20200828.models.SRTFECSimpleOptions`
        """
        self._Mode = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._SourceAddresses = None
        self._FEC = None

    @property
    def Mode(self):
        r"""SRT mode. Options: [LISTENER|CALLER]. Default value: LISTENER.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StreamId(self):
        r"""Stream Id. It can contain upper- and lower-case letters, digits, and special characters (.#!:&,=_-), with a length of 0 to 512. For the specific format, see: https://github.com/Haivision/srt/blob/master/docs/features/access-control.md#standard-keys.	
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        r"""Delay. Default value: 0. Unit: ms. Range: [0, 3000].
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        r"""Receive latency. Default value: 120. Unit: ms. Range: [0, 3000].
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        r"""Peer delay. Default value: 0. Unit: ms. Range: [0, 3000].
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        r"""Peer timeout. Default value: 5000 ms. Range: [1000, 10000].
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        r"""Decryption key. Empty by default, which means not encrypted. Only ascii characters are supported. Length range: [10, 79].
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        r"""Key length. Default value: 0. Options: [0|16|24|32].
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def SourceAddresses(self):
        r"""SRT peer address. Required when Mode is CALLER, and can only contain 1 group.
        :rtype: list of SRTSourceAddressReq
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses

    @property
    def FEC(self):
        r"""SRT FEC settings
        :rtype: :class:`tencentcloud.mdc.v20200828.models.SRTFECSimpleOptions`
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressReq()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        if params.get("FEC") is not None:
            self._FEC = SRTFECSimpleOptions()
            self._FEC._deserialize(params.get("FEC"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfo(AbstractModel):
    r"""Configuration message for creating an output.

    """

    def __init__(self):
        r"""
        :param _OutputName: Output name.
        :type OutputName: str
        :param _Description: Output description.
        :type Description: str
        :param _Protocol: Output relay protocol. Supports SRT, RTP, RTMP, RTMP_PULL, RTSP_PULL, and RIST.
        :type Protocol: str
        :param _OutputRegion: Output region.
        :type OutputRegion: str
        :param _SRTSettings: Configuration of the output SRT.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param _RTMPSettings: Configuration of the output RTMP.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param _RTPSettings: Configuration of the output RTP.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param _AllowIpList: IP whitelist list in CIDR format, for example, 0.0.0.0/0.
Valid when Protocol is RTMP_PULL. If empty, it represents no limit on client IP.
        :type AllowIpList: list of str
        :param _MaxConcurrent: Maximum number of concurrent stream pulls. Maximum value: 4. Default value: 4.
        :type MaxConcurrent: int
        :param _SecurityGroupIds: ID of the bound input security group.
        :type SecurityGroupIds: list of str
        :param _Zones: Availability zone. output supports a maximum of one user-submitted input availability zone.
        :type Zones: list of str
        :param _OutputType: Output type: Internet/TencentCSS/StreamLive
        :type OutputType: str
        :param _RISTSettings: Output RIST configuration.
        :type RISTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRistSettings`
        :param _PidSelector: For streams with multiple audio/video tracks, you can specify the track to be used
        :type PidSelector: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        :param _OutputKind: Output module type, including Pinpoint (single-point output, supports up to four concurrent outputs); MultiMesh (multiple streams output, supports more than four concurrent outputs, currently up to 200). The default type is Pinpoint output. For a single Flow, only one MultiMesh output is allowed per zone.
        :type OutputKind: str
        :param _StreamSelector: For streams with multiple audio/video tracks, you can specify the track to be used
        :type StreamSelector: :class:`tencentcloud.mdc.v20200828.models.StreamSelector`
        """
        self._OutputName = None
        self._Description = None
        self._Protocol = None
        self._OutputRegion = None
        self._SRTSettings = None
        self._RTMPSettings = None
        self._RTPSettings = None
        self._AllowIpList = None
        self._MaxConcurrent = None
        self._SecurityGroupIds = None
        self._Zones = None
        self._OutputType = None
        self._RISTSettings = None
        self._PidSelector = None
        self._OutputKind = None
        self._StreamSelector = None

    @property
    def OutputName(self):
        r"""Output name.
        :rtype: str
        """
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def Description(self):
        r"""Output description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        r"""Output relay protocol. Supports SRT, RTP, RTMP, RTMP_PULL, RTSP_PULL, and RIST.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutputRegion(self):
        r"""Output region.
        :rtype: str
        """
        return self._OutputRegion

    @OutputRegion.setter
    def OutputRegion(self, OutputRegion):
        self._OutputRegion = OutputRegion

    @property
    def SRTSettings(self):
        r"""Configuration of the output SRT.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTMPSettings(self):
        r"""Configuration of the output RTMP.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def RTPSettings(self):
        r"""Configuration of the output RTP.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def AllowIpList(self):
        r"""IP whitelist list in CIDR format, for example, 0.0.0.0/0.
Valid when Protocol is RTMP_PULL. If empty, it represents no limit on client IP.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def MaxConcurrent(self):
        r"""Maximum number of concurrent stream pulls. Maximum value: 4. Default value: 4.
        :rtype: int
        """
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def SecurityGroupIds(self):
        r"""ID of the bound input security group.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        r"""Availability zone. output supports a maximum of one user-submitted input availability zone.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def OutputType(self):
        r"""Output type: Internet/TencentCSS/StreamLive
        :rtype: str
        """
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def RISTSettings(self):
        r"""Output RIST configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRistSettings`
        """
        return self._RISTSettings

    @RISTSettings.setter
    def RISTSettings(self, RISTSettings):
        self._RISTSettings = RISTSettings

    @property
    def PidSelector(self):
        warnings.warn("parameter `PidSelector` is deprecated", DeprecationWarning) 

        r"""For streams with multiple audio/video tracks, you can specify the track to be used
        :rtype: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        """
        return self._PidSelector

    @PidSelector.setter
    def PidSelector(self, PidSelector):
        warnings.warn("parameter `PidSelector` is deprecated", DeprecationWarning) 

        self._PidSelector = PidSelector

    @property
    def OutputKind(self):
        r"""Output module type, including Pinpoint (single-point output, supports up to four concurrent outputs); MultiMesh (multiple streams output, supports more than four concurrent outputs, currently up to 200). The default type is Pinpoint output. For a single Flow, only one MultiMesh output is allowed per zone.
        :rtype: str
        """
        return self._OutputKind

    @OutputKind.setter
    def OutputKind(self, OutputKind):
        self._OutputKind = OutputKind

    @property
    def StreamSelector(self):
        r"""For streams with multiple audio/video tracks, you can specify the track to be used
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StreamSelector`
        """
        return self._StreamSelector

    @StreamSelector.setter
    def StreamSelector(self, StreamSelector):
        self._StreamSelector = StreamSelector


    def _deserialize(self, params):
        self._OutputName = params.get("OutputName")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        self._OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateOutputSrtSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = CreateOutputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateOutputInfoRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._AllowIpList = params.get("AllowIpList")
        self._MaxConcurrent = params.get("MaxConcurrent")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zones = params.get("Zones")
        self._OutputType = params.get("OutputType")
        if params.get("RISTSettings") is not None:
            self._RISTSettings = CreateOutputRistSettings()
            self._RISTSettings._deserialize(params.get("RISTSettings"))
        if params.get("PidSelector") is not None:
            self._PidSelector = PidSelector()
            self._PidSelector._deserialize(params.get("PidSelector"))
        self._OutputKind = params.get("OutputKind")
        if params.get("StreamSelector") is not None:
            self._StreamSelector = StreamSelector()
            self._StreamSelector._deserialize(params.get("StreamSelector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfoRTPSettings(AbstractModel):
    r"""Create the RTP configuration for the output of a media transmission stream.

    """

    def __init__(self):
        r"""
        :param _Destinations: Destination address. You can enter 1 to 2 addresses.
        :type Destinations: list of CreateOutputRTPSettingsDestinations
        :param _FEC: Can only be filled in with none.
        :type FEC: str
        :param _IdleTimeout: Idle timeout period, in milliseconds.
        :type IdleTimeout: int
        """
        self._Destinations = None
        self._FEC = None
        self._IdleTimeout = None

    @property
    def Destinations(self):
        r"""Destination address. You can enter 1 to 2 addresses.
        :rtype: list of CreateOutputRTPSettingsDestinations
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def FEC(self):
        r"""Can only be filled in with none.
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        r"""Idle timeout period, in milliseconds.
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRTPSettingsDestinations()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTMPSettings(AbstractModel):
    r"""RTMP configuration for creating the output of a media transmission stream.

    """

    def __init__(self):
        r"""
        :param _Destinations: Target address for repost. You can enter 1 to 2 addresses.
        :type Destinations: list of CreateOutputRtmpSettingsDestinations
        :param _ChunkSize: Chunk size of RTMP, ranging from 4096 to 40960.
        :type ChunkSize: int
        """
        self._Destinations = None
        self._ChunkSize = None

    @property
    def Destinations(self):
        r"""Target address for repost. You can enter 1 to 2 addresses.
        :rtype: list of CreateOutputRtmpSettingsDestinations
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def ChunkSize(self):
        r"""Chunk size of RTMP, ranging from 4096 to 40960.
        :rtype: int
        """
        return self._ChunkSize

    @ChunkSize.setter
    def ChunkSize(self, ChunkSize):
        self._ChunkSize = ChunkSize


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRtmpSettingsDestinations()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._ChunkSize = params.get("ChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTPSettingsDestinations(AbstractModel):
    r"""Create the RTP destination address for the output of a media transmission stream.

    """

    def __init__(self):
        r"""
        :param _Ip: Destination IP for repush.
        :type Ip: str
        :param _Port: Destination port for push.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""Destination IP for repush.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Destination port for push.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRistSettings(AbstractModel):
    r"""Create the RIST configuration for the output of a media transmission stream.

    """

    def __init__(self):
        r"""
        :param _Mode: RIST mode. Selectable: [LISTENER|CALLER]. Default: LISTENER.
        :type Mode: str
        :param _Profile: RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :type Profile: str
        :param _Buffer: RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120
        :type Buffer: int
        """
        self._Mode = None
        self._Profile = None
        self._Buffer = None

    @property
    def Mode(self):
        r"""RIST mode. Selectable: [LISTENER|CALLER]. Default: LISTENER.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Profile(self):
        r"""RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :rtype: str
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Buffer(self):
        r"""RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120
        :rtype: int
        """
        return self._Buffer

    @Buffer.setter
    def Buffer(self, Buffer):
        self._Buffer = Buffer


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Profile = params.get("Profile")
        self._Buffer = params.get("Buffer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRtmpSettingsDestinations(AbstractModel):
    r"""RTMP destination address for creating the output of a media transmission stream.

    """

    def __init__(self):
        r"""
        :param _Url: URL for push forwarding, in the format of rtmp://domain/live.
        :type Url: str
        :param _StreamKey: StreamKey for republishing, in the format of: stream?key=value.
        :type StreamKey: str
        """
        self._Url = None
        self._StreamKey = None

    @property
    def Url(self):
        r"""URL for push forwarding, in the format of rtmp://domain/live.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StreamKey(self):
        r"""StreamKey for republishing, in the format of: stream?key=value.
        :rtype: str
        """
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettings(AbstractModel):
    r"""Create the SRT configuration for the output of a media transmission stream.

    """

    def __init__(self):
        r"""
        :param _Destinations: Target address for push. Required when Mode is CALLER. Only 1 group can be filled in.
        :type Destinations: list of CreateOutputSrtSettingsDestinations
        :param _Mode: SRT mode. Valid values: `LISTENER` and `CALLER`. Default value: `CALLER`.
        :type Mode: str
        :param _StreamId: Stream Id for SRT retransmission. It can contain upper- and lower-case letters, digits, and special characters (.#!:&,=_-), with a length of 0 to 512.
        :type StreamId: str
        :param _Latency: Total delay for SRT retransmission. Default value: 0. Unit: ms. Range: [0, 3000]. This parameter simultaneously sets the sender and recipient delays (recvlatency and peerlatency) to the same value. Recommended configuration: at least 3 times the RTT to ensure effective handling of packet retransmission and confirmation during network congestion.
        :type Latency: int
        :param _RecvLatency: Receive latency for SRT relay. Default value: 120. Unit: ms. Range: [0, 3000].
This parameter indicates the time length for the recipient to cache data packets.
        :type RecvLatency: int
        :param _PeerLatency: Peer delay for SRT retransmission. Default value: 0. Unit: ms. Range: [0, 3000].
This parameter is set by the sender to inform the recipient of the expected buffer time for delay.
        :type PeerLatency: int
        :param _PeerIdleTimeout: Idle timeout for SRT relay. Default value: 5000 ms. Range: [1000, 10000].
If there is no activity on a connection within the set timeout period, it will be closed.
        :type PeerIdleTimeout: int
        :param _Passphrase: Encryption key for SRT retweet. It is empty by default, indicating not encrypted. Only ascii characters are allowed, with a length of [10, 79].
        :type Passphrase: str
        :param _PbKeyLen: Key length for SRT retransmission. Default value: 0. Options: [0|16|24|32].
        :type PbKeyLen: int
        :param _FEC: SRT FEC settings
        :type FEC: :class:`tencentcloud.mdc.v20200828.models.SRTFECFullOptions`
        """
        self._Destinations = None
        self._Mode = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._FEC = None

    @property
    def Destinations(self):
        r"""Target address for push. Required when Mode is CALLER. Only 1 group can be filled in.
        :rtype: list of CreateOutputSrtSettingsDestinations
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def Mode(self):
        r"""SRT mode. Valid values: `LISTENER` and `CALLER`. Default value: `CALLER`.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StreamId(self):
        r"""Stream Id for SRT retransmission. It can contain upper- and lower-case letters, digits, and special characters (.#!:&,=_-), with a length of 0 to 512.
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        r"""Total delay for SRT retransmission. Default value: 0. Unit: ms. Range: [0, 3000]. This parameter simultaneously sets the sender and recipient delays (recvlatency and peerlatency) to the same value. Recommended configuration: at least 3 times the RTT to ensure effective handling of packet retransmission and confirmation during network congestion.
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        r"""Receive latency for SRT relay. Default value: 120. Unit: ms. Range: [0, 3000].
This parameter indicates the time length for the recipient to cache data packets.
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        r"""Peer delay for SRT retransmission. Default value: 0. Unit: ms. Range: [0, 3000].
This parameter is set by the sender to inform the recipient of the expected buffer time for delay.
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        r"""Idle timeout for SRT relay. Default value: 5000 ms. Range: [1000, 10000].
If there is no activity on a connection within the set timeout period, it will be closed.
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        r"""Encryption key for SRT retweet. It is empty by default, indicating not encrypted. Only ascii characters are allowed, with a length of [10, 79].
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        r"""Key length for SRT retransmission. Default value: 0. Options: [0|16|24|32].
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def FEC(self):
        r"""SRT FEC settings
        :rtype: :class:`tencentcloud.mdc.v20200828.models.SRTFECFullOptions`
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputSrtSettingsDestinations()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._Mode = params.get("Mode")
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        if params.get("FEC") is not None:
            self._FEC = SRTFECFullOptions()
            self._FEC._deserialize(params.get("FEC"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettingsDestinations(AbstractModel):
    r"""Create the SRT destination address for the output of a media transmission stream.

    """

    def __init__(self):
        r"""
        :param _Ip: Output IP or domain.
        :type Ip: str
        :param _Port: Output port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""Output IP or domain.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Output port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowRequest(AbstractModel):
    r"""CreateStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowName: Stream name.
        :type FlowName: str
        :param _MaxBandwidth: Maximum bandwidth in bps. Options: [10000000, 20000000].
        :type MaxBandwidth: int
        :param _InputGroup: Input group of a stream.
        :type InputGroup: list of CreateInput
        :param _EventId: Media transmission Event ID associated with the Flow. Each Flow can only be associated with one Event.
        :type EventId: str
        :param _OutputGroup: Output group of the stream.
        :type OutputGroup: list of CreateOutputInfo
        """
        self._FlowName = None
        self._MaxBandwidth = None
        self._InputGroup = None
        self._EventId = None
        self._OutputGroup = None

    @property
    def FlowName(self):
        r"""Stream name.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def MaxBandwidth(self):
        r"""Maximum bandwidth in bps. Options: [10000000, 20000000].
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def InputGroup(self):
        r"""Input group of a stream.
        :rtype: list of CreateInput
        """
        return self._InputGroup

    @InputGroup.setter
    def InputGroup(self, InputGroup):
        self._InputGroup = InputGroup

    @property
    def EventId(self):
        r"""Media transmission Event ID associated with the Flow. Each Flow can only be associated with one Event.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def OutputGroup(self):
        r"""Output group of the stream.
        :rtype: list of CreateOutputInfo
        """
        return self._OutputGroup

    @OutputGroup.setter
    def OutputGroup(self, OutputGroup):
        self._OutputGroup = OutputGroup


    def _deserialize(self, params):
        self._FlowName = params.get("FlowName")
        self._MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self._InputGroup = []
            for item in params.get("InputGroup"):
                obj = CreateInput()
                obj._deserialize(item)
                self._InputGroup.append(obj)
        self._EventId = params.get("EventId")
        if params.get("OutputGroup") is not None:
            self._OutputGroup = []
            for item in params.get("OutputGroup"):
                obj = CreateOutputInfo()
                obj._deserialize(item)
                self._OutputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowResponse(AbstractModel):
    r"""CreateStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Information of the created Flow.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""Information of the created Flow.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamLinkInputRequest(AbstractModel):
    r"""CreateStreamLinkInput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Media transmission stream ID.</p>
        :type FlowId: str
        :param _InputGroup: <p>Input group of a stream.</p>
        :type InputGroup: list of CreateInput
        """
        self._FlowId = None
        self._InputGroup = None

    @property
    def FlowId(self):
        r"""<p>Media transmission stream ID.</p>
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InputGroup(self):
        r"""<p>Input group of a stream.</p>
        :rtype: list of CreateInput
        """
        return self._InputGroup

    @InputGroup.setter
    def InputGroup(self, InputGroup):
        self._InputGroup = InputGroup


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("InputGroup") is not None:
            self._InputGroup = []
            for item in params.get("InputGroup"):
                obj = CreateInput()
                obj._deserialize(item)
                self._InputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkInputResponse(AbstractModel):
    r"""CreateStreamLinkInput response structure.

    """

    def __init__(self):
        r"""
        :param _Info: <p>Information of the created Flow.</p>
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""<p>Information of the created Flow.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamLinkOutputInfoRequest(AbstractModel):
    r"""CreateStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Transport stream Id.
        :type FlowId: str
        :param _Output: Output configuration of the transport stream.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfo`
        """
        self._FlowId = None
        self._Output = None

    @property
    def FlowId(self):
        r"""Transport stream Id.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Output(self):
        r"""Output configuration of the transport stream.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfo`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self._Output = CreateOutputInfo()
            self._Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkOutputInfoResponse(AbstractModel):
    r"""CreateStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Output information after creation.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""Output information after creation.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = DescribeOutput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamLinkSecurityGroupRequest(AbstractModel):
    r"""CreateStreamLinkSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Name: <p>Security group name, supporting letters, digits, and underscores, unique within a Region.</p>
        :type Name: str
        :param _Whitelist: <p>Allowlist, maximum number: 10.</p>
        :type Whitelist: list of str
        """
        self._Name = None
        self._Whitelist = None

    @property
    def Name(self):
        r"""<p>Security group name, supporting letters, digits, and underscores, unique within a Region.</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Whitelist(self):
        r"""<p>Allowlist, maximum number: 10.</p>
        :rtype: list of str
        """
        return self._Whitelist

    @Whitelist.setter
    def Whitelist(self, Whitelist):
        self._Whitelist = Whitelist


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkSecurityGroupResponse(AbstractModel):
    r"""CreateStreamLinkSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Id: <p>Security group ID.</p>
        :type Id: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        r"""<p>Security group ID.</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class DeleteStreamLinkFlowRequest(AbstractModel):
    r"""DeleteStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Transport stream Id.</p>
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        r"""<p>Transport stream Id.</p>
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkFlowResponse(AbstractModel):
    r"""DeleteStreamLinkFlow response structure.

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


class DeleteStreamLinkOutputRequest(AbstractModel):
    r"""DeleteStreamLinkOutput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Stream Id.
        :type FlowId: str
        :param _OutputId: Output Id.
        :type OutputId: str
        """
        self._FlowId = None
        self._OutputId = None

    @property
    def FlowId(self):
        r"""Stream Id.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def OutputId(self):
        r"""Output Id.
        :rtype: str
        """
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._OutputId = params.get("OutputId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkOutputResponse(AbstractModel):
    r"""DeleteStreamLinkOutput response structure.

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


class DescribeFlow(AbstractModel):
    r"""Query the Flow configuration information.

    """

    def __init__(self):
        r"""
        :param _FlowId: Stream Id.
        :type FlowId: str
        :param _FlowName: Stream name.
        :type FlowName: str
        :param _State: Stream status. Valid values: IDLE, RUNNING.
        :type State: str
        :param _MaxBandwidth: Maximum bandwidth.
        :type MaxBandwidth: int
        :param _InputGroup: Input group.
        :type InputGroup: list of DescribeInput
        :param _OutputGroup: Output group.
        :type OutputGroup: list of DescribeOutput
        :param _EventId: EventId of the media transmission event associated with this Flow.
        :type EventId: str
        :param _CreateTime: Creation time of the Flow in UTC format.
        :type CreateTime: str
        :param _AllowedInputProtocols: Input protocols that can be created for this Flow.
        :type AllowedInputProtocols: list of str
        :param _AllowedOutputProtocols: Output protocols allowed to be created by this Flow
        :type AllowedOutputProtocols: list of str
        """
        self._FlowId = None
        self._FlowName = None
        self._State = None
        self._MaxBandwidth = None
        self._InputGroup = None
        self._OutputGroup = None
        self._EventId = None
        self._CreateTime = None
        self._AllowedInputProtocols = None
        self._AllowedOutputProtocols = None

    @property
    def FlowId(self):
        r"""Stream Id.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        r"""Stream name.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def State(self):
        r"""Stream status. Valid values: IDLE, RUNNING.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def MaxBandwidth(self):
        r"""Maximum bandwidth.
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def InputGroup(self):
        r"""Input group.
        :rtype: list of DescribeInput
        """
        return self._InputGroup

    @InputGroup.setter
    def InputGroup(self, InputGroup):
        self._InputGroup = InputGroup

    @property
    def OutputGroup(self):
        r"""Output group.
        :rtype: list of DescribeOutput
        """
        return self._OutputGroup

    @OutputGroup.setter
    def OutputGroup(self, OutputGroup):
        self._OutputGroup = OutputGroup

    @property
    def EventId(self):
        r"""EventId of the media transmission event associated with this Flow.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def CreateTime(self):
        r"""Creation time of the Flow in UTC format.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def AllowedInputProtocols(self):
        r"""Input protocols that can be created for this Flow.
        :rtype: list of str
        """
        return self._AllowedInputProtocols

    @AllowedInputProtocols.setter
    def AllowedInputProtocols(self, AllowedInputProtocols):
        self._AllowedInputProtocols = AllowedInputProtocols

    @property
    def AllowedOutputProtocols(self):
        r"""Output protocols allowed to be created by this Flow
        :rtype: list of str
        """
        return self._AllowedOutputProtocols

    @AllowedOutputProtocols.setter
    def AllowedOutputProtocols(self, AllowedOutputProtocols):
        self._AllowedOutputProtocols = AllowedOutputProtocols


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        self._State = params.get("State")
        self._MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self._InputGroup = []
            for item in params.get("InputGroup"):
                obj = DescribeInput()
                obj._deserialize(item)
                self._InputGroup.append(obj)
        if params.get("OutputGroup") is not None:
            self._OutputGroup = []
            for item in params.get("OutputGroup"):
                obj = DescribeOutput()
                obj._deserialize(item)
                self._OutputGroup.append(obj)
        self._EventId = params.get("EventId")
        self._CreateTime = params.get("CreateTime")
        self._AllowedInputProtocols = params.get("AllowedInputProtocols")
        self._AllowedOutputProtocols = params.get("AllowedOutputProtocols")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHLSPullSourceAddress(AbstractModel):
    r"""Query input HLS configuration message.

    """

    def __init__(self):
        r"""
        :param _Url: Url of the HLS origin server.
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""Url of the HLS origin server.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInput(AbstractModel):
    r"""Query input configuration message.

    """

    def __init__(self):
        r"""
        :param _InputId: Input Id.
        :type InputId: str
        :param _InputName: Input name.
        :type InputName: str
        :param _Description: Input description.
        :type Description: str
        :param _Protocol: Input protocol.
        :type Protocol: str
        :param _InputAddressList: Input the address list.
        :type InputAddressList: list of InputAddress
        :param _AllowIpList: Input the IP whitelist list.
        :type AllowIpList: list of str
        :param _SRTSettings: SRT configuration information of the input.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputSRTSettings`
        :param _RTPSettings: Input RTP configuration message.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTPSettings`
        :param _InputRegion: Input region.
        :type InputRegion: str
        :param _RTMPSettings: Input RTMP configuration message.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPSettings`
        :param _FailOver: Primary/replica switch input.
        :type FailOver: str
        :param _Zones: Availability zone configuration. In the current situation with disaster recovery enabled, there can be up to two, corresponding to pipeline 0 and 1 in sequence. Otherwise, there is only one availability zone.
        :type Zones: list of str
        :param _RTMPPullSettings: Input RTMP_PULL configuration message.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPPullSettings`
        :param _RTSPPullSettings: Input RTSP_PULL configuration message.
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTSPPullSettings`
        :param _HLSPullSettings: Input HLS_PULL configuration message.
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputHLSPullSettings`
        :param _ResilientStream: Configuration message for smooth streaming during delayed broadcasting.
        :type ResilientStream: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        :param _SecurityGroupIds: Bound input security group ID.	
        :type SecurityGroupIds: list of str
        :param _RISTSettings: Input RIST configuration message.
        :type RISTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRISTSettings`
        :param _StreamUrls: Input URL information related to module settings, including the provided streaming address or the configured third-party source stream URL.
        :type StreamUrls: list of StreamUrlDetail
        :param _FailOverOption: Disaster recovery configuration item
        :type FailOverOption: :class:`tencentcloud.mdc.v20200828.models.FailOverOption`
        """
        self._InputId = None
        self._InputName = None
        self._Description = None
        self._Protocol = None
        self._InputAddressList = None
        self._AllowIpList = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._InputRegion = None
        self._RTMPSettings = None
        self._FailOver = None
        self._Zones = None
        self._RTMPPullSettings = None
        self._RTSPPullSettings = None
        self._HLSPullSettings = None
        self._ResilientStream = None
        self._SecurityGroupIds = None
        self._RISTSettings = None
        self._StreamUrls = None
        self._FailOverOption = None

    @property
    def InputId(self):
        r"""Input Id.
        :rtype: str
        """
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def InputName(self):
        r"""Input name.
        :rtype: str
        """
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Description(self):
        r"""Input description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        r"""Input protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InputAddressList(self):
        r"""Input the address list.
        :rtype: list of InputAddress
        """
        return self._InputAddressList

    @InputAddressList.setter
    def InputAddressList(self, InputAddressList):
        self._InputAddressList = InputAddressList

    @property
    def AllowIpList(self):
        r"""Input the IP whitelist list.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        r"""SRT configuration information of the input.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        r"""Input RTP configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def InputRegion(self):
        r"""Input region.
        :rtype: str
        """
        return self._InputRegion

    @InputRegion.setter
    def InputRegion(self, InputRegion):
        self._InputRegion = InputRegion

    @property
    def RTMPSettings(self):
        r"""Input RTMP configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def FailOver(self):
        r"""Primary/replica switch input.
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def Zones(self):
        r"""Availability zone configuration. In the current situation with disaster recovery enabled, there can be up to two, corresponding to pipeline 0 and 1 in sequence. Otherwise, there is only one availability zone.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RTMPPullSettings(self):
        r"""Input RTMP_PULL configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def RTSPPullSettings(self):
        r"""Input RTSP_PULL configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        r"""Input HLS_PULL configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def ResilientStream(self):
        r"""Configuration message for smooth streaming during delayed broadcasting.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        """
        return self._ResilientStream

    @ResilientStream.setter
    def ResilientStream(self, ResilientStream):
        self._ResilientStream = ResilientStream

    @property
    def SecurityGroupIds(self):
        r"""Bound input security group ID.	
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def RISTSettings(self):
        r"""Input RIST configuration message.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRISTSettings`
        """
        return self._RISTSettings

    @RISTSettings.setter
    def RISTSettings(self, RISTSettings):
        self._RISTSettings = RISTSettings

    @property
    def StreamUrls(self):
        r"""Input URL information related to module settings, including the provided streaming address or the configured third-party source stream URL.
        :rtype: list of StreamUrlDetail
        """
        return self._StreamUrls

    @StreamUrls.setter
    def StreamUrls(self, StreamUrls):
        self._StreamUrls = StreamUrls

    @property
    def FailOverOption(self):
        r"""Disaster recovery configuration item
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FailOverOption`
        """
        return self._FailOverOption

    @FailOverOption.setter
    def FailOverOption(self, FailOverOption):
        self._FailOverOption = FailOverOption


    def _deserialize(self, params):
        self._InputId = params.get("InputId")
        self._InputName = params.get("InputName")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        if params.get("InputAddressList") is not None:
            self._InputAddressList = []
            for item in params.get("InputAddressList"):
                obj = InputAddress()
                obj._deserialize(item)
                self._InputAddressList.append(obj)
        self._AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = DescribeInputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = DescribeInputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._InputRegion = params.get("InputRegion")
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = DescribeInputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        self._FailOver = params.get("FailOver")
        self._Zones = params.get("Zones")
        if params.get("RTMPPullSettings") is not None:
            self._RTMPPullSettings = DescribeInputRTMPPullSettings()
            self._RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        if params.get("RTSPPullSettings") is not None:
            self._RTSPPullSettings = DescribeInputRTSPPullSettings()
            self._RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self._HLSPullSettings = DescribeInputHLSPullSettings()
            self._HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        if params.get("ResilientStream") is not None:
            self._ResilientStream = ResilientStreamConf()
            self._ResilientStream._deserialize(params.get("ResilientStream"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("RISTSettings") is not None:
            self._RISTSettings = DescribeInputRISTSettings()
            self._RISTSettings._deserialize(params.get("RISTSettings"))
        if params.get("StreamUrls") is not None:
            self._StreamUrls = []
            for item in params.get("StreamUrls"):
                obj = StreamUrlDetail()
                obj._deserialize(item)
                self._StreamUrls.append(obj)
        if params.get("FailOverOption") is not None:
            self._FailOverOption = FailOverOption()
            self._FailOverOption._deserialize(params.get("FailOverOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputHLSPullSettings(AbstractModel):
    r"""Query the configuration message of the input HLS.

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: HLS origin server address information.
        :type SourceAddresses: list of DescribeHLSPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        r"""HLS origin server address information.
        :rtype: list of DescribeHLSPullSourceAddress
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = DescribeHLSPullSourceAddress()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRISTSettings(AbstractModel):
    r"""Query the RIST configuration message of the input.

    """

    def __init__(self):
        r"""
        :param _Mode: RIST mode. Options: [LISTENER|CALLER]. Default value: LISTENER.
        :type Mode: str
        :param _Profile: RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :type Profile: str
        :param _Buffer: RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120.
        :type Buffer: int
        """
        self._Mode = None
        self._Profile = None
        self._Buffer = None

    @property
    def Mode(self):
        r"""RIST mode. Options: [LISTENER|CALLER]. Default value: LISTENER.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Profile(self):
        r"""RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :rtype: str
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Buffer(self):
        r"""RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120.
        :rtype: int
        """
        return self._Buffer

    @Buffer.setter
    def Buffer(self, Buffer):
        self._Buffer = Buffer


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Profile = params.get("Profile")
        self._Buffer = params.get("Buffer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTMPPullSettings(AbstractModel):
    r"""Query the input RTMP configuration message.

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: RTMP origin server address information.
        :type SourceAddresses: list of DescribeRTMPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        r"""RTMP origin server address information.
        :rtype: list of DescribeRTMPPullSourceAddress
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = DescribeRTMPPullSourceAddress()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTMPSettings(AbstractModel):
    r"""Query the input RTMP configuration message.

    """

    def __init__(self):
        r"""
        :param _AppName: RTMP push path.
        :type AppName: str
        :param _StreamKey: RTMP push StreamKey.
RTMP push URL splicing rule: rtmp://Ip:1935/AppName/StreamKey
        :type StreamKey: str
        """
        self._AppName = None
        self._StreamKey = None

    @property
    def AppName(self):
        r"""RTMP push path.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamKey(self):
        r"""RTMP push StreamKey.
RTMP push URL splicing rule: rtmp://Ip:1935/AppName/StreamKey
        :rtype: str
        """
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTPSettings(AbstractModel):
    r"""Query the configuration message of the input RTP.

    """

    def __init__(self):
        r"""
        :param _FEC: Whether to enable FEC.
        :type FEC: str
        :param _IdleTimeout: Idle timeout period.
        :type IdleTimeout: int
        """
        self._FEC = None
        self._IdleTimeout = None

    @property
    def FEC(self):
        r"""Whether to enable FEC.
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        r"""Idle timeout period.
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTSPPullSettings(AbstractModel):
    r"""Query the input RTSP configuration message.

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: RTSP origin server address.
        :type SourceAddresses: list of DescribeRTSPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        r"""RTSP origin server address.
        :rtype: list of DescribeRTSPPullSourceAddress
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = DescribeRTSPPullSourceAddress()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputSRTSettings(AbstractModel):
    r"""Query the input SRT configuration information.

    """

    def __init__(self):
        r"""
        :param _Mode: SRT mode.
        :type Mode: str
        :param _StreamId: Stream Id.
        :type StreamId: str
        :param _Latency: Delay.
        :type Latency: int
        :param _RecvLatency: Receive delay.
        :type RecvLatency: int
        :param _PeerLatency: Peer delay.
        :type PeerLatency: int
        :param _PeerIdleTimeout: Idle timeout period of the peer.
        :type PeerIdleTimeout: int
        :param _Passphrase: Decryption key.
        :type Passphrase: str
        :param _PbKeyLen: Key length.
        :type PbKeyLen: int
        :param _SourceAddresses: SRT peer address.
        :type SourceAddresses: list of SRTSourceAddressResp
        :param _FEC: FEC settings
        :type FEC: :class:`tencentcloud.mdc.v20200828.models.SRTFECSimpleOptions`
        """
        self._Mode = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._SourceAddresses = None
        self._FEC = None

    @property
    def Mode(self):
        r"""SRT mode.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StreamId(self):
        r"""Stream Id.
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        r"""Delay.
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        r"""Receive delay.
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        r"""Peer delay.
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        r"""Idle timeout period of the peer.
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        r"""Decryption key.
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        r"""Key length.
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def SourceAddresses(self):
        r"""SRT peer address.
        :rtype: list of SRTSourceAddressResp
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses

    @property
    def FEC(self):
        r"""FEC settings
        :rtype: :class:`tencentcloud.mdc.v20200828.models.SRTFECSimpleOptions`
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressResp()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        if params.get("FEC") is not None:
            self._FEC = SRTFECSimpleOptions()
            self._FEC._deserialize(params.get("FEC"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutput(AbstractModel):
    r"""Configuration message for querying an output.

    """

    def __init__(self):
        r"""
        :param _OutputId: <p>Output Id.</p>
        :type OutputId: str
        :param _OutputName: <p>Output name.</p>
        :type OutputName: str
        :param _OutputType: <p>Output type.</p>
        :type OutputType: str
        :param _Description: <p>Output description.</p>
        :type Description: str
        :param _Protocol: <p>Output protocol.</p>
        :type Protocol: str
        :param _OutputAddressList: <p>List of output egress address information.</p>
        :type OutputAddressList: list of OutputAddress
        :param _OutputRegion: <p>Output region.</p>
        :type OutputRegion: str
        :param _SRTSettings: <p>SRT configuration information of the output.</p>
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputSRTSettings`
        :param _RTPSettings: <p>Output RTP configuration message.</p>
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTPSettings`
        :param _RTMPSettings: <p>Output RTMP configuration message.</p>
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPSettings`
        :param _RTMPPullSettings: <p>Output RTMP pull configuration message.</p>
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPPullSettings`
        :param _AllowIpList: <p>CIDR allowlist.<br>Valid when Protocol is RTMP_PULL. If empty, it represents no limit on client IP.</p>
        :type AllowIpList: list of str
        :param _RTSPPullSettings: <p>Output RTSP pull stream configuration message.</p>
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTSPPullSettings`
        :param _HLSPullSettings: <p>Output HLS pull configuration message.</p>
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputHLSPullSettings`
        :param _MaxConcurrent: <p>Maximum number of concurrent stream pulls. Maximum value: 4. Default value: 4.</p>
        :type MaxConcurrent: int
        :param _SecurityGroupIds: <p>ID of the bound security group.</p>
        :type SecurityGroupIds: list of str
        :param _Zones: <p>Availability zone. output currently supports a maximum of one.</p>
        :type Zones: list of str
        :param _RISTSettings: <p>Output RIST configuration message.</p>
        :type RISTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRISTSettings`
        :param _PidSelector: <p>For streams with multiple audio/video tracks, you can specify the track to be used</p>
        :type PidSelector: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        :param _OutputKind: <p>Output module type, including Pinpoint (single-point output, supports up to four concurrent outputs); MultiMesh (multiple streams output, supports more than four concurrent outputs, currently up to 200). The default type is Pinpoint output. For one Flow, only one MultiMesh output is allowed in one zone.</p>
        :type OutputKind: str
        :param _StreamUrls: <p>Output module configuration, related URLs, including the provided pull stream address or the configured relay address for output to a third party</p>
        :type StreamUrls: list of StreamUrlDetail
        :param _StreamSelector: <p>For streams with multiple audio/video tracks, you can specify the track to be used</p>
        :type StreamSelector: :class:`tencentcloud.mdc.v20200828.models.StreamSelector`
        :param _State: <p>Output status.</p><p>Enumeration values:</p><ul><li>DISABLED</li><li>ENABLED</li></ul>
        :type State: str
        """
        self._OutputId = None
        self._OutputName = None
        self._OutputType = None
        self._Description = None
        self._Protocol = None
        self._OutputAddressList = None
        self._OutputRegion = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._RTMPSettings = None
        self._RTMPPullSettings = None
        self._AllowIpList = None
        self._RTSPPullSettings = None
        self._HLSPullSettings = None
        self._MaxConcurrent = None
        self._SecurityGroupIds = None
        self._Zones = None
        self._RISTSettings = None
        self._PidSelector = None
        self._OutputKind = None
        self._StreamUrls = None
        self._StreamSelector = None
        self._State = None

    @property
    def OutputId(self):
        r"""<p>Output Id.</p>
        :rtype: str
        """
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def OutputName(self):
        r"""<p>Output name.</p>
        :rtype: str
        """
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def OutputType(self):
        r"""<p>Output type.</p>
        :rtype: str
        """
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def Description(self):
        r"""<p>Output description.</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        r"""<p>Output protocol.</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutputAddressList(self):
        r"""<p>List of output egress address information.</p>
        :rtype: list of OutputAddress
        """
        return self._OutputAddressList

    @OutputAddressList.setter
    def OutputAddressList(self, OutputAddressList):
        self._OutputAddressList = OutputAddressList

    @property
    def OutputRegion(self):
        r"""<p>Output region.</p>
        :rtype: str
        """
        return self._OutputRegion

    @OutputRegion.setter
    def OutputRegion(self, OutputRegion):
        self._OutputRegion = OutputRegion

    @property
    def SRTSettings(self):
        r"""<p>SRT configuration information of the output.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        r"""<p>Output RTP configuration message.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def RTMPSettings(self):
        r"""<p>Output RTMP configuration message.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def RTMPPullSettings(self):
        r"""<p>Output RTMP pull configuration message.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def AllowIpList(self):
        r"""<p>CIDR allowlist.<br>Valid when Protocol is RTMP_PULL. If empty, it represents no limit on client IP.</p>
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def RTSPPullSettings(self):
        r"""<p>Output RTSP pull stream configuration message.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        r"""<p>Output HLS pull configuration message.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def MaxConcurrent(self):
        r"""<p>Maximum number of concurrent stream pulls. Maximum value: 4. Default value: 4.</p>
        :rtype: int
        """
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def SecurityGroupIds(self):
        r"""<p>ID of the bound security group.</p>
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        r"""<p>Availability zone. output currently supports a maximum of one.</p>
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RISTSettings(self):
        r"""<p>Output RIST configuration message.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRISTSettings`
        """
        return self._RISTSettings

    @RISTSettings.setter
    def RISTSettings(self, RISTSettings):
        self._RISTSettings = RISTSettings

    @property
    def PidSelector(self):
        warnings.warn("parameter `PidSelector` is deprecated", DeprecationWarning) 

        r"""<p>For streams with multiple audio/video tracks, you can specify the track to be used</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        """
        return self._PidSelector

    @PidSelector.setter
    def PidSelector(self, PidSelector):
        warnings.warn("parameter `PidSelector` is deprecated", DeprecationWarning) 

        self._PidSelector = PidSelector

    @property
    def OutputKind(self):
        r"""<p>Output module type, including Pinpoint (single-point output, supports up to four concurrent outputs); MultiMesh (multiple streams output, supports more than four concurrent outputs, currently up to 200). The default type is Pinpoint output. For one Flow, only one MultiMesh output is allowed in one zone.</p>
        :rtype: str
        """
        return self._OutputKind

    @OutputKind.setter
    def OutputKind(self, OutputKind):
        self._OutputKind = OutputKind

    @property
    def StreamUrls(self):
        r"""<p>Output module configuration, related URLs, including the provided pull stream address or the configured relay address for output to a third party</p>
        :rtype: list of StreamUrlDetail
        """
        return self._StreamUrls

    @StreamUrls.setter
    def StreamUrls(self, StreamUrls):
        self._StreamUrls = StreamUrls

    @property
    def StreamSelector(self):
        r"""<p>For streams with multiple audio/video tracks, you can specify the track to be used</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StreamSelector`
        """
        return self._StreamSelector

    @StreamSelector.setter
    def StreamSelector(self, StreamSelector):
        self._StreamSelector = StreamSelector

    @property
    def State(self):
        r"""<p>Output status.</p><p>Enumeration values:</p><ul><li>DISABLED</li><li>ENABLED</li></ul>
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._OutputId = params.get("OutputId")
        self._OutputName = params.get("OutputName")
        self._OutputType = params.get("OutputType")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        if params.get("OutputAddressList") is not None:
            self._OutputAddressList = []
            for item in params.get("OutputAddressList"):
                obj = OutputAddress()
                obj._deserialize(item)
                self._OutputAddressList.append(obj)
        self._OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = DescribeOutputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = DescribeOutputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = DescribeOutputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTMPPullSettings") is not None:
            self._RTMPPullSettings = DescribeOutputRTMPPullSettings()
            self._RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        self._AllowIpList = params.get("AllowIpList")
        if params.get("RTSPPullSettings") is not None:
            self._RTSPPullSettings = DescribeOutputRTSPPullSettings()
            self._RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self._HLSPullSettings = DescribeOutputHLSPullSettings()
            self._HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        self._MaxConcurrent = params.get("MaxConcurrent")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zones = params.get("Zones")
        if params.get("RISTSettings") is not None:
            self._RISTSettings = DescribeOutputRISTSettings()
            self._RISTSettings._deserialize(params.get("RISTSettings"))
        if params.get("PidSelector") is not None:
            self._PidSelector = PidSelector()
            self._PidSelector._deserialize(params.get("PidSelector"))
        self._OutputKind = params.get("OutputKind")
        if params.get("StreamUrls") is not None:
            self._StreamUrls = []
            for item in params.get("StreamUrls"):
                obj = StreamUrlDetail()
                obj._deserialize(item)
                self._StreamUrls.append(obj)
        if params.get("StreamSelector") is not None:
            self._StreamSelector = StreamSelector()
            self._StreamSelector._deserialize(params.get("StreamSelector"))
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputHLSPullServerUrl(AbstractModel):
    r"""Query the output HLS pull URL information.

    """

    def __init__(self):
        r"""
        :param _Url: Url of the HLS pull address.
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""Url of the HLS pull address.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputHLSPullSettings(AbstractModel):
    r"""Query the configuration message of the output HLS pull.

    """

    def __init__(self):
        r"""
        :param _ServerUrls: List of HLS pull addresses.
        :type ServerUrls: list of DescribeOutputHLSPullServerUrl
        """
        self._ServerUrls = None

    @property
    def ServerUrls(self):
        r"""List of HLS pull addresses.
        :rtype: list of DescribeOutputHLSPullServerUrl
        """
        return self._ServerUrls

    @ServerUrls.setter
    def ServerUrls(self, ServerUrls):
        self._ServerUrls = ServerUrls


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self._ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputHLSPullServerUrl()
                obj._deserialize(item)
                self._ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRISTSettings(AbstractModel):
    r"""Query the output RIST pull stream configuration message.

    """

    def __init__(self):
        r"""
        :param _Mode: RIST mode. Valid values: `LISTENER`, `CALLER`. Default value: `LISTENER`.
        :type Mode: str
        :param _Profile: RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :type Profile: str
        :param _Buffer: RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120.
        :type Buffer: int
        :param _SourceAddresses: Server listening address, used when the RIST mode is LISTENER.
        :type SourceAddresses: list of OutputRISTSourceAddressResp
        """
        self._Mode = None
        self._Profile = None
        self._Buffer = None
        self._SourceAddresses = None

    @property
    def Mode(self):
        r"""RIST mode. Valid values: `LISTENER`, `CALLER`. Default value: `LISTENER`.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Profile(self):
        r"""RIST configuration solution. Options: [MAIN|SIMPLE]. Default: MAIN.
        :rtype: str
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Buffer(self):
        r"""RIST buffer size in milliseconds. Minimum value: 50 ms. Maximum value: 5000 ms. Default value: 120.
        :rtype: int
        """
        return self._Buffer

    @Buffer.setter
    def Buffer(self, Buffer):
        self._Buffer = Buffer

    @property
    def SourceAddresses(self):
        r"""Server listening address, used when the RIST mode is LISTENER.
        :rtype: list of OutputRISTSourceAddressResp
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._Profile = params.get("Profile")
        self._Buffer = params.get("Buffer")
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = OutputRISTSourceAddressResp()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullServerUrl(AbstractModel):
    r"""Query the RTMP pull URL information in the output.

    """

    def __init__(self):
        r"""
        :param _TcUrl: tcUrl of the RTMP pull address.
        :type TcUrl: str
        :param _StreamKey: Stream key of the RTMP pull address.
        :type StreamKey: str
        """
        self._TcUrl = None
        self._StreamKey = None

    @property
    def TcUrl(self):
        r"""tcUrl of the RTMP pull address.
        :rtype: str
        """
        return self._TcUrl

    @TcUrl.setter
    def TcUrl(self, TcUrl):
        self._TcUrl = TcUrl

    @property
    def StreamKey(self):
        r"""Stream key of the RTMP pull address.
        :rtype: str
        """
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._TcUrl = params.get("TcUrl")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullSettings(AbstractModel):
    r"""Query the output RTMP pull stream configuration message.

    """

    def __init__(self):
        r"""
        :param _ServerUrls: List of pull addresses.
        :type ServerUrls: list of DescribeOutputRTMPPullServerUrl
        """
        self._ServerUrls = None

    @property
    def ServerUrls(self):
        r"""List of pull addresses.
        :rtype: list of DescribeOutputRTMPPullServerUrl
        """
        return self._ServerUrls

    @ServerUrls.setter
    def ServerUrls(self, ServerUrls):
        self._ServerUrls = ServerUrls


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self._ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputRTMPPullServerUrl()
                obj._deserialize(item)
                self._ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPSettings(AbstractModel):
    r"""Query the output RTMP configuration message.

    """

    def __init__(self):
        r"""
        :param _IdleTimeout: Idle timeout period.
        :type IdleTimeout: int
        :param _ChunkSize: Chunk size.
        :type ChunkSize: int
        :param _Destinations: List of target address information for RTMP repush.
        :type Destinations: list of RTMPAddressDestination
        """
        self._IdleTimeout = None
        self._ChunkSize = None
        self._Destinations = None

    @property
    def IdleTimeout(self):
        r"""Idle timeout period.
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ChunkSize(self):
        r"""Chunk size.
        :rtype: int
        """
        return self._ChunkSize

    @ChunkSize.setter
    def ChunkSize(self, ChunkSize):
        self._ChunkSize = ChunkSize

    @property
    def Destinations(self):
        r"""List of target address information for RTMP repush.
        :rtype: list of RTMPAddressDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations


    def _deserialize(self, params):
        self._IdleTimeout = params.get("IdleTimeout")
        self._ChunkSize = params.get("ChunkSize")
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = RTMPAddressDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTPSettings(AbstractModel):
    r"""Query the configuration message of the output RTP.

    """

    def __init__(self):
        r"""
        :param _Destinations: List of target address information for RTP repush.
        :type Destinations: list of RTPAddressDestination
        :param _FEC: Whether to enable FEC.
        :type FEC: str
        :param _IdleTimeout: Idle timeout period.
        :type IdleTimeout: int
        """
        self._Destinations = None
        self._FEC = None
        self._IdleTimeout = None

    @property
    def Destinations(self):
        r"""List of target address information for RTP repush.
        :rtype: list of RTPAddressDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def FEC(self):
        r"""Whether to enable FEC.
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        r"""Idle timeout period.
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = RTPAddressDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._FEC = params.get("FEC")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTSPPullServerUrl(AbstractModel):
    r"""Query the RTSP pull URL information in the output.

    """

    def __init__(self):
        r"""
        :param _Url: RTSP pull Url.
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""RTSP pull Url.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTSPPullSettings(AbstractModel):
    r"""Query the output RTSP pull stream configuration message.

    """

    def __init__(self):
        r"""
        :param _ServerUrls: List of RTSP pull addresses.
        :type ServerUrls: list of DescribeOutputRTSPPullServerUrl
        """
        self._ServerUrls = None

    @property
    def ServerUrls(self):
        r"""List of RTSP pull addresses.
        :rtype: list of DescribeOutputRTSPPullServerUrl
        """
        return self._ServerUrls

    @ServerUrls.setter
    def ServerUrls(self, ServerUrls):
        self._ServerUrls = ServerUrls


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self._ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputRTSPPullServerUrl()
                obj._deserialize(item)
                self._ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputSRTSettings(AbstractModel):
    r"""Query the output SRT configuration information.

    """

    def __init__(self):
        r"""
        :param _Destinations: Destination address list. Used when the SRT mode is CALLER.
        :type Destinations: list of SRTAddressDestination
        :param _StreamId: Stream Id.
        :type StreamId: str
        :param _Latency: Delay.
        :type Latency: int
        :param _RecvLatency: Receive delay.
        :type RecvLatency: int
        :param _PeerLatency: Peer delay.
        :type PeerLatency: int
        :param _PeerIdleTimeout: Idle timeout period of the peer.
        :type PeerIdleTimeout: int
        :param _Passphrase: Encryption key.
        :type Passphrase: str
        :param _PbKeyLen: Encryption key length.
        :type PbKeyLen: int
        :param _Mode: SRT mode.
        :type Mode: str
        :param _SourceAddresses: Server listening address, used when the SRT mode is LISTENER.
        :type SourceAddresses: list of OutputSRTSourceAddressResp
        :param _FEC: SRT FEC configuration
        :type FEC: :class:`tencentcloud.mdc.v20200828.models.SRTFECFullOptions`
        """
        self._Destinations = None
        self._StreamId = None
        self._Latency = None
        self._RecvLatency = None
        self._PeerLatency = None
        self._PeerIdleTimeout = None
        self._Passphrase = None
        self._PbKeyLen = None
        self._Mode = None
        self._SourceAddresses = None
        self._FEC = None

    @property
    def Destinations(self):
        r"""Destination address list. Used when the SRT mode is CALLER.
        :rtype: list of SRTAddressDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def StreamId(self):
        r"""Stream Id.
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        r"""Delay.
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        r"""Receive delay.
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        r"""Peer delay.
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        r"""Idle timeout period of the peer.
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        r"""Encryption key.
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        r"""Encryption key length.
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def Mode(self):
        r"""SRT mode.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SourceAddresses(self):
        r"""Server listening address, used when the SRT mode is LISTENER.
        :rtype: list of OutputSRTSourceAddressResp
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses

    @property
    def FEC(self):
        r"""SRT FEC configuration
        :rtype: :class:`tencentcloud.mdc.v20200828.models.SRTFECFullOptions`
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = SRTAddressDestination()
                obj._deserialize(item)
                self._Destinations.append(obj)
        self._StreamId = params.get("StreamId")
        self._Latency = params.get("Latency")
        self._RecvLatency = params.get("RecvLatency")
        self._PeerLatency = params.get("PeerLatency")
        self._PeerIdleTimeout = params.get("PeerIdleTimeout")
        self._Passphrase = params.get("Passphrase")
        self._PbKeyLen = params.get("PbKeyLen")
        self._Mode = params.get("Mode")
        if params.get("SourceAddresses") is not None:
            self._SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = OutputSRTSourceAddressResp()
                obj._deserialize(item)
                self._SourceAddresses.append(obj)
        if params.get("FEC") is not None:
            self._FEC = SRTFECFullOptions()
            self._FEC._deserialize(params.get("FEC"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRTMPPullSourceAddress(AbstractModel):
    r"""Query the input RTMP configuration message.

    """

    def __init__(self):
        r"""
        :param _TcUrl: TcUrl of the RTMP origin server.
        :type TcUrl: str
        :param _StreamKey: StreamKey of the RTMP origin server.
RTMP origin server URL splicing rule: $TcUrl/$StreamKey.
        :type StreamKey: str
        """
        self._TcUrl = None
        self._StreamKey = None

    @property
    def TcUrl(self):
        r"""TcUrl of the RTMP origin server.
        :rtype: str
        """
        return self._TcUrl

    @TcUrl.setter
    def TcUrl(self, TcUrl):
        self._TcUrl = TcUrl

    @property
    def StreamKey(self):
        r"""StreamKey of the RTMP origin server.
RTMP origin server URL splicing rule: $TcUrl/$StreamKey.
        :rtype: str
        """
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._TcUrl = params.get("TcUrl")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRTSPPullSourceAddress(AbstractModel):
    r"""Query the input RTSP configuration message.

    """

    def __init__(self):
        r"""
        :param _Url: Url of the RTSP origin server.
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""Url of the RTSP origin server.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowLogsRequest(AbstractModel):
    r"""DescribeStreamLinkFlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Transport stream Id.</p>
        :type FlowId: str
        :param _StartTime: <p>Start time for statistics, defaults to the last hour, supports querying up to the last 7 days.<br>UTC time, for example, '2020-01-01T12:00:00Z'.</p>
        :type StartTime: str
        :param _EndTime: <p>End time for statistics, defaulting to one hour after StartTime, with support for querying up to 24 hours of data.<br>UTC time, for example, '2020-01-01T12:00:00Z'.</p>
        :type EndTime: str
        :param _Type: <p>Input or output type. Valid values: `input`, `output`.</p>
        :type Type: list of str
        :param _Pipeline: <p>Primary or backup channel. Option [0|1].</p>
        :type Pipeline: list of str
        :param _PageSize: <p>Size per page. Default value: 100. Value range: [1, 1000].</p>
        :type PageSize: int
        :param _SortType: <p>Sort by Timestamp in ascending or descending order. The default is descending order. Options: [desc|asc].</p>
        :type SortType: str
        :param _PageNum: <p>Page number. Default value: 1. Value range: [1, 1000].</p>
        :type PageNum: int
        """
        self._FlowId = None
        self._StartTime = None
        self._EndTime = None
        self._Type = None
        self._Pipeline = None
        self._PageSize = None
        self._SortType = None
        self._PageNum = None

    @property
    def FlowId(self):
        r"""<p>Transport stream Id.</p>
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def StartTime(self):
        r"""<p>Start time for statistics, defaults to the last hour, supports querying up to the last 7 days.<br>UTC time, for example, '2020-01-01T12:00:00Z'.</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>End time for statistics, defaulting to one hour after StartTime, with support for querying up to 24 hours of data.<br>UTC time, for example, '2020-01-01T12:00:00Z'.</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        r"""<p>Input or output type. Valid values: `input`, `output`.</p>
        :rtype: list of str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pipeline(self):
        r"""<p>Primary or backup channel. Option [0|1].</p>
        :rtype: list of str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def PageSize(self):
        r"""<p>Size per page. Default value: 100. Value range: [1, 1000].</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortType(self):
        r"""<p>Sort by Timestamp in ascending or descending order. The default is descending order. Options: [desc|asc].</p>
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def PageNum(self):
        r"""<p>Page number. Default value: 1. Value range: [1, 1000].</p>
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Type = params.get("Type")
        self._Pipeline = params.get("Pipeline")
        self._PageSize = params.get("PageSize")
        self._SortType = params.get("SortType")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowLogsResponse(AbstractModel):
    r"""DescribeStreamLinkFlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: <p>Log information list.</p>
        :type Infos: list of FlowLogInfo
        :param _PageNum: <p>Current page.</p>
        :type PageNum: int
        :param _PageSize: <p>Size per page.</p>
        :type PageSize: int
        :param _TotalNum: <p>Total quantity.</p>
        :type TotalNum: int
        :param _TotalPage: <p>Total number of pages.</p>
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
        r"""<p>Log information list.</p>
        :rtype: list of FlowLogInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        r"""<p>Current page.</p>
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""<p>Size per page.</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        r"""<p>Total quantity.</p>
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        r"""<p>Total number of pages.</p>
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowLogInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowMediaStatisticsRequest(AbstractModel):
    r"""DescribeStreamLinkFlowMediaStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Transport stream ID.
        :type FlowId: str
        :param _Type: Input or output type. Valid values: `input`, `output`.
        :type Type: str
        :param _InputOutputId: Input or output Id.
        :type InputOutputId: str
        :param _Pipeline: Primary or backup channel. Valid values: 0 and 1.
        :type Pipeline: str
        :param _Period: Query interval. Options: [5s|1min|5min|15min].
        :type Period: str
        :param _StartTime: Start time for statistics. Default value: last hour. You can query data from the last 7 days at most.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :type StartTime: str
        :param _EndTime: End time for statistics. Defaults to one hour after `StartTime`. You can query the data of up to 24 hours.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :type EndTime: str
        :param _RemoteIp: Peer IP address.
        :type RemoteIp: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._RemoteIp = None

    @property
    def FlowId(self):
        r"""Transport stream ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        r"""Input or output type. Valid values: `input`, `output`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        r"""Input or output Id.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        r"""Primary or backup channel. Valid values: 0 and 1.
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def Period(self):
        r"""Query interval. Options: [5s|1min|5min|15min].
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""Start time for statistics. Default value: last hour. You can query data from the last 7 days at most.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time for statistics. Defaults to one hour after `StartTime`. You can query the data of up to 24 hours.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RemoteIp(self):
        r"""Peer IP address.
        :rtype: str
        """
        return self._RemoteIp

    @RemoteIp.setter
    def RemoteIp(self, RemoteIp):
        self._RemoteIp = RemoteIp


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RemoteIp = params.get("RemoteIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowMediaStatisticsResponse(AbstractModel):
    r"""DescribeStreamLinkFlowMediaStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of media data in the transport stream.
        :type Infos: list of FlowMediaInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        r"""List of media data in the transport stream.
        :rtype: list of FlowMediaInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowMediaInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRealtimeStatusRequest(AbstractModel):
    r"""DescribeStreamLinkFlowRealtimeStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Stream ID.</p>
        :type FlowId: str
        :param _InputIds: <p>Input an id array. If both the input and output arrays are empty, it signifies a full query.</p>
        :type InputIds: list of str
        :param _OutputIds: <p>Output id array. If both input and output arrays are empty, it signifies a full query.</p>
        :type OutputIds: list of str
        """
        self._FlowId = None
        self._InputIds = None
        self._OutputIds = None

    @property
    def FlowId(self):
        r"""<p>Stream ID.</p>
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InputIds(self):
        r"""<p>Input an id array. If both the input and output arrays are empty, it signifies a full query.</p>
        :rtype: list of str
        """
        return self._InputIds

    @InputIds.setter
    def InputIds(self, InputIds):
        self._InputIds = InputIds

    @property
    def OutputIds(self):
        r"""<p>Output id array. If both input and output arrays are empty, it signifies a full query.</p>
        :rtype: list of str
        """
        return self._OutputIds

    @OutputIds.setter
    def OutputIds(self, OutputIds):
        self._OutputIds = OutputIds


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._InputIds = params.get("InputIds")
        self._OutputIds = params.get("OutputIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowRealtimeStatusResponse(AbstractModel):
    r"""DescribeStreamLinkFlowRealtimeStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Timestamp: <p>Inquiry time. Unit: s.</p>
        :type Timestamp: int
        :param _Datas: <p>Real-time data information list.</p>
        :type Datas: list of FlowRealtimeStatusItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Timestamp = None
        self._Datas = None
        self._RequestId = None

    @property
    def Timestamp(self):
        r"""<p>Inquiry time. Unit: s.</p>
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Datas(self):
        r"""<p>Real-time data information list.</p>
        :rtype: list of FlowRealtimeStatusItem
        """
        return self._Datas

    @Datas.setter
    def Datas(self, Datas):
        self._Datas = Datas

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
        self._Timestamp = params.get("Timestamp")
        if params.get("Datas") is not None:
            self._Datas = []
            for item in params.get("Datas"):
                obj = FlowRealtimeStatusItem()
                obj._deserialize(item)
                self._Datas.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRequest(AbstractModel):
    r"""DescribeStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Stream Id.</p>
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        r"""<p>Stream Id.</p>
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowResponse(AbstractModel):
    r"""DescribeStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Info: <p>Configuration information of the stream.</p>
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""<p>Configuration information of the stream.</p>
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowSRTStatisticsRequest(AbstractModel):
    r"""DescribeStreamLinkFlowSRTStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Transport stream ID.
        :type FlowId: str
        :param _Type: Input or output type. Valid values: `input`, `output`.
        :type Type: str
        :param _InputOutputId: Input or output Id.
        :type InputOutputId: str
        :param _Pipeline: Primary or backup channel. Valid values: 0 and 1.
        :type Pipeline: str
        :param _StartTime: Start time for statistics. Default value: last hour. You can query data from the last 7 days at most.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :type StartTime: str
        :param _EndTime: End time for statistics. Default value: one hour after `StartTime`. You can query data up to 24 hours.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :type EndTime: str
        :param _Period: Query interval. Options: [5s|1min|5min|15min].
        :type Period: str
        :param _RemoteIp: Peer IP address.
        :type RemoteIp: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._RemoteIp = None

    @property
    def FlowId(self):
        r"""Transport stream ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        r"""Input or output type. Valid values: `input`, `output`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        r"""Input or output Id.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        r"""Primary or backup channel. Valid values: 0 and 1.
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def StartTime(self):
        r"""Start time for statistics. Default value: last hour. You can query data from the last 7 days at most.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time for statistics. Default value: one hour after `StartTime`. You can query data up to 24 hours.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        r"""Query interval. Options: [5s|1min|5min|15min].
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RemoteIp(self):
        r"""Peer IP address.
        :rtype: str
        """
        return self._RemoteIp

    @RemoteIp.setter
    def RemoteIp(self, RemoteIp):
        self._RemoteIp = RemoteIp


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        self._RemoteIp = params.get("RemoteIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowSRTStatisticsResponse(AbstractModel):
    r"""DescribeStreamLinkFlowSRTStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of SRT quality data in the transport stream.
        :type Infos: list of FlowSRTInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        r"""List of SRT quality data in the transport stream.
        :rtype: list of FlowSRTInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowSRTInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowStatisticsRequest(AbstractModel):
    r"""DescribeStreamLinkFlowStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Transport stream ID.
        :type FlowId: str
        :param _Type: Input or output type. Valid values: `input`, `output`.
        :type Type: str
        :param _InputOutputId: Input or output Id.
        :type InputOutputId: str
        :param _Pipeline: Primary or backup channel. Valid values: 0 and 1.
        :type Pipeline: str
        :param _Period: Query interval. Option: [5s|1min|5min|15min].
        :type Period: str
        :param _StartTime: Start time for statistics. Default value: last hour. You can query data from the last 7 days at most.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :type StartTime: str
        :param _EndTime: End time for statistics. Defaults to one hour after `StartTime`. You can query the data of up to 24 hours.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :type EndTime: str
        :param _RemoteIp: Peer client or server IP address.
        :type RemoteIp: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._RemoteIp = None

    @property
    def FlowId(self):
        r"""Transport stream ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        r"""Input or output type. Valid values: `input`, `output`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        r"""Input or output Id.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        r"""Primary or backup channel. Valid values: 0 and 1.
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def Period(self):
        r"""Query interval. Option: [5s|1min|5min|15min].
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""Start time for statistics. Default value: last hour. You can query data from the last 7 days at most.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""End time for statistics. Defaults to one hour after `StartTime`. You can query the data of up to 24 hours.
UTC time, for example, '2020-01-01T12:00:00Z'.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RemoteIp(self):
        r"""Peer client or server IP address.
        :rtype: str
        """
        return self._RemoteIp

    @RemoteIp.setter
    def RemoteIp(self, RemoteIp):
        self._RemoteIp = RemoteIp


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RemoteIp = params.get("RemoteIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowStatisticsResponse(AbstractModel):
    r"""DescribeStreamLinkFlowStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of media data in the transport stream.
        :type Infos: list of FlowStatisticsArray
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        r"""List of media data in the transport stream.
        :rtype: list of FlowStatisticsArray
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = FlowStatisticsArray()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowsRequest(AbstractModel):
    r"""DescribeStreamLinkFlows request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Current page number. Default value: 1.
        :type PageNum: int
        :param _PageSize: Size per page. Default value: 10.
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        r"""Current page number. Default value: 1.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""Size per page. Default value: 10.
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
        


class DescribeStreamLinkFlowsResponse(AbstractModel):
    r"""DescribeStreamLinkFlows response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Configuration information list of the stream.
        :type Infos: list of DescribeFlow
        :param _PageNum: Current page number.
        :type PageNum: int
        :param _PageSize: Size per page.
        :type PageSize: int
        :param _TotalNum: Total quantity.
        :type TotalNum: int
        :param _TotalPage: Total number of pages.
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
        r"""Configuration information list of the stream.
        :rtype: list of DescribeFlow
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        r"""Current page number.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        r"""Size per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        r"""Total quantity.
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        r"""Total number of pages.
        :rtype: int
        """
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

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
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = DescribeFlow()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkRegionsRequest(AbstractModel):
    r"""DescribeStreamLinkRegions request structure.

    """


class DescribeStreamLinkRegionsResponse(AbstractModel):
    r"""DescribeStreamLinkRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Media transmission region information.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.StreamLinkRegionInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""Media transmission region information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StreamLinkRegionInfo`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = StreamLinkRegionInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class FailOverOption(AbstractModel):
    r"""type FailOverOption struct {
    	FailOverType string `json:"FailOverType"` // Newly-added cold/standby COLDSTANDBY, HOTSTANDBY
    }

    """

    def __init__(self):
        r"""
        :param _FailOverType: Hot backup
        :type FailOverType: str
        """
        self._FailOverType = None

    @property
    def FailOverType(self):
        r"""Hot backup
        :rtype: str
        """
        return self._FailOverType

    @FailOverType.setter
    def FailOverType(self, FailOverType):
        self._FailOverType = FailOverType


    def _deserialize(self, params):
        self._FailOverType = params.get("FailOverType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowAudio(AbstractModel):
    r"""Audio data of the stream.

    """

    def __init__(self):
        r"""
        :param _Fps: Frame rate.
        :type Fps: int
        :param _Rate: Bitrate in bps.
        :type Rate: int
        :param _Pid: Audio Pid.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        r"""Frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        r"""Bitrate in bps.
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        r"""Audio Pid.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowLogInfo(AbstractModel):
    r"""Transmit streaming log information.

    """

    def __init__(self):
        r"""
        :param _Timestamp: Timestamp in seconds.
        :type Timestamp: int
        :param _Type: Input/output type. Valid values: `input`, `output`.
        :type Type: str
        :param _InputOutputId: Input or output Id.
        :type InputOutputId: str
        :param _Protocol: Protocol.
        :type Protocol: str
        :param _EventCode: Event code.
        :type EventCode: str
        :param _EventMessage: Event information.
        :type EventMessage: str
        :param _RemoteIp: Peer IP.
        :type RemoteIp: str
        :param _RemotePort: Peer port.
        :type RemotePort: str
        :param _Pipeline: Primary/secondary tunnel. 0: primary, 1: backup.
        :type Pipeline: str
        :param _InputOutputName: Input or output name.
        :type InputOutputName: str
        """
        self._Timestamp = None
        self._Type = None
        self._InputOutputId = None
        self._Protocol = None
        self._EventCode = None
        self._EventMessage = None
        self._RemoteIp = None
        self._RemotePort = None
        self._Pipeline = None
        self._InputOutputName = None

    @property
    def Timestamp(self):
        r"""Timestamp in seconds.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Type(self):
        r"""Input/output type. Valid values: `input`, `output`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        r"""Input or output Id.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Protocol(self):
        r"""Protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def EventCode(self):
        r"""Event code.
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventMessage(self):
        r"""Event information.
        :rtype: str
        """
        return self._EventMessage

    @EventMessage.setter
    def EventMessage(self, EventMessage):
        self._EventMessage = EventMessage

    @property
    def RemoteIp(self):
        r"""Peer IP.
        :rtype: str
        """
        return self._RemoteIp

    @RemoteIp.setter
    def RemoteIp(self, RemoteIp):
        self._RemoteIp = RemoteIp

    @property
    def RemotePort(self):
        r"""Peer port.
        :rtype: str
        """
        return self._RemotePort

    @RemotePort.setter
    def RemotePort(self, RemotePort):
        self._RemotePort = RemotePort

    @property
    def Pipeline(self):
        r"""Primary/secondary tunnel. 0: primary, 1: backup.
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def InputOutputName(self):
        r"""Input or output name.
        :rtype: str
        """
        return self._InputOutputName

    @InputOutputName.setter
    def InputOutputName(self, InputOutputName):
        self._InputOutputName = InputOutputName


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Protocol = params.get("Protocol")
        self._EventCode = params.get("EventCode")
        self._EventMessage = params.get("EventMessage")
        self._RemoteIp = params.get("RemoteIp")
        self._RemotePort = params.get("RemotePort")
        self._Pipeline = params.get("Pipeline")
        self._InputOutputName = params.get("InputOutputName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaAudio(AbstractModel):
    r"""Transmit audio data of streaming media.

    """

    def __init__(self):
        r"""
        :param _Fps: Frame rate.
        :type Fps: int
        :param _Rate: Bitrate in bps.
        :type Rate: int
        :param _Pid: Audio Pid.
        :type Pid: int
        :param _SessionId: Flag of the same push.
        :type SessionId: str
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None
        self._SessionId = None

    @property
    def Fps(self):
        r"""Frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        r"""Bitrate in bps.
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        r"""Audio Pid.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def SessionId(self):
        r"""Flag of the same push.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaInfo(AbstractModel):
    r"""Media data in the transport stream.

    """

    def __init__(self):
        r"""
        :param _Timestamp: Timestamp in seconds.
        :type Timestamp: int
        :param _Network: Total bandwidth.
        :type Network: int
        :param _Video: Video data of the transport stream.
        :type Video: list of FlowMediaVideo
        :param _Audio: Audio data of the transport stream.
        :type Audio: list of FlowMediaAudio
        :param _SessionId: Flag of the same push.
        :type SessionId: str
        :param _ClientIp: Client IP.
        :type ClientIp: str
        """
        self._Timestamp = None
        self._Network = None
        self._Video = None
        self._Audio = None
        self._SessionId = None
        self._ClientIp = None

    @property
    def Timestamp(self):
        r"""Timestamp in seconds.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Network(self):
        r"""Total bandwidth.
        :rtype: int
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Video(self):
        r"""Video data of the transport stream.
        :rtype: list of FlowMediaVideo
        """
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        r"""Audio data of the transport stream.
        :rtype: list of FlowMediaAudio
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def SessionId(self):
        r"""Flag of the same push.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ClientIp(self):
        r"""Client IP.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Network = params.get("Network")
        if params.get("Video") is not None:
            self._Video = []
            for item in params.get("Video"):
                obj = FlowMediaVideo()
                obj._deserialize(item)
                self._Video.append(obj)
        if params.get("Audio") is not None:
            self._Audio = []
            for item in params.get("Audio"):
                obj = FlowMediaAudio()
                obj._deserialize(item)
                self._Audio.append(obj)
        self._SessionId = params.get("SessionId")
        self._ClientIp = params.get("ClientIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaVideo(AbstractModel):
    r"""Transmit video data of streaming media.

    """

    def __init__(self):
        r"""
        :param _Fps: Frame rate.
        :type Fps: int
        :param _Rate: Bitrate in bps.
        :type Rate: int
        :param _Pid: Video Pid.
        :type Pid: int
        :param _SessionId: Flag of the same push.
        :type SessionId: str
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None
        self._SessionId = None

    @property
    def Fps(self):
        r"""Frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        r"""Bitrate in bps.
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        r"""Video Pid.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def SessionId(self):
        r"""Flag of the same push.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusCommon(AbstractModel):
    r"""Common status information for querying stream status in real time.

    """

    def __init__(self):
        r"""
        :param _State: Current connection status. Connected | Waiting | Idle.
        :type State: str
        :param _Mode: Connection mode. Listener|Caller.
        :type Mode: str
        :param _ConnectedTime: Connection duration, unit: ms.
        :type ConnectedTime: int
        :param _Bitrate: Real-time bitrate, unit in bps.
        :type Bitrate: int
        :param _Reconnections: Number of retries.
        :type Reconnections: int
        """
        self._State = None
        self._Mode = None
        self._ConnectedTime = None
        self._Bitrate = None
        self._Reconnections = None

    @property
    def State(self):
        r"""Current connection status. Connected | Waiting | Idle.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Mode(self):
        r"""Connection mode. Listener|Caller.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ConnectedTime(self):
        r"""Connection duration, unit: ms.
        :rtype: int
        """
        return self._ConnectedTime

    @ConnectedTime.setter
    def ConnectedTime(self, ConnectedTime):
        self._ConnectedTime = ConnectedTime

    @property
    def Bitrate(self):
        r"""Real-time bitrate, unit in bps.
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Reconnections(self):
        r"""Number of retries.
        :rtype: int
        """
        return self._Reconnections

    @Reconnections.setter
    def Reconnections(self, Reconnections):
        self._Reconnections = Reconnections


    def _deserialize(self, params):
        self._State = params.get("State")
        self._Mode = params.get("Mode")
        self._ConnectedTime = params.get("ConnectedTime")
        self._Bitrate = params.get("Bitrate")
        self._Reconnections = params.get("Reconnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusItem(AbstractModel):
    r"""Stream status information of the real-time stream status query API.

    """

    def __init__(self):
        r"""
        :param _Type: Type. Valid values: `Input`, `Output`.
        :type Type: str
        :param _InputId: Input Id. If Type is Input, this field is not empty.
        :type InputId: str
        :param _OutputId: Output Id. If Type is Output, this field is not empty.
        :type OutputId: str
        :param _FlowId: Stream Id.
        :type FlowId: str
        :param _Protocol: Protocol. SRT | RTMP.
        :type Protocol: str
        :param _CommonStatus: Common status information.
        :type CommonStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusCommon`
        :param _SRTStatus: If it is the SRT Protocol, this field will be present.
        :type SRTStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusSRT`
        :param _RTMPStatus: If it is the RTMP protocol, this field exists.
        :type RTMPStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTMP`
        :param _ConnectServerIP: Server IP address.
        :type ConnectServerIP: str
        :param _RTPStatus: If it is the RTP protocol, this field exists.
        :type RTPStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTP`
        """
        self._Type = None
        self._InputId = None
        self._OutputId = None
        self._FlowId = None
        self._Protocol = None
        self._CommonStatus = None
        self._SRTStatus = None
        self._RTMPStatus = None
        self._ConnectServerIP = None
        self._RTPStatus = None

    @property
    def Type(self):
        r"""Type. Valid values: `Input`, `Output`.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputId(self):
        r"""Input Id. If Type is Input, this field is not empty.
        :rtype: str
        """
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def OutputId(self):
        r"""Output Id. If Type is Output, this field is not empty.
        :rtype: str
        """
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def FlowId(self):
        r"""Stream Id.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Protocol(self):
        r"""Protocol. SRT | RTMP.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CommonStatus(self):
        r"""Common status information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusCommon`
        """
        return self._CommonStatus

    @CommonStatus.setter
    def CommonStatus(self, CommonStatus):
        self._CommonStatus = CommonStatus

    @property
    def SRTStatus(self):
        r"""If it is the SRT Protocol, this field will be present.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusSRT`
        """
        return self._SRTStatus

    @SRTStatus.setter
    def SRTStatus(self, SRTStatus):
        self._SRTStatus = SRTStatus

    @property
    def RTMPStatus(self):
        r"""If it is the RTMP protocol, this field exists.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTMP`
        """
        return self._RTMPStatus

    @RTMPStatus.setter
    def RTMPStatus(self, RTMPStatus):
        self._RTMPStatus = RTMPStatus

    @property
    def ConnectServerIP(self):
        r"""Server IP address.
        :rtype: str
        """
        return self._ConnectServerIP

    @ConnectServerIP.setter
    def ConnectServerIP(self, ConnectServerIP):
        self._ConnectServerIP = ConnectServerIP

    @property
    def RTPStatus(self):
        r"""If it is the RTP protocol, this field exists.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTP`
        """
        return self._RTPStatus

    @RTPStatus.setter
    def RTPStatus(self, RTPStatus):
        self._RTPStatus = RTPStatus


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._InputId = params.get("InputId")
        self._OutputId = params.get("OutputId")
        self._FlowId = params.get("FlowId")
        self._Protocol = params.get("Protocol")
        if params.get("CommonStatus") is not None:
            self._CommonStatus = FlowRealtimeStatusCommon()
            self._CommonStatus._deserialize(params.get("CommonStatus"))
        if params.get("SRTStatus") is not None:
            self._SRTStatus = FlowRealtimeStatusSRT()
            self._SRTStatus._deserialize(params.get("SRTStatus"))
        if params.get("RTMPStatus") is not None:
            self._RTMPStatus = FlowRealtimeStatusRTMP()
            self._RTMPStatus._deserialize(params.get("RTMPStatus"))
        self._ConnectServerIP = params.get("ConnectServerIP")
        if params.get("RTPStatus") is not None:
            self._RTPStatus = FlowRealtimeStatusRTP()
            self._RTPStatus._deserialize(params.get("RTPStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTMP(AbstractModel):
    r"""RTMP information of the real-time stream status query API.

    """

    def __init__(self):
        r"""
        :param _VideoFPS: Video frame rate.
        :type VideoFPS: int
        :param _AudioFPS: Audio frame rate.
        :type AudioFPS: int
        """
        self._VideoFPS = None
        self._AudioFPS = None

    @property
    def VideoFPS(self):
        r"""Video frame rate.
        :rtype: int
        """
        return self._VideoFPS

    @VideoFPS.setter
    def VideoFPS(self, VideoFPS):
        self._VideoFPS = VideoFPS

    @property
    def AudioFPS(self):
        r"""Audio frame rate.
        :rtype: int
        """
        return self._AudioFPS

    @AudioFPS.setter
    def AudioFPS(self, AudioFPS):
        self._AudioFPS = AudioFPS


    def _deserialize(self, params):
        self._VideoFPS = params.get("VideoFPS")
        self._AudioFPS = params.get("AudioFPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTP(AbstractModel):
    r"""RTP stream status information of the real-time stream status query API.

    """

    def __init__(self):
        r"""
        :param _Packets: Number of transmitted packets
        :type Packets: int
        """
        self._Packets = None

    @property
    def Packets(self):
        r"""Number of transmitted packets
        :rtype: int
        """
        return self._Packets

    @Packets.setter
    def Packets(self, Packets):
        self._Packets = Packets


    def _deserialize(self, params):
        self._Packets = params.get("Packets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusSRT(AbstractModel):
    r"""SRT information of the real-time stream status query API.

    """

    def __init__(self):
        r"""
        :param _Latency: Delay in ms.
        :type Latency: int
        :param _RTT: RTT in ms.
        :type RTT: int
        :param _Packets: Number of packets sent or received in real time.
        :type Packets: int
        :param _PacketLossRate: Packet loss rate.
        :type PacketLossRate: float
        :param _RetransmitRate: Retransmission rate.
        :type RetransmitRate: float
        :param _DroppedPackets: Real-time packet loss count.
        :type DroppedPackets: int
        :param _Encryption: Whether to encrypt. On | Off.
        :type Encryption: str
        """
        self._Latency = None
        self._RTT = None
        self._Packets = None
        self._PacketLossRate = None
        self._RetransmitRate = None
        self._DroppedPackets = None
        self._Encryption = None

    @property
    def Latency(self):
        r"""Delay in ms.
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RTT(self):
        r"""RTT in ms.
        :rtype: int
        """
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def Packets(self):
        r"""Number of packets sent or received in real time.
        :rtype: int
        """
        return self._Packets

    @Packets.setter
    def Packets(self, Packets):
        self._Packets = Packets

    @property
    def PacketLossRate(self):
        r"""Packet loss rate.
        :rtype: float
        """
        return self._PacketLossRate

    @PacketLossRate.setter
    def PacketLossRate(self, PacketLossRate):
        self._PacketLossRate = PacketLossRate

    @property
    def RetransmitRate(self):
        r"""Retransmission rate.
        :rtype: float
        """
        return self._RetransmitRate

    @RetransmitRate.setter
    def RetransmitRate(self, RetransmitRate):
        self._RetransmitRate = RetransmitRate

    @property
    def DroppedPackets(self):
        r"""Real-time packet loss count.
        :rtype: int
        """
        return self._DroppedPackets

    @DroppedPackets.setter
    def DroppedPackets(self, DroppedPackets):
        self._DroppedPackets = DroppedPackets

    @property
    def Encryption(self):
        r"""Whether to encrypt. On | Off.
        :rtype: str
        """
        return self._Encryption

    @Encryption.setter
    def Encryption(self, Encryption):
        self._Encryption = Encryption


    def _deserialize(self, params):
        self._Latency = params.get("Latency")
        self._RTT = params.get("RTT")
        self._Packets = params.get("Packets")
        self._PacketLossRate = params.get("PacketLossRate")
        self._RetransmitRate = params.get("RetransmitRate")
        self._DroppedPackets = params.get("DroppedPackets")
        self._Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowSRTInfo(AbstractModel):
    r"""SRT quality data in the transport stream.

    """

    def __init__(self):
        r"""
        :param _Timestamp: <p>Timestamp in seconds.</p>
        :type Timestamp: int
        :param _SendPacketLossRate: <p>Packet loss rate on transmitting.</p>
        :type SendPacketLossRate: int
        :param _SendRetransmissionRate: <p>Retransmission rate.</p>
        :type SendRetransmissionRate: int
        :param _RecvPacketLossRate: <p>Packet loss rate on receiving.</p>
        :type RecvPacketLossRate: int
        :param _RecvRetransmissionRate: <p>Receiving retransmission rate.</p>
        :type RecvRetransmissionRate: int
        :param _RTT: <p>RTT latency to the peer.</p>
        :type RTT: int
        :param _SessionId: <p>Flag the same streaming session.</p>
        :type SessionId: str
        :param _SendPacketDropNumber: <p>Number of discarded packets on sending.</p>
        :type SendPacketDropNumber: int
        :param _RecvPacketDropNumber: <p>Number of received dropped packets.</p>
        :type RecvPacketDropNumber: int
        :param _Bandwidth: <p>Bandwidth.</p>
        :type Bandwidth: float
        :param _SendBandwidth: <p>Transmit bandwidth</p>
        :type SendBandwidth: float
        :param _RecvBandwidth: <p>Receiving bandwidth</p>
        :type RecvBandwidth: float
        :param _SendPackets: <p>Sent packet count</p>
        :type SendPackets: int
        :param _RecvPackets: <p>Number of received packets</p>
        :type RecvPackets: int
        :param _SendLostPackets: <p>Sending lost packets</p>
        :type SendLostPackets: int
        :param _RecvLostPackets: <p>Accept lost packets</p>
        :type RecvLostPackets: int
        :param _SendRetransmitPackets: <p>Sent retransmission packet count</p>
        :type SendRetransmitPackets: int
        :param _RecvRetransmitPackets: <p>Number of received retransmission packets</p>
        :type RecvRetransmitPackets: int
        :param _FlightSize: <p>Flight window size</p>
        :type FlightSize: int
        :param _CongestionWindow: <p>Congestion window.</p>
        :type CongestionWindow: int
        :param _SendBuffer: <p>Sending buffer (ms)</p>
        :type SendBuffer: int
        :param _RecvBuffer: <p>Receive buffer (ms)</p>
        :type RecvBuffer: int
        :param _SendLatency: <p>Sending delay</p>
        :type SendLatency: int
        :param _RecvLatency: <p>Receive latency</p>
        :type RecvLatency: int
        :param _SendNAKPackets: <p>Sent NAK packet count</p>
        :type SendNAKPackets: int
        :param _RecvNAKPackets: <p>Number of received NAK packets</p>
        :type RecvNAKPackets: int
        """
        self._Timestamp = None
        self._SendPacketLossRate = None
        self._SendRetransmissionRate = None
        self._RecvPacketLossRate = None
        self._RecvRetransmissionRate = None
        self._RTT = None
        self._SessionId = None
        self._SendPacketDropNumber = None
        self._RecvPacketDropNumber = None
        self._Bandwidth = None
        self._SendBandwidth = None
        self._RecvBandwidth = None
        self._SendPackets = None
        self._RecvPackets = None
        self._SendLostPackets = None
        self._RecvLostPackets = None
        self._SendRetransmitPackets = None
        self._RecvRetransmitPackets = None
        self._FlightSize = None
        self._CongestionWindow = None
        self._SendBuffer = None
        self._RecvBuffer = None
        self._SendLatency = None
        self._RecvLatency = None
        self._SendNAKPackets = None
        self._RecvNAKPackets = None

    @property
    def Timestamp(self):
        r"""<p>Timestamp in seconds.</p>
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SendPacketLossRate(self):
        r"""<p>Packet loss rate on transmitting.</p>
        :rtype: int
        """
        return self._SendPacketLossRate

    @SendPacketLossRate.setter
    def SendPacketLossRate(self, SendPacketLossRate):
        self._SendPacketLossRate = SendPacketLossRate

    @property
    def SendRetransmissionRate(self):
        r"""<p>Retransmission rate.</p>
        :rtype: int
        """
        return self._SendRetransmissionRate

    @SendRetransmissionRate.setter
    def SendRetransmissionRate(self, SendRetransmissionRate):
        self._SendRetransmissionRate = SendRetransmissionRate

    @property
    def RecvPacketLossRate(self):
        r"""<p>Packet loss rate on receiving.</p>
        :rtype: int
        """
        return self._RecvPacketLossRate

    @RecvPacketLossRate.setter
    def RecvPacketLossRate(self, RecvPacketLossRate):
        self._RecvPacketLossRate = RecvPacketLossRate

    @property
    def RecvRetransmissionRate(self):
        r"""<p>Receiving retransmission rate.</p>
        :rtype: int
        """
        return self._RecvRetransmissionRate

    @RecvRetransmissionRate.setter
    def RecvRetransmissionRate(self, RecvRetransmissionRate):
        self._RecvRetransmissionRate = RecvRetransmissionRate

    @property
    def RTT(self):
        r"""<p>RTT latency to the peer.</p>
        :rtype: int
        """
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def SessionId(self):
        r"""<p>Flag the same streaming session.</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SendPacketDropNumber(self):
        r"""<p>Number of discarded packets on sending.</p>
        :rtype: int
        """
        return self._SendPacketDropNumber

    @SendPacketDropNumber.setter
    def SendPacketDropNumber(self, SendPacketDropNumber):
        self._SendPacketDropNumber = SendPacketDropNumber

    @property
    def RecvPacketDropNumber(self):
        r"""<p>Number of received dropped packets.</p>
        :rtype: int
        """
        return self._RecvPacketDropNumber

    @RecvPacketDropNumber.setter
    def RecvPacketDropNumber(self, RecvPacketDropNumber):
        self._RecvPacketDropNumber = RecvPacketDropNumber

    @property
    def Bandwidth(self):
        r"""<p>Bandwidth.</p>
        :rtype: float
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def SendBandwidth(self):
        r"""<p>Transmit bandwidth</p>
        :rtype: float
        """
        return self._SendBandwidth

    @SendBandwidth.setter
    def SendBandwidth(self, SendBandwidth):
        self._SendBandwidth = SendBandwidth

    @property
    def RecvBandwidth(self):
        r"""<p>Receiving bandwidth</p>
        :rtype: float
        """
        return self._RecvBandwidth

    @RecvBandwidth.setter
    def RecvBandwidth(self, RecvBandwidth):
        self._RecvBandwidth = RecvBandwidth

    @property
    def SendPackets(self):
        r"""<p>Sent packet count</p>
        :rtype: int
        """
        return self._SendPackets

    @SendPackets.setter
    def SendPackets(self, SendPackets):
        self._SendPackets = SendPackets

    @property
    def RecvPackets(self):
        r"""<p>Number of received packets</p>
        :rtype: int
        """
        return self._RecvPackets

    @RecvPackets.setter
    def RecvPackets(self, RecvPackets):
        self._RecvPackets = RecvPackets

    @property
    def SendLostPackets(self):
        r"""<p>Sending lost packets</p>
        :rtype: int
        """
        return self._SendLostPackets

    @SendLostPackets.setter
    def SendLostPackets(self, SendLostPackets):
        self._SendLostPackets = SendLostPackets

    @property
    def RecvLostPackets(self):
        r"""<p>Accept lost packets</p>
        :rtype: int
        """
        return self._RecvLostPackets

    @RecvLostPackets.setter
    def RecvLostPackets(self, RecvLostPackets):
        self._RecvLostPackets = RecvLostPackets

    @property
    def SendRetransmitPackets(self):
        r"""<p>Sent retransmission packet count</p>
        :rtype: int
        """
        return self._SendRetransmitPackets

    @SendRetransmitPackets.setter
    def SendRetransmitPackets(self, SendRetransmitPackets):
        self._SendRetransmitPackets = SendRetransmitPackets

    @property
    def RecvRetransmitPackets(self):
        r"""<p>Number of received retransmission packets</p>
        :rtype: int
        """
        return self._RecvRetransmitPackets

    @RecvRetransmitPackets.setter
    def RecvRetransmitPackets(self, RecvRetransmitPackets):
        self._RecvRetransmitPackets = RecvRetransmitPackets

    @property
    def FlightSize(self):
        r"""<p>Flight window size</p>
        :rtype: int
        """
        return self._FlightSize

    @FlightSize.setter
    def FlightSize(self, FlightSize):
        self._FlightSize = FlightSize

    @property
    def CongestionWindow(self):
        r"""<p>Congestion window.</p>
        :rtype: int
        """
        return self._CongestionWindow

    @CongestionWindow.setter
    def CongestionWindow(self, CongestionWindow):
        self._CongestionWindow = CongestionWindow

    @property
    def SendBuffer(self):
        r"""<p>Sending buffer (ms)</p>
        :rtype: int
        """
        return self._SendBuffer

    @SendBuffer.setter
    def SendBuffer(self, SendBuffer):
        self._SendBuffer = SendBuffer

    @property
    def RecvBuffer(self):
        r"""<p>Receive buffer (ms)</p>
        :rtype: int
        """
        return self._RecvBuffer

    @RecvBuffer.setter
    def RecvBuffer(self, RecvBuffer):
        self._RecvBuffer = RecvBuffer

    @property
    def SendLatency(self):
        r"""<p>Sending delay</p>
        :rtype: int
        """
        return self._SendLatency

    @SendLatency.setter
    def SendLatency(self, SendLatency):
        self._SendLatency = SendLatency

    @property
    def RecvLatency(self):
        r"""<p>Receive latency</p>
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def SendNAKPackets(self):
        r"""<p>Sent NAK packet count</p>
        :rtype: int
        """
        return self._SendNAKPackets

    @SendNAKPackets.setter
    def SendNAKPackets(self, SendNAKPackets):
        self._SendNAKPackets = SendNAKPackets

    @property
    def RecvNAKPackets(self):
        r"""<p>Number of received NAK packets</p>
        :rtype: int
        """
        return self._RecvNAKPackets

    @RecvNAKPackets.setter
    def RecvNAKPackets(self, RecvNAKPackets):
        self._RecvNAKPackets = RecvNAKPackets


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._SendPacketLossRate = params.get("SendPacketLossRate")
        self._SendRetransmissionRate = params.get("SendRetransmissionRate")
        self._RecvPacketLossRate = params.get("RecvPacketLossRate")
        self._RecvRetransmissionRate = params.get("RecvRetransmissionRate")
        self._RTT = params.get("RTT")
        self._SessionId = params.get("SessionId")
        self._SendPacketDropNumber = params.get("SendPacketDropNumber")
        self._RecvPacketDropNumber = params.get("RecvPacketDropNumber")
        self._Bandwidth = params.get("Bandwidth")
        self._SendBandwidth = params.get("SendBandwidth")
        self._RecvBandwidth = params.get("RecvBandwidth")
        self._SendPackets = params.get("SendPackets")
        self._RecvPackets = params.get("RecvPackets")
        self._SendLostPackets = params.get("SendLostPackets")
        self._RecvLostPackets = params.get("RecvLostPackets")
        self._SendRetransmitPackets = params.get("SendRetransmitPackets")
        self._RecvRetransmitPackets = params.get("RecvRetransmitPackets")
        self._FlightSize = params.get("FlightSize")
        self._CongestionWindow = params.get("CongestionWindow")
        self._SendBuffer = params.get("SendBuffer")
        self._RecvBuffer = params.get("RecvBuffer")
        self._SendLatency = params.get("SendLatency")
        self._RecvLatency = params.get("RecvLatency")
        self._SendNAKPackets = params.get("SendNAKPackets")
        self._RecvNAKPackets = params.get("RecvNAKPackets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatistics(AbstractModel):
    r"""Stream stats.

    """

    def __init__(self):
        r"""
        :param _SessionId: Session ID.
        :type SessionId: str
        :param _ClientIp: Peer IP.
        :type ClientIp: str
        :param _Network: Total bandwidth.
        :type Network: int
        :param _Video: Video data.
        :type Video: list of FlowVideo
        :param _Audio: Audio data.
        :type Audio: list of FlowAudio
        """
        self._SessionId = None
        self._ClientIp = None
        self._Network = None
        self._Video = None
        self._Audio = None

    @property
    def SessionId(self):
        r"""Session ID.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ClientIp(self):
        r"""Peer IP.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Network(self):
        r"""Total bandwidth.
        :rtype: int
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Video(self):
        r"""Video data.
        :rtype: list of FlowVideo
        """
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        r"""Audio data.
        :rtype: list of FlowAudio
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._ClientIp = params.get("ClientIp")
        self._Network = params.get("Network")
        if params.get("Video") is not None:
            self._Video = []
            for item in params.get("Video"):
                obj = FlowVideo()
                obj._deserialize(item)
                self._Video.append(obj)
        if params.get("Audio") is not None:
            self._Audio = []
            for item in params.get("Audio"):
                obj = FlowAudio()
                obj._deserialize(item)
                self._Audio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatisticsArray(AbstractModel):
    r"""List of the stream's statistical data.

    """

    def __init__(self):
        r"""
        :param _Timestamp: Timestamp.
        :type Timestamp: int
        :param _FlowStatistics: Statistics for each session.
        :type FlowStatistics: list of FlowStatistics
        """
        self._Timestamp = None
        self._FlowStatistics = None

    @property
    def Timestamp(self):
        r"""Timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def FlowStatistics(self):
        r"""Statistics for each session.
        :rtype: list of FlowStatistics
        """
        return self._FlowStatistics

    @FlowStatistics.setter
    def FlowStatistics(self, FlowStatistics):
        self._FlowStatistics = FlowStatistics


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        if params.get("FlowStatistics") is not None:
            self._FlowStatistics = []
            for item in params.get("FlowStatistics"):
                obj = FlowStatistics()
                obj._deserialize(item)
                self._FlowStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowVideo(AbstractModel):
    r"""Video data of the stream.

    """

    def __init__(self):
        r"""
        :param _Fps: Frame rate.
        :type Fps: int
        :param _Rate: Bitrate in bps.
        :type Rate: int
        :param _Pid: Audio Pid.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        r"""Frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        r"""Bitrate in bps.
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        r"""Audio Pid.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HLSPullSourceAddress(AbstractModel):
    r"""Configuration message of the created input HLS pull source station.

    """

    def __init__(self):
        r"""
        :param _Url: Url of the HLS origin server.
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""Url of the HLS origin server.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputAddress(AbstractModel):
    r"""Input address information.

    """

    def __init__(self):
        r"""
        :param _Ip: IP of the input address.
        :type Ip: str
        :param _Port: The port of the input address.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""IP of the input address.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""The port of the input address.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInput(AbstractModel):
    r"""Modify the parameters of the input.

    """

    def __init__(self):
        r"""
        :param _InputId: Input Id.
        :type InputId: str
        :param _InputName: Enter a name.
        :type InputName: str
        :param _Description: Input description.
        :type Description: str
        :param _AllowIpList: IPs allowed for push, in CIDR format.
        :type AllowIpList: list of str
        :param _SRTSettings: Configuration of SRT.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param _RTPSettings: Configuration message of RTP.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param _Protocol: Input protocol. Options: SRT, RTP, RTMP, RTMP_PULL, RTSP_PULL, RIST.
        :type Protocol: str
        :param _FailOver: Input primary/replica switch. Option: [OPEN|CLOSE].
        :type FailOver: str
        :param _RTMPPullSettings: Configuration message of RTMP_PULL.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        :param _RTSPPullSettings: Configuration message of RTSP_PULL.
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        :param _HLSPullSettings: Configuration message of HLS_PULL.
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        :param _ResilientStream: Configuration message for smooth stream output during delayed playback.
        :type ResilientStream: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        :param _SecurityGroupIds: ID of the bound input security group. Only one security group can be associated.
        :type SecurityGroupIds: list of str
        :param _Zones: Availability zone. Optional. input limit: two availability zones. For this API, only the second availability zone participates in resource allocation. It is valid if disaster recovery is enabled or the RTSP_PULL protocol is involved during switching. The address will be reallocated.	
        :type Zones: list of str
        :param _RISTSettings: Configuration information of RIST.
        :type RISTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRISTSettings`
        :param _InputRegion: Region of the input node.
        :type InputRegion: str
        :param _FailOverOption: Hot/cold backup related
        :type FailOverOption: :class:`tencentcloud.mdc.v20200828.models.FailOverOption`
        """
        self._InputId = None
        self._InputName = None
        self._Description = None
        self._AllowIpList = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._Protocol = None
        self._FailOver = None
        self._RTMPPullSettings = None
        self._RTSPPullSettings = None
        self._HLSPullSettings = None
        self._ResilientStream = None
        self._SecurityGroupIds = None
        self._Zones = None
        self._RISTSettings = None
        self._InputRegion = None
        self._FailOverOption = None

    @property
    def InputId(self):
        r"""Input Id.
        :rtype: str
        """
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def InputName(self):
        r"""Enter a name.
        :rtype: str
        """
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Description(self):
        r"""Input description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AllowIpList(self):
        r"""IPs allowed for push, in CIDR format.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        r"""Configuration of SRT.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        r"""Configuration message of RTP.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def Protocol(self):
        r"""Input protocol. Options: SRT, RTP, RTMP, RTMP_PULL, RTSP_PULL, RIST.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def FailOver(self):
        r"""Input primary/replica switch. Option: [OPEN|CLOSE].
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def RTMPPullSettings(self):
        r"""Configuration message of RTMP_PULL.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def RTSPPullSettings(self):
        r"""Configuration message of RTSP_PULL.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        r"""Configuration message of HLS_PULL.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def ResilientStream(self):
        r"""Configuration message for smooth stream output during delayed playback.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        """
        return self._ResilientStream

    @ResilientStream.setter
    def ResilientStream(self, ResilientStream):
        self._ResilientStream = ResilientStream

    @property
    def SecurityGroupIds(self):
        r"""ID of the bound input security group. Only one security group can be associated.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        r"""Availability zone. Optional. input limit: two availability zones. For this API, only the second availability zone participates in resource allocation. It is valid if disaster recovery is enabled or the RTSP_PULL protocol is involved during switching. The address will be reallocated.	
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RISTSettings(self):
        r"""Configuration information of RIST.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRISTSettings`
        """
        return self._RISTSettings

    @RISTSettings.setter
    def RISTSettings(self, RISTSettings):
        self._RISTSettings = RISTSettings

    @property
    def InputRegion(self):
        r"""Region of the input node.
        :rtype: str
        """
        return self._InputRegion

    @InputRegion.setter
    def InputRegion(self, InputRegion):
        self._InputRegion = InputRegion

    @property
    def FailOverOption(self):
        r"""Hot/cold backup related
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FailOverOption`
        """
        return self._FailOverOption

    @FailOverOption.setter
    def FailOverOption(self, FailOverOption):
        self._FailOverOption = FailOverOption


    def _deserialize(self, params):
        self._InputId = params.get("InputId")
        self._InputName = params.get("InputName")
        self._Description = params.get("Description")
        self._AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateInputSRTSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateInputRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        self._Protocol = params.get("Protocol")
        self._FailOver = params.get("FailOver")
        if params.get("RTMPPullSettings") is not None:
            self._RTMPPullSettings = CreateInputRTMPPullSettings()
            self._RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        if params.get("RTSPPullSettings") is not None:
            self._RTSPPullSettings = CreateInputRTSPPullSettings()
            self._RTSPPullSettings._deserialize(params.get("RTSPPullSettings"))
        if params.get("HLSPullSettings") is not None:
            self._HLSPullSettings = CreateInputHLSPullSettings()
            self._HLSPullSettings._deserialize(params.get("HLSPullSettings"))
        if params.get("ResilientStream") is not None:
            self._ResilientStream = ResilientStreamConf()
            self._ResilientStream._deserialize(params.get("ResilientStream"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zones = params.get("Zones")
        if params.get("RISTSettings") is not None:
            self._RISTSettings = CreateInputRISTSettings()
            self._RISTSettings._deserialize(params.get("RISTSettings"))
        self._InputRegion = params.get("InputRegion")
        if params.get("FailOverOption") is not None:
            self._FailOverOption = FailOverOption()
            self._FailOverOption._deserialize(params.get("FailOverOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOutputInfo(AbstractModel):
    r"""Modify the Output configuration.

    """

    def __init__(self):
        r"""
        :param _OutputId: Id of the Output to be modified.
        :type OutputId: str
        :param _OutputName: Output name.
        :type OutputName: str
        :param _Description: Output description.
        :type Description: str
        :param _Protocol: Output relay protocol. Supports SRT, RTP, RTMP, RTMP_PULL, RTSP_PULL, and RIST.
        :type Protocol: str
        :param _OutputType: Output type: Internet/TencentCSS/StreamLive
        :type OutputType: str
        :param _OutputKind: Output module type, including Pinpoint (single-point output, supports up to four concurrent outputs); MultiMesh (multiple outputs, supports more than four concurrent outputs, currently up to 200). The default type is Pinpoint output. For a single Flow, only one MultiMesh output is allowed in one zone.
        :type OutputKind: str
        :param _SRTSettings: Configuration of the relayed SRT.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param _RTPSettings: Configuration of the relayed RTP.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param _RTMPSettings: Configuration for relaying RTMP.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param _AllowIpList: IP whitelist list in CIDR format, for example, 0.0.0.0/0.
Valid when Protocol is RTMP_PULL. If empty, it represents no limit on client IP.
        :type AllowIpList: list of str
        :param _MaxConcurrent: Maximum number of concurrent stream pulls. Maximum value: 4. Default value: 4.
        :type MaxConcurrent: int
        :param _SecurityGroupIds: ID of the bound security group. Only one security group can be associated.	
        :type SecurityGroupIds: list of str
        :param _Zones: AZ.
        :type Zones: list of str
        :param _RISTSettings: Relay RIST configuration.
        :type RISTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRistSettings`
        :param _PidSelector: For streams with multiple audio/video tracks, you can specify the track to be used.
        :type PidSelector: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        :param _StreamSelector: For streams with multiple audio/video tracks, you can specify the track to be used.
        :type StreamSelector: :class:`tencentcloud.mdc.v20200828.models.StreamSelector`
        """
        self._OutputId = None
        self._OutputName = None
        self._Description = None
        self._Protocol = None
        self._OutputType = None
        self._OutputKind = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._RTMPSettings = None
        self._AllowIpList = None
        self._MaxConcurrent = None
        self._SecurityGroupIds = None
        self._Zones = None
        self._RISTSettings = None
        self._PidSelector = None
        self._StreamSelector = None

    @property
    def OutputId(self):
        r"""Id of the Output to be modified.
        :rtype: str
        """
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def OutputName(self):
        r"""Output name.
        :rtype: str
        """
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def Description(self):
        r"""Output description.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        r"""Output relay protocol. Supports SRT, RTP, RTMP, RTMP_PULL, RTSP_PULL, and RIST.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutputType(self):
        r"""Output type: Internet/TencentCSS/StreamLive
        :rtype: str
        """
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def OutputKind(self):
        r"""Output module type, including Pinpoint (single-point output, supports up to four concurrent outputs); MultiMesh (multiple outputs, supports more than four concurrent outputs, currently up to 200). The default type is Pinpoint output. For a single Flow, only one MultiMesh output is allowed in one zone.
        :rtype: str
        """
        return self._OutputKind

    @OutputKind.setter
    def OutputKind(self, OutputKind):
        self._OutputKind = OutputKind

    @property
    def SRTSettings(self):
        r"""Configuration of the relayed SRT.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        r"""Configuration of the relayed RTP.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def RTMPSettings(self):
        r"""Configuration for relaying RTMP.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def AllowIpList(self):
        r"""IP whitelist list in CIDR format, for example, 0.0.0.0/0.
Valid when Protocol is RTMP_PULL. If empty, it represents no limit on client IP.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def MaxConcurrent(self):
        r"""Maximum number of concurrent stream pulls. Maximum value: 4. Default value: 4.
        :rtype: int
        """
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def SecurityGroupIds(self):
        r"""ID of the bound security group. Only one security group can be associated.	
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        r"""AZ.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

    @property
    def RISTSettings(self):
        r"""Relay RIST configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRistSettings`
        """
        return self._RISTSettings

    @RISTSettings.setter
    def RISTSettings(self, RISTSettings):
        self._RISTSettings = RISTSettings

    @property
    def PidSelector(self):
        warnings.warn("parameter `PidSelector` is deprecated", DeprecationWarning) 

        r"""For streams with multiple audio/video tracks, you can specify the track to be used.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        """
        return self._PidSelector

    @PidSelector.setter
    def PidSelector(self, PidSelector):
        warnings.warn("parameter `PidSelector` is deprecated", DeprecationWarning) 

        self._PidSelector = PidSelector

    @property
    def StreamSelector(self):
        r"""For streams with multiple audio/video tracks, you can specify the track to be used.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StreamSelector`
        """
        return self._StreamSelector

    @StreamSelector.setter
    def StreamSelector(self, StreamSelector):
        self._StreamSelector = StreamSelector


    def _deserialize(self, params):
        self._OutputId = params.get("OutputId")
        self._OutputName = params.get("OutputName")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        self._OutputType = params.get("OutputType")
        self._OutputKind = params.get("OutputKind")
        if params.get("SRTSettings") is not None:
            self._SRTSettings = CreateOutputSrtSettings()
            self._SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self._RTPSettings = CreateOutputInfoRTPSettings()
            self._RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self._RTMPSettings = CreateOutputRTMPSettings()
            self._RTMPSettings._deserialize(params.get("RTMPSettings"))
        self._AllowIpList = params.get("AllowIpList")
        self._MaxConcurrent = params.get("MaxConcurrent")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._Zones = params.get("Zones")
        if params.get("RISTSettings") is not None:
            self._RISTSettings = CreateOutputRistSettings()
            self._RISTSettings._deserialize(params.get("RISTSettings"))
        if params.get("PidSelector") is not None:
            self._PidSelector = PidSelector()
            self._PidSelector._deserialize(params.get("PidSelector"))
        if params.get("StreamSelector") is not None:
            self._StreamSelector = StreamSelector()
            self._StreamSelector._deserialize(params.get("StreamSelector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowRequest(AbstractModel):
    r"""ModifyStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Stream Id.
        :type FlowId: str
        :param _FlowName: Stream name to be modified.
        :type FlowName: str
        """
        self._FlowId = None
        self._FlowName = None

    @property
    def FlowId(self):
        r"""Stream Id.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        r"""Stream name to be modified.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._FlowName = params.get("FlowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowResponse(AbstractModel):
    r"""ModifyStreamLinkFlow response structure.

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


class ModifyStreamLinkInputRequest(AbstractModel):
    r"""ModifyStreamLinkInput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Stream Id.
        :type FlowId: str
        :param _Input: Input information that needs to be modified.
        :type Input: :class:`tencentcloud.mdc.v20200828.models.ModifyInput`
        """
        self._FlowId = None
        self._Input = None

    @property
    def FlowId(self):
        r"""Stream Id.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Input(self):
        r"""Input information that needs to be modified.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyInput`
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Input") is not None:
            self._Input = ModifyInput()
            self._Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkInputResponse(AbstractModel):
    r"""ModifyStreamLinkInput response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Input information after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeInput`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""Input information after modification.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInput`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = DescribeInput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class ModifyStreamLinkOutputInfoRequest(AbstractModel):
    r"""ModifyStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: 01937702ecc509dc0f3269ca3420
        :type FlowId: str
        :param _Output: Output configuration that needs to be modified.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.ModifyOutputInfo`
        """
        self._FlowId = None
        self._Output = None

    @property
    def FlowId(self):
        r"""01937702ecc509dc0f3269ca3420
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Output(self):
        r"""Output configuration that needs to be modified.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyOutputInfo`
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self._Output = ModifyOutputInfo()
            self._Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkOutputInfoResponse(AbstractModel):
    r"""ModifyStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Output configuration after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        r"""Output configuration after modification.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

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
        if params.get("Info") is not None:
            self._Info = DescribeOutput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class OutputAddress(AbstractModel):
    r"""Egress address of the output.

    """

    def __init__(self):
        r"""
        :param _Ip: Outbound IP address.
        :type Ip: str
        """
        self._Ip = None

    @property
    def Ip(self):
        r"""Outbound IP address.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputRISTSourceAddressResp(AbstractModel):
    r"""Listening address for RIST output.

    """

    def __init__(self):
        r"""
        :param _Ip: Listening IP.
        :type Ip: str
        :param _Port: Listening port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""Listening IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Listening port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputSRTSourceAddressResp(AbstractModel):
    r"""SRT output listening address.

    """

    def __init__(self):
        r"""
        :param _Ip: Listening IP.
        :type Ip: str
        :param _Port: Listening port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""Listening IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Listening port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PidSelector(AbstractModel):
    r"""For streams with multiple audio/video tracks, you can specify the tracks to use.

    """

    def __init__(self):
        r"""
        :param _AudioPID: For streams containing multiple audio tracks, specify the audio track to use by entering a PID. The PID can be a positive integer between 1 and 8191.
        :type AudioPID: list of int
        :param _VideoPID: For streams containing multiple video tracks, specify the video track to be used by entering a PID. You can enter a positive integer between 1 and 8191 for the PID.
        :type VideoPID: list of int
        """
        self._AudioPID = None
        self._VideoPID = None

    @property
    def AudioPID(self):
        r"""For streams containing multiple audio tracks, specify the audio track to use by entering a PID. The PID can be a positive integer between 1 and 8191.
        :rtype: list of int
        """
        return self._AudioPID

    @AudioPID.setter
    def AudioPID(self, AudioPID):
        self._AudioPID = AudioPID

    @property
    def VideoPID(self):
        r"""For streams containing multiple video tracks, specify the video track to be used by entering a PID. You can enter a positive integer between 1 and 8191 for the PID.
        :rtype: list of int
        """
        return self._VideoPID

    @VideoPID.setter
    def VideoPID(self, VideoPID):
        self._VideoPID = VideoPID


    def _deserialize(self, params):
        self._AudioPID = params.get("AudioPID")
        self._VideoPID = params.get("VideoPID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTMPAddressDestination(AbstractModel):
    r"""Target address information for RTMP repush.

    """

    def __init__(self):
        r"""
        :param _Url: Destination Url for RTMP repush, in the format of 'RTMP://domain/live'.
        :type Url: str
        :param _StreamKey: Target StreamKey for RTMP republishing, in the format of 'steamid?key=value'.
        :type StreamKey: str
        """
        self._Url = None
        self._StreamKey = None

    @property
    def Url(self):
        r"""Destination Url for RTMP repush, in the format of 'RTMP://domain/live'.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StreamKey(self):
        r"""Target StreamKey for RTMP republishing, in the format of 'steamid?key=value'.
        :rtype: str
        """
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTMPPullSourceAddress(AbstractModel):
    r"""Configuration message of the created input RTMP pull source station.

    """

    def __init__(self):
        r"""
        :param _TcUrl: TcUrl of the RTMP origin server.
        :type TcUrl: str
        :param _StreamKey: StreamKey information of the RTMP origin server.
        :type StreamKey: str
        """
        self._TcUrl = None
        self._StreamKey = None

    @property
    def TcUrl(self):
        r"""TcUrl of the RTMP origin server.
        :rtype: str
        """
        return self._TcUrl

    @TcUrl.setter
    def TcUrl(self, TcUrl):
        self._TcUrl = TcUrl

    @property
    def StreamKey(self):
        r"""StreamKey information of the RTMP origin server.
        :rtype: str
        """
        return self._StreamKey

    @StreamKey.setter
    def StreamKey(self, StreamKey):
        self._StreamKey = StreamKey


    def _deserialize(self, params):
        self._TcUrl = params.get("TcUrl")
        self._StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTPAddressDestination(AbstractModel):
    r"""Target address information for RTP repush.

    """

    def __init__(self):
        r"""
        :param _Ip: IP of the destination address for repush.
        :type Ip: str
        :param _Port: Port of the destination address for push.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""IP of the destination address for repush.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Port of the destination address for push.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTSPPullSourceAddress(AbstractModel):
    r"""Configuration message of the created input RTSP pull source station.

    """

    def __init__(self):
        r"""
        :param _Url: Url of the RTSP origin server.
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        r"""Url of the RTSP origin server.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    r"""Region information.

    """

    def __init__(self):
        r"""
        :param _Name: Zone name.
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""Zone name.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResilientStreamConf(AbstractModel):
    r"""Configure smooth stream output for delayed playback.

    """

    def __init__(self):
        r"""
        :param _Enable: Whether to enable smooth delivery during delayed streaming. true: enable; false: disable. Not enabled by default.
        :type Enable: bool
        :param _BufferTime: Delay time in seconds, ranging from 10 to 300 for the time being.
        :type BufferTime: int
        """
        self._Enable = None
        self._BufferTime = None

    @property
    def Enable(self):
        r"""Whether to enable smooth delivery during delayed streaming. true: enable; false: disable. Not enabled by default.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def BufferTime(self):
        r"""Delay time in seconds, ranging from 10 to 300 for the time being.
        :rtype: int
        """
        return self._BufferTime

    @BufferTime.setter
    def BufferTime(self, BufferTime):
        self._BufferTime = BufferTime


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._BufferTime = params.get("BufferTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTAddressDestination(AbstractModel):
    r"""Target address information for repush.

    """

    def __init__(self):
        r"""
        :param _Ip: IP of the target address.
        :type Ip: str
        :param _Port: The port of the destination address.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""IP of the target address.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""The port of the destination address.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTFECFullOptions(AbstractModel):
    r"""SRT FEC advanced configuration

    """

    def __init__(self):
        r"""
        :param _Enable: Whether to enable FEC.
        :type Enable: bool
        :param _Cols: Number of FEC data packet Layout columns. Value range: >0
        :type Cols: int
        :param _Rows: Number of FEC data packet Layout rows. Value ranges from >=2 or <=-2.
        :type Rows: int
        :param _ARQ: ARQ policy when FEC is enabled. Value: "always", "onreq", "never".
        :type ARQ: str
        :param _Layout: FEC data packet Layout organization. Value: "even", "staircase"
        :type Layout: str
        """
        self._Enable = None
        self._Cols = None
        self._Rows = None
        self._ARQ = None
        self._Layout = None

    @property
    def Enable(self):
        r"""Whether to enable FEC.
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Cols(self):
        r"""Number of FEC data packet Layout columns. Value range: >0
        :rtype: int
        """
        return self._Cols

    @Cols.setter
    def Cols(self, Cols):
        self._Cols = Cols

    @property
    def Rows(self):
        r"""Number of FEC data packet Layout rows. Value ranges from >=2 or <=-2.
        :rtype: int
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def ARQ(self):
        r"""ARQ policy when FEC is enabled. Value: "always", "onreq", "never".
        :rtype: str
        """
        return self._ARQ

    @ARQ.setter
    def ARQ(self, ARQ):
        self._ARQ = ARQ

    @property
    def Layout(self):
        r"""FEC data packet Layout organization. Value: "even", "staircase"
        :rtype: str
        """
        return self._Layout

    @Layout.setter
    def Layout(self, Layout):
        self._Layout = Layout


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        self._Cols = params.get("Cols")
        self._Rows = params.get("Rows")
        self._ARQ = params.get("ARQ")
        self._Layout = params.get("Layout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTFECSimpleOptions(AbstractModel):
    r"""SRT FEC settings

    """

    def __init__(self):
        r"""
        :param _Enable: Whether FEC is enabled
        :type Enable: bool
        """
        self._Enable = None

    @property
    def Enable(self):
        r"""Whether FEC is enabled
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable


    def _deserialize(self, params):
        self._Enable = params.get("Enable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressReq(AbstractModel):
    r"""SRT input source address.

    """

    def __init__(self):
        r"""
        :param _Ip: Peer IP or domain
        :type Ip: str
        :param _Port: Peer port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""Peer IP or domain
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Peer port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressResp(AbstractModel):
    r"""SRT input source address.

    """

    def __init__(self):
        r"""
        :param _Ip: Peer IP.
        :type Ip: str
        :param _Port: Peer port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        r"""Peer IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        r"""Peer port.
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowRequest(AbstractModel):
    r"""StartStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Stream Id.</p>
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        r"""<p>Stream Id.</p>
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowResponse(AbstractModel):
    r"""StartStreamLinkFlow response structure.

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


class StopStreamLinkFlowRequest(AbstractModel):
    r"""StopStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: <p>Stream Id.</p>
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        r"""<p>Stream Id.</p>
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamLinkFlowResponse(AbstractModel):
    r"""StopStreamLinkFlow response structure.

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


class StreamLinkRegionInfo(AbstractModel):
    r"""Region information for media transmission.

    """

    def __init__(self):
        r"""
        :param _Regions: List of region information for media direct transmission.
        :type Regions: list of RegionInfo
        """
        self._Regions = None

    @property
    def Regions(self):
        r"""List of region information for media direct transmission.
        :rtype: list of RegionInfo
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamSelector(AbstractModel):
    r"""Select the specified audio track or video output

    """

    def __init__(self):
        r"""
        :param _SelectorType: Selection type: PID | TRACK
        :type SelectorType: str
        :param _PidSelector: Based on the PID configuration selector
        :type PidSelector: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        :param _TrackSelector: Select a selector based on the Track configuration
        :type TrackSelector: :class:`tencentcloud.mdc.v20200828.models.TrackSelector`
        """
        self._SelectorType = None
        self._PidSelector = None
        self._TrackSelector = None

    @property
    def SelectorType(self):
        r"""Selection type: PID | TRACK
        :rtype: str
        """
        return self._SelectorType

    @SelectorType.setter
    def SelectorType(self, SelectorType):
        self._SelectorType = SelectorType

    @property
    def PidSelector(self):
        r"""Based on the PID configuration selector
        :rtype: :class:`tencentcloud.mdc.v20200828.models.PidSelector`
        """
        return self._PidSelector

    @PidSelector.setter
    def PidSelector(self, PidSelector):
        self._PidSelector = PidSelector

    @property
    def TrackSelector(self):
        r"""Select a selector based on the Track configuration
        :rtype: :class:`tencentcloud.mdc.v20200828.models.TrackSelector`
        """
        return self._TrackSelector

    @TrackSelector.setter
    def TrackSelector(self, TrackSelector):
        self._TrackSelector = TrackSelector


    def _deserialize(self, params):
        self._SelectorType = params.get("SelectorType")
        if params.get("PidSelector") is not None:
            self._PidSelector = PidSelector()
            self._PidSelector._deserialize(params.get("PidSelector"))
        if params.get("TrackSelector") is not None:
            self._TrackSelector = TrackSelector()
            self._TrackSelector._deserialize(params.get("TrackSelector"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamUrlDetail(AbstractModel):
    r"""Description of the complete URL information

    """

    def __init__(self):
        r"""
        :param _Label: Describes carrier information and other details.
        :type Label: str
        :param _Url: URL 
        :type Url: str
        :param _Type: Playback: stream playback address;
RelayDestination: relay destination address; SourceCaptureUrl: source pull stream address; IngestEndpoint: streaming address
        :type Type: str
        """
        self._Label = None
        self._Url = None
        self._Type = None

    @property
    def Label(self):
        r"""Describes carrier information and other details.
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Url(self):
        r"""URL 
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Type(self):
        r"""Playback: stream playback address;
RelayDestination: relay destination address; SourceCaptureUrl: source pull stream address; IngestEndpoint: streaming address
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Url = params.get("Url")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrackSelector(AbstractModel):
    r"""Audio and video track selection

    """

    def __init__(self):
        r"""
        :param _VideoIndex: Video track serial number. It starts from 1. Maximum value: 32.
        :type VideoIndex: list of int
        :param _AudioIndex: Video track serial number. Starts from 1. Maximum value: 32.
        :type AudioIndex: list of int
        """
        self._VideoIndex = None
        self._AudioIndex = None

    @property
    def VideoIndex(self):
        r"""Video track serial number. It starts from 1. Maximum value: 32.
        :rtype: list of int
        """
        return self._VideoIndex

    @VideoIndex.setter
    def VideoIndex(self, VideoIndex):
        self._VideoIndex = VideoIndex

    @property
    def AudioIndex(self):
        r"""Video track serial number. Starts from 1. Maximum value: 32.
        :rtype: list of int
        """
        return self._AudioIndex

    @AudioIndex.setter
    def AudioIndex(self, AudioIndex):
        self._AudioIndex = AudioIndex


    def _deserialize(self, params):
        self._VideoIndex = params.get("VideoIndex")
        self._AudioIndex = params.get("AudioIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        