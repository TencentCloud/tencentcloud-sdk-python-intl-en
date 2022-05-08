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
from tencentcloud.tdmq.v20200217 import models


class TdmqClient(AbstractClient):
    _apiVersion = '2020-02-17'
    _endpoint = 'tdmq.tencentcloudapi.com'
    _service = 'tdmq'


    def AcknowledgeMessage(self, request):
        """This API is used to acknowledge the message in the specified topic by the provided `MessageID`.

        :param request: Request instance for AcknowledgeMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.AcknowledgeMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.AcknowledgeMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcknowledgeMessage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcknowledgeMessageResponse()
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


    def ClearCmqQueue(self, request):
        """This API is used to clear the messages in the CMQ message queue.

        :param request: Request instance for ClearCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearCmqQueue", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearCmqQueueResponse()
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


    def ClearCmqSubscriptionFilterTags(self, request):
        """This API is used to clear the message tags of a subscriber.

        :param request: Request instance for ClearCmqSubscriptionFilterTags.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqSubscriptionFilterTagsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ClearCmqSubscriptionFilterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearCmqSubscriptionFilterTags", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearCmqSubscriptionFilterTagsResponse()
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


    def CreateCluster(self, request):
        """This API is used to create a cluster.

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
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


    def CreateCmqQueue(self, request):
        """This API is used to create a CMQ queue.

        :param request: Request instance for CreateCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCmqQueue", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCmqQueueResponse()
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


    def CreateCmqSubscribe(self, request):
        """This API is used to create a CMQ subscription.

        :param request: Request instance for CreateCmqSubscribe.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqSubscribeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCmqSubscribe", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCmqSubscribeResponse()
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


    def CreateCmqTopic(self, request):
        """This API is used to create a CMQ topic.

        :param request: Request instance for CreateCmqTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateCmqTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCmqTopic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCmqTopicResponse()
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


    def CreateEnvironment(self, request):
        """This API is used to create a TDMQ namespace.

        :param request: Request instance for CreateEnvironment.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironment", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEnvironmentResponse()
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


    def CreateEnvironmentRole(self, request):
        """This API is used to create an environment role.

        :param request: Request instance for CreateEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEnvironmentRoleResponse()
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


    def CreateRocketMQCluster(self, request):
        """This API is used to create a RocketMQ cluster.

        :param request: Request instance for CreateRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRocketMQClusterResponse()
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


    def CreateRocketMQGroup(self, request):
        """This API is used to create a RocketMQ consumer group.

        :param request: Request instance for CreateRocketMQGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRocketMQGroupResponse()
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


    def CreateRocketMQNamespace(self, request):
        """This API is used to create a RocketMQ namespace.

        :param request: Request instance for CreateRocketMQNamespace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQNamespaceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQNamespace", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRocketMQNamespaceResponse()
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


    def CreateRocketMQTopic(self, request):
        """This API is used to create a RocketMQ topic.

        :param request: Request instance for CreateRocketMQTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQTopic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRocketMQTopicResponse()
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


    def CreateRole(self, request):
        """This API is used to create a role.

        :param request: Request instance for CreateRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoleResponse()
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


    def CreateSubscription(self, request):
        """This API is used to create a subscription to a topic.

        :param request: Request instance for CreateSubscription.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateSubscriptionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubscription", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubscriptionResponse()
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


    def CreateTopic(self, request):
        """This API is used to add a message topic in the specified partition and type.

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicResponse()
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


    def DeleteCluster(self, request):
        """This API is used to delete a cluster.

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterResponse()
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


    def DeleteCmqQueue(self, request):
        """This API is used to delete a CMQ queue.

        :param request: Request instance for DeleteCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCmqQueue", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCmqQueueResponse()
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


    def DeleteCmqSubscribe(self, request):
        """This API is used to delete a CMQ subscription.

        :param request: Request instance for DeleteCmqSubscribe.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqSubscribeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCmqSubscribe", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCmqSubscribeResponse()
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


    def DeleteCmqTopic(self, request):
        """This API is used to delete a CMQ topic.

        :param request: Request instance for DeleteCmqTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteCmqTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCmqTopic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCmqTopicResponse()
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


    def DeleteEnvironmentRoles(self, request):
        """This API is used to delete an environment role.

        :param request: Request instance for DeleteEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEnvironmentRolesResponse()
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


    def DeleteEnvironments(self, request):
        """This API is used to batch delete namespaces under a tenant.

        :param request: Request instance for DeleteEnvironments.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnvironments", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEnvironmentsResponse()
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


    def DeleteRocketMQCluster(self, request):
        """This API is used to delete a RocketMQ cluster.

        :param request: Request instance for DeleteRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRocketMQClusterResponse()
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


    def DeleteRocketMQGroup(self, request):
        """This API is used to delete a RocketMQ consumer group.

        :param request: Request instance for DeleteRocketMQGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRocketMQGroupResponse()
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


    def DeleteRocketMQNamespace(self, request):
        """This API is used to delete a RocketMQ namespace.

        :param request: Request instance for DeleteRocketMQNamespace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQNamespaceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQNamespace", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRocketMQNamespaceResponse()
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


    def DeleteRocketMQTopic(self, request):
        """This API is used to delete a RocketMQ topic.

        :param request: Request instance for DeleteRocketMQTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQTopic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRocketMQTopicResponse()
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


    def DeleteRoles(self, request):
        """This API is used to delete one or multiple roles.

        :param request: Request instance for DeleteRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoles", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRolesResponse()
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


    def DescribeBindVpcs(self, request):
        """This API is used to get the tenant-VPC binding relationship.

        :param request: Request instance for DescribeBindVpcs.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindVpcsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindVpcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindVpcs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindVpcsResponse()
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


    def DescribeClusterDetail(self, request):
        """This API is used to get the details of a cluster.

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterDetailResponse()
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


    def DescribeCmqDeadLetterSourceQueues(self, request):
        """This API is used to enumerate the source queues of a CMQ dead letter queue.

        :param request: Request instance for DescribeCmqDeadLetterSourceQueues.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqDeadLetterSourceQueuesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqDeadLetterSourceQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqDeadLetterSourceQueues", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCmqDeadLetterSourceQueuesResponse()
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


    def DescribeCmqQueueDetail(self, request):
        """This API is used to query the details of a CMQ queue.

        :param request: Request instance for DescribeCmqQueueDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueueDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueueDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqQueueDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCmqQueueDetailResponse()
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


    def DescribeCmqSubscriptionDetail(self, request):
        """This API is used to query the CMQ subscription details.

        :param request: Request instance for DescribeCmqSubscriptionDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqSubscriptionDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqSubscriptionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqSubscriptionDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCmqSubscriptionDetailResponse()
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


    def DescribeCmqTopicDetail(self, request):
        """This API is used to query the details of a CMQ topic.

        :param request: Request instance for DescribeCmqTopicDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqTopicDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCmqTopicDetailResponse()
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


    def DescribeEnvironmentAttributes(self, request):
        """This API is used to get the attributes of the specified namespace.

        :param request: Request instance for DescribeEnvironmentAttributes.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentAttributesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironmentAttributes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvironmentAttributesResponse()
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


    def DescribePublisherSummary(self, request):
        """This API is used to obtain message production overview information.

        :param request: Request instance for DescribePublisherSummary.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePublisherSummaryRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePublisherSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublisherSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublisherSummaryResponse()
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


    def DescribePublishers(self, request):
        """This API is used to obtain the list of producer information.

        :param request: Request instance for DescribePublishers.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePublishersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePublishersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublishers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublishersResponse()
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


    def DescribeRocketMQCluster(self, request):
        """This API is used to get the information of a specific RocketMQ cluster.

        :param request: Request instance for DescribeRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRocketMQClusterResponse()
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


    def DescribeRoles(self, request):
        """This API is used to get the list of roles.

        :param request: Request instance for DescribeRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoles", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRolesResponse()
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


    def ModifyCluster(self, request):
        """This API is used to update a cluster.

        :param request: Request instance for ModifyCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterResponse()
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


    def ModifyCmqQueueAttribute(self, request):
        """This API is used to modify the attributes of a CMQ queue.

        :param request: Request instance for ModifyCmqQueueAttribute.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqQueueAttributeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqQueueAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCmqQueueAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCmqQueueAttributeResponse()
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


    def ModifyCmqSubscriptionAttribute(self, request):
        """This API is used to modify the attributes of a CMQ subscription.

        :param request: Request instance for ModifyCmqSubscriptionAttribute.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqSubscriptionAttributeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqSubscriptionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCmqSubscriptionAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCmqSubscriptionAttributeResponse()
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


    def ModifyCmqTopicAttribute(self, request):
        """This API is used to modify the attributes of a CMQ topic.

        :param request: Request instance for ModifyCmqTopicAttribute.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqTopicAttributeRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyCmqTopicAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCmqTopicAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCmqTopicAttributeResponse()
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


    def ModifyEnvironmentAttributes(self, request):
        """This API is used to modify the attributes of the specified namespace.

        :param request: Request instance for ModifyEnvironmentAttributes.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentAttributesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvironmentAttributes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEnvironmentAttributesResponse()
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


    def ModifyEnvironmentRole(self, request):
        """This API is used to modify an environment role.

        :param request: Request instance for ModifyEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEnvironmentRoleResponse()
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


    def ModifyRocketMQCluster(self, request):
        """This API is used to update a RocketMQ cluster.

        :param request: Request instance for ModifyRocketMQCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRocketMQClusterResponse()
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


    def ModifyRocketMQGroup(self, request):
        """This API is used to update a RocketMQ consumer group.

        :param request: Request instance for ModifyRocketMQGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRocketMQGroupResponse()
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


    def ModifyRocketMQNamespace(self, request):
        """This API is used to update a RocketMQ namespace.

        :param request: Request instance for ModifyRocketMQNamespace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQNamespaceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQNamespace", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRocketMQNamespaceResponse()
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


    def ModifyRocketMQTopic(self, request):
        """This API is used to update a RocketMQ topic.

        :param request: Request instance for ModifyRocketMQTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQTopic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRocketMQTopicResponse()
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


    def ModifyRole(self, request):
        """This API is used to modify a role.

        :param request: Request instance for ModifyRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRole", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRoleResponse()
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


    def ModifyTopic(self, request):
        """This API is used to modify the topic remarks and number of partitions.

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTopicResponse()
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


    def PublishCmqMsg(self, request):
        """This API is used to send a CMQ topic message.

        :param request: Request instance for PublishCmqMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.PublishCmqMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.PublishCmqMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishCmqMsg", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishCmqMsgResponse()
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


    def ReceiveMessage(self, request):
        """This API is used to receive messages sent to the specified topic.

        :param request: Request instance for ReceiveMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ReceiveMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ReceiveMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReceiveMessage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReceiveMessageResponse()
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


    def ResetMsgSubOffsetByTimestamp(self, request):
        """This API is used to rewind a message by timestamp, accurate down to the millisecond.

        :param request: Request instance for ResetMsgSubOffsetByTimestamp.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ResetMsgSubOffsetByTimestampRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ResetMsgSubOffsetByTimestampResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetMsgSubOffsetByTimestamp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetMsgSubOffsetByTimestampResponse()
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


    def ResetRocketMQConsumerOffSet(self, request):
        """This API is used to reset the consumption offset of a specified consumer group to a specified timestamp.

        :param request: Request instance for ResetRocketMQConsumerOffSet.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ResetRocketMQConsumerOffSetRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ResetRocketMQConsumerOffSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetRocketMQConsumerOffSet", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetRocketMQConsumerOffSetResponse()
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


    def RewindCmqQueue(self, request):
        """This API is used to rewind a CMQ queue.

        :param request: Request instance for RewindCmqQueue.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.RewindCmqQueueRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RewindCmqQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RewindCmqQueue", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RewindCmqQueueResponse()
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


    def SendBatchMessages(self, request):
        """This API is used to batch send messages.

        Note: the batch message sending API in TDMQ is to package messages into a batch on the service side of TDMQ-HTTP and then send the batch as a TCP request inside the service. Therefore, when using this API, you should still follow the logic of sending a single message: each message is an independent HTTP request, and multiple HTTP requests are aggregated into one batch inside the TDMQ-HTTP service and then sent to the server; that is, batch sending messages is the same as sending a single message in terms of usage, and batch aggregation is completed inside the TDMQ-HTTP service.

        :param request: Request instance for SendBatchMessages.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendBatchMessagesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendBatchMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendBatchMessages", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendBatchMessagesResponse()
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


    def SendCmqMsg(self, request):
        """This API is used to send a CMQ message.

        :param request: Request instance for SendCmqMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendCmqMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendCmqMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendCmqMsg", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendCmqMsgResponse()
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


    def SendMessages(self, request):
        """This API is used to send one message.

        :param request: Request instance for SendMessages.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendMessagesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendMessages", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendMessagesResponse()
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


    def SendMsg(self, request):
        """This API is used to test message sending. It cannot be used in the production environment.

        :param request: Request instance for SendMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendMsg", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendMsgResponse()
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


    def UnbindCmqDeadLetter(self, request):
        """This API is used to unbind a CMQ dead letter queue.

        :param request: Request instance for UnbindCmqDeadLetter.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.UnbindCmqDeadLetterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.UnbindCmqDeadLetterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindCmqDeadLetter", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindCmqDeadLetterResponse()
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