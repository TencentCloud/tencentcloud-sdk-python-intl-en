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
from tencentcloud.tat.v20201028 import models


class TatClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'tat.tencentcloudapi.com'
    _service = 'tat'


    def CancelInvocation(self, request):
        """This API is used to cancel the command executed on one or more CVM instances.

        * If the command has not been delivered to the TAT agent, the task status is `PENDING`, `DELIVERING`, or `DELIVER_DELAYED`, and will be `CANCELLED` after the command is canceled.
        * If the command has been delivered to the TAT agent, the task status is `RUNNING`, and will be `TERMINATED` after the command is canceled.

        :param request: Request instance for CancelInvocation.
        :type request: :class:`tencentcloud.tat.v20201028.models.CancelInvocationRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CancelInvocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelInvocation", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelInvocationResponse()
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


    def CreateCommand(self, request):
        """This API is used to create a command.

        :param request: Request instance for CreateCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.CreateCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CreateCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCommand", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCommandResponse()
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


    def CreateInvoker(self, request):
        """This API is used to create an invoker.

        :param request: Request instance for CreateInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.CreateInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.CreateInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInvoker", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInvokerResponse()
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


    def DeleteCommand(self, request):
        """This API is used to delete a command.
        Commands bound to an invoker cannot be deleted.

        :param request: Request instance for DeleteCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCommand", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCommandResponse()
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


    def DeleteInvoker(self, request):
        """This API is used to delete an invoker.

        :param request: Request instance for DeleteInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.DeleteInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DeleteInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInvoker", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInvokerResponse()
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


    def DescribeAutomationAgentStatus(self, request):
        """This API is used to query the status of the TAT agent.

        :param request: Request instance for DescribeAutomationAgentStatus.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeAutomationAgentStatusRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeAutomationAgentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutomationAgentStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutomationAgentStatusResponse()
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


    def DescribeCommands(self, request):
        """This API is used to query command details.

        :param request: Request instance for DescribeCommands.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeCommandsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeCommandsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCommands", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCommandsResponse()
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


    def DescribeInvocationTasks(self, request):
        """This API is used to query execution task details.

        :param request: Request instance for DescribeInvocationTasks.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationTasksRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocationTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInvocationTasksResponse()
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


    def DescribeInvocations(self, request):
        """This API is used to query execution activity details.

        :param request: Request instance for DescribeInvocations.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvocationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvocations", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInvocationsResponse()
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


    def DescribeInvokerRecords(self, request):
        """This API is used to query the execution history of an invoker.

        :param request: Request instance for DescribeInvokerRecords.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvokerRecordsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvokerRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvokerRecords", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInvokerRecordsResponse()
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


    def DescribeInvokers(self, request):
        """This API is used to query invoker details.

        :param request: Request instance for DescribeInvokers.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeInvokersRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeInvokersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInvokers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInvokersResponse()
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


    def DescribeRegions(self, request):
        """This API is used to query the list of regions that supports TAT.
        If the `RegionState` is `AVAILABLE`, it means that TAT is available in the region. If no value is returned, TAT is not available in the region.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tat.v20201028.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DisableInvoker(self, request):
        """This API is used to disable an invoker.

        :param request: Request instance for DisableInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.DisableInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.DisableInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableInvoker", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableInvokerResponse()
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


    def EnableInvoker(self, request):
        """This API is used to enable an invoker.

        :param request: Request instance for EnableInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.EnableInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.EnableInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableInvoker", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableInvokerResponse()
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


    def InvokeCommand(self, request):
        """This API is used to trigger a command on the specified instance and returns the execution activity ID (inv-xxxxxxxx) on success. Each execution activity has one or more execution tasks (invt-xxxxxxxx) and each execution task indicates an execution record on a CVM or Lighthouse instance.

        * If the agent is not installed on the instance or is offline, an error is returned.
        * If the command type is not supported by the agent runtime environment, an error is returned.
        * The specified instance needs to be in a VPC network.
        * The specified instance needs to be in the RUNNING status.
        * Only one type of instances (CVM or Lighthouse) can be specified in a single request.

        :param request: Request instance for InvokeCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.InvokeCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.InvokeCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeCommand", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeCommandResponse()
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


    def ModifyCommand(self, request):
        """This API is used to modify a command.

        :param request: Request instance for ModifyCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.ModifyCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.ModifyCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCommand", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCommandResponse()
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


    def ModifyInvoker(self, request):
        """This API is used to modify an invoker.

        :param request: Request instance for ModifyInvoker.
        :type request: :class:`tencentcloud.tat.v20201028.models.ModifyInvokerRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.ModifyInvokerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInvoker", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInvokerResponse()
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


    def PreviewReplacedCommandContent(self, request):
        """This API is used to preview the command with custom parameters. The command is not executed.

        :param request: Request instance for PreviewReplacedCommandContent.
        :type request: :class:`tencentcloud.tat.v20201028.models.PreviewReplacedCommandContentRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.PreviewReplacedCommandContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewReplacedCommandContent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PreviewReplacedCommandContentResponse()
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


    def RunCommand(self, request):
        """This API is used to execute a command and returns the execution activity ID (inv-xxxxxxxx) on success. Each execution has one or more execution tasks (invt-xxxxxxxx) and each execution task indicates an execution record on a CVM or Lighthouse instance.

        * If the agent is not installed on the instance or is offline, an error is returned.
        * If the command type is not supported by the agent runtime environment, an error is returned.
        * The specified instance needs to be in a VPC network.
        * The specified instance needs to be in the `RUNNING` status.
        * Only one type of instances (CVM or Lighthouse) can be specified in a single request.

        :param request: Request instance for RunCommand.
        :type request: :class:`tencentcloud.tat.v20201028.models.RunCommandRequest`
        :rtype: :class:`tencentcloud.tat.v20201028.models.RunCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunCommand", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunCommandResponse()
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