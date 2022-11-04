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


class AgentParams(AbstractModel):
    """The information of the relaying robot in the room.

    """

    def __init__(self):
        r"""
        :param UserId: The [user ID](https://intl.cloud.tencent.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :type UserId: str
        :param UserSig: The signature (similar to a login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104). |
        :type UserSig: str
        :param MaxIdleTime: The timeout period (seconds) for relaying to stop automatically after all the users whose streams are mixed leave the room. The value cannot be smaller than 5 or larger than 86400 (24 hours). Default value: 30.
        :type MaxIdleTime: int
        """
        self.UserId = None
        self.UserSig = None
        self.MaxIdleTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.UserSig = params.get("UserSig")
        self.MaxIdleTime = params.get("MaxIdleTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioEncode(AbstractModel):
    """The audio encoding parameters.

    """

    def __init__(self):
        r"""
        :param SampleRate: The audio sample rate (Hz). Valid values: 48000, 44100, 32000, 24000, 16000, 8000.
        :type SampleRate: int
        :param Channel: The number of sound channels. Valid values: 1 (mono), 2 (dual).
        :type Channel: int
        :param BitRate: The audio bitrate (Kbps). Value range: 8-500.
        :type BitRate: int
        :param Codec: The audio codec. Valid values: 0 (LC-AAC), 1 (HE-AAC), 2 (HE-AACv2). The default value is 0. If this parameter is set to 2, `Channel` must be 2. If it is set to 1 or 2, `SampleRate` can only be 48000, 44100, 32000, 24000, or 16000.
        :type Codec: int
        """
        self.SampleRate = None
        self.Channel = None
        self.BitRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.SampleRate = params.get("SampleRate")
        self.Channel = params.get("Channel")
        self.BitRate = params.get("BitRate")
        self.Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioParams(AbstractModel):
    """The audio transcoding parameters for recording.

    """

    def __init__(self):
        r"""
        :param SampleRate: The audio sample rate.
1: 48000 Hz (default)
2: 44100 Hz
3: 16000 Hz
        :type SampleRate: int
        :param Channel: The number of sound channels.
1: Mono-channel
2: Dual-channel (default)
        :type Channel: int
        :param BitRate: The audio bitrate (bps). Value range: [32000, 128000]. Default: 64000.
        :type BitRate: int
        """
        self.SampleRate = None
        self.Channel = None
        self.BitRate = None


    def _deserialize(self, params):
        self.SampleRate = params.get("SampleRate")
        self.Channel = params.get("Channel")
        self.BitRate = params.get("BitRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudStorage(AbstractModel):
    """The cloud storage information.

    """

    def __init__(self):
        r"""
        :param Vendor: The cloud storage provider.
0: Tencent Cloud COS. The storage services of other providers are not supported currently.
        :type Vendor: int
        :param Region: The region of cloud storage.
        :type Region: str
        :param Bucket: The storage bucket.
        :type Bucket: str
        :param AccessKey: The access_key of the cloud storage account.
        :type AccessKey: str
        :param SecretKey: The secret_key of the cloud storage account.
        :type SecretKey: str
        :param FileNamePrefix: The bucket to save data, which is an array of strings that can contain letters (a-z and A-Z), numbers (0-9), underscores (_), and hyphens (-). For example, if the value of this parameter is `["prefix1", "prefix2"]`, the recording file `xxx.m3u8` will be saved as `prefix1/prefix2/TaskId/xxx.m3u8`.
        :type FileNamePrefix: list of str
        """
        self.Vendor = None
        self.Region = None
        self.Bucket = None
        self.AccessKey = None
        self.SecretKey = None
        self.FileNamePrefix = None


    def _deserialize(self, params):
        self.Vendor = params.get("Vendor")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")
        self.FileNamePrefix = params.get("FileNamePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudVod(AbstractModel):
    """The VOD parameters.

    """

    def __init__(self):
        r"""
        :param TencentVod: The Tencent Cloud VOD parameters.
        :type TencentVod: :class:`tencentcloud.trtc.v20190722.models.TencentVod`
        """
        self.TencentVod = None


    def _deserialize(self, params):
        if params.get("TencentVod") is not None:
            self.TencentVod = TencentVod()
            self.TencentVod._deserialize(params.get("TencentVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingRequest(AbstractModel):
    """CreateCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :type SdkAppId: int
        :param RoomId: The [room ID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are recorded.
        :type RoomId: str
        :param UserId: The [user ID](https://www.tencentcloud.com/document/product/647/37714#userid) of the recording robot in the TRTC room, which cannot be identical to the user IDs of anchors in the room or other recording robots. To distinguish this user ID from others, we recommend you include the room ID in the user ID.
        :type UserId: str
        :param UserSig: The signature (similar to a login password) required for the recording robot to enter the room. Each user ID corresponds to a signature. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104).
        :type UserSig: str
        :param RecordParams: The on-cloud recording parameters.
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        :param StorageParams: The cloud storage information of the recording file. Currently, you can only save recording files to Tencent Cloud VOD.
        :type StorageParams: :class:`tencentcloud.trtc.v20190722.models.StorageParams`
        :param RoomIdType: The type of the TRTC room ID, which must be the same as the ID type of the room whose streams are recorded.
0: String
1: 32-bit integer (default)
        :type RoomIdType: int
        :param MixTranscodeParams: The stream mixing parameters, which are valid if the mixed-stream recording mode is used.
        :type MixTranscodeParams: :class:`tencentcloud.trtc.v20190722.models.MixTranscodeParams`
        :param MixLayoutParams: The layout parameters, which are valid if the mixed-stream recording mode is used.
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param ResourceExpiredHour: The amount of time (in hours) during which API requests can be made after recording starts. Calculation starts when a recording task is started (when the recording task ID is returned). Once the period elapses, the query, modification, and stop recording APIs can no longer be called, but the recording task will continue. The default value is `72` (three days), and the maximum and minimum values allowed are `720` (30 days) and `6` respectively. If you do not set this parameter, the query, modification, and stop recording APIs can be called within 72 hours after recording starts.
        :type ResourceExpiredHour: int
        :param PrivateMapKey: The permission ticket for a TRTC room. This parameter is required if advanced permission control is enabled in the console, in which case the TRTC backend will verify users’ [PrivateMapKey](https://intl.cloud.tencent.com/document/product/647/32240?from_cn_redirect=1), which include an encrypted room ID and permission bit list. A user providing only `UserSig` and not `PrivateMapKey` will be unable to enter the room.
        :type PrivateMapKey: str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserId = None
        self.UserSig = None
        self.RecordParams = None
        self.StorageParams = None
        self.RoomIdType = None
        self.MixTranscodeParams = None
        self.MixLayoutParams = None
        self.ResourceExpiredHour = None
        self.PrivateMapKey = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserId = params.get("UserId")
        self.UserSig = params.get("UserSig")
        if params.get("RecordParams") is not None:
            self.RecordParams = RecordParams()
            self.RecordParams._deserialize(params.get("RecordParams"))
        if params.get("StorageParams") is not None:
            self.StorageParams = StorageParams()
            self.StorageParams._deserialize(params.get("StorageParams"))
        self.RoomIdType = params.get("RoomIdType")
        if params.get("MixTranscodeParams") is not None:
            self.MixTranscodeParams = MixTranscodeParams()
            self.MixTranscodeParams._deserialize(params.get("MixTranscodeParams"))
        if params.get("MixLayoutParams") is not None:
            self.MixLayoutParams = MixLayoutParams()
            self.MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        self.ResourceExpiredHour = params.get("ResourceExpiredHour")
        self.PrivateMapKey = params.get("PrivateMapKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudRecordingResponse(AbstractModel):
    """CreateCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends. After a recording task starts, if you want to perform other actions on the task, you need to specify the task ID when making API requests.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteCloudRecordingRequest(AbstractModel):
    """DeleteCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudRecordingResponse(AbstractModel):
    """DeleteCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeCloudRecordingRequest(AbstractModel):
    """DescribeCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudRecordingResponse(AbstractModel):
    """DescribeCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The unique ID of the recording task.
        :type TaskId: str
        :param Status: The status of the on-cloud recording task.
Idle: The task is idle.
InProgress: The task is in progress.
Exited: The task is being ended.
        :type Status: str
        :param StorageFileList: The information of the recording files.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type StorageFileList: list of StorageFile
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.Status = None
        self.StorageFileList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        if params.get("StorageFileList") is not None:
            self.StorageFileList = []
            for item in params.get("StorageFileList"):
                obj = StorageFile()
                obj._deserialize(item)
                self.StorageFileList.append(obj)
        self.RequestId = params.get("RequestId")


class DismissRoomByStrRoomIdRequest(AbstractModel):
    """DismissRoomByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param RoomId: Room ID
        :type RoomId: str
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomByStrRoomIdResponse(AbstractModel):
    """DismissRoomByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param RoomId: Room number.
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismissRoomResponse(AbstractModel):
    """DismissRoom response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MaxVideoUser(AbstractModel):
    """The information of the large video in screen sharing or floating layout mode.

    """

    def __init__(self):
        r"""
        :param UserMediaStream: The stream information.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self.UserMediaStream = None


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self.UserMediaStream = UserMediaStream()
            self.UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuAudioParams(AbstractModel):
    """The audio parameters for relaying.

    """

    def __init__(self):
        r"""
        :param AudioEncode: The audio encoding parameters.
        :type AudioEncode: :class:`tencentcloud.trtc.v20190722.models.AudioEncode`
        :param SubscribeAudioList: The audio mix allowlist. For the `StartPublishCdnStream` API, if you do not pass this parameter or leave it empty, the audios of all anchors will be mixed. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current allowlist; if you pass in an empty string, the audios of all anchors will be mixed.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :type SubscribeAudioList: list of McuUserInfoParams
        :param UnSubscribeAudioList: The audio mix blocklist. If you do not pass this parameter or leave it empty, there won’t be a blocklist. For the `UpdatePublishCdnStream` API, if you do not pass this parameter, no changes will be made to the current blocklist; if you pass in an empty string, the blocklist will be reset.
In cases where `SubscribeAudioList` and `UnSubscribeAudioList` are used at the same time, you need to specify both parameters. If you pass neither `SubscribeAudioList` nor `UnSubscribeAudioList`, no changes will be made. If a user is included in both parameters, the user’s audio will not be mixed.
        :type UnSubscribeAudioList: list of McuUserInfoParams
        """
        self.AudioEncode = None
        self.SubscribeAudioList = None
        self.UnSubscribeAudioList = None


    def _deserialize(self, params):
        if params.get("AudioEncode") is not None:
            self.AudioEncode = AudioEncode()
            self.AudioEncode._deserialize(params.get("AudioEncode"))
        if params.get("SubscribeAudioList") is not None:
            self.SubscribeAudioList = []
            for item in params.get("SubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self.SubscribeAudioList.append(obj)
        if params.get("UnSubscribeAudioList") is not None:
            self.UnSubscribeAudioList = []
            for item in params.get("UnSubscribeAudioList"):
                obj = McuUserInfoParams()
                obj._deserialize(item)
                self.UnSubscribeAudioList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuCustomCrop(AbstractModel):
    """The cropping parameters for mixed videos.

    """

    def __init__(self):
        r"""
        :param LocationX: The horizontal offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :type LocationX: int
        :param LocationY: The vertical offset (pixels) of the starting point for cropping. This parameter must be greater than 0.
        :type LocationY: int
        :param Width: The video width (pixels) after cropping. The sum of this parameter and `LocationX` cannot be greater than 10000.
        :type Width: int
        :param Height: The video height (pixels) after cropping. The sum of this parameter and `LocationY` cannot be greater than 10000.
        :type Height: int
        """
        self.LocationX = None
        self.LocationY = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuFeedBackRoomParams(AbstractModel):
    """Parameters for relaying to a TRTC room.

    """

    def __init__(self):
        r"""
        :param RoomId: The room ID.
        :type RoomId: str
        :param RoomIdType: The ID type of the room to which streams are relayed. `0` indicates integer, and `1` indicates string.
        :type RoomIdType: int
        :param UserId: The [user ID](https://intl.cloud.tencent.com/document/product/647/37714) of the relaying robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include the room ID in this user ID.
        :type UserId: str
        :param UserSig: The signature (similar to login password) required for the relaying robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104).
        :type UserSig: str
        """
        self.RoomId = None
        self.RoomIdType = None
        self.UserId = None
        self.UserSig = None


    def _deserialize(self, params):
        self.RoomId = params.get("RoomId")
        self.RoomIdType = params.get("RoomIdType")
        self.UserId = params.get("UserId")
        self.UserSig = params.get("UserSig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayout(AbstractModel):
    """The layout parameters.

    """

    def __init__(self):
        r"""
        :param UserMediaStream: The information of the stream that is displayed. If you do not pass this parameter, TRTC will display the videos of anchors in the room according to their room entry sequence.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        :param ImageWidth: The video width (pixels). If you do not pass this parameter, 0 will be used.
        :type ImageWidth: int
        :param ImageHeight: The video height (pixels). If you do not pass this parameter, 0 will be used.
        :type ImageHeight: int
        :param LocationX: The horizontal offset (pixels) of the video. The sum of `LocationX` and `ImageWidth` cannot exceed the width of the canvas. If you do not pass this parameter, 0 will be used.
        :type LocationX: int
        :param LocationY: The vertical offset of the video. The sum of `LocationY` and `ImageHeight` cannot exceed the height of the canvas. If you do not pass this parameter, 0 will be used.
        :type LocationY: int
        :param ZOrder: The image layer of the video. If you do not pass this parameter, 0 will be used.
        :type ZOrder: int
        :param RenderMode: The rendering mode of the video. 0 (the video is scaled and the excess parts are cropped), 1 (the video is scaled), 2 (the video is scaled and the blank spaces are filled with black bars). If you do not pass this parameter, 0 will be used.
        :type RenderMode: int
        :param BackGroundColor: The background color of the video. Below are the values for some common colors:
Red: 0xcc0033
Yellow: 0xcc9900
Green: 0xcccc33
Blue: 0x99CCFF
Black: 0x000000
White: 0xFFFFFF
Grey: 0x999999
        :type BackGroundColor: str
        :param BackgroundImageUrl: The URL of the background image for the video. This parameter allows you to specify an image to display when the user’s camera is turned off or before the user enters the room. If the dimensions of the image specified are different from those of the video window, the image will be stretched to fit the space. This parameter has a higher priority than `BackGroundColor`.
        :type BackgroundImageUrl: str
        :param CustomCrop: Custom cropping.
        :type CustomCrop: :class:`tencentcloud.trtc.v20190722.models.McuCustomCrop`
        """
        self.UserMediaStream = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.ZOrder = None
        self.RenderMode = None
        self.BackGroundColor = None
        self.BackgroundImageUrl = None
        self.CustomCrop = None


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self.UserMediaStream = UserMediaStream()
            self.UserMediaStream._deserialize(params.get("UserMediaStream"))
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.ZOrder = params.get("ZOrder")
        self.RenderMode = params.get("RenderMode")
        self.BackGroundColor = params.get("BackGroundColor")
        self.BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("CustomCrop") is not None:
            self.CustomCrop = McuCustomCrop()
            self.CustomCrop._deserialize(params.get("CustomCrop"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutParams(AbstractModel):
    """The layout parameters.

    """

    def __init__(self):
        r"""
        :param MixLayoutMode: The layout mode. Valid values: 1 (floating), 2 (screen sharing), 3 (grid), 4 (custom). Floating, screen sharing, and grid are dynamic layouts. Custom layouts are static layouts.
        :type MixLayoutMode: int
        :param PureAudioHoldPlaceMode: Whether to display users who publish only audio. 0: Yes; 1: No. This parameter is valid only if dynamic layouts are used. If you do not pass this parameter, 0 will be used.
        :type PureAudioHoldPlaceMode: int
        :param MixLayoutList: The details of a custom layout.
        :type MixLayoutList: list of McuLayout
        :param MaxVideoUser: The information of the large video in screen sharing or floating layout mode.
        :type MaxVideoUser: :class:`tencentcloud.trtc.v20190722.models.MaxVideoUser`
        """
        self.MixLayoutMode = None
        self.PureAudioHoldPlaceMode = None
        self.MixLayoutList = None
        self.MaxVideoUser = None


    def _deserialize(self, params):
        self.MixLayoutMode = params.get("MixLayoutMode")
        self.PureAudioHoldPlaceMode = params.get("PureAudioHoldPlaceMode")
        if params.get("MixLayoutList") is not None:
            self.MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = McuLayout()
                obj._deserialize(item)
                self.MixLayoutList.append(obj)
        if params.get("MaxVideoUser") is not None:
            self.MaxVideoUser = MaxVideoUser()
            self.MaxVideoUser._deserialize(params.get("MaxVideoUser"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuLayoutVolume(AbstractModel):
    """The SEI parameters for audio volume layout. You can specify the `AppData` and `PayloadType`.
    This parameter may be empty, in which case the default SEI parameters for audio volume layout will be used.

    """

    def __init__(self):
        r"""
        :param AppData: The application data, which will be embedded in the `app_data` field of the custom SEI. It must be shorter than 4,096 characters.
        :type AppData: str
        :param PayloadType: The payload type of the SEI message. The default is 100. Value range: 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :type PayloadType: int
        """
        self.AppData = None
        self.PayloadType = None


    def _deserialize(self, params):
        self.AppData = params.get("AppData")
        self.PayloadType = params.get("PayloadType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPassThrough(AbstractModel):
    """The custom pass-through SEI.

    """

    def __init__(self):
        r"""
        :param PayloadContent: The payload of the pass-through SEI.
        :type PayloadContent: str
        :param PayloadType: The payload type of the SEI message. Value range: 5 and 100-254 (244 is used internally by Tencent Cloud for timestamps).
        :type PayloadType: int
        :param PayloadUuid: This parameter is required only if `PayloadType` is 5. It must be a 32-character hexadecimal string. If `PayloadType` is not 5, this parameter will be ignored.
        :type PayloadUuid: str
        """
        self.PayloadContent = None
        self.PayloadType = None
        self.PayloadUuid = None


    def _deserialize(self, params):
        self.PayloadContent = params.get("PayloadContent")
        self.PayloadType = params.get("PayloadType")
        self.PayloadUuid = params.get("PayloadUuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuPublishCdnParam(AbstractModel):
    """The relaying parameters.

    """

    def __init__(self):
        r"""
        :param PublishCdnUrl: The URLs of the CDNs to relay to.
        :type PublishCdnUrl: str
        :param IsTencentCdn: Whether to relay to Tencent Cloud’s CDN. 0: Third-party CDN; 1 (default): Tencent Cloud’s CDN. Relaying to a third-party CDN will incur fees. To avoid unexpected charges, we recommend you pass in a specific value. For details, see the API document.
        :type IsTencentCdn: int
        """
        self.PublishCdnUrl = None
        self.IsTencentCdn = None


    def _deserialize(self, params):
        self.PublishCdnUrl = params.get("PublishCdnUrl")
        self.IsTencentCdn = params.get("IsTencentCdn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuSeiParams(AbstractModel):
    """The stream mixing SEI parameters.

    """

    def __init__(self):
        r"""
        :param LayoutVolume: The audio volume layout SEI.
        :type LayoutVolume: :class:`tencentcloud.trtc.v20190722.models.McuLayoutVolume`
        :param PassThrough: The pass-through SEI.
        :type PassThrough: :class:`tencentcloud.trtc.v20190722.models.McuPassThrough`
        """
        self.LayoutVolume = None
        self.PassThrough = None


    def _deserialize(self, params):
        if params.get("LayoutVolume") is not None:
            self.LayoutVolume = McuLayoutVolume()
            self.LayoutVolume._deserialize(params.get("LayoutVolume"))
        if params.get("PassThrough") is not None:
            self.PassThrough = McuPassThrough()
            self.PassThrough._deserialize(params.get("PassThrough"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuUserInfoParams(AbstractModel):
    """The users whose streams are mixed.

    """

    def __init__(self):
        r"""
        :param UserInfo: The user information.
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        """
        self.UserInfo = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = MixUserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuVideoParams(AbstractModel):
    """The video parameters for relaying.

    """

    def __init__(self):
        r"""
        :param VideoEncode: The video encoding parameters.
        :type VideoEncode: :class:`tencentcloud.trtc.v20190722.models.VideoEncode`
        :param LayoutParams: The layout parameters.
        :type LayoutParams: :class:`tencentcloud.trtc.v20190722.models.McuLayoutParams`
        :param BackGroundColor: The canvas color. Below are the values for some common colors:
Red: 0xcc0033
Yellow: 0xcc9900
Green: 0xcccc33
Blue: 0x99CCFF
Black: 0x000000
White: 0xFFFFFF
Grey: 0x999999
        :type BackGroundColor: str
        :param BackgroundImageUrl: The URL of the background image for the canvas. This parameter has a higher priority than `BackGroundColor`.
        :type BackgroundImageUrl: str
        :param WaterMarkList: The watermark information for the mixed stream.
        :type WaterMarkList: list of McuWaterMarkParams
        """
        self.VideoEncode = None
        self.LayoutParams = None
        self.BackGroundColor = None
        self.BackgroundImageUrl = None
        self.WaterMarkList = None


    def _deserialize(self, params):
        if params.get("VideoEncode") is not None:
            self.VideoEncode = VideoEncode()
            self.VideoEncode._deserialize(params.get("VideoEncode"))
        if params.get("LayoutParams") is not None:
            self.LayoutParams = McuLayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.BackGroundColor = params.get("BackGroundColor")
        self.BackgroundImageUrl = params.get("BackgroundImageUrl")
        if params.get("WaterMarkList") is not None:
            self.WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = McuWaterMarkParams()
                obj._deserialize(item)
                self.WaterMarkList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkImage(AbstractModel):
    """The information of the watermark image.

    """

    def __init__(self):
        r"""
        :param WaterMarkUrl: The URL of the watermark image, which must be in PNG, JPG, or JPEG format and cannot exceed 5 MB.
        :type WaterMarkUrl: str
        :param WaterMarkWidth: The watermark width (pixels).
        :type WaterMarkWidth: int
        :param WaterMarkHeight: The watermark height (pixels).
        :type WaterMarkHeight: int
        :param LocationX: The horizontal offset (pixels) of the watermark.
        :type LocationX: int
        :param LocationY: The vertical offset (pixels) of the watermark.
        :type LocationY: int
        :param ZOrder: The image layer of the watermark. If you do not pass this parameter, 0 will be used.
        :type ZOrder: int
        """
        self.WaterMarkUrl = None
        self.WaterMarkWidth = None
        self.WaterMarkHeight = None
        self.LocationX = None
        self.LocationY = None
        self.ZOrder = None


    def _deserialize(self, params):
        self.WaterMarkUrl = params.get("WaterMarkUrl")
        self.WaterMarkWidth = params.get("WaterMarkWidth")
        self.WaterMarkHeight = params.get("WaterMarkHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.ZOrder = params.get("ZOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class McuWaterMarkParams(AbstractModel):
    """The Watermark information.

    """

    def __init__(self):
        r"""
        :param WaterMarkType: The watermark type. The default is 0, which indicates an image watermark.
        :type WaterMarkType: int
        :param WaterMarkImage: The watermark image information. This parameter is required if `WaterMarkType` is 0.
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.McuWaterMarkImage`
        """
        self.WaterMarkType = None
        self.WaterMarkImage = None


    def _deserialize(self, params):
        self.WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self.WaterMarkImage = McuWaterMarkImage()
            self.WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayout(AbstractModel):
    """The custom layout parameters.

    """

    def __init__(self):
        r"""
        :param Top: The Y axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas height.
        :type Top: int
        :param Left: The X axis of the window’s top-left corner. Value range: [0, 1920]. The value cannot be larger than the canvas width.
        :type Left: int
        :param Width: The relative width of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :type Width: int
        :param Height: The relative height of the window. Value range: [0, 1920]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :type Height: int
        :param UserId: The user ID (string) of the anchor whose video is shown in the window. If you do not set this parameter, anchors’ videos will be shown in their room entry sequence.
        :type UserId: str
        :param Alpha: The degree of transparency of the canvas. Value range: [0, 255]. 0 means fully opaque, and 255 means fully transparent.
        :type Alpha: int
        :param RenderMode: 0: Stretch. In this mode, the image is stretched to fill the space available. The whole image is visible after scaling. However, if the original aspect ratio is different from the target, the image may be distorted.

1: Crop (default). In this mode, if the original aspect ratio is different from the target, the image will be cropped according to the target before being stretched to fill the space available. The image will not be distorted.

2: Blank. This mode stretches the image while keeping its original aspect ratio. If the original aspect ratio is different from the target, there may be blank spaces to the top and bottom or to the left and right of the window.

3: Smart stretch. This mode is similar to the crop mode, except that it restricts cropping to 20% of the image’s width or height at most.
        :type RenderMode: int
        :param MediaId: The type of the stream subscribed to.
0: Primary stream (default)
1: Substream
        :type MediaId: int
        :param ImageLayer: The image layer. 0 is the default value and means the bottommost layer.
        :type ImageLayer: int
        :param SubBackgroundImage: The download URL of the background image for a window. The image must be in JPG or PNG format and cannot be larger than 5 MB. If the image’s aspect ratio is different from that of the window, the image will be rendered according to the value of `RenderMode`.
        :type SubBackgroundImage: str
        """
        self.Top = None
        self.Left = None
        self.Width = None
        self.Height = None
        self.UserId = None
        self.Alpha = None
        self.RenderMode = None
        self.MediaId = None
        self.ImageLayer = None
        self.SubBackgroundImage = None


    def _deserialize(self, params):
        self.Top = params.get("Top")
        self.Left = params.get("Left")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.UserId = params.get("UserId")
        self.Alpha = params.get("Alpha")
        self.RenderMode = params.get("RenderMode")
        self.MediaId = params.get("MediaId")
        self.ImageLayer = params.get("ImageLayer")
        self.SubBackgroundImage = params.get("SubBackgroundImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixLayoutParams(AbstractModel):
    """The layout parameters for mixed-stream recording.

    """

    def __init__(self):
        r"""
        :param MixLayoutMode: Layout mode:
1: Floating
2: Screen sharing
3: Grid (default)
4: Custom

Floating: By default, the video of the first anchor (you can also specify an anchor) who enters the room is scaled to fill the screen. When other anchors enter the room, their videos appear smaller and are superimposed over the large video from left to right starting from the bottom of the canvas according to their room entry sequence. If the total number of videos is 17 or less, there will be four windows in each row (4 x 4); if it is greater than 17, there will be five windows in each row (5 x 5). Up to 25 videos can be displayed. A user who publishes only audio will still be displayed in one window.

Screen sharing: The video of a specified anchor occupies a larger part of the canvas on the left side (if you do not specify an anchor, the left window will display the canvas background). The videos of other anchors are smaller and are positioned on the right side. If the total number of videos is 17 or less, the small videos are positioned from top to bottom in up to two columns on the right side, with eight videos per column at most. If there are more than 17 videos, the additional videos are positioned at the bottom of the canvas from left to right. Up to 25 videos can be displayed. A user who publishes only audio will still be displayed in one window.

Grid: The videos of anchors are scaled and positioned automatically according to the total number of anchors in a room. Each video has the same size. Up to 25 videos can be displayed.

Custom: Specify the layout of videos by using the `MixLayoutList` parameter.
        :type MixLayoutMode: int
        :param MixLayoutList: The custom layout details. This parameter is valid if `MixLayoutMode` is set to `4`. Up to 25 videos can be displayed.
        :type MixLayoutList: list of MixLayout
        :param BackGroundColor: The background color, which is a hexadecimal value (starting with "#", followed by the color value) converted from an 8-bit RGB value. For example, the RGB value of orange is `R:255 G:165 B:0`, and its hexadecimal value is `#FFA500`. The default color is black.
        :type BackGroundColor: str
        :param MaxResolutionUserId: The user whose video is displayed in the big window. This parameter is valid if `MixLayoutMode` is set to `1` (floating) or `2` (screen sharing). If it is left empty, the first anchor entering the room is displayed in the big window in the floating mode and the canvas background is displayed in the screen sharing mode.
        :type MaxResolutionUserId: str
        :param MediaId: The stream type.
0: Primary stream (default)
1: Substream (screen sharing stream)
This parameter specifies the type of the stream displayed in the big window. If it appears in `MixLayoutList`, it indicates the type of the stream of a specified user.
        :type MediaId: int
        :param BackgroundImageUrl: The download URL of the background image for the canvas, which must be in JPG or PNG format and cannot be larger than 5 MB.
        :type BackgroundImageUrl: str
        :param PlaceHolderMode: `1` means to use placeholders, and `0` (default) means to not use placeholders. If this parameter is set to `1`, when a user is not publishing video, a placeholder image will be displayed in the window reserved for the user.
        :type PlaceHolderMode: int
        :param BackgroundImageRenderMode: The render mode to use when the aspect ratio of a video is different from that of the window. This parameter is defined the same as `RenderMode` in `MixLayoufList`.
        :type BackgroundImageRenderMode: int
        :param DefaultSubBackgroundImage: The download URL of the default background image for a window. The image must be in JPG or PNG format and cannot be larger than 5 MB. If the image’s aspect ratio is different from that of the window, the image will be rendered according to the value of `RenderMode`.
        :type DefaultSubBackgroundImage: str
        :param WaterMarkList: The watermark layout. Up to 25 watermarks are supported.
        :type WaterMarkList: list of WaterMark
        """
        self.MixLayoutMode = None
        self.MixLayoutList = None
        self.BackGroundColor = None
        self.MaxResolutionUserId = None
        self.MediaId = None
        self.BackgroundImageUrl = None
        self.PlaceHolderMode = None
        self.BackgroundImageRenderMode = None
        self.DefaultSubBackgroundImage = None
        self.WaterMarkList = None


    def _deserialize(self, params):
        self.MixLayoutMode = params.get("MixLayoutMode")
        if params.get("MixLayoutList") is not None:
            self.MixLayoutList = []
            for item in params.get("MixLayoutList"):
                obj = MixLayout()
                obj._deserialize(item)
                self.MixLayoutList.append(obj)
        self.BackGroundColor = params.get("BackGroundColor")
        self.MaxResolutionUserId = params.get("MaxResolutionUserId")
        self.MediaId = params.get("MediaId")
        self.BackgroundImageUrl = params.get("BackgroundImageUrl")
        self.PlaceHolderMode = params.get("PlaceHolderMode")
        self.BackgroundImageRenderMode = params.get("BackgroundImageRenderMode")
        self.DefaultSubBackgroundImage = params.get("DefaultSubBackgroundImage")
        if params.get("WaterMarkList") is not None:
            self.WaterMarkList = []
            for item in params.get("WaterMarkList"):
                obj = WaterMark()
                obj._deserialize(item)
                self.WaterMarkList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixTranscodeParams(AbstractModel):
    """The audio and video parameters for recording.

    """

    def __init__(self):
        r"""
        :param VideoParams: The video transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.VideoParams`
        :param AudioParams: The audio transcoding parameters for recording. If you set this parameter, you must specify all its fields. If you do not set it, the default will be used.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.AudioParams`
        """
        self.VideoParams = None
        self.AudioParams = None


    def _deserialize(self, params):
        if params.get("VideoParams") is not None:
            self.VideoParams = VideoParams()
            self.VideoParams._deserialize(params.get("VideoParams"))
        if params.get("AudioParams") is not None:
            self.AudioParams = AudioParams()
            self.AudioParams._deserialize(params.get("AudioParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MixUserInfo(AbstractModel):
    """The user information.

    """

    def __init__(self):
        r"""
        :param UserId: User ID.
        :type UserId: str
        :param RoomId: If a dynamic layout is used, the value of this parameter should be the ID of the main room. If a custom layout is used, the value of this parameter should be the same as the room ID in `MixLayoutList`.
        :type RoomId: str
        :param RoomIdType: The type of the `RoomId` parameter. 0: integer; 1: string.
        :type RoomIdType: int
        """
        self.UserId = None
        self.RoomId = None
        self.RoomIdType = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RoomId = params.get("RoomId")
        self.RoomIdType = params.get("RoomIdType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingRequest(AbstractModel):
    """ModifyCloudRecording request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The `SDKAppID` of the room whose streams are recorded.
        :type SdkAppId: int
        :param TaskId: The unique ID of the recording task, which is returned after recording starts successfully.
        :type TaskId: str
        :param MixLayoutParams: The new stream mixing layout to use.
        :type MixLayoutParams: :class:`tencentcloud.trtc.v20190722.models.MixLayoutParams`
        :param SubscribeStreamUserIds: The allowlist/blocklist for stream subscription.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        """
        self.SdkAppId = None
        self.TaskId = None
        self.MixLayoutParams = None
        self.SubscribeStreamUserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        if params.get("MixLayoutParams") is not None:
            self.MixLayoutParams = MixLayoutParams()
            self.MixLayoutParams._deserialize(params.get("MixLayoutParams"))
        if params.get("SubscribeStreamUserIds") is not None:
            self.SubscribeStreamUserIds = SubscribeStreamUserIds()
            self.SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudRecordingResponse(AbstractModel):
    """ModifyCloudRecording response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID assigned by the recording service, which uniquely identifies a recording process and becomes invalid after a recording task ends.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RecordParams(AbstractModel):
    """The on-cloud recording parameters.

    """

    def __init__(self):
        r"""
        :param RecordMode: The recording mode.
1: Single-stream recording. Records the audio and video of each subscribed user (`UserId`) in a room and saves the recording files to the cloud.
2: Mixed-stream recording. Mixes the audios and videos of subscribed users (`UserId`) in a room, records the mixed stream, and saves the recording files to the cloud.
        :type RecordMode: int
        :param MaxIdleTime: The time period (seconds) to wait after there are no anchors in a room to stop recording automatically. The value cannot be smaller than 5 or larger than 86400 (24 hours). Default value: 30.
        :type MaxIdleTime: int
        :param StreamType: The media type of the streams to record.
0: Audio and video streams (default)
1: Audio streams only
2: Video streams only
        :type StreamType: int
        :param SubscribeStreamUserIds: The allowlist/blocklist for stream subscription.
        :type SubscribeStreamUserIds: :class:`tencentcloud.trtc.v20190722.models.SubscribeStreamUserIds`
        :param OutputFormat: The output format. 0 (default): HLS; 1: HLS + MP4 (recorded in HLS and converted to MP4). This parameter is invalid if you save recording files to VOD. To specify the format of files saved to VOD, use `MediaType` of `TencentVod`.
        :type OutputFormat: int
        :param AvMerge: Whether to merge the audio and video of a user in the single-stream recording mode. 0 (default): Do not mix the audio and video; 1: Mix the audio and video into one TS file. You don’t need to specify this parameter for mixed-stream recording, which merges audios and videos by default.
        :type AvMerge: int
        """
        self.RecordMode = None
        self.MaxIdleTime = None
        self.StreamType = None
        self.SubscribeStreamUserIds = None
        self.OutputFormat = None
        self.AvMerge = None


    def _deserialize(self, params):
        self.RecordMode = params.get("RecordMode")
        self.MaxIdleTime = params.get("MaxIdleTime")
        self.StreamType = params.get("StreamType")
        if params.get("SubscribeStreamUserIds") is not None:
            self.SubscribeStreamUserIds = SubscribeStreamUserIds()
            self.SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self.OutputFormat = params.get("OutputFormat")
        self.AvMerge = params.get("AvMerge")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdRequest(AbstractModel):
    """RemoveUserByStrRoomId request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC
        :type SdkAppId: int
        :param RoomId: Room ID
        :type RoomId: str
        :param UserIds: List of up to 10 users to be removed
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserByStrRoomIdResponse(AbstractModel):
    """RemoveUserByStrRoomId response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserRequest(AbstractModel):
    """RemoveUser request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: `SDKAppId` of TRTC.
        :type SdkAppId: int
        :param RoomId: Room number.
        :type RoomId: int
        :param UserIds: List of up to 10 users to be removed.
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserResponse(AbstractModel):
    """RemoveUser response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SingleSubscribeParams(AbstractModel):
    """The information of a single stream relayed.

    """

    def __init__(self):
        r"""
        :param UserMediaStream: The stream information.
        :type UserMediaStream: :class:`tencentcloud.trtc.v20190722.models.UserMediaStream`
        """
        self.UserMediaStream = None


    def _deserialize(self, params):
        if params.get("UserMediaStream") is not None:
            self.UserMediaStream = UserMediaStream()
            self.UserMediaStream._deserialize(params.get("UserMediaStream"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishCdnStreamRequest(AbstractModel):
    """StartPublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param RoomId: The ID of the room whose streams are relayed (the main room).
        :type RoomId: str
        :param RoomIdType: The type of the `RoomId` parameter, which must be the same as the ID type of the room whose streams are relayed. 0: integer; 1: string.
        :type RoomIdType: int
        :param AgentParams: The information of the relaying robot in the room.
        :type AgentParams: :class:`tencentcloud.trtc.v20190722.models.AgentParams`
        :param WithTranscoding: Whether to transcode the streams. 0: No; 1: Yes.
        :type WithTranscoding: int
        :param AudioParams: The audio encoding parameters for relaying.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param VideoParams: The video encoding parameters for relaying. If you do not pass this parameter, only audio will be relayed.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param SingleSubscribeParams: The information of a single stream relayed. When you relay a single stream, set `WithTranscoding` to 0.
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param PublishCdnParams: The CDN information.
        :type PublishCdnParams: list of McuPublishCdnParam
        :param SeiParams: The stream mixing SEI parameters.
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param FeedBackRoomParams: The information of the room to which streams are relayed.
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        """
        self.SdkAppId = None
        self.RoomId = None
        self.RoomIdType = None
        self.AgentParams = None
        self.WithTranscoding = None
        self.AudioParams = None
        self.VideoParams = None
        self.SingleSubscribeParams = None
        self.PublishCdnParams = None
        self.SeiParams = None
        self.FeedBackRoomParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.RoomIdType = params.get("RoomIdType")
        if params.get("AgentParams") is not None:
            self.AgentParams = AgentParams()
            self.AgentParams._deserialize(params.get("AgentParams"))
        self.WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self.AudioParams = McuAudioParams()
            self.AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self.VideoParams = McuVideoParams()
            self.VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self.SingleSubscribeParams = SingleSubscribeParams()
            self.SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self.PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self.PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self.SeiParams = McuSeiParams()
            self.SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self.FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self.FeedBackRoomParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartPublishCdnStreamResponse(AbstractModel):
    """StartPublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID, which is generated by the Tencent Cloud server. You need to pass in the task ID when making a request to update or stop a relaying task.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StopPublishCdnStreamRequest(AbstractModel):
    """StopPublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param TaskId: The task ID.
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopPublishCdnStreamResponse(AbstractModel):
    """StopPublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StorageFile(AbstractModel):
    """The information of the recording files, which is returned by the `DescribeCloudRecording` API.

    """

    def __init__(self):
        r"""
        :param UserId: The user whose stream is recorded into the file. In the mixed-stream recording mode, this parameter will be empty.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type UserId: str
        :param FileName: The filename.
        :type FileName: str
        :param TrackType: The type of the media recorded.
video
audio
audio_video
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TrackType: str
        :param BeginTimeStamp: The start time (Unix timestamp) of the recording file.
        :type BeginTimeStamp: int
        """
        self.UserId = None
        self.FileName = None
        self.TrackType = None
        self.BeginTimeStamp = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.FileName = params.get("FileName")
        self.TrackType = params.get("TrackType")
        self.BeginTimeStamp = params.get("BeginTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageParams(AbstractModel):
    """The storage parameters.

    """

    def __init__(self):
        r"""
        :param CloudStorage: The account information for third-party cloud storage. This parameter is not available currently. Please use `CloudVod` instead to save files to Tencent Cloud VOD.
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param CloudVod: The account information for saving files to Tencent Cloud VOD. This parameter is required. Currently, you can only save files to Tencent Cloud VOD.
        :type CloudVod: :class:`tencentcloud.trtc.v20190722.models.CloudVod`
        """
        self.CloudStorage = None
        self.CloudVod = None


    def _deserialize(self, params):
        if params.get("CloudStorage") is not None:
            self.CloudStorage = CloudStorage()
            self.CloudStorage._deserialize(params.get("CloudStorage"))
        if params.get("CloudVod") is not None:
            self.CloudVod = CloudVod()
            self.CloudVod._deserialize(params.get("CloudVod"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribeStreamUserIds(AbstractModel):
    """The subscription allowlist/blocklist. You cannot specify an allowlist and a blocklist for audio/video subscription at the same time. The maximum number of streams one can receive at the same time is 25. When streams are mixed, up to 24 videos are supported. You can use `.*$` to specify user IDs with the same prefix, but make sure there aren’t users whose IDs contain ".*$" and are exactly the same as the prefix you pass in. If there are, TRTC will only allow or block those users.

    """

    def __init__(self):
        r"""
        :param SubscribeAudioUserIds: The allowlist for audio subscription. For example, `["1", "2", "3"]` means to only subscribe to the audios of users 1, 2, and 3, and ["1.*$"] means to only subscribe to the audios of users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :type SubscribeAudioUserIds: list of str
        :param UnSubscribeAudioUserIds: The blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audios of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to users whose ID prefix is `1`. If this parameter is left empty, the audios of all anchors in the room will be received. The array can contain at most 32 elements.
        :type UnSubscribeAudioUserIds: list of str
        :param SubscribeVideoUserIds: The allowlist for video subscription. For example, `["1", "2", "3"]` means to only subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to only subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :type SubscribeVideoUserIds: list of str
        :param UnSubscribeVideoUserIds: The blocklist for video subscription. For example, `["1", "2", "3"]` means to not subscribe to the videos of users 1, 2, and 3, and `["1.*$"]` means to not subscribe to the videos of users whose ID prefix is `1`. If this parameter is left empty, the videos of all anchors in the room will be received. The array can contain at most 32 elements.
        :type UnSubscribeVideoUserIds: list of str
        """
        self.SubscribeAudioUserIds = None
        self.UnSubscribeAudioUserIds = None
        self.SubscribeVideoUserIds = None
        self.UnSubscribeVideoUserIds = None


    def _deserialize(self, params):
        self.SubscribeAudioUserIds = params.get("SubscribeAudioUserIds")
        self.UnSubscribeAudioUserIds = params.get("UnSubscribeAudioUserIds")
        self.SubscribeVideoUserIds = params.get("SubscribeVideoUserIds")
        self.UnSubscribeVideoUserIds = params.get("UnSubscribeVideoUserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TencentVod(AbstractModel):
    """The Tencent Cloud VOD parameters.

    """

    def __init__(self):
        r"""
        :param Procedure: The operation to perform on the media uploaded. The value of this parameter is the name of a task flow template. You can create a custom task flow template in Tencent Cloud VOD.
        :type Procedure: str
        :param ExpireTime: The expiration time of the media file, which is a time period (seconds) from the current time. For example, `86400` means to save the media file for one day. To save the file permanently, set this parameter to `0`.
        :type ExpireTime: int
        :param StorageRegion: The storage region. Set this parameter if you have special requirements on the storage region.
        :type StorageRegion: str
        :param ClassId: The category ID, which is returned after you create a category by calling an API. You can use categories to manage media files.
The default value is `0`, which means others.
        :type ClassId: int
        :param SubAppId: The VOD subapplication ID. If you need to access a resource in a subapplication, set this parameter to the subapplication ID; otherwise, leave it empty.
        :type SubAppId: int
        :param SessionContext: The task flow context, which is passed through after the task is completed.
        :type SessionContext: str
        :param SourceContext: The upload context, which is passed through after upload is completed.
        :type SourceContext: str
        :param MediaType: The format of recording files saved to VOD. 0 (default): MP4; 1: HLS.
        :type MediaType: int
        """
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SubAppId = None
        self.SessionContext = None
        self.SourceContext = None
        self.MediaType = None


    def _deserialize(self, params):
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SubAppId = params.get("SubAppId")
        self.SessionContext = params.get("SessionContext")
        self.SourceContext = params.get("SourceContext")
        self.MediaType = params.get("MediaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePublishCdnStreamRequest(AbstractModel):
    """UpdatePublishCdnStream request structure.

    """

    def __init__(self):
        r"""
        :param SdkAppId: The [SDKAppID](https://intl.cloud.tencent.com/document/product/647/37714) of the TRTC room whose streams are relayed.
        :type SdkAppId: int
        :param TaskId: The task ID.
        :type TaskId: str
        :param SequenceNumber: The sequence of a request. This parameter ensures the requests to change the parameters of the same relaying task are in the correct order. It increases each time a new request is made.
        :type SequenceNumber: int
        :param WithTranscoding: Whether to transcode the streams. 0: No; 1: Yes.
        :type WithTranscoding: int
        :param AudioParams: Pass this parameter to change the users whose audios are mixed. If you do not pass this parameter, no changes will be made.
        :type AudioParams: :class:`tencentcloud.trtc.v20190722.models.McuAudioParams`
        :param VideoParams: Pass this parameter to change video parameters other than the codec, including the video layout, background image, background color, and watermark information. This parameter is valid only if streams are transcoded. If you do not pass it, no changes will be made.
        :type VideoParams: :class:`tencentcloud.trtc.v20190722.models.McuVideoParams`
        :param SingleSubscribeParams: Pass this parameter to change the single stream that is relayed. This parameter is valid only if streams are not transcoded. If you do not pass this parameter, no changes will be made.
        :type SingleSubscribeParams: :class:`tencentcloud.trtc.v20190722.models.SingleSubscribeParams`
        :param PublishCdnParams: Pass this parameter to change the CDNs to relay to. If you do not pass this parameter, no changes will be made.
        :type PublishCdnParams: list of McuPublishCdnParam
        :param SeiParams: The stream mixing SEI parameters.
        :type SeiParams: :class:`tencentcloud.trtc.v20190722.models.McuSeiParams`
        :param FeedBackRoomParams: The information of the room to which streams are relayed.
        :type FeedBackRoomParams: list of McuFeedBackRoomParams
        """
        self.SdkAppId = None
        self.TaskId = None
        self.SequenceNumber = None
        self.WithTranscoding = None
        self.AudioParams = None
        self.VideoParams = None
        self.SingleSubscribeParams = None
        self.PublishCdnParams = None
        self.SeiParams = None
        self.FeedBackRoomParams = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")
        self.SequenceNumber = params.get("SequenceNumber")
        self.WithTranscoding = params.get("WithTranscoding")
        if params.get("AudioParams") is not None:
            self.AudioParams = McuAudioParams()
            self.AudioParams._deserialize(params.get("AudioParams"))
        if params.get("VideoParams") is not None:
            self.VideoParams = McuVideoParams()
            self.VideoParams._deserialize(params.get("VideoParams"))
        if params.get("SingleSubscribeParams") is not None:
            self.SingleSubscribeParams = SingleSubscribeParams()
            self.SingleSubscribeParams._deserialize(params.get("SingleSubscribeParams"))
        if params.get("PublishCdnParams") is not None:
            self.PublishCdnParams = []
            for item in params.get("PublishCdnParams"):
                obj = McuPublishCdnParam()
                obj._deserialize(item)
                self.PublishCdnParams.append(obj)
        if params.get("SeiParams") is not None:
            self.SeiParams = McuSeiParams()
            self.SeiParams._deserialize(params.get("SeiParams"))
        if params.get("FeedBackRoomParams") is not None:
            self.FeedBackRoomParams = []
            for item in params.get("FeedBackRoomParams"):
                obj = McuFeedBackRoomParams()
                obj._deserialize(item)
                self.FeedBackRoomParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePublishCdnStreamResponse(AbstractModel):
    """UpdatePublishCdnStream response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UserMediaStream(AbstractModel):
    """The stream information.

    """

    def __init__(self):
        r"""
        :param UserInfo: The user information.
        :type UserInfo: :class:`tencentcloud.trtc.v20190722.models.MixUserInfo`
        :param StreamType: The stream type. 0: Camera; 1: Screen sharing. If you do not pass this parameter, 0 will be used.
        :type StreamType: int
        """
        self.UserInfo = None
        self.StreamType = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = MixUserInfo()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.StreamType = params.get("StreamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoEncode(AbstractModel):
    """The video encoding parameters.

    """

    def __init__(self):
        r"""
        :param Width: The width of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1920].
        :type Width: int
        :param Height: The height of the output stream (pixels). This parameter is required if audio and video are relayed. Value range: [0, 1080].
        :type Height: int
        :param Fps: The frame rate (fps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 60].
        :type Fps: int
        :param BitRate: The bitrate (Kbps) of the output stream. This parameter is required if audio and video are relayed. Value range: [0, 10000].
        :type BitRate: int
        :param Gop: The GOP (seconds) of the output stream. This parameter is required if audio and video are relayed. Value range: [1, 5].
        :type Gop: int
        """
        self.Width = None
        self.Height = None
        self.Fps = None
        self.BitRate = None
        self.Gop = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.BitRate = params.get("BitRate")
        self.Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoParams(AbstractModel):
    """The video transcoding parameters for recording.

    """

    def __init__(self):
        r"""
        :param Width: The video width in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `360`.
        :type Width: int
        :param Height: The video height in pixels. The value of this parameter cannot be larger than 1920, and the result of multiplying `Width` and `Height` cannot exceed 1920 x 1080. The default value is `640`.
        :type Height: int
        :param Fps: The video frame rate. Value range: [1, 60]. Default: 15.
        :type Fps: int
        :param BitRate: The video bitrate (bps). Value range: [64000, 8192000]. Default: 550000.
        :type BitRate: int
        :param Gop: The keyframe interval (seconds). Default value: 10.
        :type Gop: int
        """
        self.Width = None
        self.Height = None
        self.Fps = None
        self.BitRate = None
        self.Gop = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.BitRate = params.get("BitRate")
        self.Gop = params.get("Gop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMark(AbstractModel):
    """The watermark layout.

    """

    def __init__(self):
        r"""
        :param WaterMarkType: The watermark type. 0 (default): image; 1: text (not supported yet).
        :type WaterMarkType: int
        :param WaterMarkImage: The information of watermark images. This parameter is required if the watermark type is image.
        :type WaterMarkImage: :class:`tencentcloud.trtc.v20190722.models.WaterMarkImage`
        """
        self.WaterMarkType = None
        self.WaterMarkImage = None


    def _deserialize(self, params):
        self.WaterMarkType = params.get("WaterMarkType")
        if params.get("WaterMarkImage") is not None:
            self.WaterMarkImage = WaterMarkImage()
            self.WaterMarkImage._deserialize(params.get("WaterMarkImage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterMarkImage(AbstractModel):
    """The information of watermark images.

    """

    def __init__(self):
        r"""
        :param WaterMarkUrl: The download URLs of the watermark images, which must be in JPG or PNG format and cannot be larger than 5 MB.
        :type WaterMarkUrl: str
        :param Top: The Y axis of the image's top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas height.
        :type Top: int
        :param Left: The X axis of the image’s top-left corner. Value range: [0, 2560]. The value cannot be larger than the canvas width.
        :type Left: int
        :param Width: The relative width of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Left` cannot exceed the canvas width.
        :type Width: int
        :param Height: The relative height of the image. Value range: [0, 2560]. The sum of the values of this parameter and `Top` cannot exceed the canvas height.
        :type Height: int
        """
        self.WaterMarkUrl = None
        self.Top = None
        self.Left = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WaterMarkUrl = params.get("WaterMarkUrl")
        self.Top = params.get("Top")
        self.Left = params.get("Left")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        