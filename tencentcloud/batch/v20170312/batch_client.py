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
from tencentcloud.batch.v20170312 import models


class BatchClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'batch.tencentcloudapi.com'
    _service = 'batch'


    def AttachInstances(self, request):
        """This API is used to add existing instances to the compute environment.
        Requirements: <br/>
        1. The instance is not in the batch compute system.<br/>
        2. The instance is in “Running” status.<br/>
        3. Spot instances are not supported.<b/>

        For instances added to the compute environment, their UserData will be reset, and the operating systems will be reinstalled.

        :param request: Request instance for AttachInstances.
        :type request: :class:`tencentcloud.batch.v20170312.models.AttachInstancesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.AttachInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateComputeEnv(self, request):
        """This API is used to create a compute environment.

        :param request: Request instance for CreateComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskTemplate(self, request):
        """This API is used to create a task template.

        :param request: Request instance for CreateTaskTemplate.
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteComputeEnv(self, request):
        """This API is used to delete a compute environment.

        :param request: Request instance for DeleteComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJob(self, request):
        """This API is used to delete a job.
        When a job is deleted, all related information is deleted and the job cannot be queried.
        To delete a job, the job and all its task instances must be in SUCCEED or FAILED status.

        :param request: Request instance for DeleteJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJob", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTaskTemplates(self, request):
        """This API is used to delete task template information.

        :param request: Request instance for DeleteTaskTemplates.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableCvmInstanceTypes(self, request):
        """This API is used to view the information of available CVM model configurations.

        :param request: Request instance for DescribeAvailableCvmInstanceTypes.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableCvmInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableCvmInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComputeEnv(self, request):
        """This API is used to query compute environment details.

        :param request: Request instance for DescribeComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComputeEnvActivities(self, request):
        """This API is used to query the information of activities in the compute environment.

        :param request: Request instance for DescribeComputeEnvActivities.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvActivities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvActivitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComputeEnvCreateInfo(self, request):
        """This API is used to query the compute environment creation information.

        :param request: Request instance for DescribeComputeEnvCreateInfo.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvCreateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvCreateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComputeEnvCreateInfos(self, request):
        """This API is used to view the list of information of compute environment creation, including name, description, type, environment parameters, notifications, and number of desired nodes.

        :param request: Request instance for DescribeComputeEnvCreateInfos.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvCreateInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvCreateInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComputeEnvs(self, request):
        """This API is used to get the list of compute environments.

        :param request: Request instance for DescribeComputeEnvs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComputeEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComputeEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCvmZoneInstanceConfigInfos(self, request):
        """This API is used to get the model configuration information of the availability zone of BatchCompute.

        :param request: Request instance for DescribeCvmZoneInstanceConfigInfos.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCvmZoneInstanceConfigInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCvmZoneInstanceConfigInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceCategories(self, request):
        """Currently, CVM instance families are classified into different category, and each category contains several instance families. This API is used to query the instance category information.

        :param request: Request instance for DescribeInstanceCategories.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceCategories", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceCategoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJob(self, request):
        """This API is used to query the details of a job, including internal task (`Task`) and dependency (`Dependence`) information.

        :param request: Request instance for DescribeJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobSubmitInfo(self, request):
        """This API is used to query the submission information of the specified job, with the return including the job submission information used as input parameters in the JobId and SubmitJob APIs.

        :param request: Request instance for DescribeJobSubmitInfo.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobSubmitInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobSubmitInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobs(self, request):
        """This API is used to query the overview information of several jobs.

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTask(self, request):
        """This API is used to query the details of a specified task, including information of the task instances inside the task.

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLogs(self, request):
        """This API is used to get the standard outputs and standard error logs of multiple task instances.

        :param request: Request instance for DescribeTaskLogs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskTemplates(self, request):
        """This API is used to query the information of task templates.

        :param request: Request instance for DescribeTaskTemplates.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachInstances(self, request):
        """This API is used to remove instances that from compute environment.

        :param request: Request instance for DetachInstances.
        :type request: :class:`tencentcloud.batch.v20170312.models.DetachInstancesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DetachInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyComputeEnv(self, request):
        """This API is used to modify the attributes of a compute environment.

        :param request: Request instance for ModifyComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyComputeEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyComputeEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskTemplate(self, request):
        """This API is used to modify a task template.

        :param request: Request instance for ModifyTaskTemplate.
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryJobs(self, request):
        """This API is used to retry the failed task instances in a job.
        Job retry is supported only if a job is in the "FAILED" state. After the retry operation succeeds, the job will retry the failing task instances in each task in turn according to the task dependencies specified in the "DAG". The history information of the task instances will be reset, the instances will participate in subsequent scheduling and execution as if they are run for the first time.

        :param request: Request instance for RetryJobs.
        :type request: :class:`tencentcloud.batch.v20170312.models.RetryJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.RetryJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryJobs", params, headers=headers)
            response = json.loads(body)
            model = models.RetryJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateComputeNode(self, request):
        """This API is used to terminate a compute node.
        Termination is allowed for nodes in the CREATED, CREATION_FAILED, RUNNING or ABNORMAL state.

        :param request: Request instance for TerminateComputeNode.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateComputeNode", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateComputeNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateComputeNodes(self, request):
        """This API is used to terminate compute nodes in batches. It is not allowed to repeatedly terminate the same node.

        :param request: Request instance for TerminateComputeNodes.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateComputeNodes", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateComputeNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateJob(self, request):
        """This API is used to terminate a job.
        Termination is prohibited if a job is in the `SUBMITTED` state and does not take effect if it is in the `SUCCEED` state.
        Job termination is an asynchronous process, and the time it takes to complete the entire process is directly proportional to the total number of tasks. The effect of terminating a job is equivalent to performing the TerminateTaskInstance operation on all the task instances contained in the job. For more information on the specific effect and usage, see TerminateTaskInstance.

        :param request: Request instance for TerminateJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateJob", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateTaskInstance(self, request):
        """This API is used to terminate a task instance.
        `SUCCEED` and `FAILED` task instances: No action
        `SUBMITTED`, `PENDING`, and `RUNNABLE` task instances: Change status to `FAILED`.
        `STARTING`, `RUNNING` and `FAILED_INTERRUPTED` task instances: If `EnvId` is not specified, the CVM instance is terminated, and then the task status goes to `FAILED`. If `EnvId` is specified, the task instance changes to `FAILED`, then the related CVM instance is restarted.
        `FAILED_INTERRUPTED` task instances: The related resources and quotas will be released only after the termination actually succeeds.

        :param request: Request instance for TerminateTaskInstance.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))