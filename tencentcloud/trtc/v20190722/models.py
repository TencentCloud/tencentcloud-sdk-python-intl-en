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


class AbnormalEvent(AbstractModel):
    """The information of an error event (the possible cause of an abnormal user experience).

    """

    def __init__(self):
        r"""
        :param _AbnormalEventId: The error event ID. For details, see https://www.tencentcloud.com/document/product/647/37906?has_map=1
        :type AbnormalEventId: int
        :param _PeerId: The remote user ID. If this parameter is empty, it indicates that the error event is not associated with a remote user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeerId: str
        """
        self._AbnormalEventId = None
        self._PeerId = None

    @property
    def AbnormalEventId(self):
        """The error event ID. For details, see https://www.tencentcloud.com/document/product/647/37906?has_map=1
        :rtype: int
        """
        return self._AbnormalEventId

    @AbnormalEventId.setter
    def AbnormalEventId(self, AbnormalEventId):
        self._AbnormalEventId = AbnormalEventId

    @property
    def PeerId(self):
        """The remote user ID. If this parameter is empty, it indicates that the error event is not associated with a remote user.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId


    def _deserialize(self, params):
        self._AbnormalEventId = params.get("AbnormalEventId")
        self._PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalExperience(AbstractModel):
    """The information of an abnormal user experience and the possible causes.

    """

    def __init__(self):
        r"""
        :param _UserId: The user ID.
        :type UserId: str
        :param _ExperienceId: The abnormal experience ID.
        :type ExperienceId: int
        :param _RoomId: The room ID (string).
        :type RoomId: str
        :param _AbnormalEventList: The possible error events.
        :type AbnormalEventList: list of AbnormalEvent
        :param _EventTime: The report time.
        :type EventTime: int
        """
        self._UserId = None
        self._ExperienceId = None
        self._RoomId = None
        self._AbnormalEventList = None
        self._EventTime = None

    @property
    def UserId(self):
        """The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ExperienceId(self):
        """The abnormal experience ID.
        :rtype: int
        """
        return self._ExperienceId

    @ExperienceId.setter
    def ExperienceId(self, ExperienceId):
        self._ExperienceId = ExperienceId

    @property
    def RoomId(self):
        """The room ID (string).
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def AbnormalEventList(self):
        """The possible error events.
        :rtype: list of AbnormalEvent
        """
        return self._AbnormalEventList

    @AbnormalEventList.setter
    def AbnormalEventList(self, AbnormalEventList):
        self._AbnormalEventList = AbnormalEventList

    @property
    def EventTime(self):
        """The report time.
        :rtype: int
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._ExperienceId = params.get("ExperienceId")
        self._RoomId = params.get("RoomId")
        if params.get("AbnormalEventList") is not None:
            self._AbnormalEventList = []
            for item in params.get("AbnormalEventList"):
                obj = AbnormalEvent()
                obj._deserialize(item)
                self._AbnormalEventList.append(obj)
        self._EventTime = params.get("EventTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentConfig(AbstractModel):
    """Robot parameters

    """

    def __init__(self):
        r"""
        :param _UserId: The robot's UserId is used to enter a room and initiate tasks. [Note] This UserId cannot be repeated with the host viewer [UserId](https://cloud.tencent.com/document/product/647/46351#userid) in the current room. If multiple tasks are initiated in a room, the robot's UserId cannot be repeated, otherwise the previous task will be interrupted. The robot's UserId must be unique in the room.
        :type UserId: str
        :param _UserSig: The verification signature corresponding to the robot's UserId, that is, UserId and UserSig are equivalent to the robot's login password to enter the room. For the specific calculation method, please refer to the TRTC calculation [UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig) solution.
        :type UserSig: str
        :param _TargetUserId: The UserId of the robot pulling the media stream. After filling in, the robot will pull the media stream of the UserId for real-time processing
        :type TargetUserId: str
        :param _MaxIdleTime: If there is no streaming in the room for more than MaxIdleTime, the Service will automatically close the task. The default value is 60s.
        :type MaxIdleTime: int
        :param _WelcomeMessage: Robot's welcome message
        :type WelcomeMessage: str
        :param _InterruptMode: Intelligent interruption mode, the default value is 0, 0 means the server automatically interrupts, 1 means the server does not interrupt, and the client sends an interrupt signal to interrupt
        :type InterruptMode: int
        :param _InterruptSpeechDuration: Used when InterruptMode is 0, in milliseconds, with a default value of 500ms. This means that the server will interrupt when it detects a human voice that lasts for InterruptSpeechDuration milliseconds.
        :type InterruptSpeechDuration: int
        """
        self._UserId = None
        self._UserSig = None
        self._TargetUserId = None
        self._MaxIdleTime = None
        self._WelcomeMessage = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None

    @property
    def UserId(self):
        """The robot's UserId is used to enter a room and initiate tasks. [Note] This UserId cannot be repeated with the host viewer [UserId](https://cloud.tencent.com/document/product/647/46351#userid) in the current room. If multiple tasks are initiated in a room, the robot's UserId cannot be repeated, otherwise the previous task will be interrupted. The robot's UserId must be unique in the room.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        """The verification signature corresponding to the robot's UserId, that is, UserId and UserSig are equivalent to the robot's login password to enter the room. For the specific calculation method, please refer to the TRTC calculation [UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig) solution.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def TargetUserId(self):
        """The UserId of the robot pulling the media stream. After filling in, the robot will pull the media stream of the UserId for real-time processing
        :rtype: str
        """
        return self._TargetUserId

    @TargetUserId.setter
    def TargetUserId(self, TargetUserId):
        self._TargetUserId = TargetUserId

    @property
    def MaxIdleTime(self):
        """If there is no streaming in the room for more than MaxIdleTime, the Service will automatically close the task. The default value is 60s.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def WelcomeMessage(self):
        """Robot's welcome message
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def InterruptMode(self):
        """Intelligent interruption mode, the default value is 0, 0 means the server automatically interrupts, 1 means the server does not interrupt, and the client sends an interrupt signal to interrupt
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        """Used when InterruptMode is 0, in milliseconds, with a default value of 500ms. This means that the server will interrupt when it detects a human voice that lasts for InterruptSpeechDuration milliseconds.
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._TargetUserId = params.get("TargetUserId")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentParams(AbstractModel):
    """The information of the relaying robot in the room.

    """

    def __init__(self):
        r"""
        :param _UserId: The [user ID](https://intl.cloud.tencent.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :type UserId: str
        :param _UserSig: The signature (similar to a login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104). |
        :type UserSig: str
        :param _MaxIdleTime: The timeout period (seconds) for relaying to stop automatically after all the users whose streams are mixed leave the room. The value cannot be smaller than 5 or larger than 86400 (24 hours). Default value: 30.
        :type MaxIdleTime: int
        """
        self._UserId = None
        self._UserSig = None
        self._MaxIdleTime = None

    @property
    def UserId(self):
        """The [user ID](https://intl.cloud.tencent.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        """The signature (similar to a login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104). |
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def MaxIdleTime(self):
        """The timeout period (seconds) for relaying to stop automatically after all the users whose streams are mixed leave the room. The value cannot be smaller than 5 or larger than 86400 (24 hours). Default value: 30.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._MaxIdleTime = params.get("MaxIdleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEncode(AbstractModel):
    """The audio encoding parameters.

    """

    def __init__(self):
        r"""
        :param _SampleRate: The audio sample rate (Hz). Valid values: 48000, 44100, 32000, 24000, 16000, 8000.
        :type SampleRate: int
        :param _Channel: The number of sound channels. Valid values: 1 (mono), 2 (dual).
        :type Channel: int
        :param _BitRate: The audio bitrate (Kbps). Value range: 8-500.
        :type BitRate: int
        :param _Codec: The audio codec. Valid values: 0 (LC-AAC), 1 (HE-AAC), 2 (HE-AACv2). The default value is 0. If this parameter is set to 2, `Channel` must be 2. If it is set to 1 or 2, `SampleRate` can only be 48000, 44100, 32000, 24000, or 16000.
        :type Codec: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None
        self._Codec = None

    @property
    def SampleRate(self):
        """The audio sample rate (Hz). Valid values: 48000, 44100, 32000, 24000, 16000, 8000.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        """The number of sound channels. Valid values: 1 (mono), 2 (dual).
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        """The audio bitrate (Kbps). Value range: 8-500.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Codec(self):
        """The audio codec. Valid values: 0 (LC-AAC), 1 (HE-AAC), 2 (HE-AACv2). The default value is 0. If this parameter is set to 2, `Channel` must be 2. If it is set to 1 or 2, `SampleRate` can only be 48000, 44100, 32000, 24000, or 16000.
        :rtype: int
        """
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        self._Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEncodeParams(AbstractModel):
    """Audio transcoding parameters

    """

    def __init__(self):
        r"""
        :param _SampleRate: Audio Sample rate, Value range [48000, 44100], unit is Hz.
        :type SampleRate: int
        :param _Channel: Audio Channel number, Value range [1,2], 1 means Audio is Mono-channel, 2 means Audio is Dual-channel.
        :type Channel: int
        :param _BitRate: Audio Bitrate, Value range [8,500], unit is kbps.
        :type BitRate: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None

    @property
    def SampleRate(self):
        """Audio Sample rate, Value range [48000, 44100], unit is Hz.
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        """Audio Channel number, Value range [1,2], 1 means Audio is Mono-channel, 2 means Audio is Dual-channel.
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        """Audio Bitrate, Value range [8,500], unit is kbps.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioParams(AbstractModel):
    """The audio transcoding parameters for recording.

    """

    def __init__(self):
        r"""
        :param _SampleRate: The audio sample rate.
1: 48000 Hz (default)
2: 44100 Hz
3: 16000 Hz
        :type SampleRate: int
        :param _Channel: The number of sound channels.
1: Mono-channel
2: Dual-channel (default)
        :type Channel: int
        :param _BitRate: The audio bitrate (bps). Value range: [32000, 128000]. Default: 64000.
        :type BitRate: int
        """
        self._SampleRate = None
        self._Channel = None
        self._BitRate = None

    @property
    def SampleRate(self):
        """The audio sample rate.
1: 48000 Hz (default)
2: 44100 Hz
3: 16000 Hz
        :rtype: int
        """
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        """The number of sound channels.
1: Mono-channel
2: Dual-channel (default)
        :rtype: int
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        """The audio bitrate (bps). Value range: [32000, 128000]. Default: 64000.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate


    def _deserialize(self, params):
        self._SampleRate = params.get("SampleRate")
        self._Channel = params.get("Channel")
        self._BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorage(AbstractModel):
    """The cloud storage information.

    """

    def __init__(self):
        r"""
        :param _Vendor: The cloud storage provider.
`0`: Tencent Cloud COS; `1`: AWS storage. Other vendors are not supported currently.
        :type Vendor: int
        :param _Region: The region of cloud storage.
        :type Region: str
        :param _Bucket: The storage bucket.
        :type Bucket: str
        :param _AccessKey: The access_key of the cloud storage account.
        :type AccessKey: str
        :param _SecretKey: The secret_key of the cloud storage account.
        :type SecretKey: str
        :param _FileNamePrefix: The bucket to save data, which is an array of strings that can contain letters (a-z and A-Z), numbers (0-9), underscores (_), and hyphens (-). For example, if the value of this parameter is `["prefix1", "prefix2"]`, the recording file `xxx.m3u8` will be saved as `prefix1/prefix2/TaskId/xxx.m3u8`.
        :type FileNamePrefix: list of str
        """
        self._Vendor = None
        self._Region = None
        self._Bucket = None
        self._AccessKey = None
        self._SecretKey = None
        self._FileNamePrefix = None

    @property
    def Vendor(self):
        """The cloud storage provider.
`0`: Tencent Cloud COS; `1`: AWS storage. Other vendors are not supported currently.
        :rtype: int
        """
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        """The region of cloud storage.
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        """The storage bucket.
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        """The access_key of the cloud storage account.
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """The secret_key of the cloud storage account.
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
        """The bucket to save data, which is an array of strings that can contain letters (a-z and A-Z), numbers (0-9), underscores (_), and hyphens (-). For example, if the value of this parameter is `["prefix1", "prefix2"]`, the recording file `xxx.m3u8` will be saved as `prefix1/prefix2/TaskId/xxx.m3u8`.
        :rtype: list of str
        """
        return self._FileNamePrefix

    @FileNamePrefix.setter
    def FileNamePrefix(self, FileNamePrefix):
        self._FileNamePrefix = FileNamePrefix


    def _deserialize(self, params):
        self._Vendor = params.get("Vendor")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudVod(AbstractModel):
    """The VOD parameters.

    """

    def __init__(self):
        r"""
        :param _TencentVod: The Tencent Cloud VOD parameters.
        :type TencentVod: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        self._TencentVod = None

    @property
    def TencentVod(self):
        """The Tencent Cloud VOD parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        return self._TencentVod

    @TencentVod.setter
    def TencentVod(self, TencentVod):
        self._TencentVod = TencentVod


    def _deserialize(self, params):
        if params.get("TencentVod") is not None:
            self._TencentVod = TencentVod()
            self._TencentVod._deserialize(params.get("TencentVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlAIConversationRequest(AbstractModel):
    """ControlAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Unique ID of the task
        :type TaskId: str
        :param _Command: Control commands, currently supported commands are as follows:
- ServerPushText, the server sends text to the AI robot, and the AI robot will play the text
        :type Command: str
        :param _ServerPushText: The server sends a text broadcast command. This is required when Command is ServerPushText.
        :type ServerPushText: :class:`tencentcloud.trtc.v20190722.models.ServerPushText`
        """
        self._TaskId = None
        self._Command = None
        self._ServerPushText = None

    @property
    def TaskId(self):
        """Unique ID of the task
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Command(self):
        """Control commands, currently supported commands are as follows:
- ServerPushText, the server sends text to the AI robot, and the AI robot will play the text
        :rtype: str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def ServerPushText(self):
        """The server sends a text broadcast command. This is required when Command is ServerPushText.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ServerPushText`
        """
        return self._ServerPushText

    @ServerPushText.setter
    def ServerPushText(self, ServerPushText):
        self._ServerPushText = ServerPushText


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Command = params.get("Command")
        if params.get("ServerPushText") is not None:
            self._ServerPushText = ServerPushText()
            self._ServerPushText._deserialize(params.get("ServerPushText"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControlAIConversationResponse(AbstractModel):
    """ControlAIConversation response structure.

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


class CreateCloudRecordingRequest(AbstractModel):
    """CreateCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :type SdkAppId: int
        :param _RoomId: The [room ID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :type RoomId: str
        :param _UserId: The [user ID](https://www.tencentcloud.com/document/product/647/37714#userid) of the recording robot in the TRTC room, which cannot be identical to the user IDs of anchors in the room or other recording robots. To distinguish this user ID from others, we recommend you include the room ID in the user ID.
        :type UserId: str
        :param _UserSig: The signature (similar to a login password) required for the recording robot to enter the room. Each user ID corresponds to a signature. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104).
        :type UserSig: str
        :param _RecordParams: The on-cloud recording parameters.
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        :param _StorageParams: The storage information of the recording file. Currently, you can save recording files to Tencent Cloud VOD or COS.
        :type StorageParams: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        :param _RoomIdType: The type of the TRTC room ID, which must be the same as the ID type of the room whose streams are recorded.
0: String
1: 32-bit integer (default)
        :type RoomIdType: int
        :param _MixTranscodeParams: The stream mixing parameters, which are valid if the mixed-stream recording mode is used.
        :type MixTranscodeParams: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        :param _MixLayoutParams: The layout parameters, which are valid if the mixed-stream recording mode is used.
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param _ResourceExpiredHour: The amount of time (in hours) during which API requests can be made after recording starts. Calculation starts when a recording task is started (when the recording task ID is returned). Once the period elapses, the query, modification, and stop recording APIs can no longer be called, but the recording task will continue. The default value is `72` (three days), and the maximum and minimum values allowed are `720` (30 days) and `6` respectively. If you do not set this parameter, the query, modification, and stop recording APIs can be called within 72 hours after recording starts.
        :type ResourceExpiredHour: int
        :param _PrivateMapKey: The permission ticket for a TRTC room. This parameter is required if advanced permission control is enabled in the console, in which case the TRTC backend will verify users’ [PrivateMapKey](https://intl.cloud.tencent.com/document/product/647/32240?from_cn_redirect=1), which include an encrypted room ID and permission bit list. A user providing only `UserSig` and not `PrivateMapKey` will be unable to enter the room.
        :type PrivateMapKey: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._UserSig = None
        self._RecordParams = None
        self._StorageParams = None
        self._RoomIdType = None
        self._MixTranscodeParams = None
        self._MixLayoutParams = None
        self._ResourceExpiredHour = None
        self._PrivateMapKey = None

    @property
    def SdkAppId(self):
        """The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """The [room ID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        """The [user ID](https://www.tencentcloud.com/document/product/647/37714#userid) of the recording robot in the TRTC room, which cannot be identical to the user IDs of anchors in the room or other recording robots. To distinguish this user ID from others, we recommend you include the room ID in the user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        """The signature (similar to a login password) required for the recording robot to enter the room. Each user ID corresponds to a signature. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104).
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def RecordParams(self):
        """The on-cloud recording parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        """
        return self._RecordParams

    @RecordParams.setter
    def RecordParams(self, RecordParams):
        self._RecordParams = RecordParams

    @property
    def StorageParams(self):
        """The storage information of the recording file. Currently, you can save recording files to Tencent Cloud VOD or COS.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        """
        return self._StorageParams

    @StorageParams.setter
    def StorageParams(self, StorageParams):
        self._StorageParams = StorageParams

    @property
    def RoomIdType(self):
        """The type of the TRTC room ID, which must be the same as the ID type of the room whose streams are recorded.
0: String
1: 32-bit integer (default)
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def MixTranscodeParams(self):
        """The stream mixing parameters, which are valid if the mixed-stream recording mode is used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        """
        return self._MixTranscodeParams

    @MixTranscodeParams.setter
    def MixTranscodeParams(self, MixTranscodeParams):
        self._MixTranscodeParams = MixTranscodeParams

    @property
    def MixLayoutParams(self):
        """The layout parameters, which are valid if the mixed-stream recording mode is used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        """
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def ResourceExpiredHour(self):
        """The amount of time (in hours) during which API requests can be made after recording starts. Calculation starts when a recording task is started (when the recording task ID is returned). Once the period elapses, the query, modification, and stop recording APIs can no longer be called, but the recording task will continue. The default value is `72` (three days), and the maximum and minimum values allowed are `720` (30 days) and `6` respectively. If you do not set this parameter, the query, modification, and stop recording APIs can be called within 72 hours after recording starts.
        :rtype: int
        """
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour

    @property
    def PrivateMapKey(self):
        """The permission ticket for a TRTC room. This parameter is required if advanced permission control is enabled in the console, in which case the TRTC backend will verify users’ [PrivateMapKey](https://intl.cloud.tencent.com/document/product/647/32240?from_cn_redirect=1), which include an encrypted room ID and permission bit list. A user providing only `UserSig` and not `PrivateMapKey` will be unable to enter the room.
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        if params.get("RecordParams") is not None:
            self._RecordParams = RecordParams()
            self._RecordParams._deserialize(params.get("RecordParams"))
        if params.get("StorageParams") is not None:
            self._StorageParams = StorageParams()
            self._StorageParams._deserialize(params.get("StorageParams"))
        self._RoomIdType = params.get("RoomIdType")
        if params.get("MixTranscodeParams") is not None:
            self._MixTranscodeParams = MixTranscodeParams()
            self._MixTranscodeParams._deserialize(params.get("MixTranscodeParams"))
        if params.get("MixLayoutParams") is not None:
            self._MixLayoutParams = MixLayoutParams()
            self._MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        self._ResourceExpiredHour = params.get("ResourceExpiredHour")
        self._PrivateMapKey = params.get("PrivateMapKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingResponse(AbstractModel):
    """CreateCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends. After a recording task starts, if you want to perform other actions on the task, you need to specify the task ID when making API requests.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends. After a recording task starts, if you want to perform other actions on the task, you need to specify the task ID when making API requests.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteCloudRecordingRequest(AbstractModel):
    """DeleteCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """The `SDKAppID` of the room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The unique ID of the recording task, which is returned after recording starts successfully.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRecordingResponse(AbstractModel):
    """DeleteCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeAIConversationRequest(AbstractModel):
    """DescribeAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the transcription task.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the task.
        :type TaskId: str
        :param _SessionId: The SessionId filled in when starting the task. 
        :type SessionId: str
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SessionId = None

    @property
    def SdkAppId(self):
        """TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the transcription task.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The unique ID of the task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        """The SessionId filled in when starting the task. 
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIConversationResponse(AbstractModel):
    """DescribeAIConversation response structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The time when the task starts.
        :type StartTime: str
        :param _Status: Task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :type Status: str
        :param _TaskId: The unique ID of the task, generated when the task is started
        :type TaskId: str
        :param _SessionId: The SessionId filled in when opening the conversation task.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StartTime = None
        self._Status = None
        self._TaskId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def StartTime(self):
        """The time when the task starts.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        """Task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        """The unique ID of the task, generated when the task is started
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        """The SessionId filled in when opening the conversation task.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeAITranscriptionRequest(AbstractModel):
    """DescribeAITranscription request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Query the task status. If not in use, pass in an empty string. There are two query methods: 1. Fill in only TaskId. This method uses TaskId to query tasks. 2. TaskId is an empty string. Fill in SdkAppId and SessionId. This method does not require TaskId to query tasks.
        :type TaskId: str
        :param _SdkAppId: TRTC's SdkAppId is used together with SessionId.
        :type SdkAppId: int
        :param _SessionId: The SessionId passed in when starting the transcription task is used together with the SdkAppId.
        :type SessionId: str
        """
        self._TaskId = None
        self._SdkAppId = None
        self._SessionId = None

    @property
    def TaskId(self):
        """Query the task status. If not in use, pass in an empty string. There are two query methods: 1. Fill in only TaskId. This method uses TaskId to query tasks. 2. TaskId is an empty string. Fill in SdkAppId and SessionId. This method does not require TaskId to query tasks.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SdkAppId(self):
        """TRTC's SdkAppId is used together with SessionId.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def SessionId(self):
        """The SessionId passed in when starting the transcription task is used together with the SdkAppId.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SdkAppId = params.get("SdkAppId")
        self._SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAITranscriptionResponse(AbstractModel):
    """DescribeAITranscription response structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The time when the task starts.
        :type StartTime: str
        :param _Status: Transcription task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :type Status: str
        :param _TaskId: Uniquely identifies a task.
        :type TaskId: str
        :param _SessionId: The SessionId filled in when starting the transcription task. If not filled in, nothing is returned.
        :type SessionId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._StartTime = None
        self._Status = None
        self._TaskId = None
        self._SessionId = None
        self._RequestId = None

    @property
    def StartTime(self):
        """The time when the task starts.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        """Transcription task status. There are 4 values: 1. Idle means the task has not started 2. Preparing means the task is being prepared 3. InProgress means the task is running 4. Stopped means the task has stopped and resources are being cleaned up
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        """Uniquely identifies a task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SessionId(self):
        """The SessionId filled in when starting the transcription task. If not filled in, nothing is returned.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

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
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._SessionId = params.get("SessionId")
        self._RequestId = params.get("RequestId")


class DescribeCallDetailInfoRequest(AbstractModel):
    """DescribeCallDetailInfo request structure.

    """

    def __init__(self):
        r"""
        :param _CommId: The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :type CommId: str
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If `DataType` is not null, the end time and start time cannot be more than one hour apart; if `DataType` is null, the end time and start time cannot be more than four hours apart.
        :type EndTime: int
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _UserIds: The users to query. If you do not specify this, the data of six users will be returned.
        :type UserIds: list of str
        :param _DataType: The metrics to query. If you do not specify this, only the user list will be returned. If you pass in `all`, all metrics will be returned.
`appCpu`: The CPU utilization of the application.
`sysCpu`: The CPU utilization of the system.
`aBit`: The upstream/downstream audio bitrate (bps).
`aBlock`: The audio stutter duration (ms).
`bigvBit`: The upstream/downstream video bitrate (bps).
`bigvCapFps`: The frame rate for capturing videos.
`bigvEncFps`: The frame rate for sending videos.
`bigvDecFps`: The rendering frame rate.
`bigvBlock`: The video stutter duration (ms).
`aLoss`: The upstream/downstream audio packet loss.
`bigvLoss`: The upstream/downstream video packet loss.
`bigvWidth`: The upstream/downstream resolution (width).
`bigvHeight`: The upstream/downstream resolution (height).
        :type DataType: list of str
        :param _PageNumber: The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :type PageNumber: int
        :param _PageSize: The number of records per page. The default is `6`.
Value range: 1-100.
Note: If `DataType` is not null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `6`.
If `DataType` is null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `100`.
        :type PageSize: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._UserIds = None
        self._DataType = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def CommId(self):
        """The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        """The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If `DataType` is not null, the end time and start time cannot be more than one hour apart; if `DataType` is null, the end time and start time cannot be more than four hours apart.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        """The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        """The users to query. If you do not specify this, the data of six users will be returned.
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def DataType(self):
        """The metrics to query. If you do not specify this, only the user list will be returned. If you pass in `all`, all metrics will be returned.
`appCpu`: The CPU utilization of the application.
`sysCpu`: The CPU utilization of the system.
`aBit`: The upstream/downstream audio bitrate (bps).
`aBlock`: The audio stutter duration (ms).
`bigvBit`: The upstream/downstream video bitrate (bps).
`bigvCapFps`: The frame rate for capturing videos.
`bigvEncFps`: The frame rate for sending videos.
`bigvDecFps`: The rendering frame rate.
`bigvBlock`: The video stutter duration (ms).
`aLoss`: The upstream/downstream audio packet loss.
`bigvLoss`: The upstream/downstream video packet loss.
`bigvWidth`: The upstream/downstream resolution (width).
`bigvHeight`: The upstream/downstream resolution (height).
        :rtype: list of str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PageNumber(self):
        """The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """The number of records per page. The default is `6`.
Value range: 1-100.
Note: If `DataType` is not null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `6`.
If `DataType` is null, the length of the array `UserIds` and the value of `PageSize` cannot exceed `100`.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._UserIds = params.get("UserIds")
        self._DataType = params.get("DataType")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCallDetailInfoResponse(AbstractModel):
    """DescribeCallDetailInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _UserList: The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserList: list of UserInformation
        :param _Data: The call quality data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Data: list of QualityData
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._UserList = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        """The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        """The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserInformation
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def Data(self):
        """The call quality data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of QualityData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Total = params.get("Total")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCloudRecordingRequest(AbstractModel):
    """DescribeCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """The `SDKAppID` of the room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The unique ID of the recording task, which is returned after recording starts successfully.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRecordingResponse(AbstractModel):
    """DescribeCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The unique ID of the recording task.
        :type TaskId: str
        :param _Status: The status of the on-cloud recording task.
Idle: The task is idle.
InProgress: The task is in progress.
Exited: The task is being ended.
        :type Status: str
        :param _StorageFileList: The information of the recording files.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StorageFileList: list of StorageFile
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._Status = None
        self._StorageFileList = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The unique ID of the recording task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        """The status of the on-cloud recording task.
Idle: The task is idle.
InProgress: The task is in progress.
Exited: The task is being ended.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StorageFileList(self):
        """The information of the recording files.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of StorageFile
        """
        return self._StorageFileList

    @StorageFileList.setter
    def StorageFileList(self, StorageFileList):
        self._StorageFileList = StorageFileList

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
        self._TaskId = params.get("TaskId")
        self._Status = params.get("Status")
        if params.get("StorageFileList") is not None:
            self._StorageFileList = []
            for item in params.get("StorageFileList"):
                obj = StorageFile()
                obj._deserialize(item)
                self._StorageFileList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMixTranscodingUsageRequest(AbstractModel):
    """DescribeMixTranscodingUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        """The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        """The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMixTranscodingUsageResponse(AbstractModel):
    """DescribeMixTranscodingUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        """The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        """The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRecordingUsageRequest(AbstractModel):
    """DescribeRecordingUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _MixType: Whether to query single-stream or mixed-stream recording. Valid values: `single`, `multi`.
        :type MixType: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._MixType = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        """The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MixType(self):
        """Whether to query single-stream or mixed-stream recording. Valid values: `single`, `multi`.
        :rtype: str
        """
        return self._MixType

    @MixType.setter
    def MixType(self, MixType):
        self._MixType = MixType

    @property
    def SdkAppId(self):
        """The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MixType = params.get("MixType")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRecordingUsageResponse(AbstractModel):
    """DescribeRecordingUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        """The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        """The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRelayUsageRequest(AbstractModel):
    """DescribeRelayUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        """The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        """The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelayUsageResponse(AbstractModel):
    """DescribeRelayUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        """The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        """The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRoomInfoRequest(AbstractModel):
    """DescribeRoomInfo request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than 24 hours apart.
        :type EndTime: int
        :param _RoomId: The room ID, such as `223`.
        :type RoomId: str
        :param _PageNumber: The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, 10 records will be returned.
        :type PageNumber: int
        :param _PageSize: The number of records per page. The default is `10`.
Value range: 1-100.
        :type PageSize: int
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def SdkAppId(self):
        """The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        """The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than 24 hours apart.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        """The room ID, such as `223`.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def PageNumber(self):
        """The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, 10 records will be returned.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """The number of records per page. The default is `10`.
Value range: 1-100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRoomInfoResponse(AbstractModel):
    """DescribeRoomInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _RoomList: The room information.
        :type RoomList: list of RoomState
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._RoomList = None
        self._RequestId = None

    @property
    def Total(self):
        """The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RoomList(self):
        """The room information.
        :rtype: list of RoomState
        """
        return self._RoomList

    @RoomList.setter
    def RoomList(self, RoomList):
        self._RoomList = RoomList

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
        self._Total = params.get("Total")
        if params.get("RoomList") is not None:
            self._RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self._RoomList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScaleInfoRequest(AbstractModel):
    """DescribeScaleInfo request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`. The end time and start time should preferably be more than 24 hours apart.
Note: Data is collected on a daily basis. To query the data of a day, make sure the end time is later than 00:00 on that day. Otherwise, no data will be returned. For example, to query the data on the 20th, the end time must be later than 00:00 on the 20th.
        :type EndTime: int
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppId(self):
        """The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        """The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`. The end time and start time should preferably be more than 24 hours apart.
Note: Data is collected on a daily basis. To query the data of a day, make sure the end time is later than 00:00 on that day. Otherwise, no data will be returned. For example, to query the data on the 20th, the end time must be later than 00:00 on the 20th.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScaleInfoResponse(AbstractModel):
    """DescribeScaleInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _ScaleList: The returned data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScaleList: list of ScaleInfomation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._ScaleList = None
        self._RequestId = None

    @property
    def Total(self):
        """The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ScaleList(self):
        """The returned data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of ScaleInfomation
        """
        return self._ScaleList

    @ScaleList.setter
    def ScaleList(self, ScaleList):
        self._ScaleList = ScaleList

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
        self._Total = params.get("Total")
        if params.get("ScaleList") is not None:
            self._ScaleList = []
            for item in params.get("ScaleList"):
                obj = ScaleInfomation()
                obj._deserialize(item)
                self._ScaleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamIngestRequest(AbstractModel):
    """DescribeStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :type SdkAppId: int
        :param _TaskId: The unique Id of the task, will return after successfully starting the task.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The unique Id of the task, will return after successfully starting the task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamIngestResponse(AbstractModel):
    """DescribeStreamIngest response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :type Status: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketQualityDataRequest(AbstractModel):
    """DescribeTRTCMarketQualityData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SDKAppId (e.g., 1400xxxxxx)
        :type SdkAppId: str
        :param _StartTime: Query start time, format is YYYY-MM-DD. (The query time range depends on the monitoring dashboard function version, the premium edition can query up to 30 days)
        :type StartTime: str
        :param _EndTime: Query end time, format is YYYY-MM-DD.
        :type EndTime: str
        :param _Period: The granularity of the returned data, which can be set to the following values:
d: by day. This returns data for the entire UTC day of the query time range. 
h: by hour. This returns data for the entire UTC hour of the query time range.
        :type Period: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def SdkAppId(self):
        """User SDKAppId (e.g., 1400xxxxxx)
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        """Query start time, format is YYYY-MM-DD. (The query time range depends on the monitoring dashboard function version, the premium edition can query up to 30 days)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query end time, format is YYYY-MM-DD.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """The granularity of the returned data, which can be set to the following values:
d: by day. This returns data for the entire UTC day of the query time range. 
h: by hour. This returns data for the entire UTC hour of the query time range.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
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
        


class DescribeTRTCMarketQualityDataResponse(AbstractModel):
    """DescribeTRTCMarketQualityData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC Data Dashboard output parameters
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """TRTC Data Dashboard output parameters
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCMarketScaleDataRequest(AbstractModel):
    """DescribeTRTCMarketScaleData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SDKAppId
        :type SdkAppId: str
        :param _StartTime: Query start time, format is YYYY-MM-DD. (The query time range depends on the monitoring dashboard function version, the premium edition can query up to 60 days)
        :type StartTime: str
        :param _EndTime: Query end time, format is YYYY-MM-DD.
        :type EndTime: str
        :param _Period: The granularity of the returned data, which can be set to the following values:
 d: by day. This returns data for the entire UTC day of the query time range.
 h: by hour. This returns data for the entire UTC hour of the query time range.
        :type Period: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def SdkAppId(self):
        """User SDKAppId
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        """Query start time, format is YYYY-MM-DD. (The query time range depends on the monitoring dashboard function version, the premium edition can query up to 60 days)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query end time, format is YYYY-MM-DD.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """The granularity of the returned data, which can be set to the following values:
 d: by day. This returns data for the entire UTC day of the query time range.
 h: by hour. This returns data for the entire UTC hour of the query time range.
        :rtype: str
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
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
        


class DescribeTRTCMarketScaleDataResponse(AbstractModel):
    """DescribeTRTCMarketScaleData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC Data Dashboard output parameters
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """TRTC Data Dashboard output parameters
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeQualityDataRequest(AbstractModel):
    """DescribeTRTCRealTimeQualityData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SDKAppId (e.g., 1400xxxxxx)
        :type SdkAppId: str
        :param _StartTime: Start time, unix timestamp, Unit: seconds (Query time range depends on the monitoring dashboard function version, standard edition can query the last 3 hours, premium edition can query the last 12 hours)
        :type StartTime: int
        :param _EndTime: End time, unix timestamp, Unit: seconds
        :type EndTime: int
        :param _RoomId: Room ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        """User SDKAppId (e.g., 1400xxxxxx)
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        """Start time, unix timestamp, Unit: seconds (Query time range depends on the monitoring dashboard function version, standard edition can query the last 3 hours, premium edition can query the last 12 hours)
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time, unix timestamp, Unit: seconds
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        """Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeQualityDataResponse(AbstractModel):
    """DescribeTRTCRealTimeQualityData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC Real- Time Monitoring output parameters
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """TRTC Real- Time Monitoring output parameters
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTRTCRealTimeScaleDataRequest(AbstractModel):
    """DescribeTRTCRealTimeScaleData request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: User SDKAppId (e.g., 1400xxxxxx)
        :type SdkAppId: str
        :param _StartTime: Start time, unix timestamp, Unit: seconds (Query time range depends on the function version of the monitoring dashboard, premium edition can query up to 1 hours)
        :type StartTime: int
        :param _EndTime: End time, unix timestamp, Unit: seconds
        :type EndTime: int
        :param _RoomId: Room ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        """User SDKAppId (e.g., 1400xxxxxx)
        :rtype: str
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        """Start time, unix timestamp, Unit: seconds (Query time range depends on the function version of the monitoring dashboard, premium edition can query up to 1 hours)
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time, unix timestamp, Unit: seconds
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        """Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTRTCRealTimeScaleDataResponse(AbstractModel):
    """DescribeTRTCRealTimeScaleData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: TRTC Real- Time Monitoring
 output parameter
        :type Data: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """TRTC Real- Time Monitoring
 output parameter
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TRTCDataResult`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = TRTCDataResult()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeTrtcRoomUsageRequest(AbstractModel):
    """DescribeTrtcRoomUsage request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppid: The `SDKAppID` of the room.
        :type SdkAppid: int
        :param _StartTime: The start time in the format of `YYYY-MM-DD HH:MM` (accurate to the minute).
        :type StartTime: str
        :param _EndTime: The end time in the format of `YYYY-MM-DD HH:MM`. The start and end time cannot be more than 24 hours apart.
        :type EndTime: str
        """
        self._SdkAppid = None
        self._StartTime = None
        self._EndTime = None

    @property
    def SdkAppid(self):
        """The `SDKAppID` of the room.
        :rtype: int
        """
        return self._SdkAppid

    @SdkAppid.setter
    def SdkAppid(self, SdkAppid):
        self._SdkAppid = SdkAppid

    @property
    def StartTime(self):
        """The start time in the format of `YYYY-MM-DD HH:MM` (accurate to the minute).
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time in the format of `YYYY-MM-DD HH:MM`. The start and end time cannot be more than 24 hours apart.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._SdkAppid = params.get("SdkAppid")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcRoomUsageResponse(AbstractModel):
    """DescribeTrtcRoomUsage response structure.

    """

    def __init__(self):
        r"""
        :param _Data: The usage data grouped by room, in CSV format.
        :type Data: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """The usage data grouped by room, in CSV format.
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeTrtcUsageRequest(AbstractModel):
    """DescribeTrtcUsage request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: The start date in the format of YYYY-MM-DD.
        :type StartTime: str
        :param _EndTime: The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :type EndTime: str
        :param _SdkAppId: The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :type SdkAppId: int
        """
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None

    @property
    def StartTime(self):
        """The start date in the format of YYYY-MM-DD.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end date in the format of YYYY-MM-DD.
The period queried per request cannot be longer than 31 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        """The `SDKAppID` of the TRTC application to which the target room belongs. If you do not specify this parameter, the usage statistics of all TRTC applications under the current account will be returned.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrtcUsageResponse(AbstractModel):
    """DescribeTrtcUsage response structure.

    """

    def __init__(self):
        r"""
        :param _UsageKey: The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :type UsageKey: list of str
        :param _UsageList: The usage data in each time unit.
        :type UsageList: list of TrtcUsage
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UsageKey = None
        self._UsageList = None
        self._RequestId = None

    @property
    def UsageKey(self):
        """The usage type. Each element of this parameter corresponds to an element of `UsageValue` in the order they are listed.
        :rtype: list of str
        """
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        """The usage data in each time unit.
        :rtype: list of TrtcUsage
        """
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

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
        self._UsageKey = params.get("UsageKey")
        if params.get("UsageList") is not None:
            self._UsageList = []
            for item in params.get("UsageList"):
                obj = TrtcUsage()
                obj._deserialize(item)
                self._UsageList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUnusualEventRequest(AbstractModel):
    """DescribeUnusualEvent request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`. The end time and start time cannot be more than one hour apart.
        :type EndTime: int
        :param _RoomId: The room ID. Up to 20 random abnormal user experiences of the specified room will be returned.
        :type RoomId: str
        """
        self._SdkAppId = None
        self._StartTime = None
        self._EndTime = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        """The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        """The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`. The end time and start time cannot be more than one hour apart.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        """The room ID. Up to 20 random abnormal user experiences of the specified room will be returned.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUnusualEventResponse(AbstractModel):
    """DescribeUnusualEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
Value range: 0-20.
        :type Total: int
        :param _AbnormalExperienceList: The information of the abnormal user experiences.
        :type AbnormalExperienceList: list of AbnormalExperience
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._AbnormalExperienceList = None
        self._RequestId = None

    @property
    def Total(self):
        """The number of records returned.
Value range: 0-20.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AbnormalExperienceList(self):
        """The information of the abnormal user experiences.
        :rtype: list of AbnormalExperience
        """
        return self._AbnormalExperienceList

    @AbnormalExperienceList.setter
    def AbnormalExperienceList(self, AbnormalExperienceList):
        self._AbnormalExperienceList = AbnormalExperienceList

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
        self._Total = params.get("Total")
        if params.get("AbnormalExperienceList") is not None:
            self._AbnormalExperienceList = []
            for item in params.get("AbnormalExperienceList"):
                obj = AbnormalExperience()
                obj._deserialize(item)
                self._AbnormalExperienceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserEventRequest(AbstractModel):
    """DescribeUserEvent request structure.

    """

    def __init__(self):
        r"""
        :param _CommId: The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :type CommId: str
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If you pass in an end time later than the room end time, the room end time will be used.
        :type EndTime: int
        :param _UserId: The user ID.
        :type UserId: str
        :param _RoomId: The room ID, such as `223`.
        :type RoomId: str
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._UserId = None
        self._RoomId = None
        self._SdkAppId = None

    @property
    def CommId(self):
        """The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        """The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: If you pass in an end time later than the room end time, the room end time will be used.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserId(self):
        """The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        """The room ID, such as `223`.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
        """The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserEventResponse(AbstractModel):
    """DescribeUserEvent response structure.

    """

    def __init__(self):
        r"""
        :param _Data: The event list. An empty array will be returned if no data is obtained.
        :type Data: list of EventList
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """The event list. An empty array will be returned if no data is obtained.
        :rtype: list of EventList
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EventList()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUserInfoRequest(AbstractModel):
    """DescribeUserInfo request structure.

    """

    def __init__(self):
        r"""
        :param _CommId: The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :type CommId: str
        :param _StartTime: The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :type StartTime: int
        :param _EndTime: The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than four hours apart.
        :type EndTime: int
        :param _SdkAppId: The application ID, such as `1400xxxxxx`.
        :type SdkAppId: int
        :param _UserIds: The users to query. If you do not specify this, the information of six users will be returned.
Array length: 1-100.
        :type UserIds: list of str
        :param _PageNumber: The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :type PageNumber: int
        :param _PageSize: The number of records per page. The default is `6`.
Array length: 1-100.
        :type PageSize: int
        """
        self._CommId = None
        self._StartTime = None
        self._EndTime = None
        self._SdkAppId = None
        self._UserIds = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def CommId(self):
        """The unique ID of a call, whose format is `SdkAppId_CreateTime`, such as `1400xxxxxx_218695_1590065777`. `createTime` is the UNIX timestamp (seconds) when the room was created. Its value can be obtained using the [DescribeRoomInfo](https://intl.cloud.tencent.com/document/product/647/44050?from_cn_redirect=1) API.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        """The start time, which is a Unix timestamp (seconds) in local time, such as `1590065777`.
Note: Only data in the last 14 days can be queried.
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """The end time, which is a Unix timestamp (seconds) in local time, such as `1590065877`.
Note: The end and start time cannot be more than four hours apart.
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        """The application ID, such as `1400xxxxxx`.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        """The users to query. If you do not specify this, the information of six users will be returned.
Array length: 1-100.
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def PageNumber(self):
        """The page number. The default is 0.
Note: If `PageNumber` or `PageSize` is not specified, six records will be returned.
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """The number of records per page. The default is `6`.
Array length: 1-100.
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._SdkAppId = params.get("SdkAppId")
        self._UserIds = params.get("UserIds")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserInfoResponse(AbstractModel):
    """DescribeUserInfo response structure.

    """

    def __init__(self):
        r"""
        :param _Total: The number of records returned.
        :type Total: int
        :param _UserList: The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserList: list of UserInformation
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Total = None
        self._UserList = None
        self._RequestId = None

    @property
    def Total(self):
        """The number of records returned.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        """The user information.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: list of UserInformation
        """
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

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
        self._Total = params.get("Total")
        if params.get("UserList") is not None:
            self._UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self._UserList.append(obj)
        self._RequestId = params.get("RequestId")


class DismissRoomByStrRoomIdRequest(AbstractModel):
    """DismissRoomByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param _RoomId: Room ID
        :type RoomId: str
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        """`SDKAppId` of TRTC
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomByStrRoomIdResponse(AbstractModel):
    """DismissRoomByStrRoomId response structure.

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


class DismissRoomRequest(AbstractModel):
    """DismissRoom request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param _RoomId: Room number.
        :type RoomId: int
        """
        self._SdkAppId = None
        self._RoomId = None

    @property
    def SdkAppId(self):
        """`SDKAppId` of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """Room number.
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    """DismissRoom response structure.

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


class EventList(AbstractModel):
    """A list of SDK or WebRTC events.

    """

    def __init__(self):
        r"""
        :param _Content: The event information.
        :type Content: list of EventMessage
        :param _PeerId: The user ID of the sender.
        :type PeerId: str
        """
        self._Content = None
        self._PeerId = None

    @property
    def Content(self):
        """The event information.
        :rtype: list of EventMessage
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def PeerId(self):
        """The user ID of the sender.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = EventMessage()
                obj._deserialize(item)
                self._Content.append(obj)
        self._PeerId = params.get("PeerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventMessage(AbstractModel):
    """The event information, including the timestamp and event ID.

    """

    def __init__(self):
        r"""
        :param _Type: The video stream type. Valid values:
`0`: A non-video event
`2`: The big video
`3`: The small video
`7`: A relayed video
        :type Type: int
        :param _Time: The event reporting time in the format of UNIX timestamp (milliseconds), such as `1589891188801`.
        :type Time: int
        :param _EventId: The event ID. Events are classified into SDK events and WebRTC events. For more information, see https://www.tencentcloud.com/document/product/647/37906?has_map=1
        :type EventId: int
        :param _ParamOne: The first event parameter, such as the video width.
        :type ParamOne: int
        :param _ParamTwo: The second event parameter, such as the video height.
        :type ParamTwo: int
        """
        self._Type = None
        self._Time = None
        self._EventId = None
        self._ParamOne = None
        self._ParamTwo = None

    @property
    def Type(self):
        """The video stream type. Valid values:
`0`: A non-video event
`2`: The big video
`3`: The small video
`7`: A relayed video
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        """The event reporting time in the format of UNIX timestamp (milliseconds), such as `1589891188801`.
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def EventId(self):
        """The event ID. Events are classified into SDK events and WebRTC events. For more information, see https://www.tencentcloud.com/document/product/647/37906?has_map=1
        :rtype: int
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def ParamOne(self):
        """The first event parameter, such as the video width.
        :rtype: int
        """
        return self._ParamOne

    @ParamOne.setter
    def ParamOne(self, ParamOne):
        self._ParamOne = ParamOne

    @property
    def ParamTwo(self):
        """The second event parameter, such as the video height.
        :rtype: int
        """
        return self._ParamTwo

    @ParamTwo.setter
    def ParamTwo(self, ParamTwo):
        self._ParamTwo = ParamTwo


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        self._EventId = params.get("EventId")
        self._ParamOne = params.get("ParamOne")
        self._ParamTwo = params.get("ParamTwo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxVideoUser(AbstractModel):
    """The information of the large video in screen sharing or floating layout mode.

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: The stream information.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self._UserMediaStream = None

    @property
    def UserMediaStream(self):
        """The stream information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuAudioParams(AbstractModel):
    """The audio parameters for relaying.

    """

    def __init__(self):
        r"""
        :param _AudioEncode: The audio encoding parameters.
        :type AudioEncode: :class:`tencentcloud.trtc.v20190722.models.AudioEncode`
        :param _SubscribeAudioList: The audio mix allowlist. For the `StartPublishCdnStream` API, if you do not pass this parameter or leave it empty, the audios of all anchors will be mixed. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current allowlist; if you pass in an empty string, the audios of all anchors will be mixed.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :type SubscribeAudioList: list of McuUserInfoParams
        :param _UnSubscribeAudioList: The audio mix blocklist. If you do not pass this parameter or leave it empty, there won’t be a blocklist. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current blocklist; if you pass in an empty string, the blocklist will be reset.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :type UnSubscribeAudioList: list of McuUserInfoParams
        """
        self._AudioEncode = None
        self._SubscribeAudioList = None
        self._UnSubscribeAudioList = None

    @property
    def AudioEncode(self):
        """The audio encoding parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioEncode`
        """
        return self._AudioEncode

    @AudioEncode.setter
    def AudioEncode(self, AudioEncode):
        self._AudioEncode = AudioEncode

    @property
    def SubscribeAudioList(self):
        """The audio mix allowlist. For the `StartPublishCdnStream` API, if you do not pass this parameter or leave it empty, the audios of all anchors will be mixed. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current allowlist; if you pass in an empty string, the audios of all anchors will be mixed.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :rtype: list of McuUserInfoParams
        """
        return self._SubscribeAudioList

    @SubscribeAudioList.setter
    def SubscribeAudioList(self, SubscribeAudioList):
        self._SubscribeAudioList = SubscribeAudioList

    @property
    def UnSubscribeAudioList(self):
        """The audio mix blocklist. If you do not pass this parameter or leave it empty, there won’t be a blocklist. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current blocklist; if you pass in an empty string, the blocklist will be reset.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :rtype: list of McuUserInfoParams
        """
        return self._UnSubscribeAudioList

    @UnSubscribeAudioList.setter
    def UnSubscribeAudioList(self, UnSubscribeAudioList):
        self._UnSubscribeAudioList = UnSubscribeAudioList


    def _deserialize(self, params):
        if params.get("AudioEncode") is not None:
            self._AudioEncode = AudioEncode()
            self._AudioEncode._deserialize(params.get("AudioEncode"))
        if params.get("SubscribeAudioList") is not None:
            self._SubscribeAudioList = []
            for item in params.get("SubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self._SubscribeAudioList.append(obj)
        if params.get("UnSubscribeAudioList") is not None:
            self._UnSubscribeAudioList = []
            for item in params.get("UnSubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self._UnSubscribeAudioList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuCustomCrop(AbstractModel):
    """The cropping parameters for mixed videos.

    """

    def __init__(self):
        r"""
        :param _LocationX: The horizontal offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :type LocationX: int
        :param _LocationY: The vertical offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :type LocationY: int
        :param _Width: The video width (pixels) after cropping. The sum of this parameter and `LocationX` cannot be greater than 10000.
        :type Width: int
        :param _Height: The video height (pixels) after cropping. The sum of this parameter and `LocationY` cannot be greater than 10000.
        :type Height: int
        """
        self._LocationX = None
        self._LocationY = None
        self._Width = None
        self._Height = None

    @property
    def LocationX(self):
        """The horizontal offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        """The vertical offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def Width(self):
        """The video width (pixels) after cropping. The sum of this parameter and `LocationX` cannot be greater than 10000.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """The video height (pixels) after cropping. The sum of this parameter and `LocationY` cannot be greater than 10000.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuFeedBackRoomParams(AbstractModel):
    """Parameters for relaying to a TRTC room.

    """

    def __init__(self):
        r"""
        :param _RoomId: The room ID.
        :type RoomId: str
        :param _RoomIdType: The ID type of the room to which streams are relayed. `0` indicates integer, and `1` indicates string.
        :type RoomIdType: int
        :param _UserId: The [user ID](https://www.tencentcloud.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :type UserId: str
        :param _UserSig: The signature (similar to login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://www.tencentcloud.com/document/product/647/38104).
        :type UserSig: str
        """
        self._RoomId = None
        self._RoomIdType = None
        self._UserId = None
        self._UserSig = None

    @property
    def RoomId(self):
        """The room ID.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        """The ID type of the room to which streams are relayed. `0` indicates integer, and `1` indicates string.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        """The [user ID](https://www.tencentcloud.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        """The signature (similar to login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://www.tencentcloud.com/document/product/647/38104).
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig


    def _deserialize(self, params):
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayout(AbstractModel):
    """The layout parameters.

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: The information of the stream that is displayed. If you do not pass this parameter, TRTC will display the videos of anchors in the room according to their room entry sequence.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        :param _ImageWidth: The video width (pixels). If you do not pass this parameter, 0 will be used.
        :type ImageWidth: int
        :param _ImageHeight: The video height (pixels). If you do not pass this parameter, 0 will be used.
        :type ImageHeight: int
        :param _LocationX: The horizontal offset (pixels) of the video. The sum of `LocationX` and `ImageWidth` cannot exceed the width of the canvas. If you do not pass this parameter, 0 will be used.
        :type LocationX: int
        :param _LocationY: The vertical offset of the video. The sum of `LocationY` and `ImageHeight` cannot exceed the height of the canvas. If you do not pass this parameter, 0 will be used.
        :type LocationY: int
        :param _ZOrder: The image layer of the video. If you do not pass this parameter, 0 will be used.
        :type ZOrder: int
        :param _RenderMode: The rendering mode of the video. 0 (the video is scaled and the excess parts are cropped), 1 (the video is scaled), 2 (the video is scaled and the blank spaces are filled with black bars). If you do not pass this parameter, 0 will be used.
        :type RenderMode: int
        :param _BackGroundColor: (Not supported yet) The background color of a video. Below are the values for some commonly used colors:
Red: `0xcc0033`
Yellow: `0xcc9900`
Green: `0xcccc33`
Blue: `0x99CCFF`
Black: `0x000000`
White: `0xFFFFFF`
Grey: `0x999999`
        :type BackGroundColor: str
        :param _BackgroundImageUrl: The URL of the background image for the video. This parameter allows you to specify an image to display when the user’s camera is turned off or before the user enters the room. If the dimensions of the image specified are different from those of the video window, the image will be stretched to fit the space. This parameter has a higher priority than `BackGroundColor`.
        :type BackgroundImageUrl: str
        :param _CustomCrop: Custom cropping.
        :type CustomCrop: :class:`tencentcloud.trtc.v20190722.models.McuCustomCrop`
        :param _BackgroundRenderMode: The display mode of the sub-background image during output: 0 for cropping, 1 for scaling and displaying the background, 2 for scaling and displaying the black background, 3 for proportional scaling. If not filled in, the default is 3.
        :type BackgroundRenderMode: int
        """
        self._UserMediaStream = None
        self._ImageWidth = None
        self._ImageHeight = None
        self._LocationX = None
        self._LocationY = None
        self._ZOrder = None
        self._RenderMode = None
        self._BackGroundColor = None
        self._BackgroundImageUrl = None
        self._CustomCrop = None
        self._BackgroundRenderMode = None

    @property
    def UserMediaStream(self):
        """The information of the stream that is displayed. If you do not pass this parameter, TRTC will display the videos of anchors in the room according to their room entry sequence.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream

    @property
    def ImageWidth(self):
        """The video width (pixels). If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        """The video height (pixels). If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def LocationX(self):
        """The horizontal offset (pixels) of the video. The sum of `LocationX` and `ImageWidth` cannot exceed the width of the canvas. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        """The vertical offset of the video. The sum of `LocationY` and `ImageHeight` cannot exceed the height of the canvas. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        """The image layer of the video. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def RenderMode(self):
        """The rendering mode of the video. 0 (the video is scaled and the excess parts are cropped), 1 (the video is scaled), 2 (the video is scaled and the blank spaces are filled with black bars). If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def BackGroundColor(self):
        """(Not supported yet) The background color of a video. Below are the values for some commonly used colors:
Red: `0xcc0033`
Yellow: `0xcc9900`
Green: `0xcccc33`
Blue: `0x99CCFF`
Black: `0x000000`
White: `0xFFFFFF`
Grey: `0x999999`
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        """The URL of the background image for the video. This parameter allows you to specify an image to display when the user’s camera is turned off or before the user enters the room. If the dimensions of the image specified are different from those of the video window, the image will be stretched to fit the space. This parameter has a higher priority than `BackGroundColor`.
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def CustomCrop(self):
        """Custom cropping.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuCustomCrop`
        """
        return self._CustomCrop

    @CustomCrop.setter
    def CustomCrop(self, CustomCrop):
        self._CustomCrop = CustomCrop

    @property
    def BackgroundRenderMode(self):
        """The display mode of the sub-background image during output: 0 for cropping, 1 for scaling and displaying the background, 2 for scaling and displaying the black background, 3 for proportional scaling. If not filled in, the default is 3.
        :rtype: int
        """
        return self._BackgroundRenderMode

    @BackgroundRenderMode.setter
    def BackgroundRenderMode(self, BackgroundRenderMode):
        self._BackgroundRenderMode = BackgroundRenderMode


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        self._ImageWidth = params.get("ImageWidth")
        self._ImageHeight = params.get("ImageHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._ZOrder = params.get("ZOrder")
        self._RenderMode = params.get("RenderMode")
        self._BackGroundColor = params.get("BackGroundColor")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("CustomCrop") is not None:
            self._CustomCrop = McuCustomCrop()
            self._CustomCrop._deserialize(params.get("CustomCrop"))
        self._BackgroundRenderMode = params.get("BackgroundRenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutParams(AbstractModel):
    """The layout parameters.

    """

    def __init__(self):
        r"""
        :param _MixLayoutMode: The layout mode. Valid values: 1 (floating), 2 (screen sharing), 3 (grid), 4 (custom). Floating, screen sharing, and grid are dynamic layouts. Custom layouts are static layouts.
        :type MixLayoutMode: int
        :param _PureAudioHoldPlaceMode: Whether to display users who publish only audio. 0: No; 1: Yes. This parameter is valid only if a dynamic layout is used. If you do not pass this parameter, 0 will be used.
        :type PureAudioHoldPlaceMode: int
        :param _MixLayoutList: The details of a custom layout.
        :type MixLayoutList: list of McuLayout
        :param _MaxVideoUser: The information of the large video in screen sharing or floating layout mode.
        :type MaxVideoUser: :class:`tencentcloud.trtc.v20190722.models.MaxVideoUser`
        :param _RenderMode: The image fill mode. This parameter is valid if the layout mode is screen sharing, floating, or grid. `0`: The image will be cropped. `1`: The image will be scaled. `2`: The image will be scaled and there may be black bars.
        :type RenderMode: int
        """
        self._MixLayoutMode = None
        self._PureAudioHoldPlaceMode = None
        self._MixLayoutList = None
        self._MaxVideoUser = None
        self._RenderMode = None

    @property
    def MixLayoutMode(self):
        """The layout mode. Valid values: 1 (floating), 2 (screen sharing), 3 (grid), 4 (custom). Floating, screen sharing, and grid are dynamic layouts. Custom layouts are static layouts.
        :rtype: int
        """
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def PureAudioHoldPlaceMode(self):
        """Whether to display users who publish only audio. 0: No; 1: Yes. This parameter is valid only if a dynamic layout is used. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._PureAudioHoldPlaceMode

    @PureAudioHoldPlaceMode.setter
    def PureAudioHoldPlaceMode(self, PureAudioHoldPlaceMode):
        self._PureAudioHoldPlaceMode = PureAudioHoldPlaceMode

    @property
    def MixLayoutList(self):
        """The details of a custom layout.
        :rtype: list of McuLayout
        """
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def MaxVideoUser(self):
        """The information of the large video in screen sharing or floating layout mode.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MaxVideoUser`
        """
        return self._MaxVideoUser

    @MaxVideoUser.setter
    def MaxVideoUser(self, MaxVideoUser):
        self._MaxVideoUser = MaxVideoUser

    @property
    def RenderMode(self):
        """The image fill mode. This parameter is valid if the layout mode is screen sharing, floating, or grid. `0`: The image will be cropped. `1`: The image will be scaled. `2`: The image will be scaled and there may be black bars.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode


    def _deserialize(self, params):
        self._MixLayoutMode = params.get("MixLayoutMode")
        self._PureAudioHoldPlaceMode = params.get("PureAudioHoldPlaceMode")
        if params.get("MixLayoutList") is not None:
            self._MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = McuLayout()
                obj._deserialize(item)
                self._MixLayoutList.append(obj)
        if params.get("MaxVideoUser") is not None:
            self._MaxVideoUser = MaxVideoUser()
            self._MaxVideoUser._deserialize(params.get("MaxVideoUser"))
        self._RenderMode = params.get("RenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutVolume(AbstractModel):
    """The SEI parameters for audio volume layout. You can specify the `AppData` and `PayloadType`.
    This parameter may be empty, in which case the default SEI parameters for audio volume layout will be used.

    """

    def __init__(self):
        r"""
        :param _AppData: The application data, which will be embedded in the `app_data` field of the custom SEI. It must be shorter than 4,096 characters.
        :type AppData: str
        :param _PayloadType: The payload type of the SEI message. The default is 100. Value range: 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :type PayloadType: int
        :param _Interval: The SEI sending interval (milliseconds). The default value is 1000.
        :type Interval: int
        :param _FollowIdr: Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :type FollowIdr: int
        """
        self._AppData = None
        self._PayloadType = None
        self._Interval = None
        self._FollowIdr = None

    @property
    def AppData(self):
        """The application data, which will be embedded in the `app_data` field of the custom SEI. It must be shorter than 4,096 characters.
        :rtype: str
        """
        return self._AppData

    @AppData.setter
    def AppData(self, AppData):
        self._AppData = AppData

    @property
    def PayloadType(self):
        """The payload type of the SEI message. The default is 100. Value range: 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :rtype: int
        """
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def Interval(self):
        """The SEI sending interval (milliseconds). The default value is 1000.
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
        """Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :rtype: int
        """
        return self._FollowIdr

    @FollowIdr.setter
    def FollowIdr(self, FollowIdr):
        self._FollowIdr = FollowIdr


    def _deserialize(self, params):
        self._AppData = params.get("AppData")
        self._PayloadType = params.get("PayloadType")
        self._Interval = params.get("Interval")
        self._FollowIdr = params.get("FollowIdr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPassThrough(AbstractModel):
    """The custom pass-through SEI.

    """

    def __init__(self):
        r"""
        :param _PayloadContent: The payload of the pass-through SEI.
        :type PayloadContent: str
        :param _PayloadType: The payload type of the SEI message. Value range: 5 and 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :type PayloadType: int
        :param _PayloadUuid: This parameter is required only if `PayloadType` is 5. It must be a 32-character hexadecimal string. If `PayloadType` is not 5, this parameter will be ignored.
        :type PayloadUuid: str
        :param _Interval: The SEI sending interval (milliseconds). The default value is 1000.
        :type Interval: int
        :param _FollowIdr: Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :type FollowIdr: int
        """
        self._PayloadContent = None
        self._PayloadType = None
        self._PayloadUuid = None
        self._Interval = None
        self._FollowIdr = None

    @property
    def PayloadContent(self):
        """The payload of the pass-through SEI.
        :rtype: str
        """
        return self._PayloadContent

    @PayloadContent.setter
    def PayloadContent(self, PayloadContent):
        self._PayloadContent = PayloadContent

    @property
    def PayloadType(self):
        """The payload type of the SEI message. Value range: 5 and 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :rtype: int
        """
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def PayloadUuid(self):
        """This parameter is required only if `PayloadType` is 5. It must be a 32-character hexadecimal string. If `PayloadType` is not 5, this parameter will be ignored.
        :rtype: str
        """
        return self._PayloadUuid

    @PayloadUuid.setter
    def PayloadUuid(self, PayloadUuid):
        self._PayloadUuid = PayloadUuid

    @property
    def Interval(self):
        """The SEI sending interval (milliseconds). The default value is 1000.
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
        """Valid values: `1`: SEI is guaranteed when keyframes are sent; `0` (default): SEI is not guaranteed when keyframes are sent.
        :rtype: int
        """
        return self._FollowIdr

    @FollowIdr.setter
    def FollowIdr(self, FollowIdr):
        self._FollowIdr = FollowIdr


    def _deserialize(self, params):
        self._PayloadContent = params.get("PayloadContent")
        self._PayloadType = params.get("PayloadType")
        self._PayloadUuid = params.get("PayloadUuid")
        self._Interval = params.get("Interval")
        self._FollowIdr = params.get("FollowIdr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPublishCdnParam(AbstractModel):
    """The relaying parameters.

    """

    def __init__(self):
        r"""
        :param _PublishCdnUrl: The URLs of the CDNs to relay to.
        :type PublishCdnUrl: str
        :param _IsTencentCdn: Whether to relay to Tencent Cloud’s CDN. `0`: Third-party CDN; `1` (default): Tencent Cloud’s CDN. Relaying to a third-party CDN will incur fees. To avoid unexpected charges, we recommend you pass in a specific value. For details, see the API document.
        :type IsTencentCdn: int
        """
        self._PublishCdnUrl = None
        self._IsTencentCdn = None

    @property
    def PublishCdnUrl(self):
        """The URLs of the CDNs to relay to.
        :rtype: str
        """
        return self._PublishCdnUrl

    @PublishCdnUrl.setter
    def PublishCdnUrl(self, PublishCdnUrl):
        self._PublishCdnUrl = PublishCdnUrl

    @property
    def IsTencentCdn(self):
        """Whether to relay to Tencent Cloud’s CDN. `0`: Third-party CDN; `1` (default): Tencent Cloud’s CDN. Relaying to a third-party CDN will incur fees. To avoid unexpected charges, we recommend you pass in a specific value. For details, see the API document.
        :rtype: int
        """
        return self._IsTencentCdn

    @IsTencentCdn.setter
    def IsTencentCdn(self, IsTencentCdn):
        self._IsTencentCdn = IsTencentCdn


    def _deserialize(self, params):
        self._PublishCdnUrl = params.get("PublishCdnUrl")
        self._IsTencentCdn = params.get("IsTencentCdn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuSeiParams(AbstractModel):
    """The stream mixing SEI parameters.

    """

    def __init__(self):
        r"""
        :param _LayoutVolume: The audio volume layout SEI.
        :type LayoutVolume: :class:`tencentcloud.trtc.v20190722.models.McuLayoutVolume`
        :param _PassThrough: The pass-through SEI.
        :type PassThrough: :class:`tencentcloud.trtc.v20190722.models.McuPassThrough`
        """
        self._LayoutVolume = None
        self._PassThrough = None

    @property
    def LayoutVolume(self):
        """The audio volume layout SEI.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuLayoutVolume`
        """
        return self._LayoutVolume

    @LayoutVolume.setter
    def LayoutVolume(self, LayoutVolume):
        self._LayoutVolume = LayoutVolume

    @property
    def PassThrough(self):
        """The pass-through SEI.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuPassThrough`
        """
        return self._PassThrough

    @PassThrough.setter
    def PassThrough(self, PassThrough):
        self._PassThrough = PassThrough


    def _deserialize(self, params):
        if params.get("LayoutVolume") is not None:
            self._LayoutVolume = McuLayoutVolume()
            self._LayoutVolume._deserialize(params.get("LayoutVolume"))
        if params.get("PassThrough") is not None:
            self._PassThrough = McuPassThrough()
            self._PassThrough._deserialize(params.get("PassThrough"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuUserInfoParams(AbstractModel):
    """The users whose streams are mixed.

    """

    def __init__(self):
        r"""
        :param _UserInfo: The user information.
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        self._UserInfo = None

    @property
    def UserInfo(self):
        """The user information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = MixUserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuVideoParams(AbstractModel):
    """The video parameters for relaying.

    """

    def __init__(self):
        r"""
        :param _VideoEncode: The video encoding parameters.
        :type VideoEncode: :class:`tencentcloud.trtc.v20190722.models.VideoEncode`
        :param _LayoutParams: The layout parameters.
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.McuLayoutParams`
        :param _BackGroundColor: The canvas color. Below are the values for some common colors:
Red: 0xcc0033
Yellow: 0xcc9900
Green: 0xcccc33
Blue: 0x99CCFF
Black: 0x000000
White: 0xFFFFFF
Grey: 0x999999
        :type BackGroundColor: str
        :param _BackgroundImageUrl: The URL of the background image for the canvas. This parameter has a higher priority than `BackGroundColor`.
        :type BackgroundImageUrl: str
        :param _WaterMarkList: The watermark information for the mixed stream.
        :type WaterMarkList: list of McuWaterMarkParams
        :param _BackgroundRenderMode: Background image display mode during output: 0 for crop, 1 for scale and display with black background, 2 for proportional scaling. The backend default is proportional scaling.
        :type BackgroundRenderMode: int
        """
        self._VideoEncode = None
        self._LayoutParams = None
        self._BackGroundColor = None
        self._BackgroundImageUrl = None
        self._WaterMarkList = None
        self._BackgroundRenderMode = None

    @property
    def VideoEncode(self):
        """The video encoding parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoEncode`
        """
        return self._VideoEncode

    @VideoEncode.setter
    def VideoEncode(self, VideoEncode):
        self._VideoEncode = VideoEncode

    @property
    def LayoutParams(self):
        """The layout parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuLayoutParams`
        """
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def BackGroundColor(self):
        """The canvas color. Below are the values for some common colors:
Red: 0xcc0033
Yellow: 0xcc9900
Green: 0xcccc33
Blue: 0x99CCFF
Black: 0x000000
White: 0xFFFFFF
Grey: 0x999999
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        """The URL of the background image for the canvas. This parameter has a higher priority than `BackGroundColor`.
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def WaterMarkList(self):
        """The watermark information for the mixed stream.
        :rtype: list of McuWaterMarkParams
        """
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def BackgroundRenderMode(self):
        """Background image display mode during output: 0 for crop, 1 for scale and display with black background, 2 for proportional scaling. The backend default is proportional scaling.
        :rtype: int
        """
        return self._BackgroundRenderMode

    @BackgroundRenderMode.setter
    def BackgroundRenderMode(self, BackgroundRenderMode):
        self._BackgroundRenderMode = BackgroundRenderMode


    def _deserialize(self, params):
        if params.get("VideoEncode") is not None:
            self._VideoEncode = VideoEncode()
            self._VideoEncode._deserialize(params.get("VideoEncode"))
        if params.get("LayoutParams") is not None:
            self._LayoutParams = McuLayoutParams()
            self._LayoutParams._deserialize(params.get("LayoutParams"))
        self._BackGroundColor = params.get("BackGroundColor")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("WaterMarkList") is not None:
            self._WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = McuWaterMarkParams()
                obj._deserialize(item)
                self._WaterMarkList.append(obj)
        self._BackgroundRenderMode = params.get("BackgroundRenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkImage(AbstractModel):
    """The information of the watermark image.

    """

    def __init__(self):
        r"""
        :param _WaterMarkUrl: The URL of the watermark image, which must be in PNG, JPG, or JPEG format and cannot exceed 5 MB.
        :type WaterMarkUrl: str
        :param _WaterMarkWidth: The watermark width (pixels).
        :type WaterMarkWidth: int
        :param _WaterMarkHeight: The watermark height (pixels).
        :type WaterMarkHeight: int
        :param _LocationX: The horizontal offset (pixels) of the watermark.
        :type LocationX: int
        :param _LocationY: The vertical offset (pixels) of the watermark.
        :type LocationY: int
        :param _ZOrder: The image layer of the watermark. If you do not pass this parameter, 0 will be used.
        :type ZOrder: int
        """
        self._WaterMarkUrl = None
        self._WaterMarkWidth = None
        self._WaterMarkHeight = None
        self._LocationX = None
        self._LocationY = None
        self._ZOrder = None

    @property
    def WaterMarkUrl(self):
        """The URL of the watermark image, which must be in PNG, JPG, or JPEG format and cannot exceed 5 MB.
        :rtype: str
        """
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def WaterMarkWidth(self):
        """The watermark width (pixels).
        :rtype: int
        """
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        """The watermark height (pixels).
        :rtype: int
        """
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        """The horizontal offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        """The vertical offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        """The image layer of the watermark. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder


    def _deserialize(self, params):
        self._WaterMarkUrl = params.get("WaterMarkUrl")
        self._WaterMarkWidth = params.get("WaterMarkWidth")
        self._WaterMarkHeight = params.get("WaterMarkHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._ZOrder = params.get("ZOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkParams(AbstractModel):
    """The Watermark information.

    """

    def __init__(self):
        r"""
        :param _WaterMarkType: The watermark type. Valid values: `0` (default): Image; `1`: Text.
        :type WaterMarkType: int
        :param _WaterMarkImage: The watermark image information. This parameter is required if `WaterMarkType` is 0.
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkImage`
        :param _WaterMarkText: The text watermark configuration. This parameter is required if `WaterMarkType` is `1`.
        :type WaterMarkText: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkText`
        """
        self._WaterMarkType = None
        self._WaterMarkImage = None
        self._WaterMarkText = None

    @property
    def WaterMarkType(self):
        """The watermark type. Valid values: `0` (default): Image; `1`: Text.
        :rtype: int
        """
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        """The watermark image information. This parameter is required if `WaterMarkType` is 0.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkImage`
        """
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkText(self):
        """The text watermark configuration. This parameter is required if `WaterMarkType` is `1`.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkText`
        """
        return self._WaterMarkText

    @WaterMarkText.setter
    def WaterMarkText(self, WaterMarkText):
        self._WaterMarkText = WaterMarkText


    def _deserialize(self, params):
        self._WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self._WaterMarkImage = McuWaterMarkImage()
            self._WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        if params.get("WaterMarkText") is not None:
            self._WaterMarkText = McuWaterMarkText()
            self._WaterMarkText._deserialize(params.get("WaterMarkText"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkText(AbstractModel):
    """The text watermark configuration.

    """

    def __init__(self):
        r"""
        :param _Text: The text.
        :type Text: str
        :param _WaterMarkWidth: The watermark width (pixels).
        :type WaterMarkWidth: int
        :param _WaterMarkHeight: The watermark height (pixels).
        :type WaterMarkHeight: int
        :param _LocationX: The horizontal offset (pixels) of the watermark.
        :type LocationX: int
        :param _LocationY: The vertical offset (pixels) of the watermark.
        :type LocationY: int
        :param _FontSize: The font size.
        :type FontSize: int
        :param _FontColor: The text color. The default color is white. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :type FontColor: str
        :param _BackGroundColor: The text fill color. If you do not specify this parameter, the fill color will be transparent. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :type BackGroundColor: str
        """
        self._Text = None
        self._WaterMarkWidth = None
        self._WaterMarkHeight = None
        self._LocationX = None
        self._LocationY = None
        self._FontSize = None
        self._FontColor = None
        self._BackGroundColor = None

    @property
    def Text(self):
        """The text.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def WaterMarkWidth(self):
        """The watermark width (pixels).
        :rtype: int
        """
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        """The watermark height (pixels).
        :rtype: int
        """
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        """The horizontal offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        """The vertical offset (pixels) of the watermark.
        :rtype: int
        """
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def FontSize(self):
        """The font size.
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        """The text color. The default color is white. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
        """The text fill color. If you do not specify this parameter, the fill color will be transparent. Values for some commonly used colors: Red: `0xcc0033`; yellow: `0xcc9900`; green: `0xcccc33`; blue: `0x99CCFF`; black: `0x000000`; white: `0xFFFFFF`; gray: `0x999999`.	
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._WaterMarkWidth = params.get("WaterMarkWidth")
        self._WaterMarkHeight = params.get("WaterMarkHeight")
        self._LocationX = params.get("LocationX")
        self._LocationY = params.get("LocationY")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        self._BackGroundColor = params.get("BackGroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayout(AbstractModel):
    """The custom layout parameters.

    """

    def __init__(self):
        r"""
        :param _Top: The Y axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas height.
        :type Top: int
        :param _Left: The X axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas width.
        :type Left: int
        :param _Width: The relative width of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :type Width: int
        :param _Height: The relative height of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :type Height: int
        :param _UserId: The user ID (string) of the anchor whose video is shown in the window. If you do not set this parameter, anchors’ videos will be shown in their room entry sequence.
        :type UserId: str
        :param _Alpha: The degree of transparency of the canvas. Value range: [0, 255]. 0 means fully opaque, and 255 means fully transparent.
        :type Alpha: int
        :param _RenderMode: 0: Stretch. In this mode, the image is stretched to fill the space available. The whole image is visible after scaling. However, if the original aspect ratio is different from the target, the image may be distorted.

1: Crop (default). In this mode, if the original aspect ratio is different from the target, the image will be cropped according to the target before being stretched to fill the space available. The image will not be distorted.

2: Blank. This mode stretches the image while keeping its original aspect ratio. If the original aspect ratio is different from the target, there may be blank spaces to the top and bottom or to the left and right of the window.

3: Smart stretch. This mode is similar to the crop mode, except that it restricts cropping to 20% of the image’s width or height at most.
        :type RenderMode: int
        :param _MediaId: The type of the stream subscribed to.
0: Primary stream (default)
1: Substream
        :type MediaId: int
        :param _ImageLayer: The image layer. 0 is the default value and means the bottommost layer.
        :type ImageLayer: int
        :param _SubBackgroundImage: The URL of the background image for a window. The image must be in JPG or PNG format and cannot be larger than 5 MB. If the image’s aspect ratio is different from that of the window, the image will be rendered according to the value of `RenderMode`.
        :type SubBackgroundImage: str
        """
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None
        self._UserId = None
        self._Alpha = None
        self._RenderMode = None
        self._MediaId = None
        self._ImageLayer = None
        self._SubBackgroundImage = None

    @property
    def Top(self):
        """The Y axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas height.
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        """The X axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas width.
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        """The relative width of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """The relative height of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def UserId(self):
        """The user ID (string) of the anchor whose video is shown in the window. If you do not set this parameter, anchors’ videos will be shown in their room entry sequence.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Alpha(self):
        """The degree of transparency of the canvas. Value range: [0, 255]. 0 means fully opaque, and 255 means fully transparent.
        :rtype: int
        """
        return self._Alpha

    @Alpha.setter
    def Alpha(self, Alpha):
        self._Alpha = Alpha

    @property
    def RenderMode(self):
        """0: Stretch. In this mode, the image is stretched to fill the space available. The whole image is visible after scaling. However, if the original aspect ratio is different from the target, the image may be distorted.

1: Crop (default). In this mode, if the original aspect ratio is different from the target, the image will be cropped according to the target before being stretched to fill the space available. The image will not be distorted.

2: Blank. This mode stretches the image while keeping its original aspect ratio. If the original aspect ratio is different from the target, there may be blank spaces to the top and bottom or to the left and right of the window.

3: Smart stretch. This mode is similar to the crop mode, except that it restricts cropping to 20% of the image’s width or height at most.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MediaId(self):
        """The type of the stream subscribed to.
0: Primary stream (default)
1: Substream
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def ImageLayer(self):
        """The image layer. 0 is the default value and means the bottommost layer.
        :rtype: int
        """
        return self._ImageLayer

    @ImageLayer.setter
    def ImageLayer(self, ImageLayer):
        self._ImageLayer = ImageLayer

    @property
    def SubBackgroundImage(self):
        """The URL of the background image for a window. The image must be in JPG or PNG format and cannot be larger than 5 MB. If the image’s aspect ratio is different from that of the window, the image will be rendered according to the value of `RenderMode`.
        :rtype: str
        """
        return self._SubBackgroundImage

    @SubBackgroundImage.setter
    def SubBackgroundImage(self, SubBackgroundImage):
        self._SubBackgroundImage = SubBackgroundImage


    def _deserialize(self, params):
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._UserId = params.get("UserId")
        self._Alpha = params.get("Alpha")
        self._RenderMode = params.get("RenderMode")
        self._MediaId = params.get("MediaId")
        self._ImageLayer = params.get("ImageLayer")
        self._SubBackgroundImage = params.get("SubBackgroundImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayoutParams(AbstractModel):
    """The layout parameters for mixed-stream recording.

    """

    def __init__(self):
        r"""
        :param _MixLayoutMode: Layout mode:
1: Floating
2: Screen sharing
3: Grid (default)
4: Custom

Floating: By default, the video of the first anchor (you can also specify an anchor) who enters the room is scaled to fill the screen. When other anchors enter the room, their videos appear smaller and are superimposed over the large video from left to right starting from the bottom of the canvas according to their room entry sequence. If the total number of videos is 17 or less, there will be four windows in each row (4 x 4); if it is greater than 17, there will be five windows in each row (5 x 5). Up to 25 videos can be displayed. A user who publishes only audio will still be displayed in one window.

Screen sharing: The video of a specified anchor occupies a larger part of the canvas on the left side (if you do not specify an anchor, the left window will display the canvas background). The videos of other anchors are smaller and are positioned on the right side. If the total number of videos is 17 or less, the small videos are positioned from top to bottom in up to two columns on the right side, with eight videos per column at most. If there are more than 17 videos, the additional videos are positioned at the bottom of the canvas from left to right. Up to 25 videos can be displayed. A user who publishes only audio will still be displayed in one window.

Grid: The videos of anchors are scaled and positioned automatically according to the total number of anchors in a room. Each video has the same size. Up to 25 videos can be displayed.

Custom: Specify the layout of videos by using the `MixLayoutList` parameter.
        :type MixLayoutMode: int
        :param _MixLayoutList: The custom layout details. This parameter is valid if `MixLayoutMode` is set to `4`. Up to 25 videos can be displayed.
        :type MixLayoutList: list of MixLayout
        :param _BackGroundColor: The background color, which is a hexadecimal value (starting with "#", followed by the color value) converted from an 8-bit RGB value. For example, the RGB value of orange is `R:255 G:165 B:0`, and its hexadecimal value is `#FFA500`. The default color is black.
        :type BackGroundColor: str
        :param _MaxResolutionUserId: The user whose video is displayed in the big window. This parameter is valid if `MixLayoutMode` is set to `1` (floating) or `2` (screen sharing). If it is left empty, the first anchor entering the room is displayed in the big window in the floating mode and the canvas background is displayed in the screen sharing mode.
        :type MaxResolutionUserId: str
        :param _MediaId: The stream type.
0: Primary stream (default)
1: Substream (screen sharing stream)
This parameter specifies the type of the stream displayed in the big window. If it appears in `MixLayoutList`, it indicates the type of the stream of a specified user.
        :type MediaId: int
        :param _BackgroundImageUrl: The URL of the background image, which cannot contain Chinese characters. The image must be in JPG or PNG format and cannot be larger than 5 MB.
        :type BackgroundImageUrl: str
        :param _PlaceHolderMode: `1` means to use placeholders, and `0` (default) means to not use placeholders. If this parameter is set to `1`, when a user is not publishing video, a placeholder image will be displayed in the window reserved for the user.
        :type PlaceHolderMode: int
        :param _BackgroundImageRenderMode: The render mode to use when the aspect ratio of a video is different from that of the window. This parameter is defined the same as `RenderMode` in `MixLayoufList`.
        :type BackgroundImageRenderMode: int
        :param _DefaultSubBackgroundImage: The URL of the background image for a window. The image must be in JPG or PNG format and cannot be larger than 5 MB. If the image’s aspect ratio is different from that of the window, the image will be rendered according to the value of `RenderMode`.
        :type DefaultSubBackgroundImage: str
        :param _WaterMarkList: The watermark layout. Up to 25 watermarks are supported.
        :type WaterMarkList: list of WaterMark
        :param _RenderMode: The render mode to use when the aspect ratio of a video is different from that of the window. This parameter is invalid if a custom layout is used. It is defined the same as `RenderMode` in `MixLayoufList`.
        :type RenderMode: int
        :param _MaxResolutionUserAlign: This parameter is valid only if the screen sharing layout is used. If you set it to `1`, the large video window will appear on the right and the small window on the left. The default value is `0`.
        :type MaxResolutionUserAlign: int
        """
        self._MixLayoutMode = None
        self._MixLayoutList = None
        self._BackGroundColor = None
        self._MaxResolutionUserId = None
        self._MediaId = None
        self._BackgroundImageUrl = None
        self._PlaceHolderMode = None
        self._BackgroundImageRenderMode = None
        self._DefaultSubBackgroundImage = None
        self._WaterMarkList = None
        self._RenderMode = None
        self._MaxResolutionUserAlign = None

    @property
    def MixLayoutMode(self):
        """Layout mode:
1: Floating
2: Screen sharing
3: Grid (default)
4: Custom

Floating: By default, the video of the first anchor (you can also specify an anchor) who enters the room is scaled to fill the screen. When other anchors enter the room, their videos appear smaller and are superimposed over the large video from left to right starting from the bottom of the canvas according to their room entry sequence. If the total number of videos is 17 or less, there will be four windows in each row (4 x 4); if it is greater than 17, there will be five windows in each row (5 x 5). Up to 25 videos can be displayed. A user who publishes only audio will still be displayed in one window.

Screen sharing: The video of a specified anchor occupies a larger part of the canvas on the left side (if you do not specify an anchor, the left window will display the canvas background). The videos of other anchors are smaller and are positioned on the right side. If the total number of videos is 17 or less, the small videos are positioned from top to bottom in up to two columns on the right side, with eight videos per column at most. If there are more than 17 videos, the additional videos are positioned at the bottom of the canvas from left to right. Up to 25 videos can be displayed. A user who publishes only audio will still be displayed in one window.

Grid: The videos of anchors are scaled and positioned automatically according to the total number of anchors in a room. Each video has the same size. Up to 25 videos can be displayed.

Custom: Specify the layout of videos by using the `MixLayoutList` parameter.
        :rtype: int
        """
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def MixLayoutList(self):
        """The custom layout details. This parameter is valid if `MixLayoutMode` is set to `4`. Up to 25 videos can be displayed.
        :rtype: list of MixLayout
        """
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def BackGroundColor(self):
        """The background color, which is a hexadecimal value (starting with "#", followed by the color value) converted from an 8-bit RGB value. For example, the RGB value of orange is `R:255 G:165 B:0`, and its hexadecimal value is `#FFA500`. The default color is black.
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def MaxResolutionUserId(self):
        """The user whose video is displayed in the big window. This parameter is valid if `MixLayoutMode` is set to `1` (floating) or `2` (screen sharing). If it is left empty, the first anchor entering the room is displayed in the big window in the floating mode and the canvas background is displayed in the screen sharing mode.
        :rtype: str
        """
        return self._MaxResolutionUserId

    @MaxResolutionUserId.setter
    def MaxResolutionUserId(self, MaxResolutionUserId):
        self._MaxResolutionUserId = MaxResolutionUserId

    @property
    def MediaId(self):
        """The stream type.
0: Primary stream (default)
1: Substream (screen sharing stream)
This parameter specifies the type of the stream displayed in the big window. If it appears in `MixLayoutList`, it indicates the type of the stream of a specified user.
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def BackgroundImageUrl(self):
        """The URL of the background image, which cannot contain Chinese characters. The image must be in JPG or PNG format and cannot be larger than 5 MB.
        :rtype: str
        """
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def PlaceHolderMode(self):
        """`1` means to use placeholders, and `0` (default) means to not use placeholders. If this parameter is set to `1`, when a user is not publishing video, a placeholder image will be displayed in the window reserved for the user.
        :rtype: int
        """
        return self._PlaceHolderMode

    @PlaceHolderMode.setter
    def PlaceHolderMode(self, PlaceHolderMode):
        self._PlaceHolderMode = PlaceHolderMode

    @property
    def BackgroundImageRenderMode(self):
        """The render mode to use when the aspect ratio of a video is different from that of the window. This parameter is defined the same as `RenderMode` in `MixLayoufList`.
        :rtype: int
        """
        return self._BackgroundImageRenderMode

    @BackgroundImageRenderMode.setter
    def BackgroundImageRenderMode(self, BackgroundImageRenderMode):
        self._BackgroundImageRenderMode = BackgroundImageRenderMode

    @property
    def DefaultSubBackgroundImage(self):
        """The URL of the background image for a window. The image must be in JPG or PNG format and cannot be larger than 5 MB. If the image’s aspect ratio is different from that of the window, the image will be rendered according to the value of `RenderMode`.
        :rtype: str
        """
        return self._DefaultSubBackgroundImage

    @DefaultSubBackgroundImage.setter
    def DefaultSubBackgroundImage(self, DefaultSubBackgroundImage):
        self._DefaultSubBackgroundImage = DefaultSubBackgroundImage

    @property
    def WaterMarkList(self):
        """The watermark layout. Up to 25 watermarks are supported.
        :rtype: list of WaterMark
        """
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def RenderMode(self):
        """The render mode to use when the aspect ratio of a video is different from that of the window. This parameter is invalid if a custom layout is used. It is defined the same as `RenderMode` in `MixLayoufList`.
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MaxResolutionUserAlign(self):
        """This parameter is valid only if the screen sharing layout is used. If you set it to `1`, the large video window will appear on the right and the small window on the left. The default value is `0`.
        :rtype: int
        """
        return self._MaxResolutionUserAlign

    @MaxResolutionUserAlign.setter
    def MaxResolutionUserAlign(self, MaxResolutionUserAlign):
        self._MaxResolutionUserAlign = MaxResolutionUserAlign


    def _deserialize(self, params):
        self._MixLayoutMode = params.get("MixLayoutMode")
        if params.get("MixLayoutList") is not None:
            self._MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = MixLayout()
                obj._deserialize(item)
                self._MixLayoutList.append(obj)
        self._BackGroundColor = params.get("BackGroundColor")
        self._MaxResolutionUserId = params.get("MaxResolutionUserId")
        self._MediaId = params.get("MediaId")
        self._BackgroundImageUrl = params.get("BackgroundImageUrl")
        self._PlaceHolderMode = params.get("PlaceHolderMode")
        self._BackgroundImageRenderMode = params.get("BackgroundImageRenderMode")
        self._DefaultSubBackgroundImage = params.get("DefaultSubBackgroundImage")
        if params.get("WaterMarkList") is not None:
            self._WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = WaterMark()
                obj._deserialize(item)
                self._WaterMarkList.append(obj)
        self._RenderMode = params.get("RenderMode")
        self._MaxResolutionUserAlign = params.get("MaxResolutionUserAlign")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixTranscodeParams(AbstractModel):
    """The audio and video parameters for recording.

    """

    def __init__(self):
        r"""
        :param _VideoParams: The video transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        :param _AudioParams: The audio transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        self._VideoParams = None
        self._AudioParams = None

    @property
    def VideoParams(self):
        """The video transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def AudioParams(self):
        """The audio transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams


    def _deserialize(self, params):
        if params.get("VideoParams") is not None:
            self._VideoParams = VideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("AudioParams") is not None:
            self._AudioParams = AudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixUserInfo(AbstractModel):
    """The user information.

    """

    def __init__(self):
        r"""
        :param _UserId: User ID.
        :type UserId: str
        :param _RoomId: If a dynamic layout is used, the value of this parameter should be the ID of the main room. If a custom layout is used, the value of this parameter should be the same as the room ID in `MixLayoutList`.
        :type RoomId: str
        :param _RoomIdType: The type of the `RoomId` parameter. 0: integer; 1: string.
        :type RoomIdType: int
        """
        self._UserId = None
        self._RoomId = None
        self._RoomIdType = None

    @property
    def UserId(self):
        """User ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        """If a dynamic layout is used, the value of this parameter should be the ID of the main room. If a custom layout is used, the value of this parameter should be the same as the room ID in `MixLayoutList`.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        """The type of the `RoomId` parameter. 0: integer; 1: string.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingRequest(AbstractModel):
    """ModifyCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param _TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        :param _MixLayoutParams: The new stream mixing layout to use.
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param _SubscribeStreamUserIds: The allowlist/blocklist for stream subscription.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self._SdkAppId = None
        self._TaskId = None
        self._MixLayoutParams = None
        self._SubscribeStreamUserIds = None

    @property
    def SdkAppId(self):
        """The `SDKAppID` of the room whose streams are recorded.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The unique ID of the recording task, which is returned after recording starts successfully.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MixLayoutParams(self):
        """The new stream mixing layout to use.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        """
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def SubscribeStreamUserIds(self):
        """The allowlist/blocklist for stream subscription.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        if params.get("MixLayoutParams") is not None:
            self._MixLayoutParams = MixLayoutParams()
            self._MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingResponse(AbstractModel):
    """ModifyCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class QualityData(AbstractModel):
    """The quality data returned by ES.

    """

    def __init__(self):
        r"""
        :param _Content: The quality data.
        :type Content: list of TimeValue
        :param _UserId: The user ID.
        :type UserId: str
        :param _PeerId: The remote user ID. An empty string indicates that the data is upstream data.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PeerId: str
        :param _DataType: The data type.
        :type DataType: str
        """
        self._Content = None
        self._UserId = None
        self._PeerId = None
        self._DataType = None

    @property
    def Content(self):
        """The quality data.
        :rtype: list of TimeValue
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def UserId(self):
        """The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PeerId(self):
        """The remote user ID. An empty string indicates that the data is upstream data.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def DataType(self):
        """The data type.
        :rtype: str
        """
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self._Content.append(obj)
        self._UserId = params.get("UserId")
        self._PeerId = params.get("PeerId")
        self._DataType = params.get("DataType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeConfig(AbstractModel):
    """Configuration used by speech recognition

    """

    def __init__(self):
        r"""
        :param _Language: The supported languages for speech recognition are as follows, with the default being "zh" for Chinese. The values for the `Language` field follow the [ISO639](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) standard. Here is the full list of supported languages:

1. Chinese = "zh"
2. Chinese_TW = "zh-TW"
3. Chinese_DIALECT = "zh-dialect"
4. English = "en"
5. Vietnamese = "vi"
6. Japanese = "ja"
7. Korean = "ko"
8. Indonesian = "id"
9. Thai = "th"
10. Portuguese = "pt"
11. Turkish = "tr"
12. Arabic = "ar"
13. Spanish = "es"
14. Hindi = "hi"
15. French = "fr"
16. Malay = "ms"
17. Filipino = "fil"
18. German = "de"
19. Italian = "it"
20. Russian = "ru"

**Note:** If the language you need is not listed, please contact our technical support team.
        :type Language: str
        :param _AlternativeLanguage: Initiate fuzzy recognition to replace additional language types. Fill in up to 3 language types. Note: When Language is specified as "zh-dialect", fuzzy recognition is not supported and this field is invalid.
        :type AlternativeLanguage: list of str
        """
        self._Language = None
        self._AlternativeLanguage = None

    @property
    def Language(self):
        """The supported languages for speech recognition are as follows, with the default being "zh" for Chinese. The values for the `Language` field follow the [ISO639](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) standard. Here is the full list of supported languages:

1. Chinese = "zh"
2. Chinese_TW = "zh-TW"
3. Chinese_DIALECT = "zh-dialect"
4. English = "en"
5. Vietnamese = "vi"
6. Japanese = "ja"
7. Korean = "ko"
8. Indonesian = "id"
9. Thai = "th"
10. Portuguese = "pt"
11. Turkish = "tr"
12. Arabic = "ar"
13. Spanish = "es"
14. Hindi = "hi"
15. French = "fr"
16. Malay = "ms"
17. Filipino = "fil"
18. German = "de"
19. Italian = "it"
20. Russian = "ru"

**Note:** If the language you need is not listed, please contact our technical support team.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def AlternativeLanguage(self):
        """Initiate fuzzy recognition to replace additional language types. Fill in up to 3 language types. Note: When Language is specified as "zh-dialect", fuzzy recognition is not supported and this field is invalid.
        :rtype: list of str
        """
        return self._AlternativeLanguage

    @AlternativeLanguage.setter
    def AlternativeLanguage(self, AlternativeLanguage):
        self._AlternativeLanguage = AlternativeLanguage


    def _deserialize(self, params):
        self._Language = params.get("Language")
        self._AlternativeLanguage = params.get("AlternativeLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordParams(AbstractModel):
    """The on-cloud recording parameters.

    """

    def __init__(self):
        r"""
        :param _RecordMode: The recording mode.
1: Single-stream recording. Records the audio and video of each subscribed user (`UserId`) in a room and saves the recording files to the cloud.
2: Mixed-stream recording. Mixes the audios and videos of subscribed users (`UserId`) in a room, records the mixed stream, and saves the recording files to the cloud.
        :type RecordMode: int
        :param _MaxIdleTime: The time period (seconds) to wait to automatically stop recording after there are no anchors (users who publish streams) in a room. Value range: 5-86400 (max 24 hours). Default value: 30.
        :type MaxIdleTime: int
        :param _StreamType: The media type of the streams to record.
0: Audio and video streams (default)
1: Audio streams only
2: Video streams only
        :type StreamType: int
        :param _SubscribeStreamUserIds: The allowlist/blocklist for stream subscription.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        :param _OutputFormat: The output format. `0` (default): HLS; `1`: HLS + MP4; `2`: HLS + AAC;  `3` : MP4,  `4` : AAC. This parameter is invalid if you save recording files to VOD. To specify the format of files saved to VOD, use `MediaType` of `TencentVod`.
        :type OutputFormat: int
        :param _AvMerge: Whether to merge the audio and video of a user in the single-stream recording mode. 0 (default): Do not mix the audio and video; 1: Mix the audio and video into one TS file. You don’t need to specify this parameter for mixed-stream recording, which merges audios and videos by default.
        :type AvMerge: int
        :param _MaxMediaFileDuration: The maximum file duration allowed (minutes). If the output format is AAC or MP4, and the maximum file duration is exceeded, the file will be segmented. Value range: 1-1440. Default value: 1440 (24 hours). The maximum file size allowed is 2 GB. If the file size exceeds 2 GB, or the file duration exceeds 24 hours, the file will also be segmented.
This parameter is invalid if the output format is HLS.
        :type MaxMediaFileDuration: int
        :param _MediaId: The type of stream to record. `0` (default): The primary stream and substream; `1`: The primary stream; `2`: The substream.
        :type MediaId: int
        """
        self._RecordMode = None
        self._MaxIdleTime = None
        self._StreamType = None
        self._SubscribeStreamUserIds = None
        self._OutputFormat = None
        self._AvMerge = None
        self._MaxMediaFileDuration = None
        self._MediaId = None

    @property
    def RecordMode(self):
        """The recording mode.
1: Single-stream recording. Records the audio and video of each subscribed user (`UserId`) in a room and saves the recording files to the cloud.
2: Mixed-stream recording. Mixes the audios and videos of subscribed users (`UserId`) in a room, records the mixed stream, and saves the recording files to the cloud.
        :rtype: int
        """
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def MaxIdleTime(self):
        """The time period (seconds) to wait to automatically stop recording after there are no anchors (users who publish streams) in a room. Value range: 5-86400 (max 24 hours). Default value: 30.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def StreamType(self):
        """The media type of the streams to record.
0: Audio and video streams (default)
1: Audio streams only
2: Video streams only
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def SubscribeStreamUserIds(self):
        """The allowlist/blocklist for stream subscription.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

    @property
    def OutputFormat(self):
        """The output format. `0` (default): HLS; `1`: HLS + MP4; `2`: HLS + AAC;  `3` : MP4,  `4` : AAC. This parameter is invalid if you save recording files to VOD. To specify the format of files saved to VOD, use `MediaType` of `TencentVod`.
        :rtype: int
        """
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def AvMerge(self):
        """Whether to merge the audio and video of a user in the single-stream recording mode. 0 (default): Do not mix the audio and video; 1: Mix the audio and video into one TS file. You don’t need to specify this parameter for mixed-stream recording, which merges audios and videos by default.
        :rtype: int
        """
        return self._AvMerge

    @AvMerge.setter
    def AvMerge(self, AvMerge):
        self._AvMerge = AvMerge

    @property
    def MaxMediaFileDuration(self):
        """The maximum file duration allowed (minutes). If the output format is AAC or MP4, and the maximum file duration is exceeded, the file will be segmented. Value range: 1-1440. Default value: 1440 (24 hours). The maximum file size allowed is 2 GB. If the file size exceeds 2 GB, or the file duration exceeds 24 hours, the file will also be segmented.
This parameter is invalid if the output format is HLS.
        :rtype: int
        """
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration

    @property
    def MediaId(self):
        """The type of stream to record. `0` (default): The primary stream and substream; `1`: The primary stream; `2`: The substream.
        :rtype: int
        """
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId


    def _deserialize(self, params):
        self._RecordMode = params.get("RecordMode")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._StreamType = params.get("StreamType")
        if params.get("SubscribeStreamUserIds") is not None:
            self._SubscribeStreamUserIds = SubscribeStreamUserIds()
            self._SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self._OutputFormat = params.get("OutputFormat")
        self._AvMerge = params.get("AvMerge")
        self._MaxMediaFileDuration = params.get("MaxMediaFileDuration")
        self._MediaId = params.get("MediaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdRequest(AbstractModel):
    """RemoveUserByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param _RoomId: Room ID
        :type RoomId: str
        :param _UserIds: List of up to 10 users to be removed
        :type UserIds: list of str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserIds = None

    @property
    def SdkAppId(self):
        """`SDKAppId` of TRTC
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """Room ID
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
        """List of up to 10 users to be removed
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdResponse(AbstractModel):
    """RemoveUserByStrRoomId response structure.

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


class RemoveUserRequest(AbstractModel):
    """RemoveUser request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param _RoomId: Room number.
        :type RoomId: int
        :param _UserIds: List of up to 10 users to be removed.
        :type UserIds: list of str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserIds = None

    @property
    def SdkAppId(self):
        """`SDKAppId` of TRTC.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """Room number.
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
        """List of up to 10 users to be removed.
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserResponse(AbstractModel):
    """RemoveUser response structure.

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


class RoomState(AbstractModel):
    """The room information.

    """

    def __init__(self):
        r"""
        :param _CommId: The call ID, which uniquely identifies a call.
        :type CommId: str
        :param _RoomString: The room ID.
        :type RoomString: str
        :param _CreateTime: The room creation time.
        :type CreateTime: int
        :param _DestroyTime: The room termination time.
        :type DestroyTime: int
        :param _IsFinished: Whether the room is terminated.
        :type IsFinished: bool
        :param _UserId: The user ID of the room creator.
        :type UserId: str
        """
        self._CommId = None
        self._RoomString = None
        self._CreateTime = None
        self._DestroyTime = None
        self._IsFinished = None
        self._UserId = None

    @property
    def CommId(self):
        """The call ID, which uniquely identifies a call.
        :rtype: str
        """
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def RoomString(self):
        """The room ID.
        :rtype: str
        """
        return self._RoomString

    @RoomString.setter
    def RoomString(self, RoomString):
        self._RoomString = RoomString

    @property
    def CreateTime(self):
        """The room creation time.
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DestroyTime(self):
        """The room termination time.
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def IsFinished(self):
        """Whether the room is terminated.
        :rtype: bool
        """
        return self._IsFinished

    @IsFinished.setter
    def IsFinished(self, IsFinished):
        self._IsFinished = IsFinished

    @property
    def UserId(self):
        """The user ID of the room creator.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._CommId = params.get("CommId")
        self._RoomString = params.get("RoomString")
        self._CreateTime = params.get("CreateTime")
        self._DestroyTime = params.get("DestroyTime")
        self._IsFinished = params.get("IsFinished")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RowValues(AbstractModel):
    """Two-dimensional array of SeriesInfo type

    """

    def __init__(self):
        r"""
        :param _RowValue: Data value
        :type RowValue: list of int
        """
        self._RowValue = None

    @property
    def RowValue(self):
        """Data value
        :rtype: list of int
        """
        return self._RowValue

    @RowValue.setter
    def RowValue(self, RowValue):
        self._RowValue = RowValue


    def _deserialize(self, params):
        self._RowValue = params.get("RowValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class STTConfig(AbstractModel):
    """Speech-to-text parameters

    """

    def __init__(self):
        r"""
        :param _Language: The supported languages for speech recognition are as follows, with the default being "zh" for Chinese. The values for the `Language` field follow the [ISO639](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) standard. Here is the full list of supported languages:

1. Chinese = "zh"
2. Chinese_TW = "zh-TW"
3. Chinese_DIALECT = "zh-dialect"
4. English = "en"
5. Vietnamese = "vi"
6. Japanese = "ja"
7. Korean = "ko"
8. Indonesian = "id"
9. Thai = "th"
10. Portuguese = "pt"
11. Turkish = "tr"
12. Arabic = "ar"
13. Spanish = "es"
14. Hindi = "hi"
15. French = "fr"
16. Malay = "ms"
17. Filipino = "fil"
18. German = "de"
19. Italian = "it"
20. Russian = "ru"

**Note:** If the language you need is not listed, please contact our technical support team.
        :type Language: str
        :param _AlternativeLanguage: Initiate fuzzy recognition to replace additional language types. Fill in up to 3 language types. Note: When Language is specified as "zh-dialect", fuzzy recognition is not supported and this field is invalid.
        :type AlternativeLanguage: list of str
        :param _VadSilenceTime: The time for speech recognition vad is in the range of 240-2000, the default value is 1000, and the unit is ms. A smaller value will make speech recognition sentence segmentation faster.
        :type VadSilenceTime: int
        """
        self._Language = None
        self._AlternativeLanguage = None
        self._VadSilenceTime = None

    @property
    def Language(self):
        """The supported languages for speech recognition are as follows, with the default being "zh" for Chinese. The values for the `Language` field follow the [ISO639](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) standard. Here is the full list of supported languages:

1. Chinese = "zh"
2. Chinese_TW = "zh-TW"
3. Chinese_DIALECT = "zh-dialect"
4. English = "en"
5. Vietnamese = "vi"
6. Japanese = "ja"
7. Korean = "ko"
8. Indonesian = "id"
9. Thai = "th"
10. Portuguese = "pt"
11. Turkish = "tr"
12. Arabic = "ar"
13. Spanish = "es"
14. Hindi = "hi"
15. French = "fr"
16. Malay = "ms"
17. Filipino = "fil"
18. German = "de"
19. Italian = "it"
20. Russian = "ru"

**Note:** If the language you need is not listed, please contact our technical support team.
        :rtype: str
        """
        return self._Language

    @Language.setter
    def Language(self, Language):
        self._Language = Language

    @property
    def AlternativeLanguage(self):
        """Initiate fuzzy recognition to replace additional language types. Fill in up to 3 language types. Note: When Language is specified as "zh-dialect", fuzzy recognition is not supported and this field is invalid.
        :rtype: list of str
        """
        return self._AlternativeLanguage

    @AlternativeLanguage.setter
    def AlternativeLanguage(self, AlternativeLanguage):
        self._AlternativeLanguage = AlternativeLanguage

    @property
    def VadSilenceTime(self):
        """The time for speech recognition vad is in the range of 240-2000, the default value is 1000, and the unit is ms. A smaller value will make speech recognition sentence segmentation faster.
        :rtype: int
        """
        return self._VadSilenceTime

    @VadSilenceTime.setter
    def VadSilenceTime(self, VadSilenceTime):
        self._VadSilenceTime = VadSilenceTime


    def _deserialize(self, params):
        self._Language = params.get("Language")
        self._AlternativeLanguage = params.get("AlternativeLanguage")
        self._VadSilenceTime = params.get("VadSilenceTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInfomation(AbstractModel):
    """The room and user number.

    """

    def __init__(self):
        r"""
        :param _Time: Start time for each day
        :type Time: int
        :param _UserNumber: The number of users. If a user enters a room multiple times, it will be counted as one user.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserNumber: int
        :param _UserCount: The number of room entries. Every time a user enters a room, it will be counted as one room entry.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UserCount: int
        :param _RoomNumbers: The total number of rooms of the application on a day.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RoomNumbers: int
        """
        self._Time = None
        self._UserNumber = None
        self._UserCount = None
        self._RoomNumbers = None

    @property
    def Time(self):
        """Start time for each day
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def UserNumber(self):
        """The number of users. If a user enters a room multiple times, it will be counted as one user.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UserNumber

    @UserNumber.setter
    def UserNumber(self, UserNumber):
        self._UserNumber = UserNumber

    @property
    def UserCount(self):
        """The number of room entries. Every time a user enters a room, it will be counted as one room entry.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount

    @property
    def RoomNumbers(self):
        """The total number of rooms of the application on a day.
Note: This field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RoomNumbers

    @RoomNumbers.setter
    def RoomNumbers(self, RoomNumbers):
        self._RoomNumbers = RoomNumbers


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._UserNumber = params.get("UserNumber")
        self._UserCount = params.get("UserCount")
        self._RoomNumbers = params.get("RoomNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeriesInfos(AbstractModel):
    """SeriesInfos type

    """

    def __init__(self):
        r"""
        :param _Columns: Data columns
        :type Columns: list of str
        :param _Values: Data values
        :type Values: list of RowValues
        """
        self._Columns = None
        self._Values = None

    @property
    def Columns(self):
        """Data columns
        :rtype: list of str
        """
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Values(self):
        """Data values
        :rtype: list of RowValues
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Columns = params.get("Columns")
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = RowValues()
                obj._deserialize(item)
                self._Values.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerPushText(AbstractModel):
    """The server controls the AI conversation robot to broadcast the specified text

    """

    def __init__(self):
        r"""
        :param _Text: Server push broadcast text
        :type Text: str
        :param _Interrupt: Allow this text to interrupt the robot
        :type Interrupt: bool
        :param _StopAfterPlay: After the text is finished, whether to automatically close the conversation task
        :type StopAfterPlay: bool
        """
        self._Text = None
        self._Interrupt = None
        self._StopAfterPlay = None

    @property
    def Text(self):
        """Server push broadcast text
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Interrupt(self):
        """Allow this text to interrupt the robot
        :rtype: bool
        """
        return self._Interrupt

    @Interrupt.setter
    def Interrupt(self, Interrupt):
        self._Interrupt = Interrupt

    @property
    def StopAfterPlay(self):
        """After the text is finished, whether to automatically close the conversation task
        :rtype: bool
        """
        return self._StopAfterPlay

    @StopAfterPlay.setter
    def StopAfterPlay(self, StopAfterPlay):
        self._StopAfterPlay = StopAfterPlay


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Interrupt = params.get("Interrupt")
        self._StopAfterPlay = params.get("StopAfterPlay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserBlockedByStrRoomIdRequest(AbstractModel):
    """SetUserBlockedByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _StrRoomId: The room ID (string).
        :type StrRoomId: str
        :param _UserId: The user ID.
        :type UserId: str
        :param _IsMute: Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :type IsMute: int
        """
        self._SdkAppId = None
        self._StrRoomId = None
        self._UserId = None
        self._IsMute = None

    @property
    def SdkAppId(self):
        """The application ID.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StrRoomId(self):
        """The room ID (string).
        :rtype: str
        """
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId

    @property
    def UserId(self):
        """The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsMute(self):
        """Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :rtype: int
        """
        return self._IsMute

    @IsMute.setter
    def IsMute(self, IsMute):
        self._IsMute = IsMute


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._StrRoomId = params.get("StrRoomId")
        self._UserId = params.get("UserId")
        self._IsMute = params.get("IsMute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserBlockedByStrRoomIdResponse(AbstractModel):
    """SetUserBlockedByStrRoomId response structure.

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


class SetUserBlockedRequest(AbstractModel):
    """SetUserBlocked request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The application ID.
        :type SdkAppId: int
        :param _RoomId: The room ID (number).
        :type RoomId: int
        :param _UserId: The user ID.
        :type UserId: str
        :param _IsMute: Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :type IsMute: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._IsMute = None

    @property
    def SdkAppId(self):
        """The application ID.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """The room ID (number).
        :rtype: int
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        """The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsMute(self):
        """Controls the activation state of audio and video.
0: Enable audio and video,
1: Disable audio and video,
2: Disable audio only,
3: Disable video only.
        :rtype: int
        """
        return self._IsMute

    @IsMute.setter
    def IsMute(self, IsMute):
        self._IsMute = IsMute


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._UserId = params.get("UserId")
        self._IsMute = params.get("IsMute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetUserBlockedResponse(AbstractModel):
    """SetUserBlocked response structure.

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


class SingleSubscribeParams(AbstractModel):
    """The information of a single stream relayed.

    """

    def __init__(self):
        r"""
        :param _UserMediaStream: The stream information.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self._UserMediaStream = None

    @property
    def UserMediaStream(self):
        """The stream information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self._UserMediaStream = UserMediaStream()
            self._UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAIConversationRequest(AbstractModel):
    """StartAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the conversation task.
        :type SdkAppId: int
        :param _RoomId: TRTC's [RoomId](https://cloud.tencent.com/document/product/647/46351#roomid), which indicates the room number where the conversation task is started.
        :type RoomId: str
        :param _AgentConfig: Robot parameters
        :type AgentConfig: :class:`tencentcloud.trtc.v20190722.models.AgentConfig`
        :param _SessionId: The unique ID passed in by the caller can be used by the client to prevent repeated task initiation and to query the task status through this field.
        :type SessionId: str
        :param _RoomIdType: The type of TRTC room number. 0 represents a numeric room number, and 1 represents a string room number. If not filled in, the default is a numeric room number.
        :type RoomIdType: int
        :param _STTConfig: Speech recognition configuration.
        :type STTConfig: :class:`tencentcloud.trtc.v20190722.models.STTConfig`
        :param _LLMConfig: LLM configuration. It must comply with the openai specification and be a JSON string. The example is as follows: <pre> { <br> &emsp; "LLMType": "Large model type", // String required, such as: "openai" <br> &emsp; "Model": "Your model name", // String required, specify the model to be used<br> "APIKey": "Your LLM API key", // String required <br> &emsp; "APIUrl": "https://api.xxx.com/chat/completions", // String required, URL for LLM API access<br> &emsp; "Streaming": true // Boolean optional, specify whether to use streaming<br> &emsp;} </pre>
        :type LLMConfig: str
        :param _TTSConfig: TTS configuration, which is a JSON string. The Tencent Cloud TTS example is as follows: <pre>{ <br> &emsp; "AppId": your application ID, // Integer Required<br> &emsp; "TTSType": "TTS type", // String TTS type, fixed to "tencent"<br> &emsp; "SecretId": "Your key ID", // String Required<br> &emsp; "SecretKey": "Your keyKey", // String Required<br> &emsp; "VoiceType": 101001, // Integer Required, voice ID, including standard voice and premium voice. Premium voice has higher fidelity and different price from standard voice. For details, please refer to <a href="https://cloud.tencent.com/document/product/1073/34112">Overview of Speech Synthesis Billing</a>. For a complete list of timbre IDs, see <a href="https://cloud.tencent.com/document/product/1073/92668#55924b56-1a73-4663-a7a1-a8dd82d6e823">List of speech synthesis timbre IDs</a>. <br> &emsp; "Speed": 1.25, // Integer Optional, speaking speed, range: [-2, 6], corresponding to different speaking speeds: -2: 0.6 times -1: 0.8 times 0: 1.0 times (default) 1: 1.2 times 2: 1.5 times 6: 2.5 times If a more detailed speaking speed is required, 2 decimal places can be retained, such as 0.5/1.25/2.81, etc. For the conversion between parameter value and actual speech speed, please refer to <a href="https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz">Speed Conversion</a><br> &emsp; "Volume": 5, // Integer Optional, volume size, range: [0, 10], corresponding to 11 levels of volume, the default value is 0, representing normal volume. <br> &emsp; "PrimaryLanguage": "zh-CN" // String Optional, primary language<br> &emsp;}</pre>
        :type TTSConfig: str
        """
        self._SdkAppId = None
        self._RoomId = None
        self._AgentConfig = None
        self._SessionId = None
        self._RoomIdType = None
        self._STTConfig = None
        self._LLMConfig = None
        self._TTSConfig = None

    @property
    def SdkAppId(self):
        """TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the conversation task.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """TRTC's [RoomId](https://cloud.tencent.com/document/product/647/46351#roomid), which indicates the room number where the conversation task is started.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def AgentConfig(self):
        """Robot parameters
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AgentConfig`
        """
        return self._AgentConfig

    @AgentConfig.setter
    def AgentConfig(self, AgentConfig):
        self._AgentConfig = AgentConfig

    @property
    def SessionId(self):
        """The unique ID passed in by the caller can be used by the client to prevent repeated task initiation and to query the task status through this field.
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RoomIdType(self):
        """The type of TRTC room number. 0 represents a numeric room number, and 1 represents a string room number. If not filled in, the default is a numeric room number.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def STTConfig(self):
        """Speech recognition configuration.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.STTConfig`
        """
        return self._STTConfig

    @STTConfig.setter
    def STTConfig(self, STTConfig):
        self._STTConfig = STTConfig

    @property
    def LLMConfig(self):
        """LLM configuration. It must comply with the openai specification and be a JSON string. The example is as follows: <pre> { <br> &emsp; "LLMType": "Large model type", // String required, such as: "openai" <br> &emsp; "Model": "Your model name", // String required, specify the model to be used<br> "APIKey": "Your LLM API key", // String required <br> &emsp; "APIUrl": "https://api.xxx.com/chat/completions", // String required, URL for LLM API access<br> &emsp; "Streaming": true // Boolean optional, specify whether to use streaming<br> &emsp;} </pre>
        :rtype: str
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        """TTS configuration, which is a JSON string. The Tencent Cloud TTS example is as follows: <pre>{ <br> &emsp; "AppId": your application ID, // Integer Required<br> &emsp; "TTSType": "TTS type", // String TTS type, fixed to "tencent"<br> &emsp; "SecretId": "Your key ID", // String Required<br> &emsp; "SecretKey": "Your keyKey", // String Required<br> &emsp; "VoiceType": 101001, // Integer Required, voice ID, including standard voice and premium voice. Premium voice has higher fidelity and different price from standard voice. For details, please refer to <a href="https://cloud.tencent.com/document/product/1073/34112">Overview of Speech Synthesis Billing</a>. For a complete list of timbre IDs, see <a href="https://cloud.tencent.com/document/product/1073/92668#55924b56-1a73-4663-a7a1-a8dd82d6e823">List of speech synthesis timbre IDs</a>. <br> &emsp; "Speed": 1.25, // Integer Optional, speaking speed, range: [-2, 6], corresponding to different speaking speeds: -2: 0.6 times -1: 0.8 times 0: 1.0 times (default) 1: 1.2 times 2: 1.5 times 6: 2.5 times If a more detailed speaking speed is required, 2 decimal places can be retained, such as 0.5/1.25/2.81, etc. For the conversion between parameter value and actual speech speed, please refer to <a href="https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/sample/speed_sample.tar.gz">Speed Conversion</a><br> &emsp; "Volume": 5, // Integer Optional, volume size, range: [0, 10], corresponding to 11 levels of volume, the default value is 0, representing normal volume. <br> &emsp; "PrimaryLanguage": "zh-CN" // String Optional, primary language<br> &emsp;}</pre>
        :rtype: str
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        if params.get("AgentConfig") is not None:
            self._AgentConfig = AgentConfig()
            self._AgentConfig._deserialize(params.get("AgentConfig"))
        self._SessionId = params.get("SessionId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("STTConfig") is not None:
            self._STTConfig = STTConfig()
            self._STTConfig._deserialize(params.get("STTConfig"))
        self._LLMConfig = params.get("LLMConfig")
        self._TTSConfig = params.get("TTSConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAIConversationResponse(AbstractModel):
    """StartAIConversation response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Used to uniquely identify a conversation task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Used to uniquely identify a conversation task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartAITranscriptionRequest(AbstractModel):
    """StartAITranscription request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the transcription task.
        :type SdkAppId: int
        :param _RoomId: TRTC's [RoomId](https://cloud.tencent.com/document/product/647/46351#roomid), which indicates the room number where the transcription task is started.
        :type RoomId: str
        :param _TranscriptionParams: Parameters of the transcription robot.
        :type TranscriptionParams: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParams`
        :param _SessionId: The unique ID passed by the caller is used by the server to deduplicate. Note: If this parameter is passed, the server will use it first to deduplicate. If this parameter is not passed, the server's deduplication strategy is as follows: 
- If the TranscriptionMode field is 0, only one task can be opened in a room
- If the TranscriptionMode field is 1, only one task can be opened in a TargetUserId
        :type SessionId: str
        :param _RoomIdType: The type of TRTC room number. 0 represents a numeric room number, and 1 represents a string room number. If not filled in, the default is a numeric room number.
        :type RoomIdType: int
        :param _RecognizeConfig: Speech recognition configuration.
        :type RecognizeConfig: :class:`tencentcloud.trtc.v20190722.models.RecognizeConfig`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._TranscriptionParams = None
        self._SessionId = None
        self._RoomIdType = None
        self._RecognizeConfig = None

    @property
    def SdkAppId(self):
        """TRTC's [SdkAppId](https://cloud.tencent.com/document/product/647/46351#sdkappid) is the same as the SdkAppId used by the room that starts the transcription task.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """TRTC's [RoomId](https://cloud.tencent.com/document/product/647/46351#roomid), which indicates the room number where the transcription task is started.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def TranscriptionParams(self):
        """Parameters of the transcription robot.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.TranscriptionParams`
        """
        return self._TranscriptionParams

    @TranscriptionParams.setter
    def TranscriptionParams(self, TranscriptionParams):
        self._TranscriptionParams = TranscriptionParams

    @property
    def SessionId(self):
        """The unique ID passed by the caller is used by the server to deduplicate. Note: If this parameter is passed, the server will use it first to deduplicate. If this parameter is not passed, the server's deduplication strategy is as follows: 
- If the TranscriptionMode field is 0, only one task can be opened in a room
- If the TranscriptionMode field is 1, only one task can be opened in a TargetUserId
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def RoomIdType(self):
        """The type of TRTC room number. 0 represents a numeric room number, and 1 represents a string room number. If not filled in, the default is a numeric room number.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def RecognizeConfig(self):
        """Speech recognition configuration.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RecognizeConfig`
        """
        return self._RecognizeConfig

    @RecognizeConfig.setter
    def RecognizeConfig(self, RecognizeConfig):
        self._RecognizeConfig = RecognizeConfig


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        if params.get("TranscriptionParams") is not None:
            self._TranscriptionParams = TranscriptionParams()
            self._TranscriptionParams._deserialize(params.get("TranscriptionParams"))
        self._SessionId = params.get("SessionId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("RecognizeConfig") is not None:
            self._RecognizeConfig = RecognizeConfig()
            self._RecognizeConfig._deserialize(params.get("RecognizeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAITranscriptionResponse(AbstractModel):
    """StartAITranscription response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Used to uniquely identify a transcription task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Used to uniquely identify a transcription task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartPublishCdnStreamRequest(AbstractModel):
    """StartPublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param _RoomId: The ID of the room whose streams are relayed (the main room).
        :type RoomId: str
        :param _RoomIdType: The type of the `RoomId` parameter, which must be the same as the ID type of the room whose streams are relayed. 0: integer; 1: string.
        :type RoomIdType: int
        :param _AgentParams: The information of the relaying robot in the room.
        :type AgentParams: :class:`tencentcloud.trtc.v20190722.models.AgentParams`
        :param _WithTranscoding: Whether to transcode the streams. `0`: No. `1`: Yes. This parameter determines whether transcoding fees are charged. If it is `0`, streams will only be relayed, and no transcoding fees will be incurred. If it is `1`, streams will be transcoded before being relayed, and transcoding fees will be incurred.
        :type WithTranscoding: int
        :param _AudioParams: The audio encoding parameters. Because audio is always transcoded (no fees are incurred), this parameter is required when you start a relay task.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param _VideoParams: The video encoding parameters for relaying. If you do not pass this parameter, only audio will be relayed.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param _SingleSubscribeParams: The information of a single stream relayed. When you relay a single stream, set `WithTranscoding` to 0.
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param _PublishCdnParams: The information of the CDNs to relay to. You need to specify at least one between this parameter and `FeedBackRoomParams.N`.
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _SeiParams: The stream mixing SEI parameters.
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param _FeedBackRoomParams: The information of the room to which streams are relayed. Between this parameter and `PublishCdnParams`, you must specify at least one. Please note that relaying to a TRTC room is only supported in some SDK versions. For details, please contact technical support.
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._AgentParams = None
        self._WithTranscoding = None
        self._AudioParams = None
        self._VideoParams = None
        self._SingleSubscribeParams = None
        self._PublishCdnParams = None
        self._SeiParams = None
        self._FeedBackRoomParams = None

    @property
    def SdkAppId(self):
        """The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """The ID of the room whose streams are relayed (the main room).
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        """The type of the `RoomId` parameter, which must be the same as the ID type of the room whose streams are relayed. 0: integer; 1: string.
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def AgentParams(self):
        """The information of the relaying robot in the room.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AgentParams`
        """
        return self._AgentParams

    @AgentParams.setter
    def AgentParams(self, AgentParams):
        self._AgentParams = AgentParams

    @property
    def WithTranscoding(self):
        """Whether to transcode the streams. `0`: No. `1`: Yes. This parameter determines whether transcoding fees are charged. If it is `0`, streams will only be relayed, and no transcoding fees will be incurred. If it is `1`, streams will be transcoded before being relayed, and transcoding fees will be incurred.
        :rtype: int
        """
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        """The audio encoding parameters. Because audio is always transcoded (no fees are incurred), this parameter is required when you start a relay task.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        """The video encoding parameters for relaying. If you do not pass this parameter, only audio will be relayed.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        """The information of a single stream relayed. When you relay a single stream, set `WithTranscoding` to 0.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        """
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        """The information of the CDNs to relay to. You need to specify at least one between this parameter and `FeedBackRoomParams.N`.
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        """The stream mixing SEI parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        """
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
        """The information of the room to which streams are relayed. Between this parameter and `PublishCdnParams`, you must specify at least one. Please note that relaying to a TRTC room is only supported in some SDK versions. For details, please contact technical support.
        :rtype: list of McuFeedBackRoomParams
        """
        return self._FeedBackRoomParams

    @FeedBackRoomParams.setter
    def FeedBackRoomParams(self, FeedBackRoomParams):
        self._FeedBackRoomParams = FeedBackRoomParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        if params.get("AgentParams") is not None:
            self._AgentParams = AgentParams()
            self._AgentParams._deserialize(params.get("AgentParams"))
        self._WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self._AudioParams = McuAudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self._VideoParams = McuVideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self._SingleSubscribeParams = SingleSubscribeParams()
            self._SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self._SeiParams = McuSeiParams()
            self._SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self._FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self._FeedBackRoomParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishCdnStreamResponse(AbstractModel):
    """StartPublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID, which is generated by the Tencent Cloud server. You need to pass in the task ID when making a request to update or stop a relaying task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The task ID, which is generated by the Tencent Cloud server. You need to pass in the task ID when making a request to update or stop a relaying task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StartStreamIngestRequest(AbstractModel):
    """StartStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: TRTC's [SdkAppId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#sdkappid), the same as the SdkAppId corresponding to the Record room.
        :type SdkAppId: int
        :param _RoomId: TRTC's [RoomId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#roomid), the RoomId corresponding to the Record TRTC room.
        :type RoomId: str
        :param _RoomIdType: Type of TRTC RoomId. [*Note] Must be the same as the RoomId type corresponding to the Record room: 0: String type RoomId 1: 32-bit Integer type RoomId (default)
        :type RoomIdType: int
        :param _UserId: UserId of the Pull stream Relay Robot, used to enter the room and initiate the Pull stream Relay Task.
        :type UserId: str
        :param _UserSig: UserSig corresponding to the Pull stream Relay Robot UserId, i.e., UserId and UserSig are equivalent to the Robot's Login password for entering the room. For the specific Calculation method, please refer to the TRTC [UserSig](https://www.tencentcloud.com/zh/document/product/647/39074) Scheme.
        :type UserSig: str
        :param _StreamUrl: The Url of the media resource.
        :type StreamUrl: str
        :param _PrivateMapKey: TRTC room permission Encryption ticket, only needed when advanced permission control is enabled in the Console. After enabling advanced permission control in the TRTC Console, TRTC's backend service system will verify a so-called [PrivateMapKey] 'Permission ticket', which contains an encrypted RoomId and an encrypted 'Permission bit list'. Since PrivateMapKey contains RoomId, providing only UserSig without PrivateMapKey does not allow entry into the specified room.
        :type PrivateMapKey: str
        :param _VideoEncodeParams: Video Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :type VideoEncodeParams: :class:`tencentcloud.trtc.v20190722.models.VideoEncodeParams`
        :param _AudioEncodeParams: Audio Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :type AudioEncodeParams: :class:`tencentcloud.trtc.v20190722.models.AudioEncodeParams`
        :param _SourceUrl: 	
Source URL. Example value: https://a.b/test.mp4
        :type SourceUrl: list of str
        :param _SeekSecond: 
        :type SeekSecond: int
        :param _AutoPush: Enable auto relay to cdn, please make sure that this feature has been enabled in the console.
        :type AutoPush: bool
        :param _RepeatNum: Loop playback count, value range: [-1, 1000], default is 1 time. - 0 is an invalid value - -1 is for loop playback, task termination requires actively calling the stop interface or setting MaxDuration.
        :type RepeatNum: int
        :param _MaxDuration: Loop playback maximum duration, only effective when RepeatNum is set to -1, valid value range: [1, 10080], unit: minutes
        :type MaxDuration: int
        :param _Volume: Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :type Volume: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._UserId = None
        self._UserSig = None
        self._StreamUrl = None
        self._PrivateMapKey = None
        self._VideoEncodeParams = None
        self._AudioEncodeParams = None
        self._SourceUrl = None
        self._SeekSecond = None
        self._AutoPush = None
        self._RepeatNum = None
        self._MaxDuration = None
        self._Volume = None

    @property
    def SdkAppId(self):
        """TRTC's [SdkAppId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#sdkappid), the same as the SdkAppId corresponding to the Record room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        """TRTC's [RoomId](https://intl.cloud.tencent.com/document/product/647/46351?from_cn_redirect=1#roomid), the RoomId corresponding to the Record TRTC room.
        :rtype: str
        """
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        """Type of TRTC RoomId. [*Note] Must be the same as the RoomId type corresponding to the Record room: 0: String type RoomId 1: 32-bit Integer type RoomId (default)
        :rtype: int
        """
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        """UserId of the Pull stream Relay Robot, used to enter the room and initiate the Pull stream Relay Task.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        """UserSig corresponding to the Pull stream Relay Robot UserId, i.e., UserId and UserSig are equivalent to the Robot's Login password for entering the room. For the specific Calculation method, please refer to the TRTC [UserSig](https://www.tencentcloud.com/zh/document/product/647/39074) Scheme.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def StreamUrl(self):
        """The Url of the media resource.
        :rtype: str
        """
        return self._StreamUrl

    @StreamUrl.setter
    def StreamUrl(self, StreamUrl):
        self._StreamUrl = StreamUrl

    @property
    def PrivateMapKey(self):
        """TRTC room permission Encryption ticket, only needed when advanced permission control is enabled in the Console. After enabling advanced permission control in the TRTC Console, TRTC's backend service system will verify a so-called [PrivateMapKey] 'Permission ticket', which contains an encrypted RoomId and an encrypted 'Permission bit list'. Since PrivateMapKey contains RoomId, providing only UserSig without PrivateMapKey does not allow entry into the specified room.
        :rtype: str
        """
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey

    @property
    def VideoEncodeParams(self):
        warnings.warn("parameter `VideoEncodeParams` is deprecated", DeprecationWarning) 

        """Video Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.VideoEncodeParams`
        """
        return self._VideoEncodeParams

    @VideoEncodeParams.setter
    def VideoEncodeParams(self, VideoEncodeParams):
        warnings.warn("parameter `VideoEncodeParams` is deprecated", DeprecationWarning) 

        self._VideoEncodeParams = VideoEncodeParams

    @property
    def AudioEncodeParams(self):
        warnings.warn("parameter `AudioEncodeParams` is deprecated", DeprecationWarning) 

        """Audio Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.AudioEncodeParams`
        """
        return self._AudioEncodeParams

    @AudioEncodeParams.setter
    def AudioEncodeParams(self, AudioEncodeParams):
        warnings.warn("parameter `AudioEncodeParams` is deprecated", DeprecationWarning) 

        self._AudioEncodeParams = AudioEncodeParams

    @property
    def SourceUrl(self):
        warnings.warn("parameter `SourceUrl` is deprecated", DeprecationWarning) 

        """	
Source URL. Example value: https://a.b/test.mp4
        :rtype: list of str
        """
        return self._SourceUrl

    @SourceUrl.setter
    def SourceUrl(self, SourceUrl):
        warnings.warn("parameter `SourceUrl` is deprecated", DeprecationWarning) 

        self._SourceUrl = SourceUrl

    @property
    def SeekSecond(self):
        """
        :rtype: int
        """
        return self._SeekSecond

    @SeekSecond.setter
    def SeekSecond(self, SeekSecond):
        self._SeekSecond = SeekSecond

    @property
    def AutoPush(self):
        """Enable auto relay to cdn, please make sure that this feature has been enabled in the console.
        :rtype: bool
        """
        return self._AutoPush

    @AutoPush.setter
    def AutoPush(self, AutoPush):
        self._AutoPush = AutoPush

    @property
    def RepeatNum(self):
        """Loop playback count, value range: [-1, 1000], default is 1 time. - 0 is an invalid value - -1 is for loop playback, task termination requires actively calling the stop interface or setting MaxDuration.
        :rtype: int
        """
        return self._RepeatNum

    @RepeatNum.setter
    def RepeatNum(self, RepeatNum):
        self._RepeatNum = RepeatNum

    @property
    def MaxDuration(self):
        """Loop playback maximum duration, only effective when RepeatNum is set to -1, valid value range: [1, 10080], unit: minutes
        :rtype: int
        """
        return self._MaxDuration

    @MaxDuration.setter
    def MaxDuration(self, MaxDuration):
        self._MaxDuration = MaxDuration

    @property
    def Volume(self):
        """Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._StreamUrl = params.get("StreamUrl")
        self._PrivateMapKey = params.get("PrivateMapKey")
        if params.get("VideoEncodeParams") is not None:
            self._VideoEncodeParams = VideoEncodeParams()
            self._VideoEncodeParams._deserialize(params.get("VideoEncodeParams"))
        if params.get("AudioEncodeParams") is not None:
            self._AudioEncodeParams = AudioEncodeParams()
            self._AudioEncodeParams._deserialize(params.get("AudioEncodeParams"))
        self._SourceUrl = params.get("SourceUrl")
        self._SeekSecond = params.get("SeekSecond")
        self._AutoPush = params.get("AutoPush")
        self._RepeatNum = params.get("RepeatNum")
        self._MaxDuration = params.get("MaxDuration")
        self._Volume = params.get("Volume")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamIngestResponse(AbstractModel):
    """StartStreamIngest response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The Task ID of the Pull stream Relay. The Task ID is a unique identifier for a Pull stream Relay lifecycle process, and it loses its meaning when the task ends. The Task ID needs to be saved by the business as a parameter for the next operation on this task.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The Task ID of the Pull stream Relay. The Task ID is a unique identifier for a Pull stream Relay lifecycle process, and it loses its meaning when the task ends. The Task ID needs to be saved by the business as a parameter for the next operation on this task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopAIConversationRequest(AbstractModel):
    """StopAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task Unique ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Task Unique ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAIConversationResponse(AbstractModel):
    """StopAIConversation response structure.

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


class StopAITranscriptionRequest(AbstractModel):
    """StopAITranscription request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Uniquely identifies a transcription task.
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """Uniquely identifies a transcription task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopAITranscriptionResponse(AbstractModel):
    """StopAITranscription response structure.

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


class StopPublishCdnStreamRequest(AbstractModel):
    """StopPublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param _TaskId: The task ID.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishCdnStreamResponse(AbstractModel):
    """StopPublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopStreamIngestRequest(AbstractModel):
    """StopStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the task's room.
        :type SdkAppId: int
        :param _TaskId: The unique Task ID, which will be returned after the task is successfully started.
        :type TaskId: str
        """
        self._SdkAppId = None
        self._TaskId = None

    @property
    def SdkAppId(self):
        """The SDKAppId of TRTC, which is the same as the SDKAppId corresponding to the task's room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The unique Task ID, which will be returned after the task is successfully started.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamIngestResponse(AbstractModel):
    """StopStreamIngest response structure.

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


class StorageFile(AbstractModel):
    """The information of the recording files, which is returned by the `DescribeCloudRecording` API.

    """

    def __init__(self):
        r"""
        :param _UserId: The user whose stream is recorded into the file. In the mixed-stream recording mode, this parameter will be empty.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UserId: str
        :param _FileName: The filename.
        :type FileName: str
        :param _TrackType: The type of the media recorded.
video
audio
audio_video
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TrackType: str
        :param _BeginTimeStamp: The start time (Unix timestamp) of the recording file.
        :type BeginTimeStamp: int
        """
        self._UserId = None
        self._FileName = None
        self._TrackType = None
        self._BeginTimeStamp = None

    @property
    def UserId(self):
        """The user whose stream is recorded into the file. In the mixed-stream recording mode, this parameter will be empty.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def FileName(self):
        """The filename.
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def TrackType(self):
        """The type of the media recorded.
video
audio
audio_video
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._TrackType

    @TrackType.setter
    def TrackType(self, TrackType):
        self._TrackType = TrackType

    @property
    def BeginTimeStamp(self):
        """The start time (Unix timestamp) of the recording file.
        :rtype: int
        """
        return self._BeginTimeStamp

    @BeginTimeStamp.setter
    def BeginTimeStamp(self, BeginTimeStamp):
        self._BeginTimeStamp = BeginTimeStamp


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._FileName = params.get("FileName")
        self._TrackType = params.get("TrackType")
        self._BeginTimeStamp = params.get("BeginTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageParams(AbstractModel):
    """The storage parameters.

    """

    def __init__(self):
        r"""
        :param _CloudStorage: The account information for third-party storage. Please note that if you save files to COS, a recording-to-COS fee will be incurred. For details, see the document "Billing of On-Cloud Recording". If you save files to VOD, there won't be such a fee.
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param _CloudVod: The account information for VOD storage.
        :type CloudVod: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        self._CloudStorage = None
        self._CloudVod = None

    @property
    def CloudStorage(self):
        """The account information for third-party storage. Please note that if you save files to COS, a recording-to-COS fee will be incurred. For details, see the document "Billing of On-Cloud Recording". If you save files to VOD, there won't be such a fee.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        """
        return self._CloudStorage

    @CloudStorage.setter
    def CloudStorage(self, CloudStorage):
        self._CloudStorage = CloudStorage

    @property
    def CloudVod(self):
        """The account information for VOD storage.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        return self._CloudVod

    @CloudVod.setter
    def CloudVod(self, CloudVod):
        self._CloudVod = CloudVod


    def _deserialize(self, params):
        if params.get("CloudStorage") is not None:
            self._CloudStorage = CloudStorage()
            self._CloudStorage._deserialize(params.get("CloudStorage"))
        if params.get("CloudVod") is not None:
            self._CloudVod = CloudVod()
            self._CloudVod._deserialize(params.get("CloudVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeStreamUserIds(AbstractModel):
    """The subscription allowlist/blocklist. You cannot specify an allowlist and a blocklist for audio/video subscription at the same time. The maximum number of streams one can receive at the same time is 25. When streams are mixed, up to 24 videos are supported. You can use `.*$` to specify user IDs with the same prefix, but make sure there aren’t users whose IDs contain ".*$" and are exactly the same as the prefix you pass in. If there are, TRTC will only allow or block those users.

    """

    def __init__(self):
        r"""
        :param _SubscribeAudioUserIds: The allowlist for audio subscription. For example, `["1", "2", "3"]` means to only subscribe to the audios of users 1, 2, and 3, and ["1.*$"] means to only subscribe to the audios of users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :type SubscribeAudioUserIds: list of str
        :param _UnSubscribeAudioUserIds: The blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audios of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :type UnSubscribeAudioUserIds: list of str
        :param _SubscribeVideoUserIds: The allowlist for video subscription. For example, `["1", "2", "3"]` means to only subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to only subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :type SubscribeVideoUserIds: list of str
        :param _UnSubscribeVideoUserIds: The blocklist for video subscription. For example, `["1", "2", "3"]` means to not subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :type UnSubscribeVideoUserIds: list of str
        """
        self._SubscribeAudioUserIds = None
        self._UnSubscribeAudioUserIds = None
        self._SubscribeVideoUserIds = None
        self._UnSubscribeVideoUserIds = None

    @property
    def SubscribeAudioUserIds(self):
        """The allowlist for audio subscription. For example, `["1", "2", "3"]` means to only subscribe to the audios of users 1, 2, and 3, and ["1.*$"] means to only subscribe to the audios of users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._SubscribeAudioUserIds

    @SubscribeAudioUserIds.setter
    def SubscribeAudioUserIds(self, SubscribeAudioUserIds):
        self._SubscribeAudioUserIds = SubscribeAudioUserIds

    @property
    def UnSubscribeAudioUserIds(self):
        """The blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audios of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._UnSubscribeAudioUserIds

    @UnSubscribeAudioUserIds.setter
    def UnSubscribeAudioUserIds(self, UnSubscribeAudioUserIds):
        self._UnSubscribeAudioUserIds = UnSubscribeAudioUserIds

    @property
    def SubscribeVideoUserIds(self):
        """The allowlist for video subscription. For example, `["1", "2", "3"]` means to only subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to only subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._SubscribeVideoUserIds

    @SubscribeVideoUserIds.setter
    def SubscribeVideoUserIds(self, SubscribeVideoUserIds):
        self._SubscribeVideoUserIds = SubscribeVideoUserIds

    @property
    def UnSubscribeVideoUserIds(self):
        """The blocklist for video subscription. For example, `["1", "2", "3"]` means to not subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :rtype: list of str
        """
        return self._UnSubscribeVideoUserIds

    @UnSubscribeVideoUserIds.setter
    def UnSubscribeVideoUserIds(self, UnSubscribeVideoUserIds):
        self._UnSubscribeVideoUserIds = UnSubscribeVideoUserIds


    def _deserialize(self, params):
        self._SubscribeAudioUserIds = params.get("SubscribeAudioUserIds")
        self._UnSubscribeAudioUserIds = params.get("UnSubscribeAudioUserIds")
        self._SubscribeVideoUserIds = params.get("SubscribeVideoUserIds")
        self._UnSubscribeVideoUserIds = params.get("UnSubscribeVideoUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TRTCDataResult(AbstractModel):
    """TRTC Data Dashboard/Real-Time Monitoring API output parameters

    """

    def __init__(self):
        r"""
        :param _StatementID: StatementID value, fixed at 0 for Monitoring Dashboard.
        :type StatementID: int
        :param _Series: Query result data, returned in Columns-Values format.
        :type Series: list of SeriesInfos
        :param _Total: Total value, fixed at 1 for Monitoring Dashboard.
        :type Total: int
        """
        self._StatementID = None
        self._Series = None
        self._Total = None

    @property
    def StatementID(self):
        """StatementID value, fixed at 0 for Monitoring Dashboard.
        :rtype: int
        """
        return self._StatementID

    @StatementID.setter
    def StatementID(self, StatementID):
        self._StatementID = StatementID

    @property
    def Series(self):
        """Query result data, returned in Columns-Values format.
        :rtype: list of SeriesInfos
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Total(self):
        """Total value, fixed at 1 for Monitoring Dashboard.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._StatementID = params.get("StatementID")
        if params.get("Series") is not None:
            self._Series = []
            for item in params.get("Series"):
                obj = SeriesInfos()
                obj._deserialize(item)
                self._Series.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TencentVod(AbstractModel):
    """The Tencent Cloud VOD parameters.

    """

    def __init__(self):
        r"""
        :param _Procedure: The operation to perform on the media uploaded. The value of this parameter is the name of a task flow template. You can create a custom task flow template in Tencent Cloud VOD.
        :type Procedure: str
        :param _ExpireTime: The expiration time of the media file, which is a time period (seconds) from the current time. For example, `86400` means to save the media file for one day. To save the file permanently, set this parameter to `0`.
        :type ExpireTime: int
        :param _StorageRegion: The storage region. Set this parameter if you have special requirements on the storage region.
        :type StorageRegion: str
        :param _ClassId: The category ID, which is returned after you create a category by calling an API. You can use categories to manage media files.
The default value is `0`, which means others.
        :type ClassId: int
        :param _SubAppId: The VOD subapplication ID. If you need to access a resource in a subapplication, set this parameter to the subapplication ID; otherwise, leave it empty.
        :type SubAppId: int
        :param _SessionContext: The task flow context, which is passed through after the task is completed.
        :type SessionContext: str
        :param _SourceContext: The upload context, which is passed through after upload is completed.
        :type SourceContext: str
        :param _MediaType: The format of recording files uploaded to VOD. `0` (default): MP4; `1`: HLS; `2`: AAC (valid only if `StreamType` is `1`); `3`: HLS+MP4; `4`: HLS+AAC.
        :type MediaType: int
        :param _UserDefineRecordId: The custom prefix of recording files. This parameter is valid only if recording files are uploaded to VOD. It can contain letters, numbers, underscores, and hyphens and cannot exceed 64 bytes. This prefix and the automatically generated filename are connected with `__UserId_u_`.
        :type UserDefineRecordId: str
        """
        self._Procedure = None
        self._ExpireTime = None
        self._StorageRegion = None
        self._ClassId = None
        self._SubAppId = None
        self._SessionContext = None
        self._SourceContext = None
        self._MediaType = None
        self._UserDefineRecordId = None

    @property
    def Procedure(self):
        """The operation to perform on the media uploaded. The value of this parameter is the name of a task flow template. You can create a custom task flow template in Tencent Cloud VOD.
        :rtype: str
        """
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def ExpireTime(self):
        """The expiration time of the media file, which is a time period (seconds) from the current time. For example, `86400` means to save the media file for one day. To save the file permanently, set this parameter to `0`.
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def StorageRegion(self):
        """The storage region. Set this parameter if you have special requirements on the storage region.
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def ClassId(self):
        """The category ID, which is returned after you create a category by calling an API. You can use categories to manage media files.
The default value is `0`, which means others.
        :rtype: int
        """
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def SubAppId(self):
        """The VOD subapplication ID. If you need to access a resource in a subapplication, set this parameter to the subapplication ID; otherwise, leave it empty.
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def SessionContext(self):
        """The task flow context, which is passed through after the task is completed.
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SourceContext(self):
        """The upload context, which is passed through after upload is completed.
        :rtype: str
        """
        return self._SourceContext

    @SourceContext.setter
    def SourceContext(self, SourceContext):
        self._SourceContext = SourceContext

    @property
    def MediaType(self):
        """The format of recording files uploaded to VOD. `0` (default): MP4; `1`: HLS; `2`: AAC (valid only if `StreamType` is `1`); `3`: HLS+MP4; `4`: HLS+AAC.
        :rtype: int
        """
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def UserDefineRecordId(self):
        """The custom prefix of recording files. This parameter is valid only if recording files are uploaded to VOD. It can contain letters, numbers, underscores, and hyphens and cannot exceed 64 bytes. This prefix and the automatically generated filename are connected with `__UserId_u_`.
        :rtype: str
        """
        return self._UserDefineRecordId

    @UserDefineRecordId.setter
    def UserDefineRecordId(self, UserDefineRecordId):
        self._UserDefineRecordId = UserDefineRecordId


    def _deserialize(self, params):
        self._Procedure = params.get("Procedure")
        self._ExpireTime = params.get("ExpireTime")
        self._StorageRegion = params.get("StorageRegion")
        self._ClassId = params.get("ClassId")
        self._SubAppId = params.get("SubAppId")
        self._SessionContext = params.get("SessionContext")
        self._SourceContext = params.get("SourceContext")
        self._MediaType = params.get("MediaType")
        self._UserDefineRecordId = params.get("UserDefineRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeValue(AbstractModel):
    """The quality data, which consists of the `time` and `value` parameters.

    """

    def __init__(self):
        r"""
        :param _Time: The UNIX timestamp (seconds), such as `1590065877`.
        :type Time: int
        :param _Value: The metric value. For example, if the video capturing frame rate (`bigvCapFps`) at the time `1590065877` is `0`, the value of this parameter will be `0`.
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """The UNIX timestamp (seconds), such as `1590065877`.
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """The metric value. For example, if the video capturing frame rate (`bigvCapFps`) at the time `1590065877` is `0`, the value of this parameter will be `0`.
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscriptionParams(AbstractModel):
    """AI Transcription Params

    """

    def __init__(self):
        r"""
        :param _UserId: The robot's UserId is used to enter a room and initiate tasks. [Note] This UserId cannot be repeated with the host viewer [UserId](https://cloud.tencent.com/document/product/647/46351#userid) in the current room. If multiple tasks are initiated in a room, the robot's UserId cannot be repeated, otherwise the previous task will be interrupted. The robot's UserId must be unique in the room.
        :type UserId: str
        :param _UserSig: The verification signature corresponding to the robot's UserId, that is, UserId and UserSig are equivalent to the robot's login password to enter the room. For the specific calculation method, please refer to the TRTC calculation [UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig) solution.
        :type UserSig: str
        :param _MaxIdleTime: If there is no streaming in the room for more than MaxIdleTime, the background will automatically close the task. The default value is 60s.
        :type MaxIdleTime: int
        :param _TranscriptionMode: 1 means the robot subscribes to the stream of only one person, 0 means the robot subscribes to the stream of the entire room. If it is not filled in, the robot subscribes to the stream of the entire room by default.
        :type TranscriptionMode: int
        :param _TargetUserId: Required when TranscriptionMode is 1. The robot will only pull the stream of the userid and ignore other users in the room.
        :type TargetUserId: str
        """
        self._UserId = None
        self._UserSig = None
        self._MaxIdleTime = None
        self._TranscriptionMode = None
        self._TargetUserId = None

    @property
    def UserId(self):
        """The robot's UserId is used to enter a room and initiate tasks. [Note] This UserId cannot be repeated with the host viewer [UserId](https://cloud.tencent.com/document/product/647/46351#userid) in the current room. If multiple tasks are initiated in a room, the robot's UserId cannot be repeated, otherwise the previous task will be interrupted. The robot's UserId must be unique in the room.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        """The verification signature corresponding to the robot's UserId, that is, UserId and UserSig are equivalent to the robot's login password to enter the room. For the specific calculation method, please refer to the TRTC calculation [UserSig](https://cloud.tencent.com/document/product/647/45910#UserSig) solution.
        :rtype: str
        """
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def MaxIdleTime(self):
        """If there is no streaming in the room for more than MaxIdleTime, the background will automatically close the task. The default value is 60s.
        :rtype: int
        """
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def TranscriptionMode(self):
        """1 means the robot subscribes to the stream of only one person, 0 means the robot subscribes to the stream of the entire room. If it is not filled in, the robot subscribes to the stream of the entire room by default.
        :rtype: int
        """
        return self._TranscriptionMode

    @TranscriptionMode.setter
    def TranscriptionMode(self, TranscriptionMode):
        self._TranscriptionMode = TranscriptionMode

    @property
    def TargetUserId(self):
        """Required when TranscriptionMode is 1. The robot will only pull the stream of the userid and ignore other users in the room.
        :rtype: str
        """
        return self._TargetUserId

    @TargetUserId.setter
    def TargetUserId(self, TargetUserId):
        self._TargetUserId = TargetUserId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._MaxIdleTime = params.get("MaxIdleTime")
        self._TranscriptionMode = params.get("TranscriptionMode")
        self._TargetUserId = params.get("TargetUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrtcUsage(AbstractModel):
    """The TRTC audio/video duration generated in a certain time period.

    """

    def __init__(self):
        r"""
        :param _TimeKey: The time point in the format of `YYYY-MM-DD HH:mm:ss`. If more than one day is queried, `HH:mm:ss` is `00:00:00`.
        :type TimeKey: str
        :param _UsageValue: The usage (minutes). Each element of this parameter corresponds to an element of `UsageKey` in the order they are listed.
        :type UsageValue: list of float
        """
        self._TimeKey = None
        self._UsageValue = None

    @property
    def TimeKey(self):
        """The time point in the format of `YYYY-MM-DD HH:mm:ss`. If more than one day is queried, `HH:mm:ss` is `00:00:00`.
        :rtype: str
        """
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def UsageValue(self):
        """The usage (minutes). Each element of this parameter corresponds to an element of `UsageKey` in the order they are listed.
        :rtype: list of float
        """
        return self._UsageValue

    @UsageValue.setter
    def UsageValue(self, UsageValue):
        self._UsageValue = UsageValue


    def _deserialize(self, params):
        self._TimeKey = params.get("TimeKey")
        self._UsageValue = params.get("UsageValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIConversationRequest(AbstractModel):
    """UpdateAIConversation request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Task Unique ID
        :type TaskId: str
        :param _WelcomeMessage: If you do not fill in the form, no update will be performed. Welcome message from the robot
        :type WelcomeMessage: str
        :param _InterruptMode: If not filled in, no update will be performed. Intelligent interruption mode, 0 means the server automatically interrupts, 1 means the server does not interrupt, and the client sends an interrupt signal to interrupt
        :type InterruptMode: int
        :param _InterruptSpeechDuration: If not filled in, no update will be performed. Used when InterruptMode is 0, the unit is milliseconds, and the default is 500ms. It means that the server will interrupt when it detects a voice that lasts for InterruptSpeechDuration milliseconds.
        :type InterruptSpeechDuration: int
        :param _LLMConfig: If not filled in, no update will be performed. For LLM configuration, see the StartAIConversation API for details.
        :type LLMConfig: str
        :param _TTSConfig: If not filled in, no update will be performed. For TTS configuration, see the StartAIConversation API for details.
        :type TTSConfig: str
        """
        self._TaskId = None
        self._WelcomeMessage = None
        self._InterruptMode = None
        self._InterruptSpeechDuration = None
        self._LLMConfig = None
        self._TTSConfig = None

    @property
    def TaskId(self):
        """Task Unique ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def WelcomeMessage(self):
        """If you do not fill in the form, no update will be performed. Welcome message from the robot
        :rtype: str
        """
        return self._WelcomeMessage

    @WelcomeMessage.setter
    def WelcomeMessage(self, WelcomeMessage):
        self._WelcomeMessage = WelcomeMessage

    @property
    def InterruptMode(self):
        """If not filled in, no update will be performed. Intelligent interruption mode, 0 means the server automatically interrupts, 1 means the server does not interrupt, and the client sends an interrupt signal to interrupt
        :rtype: int
        """
        return self._InterruptMode

    @InterruptMode.setter
    def InterruptMode(self, InterruptMode):
        self._InterruptMode = InterruptMode

    @property
    def InterruptSpeechDuration(self):
        """If not filled in, no update will be performed. Used when InterruptMode is 0, the unit is milliseconds, and the default is 500ms. It means that the server will interrupt when it detects a voice that lasts for InterruptSpeechDuration milliseconds.
        :rtype: int
        """
        return self._InterruptSpeechDuration

    @InterruptSpeechDuration.setter
    def InterruptSpeechDuration(self, InterruptSpeechDuration):
        self._InterruptSpeechDuration = InterruptSpeechDuration

    @property
    def LLMConfig(self):
        """If not filled in, no update will be performed. For LLM configuration, see the StartAIConversation API for details.
        :rtype: str
        """
        return self._LLMConfig

    @LLMConfig.setter
    def LLMConfig(self, LLMConfig):
        self._LLMConfig = LLMConfig

    @property
    def TTSConfig(self):
        """If not filled in, no update will be performed. For TTS configuration, see the StartAIConversation API for details.
        :rtype: str
        """
        return self._TTSConfig

    @TTSConfig.setter
    def TTSConfig(self, TTSConfig):
        self._TTSConfig = TTSConfig


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._WelcomeMessage = params.get("WelcomeMessage")
        self._InterruptMode = params.get("InterruptMode")
        self._InterruptSpeechDuration = params.get("InterruptSpeechDuration")
        self._LLMConfig = params.get("LLMConfig")
        self._TTSConfig = params.get("TTSConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAIConversationResponse(AbstractModel):
    """UpdateAIConversation response structure.

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


class UpdatePublishCdnStreamRequest(AbstractModel):
    """UpdatePublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param _TaskId: The task ID.
        :type TaskId: str
        :param _SequenceNumber: The sequence of a request. This parameter ensures the requests to change the parameters of the same relaying task are in the correct order. It increases each time a new request is made.
        :type SequenceNumber: int
        :param _WithTranscoding: Whether to transcode the streams. 0: No; 1: Yes.
        :type WithTranscoding: int
        :param _AudioParams: Pass this parameter to change the users whose audios are mixed. If you do not pass this parameter, no changes will be made.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param _VideoParams: Pass this parameter to change video parameters other than the codec, including the video layout, background image, background color, and watermark information. This parameter is valid only if streams are transcoded. If you do not pass it, no changes will be made.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param _SingleSubscribeParams: Pass this parameter to change the single stream that is relayed. This parameter is valid only if streams are not transcoded. If you do not pass this parameter, no changes will be made.
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param _PublishCdnParams: Pass this parameter to change the CDNs to relay to. If you do not pass this parameter, no changes will be made.
        :type PublishCdnParams: list of McuPublishCdnParam
        :param _SeiParams: The stream mixing SEI parameters.
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param _FeedBackRoomParams: The information of the room to which streams are relayed.
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        """
        self._SdkAppId = None
        self._TaskId = None
        self._SequenceNumber = None
        self._WithTranscoding = None
        self._AudioParams = None
        self._VideoParams = None
        self._SingleSubscribeParams = None
        self._PublishCdnParams = None
        self._SeiParams = None
        self._FeedBackRoomParams = None

    @property
    def SdkAppId(self):
        """The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SequenceNumber(self):
        """The sequence of a request. This parameter ensures the requests to change the parameters of the same relaying task are in the correct order. It increases each time a new request is made.
        :rtype: int
        """
        return self._SequenceNumber

    @SequenceNumber.setter
    def SequenceNumber(self, SequenceNumber):
        self._SequenceNumber = SequenceNumber

    @property
    def WithTranscoding(self):
        """Whether to transcode the streams. 0: No; 1: Yes.
        :rtype: int
        """
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        """Pass this parameter to change the users whose audios are mixed. If you do not pass this parameter, no changes will be made.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        """
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        """Pass this parameter to change video parameters other than the codec, including the video layout, background image, background color, and watermark information. This parameter is valid only if streams are transcoded. If you do not pass it, no changes will be made.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        """
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        """Pass this parameter to change the single stream that is relayed. This parameter is valid only if streams are not transcoded. If you do not pass this parameter, no changes will be made.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        """
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        """Pass this parameter to change the CDNs to relay to. If you do not pass this parameter, no changes will be made.
        :rtype: list of McuPublishCdnParam
        """
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        """The stream mixing SEI parameters.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        """
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
        """The information of the room to which streams are relayed.
        :rtype: list of McuFeedBackRoomParams
        """
        return self._FeedBackRoomParams

    @FeedBackRoomParams.setter
    def FeedBackRoomParams(self, FeedBackRoomParams):
        self._FeedBackRoomParams = FeedBackRoomParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._SequenceNumber = params.get("SequenceNumber")
        self._WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self._AudioParams = McuAudioParams()
            self._AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self._VideoParams = McuVideoParams()
            self._VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self._SingleSubscribeParams = SingleSubscribeParams()
            self._SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self._PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self._PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self._SeiParams = McuSeiParams()
            self._SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self._FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self._FeedBackRoomParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePublishCdnStreamResponse(AbstractModel):
    """UpdatePublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: The task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """The task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class UpdateStreamIngestRequest(AbstractModel):
    """UpdateStreamIngest request structure.

    """

    def __init__(self):
        r"""
        :param _SdkAppId: The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :type SdkAppId: int
        :param _TaskId: The unique Id of the task, will return after successfully starting the task.
        :type TaskId: str
        :param _StreamUrl: The new url of the media resource.
        :type StreamUrl: str
        :param _Volume: Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :type Volume: int
        :param _IsPause: Whether to pause, the default value of false indicates no pause. During the pause, the task is still in progress and is billed. If you want to terminate the task, please call the stop interface.
        :type IsPause: bool
        """
        self._SdkAppId = None
        self._TaskId = None
        self._StreamUrl = None
        self._Volume = None
        self._IsPause = None

    @property
    def SdkAppId(self):
        """The SDKAppId of TRTC should be the same as the SDKAppId corresponding to the task room.
        :rtype: int
        """
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        """The unique Id of the task, will return after successfully starting the task.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def StreamUrl(self):
        """The new url of the media resource.
        :rtype: str
        """
        return self._StreamUrl

    @StreamUrl.setter
    def StreamUrl(self, StreamUrl):
        self._StreamUrl = StreamUrl

    @property
    def Volume(self):
        """Volume. Valid value range: [0, 100], default value is 100, indicating the original volume.
        :rtype: int
        """
        return self._Volume

    @Volume.setter
    def Volume(self, Volume):
        self._Volume = Volume

    @property
    def IsPause(self):
        """Whether to pause, the default value of false indicates no pause. During the pause, the task is still in progress and is billed. If you want to terminate the task, please call the stop interface.
        :rtype: bool
        """
        return self._IsPause

    @IsPause.setter
    def IsPause(self, IsPause):
        self._IsPause = IsPause


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._TaskId = params.get("TaskId")
        self._StreamUrl = params.get("StreamUrl")
        self._Volume = params.get("Volume")
        self._IsPause = params.get("IsPause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateStreamIngestResponse(AbstractModel):
    """UpdateStreamIngest response structure.

    """

    def __init__(self):
        r"""
        :param _Status: Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :type Status: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """Task status information. InProgress: Indicates that the current task is in progress. NotExist: Indicates that the current task does not exist. Example value: InProgress
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class UserInformation(AbstractModel):
    """The user information, including when the user entered/left the room.

    """

    def __init__(self):
        r"""
        :param _RoomStr: The room ID.
        :type RoomStr: str
        :param _UserId: The user ID.
        :type UserId: str
        :param _JoinTs: The time when the user entered the room.
        :type JoinTs: int
        :param _LeaveTs: The time when the user left the room. If the user is still in the room, the current time will be returned.
        :type LeaveTs: int
        :param _DeviceType: The device type.
        :type DeviceType: str
        :param _SdkVersion: The SDK version number.
        :type SdkVersion: str
        :param _ClientIp: The client IP address.
        :type ClientIp: str
        :param _Finished: Whether a user has left the room.
        :type Finished: bool
        """
        self._RoomStr = None
        self._UserId = None
        self._JoinTs = None
        self._LeaveTs = None
        self._DeviceType = None
        self._SdkVersion = None
        self._ClientIp = None
        self._Finished = None

    @property
    def RoomStr(self):
        """The room ID.
        :rtype: str
        """
        return self._RoomStr

    @RoomStr.setter
    def RoomStr(self, RoomStr):
        self._RoomStr = RoomStr

    @property
    def UserId(self):
        """The user ID.
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def JoinTs(self):
        """The time when the user entered the room.
        :rtype: int
        """
        return self._JoinTs

    @JoinTs.setter
    def JoinTs(self, JoinTs):
        self._JoinTs = JoinTs

    @property
    def LeaveTs(self):
        """The time when the user left the room. If the user is still in the room, the current time will be returned.
        :rtype: int
        """
        return self._LeaveTs

    @LeaveTs.setter
    def LeaveTs(self, LeaveTs):
        self._LeaveTs = LeaveTs

    @property
    def DeviceType(self):
        """The device type.
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def SdkVersion(self):
        """The SDK version number.
        :rtype: str
        """
        return self._SdkVersion

    @SdkVersion.setter
    def SdkVersion(self, SdkVersion):
        self._SdkVersion = SdkVersion

    @property
    def ClientIp(self):
        """The client IP address.
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Finished(self):
        """Whether a user has left the room.
        :rtype: bool
        """
        return self._Finished

    @Finished.setter
    def Finished(self, Finished):
        self._Finished = Finished


    def _deserialize(self, params):
        self._RoomStr = params.get("RoomStr")
        self._UserId = params.get("UserId")
        self._JoinTs = params.get("JoinTs")
        self._LeaveTs = params.get("LeaveTs")
        self._DeviceType = params.get("DeviceType")
        self._SdkVersion = params.get("SdkVersion")
        self._ClientIp = params.get("ClientIp")
        self._Finished = params.get("Finished")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserMediaStream(AbstractModel):
    """The stream information.

    """

    def __init__(self):
        r"""
        :param _UserInfo: The user information.
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        :param _StreamType: The stream type. 0: Camera; 1: Screen sharing. If you do not pass this parameter, 0 will be used.
        :type StreamType: int
        """
        self._UserInfo = None
        self._StreamType = None

    @property
    def UserInfo(self):
        """The user information.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def StreamType(self):
        """The stream type. 0: Camera; 1: Screen sharing. If you do not pass this parameter, 0 will be used.
        :rtype: int
        """
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self._UserInfo = MixUserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._StreamType = params.get("StreamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncode(AbstractModel):
    """The video encoding parameters.

    """

    def __init__(self):
        r"""
        :param _Width: The width of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1920].
        :type Width: int
        :param _Height: The height of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1080].
        :type Height: int
        :param _Fps: The frame rate (fps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 60].
        :type Fps: int
        :param _BitRate: The bitrate (Kbps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 10000].
        :type BitRate: int
        :param _Gop: The GOP (seconds) of the output stream. This parameter is required if audio and video are relayed. Value range: [1, 5].
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        """The width of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1920].
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """The height of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1080].
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        """The frame rate (fps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 60].
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        """The bitrate (Kbps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 10000].
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        """The GOP (seconds) of the output stream. This parameter is required if audio and video are relayed. Value range: [1, 5].
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncodeParams(AbstractModel):
    """Video transcoding parameters

    """

    def __init__(self):
        r"""
        :param _Width: Width. Value range [0,1920], unit is pixel value.
        :type Width: int
        :param _Height: Height. Value range [0,1080], unit is pixel value.
        :type Height: int
        :param _Fps: Frame Rate. Value range [1,60], indicating that the frame rate can be selected from 1 to 60fps.
        :type Fps: int
        :param _BitRate: Bitrate. Value range [1,10000], unit is kbps.
        :type BitRate: int
        :param _Gop: Gop. Value range [1,2], unit is second.
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        """Width. Value range [0,1920], unit is pixel value.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """Height. Value range [0,1080], unit is pixel value.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        """Frame Rate. Value range [1,60], indicating that the frame rate can be selected from 1 to 60fps.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        """Bitrate. Value range [1,10000], unit is kbps.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        """Gop. Value range [1,2], unit is second.
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoParams(AbstractModel):
    """The video transcoding parameters for recording.

    """

    def __init__(self):
        r"""
        :param _Width: The video width in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `360`.
        :type Width: int
        :param _Height: The video height in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `640`.
        :type Height: int
        :param _Fps: The video frame rate. Value range: [1, 60]. Default: 15.
        :type Fps: int
        :param _BitRate: The video bitrate (bps). Value range: [64000, 8192000]. Default: 550000.
        :type BitRate: int
        :param _Gop: The keyframe interval (seconds). Default value: 10.
        :type Gop: int
        """
        self._Width = None
        self._Height = None
        self._Fps = None
        self._BitRate = None
        self._Gop = None

    @property
    def Width(self):
        """The video width in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `360`.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """The video height in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `640`.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        """The video frame rate. Value range: [1, 60]. Default: 15.
        :rtype: int
        """
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        """The video bitrate (bps). Value range: [64000, 8192000]. Default: 550000.
        :rtype: int
        """
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
        """The keyframe interval (seconds). Default value: 10.
        :rtype: int
        """
        return self._Gop

    @Gop.setter
    def Gop(self, Gop):
        self._Gop = Gop


    def _deserialize(self, params):
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._BitRate = params.get("BitRate")
        self._Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMark(AbstractModel):
    """The watermark layout.

    """

    def __init__(self):
        r"""
        :param _WaterMarkType: The watermark type. 0 (default): image; 1: text (not supported yet).
        :type WaterMarkType: int
        :param _WaterMarkImage: The information of watermark images. This parameter is required if the watermark type is image.
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        :param _WaterMarkChar: The information of the text watermark. This parameter is required if `WaterMarkType` is `1`.
        :type WaterMarkChar: :class:`tencentcloud.trtc.v20190722.models.WaterMarkChar`
        :param _WaterMarkTimestamp: The information of the timestamp watermark. This parameter is required if `WaterMarkType` is `2`.
        :type WaterMarkTimestamp: :class:`tencentcloud.trtc.v20190722.models.WaterMarkTimestamp`
        """
        self._WaterMarkType = None
        self._WaterMarkImage = None
        self._WaterMarkChar = None
        self._WaterMarkTimestamp = None

    @property
    def WaterMarkType(self):
        """The watermark type. 0 (default): image; 1: text (not supported yet).
        :rtype: int
        """
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        """The information of watermark images. This parameter is required if the watermark type is image.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        """
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkChar(self):
        """The information of the text watermark. This parameter is required if `WaterMarkType` is `1`.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkChar`
        """
        return self._WaterMarkChar

    @WaterMarkChar.setter
    def WaterMarkChar(self, WaterMarkChar):
        self._WaterMarkChar = WaterMarkChar

    @property
    def WaterMarkTimestamp(self):
        """The information of the timestamp watermark. This parameter is required if `WaterMarkType` is `2`.
        :rtype: :class:`tencentcloud.trtc.v20190722.models.WaterMarkTimestamp`
        """
        return self._WaterMarkTimestamp

    @WaterMarkTimestamp.setter
    def WaterMarkTimestamp(self, WaterMarkTimestamp):
        self._WaterMarkTimestamp = WaterMarkTimestamp


    def _deserialize(self, params):
        self._WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self._WaterMarkImage = WaterMarkImage()
            self._WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        if params.get("WaterMarkChar") is not None:
            self._WaterMarkChar = WaterMarkChar()
            self._WaterMarkChar._deserialize(params.get("WaterMarkChar"))
        if params.get("WaterMarkTimestamp") is not None:
            self._WaterMarkTimestamp = WaterMarkTimestamp()
            self._WaterMarkTimestamp._deserialize(params.get("WaterMarkTimestamp"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkChar(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Top: The Y coordinate of the text watermark from the top left.
        :type Top: int
        :param _Left: The X coordinate of the text watermark from the top left.
        :type Left: int
        :param _Width: The watermark width (pixels).
        :type Width: int
        :param _Height: The watermark height (pixels).
        :type Height: int
        :param _Chars: The text.
        :type Chars: str
        :param _FontSize: The font size (pixels). The default value is `14`.
        :type FontSize: int
        :param _FontColor: The text color. The default color is white.
        :type FontColor: str
        :param _BackGroundColor: The background color. If this parameter is empty, the background will be transparent (default).
        :type BackGroundColor: str
        """
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None
        self._Chars = None
        self._FontSize = None
        self._FontColor = None
        self._BackGroundColor = None

    @property
    def Top(self):
        """The Y coordinate of the text watermark from the top left.
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        """The X coordinate of the text watermark from the top left.
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        """The watermark width (pixels).
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """The watermark height (pixels).
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Chars(self):
        """The text.
        :rtype: str
        """
        return self._Chars

    @Chars.setter
    def Chars(self, Chars):
        self._Chars = Chars

    @property
    def FontSize(self):
        """The font size (pixels). The default value is `14`.
        :rtype: int
        """
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        """The text color. The default color is white.
        :rtype: str
        """
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
        """The background color. If this parameter is empty, the background will be transparent (default).
        :rtype: str
        """
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor


    def _deserialize(self, params):
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Chars = params.get("Chars")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        self._BackGroundColor = params.get("BackGroundColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkImage(AbstractModel):
    """The information of watermark images.

    """

    def __init__(self):
        r"""
        :param _WaterMarkUrl: The download URLs of the watermark images, which must be in JPG or PNG format and cannot be larger than 5 MB.
        :type WaterMarkUrl: str
        :param _Top: The Y axis of the image's top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas height.
        :type Top: int
        :param _Left: The X axis of the image’s top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas width.
        :type Left: int
        :param _Width: The relative width of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :type Width: int
        :param _Height: The relative height of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :type Height: int
        """
        self._WaterMarkUrl = None
        self._Top = None
        self._Left = None
        self._Width = None
        self._Height = None

    @property
    def WaterMarkUrl(self):
        """The download URLs of the watermark images, which must be in JPG or PNG format and cannot be larger than 5 MB.
        :rtype: str
        """
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def Top(self):
        """The Y axis of the image's top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas height.
        :rtype: int
        """
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        """The X axis of the image’s top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas width.
        :rtype: int
        """
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        """The relative width of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        """The relative height of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._WaterMarkUrl = params.get("WaterMarkUrl")
        self._Top = params.get("Top")
        self._Left = params.get("Left")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkTimestamp(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Pos: The position of the timestamp watermark. Valid values: `0` (top left), `1` (top right), `2` (bottom left), `3` (bottom right), `4` (top center), `5` (bottom center), `6` (center).
        :type Pos: int
        :param _TimeZone: The time zone. The default is UTC+8.
        :type TimeZone: int
        """
        self._Pos = None
        self._TimeZone = None

    @property
    def Pos(self):
        """The position of the timestamp watermark. Valid values: `0` (top left), `1` (top right), `2` (bottom left), `3` (bottom right), `4` (top center), `5` (bottom center), `6` (center).
        :rtype: int
        """
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos

    @property
    def TimeZone(self):
        """The time zone. The default is UTC+8.
        :rtype: int
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._Pos = params.get("Pos")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        