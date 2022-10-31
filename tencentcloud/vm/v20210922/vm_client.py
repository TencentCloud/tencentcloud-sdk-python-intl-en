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
from tencentcloud.vm.v20210922 import models


class VmClient(AbstractClient):
    _apiVersion = '2021-09-22'
    _endpoint = 'vm.tencentcloudapi.com'
    _service = 'vm'


    def CancelTask(self, request):
        """This API is used to cancel a video moderation task.

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.vm.v20210922.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
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
        """This API is used to create a video moderation task via a URL or bucket.

        :param request: Request instance for CreateVideoModerationTask.
        :type request: :class:`tencentcloud.vm.v20210922.models.CreateVideoModerationTaskRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.CreateVideoModerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoModerationTask", params, headers=headers)
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
        """This API is used to get details of the video moderation task.

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.vm.v20210922.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
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

        Default request rate limit: **20 requests/sec**.

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.vm.v20210922.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.vm.v20210922.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
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