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
from tencentcloud.dts.v20211206 import models


class DtsClient(AbstractClient):
    _apiVersion = '2021-12-06'
    _endpoint = 'dts.tencentcloudapi.com'
    _service = 'dts'


    def CompleteMigrateJob(self, request):
        """This API is used to complete a data migration task.
        For tasks in incremental migration mode, you need to call this API before migration gets ready for completion to stop migrating incremental data.
        If the task status queried through the `DescribeMigrationJobs` API is ready (`Status` = `readyComplete), you can call this API to complete the migration task.

        :param request: Request instance for CompleteMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CompleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CompleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ConfigureSyncJob(self, request):
        """This API is used to configure a sync task.

        :param request: Request instance for ConfigureSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ConfigureSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ConfigureSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfigureSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ConfigureSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ContinueMigrateJob(self, request):
        """This API is used to resume a paused migration task.

        :param request: Request instance for ContinueMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ContinueMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ContinueMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ContinueMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.ContinueMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ContinueSyncJob(self, request):
        """This API is used to resume a paused data sync task.

        :param request: Request instance for ContinueSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ContinueSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ContinueSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ContinueSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ContinueSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCheckSyncJob(self, request):
        """This API is used to verify a sync task by checking required parameters and peripheral configuration.

        :param request: Request instance for CreateCheckSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateCheckSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateCheckSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCheckSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCheckSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCompareTask(self, request):
        """This API is used to create a data consistency check task. After the task is successfully created, its ID will be returned in the format of `dts-8yv4w2i1-cmp-37skmii9`, and you can call `StartCompare` to start it.

        :param request: Request instance for CreateCompareTask.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateCompareTaskRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateCompareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCompareTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCompareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigrateCheckJob(self, request):
        """This API is used to verify a migration task.
        Before migration, you should call this API to create a check task. Migration will start only if the check succeeds. You can view the check result through the `DescribeMigrationCheckJob` API.
        After successful check, if the migration task needs to be modified, a new check task should be created, and migration will start only after the new check succeeds.

        :param request: Request instance for CreateMigrateCheckJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigrateCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrateCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigrationService(self, request):
        """This API is used to purchase migration tasks. After the tasks are purchased successfully, a randomly generated list of task IDs will be returned. You can also call the `DescribeMigrationJobs` API to query the IDs of the successfully purchased tasks. Note that once a task is purchased successfully, the types and regions of the source and target databases cannot be changed.

        :param request: Request instance for CreateMigrationService.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateMigrationServiceRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateMigrationServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigrationService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrationServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModifyCheckSyncJob(self, request):
        """This API is used to check whether the current data sync task supports object modification after the task configuration is modified.

        :param request: Request instance for CreateModifyCheckSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateModifyCheckSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateModifyCheckSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModifyCheckSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModifyCheckSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSyncJob(self, request):
        """This API is used to create a sync task.

        :param request: Request instance for CreateSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.CreateSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.CreateSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCompareTask(self, request):
        """This API is used to delete a data consistency check task, which can be called when the task status is `success`, `failed`, or `canceled`.

        :param request: Request instance for DeleteCompareTask.
        :type request: :class:`tencentcloud.dts.v20211206.models.DeleteCompareTaskRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DeleteCompareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompareTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCompareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCheckSyncJobResult(self, request):
        """This API is used to query the result of the sync check task and check the required parameters and peripheral configurations.

        :param request: Request instance for DescribeCheckSyncJobResult.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeCheckSyncJobResultRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeCheckSyncJobResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckSyncJobResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCheckSyncJobResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompareReport(self, request):
        """This API is used to query the details of a data consistency check task.

        :param request: Request instance for DescribeCompareReport.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeCompareReportRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeCompareReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompareReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompareReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompareTasks(self, request):
        """This API is used to query the list of data consistency check tasks under the current task.

        :param request: Request instance for DescribeCompareTasks.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeCompareTasksRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeCompareTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompareTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompareTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrateDBInstances(self, request):
        """This API is used to query migratable database instances.

        :param request: Request instance for DescribeMigrateDBInstances.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrateDBInstancesRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationCheckJob(self, request):
        """This API is used to get the check result and query the check status and progress after a check is created.
        If the check succeeds, you can call the `StartMigrateJob` API to start migration.
        If the check fails, the cause can be queried. Modify the migration configuration or adjust relevant parameters of the source/target instances through the `ModifyMigrationJob` API based on the error message.

        :param request: Request instance for DescribeMigrationCheckJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationCheckJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationCheckJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationCheckJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationDetail(self, request):
        """This API is used to query the details of a migration task.

        :param request: Request instance for DescribeMigrationDetail.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationDetailRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationJobs(self, request):
        """This API is used to query the list of data migration tasks.

        :param request: Request instance for DescribeMigrationJobs.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeMigrationJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModifyCheckSyncJobResult(self, request):
        """This API is used to query the result of the created check task for object modification.

        :param request: Request instance for DescribeModifyCheckSyncJobResult.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeModifyCheckSyncJobResultRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeModifyCheckSyncJobResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModifyCheckSyncJobResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModifyCheckSyncJobResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSyncJobs(self, request):
        """This API is used to query the information of a sync task.

        :param request: Request instance for DescribeSyncJobs.
        :type request: :class:`tencentcloud.dts.v20211206.models.DescribeSyncJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DescribeSyncJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSyncJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSyncJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyMigrateJob(self, request):
        """This API is used to delete a data migration task. For a billed task, you must first call the `IsolateMigrateJob` API to isolate it and make sure that it is in **Isolated** status before calling this API to delete it. For a free task, you can directly call the `IsolateMigrateJob` API to delete it.

        :param request: Request instance for DestroyMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.DestroyMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DestroyMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroySyncJob(self, request):
        """This API is used to delete a sync task. Only tasks in **Isolated** status can be completely deleted. After deletion, you can call the `DescribeSyncJobs` API to get the task list. If the deleted task is not in the list, it is deleted successfully.

        :param request: Request instance for DestroySyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.DestroySyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.DestroySyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroySyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.DestroySyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateMigrateJob(self, request):
        """This API is used to isolate and return a data migration task. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status. For a billed task, after isolating it, you can call `RecoverMigrationJob` to recover it or call `DestroyMigrateJob` to delete it. For a free task, calling this API will directly delete it permanently.

        :param request: Request instance for IsolateMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.IsolateMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.IsolateMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateSyncJob(self, request):
        """This API is used to isolate a sync task. After the task is isolated, you can call the `DescribeSyncJobs` API to query its status, call `RecoverSyncJob` to recover it, or directly delete it. For a free task, calling this API will directly delete it permanently.

        :param request: Request instance for IsolateSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.IsolateSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.IsolateSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCompareTask(self, request):
        """This API is used to modify the parameters of a data consistency check task after it is created and before it starts.

        :param request: Request instance for ModifyCompareTask.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCompareTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCompareTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCompareTaskName(self, request):
        """This API is used to rename a data consistency check task.

        :param request: Request instance for ModifyCompareTaskName.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskNameRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyCompareTaskNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCompareTaskName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCompareTaskNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrateJobSpec(self, request):
        """This API is used to adjust the specification of a pay-as-you-go task. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.

        :param request: Request instance for ModifyMigrateJobSpec.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateJobSpecRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrateJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrateJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrateName(self, request):
        """This API is used to rename a migration task.

        :param request: Request instance for ModifyMigrateName.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateNameRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrateNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrateName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrateNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigrationJob(self, request):
        """This API is used to configure a migration task. After it is configured successfully, you can call the `CreateMigrationCheckJob` API to create a check task, and only after it passes the check can it be started.

        :param request: Request instance for ModifyMigrationJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifyMigrationJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifyMigrationJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigrationJob", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrationJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySyncJobConfig(self, request):
        """This API is used to modify the configuration of a data sync task after the task is started.\n Configuration modification steps:  Modify sync task configuration -> Create a modification check task -> Query the check task result -> Start the configuration modification check task

        :param request: Request instance for ModifySyncJobConfig.
        :type request: :class:`tencentcloud.dts.v20211206.models.ModifySyncJobConfigRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ModifySyncJobConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySyncJobConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySyncJobConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseMigrateJob(self, request):
        """This API is used to pause a migration task.

        :param request: Request instance for PauseMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.PauseMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.PauseMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.PauseMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseSyncJob(self, request):
        """This API is used to pause a data sync task.

        :param request: Request instance for PauseSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.PauseSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.PauseSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.PauseSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverMigrateJob(self, request):
        """This API is used to recover a data migration task in **Isolated** status. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.

        :param request: Request instance for RecoverMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.RecoverMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.RecoverMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverSyncJob(self, request):
        """This API is used to recover a sync task in **Isolated** status. After calling this API, you can call the `DescribeSyncJobs` API to query the latest task status.

        :param request: Request instance for RecoverSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.RecoverSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.RecoverSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeSyncJob(self, request):
        """This API is used to adjust the specification of a pay-as-you-go sync task. After this API is called, the backend needs to take about 3-5 minutes to implement the adjustment. You can call the `DescribeSyncJobs` API to query the latest task status.

        :param request: Request instance for ResizeSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResizeSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResizeSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeMigrateJob(self, request):
        """This API is used to retry an abnormal or failed Redis data migration task. Note that this operation will skip the check stage and directly start the task, just like by calling `StartMigrationJob`. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.

        :param request: Request instance for ResumeMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResumeMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResumeMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeSyncJob(self, request):
        """This API is used to retry a sync task after certain resolvable errors are reported. After calling this API, you can call the `DescribeSyncJobs` API to query the latest task status.

        :param request: Request instance for ResumeSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.ResumeSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.ResumeSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SkipCheckItem(self, request):
        """This API is used for the backend to skip a failed check item. Theoretically, to execute a migration task normally, any check step cannot be skipped, and the check must be passed. For products or links that support check item skipping, see [Check Item Overview](https://www.tencentcloud.com/document/product/571/42551).

        :param request: Request instance for SkipCheckItem.
        :type request: :class:`tencentcloud.dts.v20211206.models.SkipCheckItemRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.SkipCheckItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SkipCheckItem", params, headers=headers)
            response = json.loads(body)
            model = models.SkipCheckItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SkipSyncCheckItem(self, request):
        """This API is used for the backend to skip a failed check item. Theoretically, to execute a sync task normally, any check step cannot be skipped, and the check must be passed. For products or links that support check item skipping, see [Check Item Overview](https://www.tencentcloud.com/document/product/571/42551).

        :param request: Request instance for SkipSyncCheckItem.
        :type request: :class:`tencentcloud.dts.v20211206.models.SkipSyncCheckItemRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.SkipSyncCheckItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SkipSyncCheckItem", params, headers=headers)
            response = json.loads(body)
            model = models.SkipSyncCheckItemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCompare(self, request):
        """This API is used to start a data consistency check task after creating it by calling the `CreateCompareTask` API. After calling this API, you can call the `DescribeCompareTasks` API to query the latest task status.

        :param request: Request instance for StartCompare.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartCompareRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCompare", params, headers=headers)
            response = json.loads(body)
            model = models.StartCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMigrateJob(self, request):
        """This API (`StartMigrationJob`) is used to start a migration task. After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.

        :param request: Request instance for StartMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartModifySyncJob(self, request):
        """This API is used to start the configuration modification process when the modification check task status becomes “success”.

        :param request: Request instance for StartModifySyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartModifySyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartModifySyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartModifySyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartModifySyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartSyncJob(self, request):
        """This API is used to start a sync task.

        :param request: Request instance for StartSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StartSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StartSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.StartSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCompare(self, request):
        """This API is used to stop a data consistency check task.

        :param request: Request instance for StopCompare.
        :type request: :class:`tencentcloud.dts.v20211206.models.StopCompareRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StopCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCompare", params, headers=headers)
            response = json.loads(body)
            model = models.StopCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMigrateJob(self, request):
        """This API is used to stop a data migration task.
        After calling this API, you can call the `DescribeMigrationJobs` API to query the latest task status.

        :param request: Request instance for StopMigrateJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StopMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StopMigrateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMigrateJob", params, headers=headers)
            response = json.loads(body)
            model = models.StopMigrateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopSyncJob(self, request):
        """This API is used to stop a sync task. After calling this API, you can call the `DescribeSyncJobs` API to query the latest task status.

        :param request: Request instance for StopSyncJob.
        :type request: :class:`tencentcloud.dts.v20211206.models.StopSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20211206.models.StopSyncJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopSyncJob", params, headers=headers)
            response = json.loads(body)
            model = models.StopSyncJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))