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
        :param FileNamePrefix: The bucket to save data, which is an array of strings that can contain letters (a-z and A-Z) and numbers (0-9). For example, if the value of this parameter is `["prefix1", "prefix2"]`, the recording file `xxx.m3u8` will be saved as `prefix1/prefix2/TaskId/xxx.m3u8`.
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
        :param UserId: The [user ID](https://intl.cloud.tencent.com/document/product/647/37714) of the recording robot in the TRTC room, which cannot be the same as a user ID already in use. We recommend you include this user ID in the room ID.
        :type UserId: str
        :param UserSig: The signature (similar to login password) required for the recording robot to enter the room. For information on how to calculate the signature, see [What is UserSig?](https://intl.cloud.tencent.com/document/product/647/38104). |
        :type UserSig: str
        :param RecordParams: The on-cloud recording parameters.
        :type RecordParams: :class:`tencentcloud.trtc.v20190722.models.RecordParams`
        :param StorageParams: The cloud storage parameters.
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
1: Single-stream recording. Records the audio and video of each subscribed user (`UserId`) in a room and saves the recording files (M3U8/TS) to the cloud.
2: Mixed-stream recording. Mixes the audios and videos of subscribed users (`UserId`) in a room, records the mixed stream, and saves the recording files (M3U8/TS) to the cloud.
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
        :param OutputFormat: The format of recording files. 0 (default): HLS; 1: HLS + MP4 (recorded in HLS and converted to MP4).
        :type OutputFormat: int
        """
        self.RecordMode = None
        self.MaxIdleTime = None
        self.StreamType = None
        self.SubscribeStreamUserIds = None
        self.OutputFormat = None


    def _deserialize(self, params):
        self.RecordMode = params.get("RecordMode")
        self.MaxIdleTime = params.get("MaxIdleTime")
        self.StreamType = params.get("StreamType")
        if params.get("SubscribeStreamUserIds") is not None:
            self.SubscribeStreamUserIds = SubscribeStreamUserIds()
            self.SubscribeStreamUserIds._deserialize(params.get("SubscribeStreamUserIds"))
        self.OutputFormat = params.get("OutputFormat")
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
        :param CloudStorage: The cloud storage information.
        :type CloudStorage: :class:`tencentcloud.trtc.v20190722.models.CloudStorage`
        :param CloudVod: The VOD information.
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
    """The allowlist/blocklist for stream subscription. You cannot set both an allowlist and blocklist for audio or video subscription. Up to 25 streams can be subscribed to at the same time. In the mixed-stream recording mode, up to 24 videos can be displayed.

    """

    def __init__(self):
        r"""
        :param SubscribeAudioUserIds: The allowlist for audio subscription. For example, `["1", "2", "3"]` means to subscribe to the audios of users 1, 2, and 3. If this parameter is left empty, the audios of all anchors (max 32) in the room will be received.
        :type SubscribeAudioUserIds: list of str
        :param UnSubscribeAudioUserIds: The blocklist for audio subscription. For example, `["1", "2", "3"]` means to not subscribe to the audios of users 1, 2, and 3. If this parameter is left empty, the audios of all anchors (max 32) in the room will be received.
        :type UnSubscribeAudioUserIds: list of str
        :param SubscribeVideoUserIds: The allowlist for video subscription. For example, `["1", "2", "3"]` means to subscribe to the videos of users 1, 2, and 3. If this parameter is left empty, the videos of all anchors (max 32) in the room will be received.
        :type SubscribeVideoUserIds: list of str
        :param UnSubscribeVideoUserIds: The blocklist for video subscription. For example, `["1", "2", "3"]` means to not subscribe to the videos of users 1, 2, and 3. If this parameter is left empty, the videos of all anchors (max 32) in the room will be received.
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
        """
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SubAppId = None
        self.SessionContext = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SubAppId = params.get("SubAppId")
        self.SessionContext = params.get("SessionContext")
        self.SourceContext = params.get("SourceContext")
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
        