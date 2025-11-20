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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.vm.v20210922 import models
from typing import Dict


class VmClient(AbstractClient):
    _apiVersion = '2021-09-22'
    _endpoint = 'vm.intl.tencentcloudapi.com'
    _service = 'vm'

    async def CancelTask(
            self,
            request: models.CancelTaskRequest,
            opts: Dict = None,
    ) -> models.CancelTaskResponse:
        """
        This API is used to cancel a video moderation task.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoModerationTask(
            self,
            request: models.CreateVideoModerationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoModerationTaskResponse:
        """
        This API is used to create a video moderation task via a URL or bucket.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoModerationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoModerationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetail(
            self,
            request: models.DescribeTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailResponse:
        """
        This API is used to get details of the video moderation task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        This API is used to query the task queue. You can filter moderation tasks by multiple types of business information, such as business type, moderation result, and task status.<br>

        Default request rate limit: **20 requests/sec**.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)