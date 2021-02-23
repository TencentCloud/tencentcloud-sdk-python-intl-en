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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.trtc.v20190722 import models


class TrtcClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'trtc.tencentcloudapi.com'
    _service = 'trtc'


    def CreateTroubleInfo(self, request):
        """This API is used to create exception information.

        :param request: Request instance for CreateTroubleInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.CreateTroubleInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CreateTroubleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTroubleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTroubleInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalEvent(self, request):
        """This API is used to query exception occurrences under a specified `SDKAppID` and return the exception IDs and possible causes. It queries data in last 15 days, and the query period is up to 1 hour, which can start and end on different days. For more information about exceptions, please see the exception event ID mapping table: https://intl.cloud.tencent.com/document/product/647/37906.

        :param request: Request instance for DescribeAbnormalEvent.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeAbnormalEventRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeAbnormalEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAbnormalEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCallDetail(self, request):
        """This API is used to query the user list and call quality data of a specified time range in the last 14 days. When `DataType` is not null, data of up to 6 users during a period of up to 1 hour can be queried each time, and the period can start on one day and end on the next. When `DataType` and `UserIds` are null, 6 users are queried by default, and data of up to 100 users can be displayed on each page (`PageSize` set to 100 or lower). This API is used to query call quality and is not recommended for billing.
        Note: you are not advised to use the API for the processing of real-time business logic.

        :param request: Request instance for DescribeCallDetail.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCallDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCallDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDetailEvent(self, request):
        """This API is used to query a user’s activity details such as room entry/exit and video enablement/disablement during a call. It can query data for the last 14 days.

        :param request: Request instance for DescribeDetailEvent.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeDetailEventRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeDetailEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDetailEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDetailEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHistoryScale(self, request):
        """This API is used to query the daily numbers of rooms and users under a specified `SDKAppID`. It can query data once per minute for the last 14 days. If a day has not ended, the numbers of rooms and users on the day cannot be queried.

        :param request: Request instance for DescribeHistoryScale.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeHistoryScaleRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeHistoryScaleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHistoryScale", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHistoryScaleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealtimeNetwork(self, request):
        """This API is used to query the network conditions of an `SDKAppID`, including upstream and downstream packet loss, in the last 24 hours on a per-minute basis. The query period must be 1-60 minutes.

        :param request: Request instance for DescribeRealtimeNetwork.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeNetworkRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeNetworkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeNetwork", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeNetworkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealtimeQuality(self, request):
        """This API is used to query the quality metrics of an `SDKAppID` in the last 24 hours on a per-minute basis, including room entry success rate, instant playback rate of the first frame, and audio/video lag rate. The query period must be 1-60 minutes.

        :param request: Request instance for DescribeRealtimeQuality.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeQualityRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeQualityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeQuality", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeQualityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealtimeScale(self, request):
        """This API is used to query the scale of an `SDKAppID` in the last 24 hours on a per-minute basis. The query period must be 1-60 minutes.

        :param request: Request instance for DescribeRealtimeScale.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeScaleRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeScaleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeScale", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeScaleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRoomInformation(self, request):
        """This API is used to query the room list of an `SDKAppID` in the last 14 days. It returns 10 calls by default and can return up to 100 calls per query.
        Note: you are not advised to use the API for the processing of real-time business logic.

        :param request: Request instance for DescribeRoomInformation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInformationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRoomInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoomInformationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserInformation(self, request):
        """This API is used to query the user list of a specified time range (up to 4 hours) in the last 14 days. Data of 6 users is displayed on each page by default, and data of up to 100 users can be displayed on each page (`PageSize` set to 100 or lower).
        Note: you are not advised to use the API for the processing of real-time business logic.

        :param request: Request instance for DescribeUserInformation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeUserInformationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeUserInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserInformationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DismissRoom(self, request):
        """This API is used to remove all users from a room and dismiss the room. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above.

        :param request: Request instance for DismissRoom.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DismissRoom", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DismissRoomResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DismissRoomByStrRoomId(self, request):
        """This API is used to remove all users from a room and close the room. It works on all platforms. For Android, iOS, Windows, and macOS, you need to update the TRTC SDK to version 6.6 or above.

        :param request: Request instance for DismissRoomByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DismissRoomByStrRoomId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DismissRoomByStrRoomIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveUser(self, request):
        """This API is used to remove a user from a room. It is applicable to scenarios where the anchor, room owner, or admin wants to kick out a user. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above.

        :param request: Request instance for RemoveUser.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveUserByStrRoomId(self, request):
        """This API is used to remove a user from a room. It allows the anchor, room owner, or admin to kick out a user, and works on all platforms. For Android, iOS, Windows, and macOS, you need to update the TRTC SDK to version 6.6 or above.

        :param request: Request instance for RemoveUserByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveUserByStrRoomId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserByStrRoomIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartMCUMixTranscode(self, request):
        """This API is used to enable On-Cloud MixTranscoding and specify the position of each channel of image in stream mixing.

        There may be multiple channels of audio/video streams in a TRTC room. You can call this API to request the Tencent Cloud server to combine multiple channels of video images and audio into one channel and specify the position of each image so as to produce just one channel of audio/video stream for recording and live streaming. The mixing stops automatically after a room is destroyed.

        You can use this API to perform the following operations:
        - Set image and audio quality parameters of the final live stream, including video resolution, video bitrate, video frame rate, and audio quality.
        - Set the layout, i.e., the position of each channel of image. You only need to set it once when enabling On-Cloud MixTranscoding, and the layout engine will automatically arrange images as configured.
        - Set the names of recording files for future playback.
        - Set the stream ID for CDN live streaming.

        Currently, On-Cloud MixTranscoding supports the following layout templates:
        - Floating: the entire screen is covered by the video image of the first user who enters the room, and the images of other users are displayed as small images in horizontal rows in the bottom-left corner in room entry sequence. The screen can accommodate up to 4 rows of 4 small images, which float over the big image. Up to 1 big image and 15 small images can be displayed. A user sending audio only will still occupy an image spot.
        - Grid: the images of the users split the entire screen evenly. The more the users, the smaller the image dimensions. Up to 16 images can be displayed. A user sending audio only will still occupy an image spot.
        - Screen sharing: this is designed for video conferencing and online education. The shared screen (image of the anchor) is always displayed as the big image, which occupies the left half of the screen, and the images of other users occupy the right half in up to 2 columns of up to 8 small images each. Up to 1 big image and 15 small images can be displayed. If the aspect ratio of upstream images do not match that of output images, the big image on the left will be scaled and displayed in whole, while the small images on the right will be cropped.
        - Picture-in-picture: this is designed for mixing the dual-channel (small and big) image or big image with the audio of other users. The small images float over the big image. You can specify which users to be displayed as the big/small images as well as the positions of the small images. Up to 2 images are supported.
        - Custom: this is designed for cases where you want to specify the image positions of users in the mixed stream or preset image positions. If users are assigned to preset positions, the layout engine will reserve the positions for the users; if not, users will occupy the positions in room entry sequence. Once all preset positions are occupied, TRTC will stop mixing the audio and images of other users. If the placeholding feature is enabled for a custom template (`PlaceHolderMode` in `LayoutParams` set to 1), but a user for whom a place is reserved is not sending video data, the position will show the corresponding placeholder image (`PlaceImageId`).

        Note: only applications created on and after January 9, 2020 can call this API directly. Applications created before use the stream mixing service of LVB by default. If you want to switch to MCU On-Cloud MixTranscoding, please [submit a ticket](https://console.cloud.tencent.com/workorder/category).

        :param request: Request instance for StartMCUMixTranscode.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMCUMixTranscode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMCUMixTranscodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartMCUMixTranscodeByStrRoomId(self, request):
        """This API is used to enable On-Cloud MixTranscoding and specify the position of each channel of image in stream mixing.

        There may be multiple channels of audio/video streams in a TRTC room. You can call this API to request the Tencent Cloud server to mix multiple channels of video images and audio into one channel and specify the position of each image so as to produce only one channel of audio/video stream for recording and live streaming.

        You can use this API to perform the following operations:
        - Set image and audio quality parameters of the mixed stream, including video resolution, bitrate, frame rate, and audio quality.
        - Set the layout, i.e., the position of each channel of image. You only need to set it once when enabling On-Cloud MixTranscoding, and the layout engine will automatically arrange images as configured.
        - Set the names of recording files for future playback.
        - Set the stream ID for CDN live streaming.

        Currently, On-Cloud MixTranscoding supports the following layout templates:
        - Floating: the entire screen is covered by the video image of the first user who enters the room, and the images of other users are displayed as small images in horizontal rows in the bottom-left corner in room entry sequence. The screen can accommodate up to 4 rows of 4 small images, which float over the big image. Up to 1 big image and 15 small images can be displayed. A user sending audio only will still occupy an image spot.
        - Grid: the images of all users split the screen evenly. The more the users, the smaller the image dimensions. Up to 16 images can be displayed. A user sending audio only will still occupy an image spot.
        - Screen sharing: this template is designed for video conferencing and online classes. The shared screen (or camera image of the anchor) is always displayed as the big image, which occupies the left half of the screen, and the images of other users occupy the right half in up to 2 columns of a maximum of 8 small images each. Up to 1 big image and 15 small images can be displayed. If the aspect ratio of upstream images does not match that of output images, the big image on the left will be scaled and displayed in whole, while the small images on the right will be cropped.
        - Picture-in-picture: this template mixes the big and small images or big image of a user with the audio of other users. The small image floats over the big image. You can specify the user whose big and small images are displayed and the position of the small image.
        - Custom: you can use custom templates to specify the image positions of users in mixed streams or preset image positions. If users are assigned to preset positions, the layout engine will reserve the positions for the users; if not, users will occupy the positions in room entry sequence. Once all preset positions are occupied, TRTC will stop mixing the audio and images of other users. If the placeholding feature is enabled for a custom template (`PlaceHolderMode` in `LayoutParams` is set to 1), but a user for whom a place is reserved is not sending video data, the position will show the corresponding placeholder image (`PlaceImageId`).

        Note: only applications created on and after January 9, 2020 can call this API directly. Those created before use the stream mixing service of CSS by default. If you want to switch to MCU On-Cloud MixTranscoding, please [submit a ticket](https://console.cloud.tencent.com/workorder/category).

        :param request: Request instance for StartMCUMixTranscodeByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartMCUMixTranscodeByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMCUMixTranscodeByStrRoomId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMCUMixTranscodeByStrRoomIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopMCUMixTranscode(self, request):
        """This API is used to end On-Cloud MixTranscoding.

        :param request: Request instance for StopMCUMixTranscode.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMCUMixTranscode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMCUMixTranscodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopMCUMixTranscodeByStrRoomId(self, request):
        """This API is used to stop On-Cloud MixTranscoding.

        :param request: Request instance for StopMCUMixTranscodeByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopMCUMixTranscodeByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMCUMixTranscodeByStrRoomId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMCUMixTranscodeByStrRoomIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)