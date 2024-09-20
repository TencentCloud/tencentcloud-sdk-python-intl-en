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
from tencentcloud.cfg.v20210820 import models


class CfgClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'cfg.tencentcloudapi.com'
    _service = 'cfg'


    def CreateTaskFromAction(self, request):
        """This API is used to create an experiment with an action.

        :param request: Request instance for CreateTaskFromAction.
        :type request: :class:`tencentcloud.cfg.v20210820.models.CreateTaskFromActionRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.CreateTaskFromActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFromAction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFromActionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTaskFromTemplate(self, request):
        """This API is used to create an experiment using a template.

        :param request: Request instance for CreateTaskFromTemplate.
        :type request: :class:`tencentcloud.cfg.v20210820.models.CreateTaskFromTemplateRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.CreateTaskFromTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskFromTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskFromTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTask(self, request):
        """This API is used to delete a task.

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeActionFieldConfigList(self, request):
        """This API is used to obtain the dynamic configuration parameters of the action field based on action ID, including action-specific parameters and common parameters.

        :param request: Request instance for DescribeActionFieldConfigList.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeActionFieldConfigListRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeActionFieldConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeActionFieldConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeActionFieldConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeActionLibraryList(self, request):
        """This API is used to obtain the action list of Chaotic Fault Generator.

        :param request: Request instance for DescribeActionLibraryList.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeActionLibraryListRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeActionLibraryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeActionLibraryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeActionLibraryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeObjectTypeList(self, request):
        """This API is used to query the object type list.

        :param request: Request instance for DescribeObjectTypeList.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeObjectTypeListRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeObjectTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeObjectTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeObjectTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTask(self, request):
        """This API is used to query a task.

        :param request: Request instance for DescribeTask.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskResponse`

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


    def DescribeTaskExecuteLogs(self, request):
        """This API is used to obtain all logs generated during an experiment.

        :param request: Request instance for DescribeTaskExecuteLogs.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskExecuteLogsRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskExecuteLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskExecuteLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskExecuteLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskList(self, request):
        """This API is used to query the task list.

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskListRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskPolicyTriggerLog(self, request):
        """This API is used to obtain the guardrail triggering logs.

        :param request: Request instance for DescribeTaskPolicyTriggerLog.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskPolicyTriggerLogRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTaskPolicyTriggerLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskPolicyTriggerLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskPolicyTriggerLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplate(self, request):
        """This API is used to query a template library.

        :param request: Request instance for DescribeTemplate.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateList(self, request):
        """This API is used to query the template list.

        :param request: Request instance for DescribeTemplateList.
        :type request: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateListRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.DescribeTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteTask(self, request):
        """This API is used to run a task.

        :param request: Request instance for ExecuteTask.
        :type request: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteTask", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExecuteTaskInstance(self, request):
        """This API is used to trigger the action of the chaos engineering experiment and perform an experiment on the instance.

        :param request: Request instance for ExecuteTaskInstance.
        :type request: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskInstanceRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ExecuteTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExecuteTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ExecuteTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTaskRunStatus(self, request):
        """This API is used to change the task running status.

        :param request: Request instance for ModifyTaskRunStatus.
        :type request: :class:`tencentcloud.cfg.v20210820.models.ModifyTaskRunStatusRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.ModifyTaskRunStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskRunStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskRunStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TriggerPolicy(self, request):
        """This API is used to trigger the chaos engineering experiment guardrail (two types: trigger and recovery).

        :param request: Request instance for TriggerPolicy.
        :type request: :class:`tencentcloud.cfg.v20210820.models.TriggerPolicyRequest`
        :rtype: :class:`tencentcloud.cfg.v20210820.models.TriggerPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))