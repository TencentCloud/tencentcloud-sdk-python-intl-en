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
from tencentcloud.tcr.v20190924 import models


class TcrClient(AbstractClient):
    _apiVersion = '2019-09-24'
    _endpoint = 'tcr.tencentcloudapi.com'
    _service = 'tcr'


    def CheckInstance(self, request):
        """This API is used to verify the information of the Enterprise Edition instance.

        :param request: Request instance for CheckInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckInstanceResponse()
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


    def CreateImmutableTagRules(self, request):
        """This API is used to create the tag immutability rule.

        :param request: Request instance for CreateImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImmutableTagRulesResponse()
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


    def CreateInstanceToken(self, request):
        """This API is used to create a temporary or long-term instance access credential.

        :param request: Request instance for CreateInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceTokenResponse()
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


    def CreateMultipleSecurityPolicy(self, request):
        """This API is used to create multiple public network access allowlist policies of the TCR instance.

        :param request: Request instance for CreateMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMultipleSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMultipleSecurityPolicyResponse()
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


    def CreateReplicationInstance(self, request):
        """This API is used to create a replication instance.

        :param request: Request instance for CreateReplicationInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReplicationInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReplicationInstanceResponse()
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


    def DeleteImmutableTagRules(self, request):
        """This API is used to delete the tag immutability rule.

        :param request: Request instance for DeleteImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImmutableTagRulesResponse()
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


    def DeleteMultipleSecurityPolicy(self, request):
        """This API is used to delete multiple public network access allowlist policies of the instance.

        :param request: Request instance for DeleteMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMultipleSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMultipleSecurityPolicyResponse()
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


    def DescribeImmutableTagRules(self, request):
        """This API is used to list the tag immutability rule.

        :param request: Request instance for DescribeImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImmutableTagRulesResponse()
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


    def DescribeReplicationInstanceCreateTasks(self, request):
        """This API is used to query the task status of creating a replication instance.

        :param request: Request instance for DescribeReplicationInstanceCreateTasks.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceCreateTasksRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceCreateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstanceCreateTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReplicationInstanceCreateTasksResponse()
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


    def DescribeReplicationInstanceSyncStatus(self, request):
        """This API is used to query the synchronization status of a replication instance.

        :param request: Request instance for DescribeReplicationInstanceSyncStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceSyncStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstanceSyncStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstanceSyncStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReplicationInstanceSyncStatusResponse()
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


    def DescribeReplicationInstances(self, request):
        """This API is used to query the list of replication instances.

        :param request: Request instance for DescribeReplicationInstances.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstancesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeReplicationInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReplicationInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReplicationInstancesResponse()
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


    def ManageReplication(self, request):
        """This API is used to manage the instance synchronization rule.

        :param request: Request instance for ManageReplication.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageReplicationRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageReplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageReplication", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManageReplicationResponse()
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


    def ModifyImmutableTagRules(self, request):
        """This API is used to update the tag immutability rule.

        :param request: Request instance for ModifyImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImmutableTagRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImmutableTagRulesResponse()
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


    def ModifyInstance(self, request):
        """This API is used to update instance information.

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceResponse()
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