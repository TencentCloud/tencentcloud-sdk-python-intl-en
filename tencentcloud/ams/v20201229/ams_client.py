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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.ams.v20201229 import models


class AmsClient(AbstractClient):
    _apiVersion = '2020-12-29'
    _endpoint = 'ams.tencentcloudapi.com'
    _service = 'ams'


    def CancelTask(self, request):
        """This API is used to cancel a moderation task. If it returns `RequestId`, the task has been canceled successfully.<br>Default API request rate limit: **20 requests/sec**.

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAudioModerationTask(self, request):
        """This API is used to submit audio content (such as an audio file or stream URL) for smart moderation. Before using it, you need to log in to the console with the Tencent Cloud root account to [activate AMS](https://console.cloud.tencent.com/cms) and adjust the business configuration. <br>

        ### API use instructions
        - Go to [CMS console - AMS](https://console.cloud.tencent.com/cms) to activate AMS. For initial activation, you can enjoy **10 hours** of free call of the API within one month.
        - Default limit of API request rate: **20 requests/s**. When this limit is exceeded, requests will automatically join the queue of requests pending moderation for async moderation tasks (audio on demand), while an error will be reported for sync moderation tasks (audio live streaming).
        - Default limit of concurrent moderation tasks: 10 for audio on demand and 100 for audio live streaming. When this limit is exceeded, requests will automatically queue up for async moderation tasks (audio on demand), while an error will be reported for sync moderation tasks (audio live streaming).

        ### API feature description
        - This API can detect audio streams or files for non-compliant content.
        - You can set the callback address (Callback) to get the detection result (for moderation tasks in progress, the maximum callback time is the configured **segment length + 2s**). You can also call the API for querying the audio detection result to actively poll the detection result.
        - This API can recognize various types of non-compliant content, including vulgarity, abuse, porn, and advertising.
        - You can submit **up to 10** detection tasks at a time.


        ### Call description for audio file
        - Supported audio file size: **< 500 MB**
        - Supported audio file duration: **< 1 hour**
        - Supported audio bitrate: 128–256 Kbps
        - Supported audio file formats: WAV, MP3, AAC, FLAC, AMR, 3GP, M4A, WMA, OGG, and APE
        - **When the input is a video file**, the audio track can be extracted for separate audio content moderation.

        ### Call description for audio stream
        - Supported audio stream duration: **< 3 hours**
        - Supported audio bitrate: 128–256 Kbps
        - Supported audio stream transfer protocols: RTMP, HTTP, and HTTPS
        - Supported audio stream formats: RTP, SRTP, RTMP, RTMPS, MMSH, MMST, HLS, HTTP, TCP, HTTPS, and M3U8
        - **When the input is a video stream**, the audio track can be extracted for separate audio content moderation.

        ### Handling description for live streaming interruption
        - Ensure that the [CancelTask API](https://intl.cloud.tencent.com/document/product/1219/53258?from_cn_redirect=1) is connected.
        - If the live streaming task is canceled or completed, this API terminates live streaming pulling and exits moderation.
        - If the live streaming task is not canceled or completed and audio live streaming pushing is interrupted due to a fault, this API continues to try live streaming pulling within 10 minutes. If audio segment data is detected within 10 minutes, this API restores normal moderation. Otherwise, this API terminates pulling and exits moderation. If you still need moderation after pulling terminates, submit a moderation request again.

        :param request: Request instance for CreateAudioModerationTask.
        :type request: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationTaskRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.CreateAudioModerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAudioModerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAudioModerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskDetail(self, request):
        """This interface is used to view the detailed information of the audio moderation tasks, including task status, detection results, corresponding text content recognized from the audio file, recommended follow-up operations of the maliciousness tags corresponding to the detection results, and so on. For specific output content, see the output parameter examples.

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.ams.v20201229.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """This API is used to view the list of moderation tasks. You can also filter moderation tasks by multiple types of business information, such as business type, moderation result, and task status. The output content of the task list includes the total number of queried tasks, task name, task status, audio moderation type, maliciousness tag of the detection result, and suggested operation. For the specific output content, see the sample output parameters.<br>Default API request rate limit: **20 requests/sec**.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.ams.v20201229.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.ams.v20201229.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))