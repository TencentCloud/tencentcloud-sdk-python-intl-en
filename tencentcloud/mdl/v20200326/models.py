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


class AttachedInputInfo(AbstractModel):
    """Media input associated with media channel.

    """

    def __init__(self):
        """
        :param Id: Media input ID.\n        :type Id: str\n        :param AudioSelectors: Audio selector for media input. Quantity limit: [0,20]
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioSelectors: list of AudioSelectorInfo\n        """
        self.Id = None
        self.AudioSelectors = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("AudioSelectors") is not None:
            self.AudioSelectors = []
            for item in params.get("AudioSelectors"):
                obj = AudioSelectorInfo()
                obj._deserialize(item)
                self.AudioSelectors.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioPidSelectionInfo(AbstractModel):
    """Audio `Pid` selection.

    """

    def __init__(self):
        """
        :param Pid: Audio `Pid`. Default value: 0.\n        :type Pid: int\n        """
        self.Pid = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioPipelineInputStatistics(AbstractModel):
    """Pipeline input audio statistics.

    """

    def __init__(self):
        """
        :param Fps: Audio FPS.\n        :type Fps: int\n        :param Rate: Audio bitrate in bps.\n        :type Rate: int\n        :param Pid: Audio `Pid`, which is available only if the input is `rtp/udp`.\n        :type Pid: int\n        """
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
        


class AudioSelectorInfo(AbstractModel):
    """Audio selector.

    """

    def __init__(self):
        """
        :param Name: Audio name, which can contain 1-32 letters, digits, and underscores.\n        :type Name: str\n        :param AudioPidSelection: Audio `Pid` selection.\n        :type AudioPidSelection: :class:`tencentcloud.mdl.v20200326.models.AudioPidSelectionInfo`\n        """
        self.Name = None
        self.AudioPidSelection = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AudioPidSelection") is not None:
            self.AudioPidSelection = AudioPidSelectionInfo()
            self.AudioPidSelection._deserialize(params.get("AudioPidSelection"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfo(AbstractModel):
    """Audio transcoding template.

    """

    def __init__(self):
        """
        :param AudioSelectorName: Only `AttachedInputs.AudioSelectors.Name` can be selected. This parameter is required for RTP_PUSH and UDP_PUSH.\n        :type AudioSelectorName: str\n        :param Name: Audio transcoding template name, which can contain 1-20 letters and digits.\n        :type Name: str\n        :param Acodec: Audio codec. Valid value: AAC. Default value: AAC.\n        :type Acodec: str\n        :param AudioBitrate: Audio bitrate. If this parameter is left empty, the original value will be used.
Valid values: 6000, 7000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000\n        :type AudioBitrate: int\n        :param LanguageCode: Audio language code, whose length is always 3 characters.\n        :type LanguageCode: str\n        """
        self.AudioSelectorName = None
        self.Name = None
        self.Acodec = None
        self.AudioBitrate = None
        self.LanguageCode = None


    def _deserialize(self, params):
        self.AudioSelectorName = params.get("AudioSelectorName")
        self.Name = params.get("Name")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.LanguageCode = params.get("LanguageCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelAlertInfos(AbstractModel):
    """Channel alarm information.

    """

    def __init__(self):
        """
        :param Pipeline0: Alarm details of pipeline 0 under this channel.\n        :type Pipeline0: list of ChannelPipelineAlerts\n        :param Pipeline1: Alarm details of pipeline 1 under this channel.\n        :type Pipeline1: list of ChannelPipelineAlerts\n        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = ChannelPipelineAlerts()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = ChannelPipelineAlerts()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
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
        """
        :param Id: Channel ID.\n        :type Id: str\n        :param State: Channel status.\n        :type State: str\n        :param AttachedInputs: Information of associated input.\n        :type AttachedInputs: list of AttachedInputInfo\n        :param OutputGroups: Information of output group.\n        :type OutputGroups: list of OutputGroupsInfo\n        :param Name: Channel name.\n        :type Name: str\n        :param AudioTemplates: Audio transcoding template array.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioTemplates: list of AudioTemplateInfo\n        :param VideoTemplates: Video transcoding template array.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoTemplates: list of VideoTemplateInfo\n        """
        self.Id = None
        self.State = None
        self.AttachedInputs = None
        self.OutputGroups = None
        self.Name = None
        self.AudioTemplates = None
        self.VideoTemplates = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.State = params.get("State")
        if params.get("AttachedInputs") is not None:
            self.AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInputInfo()
                obj._deserialize(item)
                self.AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self.OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = OutputGroupsInfo()
                obj._deserialize(item)
                self.OutputGroups.append(obj)
        self.Name = params.get("Name")
        if params.get("AudioTemplates") is not None:
            self.AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self.AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self.VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self.VideoTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelInputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        """
        :param InputId: Input ID.\n        :type InputId: str\n        :param Statistics: Input statistics.\n        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.InputStatistics`\n        """
        self.InputId = None
        self.Statistics = None


    def _deserialize(self, params):
        self.InputId = params.get("InputId")
        if params.get("Statistics") is not None:
            self.Statistics = InputStatistics()
            self.Statistics._deserialize(params.get("Statistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelOutputsStatistics(AbstractModel):
    """Channel output information.

    """

    def __init__(self):
        """
        :param OutputGroupName: Output group name.\n        :type OutputGroupName: str\n        :param Statistics: Output group statistics.\n        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.OutputsStatistics`\n        """
        self.OutputGroupName = None
        self.Statistics = None


    def _deserialize(self, params):
        self.OutputGroupName = params.get("OutputGroupName")
        if params.get("Statistics") is not None:
            self.Statistics = OutputsStatistics()
            self.Statistics._deserialize(params.get("Statistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelPipelineAlerts(AbstractModel):
    """Channel alarm details.

    """

    def __init__(self):
        """
        :param SetTime: Alarm start time in UTC time.\n        :type SetTime: str\n        :param ClearTime: Alarm end time in UTC time.
This time is available only after the alarm ends.\n        :type ClearTime: str\n        :param Type: Alarm type.\n        :type Type: str\n        :param Message: Alarm details.\n        :type Message: str\n        """
        self.SetTime = None
        self.ClearTime = None
        self.Type = None
        self.Message = None


    def _deserialize(self, params):
        self.SetTime = params.get("SetTime")
        self.ClearTime = params.get("ClearTime")
        self.Type = params.get("Type")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaLiveChannelRequest(AbstractModel):
    """CreateMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Name: Channel name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.\n        :type Name: str\n        :param AttachedInputs: Associated media input. Quantity limit: [1,1].\n        :type AttachedInputs: list of AttachedInputInfo\n        :param OutputGroups: Configuration information of channel output groups. Quantity limit: [1,10].\n        :type OutputGroups: list of OutputGroupsInfo\n        :param AudioTemplates: Audio transcoding template array. Quantity limit: [1,20].\n        :type AudioTemplates: list of AudioTemplateInfo\n        :param VideoTemplates: Video transcoding template array. Quantity limit: [1,10].\n        :type VideoTemplates: list of VideoTemplateInfo\n        """
        self.Name = None
        self.AttachedInputs = None
        self.OutputGroups = None
        self.AudioTemplates = None
        self.VideoTemplates = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("AttachedInputs") is not None:
            self.AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInputInfo()
                obj._deserialize(item)
                self.AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self.OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = OutputGroupsInfo()
                obj._deserialize(item)
                self.OutputGroups.append(obj)
        if params.get("AudioTemplates") is not None:
            self.AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self.AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self.VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self.VideoTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaLiveChannelResponse(AbstractModel):
    """CreateMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.\n        :type Id: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateMediaLiveInputRequest(AbstractModel):
    """CreateMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Name: Media input name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.\n        :type Name: str\n        :param Type: Media input type.
Valid values: RTMP_PUSH/RTP_PUSH/UDP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL.\n        :type Type: str\n        :param SecurityGroupIds: ID of the input security group to be bound.
Only one security group can be associated.\n        :type SecurityGroupIds: list of str\n        :param InputSettings: Input settings information, one or two sets of which need to be configured for RTMP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL.\n        :type InputSettings: list of InputSettingInfo\n        """
        self.Name = None
        self.Type = None
        self.SecurityGroupIds = None
        self.InputSettings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InputSettings") is not None:
            self.InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self.InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaLiveInputResponse(AbstractModel):
    """CreateMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.\n        :type Id: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateMediaLiveInputSecurityGroupRequest(AbstractModel):
    """CreateMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Name: Input security group name, which can contain letters, digits, and underscores and must be unique at the region level.\n        :type Name: str\n        :param Whitelist: List of allowlist entries. Quantity limit: [1,10].\n        :type Whitelist: list of str\n        """
        self.Name = None
        self.Whitelist = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMediaLiveInputSecurityGroupResponse(AbstractModel):
    """CreateMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param Id: Security group ID.\n        :type Id: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class DashRemuxSettingsInfo(AbstractModel):
    """DASH configuration information.

    """

    def __init__(self):
        """
        :param SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.\n        :type SegmentDuration: int\n        :param SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.\n        :type SegmentNumber: int\n        :param PeriodTriggers: Whether to enable multi-period. Valid values: CLOSE/OPEN. Default value: CLOSE.\n        :type PeriodTriggers: str\n        """
        self.SegmentDuration = None
        self.SegmentNumber = None
        self.PeriodTriggers = None


    def _deserialize(self, params):
        self.SegmentDuration = params.get("SegmentDuration")
        self.SegmentNumber = params.get("SegmentNumber")
        self.PeriodTriggers = params.get("PeriodTriggers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaLiveChannelRequest(AbstractModel):
    """DeleteMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaLiveChannelResponse(AbstractModel):
    """DeleteMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaLiveInputRequest(AbstractModel):
    """DeleteMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaLiveInputResponse(AbstractModel):
    """DeleteMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMediaLiveInputSecurityGroupRequest(AbstractModel):
    """DeleteMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMediaLiveInputSecurityGroupResponse(AbstractModel):
    """DeleteMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveChannelAlertsRequest(AbstractModel):
    """DescribeMediaLiveChannelAlerts request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.\n        :type ChannelId: str\n        """
        self.ChannelId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveChannelAlertsResponse(AbstractModel):
    """DescribeMediaLiveChannelAlerts response structure.

    """

    def __init__(self):
        """
        :param Infos: Alarm information of two pipelines under this channel.\n        :type Infos: :class:`tencentcloud.mdl.v20200326.models.ChannelAlertInfos`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = ChannelAlertInfos()
            self.Infos._deserialize(params.get("Infos"))
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveChannelInputStatisticsRequest(AbstractModel):
    """DescribeMediaLiveChannelInputStatistics request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.\n        :type ChannelId: str\n        :param StartTime: Statistics start time, which is one hour ago by default. Maximum value: the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`.\n        :type StartTime: str\n        :param EndTime: Statistics end time, which is one hour after `StartTime` by default.
UTC time, such as `2020-01-01T12:00:00Z`.\n        :type EndTime: str\n        :param Period: Data interval. Valid values: 5s, 1min, 5min, 15min. Default value: 1min.\n        :type Period: str\n        """
        self.ChannelId = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveChannelInputStatisticsResponse(AbstractModel):
    """DescribeMediaLiveChannelInputStatistics response structure.

    """

    def __init__(self):
        """
        :param Infos: Channel input statistics array.\n        :type Infos: list of ChannelInputStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = ChannelInputStatistics()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveChannelLogsRequest(AbstractModel):
    """DescribeMediaLiveChannelLogs request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.\n        :type ChannelId: str\n        :param StartTime: Log start time, which is one hour ago by default. Maximum value: the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`.\n        :type StartTime: str\n        :param EndTime: Log end time, which is one hour after `StartTime` by default.
UTC time, such as `2020-01-01T12:00:00Z`.\n        :type EndTime: str\n        """
        self.ChannelId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveChannelLogsResponse(AbstractModel):
    """DescribeMediaLiveChannelLogs response structure.

    """

    def __init__(self):
        """
        :param Infos: Pipeline push information.\n        :type Infos: :class:`tencentcloud.mdl.v20200326.models.PipelineLogInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = PipelineLogInfo()
            self.Infos._deserialize(params.get("Infos"))
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveChannelOutputStatisticsRequest(AbstractModel):
    """DescribeMediaLiveChannelOutputStatistics request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.\n        :type ChannelId: str\n        :param StartTime: Statistics start time, which is one hour ago by default. Maximum value: the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`.\n        :type StartTime: str\n        :param EndTime: Statistics end time, which is one hour after `StartTime` by default.
UTC time, such as `2020-01-01T12:00:00Z`.\n        :type EndTime: str\n        :param Period: Data interval. Valid values: 5s, 1min, 5min, 15min. Default value: 1min.\n        :type Period: str\n        """
        self.ChannelId = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveChannelOutputStatisticsResponse(AbstractModel):
    """DescribeMediaLiveChannelOutputStatistics response structure.

    """

    def __init__(self):
        """
        :param Infos: Channel output information.\n        :type Infos: list of ChannelOutputsStatistics\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = ChannelOutputsStatistics()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveChannelRequest(AbstractModel):
    """DescribeMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveChannelResponse(AbstractModel):
    """DescribeMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param Info: Channel information.\n        :type Info: :class:`tencentcloud.mdl.v20200326.models.ChannelInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = ChannelInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveChannelsRequest(AbstractModel):
    """DescribeMediaLiveChannels request structure.

    """


class DescribeMediaLiveChannelsResponse(AbstractModel):
    """DescribeMediaLiveChannels response structure.

    """

    def __init__(self):
        """
        :param Infos: Channel list information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Infos: list of ChannelInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = ChannelInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveInputRequest(AbstractModel):
    """DescribeMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveInputResponse(AbstractModel):
    """DescribeMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param Info: MediaLive input information.\n        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = InputInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveInputSecurityGroupRequest(AbstractModel):
    """DescribeMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveInputSecurityGroupResponse(AbstractModel):
    """DescribeMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param Info: Input security group information.\n        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputSecurityGroupInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = InputSecurityGroupInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveInputSecurityGroupsRequest(AbstractModel):
    """DescribeMediaLiveInputSecurityGroups request structure.

    """


class DescribeMediaLiveInputSecurityGroupsResponse(AbstractModel):
    """DescribeMediaLiveInputSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Infos: Input security group information list.\n        :type Infos: list of InputSecurityGroupInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = InputSecurityGroupInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaLiveInputsRequest(AbstractModel):
    """DescribeMediaLiveInputs request structure.

    """


class DescribeMediaLiveInputsResponse(AbstractModel):
    """DescribeMediaLiveInputs response structure.

    """

    def __init__(self):
        """
        :param Infos: MediaLive input information list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Infos: list of InputInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = InputInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DestinationInfo(AbstractModel):
    """Relay destination address.

    """

    def __init__(self):
        """
        :param OutputUrl: Relay destination address. Length limit: [1,512].\n        :type OutputUrl: str\n        :param AuthKey: Authentication key. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AuthKey: str\n        :param Username: Authentication username. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Username: str\n        :param Password: Authentication password. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Password: str\n        """
        self.OutputUrl = None
        self.AuthKey = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.OutputUrl = params.get("OutputUrl")
        self.AuthKey = params.get("AuthKey")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmKey(AbstractModel):
    """Custom DRM key.

    """

    def __init__(self):
        """
        :param Key: DRM key, which is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.\n        :type Key: str\n        :param Track: Required for Widevine encryption. Valid values: SD, HD, UHD1, UHD2, AUDIO, ALL.
ALL refers to all tracks. If this parameter is set to ALL, no other tracks can be added.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Track: str\n        :param KeyId: Required for Widevine encryption. It is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type KeyId: str\n        :param Iv: Required when FairPlay uses the AES encryption method. It is a 32-bit hexadecimal string.
For more information about this parameter, please see: 
https://tools.ietf.org/html/rfc3826
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Iv: str\n        """
        self.Key = None
        self.Track = None
        self.KeyId = None
        self.Iv = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Track = params.get("Track")
        self.KeyId = params.get("KeyId")
        self.Iv = params.get("Iv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmSettingsInfo(AbstractModel):
    """DRM configuration information, which takes effect only for HLS and DASH.

    """

    def __init__(self):
        """
        :param State: Whether to enable DRM encryption. Valid value: CLOSE/OPEN. Default value: CLOSE.
Currently, this is supported only for HLS/DASH/HLS_ARCHIVE/DASH_ARCHIVE.\n        :type State: str\n        :param ContentId: When `Scheme` is set to TencentDRM, this parameter should be set to the `ContentId` of DRM encryption, and if this parameter is left empty, a `ContentId` will be automatically created. For more information, please see [here](https://intl.cloud.tencent.com/document/product/1000/40960?from_cn_redirect=1).
When `Scheme` is set to CustomDRMKeys, this parameter is required and should be specified by the user.\n        :type ContentId: str\n        :param Scheme: Valid values: TencentDRM, CustomDRMKeys. If this parameter is left empty, TencentDRM will be used by default.
TencentDRM refers to Tencent digital rights management (DRM) encryption. For more information, please see [here](https://intl.cloud.tencent.com/solution/drm?from_cn_redirect=1).
CustomDRMKeys refers to an encryption key customized by the user.\n        :type Scheme: str\n        :param Keys: The key customized by the content user, which is required when `Scheme` is set to CustomDRMKeys.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Keys: list of DrmKey\n        """
        self.State = None
        self.ContentId = None
        self.Scheme = None
        self.Keys = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.ContentId = params.get("ContentId")
        self.Scheme = params.get("Scheme")
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = DrmKey()
                obj._deserialize(item)
                self.Keys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HlsRemuxSettingsInfo(AbstractModel):
    """HLS protocol configuration.

    """

    def __init__(self):
        """
        :param SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.\n        :type SegmentDuration: int\n        :param SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.\n        :type SegmentNumber: int\n        :param PdtInsertion: Whether to enable PDT insertion. Valid values: CLOSE/OPEN. Default value: CLOSE.\n        :type PdtInsertion: str\n        :param PdtDuration: PDT duration in seconds. Value range: (0,3000]. Default value: 600.\n        :type PdtDuration: int\n        """
        self.SegmentDuration = None
        self.SegmentNumber = None
        self.PdtInsertion = None
        self.PdtDuration = None


    def _deserialize(self, params):
        self.SegmentDuration = params.get("SegmentDuration")
        self.SegmentNumber = params.get("SegmentNumber")
        self.PdtInsertion = params.get("PdtInsertion")
        self.PdtDuration = params.get("PdtDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """Input information.

    """

    def __init__(self):
        """
        :param Region: Input region.\n        :type Region: str\n        :param Id: Input ID.\n        :type Id: str\n        :param Name: Input name.\n        :type Name: str\n        :param Type: Input type.\n        :type Type: str\n        :param SecurityGroupIds: Array of security groups associated with input.\n        :type SecurityGroupIds: list of str\n        :param AttachedChannels: Array of channels associated with input.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AttachedChannels: list of str\n        :param InputSettings: Input configuration array.\n        :type InputSettings: list of InputSettingInfo\n        """
        self.Region = None
        self.Id = None
        self.Name = None
        self.Type = None
        self.SecurityGroupIds = None
        self.AttachedChannels = None
        self.InputSettings = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.AttachedChannels = params.get("AttachedChannels")
        if params.get("InputSettings") is not None:
            self.InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self.InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputSecurityGroupInfo(AbstractModel):
    """Input security group information.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.\n        :type Id: str\n        :param Name: Input security group name.\n        :type Name: str\n        :param Whitelist: List of allowlist entries.\n        :type Whitelist: list of str\n        :param OccupiedInputs: List of bound input streams.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OccupiedInputs: list of str\n        :param Region: Input security group address.\n        :type Region: str\n        """
        self.Id = None
        self.Name = None
        self.Whitelist = None
        self.OccupiedInputs = None
        self.Region = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Whitelist = params.get("Whitelist")
        self.OccupiedInputs = params.get("OccupiedInputs")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputSettingInfo(AbstractModel):
    """Input settings information.

    """

    def __init__(self):
        """
        :param AppName: Application name, which is used for RTMP_PUSH and can contain 1-32 letters and digits.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AppName: str\n        :param StreamName: Stream name, which is used for RTMP_PUSH and can contain 1-32 letters and digits.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StreamName: str\n        :param SourceUrl: Origin-pull URL, which is used for RTMP_PULL/HLS_PULL/MP4_PULL. Length limit: [1,512].
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SourceUrl: str\n        :param InputAddress: RTP/UDP input address, which does not need to be entered for the input parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InputAddress: str\n        """
        self.AppName = None
        self.StreamName = None
        self.SourceUrl = None
        self.InputAddress = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.SourceUrl = params.get("SourceUrl")
        self.InputAddress = params.get("InputAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputStatistics(AbstractModel):
    """Input statistics.

    """

    def __init__(self):
        """
        :param Pipeline0: Input statistics of pipeline 0.\n        :type Pipeline0: list of PipelineInputStatistics\n        :param Pipeline1: Input statistics of pipeline 1.\n        :type Pipeline1: list of PipelineInputStatistics\n        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = PipelineInputStatistics()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = PipelineInputStatistics()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """Log information.

    """

    def __init__(self):
        """
        :param Type: Log type.
It contains the value of `StreamStart` which refers to the push information.\n        :type Type: str\n        :param Time: Time when the log is printed.\n        :type Time: str\n        :param Message: Log details.\n        :type Message: :class:`tencentcloud.mdl.v20200326.models.LogMessageInfo`\n        """
        self.Type = None
        self.Time = None
        self.Message = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Time = params.get("Time")
        if params.get("Message") is not None:
            self.Message = LogMessageInfo()
            self.Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogMessageInfo(AbstractModel):
    """Log details.

    """

    def __init__(self):
        """
        :param StreamInfo: Push information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type StreamInfo: :class:`tencentcloud.mdl.v20200326.models.StreamInfo`\n        """
        self.StreamInfo = None


    def _deserialize(self, params):
        if params.get("StreamInfo") is not None:
            self.StreamInfo = StreamInfo()
            self.StreamInfo._deserialize(params.get("StreamInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaPackageSettingsInfo(AbstractModel):
    """Configuration information related to associating with the media packaging service.

    """

    def __init__(self):
        """
        :param Id: Media packaging ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMediaLiveChannelRequest(AbstractModel):
    """ModifyMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.\n        :type Id: str\n        :param Name: Channel name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.\n        :type Name: str\n        :param AttachedInputs: Associated media input. Quantity limit: [1,1].\n        :type AttachedInputs: list of AttachedInputInfo\n        :param OutputGroups: Configuration information of channel output groups. Quantity limit: [1,10].\n        :type OutputGroups: list of OutputGroupsInfo\n        :param AudioTemplates: Audio transcoding template array. Quantity limit: [1,20].\n        :type AudioTemplates: list of AudioTemplateInfo\n        :param VideoTemplates: Video transcoding template array. Quantity limit: [1,10].\n        :type VideoTemplates: list of VideoTemplateInfo\n        """
        self.Id = None
        self.Name = None
        self.AttachedInputs = None
        self.OutputGroups = None
        self.AudioTemplates = None
        self.VideoTemplates = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("AttachedInputs") is not None:
            self.AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInputInfo()
                obj._deserialize(item)
                self.AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self.OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = OutputGroupsInfo()
                obj._deserialize(item)
                self.OutputGroups.append(obj)
        if params.get("AudioTemplates") is not None:
            self.AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self.AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self.VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self.VideoTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMediaLiveChannelResponse(AbstractModel):
    """ModifyMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaLiveInputRequest(AbstractModel):
    """ModifyMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.\n        :type Id: str\n        :param Name: Media input name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.\n        :type Name: str\n        :param SecurityGroupIds: List of IDs of bound security groups.\n        :type SecurityGroupIds: list of str\n        :param InputSettings: Input settings information.
One or two sets of settings need to be configured for RTMP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL.
This parameter can be left empty for RTP_PUSH and UDP_PUSH.
Note: if it is left empty or the array is empty, the original `InputSettings` value will be used.\n        :type InputSettings: list of InputSettingInfo\n        """
        self.Id = None
        self.Name = None
        self.SecurityGroupIds = None
        self.InputSettings = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InputSettings") is not None:
            self.InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self.InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMediaLiveInputResponse(AbstractModel):
    """ModifyMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMediaLiveInputSecurityGroupRequest(AbstractModel):
    """ModifyMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.\n        :type Id: str\n        :param Name: Input security group name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.\n        :type Name: str\n        :param Whitelist: List of allowlist entries. Up to 10 entries are allowed.\n        :type Whitelist: list of str\n        """
        self.Id = None
        self.Name = None
        self.Whitelist = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMediaLiveInputSecurityGroupResponse(AbstractModel):
    """ModifyMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OutputGroupsInfo(AbstractModel):
    """Channel output group information.

    """

    def __init__(self):
        """
        :param Name: Channel output group name, which can contain 1–32 letters, digits, and underscores and must be unique at the channel level.\n        :type Name: str\n        :param Type: Output protocol type.
Valid values: HLS, DASH, HLS_ARCHIVE, HLS_MEDIA_PACKAGE, DASH_MEDIA_PACKAGE.\n        :type Type: str\n        :param Outputs: Output information.
Quantity limit: [1,1] for RTMP/RTP; [1,10] for HLS/DASH.\n        :type Outputs: list of OutputInfo\n        :param Destinations: Relay destination address. Quantity limit: [1,2].\n        :type Destinations: list of DestinationInfo\n        :param HlsRemuxSettings: HLS protocol configuration information, which takes effect only for HLS/HLS_ARCHIVE.\n        :type HlsRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.HlsRemuxSettingsInfo`\n        :param DashRemuxSettings: DASH protocol configuration information, which takes effect only for DASH/DSAH_ARCHIVE.\n        :type DashRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.DashRemuxSettingsInfo`\n        :param DrmSettings: DRM configuration information.\n        :type DrmSettings: :class:`tencentcloud.mdl.v20200326.models.DrmSettingsInfo`\n        :param MediaPackageSettings: Configuration information of media packaging, which is required when `Type` is set to MediaPackage.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MediaPackageSettings: :class:`tencentcloud.mdl.v20200326.models.MediaPackageSettingsInfo`\n        """
        self.Name = None
        self.Type = None
        self.Outputs = None
        self.Destinations = None
        self.HlsRemuxSettings = None
        self.DashRemuxSettings = None
        self.DrmSettings = None
        self.MediaPackageSettings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("Outputs") is not None:
            self.Outputs = []
            for item in params.get("Outputs"):
                obj = OutputInfo()
                obj._deserialize(item)
                self.Outputs.append(obj)
        if params.get("Destinations") is not None:
            self.Destinations = []
            for item in params.get("Destinations"):
                obj = DestinationInfo()
                obj._deserialize(item)
                self.Destinations.append(obj)
        if params.get("HlsRemuxSettings") is not None:
            self.HlsRemuxSettings = HlsRemuxSettingsInfo()
            self.HlsRemuxSettings._deserialize(params.get("HlsRemuxSettings"))
        if params.get("DashRemuxSettings") is not None:
            self.DashRemuxSettings = DashRemuxSettingsInfo()
            self.DashRemuxSettings._deserialize(params.get("DashRemuxSettings"))
        if params.get("DrmSettings") is not None:
            self.DrmSettings = DrmSettingsInfo()
            self.DrmSettings._deserialize(params.get("DrmSettings"))
        if params.get("MediaPackageSettings") is not None:
            self.MediaPackageSettings = MediaPackageSettingsInfo()
            self.MediaPackageSettings._deserialize(params.get("MediaPackageSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputInfo(AbstractModel):
    """Output information.

    """

    def __init__(self):
        """
        :param Name: Output name.\n        :type Name: str\n        :param AudioTemplateNames: Audio transcoding template name array.
Quantity limit: [0,1] for RTMP; [0,20] for others.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AudioTemplateNames: list of str\n        :param VideoTemplateNames: Video transcoding template name array. Quantity limit: [0,1].
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VideoTemplateNames: list of str\n        :param Scte35Settings: SCTE-35 information configuration.\n        :type Scte35Settings: :class:`tencentcloud.mdl.v20200326.models.Scte35SettingsInfo`\n        """
        self.Name = None
        self.AudioTemplateNames = None
        self.VideoTemplateNames = None
        self.Scte35Settings = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AudioTemplateNames = params.get("AudioTemplateNames")
        self.VideoTemplateNames = params.get("VideoTemplateNames")
        if params.get("Scte35Settings") is not None:
            self.Scte35Settings = Scte35SettingsInfo()
            self.Scte35Settings._deserialize(params.get("Scte35Settings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputsStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        """
        :param Pipeline0: Output information of pipeline 0.\n        :type Pipeline0: list of PipelineOutputStatistics\n        :param Pipeline1: Output information of pipeline 1.\n        :type Pipeline1: list of PipelineOutputStatistics\n        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = PipelineOutputStatistics()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = PipelineOutputStatistics()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineInputStatistics(AbstractModel):
    """Pipeline input statistics.

    """

    def __init__(self):
        """
        :param Timestamp: Data timestamp in seconds.\n        :type Timestamp: int\n        :param NetworkIn: Input bandwidth in bps.\n        :type NetworkIn: int\n        :param Video: Video information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input video.
For other inputs, the quantity is 1.\n        :type Video: list of VideoPipelineInputStatistics\n        :param Audio: Audio information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input audio.
For other inputs, the quantity is 1.\n        :type Audio: list of AudioPipelineInputStatistics\n        """
        self.Timestamp = None
        self.NetworkIn = None
        self.Video = None
        self.Audio = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.NetworkIn = params.get("NetworkIn")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = VideoPipelineInputStatistics()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = AudioPipelineInputStatistics()
                obj._deserialize(item)
                self.Audio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineLogInfo(AbstractModel):
    """Pipeline log information.

    """

    def __init__(self):
        """
        :param Pipeline0: Log information of pipeline 0.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Pipeline0: list of LogInfo\n        :param Pipeline1: Log information of pipeline 1.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Pipeline1: list of LogInfo\n        """
        self.Pipeline0 = None
        self.Pipeline1 = None


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self.Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self.Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = LogInfo()
                obj._deserialize(item)
                self.Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineOutputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        """
        :param Timestamp: Timestamp.
In seconds, indicating data time.\n        :type Timestamp: int\n        :param NetworkOut: Output bandwidth in bps.\n        :type NetworkOut: int\n        """
        self.Timestamp = None
        self.NetworkOut = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.NetworkOut = params.get("NetworkOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Scte35SettingsInfo(AbstractModel):
    """SCTE-35 configuration information.

    """

    def __init__(self):
        """
        :param Behavior: Whether to pass through SCTE-35 information. Valid values: NO_PASSTHROUGH/PASSTHROUGH. Default value: NO_PASSTHROUGH.\n        :type Behavior: str\n        """
        self.Behavior = None


    def _deserialize(self, params):
        self.Behavior = params.get("Behavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMediaLiveChannelRequest(AbstractModel):
    """StartMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartMediaLiveChannelResponse(AbstractModel):
    """StartMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMediaLiveChannelRequest(AbstractModel):
    """StopMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.\n        :type Id: str\n        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopMediaLiveChannelResponse(AbstractModel):
    """StopMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamAudioInfo(AbstractModel):
    """Audio information.

    """

    def __init__(self):
        """
        :param Pid: Audio `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Pid: int\n        :param Codec: Audio codec.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Codec: str\n        :param Fps: Audio frame rate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Fps: int\n        :param Rate: Audio bitrate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Rate: int\n        :param SampleRate: Audio sample rate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SampleRate: int\n        """
        self.Pid = None
        self.Codec = None
        self.Fps = None
        self.Rate = None
        self.SampleRate = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamInfo(AbstractModel):
    """Push information.

    """

    def __init__(self):
        """
        :param ClientIp: Client IP.\n        :type ClientIp: str\n        :param Video: Video information of pushed streams.\n        :type Video: list of StreamVideoInfo\n        :param Audio: Audio information of pushed streams.\n        :type Audio: list of StreamAudioInfo\n        :param Scte35: SCTE-35 information of pushed streams.\n        :type Scte35: list of StreamScte35Info\n        """
        self.ClientIp = None
        self.Video = None
        self.Audio = None
        self.Scte35 = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        if params.get("Video") is not None:
            self.Video = []
            for item in params.get("Video"):
                obj = StreamVideoInfo()
                obj._deserialize(item)
                self.Video.append(obj)
        if params.get("Audio") is not None:
            self.Audio = []
            for item in params.get("Audio"):
                obj = StreamAudioInfo()
                obj._deserialize(item)
                self.Audio.append(obj)
        if params.get("Scte35") is not None:
            self.Scte35 = []
            for item in params.get("Scte35"):
                obj = StreamScte35Info()
                obj._deserialize(item)
                self.Scte35.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamScte35Info(AbstractModel):
    """SCTE-35 information.

    """

    def __init__(self):
        """
        :param Pid: SCTE-35 `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Pid: int\n        """
        self.Pid = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamVideoInfo(AbstractModel):
    """Video information of pushed streams.

    """

    def __init__(self):
        """
        :param Pid: Video `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Pid: int\n        :param Codec: Video codec.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Codec: str\n        :param Fps: Video frame rate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Fps: int\n        :param Rate: Video bitrate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Rate: int\n        :param Width: Video width.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Width: int\n        :param Height: Video height.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Height: int\n        """
        self.Pid = None
        self.Codec = None
        self.Fps = None
        self.Rate = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Rate = params.get("Rate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoPipelineInputStatistics(AbstractModel):
    """Pipeline input video statistics.

    """

    def __init__(self):
        """
        :param Fps: Video FPS.\n        :type Fps: int\n        :param Rate: Video bitrate in bps.\n        :type Rate: int\n        :param Pid: Video `Pid`, which is available only if the input is `rtp/udp`.\n        :type Pid: int\n        """
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
        


class VideoTemplateInfo(AbstractModel):
    """Video transcoding template.

    """

    def __init__(self):
        """
        :param Name: Video transcoding template name, which can contain 1-20 letters and digits.\n        :type Name: str\n        :param Vcodec: Video codec. Valid values: H264/H265. If this parameter is left empty, the original value will be used.\n        :type Vcodec: str\n        :param VideoBitrate: Video bitrate. Value range: [50000,40000000]. The value can only be a multiple of 1,000. If this parameter is left empty, the original value will be used.\n        :type VideoBitrate: int\n        :param Width: Video width. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.\n        :type Width: int\n        :param Height: Video height. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.\n        :type Height: int\n        :param Fps: Video frame rate. Value range: [1,240]. If this parameter is left empty, the original value will be used.\n        :type Fps: int\n        :param TopSpeed: Whether to enable top speed codec. Valid value: CLOSE/OPEN. Default value: CLOSE.\n        :type TopSpeed: str\n        :param BitrateCompressionRatio: Top speed codec compression ratio. Value range: [0,50]. The lower the compression ratio, the higher the image quality.\n        :type BitrateCompressionRatio: int\n        """
        self.Name = None
        self.Vcodec = None
        self.VideoBitrate = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.TopSpeed = None
        self.BitrateCompressionRatio = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Vcodec = params.get("Vcodec")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.TopSpeed = params.get("TopSpeed")
        self.BitrateCompressionRatio = params.get("BitrateCompressionRatio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        