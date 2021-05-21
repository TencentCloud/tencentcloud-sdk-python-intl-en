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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AttachedInputInfo(AbstractModel):
    """Media input associated with media channel.

    """

    def __init__(self):
        """
        :param Id: Media input ID.
        :type Id: str
        :param AudioSelectors: Audio selector for media input. Quantity limit: [0,20]
Note: this field may return null, indicating that no valid values can be obtained.
        :type AudioSelectors: list of AudioSelectorInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AudioPidSelectionInfo(AbstractModel):
    """Audio `Pid` selection.

    """

    def __init__(self):
        """
        :param Pid: Audio `Pid`. Default value: 0.
        :type Pid: int
        """
        self.Pid = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AudioPipelineInputStatistics(AbstractModel):
    """Pipeline input audio statistics.

    """

    def __init__(self):
        """
        :param Fps: Audio FPS.
        :type Fps: int
        :param Rate: Audio bitrate in bps.
        :type Rate: int
        :param Pid: Audio `Pid`, which is available only if the input is `rtp/udp`.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AudioSelectorInfo(AbstractModel):
    """Audio selector.

    """

    def __init__(self):
        """
        :param Name: Audio name, which can contain 1-32 letters, digits, and underscores.
        :type Name: str
        :param AudioPidSelection: Audio `Pid` selection.
        :type AudioPidSelection: :class:`tencentcloud.mdl.v20200326.models.AudioPidSelectionInfo`
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AudioTemplateInfo(AbstractModel):
    """Audio transcoding template.

    """

    def __init__(self):
        """
        :param AudioSelectorName: Only `AttachedInputs.AudioSelectors.Name` can be selected. This parameter is required for RTP_PUSH and UDP_PUSH.
        :type AudioSelectorName: str
        :param Name: Audio transcoding template name, which can contain 1-20 letters and digits.
        :type Name: str
        :param Acodec: Audio codec. Valid value: AAC. Default value: AAC.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. If this parameter is left empty, the original value will be used.
Valid values: 6000, 7000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000
        :type AudioBitrate: int
        :param LanguageCode: Audio language code, whose length is always 3 characters.
        :type LanguageCode: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChannelAlertInfos(AbstractModel):
    """Channel alarm information.

    """

    def __init__(self):
        """
        :param Pipeline0: Alarm details of pipeline 0 under this channel.
        :type Pipeline0: list of ChannelPipelineAlerts
        :param Pipeline1: Alarm details of pipeline 1 under this channel.
        :type Pipeline1: list of ChannelPipelineAlerts
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChannelInfo(AbstractModel):
    """Channel information.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param State: Channel status.
        :type State: str
        :param AttachedInputs: Information of associated input.
        :type AttachedInputs: list of AttachedInputInfo
        :param OutputGroups: Information of output group.
        :type OutputGroups: list of OutputGroupsInfo
        :param Name: Channel name.
        :type Name: str
        :param AudioTemplates: Audio transcoding template array.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AudioTemplates: list of AudioTemplateInfo
        :param VideoTemplates: Video transcoding template array.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoTemplates: list of VideoTemplateInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChannelInputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        """
        :param InputId: Input ID.
        :type InputId: str
        :param Statistics: Input statistics.
        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.InputStatistics`
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChannelOutputsStatistics(AbstractModel):
    """Channel output information.

    """

    def __init__(self):
        """
        :param OutputGroupName: Output group name.
        :type OutputGroupName: str
        :param Statistics: Output group statistics.
        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.OutputsStatistics`
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ChannelPipelineAlerts(AbstractModel):
    """Channel alarm details.

    """

    def __init__(self):
        """
        :param SetTime: Alarm start time in UTC time.
        :type SetTime: str
        :param ClearTime: Alarm end time in UTC time.
This time is available only after the alarm ends.
        :type ClearTime: str
        :param Type: Alarm type.
        :type Type: str
        :param Message: Alarm details.
        :type Message: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMediaLiveChannelRequest(AbstractModel):
    """CreateMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Name: Channel name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.
        :type Name: str
        :param AttachedInputs: Associated media input. Quantity limit: [1,1].
        :type AttachedInputs: list of AttachedInputInfo
        :param OutputGroups: Configuration information of channel output groups. Quantity limit: [1,10].
        :type OutputGroups: list of OutputGroupsInfo
        :param AudioTemplates: Audio transcoding template array. Quantity limit: [1,20].
        :type AudioTemplates: list of AudioTemplateInfo
        :param VideoTemplates: Video transcoding template array. Quantity limit: [1,10].
        :type VideoTemplates: list of VideoTemplateInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMediaLiveChannelResponse(AbstractModel):
    """CreateMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMediaLiveInputRequest(AbstractModel):
    """CreateMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Name: Media input name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.
        :type Name: str
        :param Type: Media input type.
Valid values: RTMP_PUSH/RTP_PUSH/UDP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL.
        :type Type: str
        :param SecurityGroupIds: ID of the input security group to be bound.
Only one security group can be associated.
        :type SecurityGroupIds: list of str
        :param InputSettings: Input settings information, one or two sets of which need to be configured for RTMP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL.
        :type InputSettings: list of InputSettingInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMediaLiveInputResponse(AbstractModel):
    """CreateMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMediaLiveInputSecurityGroupRequest(AbstractModel):
    """CreateMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Name: Input security group name, which can contain letters, digits, and underscores and must be unique at the region level.
        :type Name: str
        :param Whitelist: List of allowlist entries. Quantity limit: [1,10].
        :type Whitelist: list of str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateMediaLiveInputSecurityGroupResponse(AbstractModel):
    """CreateMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param Id: Security group ID.
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DashRemuxSettingsInfo(AbstractModel):
    """DASH configuration information.

    """

    def __init__(self):
        """
        :param SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.
        :type SegmentDuration: int
        :param SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.
        :type SegmentNumber: int
        :param PeriodTriggers: Whether to enable multi-period. Valid values: CLOSE/OPEN. Default value: CLOSE.
        :type PeriodTriggers: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMediaLiveChannelRequest(AbstractModel):
    """DeleteMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMediaLiveChannelResponse(AbstractModel):
    """DeleteMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMediaLiveInputRequest(AbstractModel):
    """DeleteMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMediaLiveInputResponse(AbstractModel):
    """DeleteMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMediaLiveInputSecurityGroupRequest(AbstractModel):
    """DeleteMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteMediaLiveInputSecurityGroupResponse(AbstractModel):
    """DeleteMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelAlertsRequest(AbstractModel):
    """DescribeMediaLiveChannelAlerts request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.
        :type ChannelId: str
        """
        self.ChannelId = None


    def _deserialize(self, params):
        self.ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelAlertsResponse(AbstractModel):
    """DescribeMediaLiveChannelAlerts response structure.

    """

    def __init__(self):
        """
        :param Infos: Alarm information of two pipelines under this channel.
        :type Infos: :class:`tencentcloud.mdl.v20200326.models.ChannelAlertInfos`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = ChannelAlertInfos()
            self.Infos._deserialize(params.get("Infos"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelInputStatisticsRequest(AbstractModel):
    """DescribeMediaLiveChannelInputStatistics request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.
        :type ChannelId: str
        :param StartTime: Statistics start time, which is one hour ago by default. Maximum value: the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param EndTime: Statistics end time, which is one hour after `StartTime` by default.
UTC time, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param Period: Data interval. Valid values: 5s, 1min, 5min, 15min. Default value: 1min.
        :type Period: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelInputStatisticsResponse(AbstractModel):
    """DescribeMediaLiveChannelInputStatistics response structure.

    """

    def __init__(self):
        """
        :param Infos: Channel input statistics array.
        :type Infos: list of ChannelInputStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelLogsRequest(AbstractModel):
    """DescribeMediaLiveChannelLogs request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.
        :type ChannelId: str
        :param StartTime: Log start time, which is one hour ago by default. Maximum value: the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param EndTime: Log end time, which is one hour after `StartTime` by default.
UTC time, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelLogsResponse(AbstractModel):
    """DescribeMediaLiveChannelLogs response structure.

    """

    def __init__(self):
        """
        :param Infos: Pipeline push information.
        :type Infos: :class:`tencentcloud.mdl.v20200326.models.PipelineLogInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self.Infos = PipelineLogInfo()
            self.Infos._deserialize(params.get("Infos"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelOutputStatisticsRequest(AbstractModel):
    """DescribeMediaLiveChannelOutputStatistics request structure.

    """

    def __init__(self):
        """
        :param ChannelId: Channel ID.
        :type ChannelId: str
        :param StartTime: Statistics start time, which is one hour ago by default. Maximum value: the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`.
        :type StartTime: str
        :param EndTime: Statistics end time, which is one hour after `StartTime` by default.
UTC time, such as `2020-01-01T12:00:00Z`.
        :type EndTime: str
        :param Period: Data interval. Valid values: 5s, 1min, 5min, 15min. Default value: 1min.
        :type Period: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelOutputStatisticsResponse(AbstractModel):
    """DescribeMediaLiveChannelOutputStatistics response structure.

    """

    def __init__(self):
        """
        :param Infos: Channel output information.
        :type Infos: list of ChannelOutputsStatistics
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelRequest(AbstractModel):
    """DescribeMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelResponse(AbstractModel):
    """DescribeMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param Info: Channel information.
        :type Info: :class:`tencentcloud.mdl.v20200326.models.ChannelInfo`
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveChannelsRequest(AbstractModel):
    """DescribeMediaLiveChannels request structure.

    """


class DescribeMediaLiveChannelsResponse(AbstractModel):
    """DescribeMediaLiveChannels response structure.

    """

    def __init__(self):
        """
        :param Infos: Channel list information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Infos: list of ChannelInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveInputRequest(AbstractModel):
    """DescribeMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveInputResponse(AbstractModel):
    """DescribeMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param Info: MediaLive input information.
        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = InputInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveInputSecurityGroupRequest(AbstractModel):
    """DescribeMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveInputSecurityGroupResponse(AbstractModel):
    """DescribeMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param Info: Input security group information.
        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputSecurityGroupInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = InputSecurityGroupInfo()
            self.Info._deserialize(params.get("Info"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveInputSecurityGroupsRequest(AbstractModel):
    """DescribeMediaLiveInputSecurityGroups request structure.

    """


class DescribeMediaLiveInputSecurityGroupsResponse(AbstractModel):
    """DescribeMediaLiveInputSecurityGroups response structure.

    """

    def __init__(self):
        """
        :param Infos: Input security group information list.
        :type Infos: list of InputSecurityGroupInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMediaLiveInputsRequest(AbstractModel):
    """DescribeMediaLiveInputs request structure.

    """


class DescribeMediaLiveInputsResponse(AbstractModel):
    """DescribeMediaLiveInputs response structure.

    """

    def __init__(self):
        """
        :param Infos: MediaLive input information list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Infos: list of InputInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DestinationInfo(AbstractModel):
    """Relay destination address.

    """

    def __init__(self):
        """
        :param OutputUrl: Relay destination address. Length limit: [1,512].
        :type OutputUrl: str
        :param AuthKey: Authentication key. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthKey: str
        :param Username: Authentication username. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type Username: str
        :param Password: Authentication password. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type Password: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DrmKey(AbstractModel):
    """Custom DRM key.

    """

    def __init__(self):
        """
        :param Key: DRM key, which is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.
        :type Key: str
        :param Track: Required for Widevine encryption. Valid values: SD, HD, UHD1, UHD2, AUDIO, ALL.
ALL refers to all tracks. If this parameter is set to ALL, no other tracks can be added.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Track: str
        :param KeyId: Required for Widevine encryption. It is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param Iv: Required when FairPlay uses the AES encryption method. It is a 32-bit hexadecimal string.
For more information about this parameter, please see: 
https://tools.ietf.org/html/rfc3826
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Iv: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DrmSettingsInfo(AbstractModel):
    """DRM configuration information, which takes effect only for HLS and DASH.

    """

    def __init__(self):
        """
        :param State: Whether to enable DRM encryption. Valid value: CLOSE/OPEN. Default value: CLOSE.
Currently, this is supported only for HLS/DASH/HLS_ARCHIVE/DASH_ARCHIVE.
        :type State: str
        :param ContentId: When `Scheme` is set to TencentDRM, this parameter should be set to the `ContentId` of DRM encryption, and if this parameter is left empty, a `ContentId` will be automatically created. For more information, please see [here](https://intl.cloud.tencent.com/document/product/1000/40960?from_cn_redirect=1).
When `Scheme` is set to CustomDRMKeys, this parameter is required and should be specified by the user.
        :type ContentId: str
        :param Scheme: Valid values: TencentDRM, CustomDRMKeys. If this parameter is left empty, TencentDRM will be used by default.
TencentDRM refers to Tencent digital rights management (DRM) encryption. For more information, please see [here](https://intl.cloud.tencent.com/solution/drm?from_cn_redirect=1).
CustomDRMKeys refers to an encryption key customized by the user.
        :type Scheme: str
        :param Keys: The key customized by the content user, which is required when `Scheme` is set to CustomDRMKeys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Keys: list of DrmKey
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HlsRemuxSettingsInfo(AbstractModel):
    """HLS protocol configuration.

    """

    def __init__(self):
        """
        :param SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.
        :type SegmentDuration: int
        :param SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.
        :type SegmentNumber: int
        :param PdtInsertion: Whether to enable PDT insertion. Valid values: CLOSE/OPEN. Default value: CLOSE.
        :type PdtInsertion: str
        :param PdtDuration: PDT duration in seconds. Value range: (0,3000]. Default value: 600.
        :type PdtDuration: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InputInfo(AbstractModel):
    """Input information.

    """

    def __init__(self):
        """
        :param Region: Input region.
        :type Region: str
        :param Id: Input ID.
        :type Id: str
        :param Name: Input name.
        :type Name: str
        :param Type: Input type.
        :type Type: str
        :param SecurityGroupIds: Array of security groups associated with input.
        :type SecurityGroupIds: list of str
        :param AttachedChannels: Array of channels associated with input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedChannels: list of str
        :param InputSettings: Input configuration array.
        :type InputSettings: list of InputSettingInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InputSecurityGroupInfo(AbstractModel):
    """Input security group information.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.
        :type Id: str
        :param Name: Input security group name.
        :type Name: str
        :param Whitelist: List of allowlist entries.
        :type Whitelist: list of str
        :param OccupiedInputs: List of bound input streams.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OccupiedInputs: list of str
        :param Region: Input security group address.
        :type Region: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InputSettingInfo(AbstractModel):
    """Input settings information.

    """

    def __init__(self):
        """
        :param AppName: Application name, which is used for RTMP_PUSH and can contain 1-32 letters and digits.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppName: str
        :param StreamName: Stream name, which is used for RTMP_PUSH and can contain 1-32 letters and digits.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamName: str
        :param SourceUrl: Origin-pull URL, which is used for RTMP_PULL/HLS_PULL/MP4_PULL. Length limit: [1,512].
Note: this field may return null, indicating that no valid values can be obtained.
        :type SourceUrl: str
        :param InputAddress: RTP/UDP input address, which does not need to be entered for the input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InputAddress: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InputStatistics(AbstractModel):
    """Input statistics.

    """

    def __init__(self):
        """
        :param Pipeline0: Input statistics of pipeline 0.
        :type Pipeline0: list of PipelineInputStatistics
        :param Pipeline1: Input statistics of pipeline 1.
        :type Pipeline1: list of PipelineInputStatistics
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LogInfo(AbstractModel):
    """Log information.

    """

    def __init__(self):
        """
        :param Type: Log type.
It contains the value of `StreamStart` which refers to the push information.
        :type Type: str
        :param Time: Time when the log is printed.
        :type Time: str
        :param Message: Log details.
        :type Message: :class:`tencentcloud.mdl.v20200326.models.LogMessageInfo`
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LogMessageInfo(AbstractModel):
    """Log details.

    """

    def __init__(self):
        """
        :param StreamInfo: Push information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamInfo: :class:`tencentcloud.mdl.v20200326.models.StreamInfo`
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MediaPackageSettingsInfo(AbstractModel):
    """Configuration information related to associating with the media packaging service.

    """

    def __init__(self):
        """
        :param Id: Media packaging ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMediaLiveChannelRequest(AbstractModel):
    """ModifyMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
        :type Id: str
        :param Name: Channel name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.
        :type Name: str
        :param AttachedInputs: Associated media input. Quantity limit: [1,1].
        :type AttachedInputs: list of AttachedInputInfo
        :param OutputGroups: Configuration information of channel output groups. Quantity limit: [1,10].
        :type OutputGroups: list of OutputGroupsInfo
        :param AudioTemplates: Audio transcoding template array. Quantity limit: [1,20].
        :type AudioTemplates: list of AudioTemplateInfo
        :param VideoTemplates: Video transcoding template array. Quantity limit: [1,10].
        :type VideoTemplates: list of VideoTemplateInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMediaLiveChannelResponse(AbstractModel):
    """ModifyMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMediaLiveInputRequest(AbstractModel):
    """ModifyMediaLiveInput request structure.

    """

    def __init__(self):
        """
        :param Id: Media input ID.
        :type Id: str
        :param Name: Media input name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.
        :type Name: str
        :param SecurityGroupIds: List of IDs of bound security groups.
        :type SecurityGroupIds: list of str
        :param InputSettings: Input settings information.
One or two sets of settings need to be configured for RTMP_PUSH/RTMP_PULL/HLS_PULL/MP4_PULL.
This parameter can be left empty for RTP_PUSH and UDP_PUSH.
Note: if it is left empty or the array is empty, the original `InputSettings` value will be used.
        :type InputSettings: list of InputSettingInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMediaLiveInputResponse(AbstractModel):
    """ModifyMediaLiveInput response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMediaLiveInputSecurityGroupRequest(AbstractModel):
    """ModifyMediaLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        """
        :param Id: Input security group ID.
        :type Id: str
        :param Name: Input security group name, which can contain 1-32 letters, digits, and underscores and must be unique at the region level.
        :type Name: str
        :param Whitelist: List of allowlist entries. Up to 10 entries are allowed.
        :type Whitelist: list of str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyMediaLiveInputSecurityGroupResponse(AbstractModel):
    """ModifyMediaLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OutputGroupsInfo(AbstractModel):
    """Channel output group information.

    """

    def __init__(self):
        """
        :param Name: Channel output group name, which can contain 1–32 letters, digits, and underscores and must be unique at the channel level.
        :type Name: str
        :param Type: Output protocol type.
Valid values: HLS, DASH, HLS_ARCHIVE, HLS_MEDIA_PACKAGE, DASH_MEDIA_PACKAGE.
        :type Type: str
        :param Outputs: Output information.
Quantity limit: [1,1] for RTMP/RTP; [1,10] for HLS/DASH.
        :type Outputs: list of OutputInfo
        :param Destinations: Relay destination address. Quantity limit: [1,2].
        :type Destinations: list of DestinationInfo
        :param HlsRemuxSettings: HLS protocol configuration information, which takes effect only for HLS/HLS_ARCHIVE.
        :type HlsRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.HlsRemuxSettingsInfo`
        :param DashRemuxSettings: DASH protocol configuration information, which takes effect only for DASH/DSAH_ARCHIVE.
        :type DashRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.DashRemuxSettingsInfo`
        :param DrmSettings: DRM configuration information.
        :type DrmSettings: :class:`tencentcloud.mdl.v20200326.models.DrmSettingsInfo`
        :param MediaPackageSettings: Configuration information of media packaging, which is required when `Type` is set to MediaPackage.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MediaPackageSettings: :class:`tencentcloud.mdl.v20200326.models.MediaPackageSettingsInfo`
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OutputInfo(AbstractModel):
    """Output information.

    """

    def __init__(self):
        """
        :param Name: Output name.
        :type Name: str
        :param AudioTemplateNames: Audio transcoding template name array.
Quantity limit: [0,1] for RTMP; [0,20] for others.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AudioTemplateNames: list of str
        :param VideoTemplateNames: Video transcoding template name array. Quantity limit: [0,1].
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoTemplateNames: list of str
        :param Scte35Settings: SCTE-35 information configuration.
        :type Scte35Settings: :class:`tencentcloud.mdl.v20200326.models.Scte35SettingsInfo`
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OutputsStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        """
        :param Pipeline0: Output information of pipeline 0.
        :type Pipeline0: list of PipelineOutputStatistics
        :param Pipeline1: Output information of pipeline 1.
        :type Pipeline1: list of PipelineOutputStatistics
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PipelineInputStatistics(AbstractModel):
    """Pipeline input statistics.

    """

    def __init__(self):
        """
        :param Timestamp: Data timestamp in seconds.
        :type Timestamp: int
        :param NetworkIn: Input bandwidth in bps.
        :type NetworkIn: int
        :param Video: Video information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input video.
For other inputs, the quantity is 1.
        :type Video: list of VideoPipelineInputStatistics
        :param Audio: Audio information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input audio.
For other inputs, the quantity is 1.
        :type Audio: list of AudioPipelineInputStatistics
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PipelineLogInfo(AbstractModel):
    """Pipeline log information.

    """

    def __init__(self):
        """
        :param Pipeline0: Log information of pipeline 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pipeline0: list of LogInfo
        :param Pipeline1: Log information of pipeline 1.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pipeline1: list of LogInfo
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PipelineOutputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        """
        :param Timestamp: Timestamp.
In seconds, indicating data time.
        :type Timestamp: int
        :param NetworkOut: Output bandwidth in bps.
        :type NetworkOut: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Scte35SettingsInfo(AbstractModel):
    """SCTE-35 configuration information.

    """

    def __init__(self):
        """
        :param Behavior: Whether to pass through SCTE-35 information. Valid values: NO_PASSTHROUGH/PASSTHROUGH. Default value: NO_PASSTHROUGH.
        :type Behavior: str
        """
        self.Behavior = None


    def _deserialize(self, params):
        self.Behavior = params.get("Behavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartMediaLiveChannelRequest(AbstractModel):
    """StartMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartMediaLiveChannelResponse(AbstractModel):
    """StartMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopMediaLiveChannelRequest(AbstractModel):
    """StopMediaLiveChannel request structure.

    """

    def __init__(self):
        """
        :param Id: Channel ID.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopMediaLiveChannelResponse(AbstractModel):
    """StopMediaLiveChannel response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamAudioInfo(AbstractModel):
    """Audio information.

    """

    def __init__(self):
        """
        :param Pid: Audio `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        :param Codec: Audio codec.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param Fps: Audio frame rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Fps: int
        :param Rate: Audio bitrate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rate: int
        :param SampleRate: Audio sample rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SampleRate: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamInfo(AbstractModel):
    """Push information.

    """

    def __init__(self):
        """
        :param ClientIp: Client IP.
        :type ClientIp: str
        :param Video: Video information of pushed streams.
        :type Video: list of StreamVideoInfo
        :param Audio: Audio information of pushed streams.
        :type Audio: list of StreamAudioInfo
        :param Scte35: SCTE-35 information of pushed streams.
        :type Scte35: list of StreamScte35Info
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamScte35Info(AbstractModel):
    """SCTE-35 information.

    """

    def __init__(self):
        """
        :param Pid: SCTE-35 `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        """
        self.Pid = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StreamVideoInfo(AbstractModel):
    """Video information of pushed streams.

    """

    def __init__(self):
        """
        :param Pid: Video `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        :param Codec: Video codec.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param Fps: Video frame rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Fps: int
        :param Rate: Video bitrate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rate: int
        :param Width: Video width.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Width: int
        :param Height: Video height.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Height: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoPipelineInputStatistics(AbstractModel):
    """Pipeline input video statistics.

    """

    def __init__(self):
        """
        :param Fps: Video FPS.
        :type Fps: int
        :param Rate: Video bitrate in bps.
        :type Rate: int
        :param Pid: Video `Pid`, which is available only if the input is `rtp/udp`.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoTemplateInfo(AbstractModel):
    """Video transcoding template.

    """

    def __init__(self):
        """
        :param Name: Video transcoding template name, which can contain 1-20 letters and digits.
        :type Name: str
        :param Vcodec: Video codec. Valid values: H264/H265. If this parameter is left empty, the original value will be used.
        :type Vcodec: str
        :param VideoBitrate: Video bitrate. Value range: [50000,40000000]. The value can only be a multiple of 1,000. If this parameter is left empty, the original value will be used.
        :type VideoBitrate: int
        :param Width: Video width. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.
        :type Width: int
        :param Height: Video height. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.
        :type Height: int
        :param Fps: Video frame rate. Value range: [1,240]. If this parameter is left empty, the original value will be used.
        :type Fps: int
        :param TopSpeed: Whether to enable top speed codec. Valid value: CLOSE/OPEN. Default value: CLOSE.
        :type TopSpeed: str
        :param BitrateCompressionRatio: Top speed codec compression ratio. Value range: [0,50]. The lower the compression ratio, the higher the image quality.
        :type BitrateCompressionRatio: int
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        