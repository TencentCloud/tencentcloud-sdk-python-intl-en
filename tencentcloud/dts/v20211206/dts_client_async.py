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
from tencentcloud.dts.v20211206 import models
from typing import Dict


class DtsClient(AbstractClient):
    _apiVersion = '2021-12-06'
    _endpoint = 'dts.intl.tencentcloudapi.com'
    _service = 'dts'

    async def CompleteMigrateJob(
            self,
            request: models.CompleteMigrateJobRequest,
            opts: Dict = None,
    ) -> models.CompleteMigrateJobResponse:
        """
        This API is used to complete a data migration task.
        For tasks in incremental migration mode, you need to call this API before migration gets ready for completion to stop migrating incremental data.
        If the task status queried through the `DescribeMigrationJobs` API is ready (`Status` = `readyComplete`), you can call this API to complete the migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfigureSubscribeJob(
            self,
            request: models.ConfigureSubscribeJobRequest,
            opts: Dict = None,
    ) -> models.ConfigureSubscribeJobResponse:
        """
        This API is used to configure data subscription instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureSubscribeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureSubscribeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfigureSyncJob(
            self,
            request: models.ConfigureSyncJobRequest,
            opts: Dict = None,
    ) -> models.ConfigureSyncJobResponse:
        """
        This API is used to configure a sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ContinueMigrateJob(
            self,
            request: models.ContinueMigrateJobRequest,
            opts: Dict = None,
    ) -> models.ContinueMigrateJobResponse:
        """
        This API is used to resume a paused migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "ContinueMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ContinueMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ContinueSyncJob(
            self,
            request: models.ContinueSyncJobRequest,
            opts: Dict = None,
    ) -> models.ContinueSyncJobResponse:
        """
        This API is used to resume a paused data sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "ContinueSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ContinueSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCheckSyncJob(
            self,
            request: models.CreateCheckSyncJobRequest,
            opts: Dict = None,
    ) -> models.CreateCheckSyncJobResponse:
        """
        This API is used to verify a sync task by checking required parameters and peripheral configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCheckSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCheckSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCompareTask(
            self,
            request: models.CreateCompareTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCompareTaskResponse:
        """
        This API is used to create a data consistency check task. After the task is successfully created, its ID will be returned in the format of `dts-8yv4w2i1-cmp-37skmii9`, and you can call `StartCompare` to start it.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumerGroup(
            self,
            request: models.CreateConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerGroupResponse:
        """
        This API is used to creat a consumer group for the subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrateCheckJob(
            self,
            request: models.CreateMigrateCheckJobRequest,
            opts: Dict = None,
    ) -> models.CreateMigrateCheckJobResponse:
        """
        This API is used to verify a migration task.
        Before migration, you should call this API to create a check task. Migration will start only if the check succeeds. You can view the check result through the `DescribeMigrationCheckJob` API.
        After successful check, if the migration task needs to be modified, a new check task should be created, and migration will start only after the new check succeeds.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrateCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrateCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrationService(
            self,
            request: models.CreateMigrationServiceRequest,
            opts: Dict = None,
    ) -> models.CreateMigrationServiceResponse:
        """
        This API is used to purchase migration tasks. After the tasks are purchased successfully, a randomly generated list of task IDs will be returned. You can also call the `DescribeMigrationJobs` API to query the IDs of the successfully purchased tasks. Note that once a task is purchased successfully, the types and regions of the source and target databases cannot be changed.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrationService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrationServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModifyCheckSyncJob(
            self,
            request: models.CreateModifyCheckSyncJobRequest,
            opts: Dict = None,
    ) -> models.CreateModifyCheckSyncJobResponse:
        """
        This API is used to check whether the current data sync task supports object modification after the task configuration is modified.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModifyCheckSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModifyCheckSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscribe(
            self,
            request: models.CreateSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateSubscribeResponse:
        """
        This API is used to create a data subscription task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscribeCheckJob(
            self,
            request: models.CreateSubscribeCheckJobRequest,
            opts: Dict = None,
    ) -> models.CreateSubscribeCheckJobResponse:
        """
        This API is used to create a subscription check task. The task must have successfully called the ConfigureSubscribeJob interface to configure all necessary information before starting the check.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscribeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscribeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSyncJob(
            self,
            request: models.CreateSyncJobRequest,
            opts: Dict = None,
    ) -> models.CreateSyncJobResponse:
        """
        This API is used to create a sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompareTask(
            self,
            request: models.DeleteCompareTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteCompareTaskResponse:
        """
        This API is used to delete a data consistency check task, which can be called when the task status is `success`, `failed`, or `canceled`.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumerGroup(
            self,
            request: models.DeleteConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerGroupResponse:
        """
        This API is used to delete a consumer group of a subscription task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCheckSyncJobResult(
            self,
            request: models.DescribeCheckSyncJobResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCheckSyncJobResultResponse:
        """
        This API is used to query the result of the sync check task and check the required parameters and peripheral configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCheckSyncJobResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCheckSyncJobResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompareReport(
            self,
            request: models.DescribeCompareReportRequest,
            opts: Dict = None,
    ) -> models.DescribeCompareReportResponse:
        """
        This API is used to query the details of a data consistency check task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompareReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompareReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompareTasks(
            self,
            request: models.DescribeCompareTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeCompareTasksResponse:
        """
        This API is used to query the list of data consistency check tasks under the current task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompareTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompareTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroups(
            self,
            request: models.DescribeConsumerGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupsResponse:
        """
        This API is used to get consumer group details for the subscription instance configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrateDBInstances(
            self,
            request: models.DescribeMigrateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrateDBInstancesResponse:
        """
        This API is used to query migratable database instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationCheckJob(
            self,
            request: models.DescribeMigrationCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationCheckJobResponse:
        """
        This API is used to get the check result and query the check status and progress after a check is created.
        If the check succeeds, you can call the `StartMigrateJob` API to start migration.
        If the check fails, the cause can be queried. Modify the migration configuration or adjust relevant parameters of the source/target instances through the `ModifyMigrationJob` API based on the error message.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationDetail(
            self,
            request: models.DescribeMigrationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationDetailResponse:
        """
        This API is used to query the details of a migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationJobs(
            self,
            request: models.DescribeMigrationJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationJobsResponse:
        """
        This API is used to query the list of data migration tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModifyCheckSyncJobResult(
            self,
            request: models.DescribeModifyCheckSyncJobResultRequest,
            opts: Dict = None,
    ) -> models.DescribeModifyCheckSyncJobResultResponse:
        """
        This API is used to query the result of the created check task for object modification.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModifyCheckSyncJobResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModifyCheckSyncJobResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOffsetByTime(
            self,
            request: models.DescribeOffsetByTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeOffsetByTimeResponse:
        """
        This API is used to query the latest offset before the specified time in KafkaTopic.The offset output by the interface is the closest offset to this time.If the input time is much later than the current time, the output is equivalent to the latest offset;If the input time is much earlier than the current time, the output is equivalent to the oldest offset;If the input is empty, the default time is 0, which is the oldest offset to be queried.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOffsetByTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOffsetByTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeCheckJob(
            self,
            request: models.DescribeSubscribeCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeCheckJobResponse:
        """
        This API is used to query the results of a subscription check task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeDetail(
            self,
            request: models.DescribeSubscribeDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeDetailResponse:
        """
        This API is used to get the configuration information of the data subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeJobs(
            self,
            request: models.DescribeSubscribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeJobsResponse:
        """
        This API is used to get the information list of data subscription instances. Pagination is enabled by default with 20 results returned each time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscribeReturnable(
            self,
            request: models.DescribeSubscribeReturnableRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscribeReturnableResponse:
        """
        This API is used to query whether a subscription task can be terminated and returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscribeReturnable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscribeReturnableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSyncJobs(
            self,
            request: models.DescribeSyncJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeSyncJobsResponse:
        """
        This API is used to query the information of a sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSyncJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSyncJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyIsolatedSubscribe(
            self,
            request: models.DestroyIsolatedSubscribeRequest,
            opts: Dict = None,
    ) -> models.DestroyIsolatedSubscribeResponse:
        """
        This API is used to deactivate an isolated data subscription instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyIsolatedSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyIsolatedSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyMigrateJob(
            self,
            request: models.DestroyMigrateJobRequest,
            opts: Dict = None,
    ) -> models.DestroyMigrateJobResponse:
        """
        This API is used to delete a data migration task. For a billed task, you must first call the `IsolateMigrateJob` API to isolate it and make sure that it is in **Isolated** status before calling this API to delete it. For a free task, you can directly call the `IsolateMigrateJob` API to delete it.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroySyncJob(
            self,
            request: models.DestroySyncJobRequest,
            opts: Dict = None,
    ) -> models.DestroySyncJobResponse:
        """
        This API is used to delete a sync task. Only tasks in **Isolated** status can be completely deleted. After deletion, you can call the `DescribeSyncJobs` API to get the task list. If the deleted task is not in the list, it is deleted successfully.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroySyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroySyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateMigrateJob(
            self,
            request: models.IsolateMigrateJobRequest,
            opts: Dict = None,
    ) -> models.IsolateMigrateJobResponse:
        """
        This API is used to isolate and return a data migration task. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status. For a billed task, after isolating it, you can call `RecoverMigrationJob` to recover it or call `DestroyMigrateJob` to delete it. For a free task, calling this API will directly delete it permanently.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateSubscribe(
            self,
            request: models.IsolateSubscribeRequest,
            opts: Dict = None,
    ) -> models.IsolateSubscribeResponse:
        """
        This API is used to isolate the subscription task. After calling, the subscription task will not be available. Pay-as-you-go tasks will stop billing, and monthly subscription tasks will refund automatically.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateSyncJob(
            self,
            request: models.IsolateSyncJobRequest,
            opts: Dict = None,
    ) -> models.IsolateSyncJobResponse:
        """
        This API is used to isolate a sync task. After the task is isolated, you can call the `DescribeSyncJobs` API to query its status, call `RecoverSyncJob` to recover it, or directly delete it. For a free task, calling this API will directly delete it permanently.
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCompareTask(
            self,
            request: models.ModifyCompareTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyCompareTaskResponse:
        """
        This API is used to modify the parameters of a data consistency check task after it is created and before it starts.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCompareTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCompareTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCompareTaskName(
            self,
            request: models.ModifyCompareTaskNameRequest,
            opts: Dict = None,
    ) -> models.ModifyCompareTaskNameResponse:
        """
        This API is used to rename a data consistency check task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCompareTaskName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCompareTaskNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroupDescription(
            self,
            request: models.ModifyConsumerGroupDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupDescriptionResponse:
        """
        This API is used to modify the description of the specified subscription consumption group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroupDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroupPassword(
            self,
            request: models.ModifyConsumerGroupPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupPasswordResponse:
        """
        This API is used to modify the password of the specified subscription consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroupPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateJobSpec(
            self,
            request: models.ModifyMigrateJobSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateJobSpecResponse:
        """
        This API is used to adjust the specification of a pay-as-you-go task. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateJobSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateJobSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateName(
            self,
            request: models.ModifyMigrateNameRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateNameResponse:
        """
        This API is used to rename a migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateRateLimit(
            self,
            request: models.ModifyMigrateRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateRateLimitResponse:
        """
        This API is used to restrict the rate limit of the task, when a user finds that migration task has a large impact on the load of user's database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrateRuntimeAttribute(
            self,
            request: models.ModifyMigrateRuntimeAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrateRuntimeAttributeResponse:
        """
        This API is used to modify task runtime attributes. This interface is different from the configuration class interface and does not perform state machine evaluation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrateRuntimeAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrateRuntimeAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrationJob(
            self,
            request: models.ModifyMigrationJobRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrationJobResponse:
        """
        This API is used to configure a migration task. After it is configured successfully, you can call the `CreateMigrationCheckJob` API to create a check task, and only after it passes the check can it be started.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrationJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrationJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeAutoRenewFlag(
            self,
            request: models.ModifySubscribeAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeAutoRenewFlagResponse:
        """
        This API is used to modify the auto-renewal flag of your subscription instance. Only the monthly subscription modification task makes sense. After modifying, the pay-as-you-go task has no impact.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubscribeName(
            self,
            request: models.ModifySubscribeNameRequest,
            opts: Dict = None,
    ) -> models.ModifySubscribeNameResponse:
        """
        This API is used to modify the name of the data subscription instance.
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
        This API is used to modify the data subscription object and Kafka partition rule. For MongoDB subscription, you can also modify the output aggregation rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubscribeObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubscribeObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySyncJobConfig(
            self,
            request: models.ModifySyncJobConfigRequest,
            opts: Dict = None,
    ) -> models.ModifySyncJobConfigResponse:
        """
        This API is used to modify the configuration of a data sync task after the task is started.\n Configuration modification steps:  Modify sync task configuration -> Create a modification check task -> Query the check task result -> Start the configuration modification check task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncJobConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncJobConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySyncRateLimit(
            self,
            request: models.ModifySyncRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifySyncRateLimitResponse:
        """
        This API is used to restrict the rate limit of the task, when a user finds that the sync task has a large impact on the load of user's database.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySyncRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySyncRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseMigrateJob(
            self,
            request: models.PauseMigrateJobRequest,
            opts: Dict = None,
    ) -> models.PauseMigrateJobResponse:
        """
        This API is used to pause a migration task.
        """
        
        kwargs = {}
        kwargs["action"] = "PauseMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseSyncJob(
            self,
            request: models.PauseSyncJobRequest,
            opts: Dict = None,
    ) -> models.PauseSyncJobResponse:
        """
        This API is used to pause a data sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "PauseSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverMigrateJob(
            self,
            request: models.RecoverMigrateJobRequest,
            opts: Dict = None,
    ) -> models.RecoverMigrateJobResponse:
        """
        This API is used to recover a data migration task in **Isolated** status. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverSyncJob(
            self,
            request: models.RecoverSyncJobRequest,
            opts: Dict = None,
    ) -> models.RecoverSyncJobResponse:
        """
        This API is used to recover a sync task in **Isolated** status. After calling this API, you can call the `DescribeSyncJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetConsumerGroupOffset(
            self,
            request: models.ResetConsumerGroupOffsetRequest,
            opts: Dict = None,
    ) -> models.ResetConsumerGroupOffsetResponse:
        """
        This API is used to reset the offset of the subscription consumer group. Call the DescribeConsumerGroups API to query the status of the consumer group, only when the status is Dead or Empty can this operation be executed. Otherwise, the reset will not be effective and the API will not return any error.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetConsumerGroupOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetConsumerGroupOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetSubscribe(
            self,
            request: models.ResetSubscribeRequest,
            opts: Dict = None,
    ) -> models.ResetSubscribeResponse:
        """
        This API is used to reset the subscription instance. After resetting, the subscription task can be reconfigured.You can call DescribeSubscribeDetail to query the subscription information to determine whether the subscription is successful. When SubsStatus changes to notStarted, it means the reset is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeSyncJob(
            self,
            request: models.ResizeSyncJobRequest,
            opts: Dict = None,
    ) -> models.ResizeSyncJobResponse:
        """
        This API is used to adjust the specification of a pay-as-you-go sync task. After this API is called, the backend needs to take about 3-5 minutes to implement the adjustment. You can call the `DescribeSyncJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeMigrateJob(
            self,
            request: models.ResumeMigrateJobRequest,
            opts: Dict = None,
    ) -> models.ResumeMigrateJobResponse:
        """
        This API is used to retry an abnormal or failed Redis data migration task. Note that this operation will skip the check stage and directly start the task, just like by calling `StartMigrationJob`. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeSubscribe(
            self,
            request: models.ResumeSubscribeRequest,
            opts: Dict = None,
    ) -> models.ResumeSubscribeResponse:
        """
        This API is used to resume faulty subscription tasks. When the status of the subscription task is set to error, you can resume task via this API.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeSyncJob(
            self,
            request: models.ResumeSyncJobRequest,
            opts: Dict = None,
    ) -> models.ResumeSyncJobResponse:
        """
        This API is used to retry a sync task after certain resolvable errors are reported. After calling this API, you can call the `DescribeSyncJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SkipCheckItem(
            self,
            request: models.SkipCheckItemRequest,
            opts: Dict = None,
    ) -> models.SkipCheckItemResponse:
        """
        This API is used for the backend to skip a failed check item. Theoretically, to execute a migration task normally, any check step cannot be skipped, and the check must be passed. For products or links that support check item skipping, see [Check Item Overview](https://www.tencentcloud.com/document/product/571/42551).
        """
        
        kwargs = {}
        kwargs["action"] = "SkipCheckItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SkipCheckItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SkipSyncCheckItem(
            self,
            request: models.SkipSyncCheckItemRequest,
            opts: Dict = None,
    ) -> models.SkipSyncCheckItemResponse:
        """
        This API is used for the backend to skip a failed check item. Theoretically, to execute a sync task normally, any check step cannot be skipped, and the check must be passed. For products or links that support check item skipping, see [Check Item Overview](https://www.tencentcloud.com/document/product/571/42551).
        """
        
        kwargs = {}
        kwargs["action"] = "SkipSyncCheckItem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SkipSyncCheckItemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCompare(
            self,
            request: models.StartCompareRequest,
            opts: Dict = None,
    ) -> models.StartCompareResponse:
        """
        This API is used to start a data consistency check task after creating it by calling the `CreateCompareTask` API. After calling this API, you can call the `DescribeCompareTasks` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "StartCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMigrateJob(
            self,
            request: models.StartMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StartMigrateJobResponse:
        """
        This API (`StartMigrationJob`) is used to start a migration task. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "StartMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartModifySyncJob(
            self,
            request: models.StartModifySyncJobRequest,
            opts: Dict = None,
    ) -> models.StartModifySyncJobResponse:
        """
        This API is used to start the configuration modification process when the modification check task status becomes “success”.
        """
        
        kwargs = {}
        kwargs["action"] = "StartModifySyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartModifySyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartSubscribe(
            self,
            request: models.StartSubscribeRequest,
            opts: Dict = None,
    ) -> models.StartSubscribeResponse:
        """
        This API is used to start a Kafka version of the data subscription instance. This interface can be called only when the status of the subscription task is checkPass.
        """
        
        kwargs = {}
        kwargs["action"] = "StartSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartSyncJob(
            self,
            request: models.StartSyncJobRequest,
            opts: Dict = None,
    ) -> models.StartSyncJobResponse:
        """
        This API is used to start a sync task.
        """
        
        kwargs = {}
        kwargs["action"] = "StartSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCompare(
            self,
            request: models.StopCompareRequest,
            opts: Dict = None,
    ) -> models.StopCompareResponse:
        """
        This API is used to stop a data consistency check task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopCompare"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCompareResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMigrateJob(
            self,
            request: models.StopMigrateJobRequest,
            opts: Dict = None,
    ) -> models.StopMigrateJobResponse:
        """
        This API is used to stop a data migration task.
        After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "StopMigrateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMigrateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSyncJob(
            self,
            request: models.StopSyncJobRequest,
            opts: Dict = None,
    ) -> models.StopSyncJobResponse:
        """
        This API is used to stop a sync task. After calling this API, you can call the `DescribeSyncJobs` API to query the latest task status.
        """
        
        kwargs = {}
        kwargs["action"] = "StopSyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)