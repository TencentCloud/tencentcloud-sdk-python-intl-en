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
from tencentcloud.dts.v20180330 import models
from typing import Dict


class DtsClient(AbstractClient):
    _apiVersion = '2018-03-30'
    _endpoint = 'dts.intl.tencentcloudapi.com'
    _service = 'dts'

    async def ActivateSubscribe(
            self,
            request: models.ActivateSubscribeRequest,
            opts: Dict = None,
    ) -> models.ActivateSubscribeResponse:
        """
        This API is used to configure a data subscription, which can be called only for subscription instances in unconfigured status.
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteMigrateJob(
            self,
            request: models.CompleteMigrateJobRequest,
            opts: Dict = None,
    ) -> models.CompleteMigrateJobResponse:
        """
        This API (CompleteMigrateJob) is used to complete a data migration task.
        For tasks in incremental migration mode, you need to call this API before migration gets ready, so as to stop migrating incremental data.
        If the task status queried through the (DescribeMigrateJobs) API is ready (status=8), you can call this API to complete the migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrateCheckJob(
            self,
            request: models.CreateMigrateCheckJobRequest,
            opts: Dict = None,
    ) -> models.CreateMigrateCheckJobResponse:
        """
        This API is used to create a migration check task.
        Before migration, you should call this API to create a check. Migration will start only if the check succeeds. You can view the check result through the `DescribeMigrateCheckJob` API.
        After successful check, if the migration task needs to be modified, a new check task should be created and migration will begin only after the new check succeeds.

        For a finance zone link, use the domain name https://dts.ap-shenzhen-fsi.tencentcloudapi.com.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrateCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrateCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrateJob(
            self,
            request: models.CreateMigrateJobRequest,
            opts: Dict = None,
    ) -> models.CreateMigrateJobResponse:
        """
        This API (CreateMigrateJob) is used to create a data migration task.

        For a finance zone linkage, please use the domain name dts.ap-shenzhen-fsi.tencentcloudapi.com.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscribe(
            self,
            request: models.CreateSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateSubscribeResponse:
        """
        This API is used to create a data subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMigrateJob(
            self,
            request: models.DeleteMigrateJobRequest,
            opts: Dict = None,
    ) -> models.DeleteMigrateJobResponse:
        """
        This API (DeleteMigrationJob) is used to delete a data migration task. If the task status queried through the DescribeMigrateJobs API is checking (status=3), running (status=7), ready (status=8), canceling (status=11), or completing (status=12), the task cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        This API is used to query the execution result of a task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrateCheckJob(
            self,
            request: models.DescribeMigrateCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrateCheckJobResponse:
        """
        This API is used to get the check result and query check status and progress after a check is created.
        If the check succeeds, you can call the StartMigrateJob API to start migration.
        If the check fails, the reason can be queried. Please modify the migration configuration or adjust relevant parameters of the source/target instances through the ModifyMigrateJob API based on the error message.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrateCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrateCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrateJobs(
            self,
            request: models.DescribeMigrateJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrateJobsResponse:
        """
        This API is used to query data migration tasks.
        For a finance zone linkage, please use the domain name https://dts.ap-shenzhen-fsi.tencentcloudapi.com.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrateJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrateJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeConf(
            self,
            request: models.DescribeSubscribeConfRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeConfResponse:
        """
        This API is used to query the subscription instance configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribes(
            self,
            request: models.DescribeSubscribesRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribesResponse:
        """
        This API is used to get the information list of data subscription instances. Pagination is enabled by default with 20 results returned each time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateSubscribe(
            self,
            request: models.IsolateSubscribeRequest,
            opts: Dict = None,
    ) -> models.IsolateSubscribeResponse:
        """
        This API is used to isolate an hourly billed subscription instance. After this API is called, the instance will become unavailable and billing will stop for it.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateJob(
            self,
            request: models.ModifyMigrateJobRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateJobResponse:
        """
        This API (ModifyMigrateJob) is used to modify a data migration task.
        If the status of a migration task is creating (status=1), check succeeded (status=4), check failed (status=5), or migration failed (status=10), this API can be called to modify the task, but the type of the source and target instances and the region of the target instance cannot be modified.

        For a finance zone linkage, please use the domain name dts.ap-shenzhen-fsi.tencentcloudapi.com.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeConsumeTime(
            self,
            request: models.ModifySubscribeConsumeTimeRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeConsumeTimeResponse:
        """
        This API is used to modify the consumption time point of a data subscription channel.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeConsumeTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeConsumeTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeName(
            self,
            request: models.ModifySubscribeNameRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeNameResponse:
        """
        This API is used to rename a data subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeObjects(
            self,
            request: models.ModifySubscribeObjectsRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeObjectsResponse:
        """
        This API is used to modify the subscription rule of a data subscription channel.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeVipVport(
            self,
            request: models.ModifySubscribeVipVportRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeVipVportResponse:
        """
        This API is used to modify the IP and port number of a data subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeVipVport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeVipVportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OfflineIsolatedSubscribe(
            self,
            request: models.OfflineIsolatedSubscribeRequest,
            opts: Dict = None,
    ) -> models.OfflineIsolatedSubscribeResponse:
        """
        This API is used to deactivate an isolated data subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "OfflineIsolatedSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OfflineIsolatedSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetSubscribe(
            self,
            request: models.ResetSubscribeRequest,
            opts: Dict = None,
    ) -> models.ResetSubscribeResponse:
        """
        This API is used to reset a data subscription instance. Once reset, an activated instance can be bound to other database instances through the `ActivateSubscribe` API.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMigrateJob(
            self,
            request: models.StartMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StartMigrateJobResponse:
        """
        This API (StartMigrationJob) is used to start a migration task. After the API is called, non-scheduled migration tasks will start the migration immediately, while scheduled tasks will start the countdown.
        Before calling this API, be sure to use the CreateMigrateCheckJob API to check the data migration task, which can be started only if its status queried through the DescribeMigrateJobs API is check succeeded (status=4).
        """
        
        kwargs = {}
        kwargs["action"] = "StartMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMigrateJob(
            self,
            request: models.StopMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StopMigrateJobResponse:
        """
        This API (StopMigrateJob) is used to cancel a data migration task.
        During migration, this API can be used to cancel migration if the task status queried through the DescribeMigrateJobs API is running (status=7) or ready (status=8), and the migration task will fail.
        """
        
        kwargs = {}
        kwargs["action"] = "StopMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)