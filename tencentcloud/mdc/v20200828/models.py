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
        :param InputName: Input name, which can contain 1 to 32 letters, digits, and underscores.
        :type InputName: str
        :param Protocol: Input protocol. Valid values: `SRT`, `RTP`, `RTMP`
        :type Protocol: str
        :param Description: Input description. Length: [0, 255].
        :type Description: str
        :param AllowIpList: Allowlist of input IPs in CIDR format.
        :type AllowIpList: list of str
        :param SRTSettings: SRT configuration information of input.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param RTPSettings: RTP configuration information of input.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param FailOver: Input failover. Valid values: `OPEN`, `CLOSE` (default)
        :type FailOver: str
        """
        self.InputName = None
        self.Protocol = None
        self.Description = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.FailOver = None


    def _deserialize(self, params):
        self.InputName = params.get("InputName")
        self.Protocol = params.get("Protocol")
        self.Description = params.get("Description")
        self.AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateInputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateInputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.FailOver = params.get("FailOver")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputRTPSettings(AbstractModel):
    """RTP configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param FEC: Default value: none. Valid values: ['none'].
        :type FEC: str
        :param IdleTimeout: Idle timeout period in ms. Default value: 5000. Value range: [1000, 10000].
        :type IdleTimeout: int
        """
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInputSRTSettings(AbstractModel):
    """SRT configuration information of the created input.

    """

    def __init__(self):
        r"""
        :param Mode: The SRT mode. Valid values: LISTENER (default), CALLER.
        :type Mode: str
        :param StreamId: Stream ID, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :type StreamId: str
        :param Latency: Latency in ms. Default value: 0. Value range: [0, 3000].
        :type Latency: int
        :param RecvLatency: Receive latency in ms. Default value: 120. Value range: [0, 3000].
        :type RecvLatency: int
        :param PeerLatency: Peer latency in ms. Default value: 0. Value range: [0, 3000].
        :type PeerLatency: int
        :param PeerIdleTimeout: Peer timeout period in ms. Default value: 5000. Value range: [1000, 10000].
        :type PeerIdleTimeout: int
        :param Passphrase: Decryption key, which is empty by default, indicating not to encrypt. Only ASCII codes can be filled. Length: [10, 79].
        :type Passphrase: str
        :param PbKeyLen: Key length. Default value: 0. Valid values: 0, 16, 24, 32.
        :type PbKeyLen: int
        :param SourceAddresses: The SRT peer address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :type SourceAddresses: list of SRTSourceAddressReq
        """
        self.Mode = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.SourceAddresses = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressReq()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfo(AbstractModel):
    """The information of the output to create.

    """

    def __init__(self):
        r"""
        :param OutputName: The output name.
        :type OutputName: str
        :param Description: Description of the output.
        :type Description: str
        :param Protocol: The output protocol. Valid values: SRT, RTP, RTMP, RTMP_PULL.
        :type Protocol: str
        :param OutputRegion: The output region.
        :type OutputRegion: str
        :param SRTSettings: The SRT configuration.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param RTMPSettings: The RTMP configuration.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param RTPSettings: The RTP configuration.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param AllowIpList: The IP allowlist. The address must be in CIDR format, such as `0.0.0.0/0`.
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If it is left empty, there is no restriction on clients’ IP addresses.
        :type AllowIpList: list of str
        """
        self.OutputName = None
        self.Description = None
        self.Protocol = None
        self.OutputRegion = None
        self.SRTSettings = None
        self.RTMPSettings = None
        self.RTPSettings = None
        self.AllowIpList = None


    def _deserialize(self, params):
        self.OutputName = params.get("OutputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        self.OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateOutputSrtSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = CreateOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateOutputInfoRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputInfoRTPSettings(AbstractModel):
    """The RTP configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param Destinations: The relay destination addresses. One or two addresses are allowed.
        :type Destinations: list of CreateOutputRTPSettingsDestinations
        :param FEC: This parameter must be set to `none`.
        :type FEC: str
        :param IdleTimeout: The timeout period (ms).
        :type IdleTimeout: int
        """
        self.Destinations = None
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRTPSettingsDestinations()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTMPSettings(AbstractModel):
    """The RTMP configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param Destinations: The relay destination addresses. One or two addresses are allowed.
        :type Destinations: list of CreateOutputRtmpSettingsDestinations
        :param ChunkSize: The RTMP chunk size. Value range: [4096, 40960].
        :type ChunkSize: int
        """
        self.Destinations = None
        self.ChunkSize = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputRtmpSettingsDestinations()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.ChunkSize = params.get("ChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTPSettingsDestinations(AbstractModel):
    """The RTP destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param Ip: The relay destination IP.
        :type Ip: str
        :param Port: The relay destination port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRtmpSettingsDestinations(AbstractModel):
    """The RTMP destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param Url: The relay URL. Format: `rtmp://domain/live`.
        :type Url: str
        :param StreamKey: The `StreamKey` for relay. Format: `stream?key=value`.
        :type StreamKey: str
        """
        self.Url = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettings(AbstractModel):
    """The SRT configuration of the output to create.

    """

    def __init__(self):
        r"""
        :param Destinations: The relay destination address, which is required if `Mode` is `CALLER`. Only one address is allowed.
        :type Destinations: list of CreateOutputSrtSettingsDestinations
        :param StreamId: The stream ID for relay, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).
        :type StreamId: str
        :param Latency: The total latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :type Latency: int
        :param RecvLatency: The receive latency (ms) of SRT relay. Value range: [0, 3000]. Default: 120.
        :type RecvLatency: int
        :param PeerLatency: The peer-to-peer latency (ms) of SRT relay. Value range: [0, 3000]. Default: 0.
        :type PeerLatency: int
        :param PeerIdleTimeout: The timeout period (ms) for the SRT relay peer. Value range: [1000, 10000]. Default: 5000.
        :type PeerIdleTimeout: int
        :param Passphrase: The encryption key for SRT relay, which is empty by default, indicating not to encrypt. Only ASCII codes are allowed. Length: [10, 79].
        :type Passphrase: str
        :param PbKeyLen: The key length for SRT relay. Valid values: 0 (default), 16, 24, 32.
        :type PbKeyLen: int
        :param Mode: The SRT mode. Valid values: LISTENER, CALLER (default).
        :type Mode: str
        """
        self.Destinations = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.Mode = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = CreateOutputSrtSettingsDestinations()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettingsDestinations(AbstractModel):
    """The SRT destination address of the output to create.

    """

    def __init__(self):
        r"""
        :param Ip: The output IP.
        :type Ip: str
        :param Port: The output port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowRequest(AbstractModel):
    """CreateStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param FlowName: Flow name
        :type FlowName: str
        :param MaxBandwidth: Maximum bandwidth in bps. Valid values: `10000000`, `20000000`, `50000000`
        :type MaxBandwidth: int
        :param InputGroup: Flow input group
        :type InputGroup: list of CreateInput
        """
        self.FlowName = None
        self.MaxBandwidth = None
        self.InputGroup = None


    def _deserialize(self, params):
        self.FlowName = params.get("FlowName")
        self.MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self.InputGroup = []
            for item in params.get("InputGroup"):
                obj = CreateInput()
                obj._deserialize(item)
                self.InputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkFlowResponse(AbstractModel):
    """CreateStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param Info: Information of the created flow
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeFlow()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class CreateStreamLinkOutputInfoRequest(AbstractModel):
    """CreateStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param Output: The output configuration of the flow.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfo`
        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = CreateOutputInfo()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLinkOutputInfoResponse(AbstractModel):
    """CreateStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param Info: The information of the created output.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeOutput()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DeleteStreamLinkFlowRequest(AbstractModel):
    """DeleteStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Flow ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkFlowResponse(AbstractModel):
    """DeleteStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStreamLinkOutputRequest(AbstractModel):
    """DeleteStreamLinkOutput request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Flow ID
        :type FlowId: str
        :param OutputId: Output ID
        :type OutputId: str
        """
        self.FlowId = None
        self.OutputId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.OutputId = params.get("OutputId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLinkOutputResponse(AbstractModel):
    """DeleteStreamLinkOutput response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeFlow(AbstractModel):
    """Configuration information of the queried flow.

    """

    def __init__(self):
        r"""
        :param FlowId: Flow ID.
        :type FlowId: str
        :param FlowName: Flow name.
        :type FlowName: str
        :param State: Flow status. Valid values: `IDLE`, `RUNNING`
        :type State: str
        :param MaxBandwidth: Maximum bandwidth value.
        :type MaxBandwidth: int
        :param InputGroup: Input group.
        :type InputGroup: list of DescribeInput
        :param OutputGroup: Output group.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutputGroup: list of DescribeOutput
        """
        self.FlowId = None
        self.FlowName = None
        self.State = None
        self.MaxBandwidth = None
        self.InputGroup = None
        self.OutputGroup = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        self.State = params.get("State")
        self.MaxBandwidth = params.get("MaxBandwidth")
        if params.get("InputGroup") is not None:
            self.InputGroup = []
            for item in params.get("InputGroup"):
                obj = DescribeInput()
                obj._deserialize(item)
                self.InputGroup.append(obj)
        if params.get("OutputGroup") is not None:
            self.OutputGroup = []
            for item in params.get("OutputGroup"):
                obj = DescribeOutput()
                obj._deserialize(item)
                self.OutputGroup.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInput(AbstractModel):
    """Configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param InputId: Input ID.
        :type InputId: str
        :param InputName: Input name.
        :type InputName: str
        :param Description: Input description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param Protocol: Input protocol.
        :type Protocol: str
        :param InputAddressList: Input address list.
        :type InputAddressList: list of InputAddress
        :param AllowIpList: Input IP allowlist.
        :type AllowIpList: list of str
        :param SRTSettings: SRT configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputSRTSettings`
        :param RTPSettings: RTP configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTPSettings`
        :param InputRegion: Input region.
        :type InputRegion: str
        :param RTMPSettings: RTMP configuration information of an input
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTMPSettings`
        :param FailOver: Input failover
Note: this field may return `null`, indicating that no valid value was found.
        :type FailOver: str
        """
        self.InputId = None
        self.InputName = None
        self.Description = None
        self.Protocol = None
        self.InputAddressList = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.InputRegion = None
        self.RTMPSettings = None
        self.FailOver = None


    def _deserialize(self, params):
        self.InputId = params.get("InputId")
        self.InputName = params.get("InputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        if params.get("InputAddressList") is not None:
            self.InputAddressList = []
            for item in params.get("InputAddressList"):
                obj = InputAddress()
                obj._deserialize(item)
                self.InputAddressList.append(obj)
        self.AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = DescribeInputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = DescribeInputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.InputRegion = params.get("InputRegion")
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = DescribeInputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        self.FailOver = params.get("FailOver")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTMPSettings(AbstractModel):
    """RTMP configuration information of the queried input

    """

    def __init__(self):
        r"""
        :param AppName: Path for RTMP stream pushing
Note: this field may return `null`, indicating that no valid value was found.
        :type AppName: str
        :param StreamKey: StreamKey for RTMP stream pushing
Format of an RTMP stream pushing URL: rtmp://IP address:1935/AppName/StreamKey
        :type StreamKey: str
        """
        self.AppName = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputRTPSettings(AbstractModel):
    """RTP configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param FEC: Whether it is FEC.
        :type FEC: str
        :param IdleTimeout: Idle timeout period.
        :type IdleTimeout: int
        """
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInputSRTSettings(AbstractModel):
    """SRT configuration information of the queried input.

    """

    def __init__(self):
        r"""
        :param Mode: The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param StreamId: Stream ID.
        :type StreamId: str
        :param Latency: Latency.
        :type Latency: int
        :param RecvLatency: Receive latency.
        :type RecvLatency: int
        :param PeerLatency: Peer latency.
        :type PeerLatency: int
        :param PeerIdleTimeout: Peer idle timeout period.
        :type PeerIdleTimeout: int
        :param Passphrase: Decryption key.
        :type Passphrase: str
        :param PbKeyLen: Key length.
        :type PbKeyLen: int
        :param SourceAddresses: The SRT peer address.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SourceAddresses: list of SRTSourceAddressResp
        """
        self.Mode = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.SourceAddresses = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = SRTSourceAddressResp()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutput(AbstractModel):
    """Configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param OutputId: Output ID.
        :type OutputId: str
        :param OutputName: Output name.
        :type OutputName: str
        :param OutputType: Output type.
        :type OutputType: str
        :param Description: Output description.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Description: str
        :param Protocol: Output protocol.
        :type Protocol: str
        :param OutputAddressList: Output destination address information list.
        :type OutputAddressList: list of OutputAddress
        :param OutputRegion: Output region.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OutputRegion: str
        :param SRTSettings: SRT configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputSRTSettings`
        :param RTPSettings: RTP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTPSettings`
        :param RTMPSettings: RTMP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPSettings`
        :param RTMPPullSettings: RTMP pull configuration of the output
Note: This field may return `null`, indicating that no valid value was found.
        :type RTMPPullSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPPullSettings`
        :param AllowIpList: CIDR allowlist
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If this parameter is left empty, there is no restriction on clients’ IP addresses.
Note: This field may return `null`, indicating that no valid value was found.
        :type AllowIpList: list of str
        """
        self.OutputId = None
        self.OutputName = None
        self.OutputType = None
        self.Description = None
        self.Protocol = None
        self.OutputAddressList = None
        self.OutputRegion = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.RTMPSettings = None
        self.RTMPPullSettings = None
        self.AllowIpList = None


    def _deserialize(self, params):
        self.OutputId = params.get("OutputId")
        self.OutputName = params.get("OutputName")
        self.OutputType = params.get("OutputType")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        if params.get("OutputAddressList") is not None:
            self.OutputAddressList = []
            for item in params.get("OutputAddressList"):
                obj = OutputAddress()
                obj._deserialize(item)
                self.OutputAddressList.append(obj)
        self.OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = DescribeOutputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = DescribeOutputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = DescribeOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        if params.get("RTMPPullSettings") is not None:
            self.RTMPPullSettings = DescribeOutputRTMPPullSettings()
            self.RTMPPullSettings._deserialize(params.get("RTMPPullSettings"))
        self.AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullServerUrl(AbstractModel):
    """RTMP pull URL of the output

    """

    def __init__(self):
        r"""
        :param TcUrl: `tcUrl` of the RTMP pull URL
        :type TcUrl: str
        :param StreamKey: Stream key of the RTMP pull URL
        :type StreamKey: str
        """
        self.TcUrl = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.TcUrl = params.get("TcUrl")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPPullSettings(AbstractModel):
    """RTMP pull configuration of the output

    """

    def __init__(self):
        r"""
        :param ServerUrls: List of pull URLs
Note: This field may return `null`, indicating that no valid value was found.
        :type ServerUrls: list of DescribeOutputRTMPPullServerUrl
        """
        self.ServerUrls = None


    def _deserialize(self, params):
        if params.get("ServerUrls") is not None:
            self.ServerUrls = []
            for item in params.get("ServerUrls"):
                obj = DescribeOutputRTMPPullServerUrl()
                obj._deserialize(item)
                self.ServerUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTMPSettings(AbstractModel):
    """RTMP configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdleTimeout: int
        :param ChunkSize: Chunk size.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ChunkSize: int
        :param Destinations: Destination address information list of RTMP push.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of RTMPAddressDestination
        """
        self.IdleTimeout = None
        self.ChunkSize = None
        self.Destinations = None


    def _deserialize(self, params):
        self.IdleTimeout = params.get("IdleTimeout")
        self.ChunkSize = params.get("ChunkSize")
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = RTMPAddressDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputRTPSettings(AbstractModel):
    """RTP configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param Destinations: Destination address information list of RTP push.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Destinations: list of RTPAddressDestination
        :param FEC: Whether it is FEC.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FEC: str
        :param IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IdleTimeout: int
        """
        self.Destinations = None
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = RTPAddressDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOutputSRTSettings(AbstractModel):
    """SRT configuration information of the queried output.

    """

    def __init__(self):
        r"""
        :param Destinations: A list of the destination addresses for relay. This parameter is valid if `Mode` is `CALLER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Destinations: list of SRTAddressDestination
        :param StreamId: Stream ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamId: str
        :param Latency: Latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Latency: int
        :param RecvLatency: Receive latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RecvLatency: int
        :param PeerLatency: Peer latency.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeerLatency: int
        :param PeerIdleTimeout: Peer idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PeerIdleTimeout: int
        :param Passphrase: Encryption key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Passphrase: str
        :param PbKeyLen: Encryption key length.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PbKeyLen: int
        :param Mode: The SRT mode.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mode: str
        :param SourceAddresses: The server’s listen address, which is valid if `Mode` is `LISTENER`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SourceAddresses: list of OutputSRTSourceAddressResp
        """
        self.Destinations = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None
        self.Mode = None
        self.SourceAddresses = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = SRTAddressDestination()
                obj._deserialize(item)
                self.Destinations.append(obj)
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
        self.Mode = params.get("Mode")
        if params.get("SourceAddresses") is not None:
            self.SourceAddresses = []
            for item in params.get("SourceAddresses"):
                obj = OutputSRTSourceAddressResp()
                obj._deserialize(item)
                self.SourceAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowLogsRequest(AbstractModel):
    """DescribeStreamLinkFlowLogs request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: list of str
        :param Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: list of str
        :param PageSize: The page size. Value range: [1, 1000]. Default: 100.
        :type PageSize: int
        :param SortType: Whether to sort the records by timestamp in descending or ascending order. Valid values: desc (default), asc.
        :type SortType: str
        :param PageNum: The page number. Value range: [1, 1000]. Default: 1.
        :type PageNum: int
        """
        self.FlowId = None
        self.StartTime = None
        self.EndTime = None
        self.Type = None
        self.Pipeline = None
        self.PageSize = None
        self.SortType = None
        self.PageNum = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Type = params.get("Type")
        self.Pipeline = params.get("Pipeline")
        self.PageSize = params.get("PageSize")
        self.SortType = params.get("SortType")
        self.PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowLogsResponse(AbstractModel):
    """DescribeStreamLinkFlowLogs response structure.

    """

    def __init__(self):
        r"""
        :param Infos: A list of the logs.
        :type Infos: list of FlowLogInfo
        :param PageNum: The current page number.
        :type PageNum: int
        :param PageSize: The number of records per page.
        :type PageSize: int
        :param TotalNum: The total number of records.
        :type TotalNum: int
        :param TotalPage: The total number of pages.
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
                obj = FlowLogInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowMediaStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        :param StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        """
        self.FlowId = None
        self.Type = None
        self.InputOutputId = None
        self.Pipeline = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Pipeline = params.get("Pipeline")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowMediaStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowMediaStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Infos: A list of the media data.
        :type Infos: list of FlowMediaInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = FlowMediaInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRealtimeStatusRequest(AbstractModel):
    """DescribeStreamLinkFlowRealtimeStatus request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param InputIds: The IDs of the inputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
        :type InputIds: list of str
        :param OutputIds: The IDs of the outputs to query. If this parameter and `OutputIds` are both empty, all inputs and outputs are queried.
        :type OutputIds: list of str
        """
        self.FlowId = None
        self.InputIds = None
        self.OutputIds = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InputIds = params.get("InputIds")
        self.OutputIds = params.get("OutputIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowRealtimeStatusResponse(AbstractModel):
    """DescribeStreamLinkFlowRealtimeStatus response structure.

    """

    def __init__(self):
        r"""
        :param Timestamp: The timestamp (seconds) of the query.
        :type Timestamp: int
        :param Datas: A list of the real-time data.
        :type Datas: list of FlowRealtimeStatusItem
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Timestamp = None
        self.Datas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        if params.get("Datas") is not None:
            self.Datas = []
            for item in params.get("Datas"):
                obj = FlowRealtimeStatusItem()
                obj._deserialize(item)
                self.Datas.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowRequest(AbstractModel):
    """DescribeStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Flow ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowResponse(AbstractModel):
    """DescribeStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param Info: Configuration information of a flow
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeFlow()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowSRTStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        """
        self.FlowId = None
        self.Type = None
        self.InputOutputId = None
        self.Pipeline = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Pipeline = params.get("Pipeline")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowSRTStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowSRTStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Infos: A list of the SRT streaming performance data.
        :type Infos: list of FlowSRTInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = FlowSRTInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowStatisticsRequest(AbstractModel):
    """DescribeStreamLinkFlowStatistics request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param Type: Whether to query the inputs or outputs. Valid values: input, output.
        :type Type: str
        :param InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param Pipeline: Whether to query the primary or backup pipeline. Valid values: 0, 1.
        :type Pipeline: str
        :param Period: The query interval. Valid values: 5s, 1min, 5min, 15min.
        :type Period: str
        :param StartTime: The start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param EndTime: The end time for query, which is 1 hour after the start time by default. The longest time range allowed for query is 24 hours.
It must be in UTC format, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        """
        self.FlowId = None
        self.Type = None
        self.InputOutputId = None
        self.Pipeline = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Pipeline = params.get("Pipeline")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLinkFlowStatisticsResponse(AbstractModel):
    """DescribeStreamLinkFlowStatistics response structure.

    """

    def __init__(self):
        r"""
        :param Infos: A list of the media data.
        :type Infos: list of FlowStatisticsArray
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = FlowStatisticsArray()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkFlowsRequest(AbstractModel):
    """DescribeStreamLinkFlows request structure.

    """

    def __init__(self):
        r"""
        :param PageNum: Number of the current page. Default value: `1`
        :type PageNum: int
        :param PageSize: Number of entries per page. Default value: `10`
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
        


class DescribeStreamLinkFlowsResponse(AbstractModel):
    """DescribeStreamLinkFlows response structure.

    """

    def __init__(self):
        r"""
        :param Infos: List of the configuration information of the flows
        :type Infos: list of DescribeFlow
        :param PageNum: Number of the current page
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
                obj = DescribeFlow()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeStreamLinkRegionsRequest(AbstractModel):
    """DescribeStreamLinkRegions request structure.

    """


class DescribeStreamLinkRegionsResponse(AbstractModel):
    """DescribeStreamLinkRegions response structure.

    """

    def __init__(self):
        r"""
        :param Info: StreamLink region information
        :type Info: :class:`tencentcloud.mdc.v20200828.models.StreamLinkRegionInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = StreamLinkRegionInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class FlowAudio(AbstractModel):
    """The audio data of the flow.

    """

    def __init__(self):
        r"""
        :param Fps: The frame rate.
        :type Fps: int
        :param Rate: The bitrate (bps).
        :type Rate: int
        :param Pid: The audio PID.
        :type Pid: int
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowLogInfo(AbstractModel):
    """The logs of a flow.

    """

    def __init__(self):
        r"""
        :param Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param Type: Whether it is an input or output.
        :type Type: str
        :param InputOutputId: The input or output ID.
        :type InputOutputId: str
        :param Protocol: The protocol.
        :type Protocol: str
        :param EventCode: The event code.
        :type EventCode: str
        :param EventMessage: The event information.
        :type EventMessage: str
        :param RemoteIp: The peer IP.
        :type RemoteIp: str
        :param RemotePort: The peer port.
        :type RemotePort: str
        :param Pipeline: Whether it is a primary or backup pipeline. Valid values: 0 (primary), 1 (backup).
        :type Pipeline: str
        :param InputOutputName: The input or output name.
        :type InputOutputName: str
        """
        self.Timestamp = None
        self.Type = None
        self.InputOutputId = None
        self.Protocol = None
        self.EventCode = None
        self.EventMessage = None
        self.RemoteIp = None
        self.RemotePort = None
        self.Pipeline = None
        self.InputOutputName = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Type = params.get("Type")
        self.InputOutputId = params.get("InputOutputId")
        self.Protocol = params.get("Protocol")
        self.EventCode = params.get("EventCode")
        self.EventMessage = params.get("EventMessage")
        self.RemoteIp = params.get("RemoteIp")
        self.RemotePort = params.get("RemotePort")
        self.Pipeline = params.get("Pipeline")
        self.InputOutputName = params.get("InputOutputName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaAudio(AbstractModel):
    """The audio data of a flow.

    """

    def __init__(self):
        r"""
        :param Fps: The frame rate.
        :type Fps: int
        :param Rate: The bitrate (bps).
        :type Rate: int
        :param Pid: The audio PID.
        :type Pid: int
        :param SessionId: The ID of a push session.
        :type SessionId: str
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaInfo(AbstractModel):
    """The media data of a flow.

    """

    def __init__(self):
        r"""
        :param Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param Network: The total bandwidth.
        :type Network: int
        :param Video: The video data of the flow.
        :type Video: list of FlowMediaVideo
        :param Audio: The audio data of the flow.
        :type Audio: list of FlowMediaAudio
        :param SessionId: The ID of a push session.
        :type SessionId: str
        :param ClientIp: The client IP.
        :type ClientIp: str
        """
        self.Timestamp = None
        self.Network = None
        self.Video = None
        self.Audio = None
        self.SessionId = None
        self.ClientIp = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.Network = params.get("Network")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = FlowMediaVideo()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = FlowMediaAudio()
                obj._deserialize(item)
                self.Audio.append(obj)
        self.SessionId = params.get("SessionId")
        self.ClientIp = params.get("ClientIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowMediaVideo(AbstractModel):
    """The video data of a flow.

    """

    def __init__(self):
        r"""
        :param Fps: The frame rate.
        :type Fps: int
        :param Rate: The bitrate (bps).
        :type Rate: int
        :param Pid: The video PID.
        :type Pid: int
        :param SessionId: The ID of a push session.
        :type SessionId: str
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusCommon(AbstractModel):
    """The common real-time status information of a flow.

    """

    def __init__(self):
        r"""
        :param State: The connection status. Valid values: Connected, Waiting, Idle.
        :type State: str
        :param Mode: The connection mode. Valid values: Listener, Caller.
        :type Mode: str
        :param ConnectedTime: The connected time.
        :type ConnectedTime: int
        :param Bitrate: The real-time bitrate (bps).
        :type Bitrate: int
        :param Reconnections: The number of retries.
        :type Reconnections: int
        """
        self.State = None
        self.Mode = None
        self.ConnectedTime = None
        self.Bitrate = None
        self.Reconnections = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.Mode = params.get("Mode")
        self.ConnectedTime = params.get("ConnectedTime")
        self.Bitrate = params.get("Bitrate")
        self.Reconnections = params.get("Reconnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusItem(AbstractModel):
    """The real-time status information of a flow.

    """

    def __init__(self):
        r"""
        :param Type: Whether it is an input or output. Valid values: Input, Output.
        :type Type: str
        :param InputId: The input ID, which is not empty if `Type` is `Input`.
        :type InputId: str
        :param OutputId: The output ID, which is not empty if `Type` is `Output`.
        :type OutputId: str
        :param FlowId: The flow ID.
        :type FlowId: str
        :param Protocol: The protocol used. Valid values: SRT, RTP, RTMP.
        :type Protocol: str
        :param CommonStatus: The common status information.
        :type CommonStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusCommon`
        :param SRTStatus: This parameter is returned if `Protocol` is `SRT`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SRTStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusSRT`
        :param RTMPStatus: This parameter is returned if `Protocol` is `RTMP`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RTMPStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTMP`
        :param ConnectServerIP: The server IP.
        :type ConnectServerIP: str
        :param RTPStatus: This parameter is returned if the RTP protocol is used.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RTPStatus: :class:`tencentcloud.mdc.v20200828.models.FlowRealtimeStatusRTP`
        """
        self.Type = None
        self.InputId = None
        self.OutputId = None
        self.FlowId = None
        self.Protocol = None
        self.CommonStatus = None
        self.SRTStatus = None
        self.RTMPStatus = None
        self.ConnectServerIP = None
        self.RTPStatus = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InputId = params.get("InputId")
        self.OutputId = params.get("OutputId")
        self.FlowId = params.get("FlowId")
        self.Protocol = params.get("Protocol")
        if params.get("CommonStatus") is not None:
            self.CommonStatus = FlowRealtimeStatusCommon()
            self.CommonStatus._deserialize(params.get("CommonStatus"))
        if params.get("SRTStatus") is not None:
            self.SRTStatus = FlowRealtimeStatusSRT()
            self.SRTStatus._deserialize(params.get("SRTStatus"))
        if params.get("RTMPStatus") is not None:
            self.RTMPStatus = FlowRealtimeStatusRTMP()
            self.RTMPStatus._deserialize(params.get("RTMPStatus"))
        self.ConnectServerIP = params.get("ConnectServerIP")
        if params.get("RTPStatus") is not None:
            self.RTPStatus = FlowRealtimeStatusRTP()
            self.RTPStatus._deserialize(params.get("RTPStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTMP(AbstractModel):
    """The real-time RTMP streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param VideoFPS: The video frame rate.
        :type VideoFPS: int
        :param AudioFPS: The audio frame rate.
        :type AudioFPS: int
        """
        self.VideoFPS = None
        self.AudioFPS = None


    def _deserialize(self, params):
        self.VideoFPS = params.get("VideoFPS")
        self.AudioFPS = params.get("AudioFPS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusRTP(AbstractModel):
    """The real-time RTP streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param Packets: The number of packets transmitted.
        :type Packets: int
        """
        self.Packets = None


    def _deserialize(self, params):
        self.Packets = params.get("Packets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowRealtimeStatusSRT(AbstractModel):
    """The real-time SRT streaming information of a flow.

    """

    def __init__(self):
        r"""
        :param Latency: The latency (ms).
        :type Latency: int
        :param RTT: RTT (ms).
        :type RTT: int
        :param Packets: The number of packets sent or received.
        :type Packets: int
        :param PacketLossRate: The packet loss rate.
        :type PacketLossRate: float
        :param RetransmitRate: The retransmission rate.
        :type RetransmitRate: float
        :param DroppedPackets: The number of packets dropped.
        :type DroppedPackets: int
        :param Encryption: Whether to encrypt the stream. Valid values: On, Off.
        :type Encryption: str
        """
        self.Latency = None
        self.RTT = None
        self.Packets = None
        self.PacketLossRate = None
        self.RetransmitRate = None
        self.DroppedPackets = None
        self.Encryption = None


    def _deserialize(self, params):
        self.Latency = params.get("Latency")
        self.RTT = params.get("RTT")
        self.Packets = params.get("Packets")
        self.PacketLossRate = params.get("PacketLossRate")
        self.RetransmitRate = params.get("RetransmitRate")
        self.DroppedPackets = params.get("DroppedPackets")
        self.Encryption = params.get("Encryption")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowSRTInfo(AbstractModel):
    """The SRT streaming performance data.

    """

    def __init__(self):
        r"""
        :param Timestamp: The timestamp (seconds).
        :type Timestamp: int
        :param SendPacketLossRate: The packet loss rate for sending.
        :type SendPacketLossRate: int
        :param SendRetransmissionRate: The retry rate for sending.
        :type SendRetransmissionRate: int
        :param RecvPacketLossRate: The packet loss rate for receiving.
        :type RecvPacketLossRate: int
        :param RecvRetransmissionRate: The retry rate for receiving.
        :type RecvRetransmissionRate: int
        :param RTT: The peer RTT.
        :type RTT: int
        :param SessionId: The ID of a push session.
        :type SessionId: str
        :param SendPacketDropNumber: The number of dropped packets for sending.
        :type SendPacketDropNumber: int
        :param RecvPacketDropNumber: The number of dropped packets for receiving.
        :type RecvPacketDropNumber: int
        """
        self.Timestamp = None
        self.SendPacketLossRate = None
        self.SendRetransmissionRate = None
        self.RecvPacketLossRate = None
        self.RecvRetransmissionRate = None
        self.RTT = None
        self.SessionId = None
        self.SendPacketDropNumber = None
        self.RecvPacketDropNumber = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.SendPacketLossRate = params.get("SendPacketLossRate")
        self.SendRetransmissionRate = params.get("SendRetransmissionRate")
        self.RecvPacketLossRate = params.get("RecvPacketLossRate")
        self.RecvRetransmissionRate = params.get("RecvRetransmissionRate")
        self.RTT = params.get("RTT")
        self.SessionId = params.get("SessionId")
        self.SendPacketDropNumber = params.get("SendPacketDropNumber")
        self.RecvPacketDropNumber = params.get("RecvPacketDropNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatistics(AbstractModel):
    """The flow statistics.

    """

    def __init__(self):
        r"""
        :param SessionId: The session ID.
        :type SessionId: str
        :param ClientIp: The peer IP.
        :type ClientIp: str
        :param Network: The total bandwidth.
        :type Network: int
        :param Video: The video data.
        :type Video: list of FlowVideo
        :param Audio: The audio data.
        :type Audio: list of FlowAudio
        """
        self.SessionId = None
        self.ClientIp = None
        self.Network = None
        self.Video = None
        self.Audio = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.ClientIp = params.get("ClientIp")
        self.Network = params.get("Network")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = FlowVideo()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = FlowAudio()
                obj._deserialize(item)
                self.Audio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowStatisticsArray(AbstractModel):
    """A list of the flow statistics.

    """

    def __init__(self):
        r"""
        :param Timestamp: The timestamp.
        :type Timestamp: int
        :param FlowStatistics: The statistics of all the sessions.
        :type FlowStatistics: list of FlowStatistics
        """
        self.Timestamp = None
        self.FlowStatistics = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        if params.get("FlowStatistics") is not None:
            self.FlowStatistics = []
            for item in params.get("FlowStatistics"):
                obj = FlowStatistics()
                obj._deserialize(item)
                self.FlowStatistics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowVideo(AbstractModel):
    """The video data of a flow.

    """

    def __init__(self):
        r"""
        :param Fps: The frame rate.
        :type Fps: int
        :param Rate: The bitrate (bps).
        :type Rate: int
        :param Pid: The audio PID.
        :type Pid: int
        """
        self.Fps = None
        self.Rate = None
        self.Pid = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputAddress(AbstractModel):
    """Input address information.

    """

    def __init__(self):
        r"""
        :param Ip: Input address IP.
        :type Ip: str
        :param Port: Input address port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInput(AbstractModel):
    """The new input configuration.

    """

    def __init__(self):
        r"""
        :param InputId: The input ID.
        :type InputId: str
        :param InputName: The input name.
        :type InputName: str
        :param Description: The description of the input.
        :type Description: str
        :param AllowIpList: The IP addresses (CIDR) allowed to push streams.
        :type AllowIpList: list of str
        :param SRTSettings: The SRT configuration information.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param RTPSettings: The RTP configuration information.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param Protocol: The input protocol. Valid values: SRT, RTP, RTMP.
If there is an RTP input, the output must be RTP.
If there is an RTMP input, the output must be SRT or RTMP.
If there is an SRT input, the output must be SRT.
        :type Protocol: str
        :param FailOver: Whether to enable input failover. Valid values: OPEN, CLOSE.
        :type FailOver: str
        """
        self.InputId = None
        self.InputName = None
        self.Description = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.Protocol = None
        self.FailOver = None


    def _deserialize(self, params):
        self.InputId = params.get("InputId")
        self.InputName = params.get("InputName")
        self.Description = params.get("Description")
        self.AllowIpList = params.get("AllowIpList")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateInputSRTSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateInputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        self.Protocol = params.get("Protocol")
        self.FailOver = params.get("FailOver")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyOutputInfo(AbstractModel):
    """The new output configuration.

    """

    def __init__(self):
        r"""
        :param OutputId: The ID of the output to modify.
        :type OutputId: str
        :param OutputName: The output name.
        :type OutputName: str
        :param Description: The description of the output.
        :type Description: str
        :param Protocol: The output protocol. Valid values: SRT, RTP, RTMP.
        :type Protocol: str
        :param SRTSettings: The SRT relay configuration.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param RTPSettings: The RTP relay configuration.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputInfoRTPSettings`
        :param RTMPSettings: The RTMP relay configuration.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        :param AllowIpList: The IP allowlist. The address must be in CIDR format, such as `0.0.0.0/0`.
This parameter is valid if `Protocol` is set to `RTMP_PULL`. If it is left empty, there is no restriction on clients’ IP addresses.
        :type AllowIpList: list of str
        """
        self.OutputId = None
        self.OutputName = None
        self.Description = None
        self.Protocol = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.RTMPSettings = None
        self.AllowIpList = None


    def _deserialize(self, params):
        self.OutputId = params.get("OutputId")
        self.OutputName = params.get("OutputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateOutputSrtSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateOutputInfoRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = CreateOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))
        self.AllowIpList = params.get("AllowIpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowRequest(AbstractModel):
    """ModifyStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Flow ID
        :type FlowId: str
        :param FlowName: Name of the flow to modify
        :type FlowName: str
        """
        self.FlowId = None
        self.FlowName = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkFlowResponse(AbstractModel):
    """ModifyStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyStreamLinkInputRequest(AbstractModel):
    """ModifyStreamLinkInput request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param Input: The input information to modify.
        :type Input: :class:`tencentcloud.mdc.v20200828.models.ModifyInput`
        """
        self.FlowId = None
        self.Input = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Input") is not None:
            self.Input = ModifyInput()
            self.Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkInputResponse(AbstractModel):
    """ModifyStreamLinkInput response structure.

    """

    def __init__(self):
        r"""
        :param Info: The input information after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeInput`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeInput()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class ModifyStreamLinkOutputInfoRequest(AbstractModel):
    """ModifyStreamLinkOutputInfo request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: The flow ID.
        :type FlowId: str
        :param Output: The output configuration to modify.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.ModifyOutputInfo`
        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = ModifyOutputInfo()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLinkOutputInfoResponse(AbstractModel):
    """ModifyStreamLinkOutputInfo response structure.

    """

    def __init__(self):
        r"""
        :param Info: The output configuration after modification.
        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = DescribeOutput()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class OutputAddress(AbstractModel):
    """Output destination address.

    """

    def __init__(self):
        r"""
        :param Ip: Output destination IP.
        :type Ip: str
        """
        self.Ip = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputSRTSourceAddressResp(AbstractModel):
    """The listen address for an SRT output.

    """

    def __init__(self):
        r"""
        :param Ip: The listen IP.
        :type Ip: str
        :param Port: The listen port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTMPAddressDestination(AbstractModel):
    """Destination address information of RTMP push.

    """

    def __init__(self):
        r"""
        :param Url: Destination URL of RTMP push in the format of 'rtmp://domain/live'.
        :type Url: str
        :param StreamKey: Destination `StreamKey` of RTMP push in the format of 'streamid?key=value'.
        :type StreamKey: str
        """
        self.Url = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StreamKey = params.get("StreamKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RTPAddressDestination(AbstractModel):
    """Destination address information of RTP push.

    """

    def __init__(self):
        r"""
        :param Ip: Push destination address IP.
        :type Ip: str
        :param Port: Push destination address port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param Name: Region name
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTAddressDestination(AbstractModel):
    """Push destination address information.

    """

    def __init__(self):
        r"""
        :param Ip: Destination address IP.
        :type Ip: str
        :param Port: Destination address port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressReq(AbstractModel):
    """The SRT input address.

    """

    def __init__(self):
        r"""
        :param Ip: The peer IP.
        :type Ip: str
        :param Port: The peer port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SRTSourceAddressResp(AbstractModel):
    """The SRT input address.

    """

    def __init__(self):
        r"""
        :param Ip: The peer IP.
        :type Ip: str
        :param Port: The peer port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowRequest(AbstractModel):
    """StartStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Flow ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLinkFlowResponse(AbstractModel):
    """StartStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopStreamLinkFlowRequest(AbstractModel):
    """StopStreamLinkFlow request structure.

    """

    def __init__(self):
        r"""
        :param FlowId: Flow ID
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamLinkFlowResponse(AbstractModel):
    """StopStreamLinkFlow response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamLinkRegionInfo(AbstractModel):
    """StreamLink region information

    """

    def __init__(self):
        r"""
        :param Regions: List of StreamLink regions
        :type Regions: list of RegionInfo
        """
        self.Regions = None


    def _deserialize(self, params):
        if params.get("Regions") is not None:
            self.Regions = []
            for item in params.get("Regions"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        