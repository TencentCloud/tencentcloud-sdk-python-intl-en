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
        """
        :param InputName: Input name, which can contain 1 to 32 letters, digits, and underscores.\n        :type InputName: str\n        :param Protocol: Input protocol. Valid values: SRT, RTP.\n        :type Protocol: str\n        :param Description: Input description. Length: [0, 255].\n        :type Description: str\n        :param AllowIpList: Allowlist of input IPs in CIDR format.\n        :type AllowIpList: list of str\n        :param SRTSettings: SRT configuration information of input.\n        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`\n        :param RTPSettings: RTP configuration information of input.\n        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`\n        """
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
        """
        :param FEC: Default value: none. Valid values: ['none'].\n        :type FEC: str\n        :param IdleTimeout: Idle timeout period in ms. Default value: 5000. Value range: [1000, 10000].\n        :type IdleTimeout: int\n        """
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
        """
        :param StreamId: Stream ID, which can contain 0 to 512 letters, digits, and special characters (.#!:&,=_-).\n        :type StreamId: str\n        :param Latency: Latency in ms. Default value: 0. Value range: [0, 3000].\n        :type Latency: int\n        :param RecvLatency: Receive latency in ms. Default value: 120. Value range: [0, 3000].\n        :type RecvLatency: int\n        :param PeerLatency: Peer latency in ms. Default value: 0. Value range: [0, 3000].\n        :type PeerLatency: int\n        :param PeerIdleTimeout: Peer timeout period in ms. Default value: 5000. Value range: [1000, 10000].\n        :type PeerIdleTimeout: int\n        :param Passphrase: Decryption key, which is empty by default, indicating not to encrypt. Only ASCII codes can be filled. Length: [10, 79].\n        :type Passphrase: str\n        :param PbKeyLen: Key length. Default value: 0. Valid values: 0, 16, 24, 32.\n        :type PbKeyLen: int\n        """
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
        


class CreateMediaConnectFlowRequest(AbstractModel):
    """CreateMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowName: Flow name.\n        :type FlowName: str\n        :param MaxBandwidth: Maximum bandwidth in bps. Valid values: 10000000, 20000000, 50000000.\n        :type MaxBandwidth: int\n        :param InputGroup: Flow input group.\n        :type InputGroup: list of CreateInput\n        """
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
        


class CreateMediaConnectFlowResponse(AbstractModel):
    """CreateMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param Info: Information of the created flow.\n        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param FlowId: Flow ID.\n        :type FlowId: str\n        :param Output: Output configuration of a flow.\n        :type Output: :class:`tencentcloud.mdc.v20200828.models.CreateOutput`\n        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = CreateOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaConnectOutputResponse(AbstractModel):
    """CreateMediaConnectOutput response structure.

    """

    def __init__(self):
        """
        :param Info: Information of the created output.\n        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param OutputName: Output name.\n        :type OutputName: str\n        :param Description: Output description.\n        :type Description: str\n        :param Protocol: Output protocol.\n        :type Protocol: str\n        :param OutputRegion: Output region.\n        :type OutputRegion: str\n        :param SRTSettings: SRT configuration of output.\n        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`\n        :param RTPSettings: RTP configuration of output.\n        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`\n        :param RTMPSettings: RTMP configuration of output.\n        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTMPSettings(AbstractModel):
    """RTMP configuration of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Destinations: Push destination address. You can enter one or two addresses.\n        :type Destinations: list of CreateOutputRtmpSettingsDestinations\n        :param ChunkSize: RTMP chunk size. Value range: [4096, 40960].\n        :type ChunkSize: int\n        """
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
        


class CreateOutputRTPSettings(AbstractModel):
    """RTP configuration of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Destinations: Push destination address. You can enter one or two addresses.\n        :type Destinations: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTPSettingsDestinations`\n        :param FEC: Only `none` can be entered.\n        :type FEC: str\n        :param IdleTimeout: Idle timeout period.\n        :type IdleTimeout: int\n        """
        self.Destinations = None
        self.FEC = None
        self.IdleTimeout = None


    def _deserialize(self, params):
        if params.get("Destinations") is not None:
            self.Destinations = CreateOutputRTPSettingsDestinations()
            self.Destinations._deserialize(params.get("Destinations"))
        self.FEC = params.get("FEC")
        self.IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputRTPSettingsDestinations(AbstractModel):
    """RTP destination address of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Ip: Push destination IP.\n        :type Ip: str\n        :param Port: Push destination port.\n        :type Port: int\n        """
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
    """RTMP destination address of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Url: Push URL in the format of `rtmp://domain/live`.\n        :type Url: str\n        :param StreamKey: Push `StreamKey` in the format of `stream?key=value`.\n        :type StreamKey: str\n        """
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
    """SRT configuration of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Destinations: Push destination address. Please configure one or two addresses.\n        :type Destinations: list of CreateOutputSrtSettingsDestinations\n        :param StreamId: Stream ID of SRT push.\n        :type StreamId: str\n        :param Latency: Total latency of SRT push.\n        :type Latency: int\n        :param RecvLatency: Receive latency of SRT push.\n        :type RecvLatency: int\n        :param PeerLatency: Peer latency of SRT push.\n        :type PeerLatency: int\n        :param PeerIdleTimeout: Peer idle timeout period of SRT push.\n        :type PeerIdleTimeout: int\n        :param Passphrase: Encryption key of SRT push.\n        :type Passphrase: str\n        :param PbKeyLen: Key length of SRT push.\n        :type PbKeyLen: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOutputSrtSettingsDestinations(AbstractModel):
    """SRT destination address of the created MediaConnect flow output.

    """

    def __init__(self):
        """
        :param Ip: Output IP.\n        :type Ip: str\n        :param Port: Output port.\n        :type Port: int\n        """
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
        


class DeleteMediaConnectFlowRequest(AbstractModel):
    """DeleteMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaConnectFlowResponse(AbstractModel):
    """DeleteMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaConnectOutputRequest(AbstractModel):
    """DeleteMediaConnectOutput request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        :param OutputId: Output ID.\n        :type OutputId: str\n        """
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
        


class DeleteMediaConnectOutputResponse(AbstractModel):
    """DeleteMediaConnectOutput response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeFlow(AbstractModel):
    """Configuration information of the queried flow.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        :param FlowName: Flow name.\n        :type FlowName: str\n        :param State: Flow status.\n        :type State: str\n        :param MaxBandwidth: Maximum bandwidth value.\n        :type MaxBandwidth: int\n        :param InputGroup: Input group.\n        :type InputGroup: list of DescribeInput\n        :param OutputGroup: Output group.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OutputGroup: list of DescribeOutput\n        """
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
        """
        :param InputId: Input ID.\n        :type InputId: str\n        :param InputName: Input name.\n        :type InputName: str\n        :param Description: Input description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param Protocol: Input protocol.\n        :type Protocol: str\n        :param InputAddressList: Input address list.\n        :type InputAddressList: list of InputAddress\n        :param AllowIpList: Input IP allowlist.\n        :type AllowIpList: list of str\n        :param SRTSettings: SRT configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputSRTSettings`\n        :param RTPSettings: RTP configuration information of input.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeInputRTPSettings`\n        :param InputRegion: Input region.\n        :type InputRegion: str\n        """
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
        """
        :param FEC: Whether it is FEC.\n        :type FEC: str\n        :param IdleTimeout: Idle timeout period.\n        :type IdleTimeout: int\n        """
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
        """
        :param StreamId: Stream ID.\n        :type StreamId: str\n        :param Latency: Latency.\n        :type Latency: int\n        :param RecvLatency: Receive latency.\n        :type RecvLatency: int\n        :param PeerLatency: Peer latency.\n        :type PeerLatency: int\n        :param PeerIdleTimeout: Peer idle timeout period.\n        :type PeerIdleTimeout: int\n        :param Passphrase: Decryption key.\n        :type Passphrase: str\n        :param PbKeyLen: Key length.\n        :type PbKeyLen: int\n        """
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
        


class DescribeMediaConnectFlowRequest(AbstractModel):
    """DescribeMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaConnectFlowResponse(AbstractModel):
    """DescribeMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param Info: Configuration information of a flow.\n        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeFlow`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param PageNum: Number of current pages. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Default value: 10.\n        :type PageSize: int\n        """
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
        


class DescribeMediaConnectFlowsResponse(AbstractModel):
    """DescribeMediaConnectFlows response structure.

    """

    def __init__(self):
        """
        :param Infos: Configuration information list of a flow.\n        :type Infos: list of DescribeFlow\n        :param PageNum: Number of current pages.\n        :type PageNum: int\n        :param PageSize: Number of entries per page.\n        :type PageSize: int\n        :param TotalNum: Total number.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param OutputId: Output ID.\n        :type OutputId: str\n        :param OutputName: Output name.\n        :type OutputName: str\n        :param OutputType: Output type.\n        :type OutputType: str\n        :param Description: Output description.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Description: str\n        :param Protocol: Output protocol.\n        :type Protocol: str\n        :param OutputAddressList: Output destination address information list.\n        :type OutputAddressList: list of OutputAddress\n        :param OutputRegion: Output region.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OutputRegion: str\n        :param SRTSettings: SRT configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputSRTSettings`\n        :param RTPSettings: RTP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTPSettings`\n        :param RTMPSettings: RTMP configuration information of output.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.DescribeOutputRTMPSettings`\n        """
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
        """
        :param IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IdleTimeout: int\n        :param ChunkSize: Chunk size.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ChunkSize: int\n        :param Destinations: Destination address information list of RTMP push.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Destinations: list of RTMPAddressDestination\n        """
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
        """
        :param Destinations: Destination address information list of RTP push.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Destinations: list of RTPAddressDestination\n        :param FEC: Whether it is FEC.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FEC: str\n        :param IdleTimeout: Idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IdleTimeout: int\n        """
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
        """
        :param Destinations: Push destination address information list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Destinations: list of SRTAddressDestination\n        :param StreamId: Stream ID.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StreamId: str\n        :param Latency: Latency.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Latency: int\n        :param RecvLatency: Receive latency.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RecvLatency: int\n        :param PeerLatency: Peer latency.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PeerLatency: int\n        :param PeerIdleTimeout: Peer idle timeout period.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PeerIdleTimeout: int\n        :param Passphrase: Encryption key.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Passphrase: str\n        :param PbKeyLen: Encryption key length.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PbKeyLen: int\n        """
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
        


class InputAddress(AbstractModel):
    """Input address information.

    """

    def __init__(self):
        """
        :param Ip: Input address IP.\n        :type Ip: str\n        :param Port: Input address port.\n        :type Port: int\n        """
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
    """Parameters of the modified input.

    """

    def __init__(self):
        """
        :param InputId: Input ID.\n        :type InputId: str\n        :param InputName: Input name.\n        :type InputName: str\n        :param Description: Input description.\n        :type Description: str\n        :param AllowIpList: Allowed push IP in CIDR format.\n        :type AllowIpList: list of str\n        :param SRTSettings: SRT configuration information.\n        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputSRTSettings`\n        :param RTPSettings: RTP configuration information.\n        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateInputRTPSettings`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMediaConnectFlowRequest(AbstractModel):
    """ModifyMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        :param FlowName: Name of the flow to be modified.\n        :type FlowName: str\n        """
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
        


class ModifyMediaConnectFlowResponse(AbstractModel):
    """ModifyMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaConnectInputRequest(AbstractModel):
    """ModifyMediaConnectInput request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        :param Input: Information of the input to be modified.\n        :type Input: :class:`tencentcloud.mdc.v20200828.models.ModifyInput`\n        """
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
        


class ModifyMediaConnectInputResponse(AbstractModel):
    """ModifyMediaConnectInput response structure.

    """

    def __init__(self):
        """
        :param Info: Input information after modification.\n        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeInput`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param FlowId: Flow ID.\n        :type FlowId: str\n        :param Output: Configuration of the output to be modified.\n        :type Output: :class:`tencentcloud.mdc.v20200828.models.ModifyOutput`\n        """
        self.FlowId = None
        self.Output = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Output") is not None:
            self.Output = ModifyOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMediaConnectOutputResponse(AbstractModel):
    """ModifyMediaConnectOutput response structure.

    """

    def __init__(self):
        """
        :param Info: Output configuration after modification.\n        :type Info: :class:`tencentcloud.mdc.v20200828.models.DescribeOutput`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param OutputId: ID of the output to be modified.\n        :type OutputId: str\n        :param OutputName: Output name.\n        :type OutputName: str\n        :param Description: Output description.\n        :type Description: str\n        :param Protocol: Output push protocol. Valid values: SRT, RTMP.\n        :type Protocol: str\n        :param SRTSettings: Configuration of SRT push.\n        :type SRTSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputSrtSettings`\n        :param RTPSettings: Configuration of RTP push.\n        :type RTPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTPSettings`\n        :param RTMPSettings: Configuration of RTMP push.\n        :type RTMPSettings: :class:`tencentcloud.mdc.v20200828.models.CreateOutputRTMPSettings`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputAddress(AbstractModel):
    """Output destination address.

    """

    def __init__(self):
        """
        :param Ip: Output destination IP.\n        :type Ip: str\n        """
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
        """
        :param Url: Destination URL of RTMP push in the format of 'rtmp://domain/live'.\n        :type Url: str\n        :param StreamKey: Destination `StreamKey` of RTMP push in the format of 'streamid?key=value'.\n        :type StreamKey: str\n        """
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
        """
        :param Ip: Push destination address IP.\n        :type Ip: str\n        :param Port: Push destination address port.\n        :type Port: int\n        """
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
        


class SRTAddressDestination(AbstractModel):
    """Push destination address information.

    """

    def __init__(self):
        """
        :param Ip: Destination address IP.\n        :type Ip: str\n        :param Port: Destination address port.\n        :type Port: int\n        """
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
        


class StartMediaConnectFlowRequest(AbstractModel):
    """StartMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMediaConnectFlowResponse(AbstractModel):
    """StartMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMediaConnectFlowRequest(AbstractModel):
    """StopMediaConnectFlow request structure.

    """

    def __init__(self):
        """
        :param FlowId: Flow ID.\n        :type FlowId: str\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMediaConnectFlowResponse(AbstractModel):
    """StopMediaConnectFlow response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")