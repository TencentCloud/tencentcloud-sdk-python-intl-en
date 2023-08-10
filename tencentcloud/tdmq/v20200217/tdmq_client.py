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
            model = models.AcknowledgeMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ClearCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ClearCmqSubscriptionFilterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateCmqSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateCmqTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQUser(self, request):
        """This API is used to create a TDMQ for RabbitMQ user.

        :param request: Request instance for CreateRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQVipInstance(self, request):
        """This API is used to create a TDMQ for RabbitMQ exclusive instance.

        :param request: Request instance for CreateRabbitMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQVirtualHost(self, request):
        """This API is used to create a TDMQ for RabbitMQ vhost.

        :param request: Request instance for CreateRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateRocketMQGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateRocketMQNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateRocketMQTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteCmqSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteCmqTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQUser(self, request):
        """This API is used to delete a TDMQ for RabbitMQ user.

        :param request: Request instance for DeleteRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQVipInstance(self, request):
        """This API is used to delete a TDMQ for RabbitMQ exclusive instance.

        :param request: Request instance for DeleteRabbitMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQVirtualHost(self, request):
        """This API is used to delete a TDMQ for RabbitMQ vhost.

        :param request: Request instance for DeleteRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteRocketMQGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteRocketMQNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteRocketMQTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DeleteRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubscriptions(self, request):
        """This API is used to delete a subscription.

        :param request: Request instance for DeleteSubscriptions.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteSubscriptionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSubscriptions", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSubscriptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopics(self, request):
        """This API is used to batch delete topics.

        :param request: Request instance for DeleteTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBindClusters(self, request):
        """This API is used to get the list of dedicated clusters bound to a user.

        :param request: Request instance for DescribeBindClusters.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindClustersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeBindClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeBindVpcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """This API is used to get the list of clusters.

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeCmqDeadLetterSourceQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeCmqQueueDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmqQueues(self, request):
        """This API is used to query all CMQ queues.

        :param request: Request instance for DescribeCmqQueues.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueuesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmqQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeCmqSubscriptionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeCmqTopicDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCmqTopics(self, request):
        """This API is used to enumerate all CMQ topics.

        :param request: Request instance for DescribeCmqTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeCmqTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCmqTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCmqTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeEnvironmentAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironmentRoles(self, request):
        """This API is used to get the list of namespace roles.

        :param request: Request instance for DescribeEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvironments(self, request):
        """This API is used to get the list of namespaces under a tenant.

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribePublisherSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribePublishersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePulsarProInstanceDetail(self, request):
        """This API is used to obtain the information of a TDMQ for Pulsar pro cluster instance.

        :param request: Request instance for DescribePulsarProInstanceDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstanceDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePulsarProInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePulsarProInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePulsarProInstances(self, request):
        """This API is used to query the list of the purchased TDMQ for Pulsar pro instances.

        :param request: Request instance for DescribePulsarProInstances.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstancesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribePulsarProInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePulsarProInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePulsarProInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQNodeList(self, request):
        """This API is used to query the list of TDMQ for RabbitMQ exclusive cluster nodes.

        :param request: Request instance for DescribeRabbitMQNodeList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQNodeListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQNodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQNodeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQNodeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQUser(self, request):
        """This API is used to query the list of TDMQ for RabbitMQ users.

        :param request: Request instance for DescribeRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQVipInstances(self, request):
        """This API is used to query the list of the purchased TDMQ for RabbitMQ exclusive instances.

        :param request: Request instance for DescribeRabbitMQVipInstances.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstancesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQVipInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQVipInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQVirtualHost(self, request):
        """This API is used to query the list of TDMQ for RabbitMQ vhosts.

        :param request: Request instance for DescribeRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQVirtualHostList(self, request):
        """This API is used to query the list of TDMQ for RabbitMQ exclusive vhosts.

        :param request: Request instance for DescribeRabbitMQVirtualHostList.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVirtualHostListRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVirtualHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQVirtualHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQVirtualHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQClusters(self, request):
        """This API is used to get the list of RocketMQ clusters.

        :param request: Request instance for DescribeRocketMQClusters.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClustersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQGroups(self, request):
        """This API is used to get the list of RocketMQ consumer groups.

        :param request: Request instance for DescribeRocketMQGroups.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQGroupsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQMsg(self, request):
        """This API is used to query the TDMQ for RocketMQ message details.

        :param request: Request instance for DescribeRocketMQMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQNamespaces(self, request):
        """This API is used to get the list of RocketMQ namespaces.

        :param request: Request instance for DescribeRocketMQNamespaces.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQNamespacesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopics(self, request):
        """This API is used to get the list of RocketMQ topics.

        :param request: Request instance for DescribeRocketMQTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQVipInstanceDetail(self, request):
        """This API is used to get the information of a specific TDMQ for RocketMQ exclusive cluster.

        :param request: Request instance for DescribeRocketMQVipInstanceDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstanceDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQVipInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQVipInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQVipInstances(self, request):
        """This API is used to query the list of the purchased TDMQ for RocketMQ exclusive instances.

        :param request: Request instance for DescribeRocketMQVipInstances.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstancesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQVipInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQVipInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQVipInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.DescribeRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubscriptions(self, request):
        """This API is used to query the list of subscribers under the specified environment and topic.

        :param request: Request instance for DescribeSubscriptions.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeSubscriptionsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeSubscriptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubscriptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubscriptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopics(self, request):
        """This API is used to get the list of topics under an environment.

        :param request: Request instance for DescribeTopics.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyCmqQueueAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyCmqSubscriptionAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyCmqTopicAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyEnvironmentAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQUser(self, request):
        """This API is used to modify a TDMQ for RabbitMQ user.

        :param request: Request instance for ModifyRabbitMQUser.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQUserRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQVirtualHost(self, request):
        """This API is used to modify a TDMQ for RabbitMQ vhost.

        :param request: Request instance for ModifyRabbitMQVirtualHost.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQVirtualHostRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQVirtualHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQVirtualHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQVirtualHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyRocketMQClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyRocketMQGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQInstanceSpec(self, request):
        """This API is used to modify the configurations of a TDMQ for RocketMQ exclusive instance, including the upgrade of the instance specification, node count, and storage, and the downgrade of the instance specification. After you call this API to place the order and make payments, the configuration modification will be in progress. You can query whether the modification has been completed through the `DescribeRocketMQVipInstances` API`.

        :param request: Request instance for ModifyRocketMQInstanceSpec.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceSpecRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyRocketMQNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyRocketMQTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ModifyTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.PublishCmqMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReceiveMessage(self, request):
        """Currently, the `ReceiveMessage` API only supports partitioned topics. It is used to receive messages sent to a specified partitioned topic. If it is called when there are no messages in the partitioned topic, the `ReceiveTimeout` exception will be reported.

        Instructions on how to use `BatchReceivePolicy`:

        `BatchReceive` has three parameters:

        ● `MaxNumMessages`: The maximum number of messages returned by `Receive` when `BatchReceive` is used.
        ● `MaxNumBytes`: The maximum size (in bytes) of the message returned by `Receive` when `BatchReceive` is used.
        ● `Timeout`: The maximum timeout period (in milliseconds) of calling `Receive` when `BatchReceive` is used.

        By default, if you don’t specify any of the three parameters, the `BatchReceive` feature is disabled; if one of the three parameter values is above zero, `BatchReceive` is enabled. `BatchReceive` will be disabled when any of the three parameter values reaches the threshold you specify.

        Note: The values of both `MaxNumMessages` and `MaxNumBytes` are subject to the value of `ReceiveQueueSize`. If the values of `ReceiveQueueSize` and `MaxNumMessages` are 5 and 10, respectively, you can receive up to five rather than 10 messages when `BatchReceive` is used.



        The API configured with `BatchReceivePolicy` returns multiple messages at a time.

        1. These messages are separated by “###”. After receiving them, you can separate them with split tools in different languages.
        2. MessageIDs are separated by “###”. After receiving the messages, you can separate the MessageIDs with split tools in different languages, so that you can obtain the `MessageID` field information required for calling the `AcknowledgeMessage` API.

        :param request: Request instance for ReceiveMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ReceiveMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ReceiveMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReceiveMessage", params, headers=headers)
            response = json.loads(body)
            model = models.ReceiveMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ResetMsgSubOffsetByTimestampResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.ResetRocketMQConsumerOffSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.RewindCmqQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.SendBatchMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.SendCmqMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendMessages(self, request):
        """This API is used to send a single message.
        The message cannot be sent to a persistent topic.

        :param request: Request instance for SendMessages.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendMessagesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendMessages", params, headers=headers)
            response = json.loads(body)
            model = models.SendMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.SendMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendRocketMQMessage(self, request):
        """This document is used to send a TDMQ for RocketMQ message.

        :param request: Request instance for SendRocketMQMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SendRocketMQMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SendRocketMQMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendRocketMQMessage", params, headers=headers)
            response = json.loads(body)
            model = models.SendRocketMQMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
            model = models.UnbindCmqDeadLetterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))