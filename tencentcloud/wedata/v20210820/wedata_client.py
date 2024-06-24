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
from tencentcloud.wedata.v20210820 import models


class WedataClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'


    def BatchCreateIntegrationTaskAlarms(self, request):
        """Bulk Create Task Alert Rules

        :param request: Request instance for BatchCreateIntegrationTaskAlarms.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchCreateIntegrationTaskAlarmsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchCreateIntegrationTaskAlarmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateIntegrationTaskAlarms", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateIntegrationTaskAlarmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteIntegrationTasks(self, request):
        """Batch Delete Integration Tasks.

        :param request: Request instance for BatchDeleteIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeleteOpsTasks(self, request):
        """Task Operation and Maintenance - Batch Delete Tasks

        :param request: Request instance for BatchDeleteOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchForceSuccessIntegrationTaskInstances(self, request):
        """Batch set successful integration task instances

        :param request: Request instance for BatchForceSuccessIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchForceSuccessIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchForceSuccessIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchForceSuccessIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchForceSuccessIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchKillIntegrationTaskInstances(self, request):
        """Batch Terminate Integration Task Instances

        :param request: Request instance for BatchKillIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchKillIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchKillIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchKillIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchKillIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchMakeUpIntegrationTasks(self, request):
        """Perform Batch Data Supplement Operation on Integrated Offline Tasks

        :param request: Request instance for BatchMakeUpIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchMakeUpIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchMakeUpIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchMakeUpIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchMakeUpIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyOpsOwners(self, request):
        """Batch Modify Task Assignee

        :param request: Request instance for BatchModifyOpsOwners.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOpsOwnersRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOpsOwnersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyOpsOwners", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyOpsOwnersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRerunIntegrationTaskInstances(self, request):
        """Batch Rerun Integration Task Instances

        :param request: Request instance for BatchRerunIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchRerunIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchRerunIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRerunIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRerunIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchResumeIntegrationTasks(self, request):
        """Batch Continue Execution of Integrated Real-time Tasks

        :param request: Request instance for BatchResumeIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchResumeIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchResumeIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchResumeIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchResumeIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRunOpsTask(self, request):
        """Task Operation and Maintenance - Task List Batch Startup

        :param request: Request instance for BatchRunOpsTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchRunOpsTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchRunOpsTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRunOpsTask", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRunOpsTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStartIntegrationTasks(self, request):
        """Batch Run Integration Tasks

        :param request: Request instance for BatchStartIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStartIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStartIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStartIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStartIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopIntegrationTasks(self, request):
        """Batch Stop Integration Tasks

        :param request: Request instance for BatchStopIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopOpsTasks(self, request):
        """Only valid for tasks in "Scheduling In Progress" and "Paused" statuses, terminate the task instances of the selected tasks, and stop scheduling

        :param request: Request instance for BatchStopOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchStopWorkflowsByIds(self, request):
        """Batch Stop Workflow

        :param request: Request instance for BatchStopWorkflowsByIds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopWorkflowsByIdsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopWorkflowsByIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopWorkflowsByIds", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopWorkflowsByIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchSuspendIntegrationTasks(self, request):
        """Batch pause integration tasks

        :param request: Request instance for BatchSuspendIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchSuspendIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchSuspendIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchSuspendIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchSuspendIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchUpdateIntegrationTasks(self, request):
        """Bulk Update Integration Tasks (Currently only supports bulk updating of the person in charge)

        :param request: Request instance for BatchUpdateIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchUpdateIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchUpdateIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAlarmRegularNameExist(self, request):
        """Check for Duplicate Alert Rule Names

        :param request: Request instance for CheckAlarmRegularNameExist.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckAlarmRegularNameExistRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckAlarmRegularNameExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAlarmRegularNameExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAlarmRegularNameExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIntegrationNodeNameExists(self, request):
        """Determining if the name of the integrated node exists

        :param request: Request instance for CheckIntegrationNodeNameExists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationNodeNameExistsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationNodeNameExistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIntegrationNodeNameExists", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIntegrationNodeNameExistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckIntegrationTaskNameExists(self, request):
        """Check if Integration Task Name Exists

        :param request: Request instance for CheckIntegrationTaskNameExists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationTaskNameExistsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationTaskNameExistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIntegrationTaskNameExists", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIntegrationTaskNameExistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTaskNameExist(self, request):
        """Offline Task Renaming Verification

        :param request: Request instance for CheckTaskNameExist.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTaskNameExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTaskNameExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitIntegrationTask(self, request):
        """Submit integration task

        :param request: Request instance for CommitIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitRuleGroupTask(self, request):
        """Submit Rule Group to Run Task Interface

        :param request: Request instance for CommitRuleGroupTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitRuleGroupTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitRuleGroupTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CountOpsInstanceState(self, request):
        """Statistics on task instance status

        :param request: Request instance for CountOpsInstanceState.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CountOpsInstanceStateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CountOpsInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CountOpsInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.CountOpsInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomFunction(self, request):
        """Create User-Defined Function

        :param request: Request instance for CreateCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataSource(self, request):
        """Create Data Source

        :param request: Request instance for CreateDataSource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDsFolder(self, request):
        """Orchestration Space - Create Folder

        :param request: Request instance for CreateDsFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateDsFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateDsFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDsFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDsFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHiveTable(self, request):
        """Create Hive Table

        :param request: Request instance for CreateHiveTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHiveTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHiveTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHiveTableByDDL(self, request):
        """Create Hive table and return table name

        :param request: Request instance for CreateHiveTableByDDL.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableByDDLRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableByDDLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHiveTableByDDL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHiveTableByDDLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntegrationNode(self, request):
        """Create Integration Node

        :param request: Request instance for CreateIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIntegrationTask(self, request):
        """Create Integration Task

        :param request: Request instance for CreateIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOfflineTask(self, request):
        """Create Offline Task

        :param request: Request instance for CreateOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOpsMakePlan(self, request):
        """Bulk Data Supplement (Create Supplementary Entry Task)

        :param request: Request instance for CreateOpsMakePlan.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateOpsMakePlanRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateOpsMakePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOpsMakePlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOpsMakePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """Create quality rule interface

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRuleTemplate(self, request):
        """Create Rule Template

        :param request: Request instance for CreateRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTask(self, request):
        """Creating task

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskAlarmRegular(self, request):
        """Create task alert rules

        :param request: Request instance for CreateTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskFolder(self, request):
        """Orchestration Space - Workflow - Create Task Folder

        :param request: Request instance for CreateTaskFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskVersionDs(self, request):
        """Submit Task Version

        :param request: Request instance for CreateTaskVersionDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskVersionDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskVersionDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskVersionDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskVersionDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkflowDs(self, request):
        """Creating workflow

        :param request: Request instance for CreateWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DagInstances(self, request):
        """Pull DAG Instance

        :param request: Request instance for DagInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DagInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DagInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DagInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DagInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomFunction(self, request):
        """Delete user-defined Definition functions

        :param request: Request instance for DeleteCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataSources(self, request):
        """Delete Data Source

        :param request: Request instance for DeleteDataSources.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDataSourcesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDataSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataSources", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDsFolder(self, request):
        """Orchestration space - delete folders

        :param request: Request instance for DeleteDsFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDsFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDsFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDsFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDsFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFile(self, request):
        """Delete File

        :param request: Request instance for DeleteFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFilePath(self, request):
        """Development Space - Batch Delete Directories and Files

        :param request: Request instance for DeleteFilePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteFilePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteFilePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFilePath", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFilePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIntegrationNode(self, request):
        """Delete Integration Node

        :param request: Request instance for DeleteIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIntegrationTask(self, request):
        """Delete integration tasks

        :param request: Request instance for DeleteIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteOfflineTask(self, request):
        """Deleting task

        :param request: Request instance for DeleteOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjectParamDs(self, request):
        """Delete Project Parameters

        :param request: Request instance for DeleteProjectParamDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectParamDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectParamDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectParamDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectParamDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProjectUsers(self, request):
        """Delete Project Users

        :param request: Request instance for DeleteProjectUsers.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectUsersRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteProjectUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProjectUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProjectUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResource(self, request):
        """Remove resources in Resource Management

        :param request: Request instance for DeleteResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceFile(self, request):
        """Resource Management - Delete Resource File

        :param request: Request instance for DeleteResourceFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceFiles(self, request):
        """Resource Management-Batch Delete Resource Files

        :param request: Request instance for DeleteResourceFiles.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFilesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """Delete Quality Rule Interface

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRuleTemplate(self, request):
        """Deleting Rule Template

        :param request: Request instance for DeleteRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskAlarmRegular(self, request):
        """Delete Task Alert Rule

        :param request: Request instance for DeleteTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskDs(self, request):
        """Delete Orchestration Space Task

        :param request: Request instance for DeleteTaskDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskDs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkflowById(self, request):
        """Delete Workflow by Workflow Id

        :param request: Request instance for DeleteWorkflowById.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowByIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowById", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmEvents(self, request):
        """Alert event list

        :param request: Request instance for DescribeAlarmEvents.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmEventsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmReceiver(self, request):
        """Alert Recipient Details

        :param request: Request instance for DescribeAlarmReceiver.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmReceiverRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllByFolderNew(self, request):
        """Query all subfolders + workflows under the parent directory

        :param request: Request instance for DescribeAllByFolderNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAllByFolderNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAllByFolderNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllByFolderNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllByFolderNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApproveList(self, request):
        """Getting pending approval list

        :param request: Request instance for DescribeApproveList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApproveList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApproveListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApproveTypeList(self, request):
        """Get Approval Category List

        :param request: Request instance for DescribeApproveTypeList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveTypeListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeApproveTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApproveTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApproveTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBatchOperateTask(self, request):
        """Batch operation page to retrieve task list

        :param request: Request instance for DescribeBatchOperateTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeBatchOperateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeBatchOperateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBatchOperateTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBatchOperateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeColumnLineage(self, request):
        """List Field Lineage Information

        :param request: Request instance for DescribeColumnLineage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeColumnLineage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeColumnLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeColumnsMeta(self, request):
        """Query all column metadata of the table

        :param request: Request instance for DescribeColumnsMeta.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnsMetaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeColumnsMetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeColumnsMeta", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeColumnsMetaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataCheckStat(self, request):
        """Data Quality Overview Page Data Monitoring Interface

        :param request: Request instance for DescribeDataCheckStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataCheckStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataCheckStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataCheckStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataCheckStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceInfoList(self, request):
        """Obtain Data Source Information - Data Source Pagination List

        :param request: Request instance for DescribeDataSourceInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataSourceList(self, request):
        """Data Source Details

        :param request: Request instance for DescribeDataSourceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseInfoList(self, request):
        """Obtain Database Information

        :param request: Request instance for DescribeDatabaseInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseMetas(self, request):
        """Querying database list

        :param request: Request instance for DescribeDatabaseMetas.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseMetasRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseMetasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseMetas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseMetasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasource(self, request):
        """Data Source Details

        :param request: Request instance for DescribeDatasource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatasourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependOpsTasks(self, request):
        """Search for upstream/downstream task nodes by hierarchy

        :param request: Request instance for DescribeDependOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDependTaskLists(self, request):
        """Query Task Detail List by taskIds

        :param request: Request instance for DescribeDependTaskLists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTaskListsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTaskListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependTaskLists", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependTaskListsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDimensionScore(self, request):
        """Quality Report - Query Quality Score

        :param request: Request instance for DescribeDimensionScore.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDimensionScoreRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDimensionScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDimensionScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDimensionScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrInstancePage(self, request):
        """Paginated Query of Trial Run Instance List

        :param request: Request instance for DescribeDrInstancePage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDrInstancePageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDrInstancePageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrInstancePage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrInstancePageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsFolderTree(self, request):
        """Query Directory Tree

        :param request: Request instance for DescribeDsFolderTree.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsFolderTreeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsFolderTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsFolderTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsFolderTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDsParentFolderTree(self, request):
        """Query Parent Directory Tree, for Workflow, Task Localization

        :param request: Request instance for DescribeDsParentFolderTree.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDsParentFolderTreeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDsParentFolderTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDsParentFolderTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDsParentFolderTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEvent(self, request):
        """View Event Details by Project ID and Event Name

        :param request: Request instance for DescribeEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventCases(self, request):
        """Find Event Instances Based on Conditions

        :param request: Request instance for DescribeEventCases.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventCasesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventCasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventCases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventCasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventConsumeTasks(self, request):
        """Viewing consumption tasks of event instances

        :param request: Request instance for DescribeEventConsumeTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeEventConsumeTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeEventConsumeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventConsumeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventConsumeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExecStrategy(self, request):
        """Query Rule Group Execution Policy

        :param request: Request instance for DescribeExecStrategy.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeExecStrategyRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeExecStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExecStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFieldBasicInfo(self, request):
        """Metadata Model - Field Basic Information Query Interface

        :param request: Request instance for DescribeFieldBasicInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFieldBasicInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFieldBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFieldBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFieldBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFolderWorkflowList(self, request):
        """Get all workflow lists under the project by Project ID

        :param request: Request instance for DescribeFolderWorkflowList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFolderWorkflowList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFolderWorkflowListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionKinds(self, request):
        """Query Function Classification

        :param request: Request instance for DescribeFunctionKinds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionKindsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionKindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionKinds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionKindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFunctionTypes(self, request):
        """Query Function Type

        :param request: Request instance for DescribeFunctionTypes.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionTypesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceByCycle(self, request):
        """Query all instances by cycle type

        :param request: Request instance for DescribeInstanceByCycle.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceByCycleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceByCycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceByCycle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceByCycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLastLog(self, request):
        """Log Detail Acquisition Page

        :param request: Request instance for DescribeInstanceLastLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLastLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLastLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLastLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLastLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        """Get Instance List

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLog(self, request):
        """Get Instance Running Logs

        :param request: Request instance for DescribeInstanceLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogDetail(self, request):
        """Obtain Specific Instance-related Log Information

        :param request: Request instance for DescribeInstanceLogDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogFile(self, request):
        """Download Log File, Return Log Download URL

        :param request: Request instance for DescribeInstanceLogFile.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogFileRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLogList(self, request):
        """Offline Task Instance Run Log List

        :param request: Request instance for DescribeInstanceLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationNode(self, request):
        """Query integrated nodes

        :param request: Request instance for DescribeIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatistics(self, request):
        """DataInLong Dashboard Overview

        :param request: Request instance for DescribeIntegrationStatistics.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsInstanceTrend(self, request):
        """DataInLong dashboard instance status statistical trend

        :param request: Request instance for DescribeIntegrationStatisticsInstanceTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsInstanceTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsInstanceTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsInstanceTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsInstanceTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsRecordsTrend(self, request):
        """DataInLong Dashboard synchronization count trend

        :param request: Request instance for DescribeIntegrationStatisticsRecordsTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRecordsTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRecordsTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsRecordsTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsRecordsTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsTaskStatus(self, request):
        """DataInLong Dashboard Task Status Distribution Statistics

        :param request: Request instance for DescribeIntegrationStatisticsTaskStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationStatisticsTaskStatusTrend(self, request):
        """DataInLong Dashboard Task Status Statistical Trend

        :param request: Request instance for DescribeIntegrationStatisticsTaskStatusTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsTaskStatusTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsTaskStatusTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationTask(self, request):
        """Query integration tasks

        :param request: Request instance for DescribeIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationTasks(self, request):
        """Query Integration Task List

        :param request: Request instance for DescribeIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIntegrationVersionNodesInfo(self, request):
        """Query Integration Task Version Node Information

        :param request: Request instance for DescribeIntegrationVersionNodesInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationVersionNodesInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationVersionNodesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationVersionNodesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationVersionNodesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfflineTaskToken(self, request):
        """Getting long connection Token for offline tasks

        :param request: Request instance for DescribeOfflineTaskToken.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOfflineTaskTokenRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOfflineTaskTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineTaskToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineTaskTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOperateOpsTasks(self, request):
        """Task Operation and Maintenance List Combined Condition Query

        :param request: Request instance for DescribeOperateOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOperateOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOperateOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOperateOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsInstanceLogList(self, request):
        """Instance Operation and Maintenance - Get Instance Log List

        :param request: Request instance for DescribeOpsInstanceLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsInstanceLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsInstanceLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsInstanceLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsInstanceLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsMakePlanInstances(self, request):
        """Obtain the Supplementary Instance List based on the Supplementary Plan and Task.

        :param request: Request instance for DescribeOpsMakePlanInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsMakePlanInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsMakePlanInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsMakePlanTasks(self, request):
        """View Supplemental Plan Tasks

        :param request: Request instance for DescribeOpsMakePlanTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlanTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsMakePlanTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsMakePlanTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsMakePlans(self, request):
        """Paginated Query of Supplement Plan Based on Conditions

        :param request: Request instance for DescribeOpsMakePlans.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlansRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsMakePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsMakePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsMakePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpsWorkflows(self, request):
        """Querying User Production Workflow List

        :param request: Request instance for DescribeOpsWorkflows.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsWorkflowsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOpsWorkflowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpsWorkflows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpsWorkflowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrganizationalFunctions(self, request):
        """Query Full Functionality

        :param request: Request instance for DescribeOrganizationalFunctions.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOrganizationalFunctionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOrganizationalFunctionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationalFunctions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationalFunctionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProject(self, request):
        """Retrieving Project Information

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityScore(self, request):
        """Quality Report - Quality Score

        :param request: Request instance for DescribeQualityScore.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityScoreTrend(self, request):
        """Quality Report - Quality Score Periodic Trend

        :param request: Request instance for DescribeQualityScoreTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityScoreTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityScoreTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealTimeTaskInstanceNodeInfo(self, request):
        """Query Real-time Task Instance Node Information

        :param request: Request instance for DescribeRealTimeTaskInstanceNodeInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealTimeTaskMetricOverview(self, request):
        """Real-time Task Running Metrics Overview

        :param request: Request instance for DescribeRealTimeTaskMetricOverview.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskMetricOverviewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskMetricOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskMetricOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskMetricOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRealTimeTaskSpeed(self, request):
        """Real-time task synchronization speed trend

        :param request: Request instance for DescribeRealTimeTaskSpeed.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskSpeedRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskSpeedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskSpeed", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskSpeedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceManagePathTrees(self, request):
        """Retrieve resource management directory tree

        :param request: Request instance for DescribeResourceManagePathTrees.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeResourceManagePathTreesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeResourceManagePathTreesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceManagePathTrees", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceManagePathTreesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRule(self, request):
        """Queries rule details

        :param request: Request instance for DescribeRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleDimStat(self, request):
        """Data Quality Overview Page Triggers Dimension Distribution Statistics Interface

        :param request: Request instance for DescribeRuleDimStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDimStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDimStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleDimStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleDimStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecDetail(self, request):
        """Query Rule Execution Result Details

        :param request: Request instance for DescribeRuleExecDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecLog(self, request):
        """Rule Execution Log Query

        :param request: Request instance for DescribeRuleExecLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecResults(self, request):
        """Query Rule Execution Result List

        :param request: Request instance for DescribeRuleExecResults.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecResults", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleExecStat(self, request):
        """Data Quality Overview Page Rule Operation Interface

        :param request: Request instance for DescribeRuleExecStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroup(self, request):
        """Query Rule Group Details Interface

        :param request: Request instance for DescribeRuleGroup.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupExecResultsByPage(self, request):
        """Rule Group Execution Result Pagination Query Interface

        :param request: Request instance for DescribeRuleGroupExecResultsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupExecResultsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupExecResultsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupSubscription(self, request):
        """Query Rule Group Subscription Information

        :param request: Request instance for DescribeRuleGroupSubscription.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupSubscriptionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupTable(self, request):
        """Query Table Binding Execution Rule Group Information

        :param request: Request instance for DescribeRuleGroupTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleGroupsByPage(self, request):
        """[Filter Criteria]
        {Table Name (TableName), supports fuzzy matching}       {Table Owner (TableOwnerName), supports fuzzy matching}      {Monitoring Methods (MonitorTypes), 1. Not Configured 2. Linked to Production Scheduling 3. Offline Periodic Inspection, supports multiple selections}  {Subscriber (ReceiverUin)}
        [Required Fields]
        {Data Source (DatasourceId)}

        :param request: Request instance for DescribeRuleGroupsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTemplate(self, request):
        """Query Template Details

        :param request: Request instance for DescribeRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTemplates(self, request):
        """Viewing Rule Template List

        :param request: Request instance for DescribeRuleTemplates.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuleTemplatesByPage(self, request):
        """[Filter Conditions] {Template Name (Name), supports fuzzy matching} {Template Type (type), 1.System Template 2.Custom Definition Template} {Quality Detection Dimensions (QualityDims), 1.Accuracy 2.Uniqueness 3.Integrity 4.Consistency 5.Timeliness 6.Validity} [Sorting Field] {Citation Sorting Type (CitationOrderType), sort by citation count ASC DESC}

        :param request: Request instance for DescribeRuleTemplatesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplatesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplatesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        """Query Quality Rule List

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRulesByPage(self, request):
        """Paginated Query of Quality Rules

        :param request: Request instance for DescribeRulesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScheduleInstances(self, request):
        """Get Instance List

        :param request: Request instance for DescribeScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerInstanceStatus(self, request):
        """Operation and Maintenance Dashboard-Instance Status Distribution

        :param request: Request instance for DescribeSchedulerInstanceStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerInstanceStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerInstanceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerInstanceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerInstanceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerRunTimeInstanceCntByStatus(self, request):
        """Operation and Maintenance Dashboard - Instance Running Duration Ranking

        :param request: Request instance for DescribeSchedulerRunTimeInstanceCntByStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerRunTimeInstanceCntByStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerRunTimeInstanceCntByStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerRunTimeInstanceCntByStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerRunTimeInstanceCntByStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerTaskCntByStatus(self, request):
        """Task Status Statistics

        :param request: Request instance for DescribeSchedulerTaskCntByStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskCntByStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskCntByStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerTaskCntByStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerTaskCntByStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSchedulerTaskTypeCnt(self, request):
        """Operation and Maintenance Dashboard - Task Status Distribution

        :param request: Request instance for DescribeSchedulerTaskTypeCnt.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskTypeCntRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSchedulerTaskTypeCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSchedulerTaskTypeCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSchedulerTaskTypeCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStatisticInstanceStatusTrendOps(self, request):
        """Task Status Trend

        :param request: Request instance for DescribeStatisticInstanceStatusTrendOps.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeStatisticInstanceStatusTrendOpsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeStatisticInstanceStatusTrendOpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStatisticInstanceStatusTrendOps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStatisticInstanceStatusTrendOpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamTaskLogList(self, request):
        """Query real-time task log list

        :param request: Request instance for DescribeStreamTaskLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeStreamTaskLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeStreamTaskLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamTaskLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamTaskLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSuccessorOpsTaskInfos(self, request):
        """Get Downstream Task Information

        :param request: Request instance for DescribeSuccessorOpsTaskInfos.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeSuccessorOpsTaskInfosRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeSuccessorOpsTaskInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSuccessorOpsTaskInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSuccessorOpsTaskInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableBasicInfo(self, request):
        """Metadata Model-Table Basic Information Query Interface

        :param request: Request instance for DescribeTableBasicInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableBasicInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableInfoList(self, request):
        """Retrieve Data Table Information

        :param request: Request instance for DescribeTableInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableLineage(self, request):
        """List Table Lineage Information

        :param request: Request instance for DescribeTableLineage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableLineage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableLineageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableLineageInfo(self, request):
        """List Table Lineage Information

        :param request: Request instance for DescribeTableLineageInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableLineageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableLineageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableLineageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableMeta(self, request):
        """Querying Table Metadata Details

        :param request: Request instance for DescribeTableMeta.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableMeta", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableMetaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableMetas(self, request):
        """Get Table Metadata List

        :param request: Request instance for DescribeTableMetas.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetasRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableMetasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableMetas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableMetasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableQualityDetails(self, request):
        """Quality Report - Query Table Quality Details

        :param request: Request instance for DescribeTableQualityDetails.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableQualityDetailsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableQualityDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableQualityDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableQualityDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableSchemaInfo(self, request):
        """Retrieve Table Schema Information

        :param request: Request instance for DescribeTableSchemaInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableSchemaInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableSchemaInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableSchemaInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableSchemaInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableScoreTrend(self, request):
        """Query Table Score Trend

        :param request: Request instance for DescribeTableScoreTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableScoreTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableScoreTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableScoreTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableScoreTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskAlarmRegulations(self, request):
        """Query Task Alert Rule List

        :param request: Request instance for DescribeTaskAlarmRegulations.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskAlarmRegulationsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskAlarmRegulationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskAlarmRegulations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskAlarmRegulationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskByCycle(self, request):
        """Query all tasks by cycle type

        :param request: Request instance for DescribeTaskByCycle.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskByCycle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskByCycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskByCycleReport(self, request):
        """Task Status Cycle Growth Trend

        :param request: Request instance for DescribeTaskByCycleReport.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleReportRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByCycleReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskByCycleReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskByCycleReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskByStatusReport(self, request):
        """Task Status Trend

        :param request: Request instance for DescribeTaskByStatusReport.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByStatusReportRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskByStatusReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskByStatusReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskByStatusReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLockStatus(self, request):
        """View Task Lock Status Information

        :param request: Request instance for DescribeTaskLockStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLockStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLockStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLockStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLockStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskRunHistory(self, request):
        """Paging Query Task Execution History

        :param request: Request instance for DescribeTaskRunHistory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskRunHistoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskRunHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskRunHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskRunHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskScript(self, request):
        """Query Task Script

        :param request: Request instance for DescribeTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskScript", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateDimCount(self, request):
        """Query rule template dimension distribution

        :param request: Request instance for DescribeTemplateDimCount.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateDimCountRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateDimCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateDimCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateDimCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeThirdTaskRunLog(self, request):
        """Get third-party operation logs

        :param request: Request instance for DescribeThirdTaskRunLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeThirdTaskRunLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeThirdTaskRunLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeThirdTaskRunLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeThirdTaskRunLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopTableStat(self, request):
        """Data Quality Overview Page Table Ranking Interface

        :param request: Request instance for DescribeTopTableStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTopTableStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTopTableStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopTableStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopTableStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrendStat(self, request):
        """Data Quality Overview Page Trend Change Interface

        :param request: Request instance for DescribeTrendStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTrendStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTrendStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrendStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrendStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowCanvasInfo(self, request):
        """Query Workflow Canvas

        :param request: Request instance for DescribeWorkflowCanvasInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowCanvasInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowCanvasInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowCanvasInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowExecuteById(self, request):
        """Query Workflow Canvas Run Start and End Time

        :param request: Request instance for DescribeWorkflowExecuteById.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowExecuteByIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowExecuteByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowExecuteById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowExecuteByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowInfoById(self, request):
        """Query Workflow Details by Workflow ID

        :param request: Request instance for DescribeWorkflowInfoById.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowInfoByIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowInfoByIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowInfoById", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowInfoByIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowListByProjectId(self, request):
        """Get all workflow lists under the project by Project ID

        :param request: Request instance for DescribeWorkflowListByProjectId.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowListByProjectIdRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowListByProjectIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowListByProjectId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowListByProjectIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkflowTaskCount(self, request):
        """Query the number of workflow tasks

        :param request: Request instance for DescribeWorkflowTaskCount.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowTaskCountRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeWorkflowTaskCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkflowTaskCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkflowTaskCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DiagnosePro(self, request):
        """Instance diagnosis for diagnosing instances in INITIAL, DEPENDENCE, ALLOCATED, LAUNCHED, EVENT_LISTENING, BEFORE_ASPECT, EXPIRED, FAILED states

        :param request: Request instance for DiagnosePro.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DiagnoseProRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DiagnoseProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DiagnosePro", params, headers=headers)
            response = json.loads(body)
            model = models.DiagnoseProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DryRunDIOfflineTask(self, request):
        """Debug and Run Integration Task

        :param request: Request instance for DryRunDIOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DryRunDIOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DryRunDIOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DryRunDIOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.DryRunDIOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FindAllFolder(self, request):
        """Orchestration Space Bulk Operation Page Find All Folders

        :param request: Request instance for FindAllFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FindAllFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FindAllFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FindAllFolder", params, headers=headers)
            response = json.loads(body)
            model = models.FindAllFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeOpsTasks(self, request):
        """Task Operation and Maintenance - Bulk Pause Tasks

        :param request: Request instance for FreezeOpsTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeOpsTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeOpsTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeOpsTasks", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeOpsTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeTasksByWorkflowIds(self, request):
        """Pause All Tasks Under Workflow

        :param request: Request instance for FreezeTasksByWorkflowIds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByWorkflowIdsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByWorkflowIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasksByWorkflowIds", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeTasksByWorkflowIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenHiveTableDDLSql(self, request):
        """Generate SQL for Creating Hive Table

        :param request: Request instance for GenHiveTableDDLSql.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GenHiveTableDDLSqlRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GenHiveTableDDLSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenHiveTableDDLSql", params, headers=headers)
            response = json.loads(body)
            model = models.GenHiveTableDDLSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFileInfo(self, request):
        """Development Space - Obtain data development script information

        :param request: Request instance for GetFileInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetFileInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetFileInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFileInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetFileInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetIntegrationNodeColumnSchema(self, request):
        """Extracting DataInLong Node Field Schema

        :param request: Request instance for GetIntegrationNodeColumnSchema.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetIntegrationNodeColumnSchemaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetIntegrationNodeColumnSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetIntegrationNodeColumnSchema", params, headers=headers)
            response = json.loads(body)
            model = models.GetIntegrationNodeColumnSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOfflineDIInstanceList(self, request):
        """Get Offline Task Instance List (New)

        :param request: Request instance for GetOfflineDIInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetOfflineDIInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetOfflineDIInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOfflineDIInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetOfflineDIInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOfflineInstanceList(self, request):
        """Obtain Offline Task Instances

        :param request: Request instance for GetOfflineInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetOfflineInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetOfflineInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOfflineInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetOfflineInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillOpsMakePlanInstances(self, request):
        """Batch Termination of Instances by Supplement Plan.

        :param request: Request instance for KillOpsMakePlanInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillOpsMakePlanInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillOpsMakePlanInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillOpsMakePlanInstances", params, headers=headers)
            response = json.loads(body)
            model = models.KillOpsMakePlanInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillScheduleInstances(self, request):
        """Batch Termination of Instances

        :param request: Request instance for KillScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.KillScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LockIntegrationTask(self, request):
        """Lock Integration Task

        :param request: Request instance for LockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.LockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.LockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.LockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApproveStatus(self, request):
        """Modify Approval Form Status

        :param request: Request instance for ModifyApproveStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyApproveStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyApproveStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApproveStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApproveStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataSource(self, request):
        """Modify Data Source

        :param request: Request instance for ModifyDataSource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDimensionWeight(self, request):
        """Quality Report - Modify Dimension Permissions

        :param request: Request instance for ModifyDimensionWeight.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDimensionWeightRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDimensionWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDimensionWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDimensionWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDsFolder(self, request):
        """Data Development Module - Folder Update

        :param request: Request instance for ModifyDsFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDsFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDsFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDsFolder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDsFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExecStrategy(self, request):
        """Update Rule Group Execution Strategy

        :param request: Request instance for ModifyExecStrategy.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyExecStrategyRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyExecStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExecStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExecStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIntegrationNode(self, request):
        """Updating Integrated Nodes

        :param request: Request instance for ModifyIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIntegrationTask(self, request):
        """Update Integration Task

        :param request: Request instance for ModifyIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMonitorStatus(self, request):
        """Update Monitoring Status

        :param request: Request instance for ModifyMonitorStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyMonitorStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyMonitorStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMonitorStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMonitorStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        """Update Quality Rule Interface

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRuleGroupSubscription(self, request):
        """Update Rule Group Subscription Information

        :param request: Request instance for ModifyRuleGroupSubscription.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleGroupSubscriptionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleGroupSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleGroupSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleGroupSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRuleTemplate(self, request):
        """Edit Rule Template

        :param request: Request instance for ModifyRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskAlarmRegular(self, request):
        """Modify task alert rules

        :param request: Request instance for ModifyTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskInfo(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Update Task

        :param request: Request instance for ModifyTaskInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskLinks(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Add Parent Task Dependency

        :param request: Request instance for ModifyTaskLinks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskLinks", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskLinksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskName(self, request):
        """Rename Task (Task Editing)

        :param request: Request instance for ModifyTaskName.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskNameRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskScript(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Modify Task Script

        :param request: Request instance for ModifyTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskScript", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkflowInfo(self, request):
        """Update Workflow Information

        :param request: Request instance for ModifyWorkflowInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkflowInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkflowSchedule(self, request):
        """Update Workflow Scheduling

        :param request: Request instance for ModifyWorkflowSchedule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkflowScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MoveTasksToFolder(self, request):
        """Orchestration Space - Workflow - Move Task to Workflow Folder

        :param request: Request instance for MoveTasksToFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MoveTasksToFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MoveTasksToFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MoveTasksToFolder", params, headers=headers)
            response = json.loads(body)
            model = models.MoveTasksToFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterEvent(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Registration Event

        :param request: Request instance for RegisterEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEvent", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterEventListener(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Register Event Listener

        :param request: Request instance for RegisterEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEventListener", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterEventListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveWorkflowDs(self, request):
        """Delete orchestration space workflow

        :param request: Request instance for RemoveWorkflowDs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RemoveWorkflowDsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RemoveWorkflowDsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveWorkflowDs", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveWorkflowDsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeIntegrationTask(self, request):
        """Continue Integration Task

        :param request: Request instance for ResumeIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ResumeIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ResumeIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RobAndLockIntegrationTask(self, request):
        """Preemptive locking of integration tasks

        :param request: Request instance for RobAndLockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RobAndLockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RobAndLockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RobAndLockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.RobAndLockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunForceSucScheduleInstances(self, request):
        """Instance Batch Successfully Configured

        :param request: Request instance for RunForceSucScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunForceSucScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunForceSucScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunForceSucScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunForceSucScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunRerunScheduleInstances(self, request):
        """Instance Batch Rerun

        :param request: Request instance for RunRerunScheduleInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunRerunScheduleInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunRerunScheduleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunRerunScheduleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunRerunScheduleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunTasksByMultiWorkflow(self, request):
        """Batch startup of workflows

        :param request: Request instance for RunTasksByMultiWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunTasksByMultiWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunTasksByMultiWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunTasksByMultiWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.RunTasksByMultiWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SaveCustomFunction(self, request):
        """Save User-Defined Function

        :param request: Request instance for SaveCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SaveCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SaveCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.SaveCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTaskAlarmNew(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Set Task Alerts, Create/Update Alert Information (Latest)

        :param request: Request instance for SetTaskAlarmNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTaskAlarmNew", params, headers=headers)
            response = json.loads(body)
            model = models.SetTaskAlarmNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartIntegrationTask(self, request):
        """Initiate Integration Task

        :param request: Request instance for StartIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StartIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StartIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StartIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopIntegrationTask(self, request):
        """Stop Integration Task

        :param request: Request instance for StopIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StopIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StopIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitCustomFunction(self, request):
        """Submit Custom Definition Function

        :param request: Request instance for SubmitCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitSqlTask(self, request):
        """Ad Hoc Analysis - Submit SQL Task

        :param request: Request instance for SubmitSqlTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitSqlTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitSqlTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitSqlTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitSqlTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTask(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Submit a Task

        :param request: Request instance for SubmitTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTaskTestRun(self, request):
        """No

        :param request: Request instance for SubmitTaskTestRun.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskTestRunRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskTestRunResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTaskTestRun", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTaskTestRunResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitWorkflow(self, request):
        """Submit Workflow

        :param request: Request instance for SubmitWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SuspendIntegrationTask(self, request):
        """Pause Integration Task

        :param request: Request instance for SuspendIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SuspendIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SuspendIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SuspendIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.SuspendIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TaskLog(self, request):
        """Query Inlong Manager Logs

        :param request: Request instance for TaskLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TaskLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TaskLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TaskLog", params, headers=headers)
            response = json.loads(body)
            model = models.TaskLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerDsEvent(self, request):
        """Event Management - Triggered Events

        :param request: Request instance for TriggerDsEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TriggerDsEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TriggerDsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerDsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerDsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerEvent(self, request):
        """<p style="color:red;">[Note: This version is only available to a portion of allowlist customers in the Guangzhou Region]</p>
        Trigger events

        :param request: Request instance for TriggerEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TriggerEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TriggerEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerEvent", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnlockIntegrationTask(self, request):
        """Unlock Integration Task

        :param request: Request instance for UnlockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UnlockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UnlockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.UnlockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateWorkflowOwner(self, request):
        """Modifying Workflow Person in Charge

        :param request: Request instance for UpdateWorkflowOwner.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateWorkflowOwnerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateWorkflowOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateWorkflowOwner", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateWorkflowOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadContent(self, request):
        """Save Task Information

        :param request: Request instance for UploadContent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UploadContentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UploadContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadContent", params, headers=headers)
            response = json.loads(body)
            model = models.UploadContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))