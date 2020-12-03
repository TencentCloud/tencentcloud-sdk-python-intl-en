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


class CreateInput(AbstractModel):
    """Configuration information of the created input.

    """

    def __init__(self):
        """
        :param InputName: Input name, which can contain 1 to 32 letters, digits, and underscores.
        :type InputName: str
        :param Protocol: Input protocol. Valid values: SRT, RTP.
        :type Protocol: str
        :param Description: Input description. Length: [0, 255].
        :type Description: str
        :param AllowIpList: Allowlist of input IPs in CIDR format.
        :type AllowIpList: list of str
        :param SRTSettings: SRT configuration information of input.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param RTPSettings: RTP configuration information of input.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        """
        self.InputName = None
        self.Protocol = None
        self.Description = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None


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


class CreateInputRTPSettings(AbstractModel):
    """RTP configuration information of the created input.

    """

    def __init__(self):
        """
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


class CreateInputSRTSettings(AbstractModel):
    """SRT configuration information of the created input.

    """

    def __init__(self):
        """
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


class CreateMediaConnectFlowRequest(AbstractModel):
    """CreateMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowName: Flow name.
        :type FlowName: str
        :param MaxBandwidth: Maximum bandwidth in bps. Valid values: 10000000, 20000000, 50000000.
        :type MaxBandwidth: int
        :param InputGroup: Flow input group.
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


class CreateMediaConnectFlowResponse(AbstractModel):
    """CreateMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param Info: Information of the created flow.
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


class CreateMediaConnectOutputRequest(AbstractModel):
    """CreateMediaConnectOutput request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        :param Output: Output configuration of a flow.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.CreateOutput`
        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = CreateOutput()
            self.Output._deserialize(params.get("Output"))


class CreateMediaConnectOutputResponse(AbstractModel):
    """CreateMediaConnectOutput response structure.

    """

    def __init__(self):
        """
        :param Info: Information of the created output.
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


class CreateOutput(AbstractModel):
    """Configuration information of the created output.

    """

    def __init__(self):
        """
        :param OutputName: Output name.
        :type OutputName: str
        :param Description: Output description.
        :type Description: str
        :param Protocol: Output protocol.
        :type Protocol: str
        :param OutputRegion: Output region.
        :type OutputRegion: str
        :param SRTSettings: SRT configuration of output.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param RTPSettings: RTP configuration of output.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        :param RTMPSettings: RTMP configuration of output.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        """
        self.OutputName = None
        self.Description = None
        self.Protocol = None
        self.OutputRegion = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.RTMPSettings = None


    def _deserialize(self, params):
        self.OutputName = params.get("OutputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        self.OutputRegion = params.get("OutputRegion")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateOutputSrtSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateInputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = CreateOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))


class CreateOutputRTMPSettings(AbstractModel):
    """RTMP configuration of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Destinations: Push destination address. You can enter one or two addresses.
        :type Destinations: list of CreateOutputRtmpSettingsDestinations
        :param ChunkSize: RTMP chunk size. Value range: [4096, 40960].
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


class CreateOutputRTPSettings(AbstractModel):
    """RTP configuration of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Destinations: Push destination address. You can enter one or two addresses.
        :type Destinations: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTPSettingsDestinations`
        :param FEC: Only `none` can be entered.
        :type FEC: str
        :param IdleTimeout: Idle timeout period.
        :type IdleTimeout: int
        """
        self.Destinations = None
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = CreateOutputRTPSettingsDestinations()
            self.Destinations._deserialize(params.get("Destinations"))
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")


class CreateOutputRTPSettingsDestinations(AbstractModel):
    """RTP destination address of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Ip: Push destination IP.
        :type Ip: str
        :param Port: Push destination port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")


class CreateOutputRtmpSettingsDestinations(AbstractModel):
    """RTMP destination address of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Url: Push URL in the format of `rtmp://domain/live`.
        :type Url: str
        :param StreamKey: Push `StreamKey` in the format of `stream?key=value`.
        :type StreamKey: str
        """
        self.Url = None
        self.StreamKey = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StreamKey = params.get("StreamKey")


class CreateOutputSrtSettings(AbstractModel):
    """SRT configuration of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Destinations: Push destination address. Please configure one or two addresses.
        :type Destinations: list of CreateOutputSrtSettingsDestinations
        :param StreamId: Stream ID of SRT push.
        :type StreamId: str
        :param Latency: Total latency of SRT push.
        :type Latency: int
        :param RecvLatency: Receive latency of SRT push.
        :type RecvLatency: int
        :param PeerLatency: Peer latency of SRT push.
        :type PeerLatency: int
        :param PeerIdleTimeout: Peer idle timeout period of SRT push.
        :type PeerIdleTimeout: int
        :param Passphrase: Encryption key of SRT push.
        :type Passphrase: str
        :param PbKeyLen: Key length of SRT push.
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


class CreateOutputSrtSettingsDestinations(AbstractModel):
    """SRT destination address of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Ip: Output IP.
        :type Ip: str
        :param Port: Output port.
        :type Port: int
        """
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")


class DeleteMediaConnectFlowRequest(AbstractModel):
    """DeleteMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DeleteMediaConnectFlowResponse(AbstractModel):
    """DeleteMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaConnectOutputRequest(AbstractModel):
    """DeleteMediaConnectOutput request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        :param OutputId: Output ID.
        :type OutputId: str
        """
        self.FlowId = None
        self.OutputId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.OutputId = params.get("OutputId")


class DeleteMediaConnectOutputResponse(AbstractModel):
    """DeleteMediaConnectOutput response structure.

    """

    def __init__(self):
        """
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
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        :param FlowName: Flow name.
        :type FlowName: str
        :param State: Flow status.
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


class DescribeInput(AbstractModel):
    """Configuration information of the queried input.

    """

    def __init__(self):
        """
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


class DescribeInputRTPSettings(AbstractModel):
    """RTP configuration information of the queried input.

    """

    def __init__(self):
        """
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


class DescribeInputSRTSettings(AbstractModel):
    """SRT configuration information of the queried input.

    """

    def __init__(self):
        """
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


class DescribeMediaConnectFlowRequest(AbstractModel):
    """DescribeMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DescribeMediaConnectFlowResponse(AbstractModel):
    """DescribeMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param Info: Configuration information of a flow.
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


class DescribeMediaConnectFlowsRequest(AbstractModel):
    """DescribeMediaConnectFlows request structure.

    """

    def __init__(self):
        """
        :param PageNum: Number of current pages. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Default value: 10.
        :type PageSize: int
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeMediaConnectFlowsResponse(AbstractModel):
    """DescribeMediaConnectFlows response structure.

    """

    def __init__(self):
        """
        :param Infos: Configuration information list of a flow.
        :type Infos: list of DescribeFlow
        :param PageNum: Number of current pages.
        :type PageNum: int
        :param PageSize: Number of entries per page.
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
                obj = DescribeFlow()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeOutput(AbstractModel):
    """Configuration information of the queried output.

    """

    def __init__(self):
        """
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


class DescribeOutputRTMPSettings(AbstractModel):
    """RTMP configuration information of the queried output.

    """

    def __init__(self):
        """
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


class DescribeOutputRTPSettings(AbstractModel):
    """RTP configuration information of the queried output.

    """

    def __init__(self):
        """
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


class DescribeOutputSRTSettings(AbstractModel):
    """SRT configuration information of the queried output.

    """

    def __init__(self):
        """
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


class InputAddress(AbstractModel):
    """Input address information.

    """

    def __init__(self):
        """
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


class ModifyInput(AbstractModel):
    """Parameters of the modified input.

    """

    def __init__(self):
        """
        :param InputId: Input ID.
        :type InputId: str
        :param InputName: Input name.
        :type InputName: str
        :param Description: Input description.
        :type Description: str
        :param AllowIpList: Allowed push IP in CIDR format.
        :type AllowIpList: list of str
        :param SRTSettings: SRT configuration information.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`
        :param RTPSettings: RTP configuration information.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`
        """
        self.InputId = None
        self.InputName = None
        self.Description = None
        self.AllowIpList = None
        self.SRTSettings = None
        self.RTPSettings = None


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


class ModifyMediaConnectFlowRequest(AbstractModel):
    """ModifyMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        :param FlowName: Name of the flow to be modified.
        :type FlowName: str
        """
        self.FlowId = None
        self.FlowName = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")


class ModifyMediaConnectFlowResponse(AbstractModel):
    """ModifyMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaConnectInputRequest(AbstractModel):
    """ModifyMediaConnectInput request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        :param Input: Information of the input to be modified.
        :type Input: :class:`tencentcloud.mdc.v20200828.models.ModifyInput`
        """
        self.FlowId = None
        self.Input = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Input") is not None:
            self.Input = ModifyInput()
            self.Input._deserialize(params.get("Input"))


class ModifyMediaConnectInputResponse(AbstractModel):
    """ModifyMediaConnectInput response structure.

    """

    def __init__(self):
        """
        :param Info: Input information after modification.
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


class ModifyMediaConnectOutputRequest(AbstractModel):
    """ModifyMediaConnectOutput request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        :param Output: Configuration of the output to be modified.
        :type Output: :class:`tencentcloud.mdc.v20200828.models.ModifyOutput`
        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = ModifyOutput()
            self.Output._deserialize(params.get("Output"))


class ModifyMediaConnectOutputResponse(AbstractModel):
    """ModifyMediaConnectOutput response structure.

    """

    def __init__(self):
        """
        :param Info: Output configuration after modification.
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


class ModifyOutput(AbstractModel):
    """Configuration of the modified output.

    """

    def __init__(self):
        """
        :param OutputId: ID of the output to be modified.
        :type OutputId: str
        :param OutputName: Output name.
        :type OutputName: str
        :param Description: Output description.
        :type Description: str
        :param Protocol: Output push protocol. Valid values: SRT, RTMP.
        :type Protocol: str
        :param SRTSettings: Configuration of SRT push.
        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`
        :param RTPSettings: Configuration of RTP push.
        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTPSettings`
        :param RTMPSettings: Configuration of RTMP push.
        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`
        """
        self.OutputId = None
        self.OutputName = None
        self.Description = None
        self.Protocol = None
        self.SRTSettings = None
        self.RTPSettings = None
        self.RTMPSettings = None


    def _deserialize(self, params):
        self.OutputId = params.get("OutputId")
        self.OutputName = params.get("OutputName")
        self.Description = params.get("Description")
        self.Protocol = params.get("Protocol")
        if params.get("SRTSettings") is not None:
            self.SRTSettings = CreateOutputSrtSettings()
            self.SRTSettings._deserialize(params.get("SRTSettings"))
        if params.get("RTPSettings") is not None:
            self.RTPSettings = CreateOutputRTPSettings()
            self.RTPSettings._deserialize(params.get("RTPSettings"))
        if params.get("RTMPSettings") is not None:
            self.RTMPSettings = CreateOutputRTMPSettings()
            self.RTMPSettings._deserialize(params.get("RTMPSettings"))


class OutputAddress(AbstractModel):
    """Output destination address.

    """

    def __init__(self):
        """
        :param Ip: Output destination IP.
        :type Ip: str
        """
        self.Ip = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")


class RTMPAddressDestination(AbstractModel):
    """Destination address information of RTMP push.

    """

    def __init__(self):
        """
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


class RTPAddressDestination(AbstractModel):
    """Destination address information of RTP push.

    """

    def __init__(self):
        """
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


class SRTAddressDestination(AbstractModel):
    """Push destination address information.

    """

    def __init__(self):
        """
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


class StartMediaConnectFlowRequest(AbstractModel):
    """StartMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class StartMediaConnectFlowResponse(AbstractModel):
    """StartMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMediaConnectFlowRequest(AbstractModel):
    """StopMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.
        :type FlowId: str
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class StopMediaConnectFlowResponse(AbstractModel):
    """StopMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")