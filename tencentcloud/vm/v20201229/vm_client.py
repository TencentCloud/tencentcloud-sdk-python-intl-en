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
from tencentcloud.vm.v20201229 import models


class VmClient(AbstractClient):
    _apiVersion = '2020-12-29'
    _endpoint = 'vm.tencentcloudapi.com'
    _service = 'vm'


    def CancelTask(self, request):
        """This API is used to cancel a moderation task. It will return the `TaskId` of the task after the task is canceled successfully.<br>

        Default API request rate limit: **20 requests/sec**.

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.vm.v20201229.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20201229.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
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


    def CreateVideoModerationTask(self, request):
        """This API is used to submit a video file or stream for smart moderation. Before using it, you need to log in to the console with the Tencent Cloud root account [to activate VM](https://console.cloud.tencent.com/cms/video/package) and adjust the business configuration.<br>
        ### Feature use instructions

        - Go to the "[CMS console - VM](https://console.cloud.tencent.com/cms/video/package)" to activate AMS.

        - This API is a paid API. For its billing mode, see [VM Pricing](https://intl.cloud.tencent.com/product/vm/pricing?from_cn_redirect=1).

        - Default API request rate limit: **20 requests/sec**. When this limit is exceeded, requests for async moderation tasks (video on demand) will automatically join the queue of requests pending moderation, while an error will be reported for sync moderation tasks (video live streaming).
        - Default limit on the number of concurrent moderation channels: 10. When this limit is exceeded, requests for async moderation tasks (video on demand) will automatically join the queue of requests pending moderation, while an error will be reported for sync moderation tasks (video live streaming).


        ### API feature description

        - It can automatically detect video files or streams and recognize non-compliant content in them based on the deep learning technology from the perspectives of OCR-based text recognition, object detection (such as object, advertising logo, and QR code), image recognition, and audio moderation;
        - It allows you to set the callback address (Callback) to get the detection result or call the API for viewing task details to get the details of the detection result through polling. For normal video moderation tasks, if non-compliant content is contained, the captured frames will be called back within **3s**, and the audio segments will be called back within the configured **segment duration + 2s**; for queued moderation tasks, the callback time will be equal to the sum of the callback time for normal moderation and waiting time;
        - The API for viewing the moderation task list can be called to query the task queue. You can filter moderation tasks by multiple types of business information, such as business type, moderation result, and task status;
        - It can recognize various non-compliant scenarios, including vulgarity, abuse, pornography, and advertising;
        - It allows you to customize moderation policies based on different business scenarios;
        - You can customize blocklist/allowlist dictionaries and image libraries to filter non-compliant content of custom types (currently, only blocklist configuration is supported);
        - You can customize the moderation task priority, so that when multiple tasks are queuing, the task priority will be automatically adjusted according to the configuration;
        - You can submit detection tasks in batches and **create up to 10 tasks at a time**;

        ### Call description for video file

        - Supported video file size: **< 3 GB**
        - Supported video file resolution: **the optimal resolution is 1920x1080 (1080p)**. For video files of less than 300 MB in size, their resolution can be greater than 1080p; for video files of a greater size, you can call [MPS](https://intl.cloud.tencent.com/product/mps/details?from_cn_redirect=1) to transcode them before submitting them for moderation;
        - Supported video file formats: FLV, MKV, MP4, RMVB, AVI, WMV, 3GP, TS, MOV, RM, MPEG, and WMF;
        - Supported video file access methods: URL (over HTTP/HTTPS) and Tencent Cloud COS;
        - If you pass in the access URL of a video file, you need to **limit its header file read time to 3 seconds**. To ensure the stability and reliability of the video to be detected, we recommend you use Tencent Cloud COS for storage or CDN for caching;
        - You can configure whether to enable audio moderation, and if it is not enabled, only the image content of video files will be moderated.

        ### Call description for video stream

        - Supported video stream duration: **< 5 hours**
        - Supported video stream resolution: **1920x1080 (1080p)**. For videos with a higher resolution, you can call [live transcoding](https://intl.cloud.tencent.com/document/product/267/39889?from_cn_redirect=1) to transcode them before submitting them for moderation;
        - Supported video stream formats: mainstream video stream codecs such as RMTP and FLV;
        - Supported video transfer protocols: HTTP, HTTPS, and RTMP;
        - You can configure whether to enable audio moderation, and if it is not enabled, only the image content of video streams will be moderated.

        :param request: Request instance for CreateVideoModerationTask.
        :type request: :class:`tencentcloud.vm.v20201229.models.CreateVideoModerationTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20201229.models.CreateVideoModerationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVideoModerationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVideoModerationTaskResponse()
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


    def DescribeTaskDetail(self, request):
        """This API is used to poll the details of the detection result.<br>

        Default API request rate limit: **200 requests/sec**.

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.vm.v20201229.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.vm.v20201229.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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


    def DescribeTasks(self, request):
        """This API is used to query the task queue. You can filter moderation tasks by multiple types of business information, such as business type, moderation result, and task status.<br>

        Default API request rate limit: **20 requests/sec**.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.vm.v20201229.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.vm.v20201229.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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