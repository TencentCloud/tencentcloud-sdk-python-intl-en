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
from tencentcloud.batch.v20170312 import models
from typing import Dict


class BatchClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'batch.intl.tencentcloudapi.com'
    _service = 'batch'

    async def AttachInstances(
            self,
            request: models.AttachInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachInstancesResponse:
        """
        This API is used to add existing instances to the compute environment.
        Requirements: <br/>
        1. The instance is not in the batch compute system.<br/>
        2. The instance is in “Running” status.<br/>
        3. Spot instances are not supported.<b/>

        For instances added to the compute environment, their UserData will be reset, and the operating systems will be reinstalled.
        """
        
        kwargs = {}
        kwargs["action"] = "AttachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateComputeEnv(
            self,
            request: models.CreateComputeEnvRequest,
            opts: Dict = None,
    ) -> models.CreateComputeEnvResponse:
        """
        This API is used to create a compute environment.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskTemplate(
            self,
            request: models.CreateTaskTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTaskTemplateResponse:
        """
        This API is used to create a task template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteComputeEnv(
            self,
            request: models.DeleteComputeEnvRequest,
            opts: Dict = None,
    ) -> models.DeleteComputeEnvResponse:
        """
        This API is used to delete a compute environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJob(
            self,
            request: models.DeleteJobRequest,
            opts: Dict = None,
    ) -> models.DeleteJobResponse:
        """
        This API is used to delete a job.
        When a job is deleted, all related information is deleted and the job cannot be queried.
        To delete a job, the job and all its task instances must be in SUCCEED or FAILED status.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTaskTemplates(
            self,
            request: models.DeleteTaskTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskTemplatesResponse:
        """
        This API is used to delete task template information.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableCvmInstanceTypes(
            self,
            request: models.DescribeAvailableCvmInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableCvmInstanceTypesResponse:
        """
        This API is used to view the information of available CVM model configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableCvmInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableCvmInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnv(
            self,
            request: models.DescribeComputeEnvRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvResponse:
        """
        This API is used to query compute environment details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvActivities(
            self,
            request: models.DescribeComputeEnvActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvActivitiesResponse:
        """
        This API is used to query the information of activities in the compute environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvCreateInfo(
            self,
            request: models.DescribeComputeEnvCreateInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvCreateInfoResponse:
        """
        This API is used to query the compute environment creation information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvCreateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvCreateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvCreateInfos(
            self,
            request: models.DescribeComputeEnvCreateInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvCreateInfosResponse:
        """
        This API is used to view the list of information of compute environment creation, including name, description, type, environment parameters, notifications, and number of desired nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvCreateInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvCreateInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeComputeEnvs(
            self,
            request: models.DescribeComputeEnvsRequest,
            opts: Dict = None,
    ) -> models.DescribeComputeEnvsResponse:
        """
        This API is used to get the list of compute environments.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeComputeEnvs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeComputeEnvsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCvmZoneInstanceConfigInfos(
            self,
            request: models.DescribeCvmZoneInstanceConfigInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeCvmZoneInstanceConfigInfosResponse:
        """
        This API is used to get the model configuration information of the availability zone of BatchCompute.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCvmZoneInstanceConfigInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCvmZoneInstanceConfigInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceCategories(
            self,
            request: models.DescribeInstanceCategoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceCategoriesResponse:
        """
        Currently, CVM instance families are classified into different category, and each category contains several instance families. This API is used to query the instance category information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceCategories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceCategoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJob(
            self,
            request: models.DescribeJobRequest,
            opts: Dict = None,
    ) -> models.DescribeJobResponse:
        """
        This API is used to query the details of a job, including internal task (`Task`) and dependency (`Dependence`) information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobSubmitInfo(
            self,
            request: models.DescribeJobSubmitInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJobSubmitInfoResponse:
        """
        This API is used to query the submission information of the specified job, with the return including the job submission information used as input parameters in the JobId and SubmitJob APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobSubmitInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobSubmitInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        This API is used to query the overview information of several jobs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTask(
            self,
            request: models.DescribeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResponse:
        """
        This API is used to query the details of a specified task, including information of the task instances inside the task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLogs(
            self,
            request: models.DescribeTaskLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogsResponse:
        """
        This API is used to get the standard outputs and standard error logs of multiple task instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskTemplates(
            self,
            request: models.DescribeTaskTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskTemplatesResponse:
        """
        This API is used to query the information of task templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachInstances(
            self,
            request: models.DetachInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachInstancesResponse:
        """
        This API is used to remove instances that from compute environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyComputeEnv(
            self,
            request: models.ModifyComputeEnvRequest,
            opts: Dict = None,
    ) -> models.ModifyComputeEnvResponse:
        """
        This API is used to modify the attributes of a compute environment.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyComputeEnv"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyComputeEnvResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskTemplate(
            self,
            request: models.ModifyTaskTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskTemplateResponse:
        """
        This API is used to modify a task template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryJobs(
            self,
            request: models.RetryJobsRequest,
            opts: Dict = None,
    ) -> models.RetryJobsResponse:
        """
        This API is used to retry the failed task instances in a job.
        Job retry is supported only if a job is in the "FAILED" state. After the retry operation succeeds, the job will retry the failing task instances in each task in turn according to the task dependencies specified in the "DAG". The history information of the task instances will be reset, the instances will participate in subsequent scheduling and execution as if they are run for the first time.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateComputeNode(
            self,
            request: models.TerminateComputeNodeRequest,
            opts: Dict = None,
    ) -> models.TerminateComputeNodeResponse:
        """
        This API is used to terminate a compute node.
        Termination is allowed for nodes in the CREATED, CREATION_FAILED, RUNNING or ABNORMAL state.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateComputeNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateComputeNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateComputeNodes(
            self,
            request: models.TerminateComputeNodesRequest,
            opts: Dict = None,
    ) -> models.TerminateComputeNodesResponse:
        """
        This API is used to terminate compute nodes in batches. It is not allowed to repeatedly terminate the same node.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateComputeNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateComputeNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateJob(
            self,
            request: models.TerminateJobRequest,
            opts: Dict = None,
    ) -> models.TerminateJobResponse:
        """
        This API is used to terminate a job.
        Termination is prohibited if a job is in the `SUBMITTED` state and does not take effect if it is in the `SUCCEED` state.
        Job termination is an asynchronous process, and the time it takes to complete the entire process is directly proportional to the total number of tasks. The effect of terminating a job is equivalent to performing the TerminateTaskInstance operation on all the task instances contained in the job. For more information on the specific effect and usage, see TerminateTaskInstance.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateTaskInstance(
            self,
            request: models.TerminateTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateTaskInstanceResponse:
        """
        This API is used to terminate a task instance.
        `SUCCEED` and `FAILED` task instances: No action
        `SUBMITTED`, `PENDING`, and `RUNNABLE` task instances: Change status to `FAILED`.
        `STARTING`, `RUNNING` and `FAILED_INTERRUPTED` task instances: If `EnvId` is not specified, the CVM instance is terminated, and then the task status goes to `FAILED`. If `EnvId` is specified, the task instance changes to `FAILED`, then the related CVM instance is restarted.
        `FAILED_INTERRUPTED` task instances: The related resources and quotas will be released only after the termination actually succeeds.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)