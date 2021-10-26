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
        """
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
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
        """
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.Latency = params.get("Latency")
        self.RecvLatency = params.get("RecvLatency")
        self.PeerLatency = params.get("PeerLatency")
        self.PeerIdleTimeout = params.get("PeerIdleTimeout")
        self.Passphrase = params.get("Passphrase")
        self.PbKeyLen = params.get("PbKeyLen")
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
        :param Destinations: Push destination address information list.
Note: this field may return null, indicating that no valid values can be obtained.
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
        """
        self.Destinations = None
        self.StreamId = None
        self.Latency = None
        self.RecvLatency = None
        self.PeerLatency = None
        self.PeerIdleTimeout = None
        self.Passphrase = None
        self.PbKeyLen = None


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        