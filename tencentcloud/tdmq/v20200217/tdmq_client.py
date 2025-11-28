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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tdmq.v20200217 import models


class TdmqClient(AbstractClient):
    _apiVersion = '2020-02-17'
    _endpoint = 'tdmq.intl.tencentcloudapi.com'
    _service = 'tdmq'


    def AcknowledgeMessage(self, request):
        r"""This API is used to acknowledge the message in the specified topic by the provided `MessageID`.

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
        r"""This API is used to clear the messages in the CMQ message queue.

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
        r"""This API is used to clear the message tags of a subscriber.

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
        r"""This API is used to create a cluster.

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
        r"""This API is used to create a CMQ queue.

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
        r"""This API is used to create a CMQ subscription.

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
        r"""This API is used to create a CMQ topic.

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
        r"""This API is used to create a TDMQ namespace.

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
        r"""This API is used to create an environment role.

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


    def CreateProCluster(self, request):
        r"""This api is used to create a professional cluster with prepayment via api calls.

        :param request: Request instance for CreateProCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateProClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateProClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQBinding(self, request):
        r"""This API is used to create a TDMQ for RabbitMQ routing relationship.

        :param request: Request instance for CreateRabbitMQBinding.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQBindingRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRabbitMQBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRabbitMQBinding", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRabbitMQBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRabbitMQUser(self, request):
        r"""This API is used to create a TDMQ for RabbitMQ user.

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
        r"""This API is used to create a RabbitMQ managed instance.

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
        r"""This API is used to create a TDMQ for RabbitMQ vhost.

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
        r"""This API is used to create a RocketMQ cluster.

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


    def CreateRocketMQEnvironmentRole(self, request):
        r"""Creates environment role authorization

        :param request: Request instance for CreateRocketMQEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQGroup(self, request):
        r"""This API is used to create a RocketMQ consumer group.

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
        r"""This API is used to create a RocketMQ namespace.

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


    def CreateRocketMQRole(self, request):
        r"""This API is used to create a role.

        :param request: Request instance for CreateRocketMQRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRocketMQTopic(self, request):
        r"""This API is used to create a RocketMQ topic.

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


    def CreateRocketMQVipInstance(self, request):
        r"""This API is used to create a RocketMQ Exclusive Edition instance.

        :param request: Request instance for CreateRocketMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.CreateRocketMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRocketMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRocketMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRole(self, request):
        r"""This API is used to create a role.

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
        r"""This API is used to create a subscription to a topic.

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
        r"""This API is used to add a message topic in the specified partition and type.

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
        r"""This API is used to delete a cluster.

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
        r"""This API is used to delete a CMQ queue.

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
        r"""This API is used to delete a CMQ subscription.

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
        r"""This API is used to delete a CMQ topic.

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
        r"""This API is used to delete an environment role.

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
        r"""This API is used to batch delete namespaces under a tenant.

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


    def DeleteProCluster(self, request):
        r"""This API is used to delete a professional cluster with prepayment via API calls.

        :param request: Request instance for DeleteProCluster.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteProClusterRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteProClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQBinding(self, request):
        r"""This API is used to unbind RabbitMQ routing relationships.

        :param request: Request instance for DeleteRabbitMQBinding.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQBindingRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQBindingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQBinding", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQBindingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQPermission(self, request):
        r"""This API is used to delete RabbitMQ permissions.

        :param request: Request instance for DeleteRabbitMQPermission.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQPermissionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRabbitMQPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRabbitMQPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRabbitMQPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRabbitMQUser(self, request):
        r"""This API is used to delete a TDMQ for RabbitMQ user.

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
        r"""This API is used to delete a RabbitMQ managed instance.

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
        r"""This API is used to delete a TDMQ for RabbitMQ vhost.

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
        r"""This API is used to delete a RocketMQ cluster.

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


    def DeleteRocketMQEnvironmentRoles(self, request):
        r"""Deletes environment role authorization

        :param request: Request instance for DeleteRocketMQEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQGroup(self, request):
        r"""This API is used to delete a RocketMQ consumer group.

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
        r"""This API is used to delete a RocketMQ namespace.

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


    def DeleteRocketMQRoles(self, request):
        r"""Deletes roles. Batch deletion is supported.

        :param request: Request instance for DeleteRocketMQRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRocketMQTopic(self, request):
        r"""This API is used to delete a RocketMQ topic.

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


    def DeleteRocketMQVipInstance(self, request):
        r"""This API is used to delete a RocketMQ Exclusive Edition instance.

        :param request: Request instance for DeleteRocketMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DeleteRocketMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRocketMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRocketMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoles(self, request):
        r"""This API is used to delete one or multiple roles.

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
        r"""This API is used to delete a subscription.

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
        r"""This API is used to batch delete topics.

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
        r"""This API is used to get the list of dedicated clusters bound to a user.

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
        r"""This API is used to get the tenant-VPC binding relationship.

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
        r"""This API is used to get the details of a cluster.

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
        r"""This API is used to get the list of clusters.

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


    def DescribeCmqQueueDetail(self, request):
        r"""This API is used to query the details of a CMQ queue.

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
        r"""This API is used to query all CMQ queues.

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
        r"""This API is used to query the CMQ subscription details.

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
        r"""This API is used to query the details of a CMQ topic.

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
        r"""This API is used to enumerate all CMQ topics.

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
        r"""This API is used to get the attributes of the specified namespace.

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
        r"""This API is used to get the list of namespace roles.

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
        r"""This API is used to get the list of namespaces under a tenant.

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


    def DescribeMqMsgTrace(self, request):
        r"""Queries message trajectory

        :param request: Request instance for DescribeMqMsgTrace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeMqMsgTraceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeMqMsgTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMqMsgTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMqMsgTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMsg(self, request):
        r"""This API is used to get message details.

        :param request: Request instance for DescribeMsg.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMsgTrace(self, request):
        r"""Queries message trajectory

        :param request: Request instance for DescribeMsgTrace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgTraceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeMsgTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMsgTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMsgTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublisherSummary(self, request):
        r"""This API is used to obtain message production overview information.

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
        r"""This API is used to obtain the list of producer information.

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
        r"""This API is used to obtain the information of a TDMQ for Pulsar pro cluster instance.

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
        r"""This API is used to query the list of the purchased TDMQ for Pulsar pro instances.

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


    def DescribeRabbitMQBindings(self, request):
        r"""This API is used to query the list of RabbitMQ route relations.

        :param request: Request instance for DescribeRabbitMQBindings.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQBindingsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQBindingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQBindings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQBindingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQExchanges(self, request):
        r"""This API is used to query the list of TDMQ for RabbitMQ exchanges.

        :param request: Request instance for DescribeRabbitMQExchanges.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQExchangesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQExchangesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQExchanges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQExchangesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQNodeList(self, request):
        r"""This API is used to query the RabbitMQ managed node list.

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


    def DescribeRabbitMQPermission(self, request):
        r"""This API is used to query the list of TDMQ for RabbitMQ permissions.

        :param request: Request instance for DescribeRabbitMQPermission.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQPermissionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQPermission", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQQueueDetail(self, request):
        r"""This API is used to query the details of RabbitMQ queues.

        :param request: Request instance for DescribeRabbitMQQueueDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueueDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueueDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQQueueDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQQueueDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQQueues(self, request):
        r"""This API is used to query the list of TDMQ for RabbitMQ queues.

        :param request: Request instance for DescribeRabbitMQQueues.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueuesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQUser(self, request):
        r"""This API is used to query the list of TDMQ for RabbitMQ users.

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


    def DescribeRabbitMQVipInstance(self, request):
        r"""This API is used to obtain information about one RabbitMQ managed instance.

        :param request: Request instance for DescribeRabbitMQVipInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRabbitMQVipInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRabbitMQVipInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRabbitMQVipInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRabbitMQVipInstances(self, request):
        r"""This API is used to query the RabbitMQ managed instance list of user purchases.

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
        r"""This API is used to query the list of TDMQ for RabbitMQ vhosts.

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


    def DescribeRocketMQCluster(self, request):
        r"""This API is used to get the information of a specific RocketMQ cluster.

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
        r"""This API is used to get the list of RocketMQ clusters.

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


    def DescribeRocketMQEnvironmentRoles(self, request):
        r"""Obtains the namespace role list

        :param request: Request instance for DescribeRocketMQEnvironmentRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQEnvironmentRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQEnvironmentRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQEnvironmentRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQEnvironmentRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQGroups(self, request):
        r"""This API is used to get the list of RocketMQ consumer groups.

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
        r"""This API is used to query the TDMQ for RocketMQ message details.

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


    def DescribeRocketMQMsgTrace(self, request):
        r"""Queries message trajectory

        :param request: Request instance for DescribeRocketMQMsgTrace.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgTraceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQMsgTraceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQMsgTrace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQMsgTraceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQNamespaces(self, request):
        r"""This API is used to get the list of RocketMQ namespaces.

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


    def DescribeRocketMQProducers(self, request):
        r"""This API is used to query the producer client list under a specified topic in RocketMQ.

        :param request: Request instance for DescribeRocketMQProducers.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQProducersRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQProducersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQProducers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQProducersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQPublicAccessMonitorData(self, request):
        r"""This API is used to pull public network metric monitoring data from TCOP. Currently, only inbound bandwidth and outbound bandwidth metrics from client to LB are supported.

        :param request: Request instance for DescribeRocketMQPublicAccessMonitorData.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessMonitorDataRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQPublicAccessMonitorData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQPublicAccessMonitorDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQPublicAccessPoint(self, request):
        r"""This API is used to query the public network access information of RocketMQ instances.

        :param request: Request instance for DescribeRocketMQPublicAccessPoint.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessPointRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQPublicAccessPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQPublicAccessPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQPublicAccessPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQRoles(self, request):
        r"""Obtains the list of roles

        :param request: Request instance for DescribeRocketMQRoles.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQRolesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopUsages(self, request):
        r"""Used to obtain the RocketMQ metric sorting list, such as sorting topics under a cluster instance by the most occupied storage space.

        :param request: Request instance for DescribeRocketMQTopUsages.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopUsagesRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopUsagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopUsages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopUsagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopic(self, request):
        r"""This API is used to obtain RocketMQ topic details.

        :param request: Request instance for DescribeRocketMQTopic.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopicMsgs(self, request):
        r"""Query RocketMQ messages.

        :param request: Request instance for DescribeRocketMQTopicMsgs.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicMsgsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicMsgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopicMsgs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicMsgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopicStats(self, request):
        r"""This API is used to obtain the topic production details list.

        :param request: Request instance for DescribeRocketMQTopicStats.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicStatsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicStatsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopicStats", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicStatsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQTopics(self, request):
        r"""This API is used to get the list of RocketMQ topics.

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


    def DescribeRocketMQTopicsByGroup(self, request):
        r"""Obtains the list of topics subscribed under a specified consumer group

        :param request: Request instance for DescribeRocketMQTopicsByGroup.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsByGroupRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeRocketMQTopicsByGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRocketMQTopicsByGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRocketMQTopicsByGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRocketMQVipInstanceDetail(self, request):
        r"""This API is used to get the information of a specific TDMQ for RocketMQ exclusive cluster.

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
        r"""This API is used to query the list of the purchased TDMQ for RocketMQ exclusive instances.

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
        r"""This API is used to get the list of roles.

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
        r"""This API is used to query the list of subscribers under the specified environment and topic.

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


    def DescribeTopicMsgs(self, request):
        r"""This API is used to query messages.

        :param request: Request instance for DescribeTopicMsgs.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicMsgsRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.DescribeTopicMsgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicMsgs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicMsgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopics(self, request):
        r"""This API is used to get the list of topics under an environment.

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


    def ExportRocketMQMessageDetail(self, request):
        r"""Export the RocketMQ message details.

        :param request: Request instance for ExportRocketMQMessageDetail.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ExportRocketMQMessageDetailRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ExportRocketMQMessageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportRocketMQMessageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportRocketMQMessageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCluster(self, request):
        r"""This API is used to update a cluster.

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
        r"""This API is used to modify the attributes of a CMQ queue.

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
        r"""This API is used to modify the attributes of a CMQ subscription.

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
        r"""This API is used to modify the attributes of a CMQ topic.

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
        r"""This API is used to modify the attributes of the specified namespace.

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
        r"""This API is used to modify an environment role.

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


    def ModifyPublicNetworkSecurityPolicy(self, request):
        r"""This API is used to modify the public network security policy for pulsar Pro Edition.

        :param request: Request instance for ModifyPublicNetworkSecurityPolicy.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyPublicNetworkSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyPublicNetworkSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublicNetworkSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublicNetworkSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQPermission(self, request):
        r"""This API is used to modify RabbitMQ permissions.

        :param request: Request instance for ModifyRabbitMQPermission.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQPermissionRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRabbitMQPermissionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRabbitMQPermission", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRabbitMQPermissionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRabbitMQUser(self, request):
        r"""This API is used to modify a TDMQ for RabbitMQ user.

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
        r"""This API is used to modify a TDMQ for RabbitMQ vhost.

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
        r"""This API is used to update a RocketMQ cluster.

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


    def ModifyRocketMQEnvironmentRole(self, request):
        r"""Modifies environment role authorization

        :param request: Request instance for ModifyRocketMQEnvironmentRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQEnvironmentRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQEnvironmentRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQEnvironmentRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQEnvironmentRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQGroup(self, request):
        r"""This API is used to update a RocketMQ consumer group.

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


    def ModifyRocketMQInstance(self, request):
        r"""Modify the RocketMQ dedicated instance.

        :param request: Request instance for ModifyRocketMQInstance.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQInstanceSpec(self, request):
        r"""This API is used to modify the configurations of a TDMQ for RocketMQ exclusive instance, including the upgrade of the instance specification, node count, and storage, and the downgrade of the instance specification. After you call this API to place the order and make payments, the configuration modification will be in progress. You can query whether the modification has been completed through the `DescribeRocketMQVipInstances` API`.

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
        r"""This API is used to update a RocketMQ namespace.

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


    def ModifyRocketMQRole(self, request):
        r"""Modifies roles

        :param request: Request instance for ModifyRocketMQRole.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQRoleRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.ModifyRocketMQRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRocketMQRole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRocketMQRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRocketMQTopic(self, request):
        r"""This API is used to update a RocketMQ topic.

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
        r"""This API is used to modify a role.

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
        r"""This API is used to modify the topic remarks and number of partitions.

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
        r"""This API is used to send a CMQ topic message.

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
        r"""This API is used to receive messages sent to a specified Partitioned Topic. It supports only Partitioned Topic type. When there are no messages in the Partitioned Topic but the API is still called, it throws a ReceiveTimeout exception.

        This API is used to batch receive policies.

        This API is used to provide the following three parameters:.

        MaxNumMessages: The maximum number of messages returned by the Receive API each time when using BatchReceive.
        MaxNumBytes: the maximum size of messages returned by the Receive API in a single BatchReceive operation, in bytes.
        Timeout: The maximum timeout period for each Receive API call when using BatchReceive is how long, in MS.

        This API is used to disable the BatchReceive feature if none of the three parameters are specified. If any one of the three parameters has a value greater than 0, BatchReceive is enabled. BatchReceive completes when reaching the threshold specified in any one of the three parameters.

        Note: MaxNumMessages and MaxNumBytes are subject to the size of ReceiveQueueSize for each receipt of messages. If ReceiveQueueSize is set to 5 and MaxNumMessages is set to 10, then BatchReceive will receive at most 5 messages at once rather than 10.



        This API is used to return multiple messages at one time.

        This API is used to Split multiple messages with the special character '###', allowing the business side to use Split tools in different languages to separate messages after receiving them.
        Multiple MessageIDs use the special character '###' to separate with each other. After receiving the message, the business side can leverage the Split tool provided by different languages to separate different messages. (Used for filling in the necessary MessageID field information when calling the AcknowledgeMessage API.).

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
        r"""This API is used to rewind a message by timestamp, accurate down to the millisecond.

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
        r"""This API is used to reset the consumption offset of a specified consumer group to a specified timestamp.

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


    def RetryRocketMQDlqMessage(self, request):
        r"""Resend the RocketMQ dead letter messages.

        :param request: Request instance for RetryRocketMQDlqMessage.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.RetryRocketMQDlqMessageRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.RetryRocketMQDlqMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryRocketMQDlqMessage", params, headers=headers)
            response = json.loads(body)
            model = models.RetryRocketMQDlqMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RewindCmqQueue(self, request):
        r"""This API is used to rewind a CMQ queue.

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
        r"""This API is used to batch send messages.

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
        r"""This API is used to send a CMQ message.

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
        r"""This API is used to send a single message.
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
        r"""This API is used to test message sending. It cannot be used in the production environment.

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
        r"""This API is used to send messages through RocketMQ. It is only used for sending a small number of test messages from the console and does not provide SLA. Cloud API is subject to traffic throttling. In real business scenarios, use the RocketMQ SDK to send messages.

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


    def SetRocketMQPublicAccessPoint(self, request):
        r"""This API is used to enable/disable public network access, and set the security access policy.

        :param request: Request instance for SetRocketMQPublicAccessPoint.
        :type request: :class:`tencentcloud.tdmq.v20200217.models.SetRocketMQPublicAccessPointRequest`
        :rtype: :class:`tencentcloud.tdmq.v20200217.models.SetRocketMQPublicAccessPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetRocketMQPublicAccessPoint", params, headers=headers)
            response = json.loads(body)
            model = models.SetRocketMQPublicAccessPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindCmqDeadLetter(self, request):
        r"""This API is used to unbind a CMQ dead letter queue.

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