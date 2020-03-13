# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def AttachInstances(self, request):
        """This API is used to add existing instances to the compute environment.
        Considerations: <br/>
        1. The instance should not be in the batch compute system.<br/>
        2. The instance status should be “running”.<br/>
        3. It supports dedicated CVMs and pay-as-you-go instances that billed on an hourly basis. Spot instances are not supported.<b/>

        For instances added to the compute environment, their UserData will be reset and the operating systems will be reinstalled.

        :param request: Request instance for AttachInstances.
        :type request: :class:`tencentcloud.batch.v20170312.models.AttachInstancesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.AttachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachInstancesResponse()
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


    def CreateComputeEnv(self, request):
        """This API is used to create a compute environment.

        :param request: Request instance for CreateComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateComputeEnvResponse()
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


    def CreateTaskTemplate(self, request):
        """This API is used to create a task template.

        :param request: Request instance for CreateTaskTemplate.
        :type request: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.CreateTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTaskTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskTemplateResponse()
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


    def DeleteComputeEnv(self, request):
        """This API is used to delete a compute environment.

        :param request: Request instance for DeleteComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteComputeEnvResponse()
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


    def DeleteJob(self, request):
        """This API is used to delete a job.
        Deleting a job is equivalent to deleting all the information related to the job. After successful deletion, all information related to the job cannot be queried.
        The job to be deleted must be in a completed state, and all task instances contained in it must also be in a completed state; otherwise, the operation will be prohibited. The completed state can be either SUCCEED or FAILED.

        :param request: Request instance for DeleteJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteJobResponse()
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


    def DeleteTaskTemplates(self, request):
        """This API is used to delete task template information.

        :param request: Request instance for DeleteTaskTemplates.
        :type request: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DeleteTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTaskTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTaskTemplatesResponse()
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


    def DescribeAvailableCvmInstanceTypes(self, request):
        """This API is used to view the information of available CVM model configurations.

        :param request: Request instance for DescribeAvailableCvmInstanceTypes.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAvailableCvmInstanceTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableCvmInstanceTypesResponse()
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


    def DescribeComputeEnv(self, request):
        """This API is used to query compute environment details.

        :param request: Request instance for DescribeComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvResponse()
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


    def DescribeComputeEnvActivities(self, request):
        """This API is used to query the information of activities in the compute environment.

        :param request: Request instance for DescribeComputeEnvActivities.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvActivitiesResponse()
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


    def DescribeComputeEnvCreateInfo(self, request):
        """Views compute environment creation information.

        :param request: Request instance for DescribeComputeEnvCreateInfo.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvCreateInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvCreateInfoResponse()
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


    def DescribeComputeEnvCreateInfos(self, request):
        """This API is used to view the list of information of compute environment creation, including name, description, type, environment parameters, notifications, and number of desired nodes.

        :param request: Request instance for DescribeComputeEnvCreateInfos.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvCreateInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvCreateInfosResponse()
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


    def DescribeComputeEnvs(self, request):
        """This API is used to view the list of compute environments.

        :param request: Request instance for DescribeComputeEnvs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeComputeEnvsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvsResponse()
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


    def DescribeCvmZoneInstanceConfigInfos(self, request):
        """This API is used to get the model configuration information of the availability zone of BatchCompute.

        :param request: Request instance for DescribeCvmZoneInstanceConfigInfos.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCvmZoneInstanceConfigInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCvmZoneInstanceConfigInfosResponse()
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


    def DescribeInstanceCategories(self, request):
        """Currently, CVM instance families are classified into different category, and each category contains several instance families. This API is used to query the instance category information.

        :param request: Request instance for DescribeInstanceCategories.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceCategories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceCategoriesResponse()
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


    def DescribeJob(self, request):
        """This API is used to view the details of a job, including internal task (Task) and dependency (Dependence) information.

        :param request: Request instance for DescribeJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobResponse()
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


    def DescribeJobSubmitInfo(self, request):
        """This API is used to query the submission information of the specified job, with the return including the job submission information used as input parameters in the JobId and SubmitJob APIs.

        :param request: Request instance for DescribeJobSubmitInfo.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobSubmitInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJobSubmitInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobSubmitInfoResponse()
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


    def DescribeJobs(self, request):
        """This API is used to query the overview information of several instances.

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobsResponse()
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


    def DescribeTask(self, request):
        """This API is used to query the details of a specified task, including information of the task instances inside the task.

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
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


    def DescribeTaskLogs(self, request):
        """This API is used to get the standard outputs and standard error logs of multiple task instances.

        :param request: Request instance for DescribeTaskLogs.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskLogsResponse()
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


    def DescribeTaskTemplates(self, request):
        """This API is used to query the information of task templates.

        :param request: Request instance for DescribeTaskTemplates.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskTemplatesResponse()
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


    def DetachInstances(self, request):
        """This API is used to remove instances that from compute environment.

        :param request: Request instance for DetachInstances.
        :type request: :class:`tencentcloud.batch.v20170312.models.DetachInstancesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DetachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachInstancesResponse()
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


    def ModifyComputeEnv(self, request):
        """This API is used to modify the attributes of a compute environment.

        :param request: Request instance for ModifyComputeEnv.
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyComputeEnvResponse()
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


    def ModifyTaskTemplate(self, request):
        """This API is used to modify a task template.

        :param request: Request instance for ModifyTaskTemplate.
        :type request: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.ModifyTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTaskTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskTemplateResponse()
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


    def RetryJobs(self, request):
        """This API is used to retry the failing task instance in instances.
        Job retry is supported only if a job is in the "FAILED" state. After the retry operation succeeds, the instance will retry the failing task instances in each task in turn according to the task dependencies specified in the "DAG". The history information of the task instances will be reset, the instances will participate in subsequent scheduling and execution as if they are run for the first time.

        :param request: Request instance for RetryJobs.
        :type request: :class:`tencentcloud.batch.v20170312.models.RetryJobsRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.RetryJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RetryJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RetryJobsResponse()
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


    def SubmitJob(self, request):
        """This API is used to submit a instance.

        :param request: Request instance for SubmitJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.SubmitJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.SubmitJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitJobResponse()
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


    def TerminateComputeNode(self, request):
        """This API is used to terminate a compute node.
        Termination is allowed for nodes in the CREATED, CREATION_FAILED, RUNNING or ABNORMAL state.

        :param request: Request instance for TerminateComputeNode.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateComputeNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateComputeNodeResponse()
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


    def TerminateComputeNodes(self, request):
        """This API is used to terminate compute nodes in batches. It is not allowed to repeatedly terminate the same node.

        :param request: Request instance for TerminateComputeNodes.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateComputeNodesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateComputeNodes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateComputeNodesResponse()
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


    def TerminateJob(self, request):
        """This API is used to terminate an instance.
        Termination is prohibited if an instance is in the "SUBMITTED" state and does not take effect if it is in the "SUCCEED" state.
        Instance termination is an asynchronous process, and the time it takes to complete the entire process is directly proportional to the total number of tasks. The effect of terminating an instance is equivalent to performing the TerminateTaskInstance operation on all the task instances contained in the job. For more information on the specific effect and usage, see TerminateTaskInstance.

        :param request: Request instance for TerminateJob.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateJobRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateJobResponse()
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


    def TerminateTaskInstance(self, request):
        """This API is used to terminate a task instance.
        Task instances in the "SUCCEED" or "FAILED" state will not be processed.
        Task instances in the "SUBMITTED", "PENDING", or "RUNNABLE" state will be set to the "FAILED" state.
        For task instances in the "STARTING", "RUNNING", or "FAILED_INTERRUPTED" state, there will be two cases: if no compute environment is specified, the CVM instance will be terminated first, and then the state will be set to "FAILED"; if a compute environment's EnvId is specified, the state of the task instances will be set to "FAILED" first, and then the CVM instance that performs the task will be restarted. Both cases takes a certain amount of time to be completed.
        For task instances in the "FAILED_INTERRUPTED" state, the related resources and quotas will be released only after the termination actually succeeds.

        :param request: Request instance for TerminateTaskInstance.
        :type request: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.TerminateTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateTaskInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateTaskInstanceResponse()
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