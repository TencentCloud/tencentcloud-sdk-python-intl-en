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
        return self._AbnormalEventId

    @AbnormalEventId.setter
    def AbnormalEventId(self, AbnormalEventId):
        self._AbnormalEventId = AbnormalEventId

    @property
    def PeerId(self):
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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ExperienceId(self):
        return self._ExperienceId

    @ExperienceId.setter
    def ExperienceId(self, ExperienceId):
        self._ExperienceId = ExperienceId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def AbnormalEventList(self):
        return self._AbnormalEventList

    @AbnormalEventList.setter
    def AbnormalEventList(self, AbnormalEventList):
        self._AbnormalEventList = AbnormalEventList

    @property
    def EventTime(self):
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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def MaxIdleTime(self):
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
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Codec(self):
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
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
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
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def BitRate(self):
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
        return self._Vendor

    @Vendor.setter
    def Vendor(self, Vendor):
        self._Vendor = Vendor

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def FileNamePrefix(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def RecordParams(self):
        return self._RecordParams

    @RecordParams.setter
    def RecordParams(self, RecordParams):
        self._RecordParams = RecordParams

    @property
    def StorageParams(self):
        return self._StorageParams

    @StorageParams.setter
    def StorageParams(self, StorageParams):
        self._StorageParams = StorageParams

    @property
    def RoomIdType(self):
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def MixTranscodeParams(self):
        return self._MixTranscodeParams

    @MixTranscodeParams.setter
    def MixTranscodeParams(self, MixTranscodeParams):
        self._MixTranscodeParams = MixTranscodeParams

    @property
    def MixLayoutParams(self):
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def ResourceExpiredHour(self):
        return self._ResourceExpiredHour

    @ResourceExpiredHour.setter
    def ResourceExpiredHour(self, ResourceExpiredHour):
        self._ResourceExpiredHour = ResourceExpiredHour

    @property
    def PrivateMapKey(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def DataType(self):
        return self._DataType

    @DataType.setter
    def DataType(self, DataType):
        self._DataType = DataType

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StorageFileList(self):
        return self._StorageFileList

    @StorageFileList.setter
    def StorageFileList(self, StorageFileList):
        self._StorageFileList = StorageFileList

    @property
    def RequestId(self):
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
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
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
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
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
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MixType(self):
        return self._MixType

    @MixType.setter
    def MixType(self, MixType):
        self._MixType = MixType

    @property
    def SdkAppId(self):
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
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
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
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
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
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RoomList(self):
        return self._RoomList

    @RoomList.setter
    def RoomList(self, RoomList):
        self._RoomList = RoomList

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ScaleList(self):
        return self._ScaleList

    @ScaleList.setter
    def ScaleList(self, ScaleList):
        self._ScaleList = ScaleList

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
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
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
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
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
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
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
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
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
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
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._SdkAppid

    @SdkAppid.setter
    def SdkAppid(self, SdkAppid):
        self._SdkAppid = SdkAppid

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
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
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
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
        return self._UsageKey

    @UsageKey.setter
    def UsageKey(self, UsageKey):
        self._UsageKey = UsageKey

    @property
    def UsageList(self):
        return self._UsageList

    @UsageList.setter
    def UsageList(self, UsageList):
        self._UsageList = UsageList

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def RoomId(self):
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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AbnormalExperienceList(self):
        return self._AbnormalExperienceList

    @AbnormalExperienceList.setter
    def AbnormalExperienceList(self, AbnormalExperienceList):
        self._AbnormalExperienceList = AbnormalExperienceList

    @property
    def RequestId(self):
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
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def SdkAppId(self):
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
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
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
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def PageNumber(self):
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
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
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def UserList(self):
        return self._UserList

    @UserList.setter
    def UserList(self, UserList):
        self._UserList = UserList

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
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
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def PeerId(self):
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def EventId(self):
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def ParamOne(self):
        return self._ParamOne

    @ParamOne.setter
    def ParamOne(self, ParamOne):
        self._ParamOne = ParamOne

    @property
    def ParamTwo(self):
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
        return self._AudioEncode

    @AudioEncode.setter
    def AudioEncode(self, AudioEncode):
        self._AudioEncode = AudioEncode

    @property
    def SubscribeAudioList(self):
        return self._SubscribeAudioList

    @SubscribeAudioList.setter
    def SubscribeAudioList(self, SubscribeAudioList):
        self._SubscribeAudioList = SubscribeAudioList

    @property
    def UnSubscribeAudioList(self):
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
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
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
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
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
        return self._UserMediaStream

    @UserMediaStream.setter
    def UserMediaStream(self, UserMediaStream):
        self._UserMediaStream = UserMediaStream

    @property
    def ImageWidth(self):
        return self._ImageWidth

    @ImageWidth.setter
    def ImageWidth(self, ImageWidth):
        self._ImageWidth = ImageWidth

    @property
    def ImageHeight(self):
        return self._ImageHeight

    @ImageHeight.setter
    def ImageHeight(self, ImageHeight):
        self._ImageHeight = ImageHeight

    @property
    def LocationX(self):
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
        return self._ZOrder

    @ZOrder.setter
    def ZOrder(self, ZOrder):
        self._ZOrder = ZOrder

    @property
    def RenderMode(self):
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def BackGroundColor(self):
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def CustomCrop(self):
        return self._CustomCrop

    @CustomCrop.setter
    def CustomCrop(self, CustomCrop):
        self._CustomCrop = CustomCrop

    @property
    def BackgroundRenderMode(self):
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
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def PureAudioHoldPlaceMode(self):
        return self._PureAudioHoldPlaceMode

    @PureAudioHoldPlaceMode.setter
    def PureAudioHoldPlaceMode(self, PureAudioHoldPlaceMode):
        self._PureAudioHoldPlaceMode = PureAudioHoldPlaceMode

    @property
    def MixLayoutList(self):
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def MaxVideoUser(self):
        return self._MaxVideoUser

    @MaxVideoUser.setter
    def MaxVideoUser(self, MaxVideoUser):
        self._MaxVideoUser = MaxVideoUser

    @property
    def RenderMode(self):
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
        return self._AppData

    @AppData.setter
    def AppData(self, AppData):
        self._AppData = AppData

    @property
    def PayloadType(self):
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
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
        return self._PayloadContent

    @PayloadContent.setter
    def PayloadContent(self, PayloadContent):
        self._PayloadContent = PayloadContent

    @property
    def PayloadType(self):
        return self._PayloadType

    @PayloadType.setter
    def PayloadType(self, PayloadType):
        self._PayloadType = PayloadType

    @property
    def PayloadUuid(self):
        return self._PayloadUuid

    @PayloadUuid.setter
    def PayloadUuid(self, PayloadUuid):
        self._PayloadUuid = PayloadUuid

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def FollowIdr(self):
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
        return self._PublishCdnUrl

    @PublishCdnUrl.setter
    def PublishCdnUrl(self, PublishCdnUrl):
        self._PublishCdnUrl = PublishCdnUrl

    @property
    def IsTencentCdn(self):
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
        return self._LayoutVolume

    @LayoutVolume.setter
    def LayoutVolume(self, LayoutVolume):
        self._LayoutVolume = LayoutVolume

    @property
    def PassThrough(self):
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
        return self._VideoEncode

    @VideoEncode.setter
    def VideoEncode(self, VideoEncode):
        self._VideoEncode = VideoEncode

    @property
    def LayoutParams(self):
        return self._LayoutParams

    @LayoutParams.setter
    def LayoutParams(self, LayoutParams):
        self._LayoutParams = LayoutParams

    @property
    def BackGroundColor(self):
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def BackgroundImageUrl(self):
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def WaterMarkList(self):
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def BackgroundRenderMode(self):
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
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def WaterMarkWidth(self):
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def ZOrder(self):
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
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkText(self):
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
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def WaterMarkWidth(self):
        return self._WaterMarkWidth

    @WaterMarkWidth.setter
    def WaterMarkWidth(self, WaterMarkWidth):
        self._WaterMarkWidth = WaterMarkWidth

    @property
    def WaterMarkHeight(self):
        return self._WaterMarkHeight

    @WaterMarkHeight.setter
    def WaterMarkHeight(self, WaterMarkHeight):
        self._WaterMarkHeight = WaterMarkHeight

    @property
    def LocationX(self):
        return self._LocationX

    @LocationX.setter
    def LocationX(self, LocationX):
        self._LocationX = LocationX

    @property
    def LocationY(self):
        return self._LocationY

    @LocationY.setter
    def LocationY(self, LocationY):
        self._LocationY = LocationY

    @property
    def FontSize(self):
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
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
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Alpha(self):
        return self._Alpha

    @Alpha.setter
    def Alpha(self, Alpha):
        self._Alpha = Alpha

    @property
    def RenderMode(self):
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MediaId(self):
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def ImageLayer(self):
        return self._ImageLayer

    @ImageLayer.setter
    def ImageLayer(self, ImageLayer):
        self._ImageLayer = ImageLayer

    @property
    def SubBackgroundImage(self):
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
        return self._MixLayoutMode

    @MixLayoutMode.setter
    def MixLayoutMode(self, MixLayoutMode):
        self._MixLayoutMode = MixLayoutMode

    @property
    def MixLayoutList(self):
        return self._MixLayoutList

    @MixLayoutList.setter
    def MixLayoutList(self, MixLayoutList):
        self._MixLayoutList = MixLayoutList

    @property
    def BackGroundColor(self):
        return self._BackGroundColor

    @BackGroundColor.setter
    def BackGroundColor(self, BackGroundColor):
        self._BackGroundColor = BackGroundColor

    @property
    def MaxResolutionUserId(self):
        return self._MaxResolutionUserId

    @MaxResolutionUserId.setter
    def MaxResolutionUserId(self, MaxResolutionUserId):
        self._MaxResolutionUserId = MaxResolutionUserId

    @property
    def MediaId(self):
        return self._MediaId

    @MediaId.setter
    def MediaId(self, MediaId):
        self._MediaId = MediaId

    @property
    def BackgroundImageUrl(self):
        return self._BackgroundImageUrl

    @BackgroundImageUrl.setter
    def BackgroundImageUrl(self, BackgroundImageUrl):
        self._BackgroundImageUrl = BackgroundImageUrl

    @property
    def PlaceHolderMode(self):
        return self._PlaceHolderMode

    @PlaceHolderMode.setter
    def PlaceHolderMode(self, PlaceHolderMode):
        self._PlaceHolderMode = PlaceHolderMode

    @property
    def BackgroundImageRenderMode(self):
        return self._BackgroundImageRenderMode

    @BackgroundImageRenderMode.setter
    def BackgroundImageRenderMode(self, BackgroundImageRenderMode):
        self._BackgroundImageRenderMode = BackgroundImageRenderMode

    @property
    def DefaultSubBackgroundImage(self):
        return self._DefaultSubBackgroundImage

    @DefaultSubBackgroundImage.setter
    def DefaultSubBackgroundImage(self, DefaultSubBackgroundImage):
        self._DefaultSubBackgroundImage = DefaultSubBackgroundImage

    @property
    def WaterMarkList(self):
        return self._WaterMarkList

    @WaterMarkList.setter
    def WaterMarkList(self, WaterMarkList):
        self._WaterMarkList = WaterMarkList

    @property
    def RenderMode(self):
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def MaxResolutionUserAlign(self):
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
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def AudioParams(self):
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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def MixLayoutParams(self):
        return self._MixLayoutParams

    @MixLayoutParams.setter
    def MixLayoutParams(self, MixLayoutParams):
        self._MixLayoutParams = MixLayoutParams

    @property
    def SubscribeStreamUserIds(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
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
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def PeerId(self):
        return self._PeerId

    @PeerId.setter
    def PeerId(self, PeerId):
        self._PeerId = PeerId

    @property
    def DataType(self):
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
        return self._RecordMode

    @RecordMode.setter
    def RecordMode(self, RecordMode):
        self._RecordMode = RecordMode

    @property
    def MaxIdleTime(self):
        return self._MaxIdleTime

    @MaxIdleTime.setter
    def MaxIdleTime(self, MaxIdleTime):
        self._MaxIdleTime = MaxIdleTime

    @property
    def StreamType(self):
        return self._StreamType

    @StreamType.setter
    def StreamType(self, StreamType):
        self._StreamType = StreamType

    @property
    def SubscribeStreamUserIds(self):
        return self._SubscribeStreamUserIds

    @SubscribeStreamUserIds.setter
    def SubscribeStreamUserIds(self, SubscribeStreamUserIds):
        self._SubscribeStreamUserIds = SubscribeStreamUserIds

    @property
    def OutputFormat(self):
        return self._OutputFormat

    @OutputFormat.setter
    def OutputFormat(self, OutputFormat):
        self._OutputFormat = OutputFormat

    @property
    def AvMerge(self):
        return self._AvMerge

    @AvMerge.setter
    def AvMerge(self, AvMerge):
        self._AvMerge = AvMerge

    @property
    def MaxMediaFileDuration(self):
        return self._MaxMediaFileDuration

    @MaxMediaFileDuration.setter
    def MaxMediaFileDuration(self, MaxMediaFileDuration):
        self._MaxMediaFileDuration = MaxMediaFileDuration

    @property
    def MediaId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserIds(self):
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
        return self._CommId

    @CommId.setter
    def CommId(self, CommId):
        self._CommId = CommId

    @property
    def RoomString(self):
        return self._RoomString

    @RoomString.setter
    def RoomString(self, RoomString):
        self._RoomString = RoomString

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def IsFinished(self):
        return self._IsFinished

    @IsFinished.setter
    def IsFinished(self, IsFinished):
        self._IsFinished = IsFinished

    @property
    def UserId(self):
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
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def UserNumber(self):
        return self._UserNumber

    @UserNumber.setter
    def UserNumber(self, UserNumber):
        self._UserNumber = UserNumber

    @property
    def UserCount(self):
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount

    @property
    def RoomNumbers(self):
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
        return self._Columns

    @Columns.setter
    def Columns(self, Columns):
        self._Columns = Columns

    @property
    def Values(self):
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
        :param _IsMute: Whether to disable the user’s audio and video. 0: Enable; 1: Disable.
        :type IsMute: int
        """
        self._SdkAppId = None
        self._StrRoomId = None
        self._UserId = None
        self._IsMute = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def StrRoomId(self):
        return self._StrRoomId

    @StrRoomId.setter
    def StrRoomId(self, StrRoomId):
        self._StrRoomId = StrRoomId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsMute(self):
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
        :param _IsMute: Whether to disable the user’s audio and video. 0: Enable; 1: Disable.
        :type IsMute: int
        """
        self._SdkAppId = None
        self._RoomId = None
        self._UserId = None
        self._IsMute = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def IsMute(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def AgentParams(self):
        return self._AgentParams

    @AgentParams.setter
    def AgentParams(self, AgentParams):
        self._AgentParams = AgentParams

    @property
    def WithTranscoding(self):
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
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
        :param _RoomIdType: Type of TRTC RoomId. 【*Note】Must be the same as the RoomId type corresponding to the Record room: 0: String type RoomId 1: 32-bit Integer type RoomId (default)
        :type RoomIdType: int
        :param _UserId: UserId of the Pull stream Relay Robot, used to enter the room and initiate the Pull stream Relay Task.
        :type UserId: str
        :param _UserSig: UserSig corresponding to the Pull stream Relay Robot UserId, i.e., UserId and UserSig are equivalent to the Robot's Login password for entering the room. For the specific Calculation method, please refer to the TRTC [UserSig](https://intl.cloud.tencent.com/document/product/647/45910?from_cn_redirect=1#UserSig) Scheme.
        :type UserSig: str
        :param _SourceUrl: 	
Source URL. Example value: https://a.b/test.mp4
        :type SourceUrl: list of str
        :param _PrivateMapKey: TRTC room permission Encryption ticket, only needed when advanced permission control is enabled in the Console. After enabling advanced permission control in the TRTC Console, TRTC's backend service system will verify a so-called [PrivateMapKey] 'Permission ticket', which contains an encrypted RoomId and an encrypted 'Permission bit list'. Since PrivateMapKey contains RoomId, providing only UserSig without PrivateMapKey does not allow entry into the specified room.
        :type PrivateMapKey: str
        :param _VideoEncodeParams: Video Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :type VideoEncodeParams: :class:`tencentcloud.trtc.v20190722.models.VideoEncodeParams`
        :param _AudioEncodeParams: Audio Codec Parameters. Optional, if not filled, Keep original stream Parameters.
        :type AudioEncodeParams: :class:`tencentcloud.trtc.v20190722.models.AudioEncodeParams`
        """
        self._SdkAppId = None
        self._RoomId = None
        self._RoomIdType = None
        self._UserId = None
        self._UserSig = None
        self._SourceUrl = None
        self._PrivateMapKey = None
        self._VideoEncodeParams = None
        self._AudioEncodeParams = None

    @property
    def SdkAppId(self):
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def RoomId(self):
        return self._RoomId

    @RoomId.setter
    def RoomId(self, RoomId):
        self._RoomId = RoomId

    @property
    def RoomIdType(self):
        return self._RoomIdType

    @RoomIdType.setter
    def RoomIdType(self, RoomIdType):
        self._RoomIdType = RoomIdType

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserSig(self):
        return self._UserSig

    @UserSig.setter
    def UserSig(self, UserSig):
        self._UserSig = UserSig

    @property
    def SourceUrl(self):
        return self._SourceUrl

    @SourceUrl.setter
    def SourceUrl(self, SourceUrl):
        self._SourceUrl = SourceUrl

    @property
    def PrivateMapKey(self):
        return self._PrivateMapKey

    @PrivateMapKey.setter
    def PrivateMapKey(self, PrivateMapKey):
        self._PrivateMapKey = PrivateMapKey

    @property
    def VideoEncodeParams(self):
        return self._VideoEncodeParams

    @VideoEncodeParams.setter
    def VideoEncodeParams(self, VideoEncodeParams):
        self._VideoEncodeParams = VideoEncodeParams

    @property
    def AudioEncodeParams(self):
        return self._AudioEncodeParams

    @AudioEncodeParams.setter
    def AudioEncodeParams(self, AudioEncodeParams):
        self._AudioEncodeParams = AudioEncodeParams


    def _deserialize(self, params):
        self._SdkAppId = params.get("SdkAppId")
        self._RoomId = params.get("RoomId")
        self._RoomIdType = params.get("RoomIdType")
        self._UserId = params.get("UserId")
        self._UserSig = params.get("UserSig")
        self._SourceUrl = params.get("SourceUrl")
        self._PrivateMapKey = params.get("PrivateMapKey")
        if params.get("VideoEncodeParams") is not None:
            self._VideoEncodeParams = VideoEncodeParams()
            self._VideoEncodeParams._deserialize(params.get("VideoEncodeParams"))
        if params.get("AudioEncodeParams") is not None:
            self._AudioEncodeParams = AudioEncodeParams()
            self._AudioEncodeParams._deserialize(params.get("AudioEncodeParams"))
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
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
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def TrackType(self):
        return self._TrackType

    @TrackType.setter
    def TrackType(self, TrackType):
        self._TrackType = TrackType

    @property
    def BeginTimeStamp(self):
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
        return self._CloudStorage

    @CloudStorage.setter
    def CloudStorage(self, CloudStorage):
        self._CloudStorage = CloudStorage

    @property
    def CloudVod(self):
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
        return self._SubscribeAudioUserIds

    @SubscribeAudioUserIds.setter
    def SubscribeAudioUserIds(self, SubscribeAudioUserIds):
        self._SubscribeAudioUserIds = SubscribeAudioUserIds

    @property
    def UnSubscribeAudioUserIds(self):
        return self._UnSubscribeAudioUserIds

    @UnSubscribeAudioUserIds.setter
    def UnSubscribeAudioUserIds(self, UnSubscribeAudioUserIds):
        self._UnSubscribeAudioUserIds = UnSubscribeAudioUserIds

    @property
    def SubscribeVideoUserIds(self):
        return self._SubscribeVideoUserIds

    @SubscribeVideoUserIds.setter
    def SubscribeVideoUserIds(self, SubscribeVideoUserIds):
        self._SubscribeVideoUserIds = SubscribeVideoUserIds

    @property
    def UnSubscribeVideoUserIds(self):
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
        return self._StatementID

    @StatementID.setter
    def StatementID(self, StatementID):
        self._StatementID = StatementID

    @property
    def Series(self):
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series

    @property
    def Total(self):
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
        return self._Procedure

    @Procedure.setter
    def Procedure(self, Procedure):
        self._Procedure = Procedure

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def StorageRegion(self):
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def ClassId(self):
        return self._ClassId

    @ClassId.setter
    def ClassId(self, ClassId):
        self._ClassId = ClassId

    @property
    def SubAppId(self):
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def SessionContext(self):
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext

    @property
    def SourceContext(self):
        return self._SourceContext

    @SourceContext.setter
    def SourceContext(self, SourceContext):
        self._SourceContext = SourceContext

    @property
    def MediaType(self):
        return self._MediaType

    @MediaType.setter
    def MediaType(self, MediaType):
        self._MediaType = MediaType

    @property
    def UserDefineRecordId(self):
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
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
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
        return self._TimeKey

    @TimeKey.setter
    def TimeKey(self, TimeKey):
        self._TimeKey = TimeKey

    @property
    def UsageValue(self):
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
        return self._SdkAppId

    @SdkAppId.setter
    def SdkAppId(self, SdkAppId):
        self._SdkAppId = SdkAppId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SequenceNumber(self):
        return self._SequenceNumber

    @SequenceNumber.setter
    def SequenceNumber(self, SequenceNumber):
        self._SequenceNumber = SequenceNumber

    @property
    def WithTranscoding(self):
        return self._WithTranscoding

    @WithTranscoding.setter
    def WithTranscoding(self, WithTranscoding):
        self._WithTranscoding = WithTranscoding

    @property
    def AudioParams(self):
        return self._AudioParams

    @AudioParams.setter
    def AudioParams(self, AudioParams):
        self._AudioParams = AudioParams

    @property
    def VideoParams(self):
        return self._VideoParams

    @VideoParams.setter
    def VideoParams(self, VideoParams):
        self._VideoParams = VideoParams

    @property
    def SingleSubscribeParams(self):
        return self._SingleSubscribeParams

    @SingleSubscribeParams.setter
    def SingleSubscribeParams(self, SingleSubscribeParams):
        self._SingleSubscribeParams = SingleSubscribeParams

    @property
    def PublishCdnParams(self):
        return self._PublishCdnParams

    @PublishCdnParams.setter
    def PublishCdnParams(self, PublishCdnParams):
        self._PublishCdnParams = PublishCdnParams

    @property
    def SeiParams(self):
        return self._SeiParams

    @SeiParams.setter
    def SeiParams(self, SeiParams):
        self._SeiParams = SeiParams

    @property
    def FeedBackRoomParams(self):
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
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
        return self._RoomStr

    @RoomStr.setter
    def RoomStr(self, RoomStr):
        self._RoomStr = RoomStr

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def JoinTs(self):
        return self._JoinTs

    @JoinTs.setter
    def JoinTs(self, JoinTs):
        self._JoinTs = JoinTs

    @property
    def LeaveTs(self):
        return self._LeaveTs

    @LeaveTs.setter
    def LeaveTs(self, LeaveTs):
        self._LeaveTs = LeaveTs

    @property
    def DeviceType(self):
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def SdkVersion(self):
        return self._SdkVersion

    @SdkVersion.setter
    def SdkVersion(self, SdkVersion):
        self._SdkVersion = SdkVersion

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Finished(self):
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
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

    @property
    def StreamType(self):
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
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
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
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
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
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def BitRate(self):
        return self._BitRate

    @BitRate.setter
    def BitRate(self, BitRate):
        self._BitRate = BitRate

    @property
    def Gop(self):
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
        return self._WaterMarkType

    @WaterMarkType.setter
    def WaterMarkType(self, WaterMarkType):
        self._WaterMarkType = WaterMarkType

    @property
    def WaterMarkImage(self):
        return self._WaterMarkImage

    @WaterMarkImage.setter
    def WaterMarkImage(self, WaterMarkImage):
        self._WaterMarkImage = WaterMarkImage

    @property
    def WaterMarkChar(self):
        return self._WaterMarkChar

    @WaterMarkChar.setter
    def WaterMarkChar(self, WaterMarkChar):
        self._WaterMarkChar = WaterMarkChar

    @property
    def WaterMarkTimestamp(self):
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
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Chars(self):
        return self._Chars

    @Chars.setter
    def Chars(self, Chars):
        self._Chars = Chars

    @property
    def FontSize(self):
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor

    @property
    def BackGroundColor(self):
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
        return self._WaterMarkUrl

    @WaterMarkUrl.setter
    def WaterMarkUrl(self, WaterMarkUrl):
        self._WaterMarkUrl = WaterMarkUrl

    @property
    def Top(self):
        return self._Top

    @Top.setter
    def Top(self, Top):
        self._Top = Top

    @property
    def Left(self):
        return self._Left

    @Left.setter
    def Left(self, Left):
        self._Left = Left

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
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
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos

    @property
    def TimeZone(self):
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
        