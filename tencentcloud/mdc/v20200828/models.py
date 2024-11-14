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


class CreateInput(AbstractModel):
    """Configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param _InputName: Input name, which can contain 1 to 32 letters, digits, and underscores.
        :type InputName: str
        :param _Protocol: Input protocol. Valid values: `SRT`, `RTP`, `RTMP`, `RTMP_PULL`, `RTSP_PULL `, `HLS_PULL`.
        :type Protocol: str
        :param _Description: Input description. Length: [0, 255].
        :type Description: str
        :param _AllowIpList: Allowlist of input IPs in CIDR format.
        :type AllowIpList: list of str
        :param _SRTSettings: SRT configuration information of input.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param _RTPSettings: RTP configuration information of input.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param _FailOver: Input failover. Valid values: `OPEN`, `CLOSE` (default)
        :type FailOver: str
        :param _RTMPPullSettings: Input RTMP_PULL configuration information.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        :param _RTSPPullSettings: Input RTSP_PULL configuration information.
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        :param _HLSPullSettings: Input HLS_PULL configuration information.
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        :param _ResilientStream: Delayed broadcast smooth streaming configuration information.
        :type ResilientStream: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        :param _SecurityGroupIds: The bound security group IDs.
        :type SecurityGroupIds: list of str
        :param _Zones: Availability zone, optional. If disaster recovery is enabled, you must enter two different availability zones. Otherwise, you can only enter one availability zone at most.
        :type Zones: list of str
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

    @property
    def InputName(self):
        """Input name, which can contain 1 to 32 letters, digits, and underscores.
        :rtype: str
        """
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Protocol(self):
        """Input protocol. Valid values: `SRT`, `RTP`, `RTMP`, `RTMP_PULL`, `RTSP_PULL `, `HLS_PULL`.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Description(self):
        """Input description. Length: [0, 255].
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AllowIpList(self):
        """Allowlist of input IPs in CIDR format.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        """SRT configuration information of input.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        """RTP configuration information of input.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def FailOver(self):
        """Input failover. Valid values: `OPEN`, `CLOSE` (default)
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def RTMPPullSettings(self):
        """Input RTMP_PULL configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def RTSPPullSettings(self):
        """Input RTSP_PULL configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        """Input HLS_PULL configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def ResilientStream(self):
        """Delayed broadcast smooth streaming configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        """
        return self._ResilientStream

    @ResilientStream.setter
    def ResilientStream(self, ResilientStream):
        self._ResilientStream = ResilientStream

    @property
    def SecurityGroupIds(self):
        """The bound security group IDs.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        """Availability zone, optional. If disaster recovery is enabled, you must enter two different availability zones. Otherwise, you can only enter one availability zone at most.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputHLSPullSettings(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: 
        :type SourceAddresses: list of HLSPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        """
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
        


class CreateInputRTMPPullSettings(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: 
        :type SourceAddresses: list of RTMPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        """
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
    """RTP configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param _FEC: Default value: none. Valid values: ['none'].
        :type FEC: str
        :param _IdleTimeout: Idle timeout period in ms. Default value: 5000. Value range: [1000, 10000].
        :type IdleTimeout: int
        """
        self._FEC = None
        self._IdleTimeout = None

    @property
    def FEC(self):
        """Default value: none. Valid values: ['none'].
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        """Idle timeout period in ms. Default value: 5000. Value range: [1000, 10000].
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
    """

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: 
        :type SourceAddresses: list of RTSPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        """
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
    """SRT configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param _Mode: The SRT mode. Valid values: LISTENER (default), CALLER.
        :type Mode: str
        :param _StreamId: Stream ID, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :type StreamId: str
        :param _Latency: Latency in ms. Default value: 0. Value range: [0, 3000].
        :type Latency: int
        :param _RecvLatency: Receive latency in ms. Default value: 120. Value range: [0, 3000].
        :type RecvLatency: int
        :param _PeerLatency: Peer latency in ms. Default value: 0. Value range: [0, 3000].
        :type PeerLatency: int
        :param _PeerIdleTimeout: Peer timeout period in ms. Default value: 5000. Value range: [1000, 10000].
        :type PeerIdleTimeout: int
        :param _Passphrase: Decryption key, which is empty by default, indicating not to encrypt. Only ASCII codes can be filled. Length: [10, 79].
        :type Passphrase: str
        :param _PbKeyLen: Key length. Default value: 0. Valid values: 0, 16, 24, 32.
        :type PbKeyLen: int
        :param _SourceAddresses: The SRT peer address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :type SourceAddresses: list of SRTSourceAddressReq
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

    @property
    def Mode(self):
        """The SRT mode. Valid values: LISTENER (default), CALLER.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StreamId(self):
        """Stream ID, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        """Latency in ms. Default value: 0. Value range: [0, 3000].
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        """Receive latency in ms. Default value: 120. Value range: [0, 3000].
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        """Peer latency in ms. Default value: 0. Value range: [0, 3000].
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        """Peer timeout period in ms. Default value: 5000. Value range: [1000, 10000].
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        """Decryption key, which is empty by default, indicating not to encrypt. Only ASCII codes can be filled. Length: [10, 79].
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        """Key length. Default value: 0. Valid values: 0, 16, 24, 32.
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def SourceAddresses(self):
        """The SRT peer address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :rtype: list of SRTSourceAddressReq
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfo(AbstractModel):
    """The information of the output to create.

    """

    def __init__(self):
        r"""
        :param _OutputName: The output name.
        :type OutputName: str
        :param _Description: Description of the output.
        :type Description: str
        :param _Protocol: The output protocol. Valid values: SRT, RTP, RTMP, RTMP_PULL.
        :type Protocol: str
        :param _OutputRegion: The output region.
        :type OutputRegion: str
        :param _SRTSettings: The SRT configuration.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param _RTMPSettings: The RTMP configuration.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param _RTPSettings: The RTP configuration.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param _AllowIpList: IP whitelist, in CIDR format, such as 0.0.0.0/0. This is valid when Protocol is RTMP_PULL, and empty means no restriction on client IP.
        :type AllowIpList: list of str
        :param _MaxConcurrent: The maximum number of concurrent stream pulls is 4, and the default value is 4.
        :type MaxConcurrent: int
        :param _SecurityGroupIds: The bound security group IDs.
        :type SecurityGroupIds: list of str
        :param _Zones: Availability zone: output supports at most one availability zone as input.
        :type Zones: list of str
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

    @property
    def OutputName(self):
        """The output name.
        :rtype: str
        """
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def Description(self):
        """Description of the output.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        """The output protocol. Valid values: SRT, RTP, RTMP, RTMP_PULL.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutputRegion(self):
        """The output region.
        :rtype: str
        """
        return self._OutputRegion

    @OutputRegion.setter
    def OutputRegion(self, OutputRegion):
        self._OutputRegion = OutputRegion

    @property
    def SRTSettings(self):
        """The SRT configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTMPSettings(self):
        """The RTMP configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def RTPSettings(self):
        """The RTP configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def AllowIpList(self):
        """IP whitelist, in CIDR format, such as 0.0.0.0/0. This is valid when Protocol is RTMP_PULL, and empty means no restriction on client IP.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def MaxConcurrent(self):
        """The maximum number of concurrent stream pulls is 4, and the default value is 4.
        :rtype: int
        """
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def SecurityGroupIds(self):
        """The bound security group IDs.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        """Availability zone: output supports at most one availability zone as input.
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfoRTPSettings(AbstractModel):
    """The RTP configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param _Destinations: The relay destination addresses. One or two addresses are allowed.
        :type Destinations: list of CreateOutputRTPSettingsDestinations
        :param _FEC: This parameter must be set to `none`.
        :type FEC: str
        :param _IdleTimeout: The timeout period (ms).
        :type IdleTimeout: int
        """
        self._Destinations = None
        self._FEC = None
        self._IdleTimeout = None

    @property
    def Destinations(self):
        """The relay destination addresses. One or two addresses are allowed.
        :rtype: list of CreateOutputRTPSettingsDestinations
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def FEC(self):
        """This parameter must be set to `none`.
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        """The timeout period (ms).
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
    """The RTMP configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param _Destinations: The relay destination addresses. One or two addresses are allowed.
        :type Destinations: list of CreateOutputRtmpSettingsDestinations
        :param _ChunkSize: The RTMP chunk size. Value range: [4096, 40960].
        :type ChunkSize: int
        """
        self._Destinations = None
        self._ChunkSize = None

    @property
    def Destinations(self):
        """The relay destination addresses. One or two addresses are allowed.
        :rtype: list of CreateOutputRtmpSettingsDestinations
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def ChunkSize(self):
        """The RTMP chunk size. Value range: [4096, 40960].
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
    """The RTP destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param _Ip: The relay destination IP.
        :type Ip: str
        :param _Port: The relay destination port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """The relay destination IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """The relay destination port.
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
        


class CreateOutputRtmpSettingsDestinations(AbstractModel):
    """The RTMP destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param _Url: The relay URL. Format: `rtmp://domain/live`.
        :type Url: str
        :param _StreamKey: The `StreamKey` for relay. Format: `stream?key=value`.
        :type StreamKey: str
        """
        self._Url = None
        self._StreamKey = None

    @property
    def Url(self):
        """The relay URL. Format: `rtmp://domain/live`.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StreamKey(self):
        """The `StreamKey` for relay. Format: `stream?key=value`.
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
    """The SRT configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param _Destinations: The relay destination address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :type Destinations: list of CreateOutputSrtSettingsDestinations
        :param _StreamId: The stream ID for relay, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :type StreamId: str
        :param _Latency: The total latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :type Latency: int
        :param _RecvLatency: The receive latency (ms) of SRT relay. Value range: [0, 3000]. Default: 120.
        :type RecvLatency: int
        :param _PeerLatency: The peer-to-peer latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :type PeerLatency: int
        :param _PeerIdleTimeout: The timeout period (ms) for the SRT relay peer. Value range: [1000, 10000]. Default: 5000.
        :type PeerIdleTimeout: int
        :param _Passphrase: The encryption key for SRT relay, which is empty by default, indicating not to encrypt. Only ASCII codes are allowed. Length: [10, 79].
        :type Passphrase: str
        :param _PbKeyLen: The key length for SRT relay. Valid values: 0 (default), 16, 24, 32.
        :type PbKeyLen: int
        :param _Mode: The SRT mode. Valid values: LISTENER, CALLER (default).
        :type Mode: str
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

    @property
    def Destinations(self):
        """The relay destination address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :rtype: list of CreateOutputSrtSettingsDestinations
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def StreamId(self):
        """The stream ID for relay, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        """The total latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        """The receive latency (ms) of SRT relay. Value range: [0, 3000]. Default: 120.
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        """The peer-to-peer latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        """The timeout period (ms) for the SRT relay peer. Value range: [1000, 10000]. Default: 5000.
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        """The encryption key for SRT relay, which is empty by default, indicating not to encrypt. Only ASCII codes are allowed. Length: [10, 79].
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        """The key length for SRT relay. Valid values: 0 (default), 16, 24, 32.
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def Mode(self):
        """The SRT mode. Valid values: LISTENER, CALLER (default).
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputSrtSettingsDestinations()
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettingsDestinations(AbstractModel):
    """The SRT destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param _Ip: The output IP.
        :type Ip: str
        :param _Port: The output port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """The output IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """The output port.
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
    """CreateStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowName: Flow name
        :type FlowName: str
        :param _MaxBandwidth: Maximum bandwidth in bps. Valid values: `10000000`, `20000000`, `50000000`
        :type MaxBandwidth: int
        :param _InputGroup: Flow input group
        :type InputGroup: list of CreateInput
        :param _EventId: The media transmission event ID associated with the Flow. Each flow can only be associated with one event.
        :type EventId: str
        """
        self._FlowName = None
        self._MaxBandwidth = None
        self._InputGroup = None
        self._EventId = None

    @property
    def FlowName(self):
        """Flow name
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def MaxBandwidth(self):
        """Maximum bandwidth in bps. Valid values: `10000000`, `20000000`, `50000000`
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def InputGroup(self):
        """Flow input group
        :rtype: list of CreateInput
        """
        return self._InputGroup

    @InputGroup.setter
    def InputGroup(self, InputGroup):
        self._InputGroup = InputGroup

    @property
    def EventId(self):
        """The media transmission event ID associated with the Flow. Each flow can only be associated with one event.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowResponse(AbstractModel):
    """CreateStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Information of the created flow
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Information of the created flow
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
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
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamLinkInputRequest(AbstractModel):
    """CreateStreamLinkInput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: StreamLink stream ID.
        :type FlowId: str
        :param _InputGroup: The input group of the Flow.
        :type InputGroup: list of CreateInput
        """
        self._FlowId = None
        self._InputGroup = None

    @property
    def FlowId(self):
        """StreamLink stream ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InputGroup(self):
        """The input group of the Flow.
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
    """CreateStreamLinkInput response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Created Flow information.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Created Flow information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
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
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class CreateStreamLinkOutputInfoRequest(AbstractModel):
    """CreateStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Output: The output configuration of the flow.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfo`
        """
        self._FlowId = None
        self._Output = None

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Output(self):
        """The output configuration of the flow.
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
    """CreateStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The information of the created output.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """The information of the created output.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
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
            self._Info = DescribeOutput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DeleteStreamLinkFlowRequest(AbstractModel):
    """DeleteStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """Flow ID
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
    """DeleteStreamLinkFlow response structure.

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


class DeleteStreamLinkOutputRequest(AbstractModel):
    """DeleteStreamLinkOutput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        :param _OutputId: Output ID
        :type OutputId: str
        """
        self._FlowId = None
        self._OutputId = None

    @property
    def FlowId(self):
        """Flow ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def OutputId(self):
        """Output ID
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
    """DeleteStreamLinkOutput response structure.

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


class DescribeFlow(AbstractModel):
    """Configuration information of the queried flow.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID.
        :type FlowId: str
        :param _FlowName: Flow name.
        :type FlowName: str
        :param _State: Flow status. Valid values: `IDLE`, `RUNNING`
        :type State: str
        :param _MaxBandwidth: Maximum bandwidth value.
        :type MaxBandwidth: int
        :param _InputGroup: Input group.
        :type InputGroup: list of DescribeInput
        :param _OutputGroup: Output group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutputGroup: list of DescribeOutput
        :param _EventId: EventId of the StreamLink event associated with this Flow.
        :type EventId: str
        """
        self._FlowId = None
        self._FlowName = None
        self._State = None
        self._MaxBandwidth = None
        self._InputGroup = None
        self._OutputGroup = None
        self._EventId = None

    @property
    def FlowId(self):
        """Flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        """Flow name.
        :rtype: str
        """
        return self._FlowName

    @FlowName.setter
    def FlowName(self, FlowName):
        self._FlowName = FlowName

    @property
    def State(self):
        """Flow status. Valid values: `IDLE`, `RUNNING`
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def MaxBandwidth(self):
        """Maximum bandwidth value.
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def InputGroup(self):
        """Input group.
        :rtype: list of DescribeInput
        """
        return self._InputGroup

    @InputGroup.setter
    def InputGroup(self, InputGroup):
        self._InputGroup = InputGroup

    @property
    def OutputGroup(self):
        """Output group.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of DescribeOutput
        """
        return self._OutputGroup

    @OutputGroup.setter
    def OutputGroup(self, OutputGroup):
        self._OutputGroup = OutputGroup

    @property
    def EventId(self):
        """EventId of the StreamLink event associated with this Flow.
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHLSPullSourceAddress(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Url: 
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """
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
    """Configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param _InputId: Input ID.
        :type InputId: str
        :param _InputName: Input name.
        :type InputName: str
        :param _Description: Input description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Protocol: Input protocol.
        :type Protocol: str
        :param _InputAddressList: Input address list.
        :type InputAddressList: list of InputAddress
        :param _AllowIpList: Input IP allowlist.
        :type AllowIpList: list of str
        :param _SRTSettings: SRT configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputSRTSettings`
        :param _RTPSettings: RTP configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTPSettings`
        :param _InputRegion: Input region.
        :type InputRegion: str
        :param _RTMPSettings: RTMP configuration information of an input
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPSettings`
        :param _FailOver: Input failover
Note: this field may return `null`, indicating that no valid value was found.
        :type FailOver: str
        :param _RTMPPullSettings: 
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPPullSettings`
        :param _RTSPPullSettings: 
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTSPPullSettings`
        :param _HLSPullSettings: 
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputHLSPullSettings`
        :param _ResilientStream: 
        :type ResilientStream: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        :param _SecurityGroupIds: The bound security group ID.
        :type SecurityGroupIds: list of str
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
        self._RTMPPullSettings = None
        self._RTSPPullSettings = None
        self._HLSPullSettings = None
        self._ResilientStream = None
        self._SecurityGroupIds = None

    @property
    def InputId(self):
        """Input ID.
        :rtype: str
        """
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def InputName(self):
        """Input name.
        :rtype: str
        """
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Description(self):
        """Input description.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        """Input protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InputAddressList(self):
        """Input address list.
        :rtype: list of InputAddress
        """
        return self._InputAddressList

    @InputAddressList.setter
    def InputAddressList(self, InputAddressList):
        self._InputAddressList = InputAddressList

    @property
    def AllowIpList(self):
        """Input IP allowlist.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        """SRT configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        """RTP configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def InputRegion(self):
        """Input region.
        :rtype: str
        """
        return self._InputRegion

    @InputRegion.setter
    def InputRegion(self, InputRegion):
        self._InputRegion = InputRegion

    @property
    def RTMPSettings(self):
        """RTMP configuration information of an input
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def FailOver(self):
        """Input failover
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def RTMPPullSettings(self):
        """
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def RTSPPullSettings(self):
        """
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        """
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def ResilientStream(self):
        """
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        """
        return self._ResilientStream

    @ResilientStream.setter
    def ResilientStream(self, ResilientStream):
        self._ResilientStream = ResilientStream

    @property
    def SecurityGroupIds(self):
        """The bound security group ID.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputHLSPullSettings(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: 
        :type SourceAddresses: list of DescribeHLSPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        """
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
        


class DescribeInputRTMPPullSettings(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: 
        :type SourceAddresses: list of DescribeRTMPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        """
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
    """RTMP configuration information of the queried input

    """

    def __init__(self):
        r"""
        :param _AppName: Path for RTMP stream pushing
Note: this field may return `null`, indicating that no valid value was found.
        :type AppName: str
        :param _StreamKey: StreamKey for RTMP stream pushing
Format of an RTMP stream pushing URL: rtmp://IP address:1935/AppName/StreamKey
        :type StreamKey: str
        """
        self._AppName = None
        self._StreamKey = None

    @property
    def AppName(self):
        """Path for RTMP stream pushing
Note: this field may return `null`, indicating that no valid value was found.
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamKey(self):
        """StreamKey for RTMP stream pushing
Format of an RTMP stream pushing URL: rtmp://IP address:1935/AppName/StreamKey
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
    """RTP configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param _FEC: Whether it is FEC.
        :type FEC: str
        :param _IdleTimeout: Idle timeout period.
        :type IdleTimeout: int
        """
        self._FEC = None
        self._IdleTimeout = None

    @property
    def FEC(self):
        """Whether it is FEC.
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        """Idle timeout period.
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
    """

    """

    def __init__(self):
        r"""
        :param _SourceAddresses: 
        :type SourceAddresses: list of DescribeRTSPPullSourceAddress
        """
        self._SourceAddresses = None

    @property
    def SourceAddresses(self):
        """
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
    """SRT configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param _Mode: The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param _StreamId: Stream ID.
        :type StreamId: str
        :param _Latency: Latency.
        :type Latency: int
        :param _RecvLatency: Receive latency.
        :type RecvLatency: int
        :param _PeerLatency: Peer latency.
        :type PeerLatency: int
        :param _PeerIdleTimeout: Peer idle timeout period.
        :type PeerIdleTimeout: int
        :param _Passphrase: Decryption key.
        :type Passphrase: str
        :param _PbKeyLen: Key length.
        :type PbKeyLen: int
        :param _SourceAddresses: The SRT peer address.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SourceAddresses: list of SRTSourceAddressResp
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

    @property
    def Mode(self):
        """The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StreamId(self):
        """Stream ID.
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        """Latency.
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        """Receive latency.
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        """Peer latency.
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        """Peer idle timeout period.
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        """Decryption key.
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        """Key length.
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def SourceAddresses(self):
        """The SRT peer address.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of SRTSourceAddressResp
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutput(AbstractModel):
    """Configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _OutputId: Output ID.
        :type OutputId: str
        :param _OutputName: Output name.
        :type OutputName: str
        :param _OutputType: Output type.
        :type OutputType: str
        :param _Description: Output description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param _Protocol: Output protocol.
        :type Protocol: str
        :param _OutputAddressList: Output destination address information list.
        :type OutputAddressList: list of OutputAddress
        :param _OutputRegion: Output region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutputRegion: str
        :param _SRTSettings: SRT configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputSRTSettings`
        :param _RTPSettings: RTP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTPSettings`
        :param _RTMPSettings: RTMP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPSettings`
        :param _RTMPPullSettings: RTMP pull configuration of the output
Note: This field may return `null`, indicating that no valid value was found.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPPullSettings`
        :param _AllowIpList: CIDR allowlist
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If this parameter is left empty, there is no restriction on clients’ IP addresses.
Note: This field may return `null`, indicating that no valid value was found.
        :type AllowIpList: list of str
        :param _RTSPPullSettings: 
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTSPPullSettings`
        :param _HLSPullSettings: 
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputHLSPullSettings`
        :param _MaxConcurrent: 
        :type MaxConcurrent: int
        :param _SecurityGroupIds: The bound security group IDs.
        :type SecurityGroupIds: list of str
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

    @property
    def OutputId(self):
        """Output ID.
        :rtype: str
        """
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def OutputName(self):
        """Output name.
        :rtype: str
        """
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def OutputType(self):
        """Output type.
        :rtype: str
        """
        return self._OutputType

    @OutputType.setter
    def OutputType(self, OutputType):
        self._OutputType = OutputType

    @property
    def Description(self):
        """Output description.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        """Output protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def OutputAddressList(self):
        """Output destination address information list.
        :rtype: list of OutputAddress
        """
        return self._OutputAddressList

    @OutputAddressList.setter
    def OutputAddressList(self, OutputAddressList):
        self._OutputAddressList = OutputAddressList

    @property
    def OutputRegion(self):
        """Output region.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OutputRegion

    @OutputRegion.setter
    def OutputRegion(self, OutputRegion):
        self._OutputRegion = OutputRegion

    @property
    def SRTSettings(self):
        """SRT configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        """RTP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def RTMPSettings(self):
        """RTMP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def RTMPPullSettings(self):
        """RTMP pull configuration of the output
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def AllowIpList(self):
        """CIDR allowlist
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If this parameter is left empty, there is no restriction on clients’ IP addresses.
Note: This field may return `null`, indicating that no valid value was found.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def RTSPPullSettings(self):
        """
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        """
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def MaxConcurrent(self):
        """
        :rtype: int
        """
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def SecurityGroupIds(self):
        """The bound security group IDs.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputHLSPullServerUrl(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Url: 
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """
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
    """

    """

    def __init__(self):
        r"""
        :param _ServerUrls: 
        :type ServerUrls: list of DescribeOutputHLSPullServerUrl
        """
        self._ServerUrls = None

    @property
    def ServerUrls(self):
        """
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
        


class DescribeOutputRTMPPullServerUrl(AbstractModel):
    """RTMP pull URL of the output

    """

    def __init__(self):
        r"""
        :param _TcUrl: `tcUrl` of the RTMP pull URL
        :type TcUrl: str
        :param _StreamKey: Stream key of the RTMP pull URL
        :type StreamKey: str
        """
        self._TcUrl = None
        self._StreamKey = None

    @property
    def TcUrl(self):
        """`tcUrl` of the RTMP pull URL
        :rtype: str
        """
        return self._TcUrl

    @TcUrl.setter
    def TcUrl(self, TcUrl):
        self._TcUrl = TcUrl

    @property
    def StreamKey(self):
        """Stream key of the RTMP pull URL
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
    """RTMP pull configuration of the output

    """

    def __init__(self):
        r"""
        :param _ServerUrls: List of pull URLs
Note: This field may return `null`, indicating that no valid value was found.
        :type ServerUrls: list of DescribeOutputRTMPPullServerUrl
        """
        self._ServerUrls = None

    @property
    def ServerUrls(self):
        """List of pull URLs
Note: This field may return `null`, indicating that no valid value was found.
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
    """RTMP configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdleTimeout: int
        :param _ChunkSize: Chunk size.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChunkSize: int
        :param _Destinations: Destination address information list of RTMP push.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of RTMPAddressDestination
        """
        self._IdleTimeout = None
        self._ChunkSize = None
        self._Destinations = None

    @property
    def IdleTimeout(self):
        """Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ChunkSize(self):
        """Chunk size.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._ChunkSize

    @ChunkSize.setter
    def ChunkSize(self, ChunkSize):
        self._ChunkSize = ChunkSize

    @property
    def Destinations(self):
        """Destination address information list of RTMP push.
Note: this field may return null, indicating that no valid values can be obtained.
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
    """RTP configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _Destinations: Destination address information list of RTP push.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of RTPAddressDestination
        :param _FEC: Whether it is FEC.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FEC: str
        :param _IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdleTimeout: int
        """
        self._Destinations = None
        self._FEC = None
        self._IdleTimeout = None

    @property
    def Destinations(self):
        """Destination address information list of RTP push.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of RTPAddressDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def FEC(self):
        """Whether it is FEC.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FEC

    @FEC.setter
    def FEC(self, FEC):
        self._FEC = FEC

    @property
    def IdleTimeout(self):
        """Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
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
    """

    """

    def __init__(self):
        r"""
        :param _Url: 
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """
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
    """

    """

    def __init__(self):
        r"""
        :param _ServerUrls: 
        :type ServerUrls: list of DescribeOutputRTSPPullServerUrl
        """
        self._ServerUrls = None

    @property
    def ServerUrls(self):
        """
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
    """SRT configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param _Destinations: A list of the destination addresses for relay. This parameter is valid if `Mode` is `CALLER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Destinations: list of SRTAddressDestination
        :param _StreamId: Stream ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamId: str
        :param _Latency: Latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Latency: int
        :param _RecvLatency: Receive latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RecvLatency: int
        :param _PeerLatency: Peer latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeerLatency: int
        :param _PeerIdleTimeout: Peer idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeerIdleTimeout: int
        :param _Passphrase: Encryption key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Passphrase: str
        :param _PbKeyLen: Encryption key length.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PbKeyLen: int
        :param _Mode: The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param _SourceAddresses: The server’s listen address, which is valid if `Mode` is `LISTENER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SourceAddresses: list of OutputSRTSourceAddressResp
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

    @property
    def Destinations(self):
        """A list of the destination addresses for relay. This parameter is valid if `Mode` is `CALLER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of SRTAddressDestination
        """
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def StreamId(self):
        """Stream ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._StreamId

    @StreamId.setter
    def StreamId(self, StreamId):
        self._StreamId = StreamId

    @property
    def Latency(self):
        """Latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RecvLatency(self):
        """Receive latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RecvLatency

    @RecvLatency.setter
    def RecvLatency(self, RecvLatency):
        self._RecvLatency = RecvLatency

    @property
    def PeerLatency(self):
        """Peer latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PeerLatency

    @PeerLatency.setter
    def PeerLatency(self, PeerLatency):
        self._PeerLatency = PeerLatency

    @property
    def PeerIdleTimeout(self):
        """Peer idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PeerIdleTimeout

    @PeerIdleTimeout.setter
    def PeerIdleTimeout(self, PeerIdleTimeout):
        self._PeerIdleTimeout = PeerIdleTimeout

    @property
    def Passphrase(self):
        """Encryption key.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase):
        self._Passphrase = Passphrase

    @property
    def PbKeyLen(self):
        """Encryption key length.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._PbKeyLen

    @PbKeyLen.setter
    def PbKeyLen(self, PbKeyLen):
        self._PbKeyLen = PbKeyLen

    @property
    def Mode(self):
        """The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SourceAddresses(self):
        """The server’s listen address, which is valid if `Mode` is `LISTENER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of OutputSRTSourceAddressResp
        """
        return self._SourceAddresses

    @SourceAddresses.setter
    def SourceAddresses(self, SourceAddresses):
        self._SourceAddresses = SourceAddresses


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRTMPPullSourceAddress(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _TcUrl: 
        :type TcUrl: str
        :param _StreamKey: 
        :type StreamKey: str
        """
        self._TcUrl = None
        self._StreamKey = None

    @property
    def TcUrl(self):
        """
        :rtype: str
        """
        return self._TcUrl

    @TcUrl.setter
    def TcUrl(self, TcUrl):
        self._TcUrl = TcUrl

    @property
    def StreamKey(self):
        """
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
    """

    """

    def __init__(self):
        r"""
        :param _Url: 
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """
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
    """DescribeStreamLinkFlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: list of str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: list of str
        :param _PageSize: The page size. Value range: [1, 1000]. Default: 100.
        :type PageSize: int
        :param _SortType: Whether to sort the records by timestamp in descending or ascending order. Valid values: desc (default), asc.
        :type SortType: str
        :param _PageNum: The page number. Value range: [1, 1000]. Default: 1.
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
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def StartTime(self):
        """The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Type(self):
        """Whether to query the inputs or outputs. Valid values: input, output.
        :rtype: list of str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pipeline(self):
        """Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :rtype: list of str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def PageSize(self):
        """The page size. Value range: [1, 1000]. Default: 100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def SortType(self):
        """Whether to sort the records by timestamp in descending or ascending order. Valid values: desc (default), asc.
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def PageNum(self):
        """The page number. Value range: [1, 1000]. Default: 1.
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
    """DescribeStreamLinkFlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the logs.
        :type Infos: list of FlowLogInfo
        :param _PageNum: The current page number.
        :type PageNum: int
        :param _PageSize: The number of records per page.
        :type PageSize: int
        :param _TotalNum: The total number of records.
        :type TotalNum: int
        :param _TotalPage: The total number of pages.
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
        """A list of the logs.
        :rtype: list of FlowLogInfo
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """The current page number.
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """The number of records per page.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        """The total number of records.
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        """The total number of pages.
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
                obj = FlowLogInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowMediaStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param _Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        """Whether to query the inputs or outputs. Valid values: input, output.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        """The input or output ID.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        """Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def Period(self):
        """The query interval. Valid values: 5s, 1min, 5min, 15min.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowMediaStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the media data.
        :type Infos: list of FlowMediaInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        """A list of the media data.
        :rtype: list of FlowMediaInfo
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
                obj = FlowMediaInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRealtimeStatusRequest(AbstractModel):
    """DescribeStreamLinkFlowRealtimeStatus request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _InputIds: The IDs of the inputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
        :type InputIds: list of str
        :param _OutputIds: The IDs of the outputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
        :type OutputIds: list of str
        """
        self._FlowId = None
        self._InputIds = None
        self._OutputIds = None

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def InputIds(self):
        """The IDs of the inputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
        :rtype: list of str
        """
        return self._InputIds

    @InputIds.setter
    def InputIds(self, InputIds):
        self._InputIds = InputIds

    @property
    def OutputIds(self):
        """The IDs of the outputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
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
    """DescribeStreamLinkFlowRealtimeStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds) of the query.
        :type Timestamp: int
        :param _Datas: A list of the real-time data.
        :type Datas: list of FlowRealtimeStatusItem
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Timestamp = None
        self._Datas = None
        self._RequestId = None

    @property
    def Timestamp(self):
        """The timestamp (seconds) of the query.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Datas(self):
        """A list of the real-time data.
        :rtype: list of FlowRealtimeStatusItem
        """
        return self._Datas

    @Datas.setter
    def Datas(self, Datas):
        self._Datas = Datas

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
        self._Timestamp = params.get("Timestamp")
        if params.get("Datas") is not None:
            self._Datas = []
            for item in params.get("Datas"):
                obj = FlowRealtimeStatusItem()
                obj._deserialize(item)
                self._Datas.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRequest(AbstractModel):
    """DescribeStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """Flow ID
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
    """DescribeStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Configuration information of a flow
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """Configuration information of a flow
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
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
            self._Info = DescribeFlow()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowSRTStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param _Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        """Whether to query the inputs or outputs. Valid values: input, output.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        """The input or output ID.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        """Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def StartTime(self):
        """The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """The query interval. Valid values: 5s, 1min, 5min, 15min.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowSRTStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the SRT streaming performance data.
        :type Infos: list of FlowSRTInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        """A list of the SRT streaming performance data.
        :rtype: list of FlowSRTInfo
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
                obj = FlowSRTInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param _Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        :param _StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param _EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        """
        self._FlowId = None
        self._Type = None
        self._InputOutputId = None
        self._Pipeline = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Type(self):
        """Whether to query the inputs or outputs. Valid values: input, output.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        """The input or output ID.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Pipeline(self):
        """Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def Period(self):
        """The query interval. Valid values: 5s, 1min, 5min, 15min.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._FlowId = params.get("FlowId")
        self._Type = params.get("Type")
        self._InputOutputId = params.get("InputOutputId")
        self._Pipeline = params.get("Pipeline")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the media data.
        :type Infos: list of FlowStatisticsArray
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        """A list of the media data.
        :rtype: list of FlowStatisticsArray
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
                obj = FlowStatisticsArray()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkFlowsRequest(AbstractModel):
    """DescribeStreamLinkFlows request structure.

    """

    def __init__(self):
        r"""
        :param _PageNum: Number of the current page. Default value: `1`
        :type PageNum: int
        :param _PageSize: Number of entries per page. Default value: `10`
        :type PageSize: int
        """
        self._PageNum = None
        self._PageSize = None

    @property
    def PageNum(self):
        """Number of the current page. Default value: `1`
        :rtype: int
        """
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        """Number of entries per page. Default value: `10`
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
    """DescribeStreamLinkFlows response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of the configuration information of the flows
        :type Infos: list of DescribeFlow
        :param _PageNum: Number of the current page
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
        """List of the configuration information of the flows
        :rtype: list of DescribeFlow
        """
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        """Number of the current page
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
                obj = DescribeFlow()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamLinkRegionsRequest(AbstractModel):
    """DescribeStreamLinkRegions request structure.

    """


class DescribeStreamLinkRegionsResponse(AbstractModel):
    """DescribeStreamLinkRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Info: StreamLink region information
        :type Info: :class:`tencentcloud.mdc.v20200828.models.StreamLinkRegionInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """StreamLink region information
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StreamLinkRegionInfo`
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
            self._Info = StreamLinkRegionInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class FlowAudio(AbstractModel):
    """The audio data of the flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The audio PID.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        """The frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        """The bitrate (bps).
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        """The audio PID.
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
    """The logs of a flow.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param _Type: Whether it is an input or output.
        :type Type: str
        :param _InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param _Protocol: The protocol.
        :type Protocol: str
        :param _EventCode: The event code.
        :type EventCode: str
        :param _EventMessage: The event information.
        :type EventMessage: str
        :param _RemoteIp: The peer IP.
        :type RemoteIp: str
        :param _RemotePort: The peer port.
        :type RemotePort: str
        :param _Pipeline: Whether it is a primary or backup pipeline. Valid values: 0 (primary), 1 (backup).
        :type Pipeline: str
        :param _InputOutputName: The input or output name.
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
        """The timestamp (seconds).
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Type(self):
        """Whether it is an input or output.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputOutputId(self):
        """The input or output ID.
        :rtype: str
        """
        return self._InputOutputId

    @InputOutputId.setter
    def InputOutputId(self, InputOutputId):
        self._InputOutputId = InputOutputId

    @property
    def Protocol(self):
        """The protocol.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def EventCode(self):
        """The event code.
        :rtype: str
        """
        return self._EventCode

    @EventCode.setter
    def EventCode(self, EventCode):
        self._EventCode = EventCode

    @property
    def EventMessage(self):
        """The event information.
        :rtype: str
        """
        return self._EventMessage

    @EventMessage.setter
    def EventMessage(self, EventMessage):
        self._EventMessage = EventMessage

    @property
    def RemoteIp(self):
        """The peer IP.
        :rtype: str
        """
        return self._RemoteIp

    @RemoteIp.setter
    def RemoteIp(self, RemoteIp):
        self._RemoteIp = RemoteIp

    @property
    def RemotePort(self):
        """The peer port.
        :rtype: str
        """
        return self._RemotePort

    @RemotePort.setter
    def RemotePort(self, RemotePort):
        self._RemotePort = RemotePort

    @property
    def Pipeline(self):
        """Whether it is a primary or backup pipeline. Valid values: 0 (primary), 1 (backup).
        :rtype: str
        """
        return self._Pipeline

    @Pipeline.setter
    def Pipeline(self, Pipeline):
        self._Pipeline = Pipeline

    @property
    def InputOutputName(self):
        """The input or output name.
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
    """The audio data of a flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The audio PID.
        :type Pid: int
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None
        self._SessionId = None

    @property
    def Fps(self):
        """The frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        """The bitrate (bps).
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        """The audio PID.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def SessionId(self):
        """The ID of a push session.
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
    """The media data of a flow.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param _Network: The total bandwidth.
        :type Network: int
        :param _Video: The video data of the flow.
        :type Video: list of FlowMediaVideo
        :param _Audio: The audio data of the flow.
        :type Audio: list of FlowMediaAudio
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        :param _ClientIp: The client IP.
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
        """The timestamp (seconds).
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Network(self):
        """The total bandwidth.
        :rtype: int
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Video(self):
        """The video data of the flow.
        :rtype: list of FlowMediaVideo
        """
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        """The audio data of the flow.
        :rtype: list of FlowMediaAudio
        """
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def SessionId(self):
        """The ID of a push session.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ClientIp(self):
        """The client IP.
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
    """The video data of a flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The video PID.
        :type Pid: int
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None
        self._SessionId = None

    @property
    def Fps(self):
        """The frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        """The bitrate (bps).
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        """The video PID.
        :rtype: int
        """
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def SessionId(self):
        """The ID of a push session.
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
    """The common real-time status information of a flow.

    """

    def __init__(self):
        r"""
        :param _State: The connection status. Valid values: Connected, Waiting, Idle.
        :type State: str
        :param _Mode: The connection mode. Valid values: Listener, Caller.
        :type Mode: str
        :param _ConnectedTime: The connected time.
        :type ConnectedTime: int
        :param _Bitrate: The real-time bitrate (bps).
        :type Bitrate: int
        :param _Reconnections: The number of retries.
        :type Reconnections: int
        """
        self._State = None
        self._Mode = None
        self._ConnectedTime = None
        self._Bitrate = None
        self._Reconnections = None

    @property
    def State(self):
        """The connection status. Valid values: Connected, Waiting, Idle.
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Mode(self):
        """The connection mode. Valid values: Listener, Caller.
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ConnectedTime(self):
        """The connected time.
        :rtype: int
        """
        return self._ConnectedTime

    @ConnectedTime.setter
    def ConnectedTime(self, ConnectedTime):
        self._ConnectedTime = ConnectedTime

    @property
    def Bitrate(self):
        """The real-time bitrate (bps).
        :rtype: int
        """
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Reconnections(self):
        """The number of retries.
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
    """The real-time status information of a flow.

    """

    def __init__(self):
        r"""
        :param _Type: Whether it is an input or output. Valid values: Input, Output.
        :type Type: str
        :param _InputId: The input ID, which is not empty if `Type` is `Input`.
        :type InputId: str
        :param _OutputId: The output ID, which is not empty if `Type` is `Output`.
        :type OutputId: str
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Protocol: The protocol used. Valid values: SRT, RTP, RTMP.
        :type Protocol: str
        :param _CommonStatus: The common status information.
        :type CommonStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusCommon`
        :param _SRTStatus: This parameter is returned if `Protocol` is `SRT`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SRTStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusSRT`
        :param _RTMPStatus: This parameter is returned if `Protocol` is `RTMP`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RTMPStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTMP`
        :param _ConnectServerIP: The server IP.
        :type ConnectServerIP: str
        :param _RTPStatus: This parameter is returned if the RTP protocol is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
        """Whether it is an input or output. Valid values: Input, Output.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InputId(self):
        """The input ID, which is not empty if `Type` is `Input`.
        :rtype: str
        """
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def OutputId(self):
        """The output ID, which is not empty if `Type` is `Output`.
        :rtype: str
        """
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Protocol(self):
        """The protocol used. Valid values: SRT, RTP, RTMP.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CommonStatus(self):
        """The common status information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusCommon`
        """
        return self._CommonStatus

    @CommonStatus.setter
    def CommonStatus(self, CommonStatus):
        self._CommonStatus = CommonStatus

    @property
    def SRTStatus(self):
        """This parameter is returned if `Protocol` is `SRT`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusSRT`
        """
        return self._SRTStatus

    @SRTStatus.setter
    def SRTStatus(self, SRTStatus):
        self._SRTStatus = SRTStatus

    @property
    def RTMPStatus(self):
        """This parameter is returned if `Protocol` is `RTMP`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTMP`
        """
        return self._RTMPStatus

    @RTMPStatus.setter
    def RTMPStatus(self, RTMPStatus):
        self._RTMPStatus = RTMPStatus

    @property
    def ConnectServerIP(self):
        """The server IP.
        :rtype: str
        """
        return self._ConnectServerIP

    @ConnectServerIP.setter
    def ConnectServerIP(self, ConnectServerIP):
        self._ConnectServerIP = ConnectServerIP

    @property
    def RTPStatus(self):
        """This parameter is returned if the RTP protocol is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
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
    """The real-time RTMP streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param _VideoFPS: The video frame rate.
        :type VideoFPS: int
        :param _AudioFPS: The audio frame rate.
        :type AudioFPS: int
        """
        self._VideoFPS = None
        self._AudioFPS = None

    @property
    def VideoFPS(self):
        """The video frame rate.
        :rtype: int
        """
        return self._VideoFPS

    @VideoFPS.setter
    def VideoFPS(self, VideoFPS):
        self._VideoFPS = VideoFPS

    @property
    def AudioFPS(self):
        """The audio frame rate.
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
    """The real-time RTP streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param _Packets: The number of packets transmitted.
        :type Packets: int
        """
        self._Packets = None

    @property
    def Packets(self):
        """The number of packets transmitted.
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
    """The real-time SRT streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param _Latency: The latency (ms).
        :type Latency: int
        :param _RTT: RTT (ms).
        :type RTT: int
        :param _Packets: The number of packets sent or received.
        :type Packets: int
        :param _PacketLossRate: The packet loss rate.
        :type PacketLossRate: float
        :param _RetransmitRate: The retransmission rate.
        :type RetransmitRate: float
        :param _DroppedPackets: The number of packets dropped.
        :type DroppedPackets: int
        :param _Encryption: Whether to encrypt the stream. Valid values: On, Off.
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
        """The latency (ms).
        :rtype: int
        """
        return self._Latency

    @Latency.setter
    def Latency(self, Latency):
        self._Latency = Latency

    @property
    def RTT(self):
        """RTT (ms).
        :rtype: int
        """
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def Packets(self):
        """The number of packets sent or received.
        :rtype: int
        """
        return self._Packets

    @Packets.setter
    def Packets(self, Packets):
        self._Packets = Packets

    @property
    def PacketLossRate(self):
        """The packet loss rate.
        :rtype: float
        """
        return self._PacketLossRate

    @PacketLossRate.setter
    def PacketLossRate(self, PacketLossRate):
        self._PacketLossRate = PacketLossRate

    @property
    def RetransmitRate(self):
        """The retransmission rate.
        :rtype: float
        """
        return self._RetransmitRate

    @RetransmitRate.setter
    def RetransmitRate(self, RetransmitRate):
        self._RetransmitRate = RetransmitRate

    @property
    def DroppedPackets(self):
        """The number of packets dropped.
        :rtype: int
        """
        return self._DroppedPackets

    @DroppedPackets.setter
    def DroppedPackets(self, DroppedPackets):
        self._DroppedPackets = DroppedPackets

    @property
    def Encryption(self):
        """Whether to encrypt the stream. Valid values: On, Off.
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
    """The SRT streaming performance data.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param _SendPacketLossRate: The packet loss rate for sending.
        :type SendPacketLossRate: int
        :param _SendRetransmissionRate: The retry rate for sending.
        :type SendRetransmissionRate: int
        :param _RecvPacketLossRate: The packet loss rate for receiving.
        :type RecvPacketLossRate: int
        :param _RecvRetransmissionRate: The retry rate for receiving.
        :type RecvRetransmissionRate: int
        :param _RTT: The peer RTT.
        :type RTT: int
        :param _SessionId: The ID of a push session.
        :type SessionId: str
        :param _SendPacketDropNumber: The number of dropped packets for sending.
        :type SendPacketDropNumber: int
        :param _RecvPacketDropNumber: The number of dropped packets for receiving.
        :type RecvPacketDropNumber: int
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

    @property
    def Timestamp(self):
        """The timestamp (seconds).
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def SendPacketLossRate(self):
        """The packet loss rate for sending.
        :rtype: int
        """
        return self._SendPacketLossRate

    @SendPacketLossRate.setter
    def SendPacketLossRate(self, SendPacketLossRate):
        self._SendPacketLossRate = SendPacketLossRate

    @property
    def SendRetransmissionRate(self):
        """The retry rate for sending.
        :rtype: int
        """
        return self._SendRetransmissionRate

    @SendRetransmissionRate.setter
    def SendRetransmissionRate(self, SendRetransmissionRate):
        self._SendRetransmissionRate = SendRetransmissionRate

    @property
    def RecvPacketLossRate(self):
        """The packet loss rate for receiving.
        :rtype: int
        """
        return self._RecvPacketLossRate

    @RecvPacketLossRate.setter
    def RecvPacketLossRate(self, RecvPacketLossRate):
        self._RecvPacketLossRate = RecvPacketLossRate

    @property
    def RecvRetransmissionRate(self):
        """The retry rate for receiving.
        :rtype: int
        """
        return self._RecvRetransmissionRate

    @RecvRetransmissionRate.setter
    def RecvRetransmissionRate(self, RecvRetransmissionRate):
        self._RecvRetransmissionRate = RecvRetransmissionRate

    @property
    def RTT(self):
        """The peer RTT.
        :rtype: int
        """
        return self._RTT

    @RTT.setter
    def RTT(self, RTT):
        self._RTT = RTT

    @property
    def SessionId(self):
        """The ID of a push session.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SendPacketDropNumber(self):
        """The number of dropped packets for sending.
        :rtype: int
        """
        return self._SendPacketDropNumber

    @SendPacketDropNumber.setter
    def SendPacketDropNumber(self, SendPacketDropNumber):
        self._SendPacketDropNumber = SendPacketDropNumber

    @property
    def RecvPacketDropNumber(self):
        """The number of dropped packets for receiving.
        :rtype: int
        """
        return self._RecvPacketDropNumber

    @RecvPacketDropNumber.setter
    def RecvPacketDropNumber(self, RecvPacketDropNumber):
        self._RecvPacketDropNumber = RecvPacketDropNumber


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatistics(AbstractModel):
    """The flow statistics.

    """

    def __init__(self):
        r"""
        :param _SessionId: The session ID.
        :type SessionId: str
        :param _ClientIp: The peer IP.
        :type ClientIp: str
        :param _Network: The total bandwidth.
        :type Network: int
        :param _Video: The video data.
        :type Video: list of FlowVideo
        :param _Audio: The audio data.
        :type Audio: list of FlowAudio
        """
        self._SessionId = None
        self._ClientIp = None
        self._Network = None
        self._Video = None
        self._Audio = None

    @property
    def SessionId(self):
        """The session ID.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def ClientIp(self):
        """The peer IP.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Network(self):
        """The total bandwidth.
        :rtype: int
        """
        return self._Network

    @Network.setter
    def Network(self, Network):
        self._Network = Network

    @property
    def Video(self):
        """The video data.
        :rtype: list of FlowVideo
        """
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        """The audio data.
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
    """A list of the flow statistics.

    """

    def __init__(self):
        r"""
        :param _Timestamp: The timestamp.
        :type Timestamp: int
        :param _FlowStatistics: The statistics of all the sessions.
        :type FlowStatistics: list of FlowStatistics
        """
        self._Timestamp = None
        self._FlowStatistics = None

    @property
    def Timestamp(self):
        """The timestamp.
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def FlowStatistics(self):
        """The statistics of all the sessions.
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
    """The video data of a flow.

    """

    def __init__(self):
        r"""
        :param _Fps: The frame rate.
        :type Fps: int
        :param _Rate: The bitrate (bps).
        :type Rate: int
        :param _Pid: The audio PID.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        """The frame rate.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        """The bitrate (bps).
        :rtype: int
        """
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        """The audio PID.
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
    """

    """

    def __init__(self):
        r"""
        :param _Url: 
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """
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
    """Input address information.

    """

    def __init__(self):
        r"""
        :param _Ip: Input address IP.
        :type Ip: str
        :param _Port: Input address port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """Input address IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Input address port.
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
    """The new input configuration.

    """

    def __init__(self):
        r"""
        :param _InputId: The input ID.
        :type InputId: str
        :param _InputName: The input name.
        :type InputName: str
        :param _Description: The description of the input.
        :type Description: str
        :param _AllowIpList: The IP addresses (CIDR) allowed to push streams.
        :type AllowIpList: list of str
        :param _SRTSettings: The SRT configuration information.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param _RTPSettings: The RTP configuration information.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param _Protocol: The input protocol. Valid values: SRT, RTP, RTMP.
If there is an RTP input, the output must be RTP.
If there is an RTMP input, the output must be SRT or RTMP.
If there is an SRT input, the output must be SRT.
        :type Protocol: str
        :param _FailOver: Whether to enable input failover. Valid values: OPEN, CLOSE.
        :type FailOver: str
        :param _RTMPPullSettings: Configuration information for RTMP_PULL.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        :param _RTSPPullSettings: Configuration information of RTSP_PULL.
        :type RTSPPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        :param _HLSPullSettings: HLS_PULL configuration information.
        :type HLSPullSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        :param _ResilientStream: Delayed broadcast smooth streaming configuration information.
        :type ResilientStream: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        :param _SecurityGroupIds: The ID of the input security group to bind. Only one security group can be associated.
        :type SecurityGroupIds: list of str
        :param _Zones: Availability zone, optional, supports up to two availability zones. For interfaces that need to be changed, the second availability zone will participate in resource allocation. This is effective if disaster recovery is enabled for input or RTSP_PULL protocol switching is involved (addresses will be reallocated).
        :type Zones: list of str
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

    @property
    def InputId(self):
        """The input ID.
        :rtype: str
        """
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def InputName(self):
        """The input name.
        :rtype: str
        """
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Description(self):
        """The description of the input.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AllowIpList(self):
        """The IP addresses (CIDR) allowed to push streams.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def SRTSettings(self):
        """The SRT configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        """The RTP configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def Protocol(self):
        """The input protocol. Valid values: SRT, RTP, RTMP.
If there is an RTP input, the output must be RTP.
If there is an RTMP input, the output must be SRT or RTMP.
If there is an SRT input, the output must be SRT.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def FailOver(self):
        """Whether to enable input failover. Valid values: OPEN, CLOSE.
        :rtype: str
        """
        return self._FailOver

    @FailOver.setter
    def FailOver(self, FailOver):
        self._FailOver = FailOver

    @property
    def RTMPPullSettings(self):
        """Configuration information for RTMP_PULL.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTMPPullSettings`
        """
        return self._RTMPPullSettings

    @RTMPPullSettings.setter
    def RTMPPullSettings(self, RTMPPullSettings):
        self._RTMPPullSettings = RTMPPullSettings

    @property
    def RTSPPullSettings(self):
        """Configuration information of RTSP_PULL.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTSPPullSettings`
        """
        return self._RTSPPullSettings

    @RTSPPullSettings.setter
    def RTSPPullSettings(self, RTSPPullSettings):
        self._RTSPPullSettings = RTSPPullSettings

    @property
    def HLSPullSettings(self):
        """HLS_PULL configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateInputHLSPullSettings`
        """
        return self._HLSPullSettings

    @HLSPullSettings.setter
    def HLSPullSettings(self, HLSPullSettings):
        self._HLSPullSettings = HLSPullSettings

    @property
    def ResilientStream(self):
        """Delayed broadcast smooth streaming configuration information.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ResilientStreamConf`
        """
        return self._ResilientStream

    @ResilientStream.setter
    def ResilientStream(self, ResilientStream):
        self._ResilientStream = ResilientStream

    @property
    def SecurityGroupIds(self):
        """The ID of the input security group to bind. Only one security group can be associated.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Zones(self):
        """Availability zone, optional, supports up to two availability zones. For interfaces that need to be changed, the second availability zone will participate in resource allocation. This is effective if disaster recovery is enabled for input or RTSP_PULL protocol switching is involved (addresses will be reallocated).
        :rtype: list of str
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOutputInfo(AbstractModel):
    """The new output configuration.

    """

    def __init__(self):
        r"""
        :param _OutputId: The ID of the output to modify.
        :type OutputId: str
        :param _OutputName: The output name.
        :type OutputName: str
        :param _Description: The description of the output.
        :type Description: str
        :param _Protocol: The output protocol. Valid values: SRT, RTP, RTMP.
        :type Protocol: str
        :param _SRTSettings: The SRT relay configuration.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param _RTPSettings: The RTP relay configuration.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param _RTMPSettings: The RTMP relay configuration.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param _AllowIpList: IP whitelist, in CIDR format, such as 0.0.0.0/0. This is valid when Protocol is RTMP_PULL, and empty means no restriction on client IP.
        :type AllowIpList: list of str
        :param _MaxConcurrent: The maximum number of concurrent stream pulls is 4, and the default value is 4.
        :type MaxConcurrent: int
        :param _SecurityGroupIds: The bound security group IDs.
        :type SecurityGroupIds: list of str
        """
        self._OutputId = None
        self._OutputName = None
        self._Description = None
        self._Protocol = None
        self._SRTSettings = None
        self._RTPSettings = None
        self._RTMPSettings = None
        self._AllowIpList = None
        self._MaxConcurrent = None
        self._SecurityGroupIds = None

    @property
    def OutputId(self):
        """The ID of the output to modify.
        :rtype: str
        """
        return self._OutputId

    @OutputId.setter
    def OutputId(self, OutputId):
        self._OutputId = OutputId

    @property
    def OutputName(self):
        """The output name.
        :rtype: str
        """
        return self._OutputName

    @OutputName.setter
    def OutputName(self, OutputName):
        self._OutputName = OutputName

    @property
    def Description(self):
        """The description of the output.
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        """The output protocol. Valid values: SRT, RTP, RTMP.
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SRTSettings(self):
        """The SRT relay configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        """
        return self._SRTSettings

    @SRTSettings.setter
    def SRTSettings(self, SRTSettings):
        self._SRTSettings = SRTSettings

    @property
    def RTPSettings(self):
        """The RTP relay configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        """
        return self._RTPSettings

    @RTPSettings.setter
    def RTPSettings(self, RTPSettings):
        self._RTPSettings = RTPSettings

    @property
    def RTMPSettings(self):
        """The RTMP relay configuration.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        """
        return self._RTMPSettings

    @RTMPSettings.setter
    def RTMPSettings(self, RTMPSettings):
        self._RTMPSettings = RTMPSettings

    @property
    def AllowIpList(self):
        """IP whitelist, in CIDR format, such as 0.0.0.0/0. This is valid when Protocol is RTMP_PULL, and empty means no restriction on client IP.
        :rtype: list of str
        """
        return self._AllowIpList

    @AllowIpList.setter
    def AllowIpList(self, AllowIpList):
        self._AllowIpList = AllowIpList

    @property
    def MaxConcurrent(self):
        """The maximum number of concurrent stream pulls is 4, and the default value is 4.
        :rtype: int
        """
        return self._MaxConcurrent

    @MaxConcurrent.setter
    def MaxConcurrent(self, MaxConcurrent):
        self._MaxConcurrent = MaxConcurrent

    @property
    def SecurityGroupIds(self):
        """The bound security group IDs.
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._OutputId = params.get("OutputId")
        self._OutputName = params.get("OutputName")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowRequest(AbstractModel):
    """ModifyStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        :param _FlowName: Name of the flow to modify
        :type FlowName: str
        """
        self._FlowId = None
        self._FlowName = None

    @property
    def FlowId(self):
        """Flow ID
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def FlowName(self):
        """Name of the flow to modify
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
    """ModifyStreamLinkFlow response structure.

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


class ModifyStreamLinkInputRequest(AbstractModel):
    """ModifyStreamLinkInput request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Input: The input information to modify.
        :type Input: :class:`tencentcloud.mdc.v20200828.models.ModifyInput`
        """
        self._FlowId = None
        self._Input = None

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Input(self):
        """The input information to modify.
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
    """ModifyStreamLinkInput response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The input information after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeInput`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """The input information after modification.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeInput`
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
            self._Info = DescribeInput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class ModifyStreamLinkOutputInfoRequest(AbstractModel):
    """ModifyStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: The flow ID.
        :type FlowId: str
        :param _Output: The output configuration to modify.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.ModifyOutputInfo`
        """
        self._FlowId = None
        self._Output = None

    @property
    def FlowId(self):
        """The flow ID.
        :rtype: str
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def Output(self):
        """The output configuration to modify.
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
    """ModifyStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The output configuration after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        """The output configuration after modification.
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
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
            self._Info = DescribeOutput()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class OutputAddress(AbstractModel):
    """Output destination address.

    """

    def __init__(self):
        r"""
        :param _Ip: Output destination IP.
        :type Ip: str
        """
        self._Ip = None

    @property
    def Ip(self):
        """Output destination IP.
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
        


class OutputSRTSourceAddressResp(AbstractModel):
    """The listen address for an SRT output.

    """

    def __init__(self):
        r"""
        :param _Ip: The listen IP.
        :type Ip: str
        :param _Port: The listen port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """The listen IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """The listen port.
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
        


class RTMPAddressDestination(AbstractModel):
    """Destination address information of RTMP push.

    """

    def __init__(self):
        r"""
        :param _Url: Destination URL of RTMP push in the format of 'rtmp://domain/live'.
        :type Url: str
        :param _StreamKey: Destination `StreamKey` of RTMP push in the format of 'streamid?key=value'.
        :type StreamKey: str
        """
        self._Url = None
        self._StreamKey = None

    @property
    def Url(self):
        """Destination URL of RTMP push in the format of 'rtmp://domain/live'.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StreamKey(self):
        """Destination `StreamKey` of RTMP push in the format of 'streamid?key=value'.
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
    """

    """

    def __init__(self):
        r"""
        :param _TcUrl: 
        :type TcUrl: str
        :param _StreamKey: 
        :type StreamKey: str
        """
        self._TcUrl = None
        self._StreamKey = None

    @property
    def TcUrl(self):
        """
        :rtype: str
        """
        return self._TcUrl

    @TcUrl.setter
    def TcUrl(self, TcUrl):
        self._TcUrl = TcUrl

    @property
    def StreamKey(self):
        """
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
    """Destination address information of RTP push.

    """

    def __init__(self):
        r"""
        :param _Ip: Push destination address IP.
        :type Ip: str
        :param _Port: Push destination address port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """Push destination address IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Push destination address port.
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
    """

    """

    def __init__(self):
        r"""
        :param _Url: 
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        """
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
    """Region information

    """

    def __init__(self):
        r"""
        :param _Name: Region name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """Region name
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
    """

    """

    def __init__(self):
        r"""
        :param _Enable: 
        :type Enable: bool
        :param _BufferTime: 
        :type BufferTime: int
        """
        self._Enable = None
        self._BufferTime = None

    @property
    def Enable(self):
        """
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def BufferTime(self):
        """
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
    """Push destination address information.

    """

    def __init__(self):
        r"""
        :param _Ip: Destination address IP.
        :type Ip: str
        :param _Port: Destination address port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """Destination address IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """Destination address port.
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
        


class SRTSourceAddressReq(AbstractModel):
    """The SRT input address.

    """

    def __init__(self):
        r"""
        :param _Ip: The peer IP.
        :type Ip: str
        :param _Port: The peer port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """The peer IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """The peer port.
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
    """The SRT input address.

    """

    def __init__(self):
        r"""
        :param _Ip: The peer IP.
        :type Ip: str
        :param _Port: The peer port.
        :type Port: int
        """
        self._Ip = None
        self._Port = None

    @property
    def Ip(self):
        """The peer IP.
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        """The peer port.
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
    """StartStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """Flow ID
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
    """StartStreamLinkFlow response structure.

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


class StopStreamLinkFlowRequest(AbstractModel):
    """StopStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param _FlowId: Flow ID
        :type FlowId: str
        """
        self._FlowId = None

    @property
    def FlowId(self):
        """Flow ID
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
    """StopStreamLinkFlow response structure.

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


class StreamLinkRegionInfo(AbstractModel):
    """StreamLink region information

    """

    def __init__(self):
        r"""
        :param _Regions: List of StreamLink regions
        :type Regions: list of RegionInfo
        """
        self._Regions = None

    @property
    def Regions(self):
        """List of StreamLink regions
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
        