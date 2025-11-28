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
from tencentcloud.tdmq.v20200217 import models
from typing import Dict


class TdmqClient(AbstractClient):
    _apiVersion = '2020-02-17'
    _endpoint = 'tdmq.intl.tencentcloudapi.com'
    _service = 'tdmq'

    async def AcknowledgeMessage(
            self,
            request: models.AcknowledgeMessageRequest,
            opts: Dict = None,
    ) -> models.AcknowledgeMessageResponse:
        """
        This API is used to acknowledge the message in the specified topic by the provided `MessageID`.
        """
        
        kwargs = {}
        kwargs["action"] = "AcknowledgeMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcknowledgeMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearCmqQueue(
            self,
            request: models.ClearCmqQueueRequest,
            opts: Dict = None,
    ) -> models.ClearCmqQueueResponse:
        """
        This API is used to clear the messages in the CMQ message queue.
        """
        
        kwargs = {}
        kwargs["action"] = "ClearCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearCmqSubscriptionFilterTags(
            self,
            request: models.ClearCmqSubscriptionFilterTagsRequest,
            opts: Dict = None,
    ) -> models.ClearCmqSubscriptionFilterTagsResponse:
        """
        This API is used to clear the message tags of a subscriber.
        """
        
        kwargs = {}
        kwargs["action"] = "ClearCmqSubscriptionFilterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearCmqSubscriptionFilterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        This API is used to create a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCmqQueue(
            self,
            request: models.CreateCmqQueueRequest,
            opts: Dict = None,
    ) -> models.CreateCmqQueueResponse:
        """
        This API is used to create a CMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCmqSubscribe(
            self,
            request: models.CreateCmqSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateCmqSubscribeResponse:
        """
        This API is used to create a CMQ subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCmqSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCmqSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCmqTopic(
            self,
            request: models.CreateCmqTopicRequest,
            opts: Dict = None,
    ) -> models.CreateCmqTopicResponse:
        """
        This API is used to create a CMQ topic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCmqTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCmqTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironment(
            self,
            request: models.CreateEnvironmentRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentResponse:
        """
        This API is used to create a TDMQ namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnvironmentRole(
            self,
            request: models.CreateEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.CreateEnvironmentRoleResponse:
        """
        This API is used to create an environment role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProCluster(
            self,
            request: models.CreateProClusterRequest,
            opts: Dict = None,
    ) -> models.CreateProClusterResponse:
        """
        This api is used to create a professional cluster with prepayment via api calls.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQBinding(
            self,
            request: models.CreateRabbitMQBindingRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQBindingResponse:
        """
        This API is used to create a TDMQ for RabbitMQ routing relationship.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQUser(
            self,
            request: models.CreateRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQUserResponse:
        """
        This API is used to create a TDMQ for RabbitMQ user.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQVipInstance(
            self,
            request: models.CreateRabbitMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQVipInstanceResponse:
        """
        This API is used to create a RabbitMQ managed instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRabbitMQVirtualHost(
            self,
            request: models.CreateRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.CreateRabbitMQVirtualHostResponse:
        """
        This API is used to create a TDMQ for RabbitMQ vhost.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQCluster(
            self,
            request: models.CreateRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQClusterResponse:
        """
        This API is used to create a RocketMQ cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQEnvironmentRole(
            self,
            request: models.CreateRocketMQEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQEnvironmentRoleResponse:
        """
        Creates environment role authorization
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQGroup(
            self,
            request: models.CreateRocketMQGroupRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQGroupResponse:
        """
        This API is used to create a RocketMQ consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQNamespace(
            self,
            request: models.CreateRocketMQNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQNamespaceResponse:
        """
        This API is used to create a RocketMQ namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQRole(
            self,
            request: models.CreateRocketMQRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQRoleResponse:
        """
        This API is used to create a role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQTopic(
            self,
            request: models.CreateRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQTopicResponse:
        """
        This API is used to create a RocketMQ topic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRocketMQVipInstance(
            self,
            request: models.CreateRocketMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateRocketMQVipInstanceResponse:
        """
        This API is used to create a RocketMQ Exclusive Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRocketMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRocketMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRole(
            self,
            request: models.CreateRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRoleResponse:
        """
        This API is used to create a role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubscription(
            self,
            request: models.CreateSubscriptionRequest,
            opts: Dict = None,
    ) -> models.CreateSubscriptionResponse:
        """
        This API is used to create a subscription to a topic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        This API is used to add a message topic in the specified partition and type.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        This API is used to delete a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCmqQueue(
            self,
            request: models.DeleteCmqQueueRequest,
            opts: Dict = None,
    ) -> models.DeleteCmqQueueResponse:
        """
        This API is used to delete a CMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCmqSubscribe(
            self,
            request: models.DeleteCmqSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeleteCmqSubscribeResponse:
        """
        This API is used to delete a CMQ subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCmqSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCmqSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCmqTopic(
            self,
            request: models.DeleteCmqTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteCmqTopicResponse:
        """
        This API is used to delete a CMQ topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCmqTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCmqTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironmentRoles(
            self,
            request: models.DeleteEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentRolesResponse:
        """
        This API is used to delete an environment role.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEnvironments(
            self,
            request: models.DeleteEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DeleteEnvironmentsResponse:
        """
        This API is used to batch delete namespaces under a tenant.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProCluster(
            self,
            request: models.DeleteProClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteProClusterResponse:
        """
        This API is used to delete a professional cluster with prepayment via API calls.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQBinding(
            self,
            request: models.DeleteRabbitMQBindingRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQBindingResponse:
        """
        This API is used to unbind RabbitMQ routing relationships.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQBinding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQBindingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQPermission(
            self,
            request: models.DeleteRabbitMQPermissionRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQPermissionResponse:
        """
        This API is used to delete RabbitMQ permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQUser(
            self,
            request: models.DeleteRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQUserResponse:
        """
        This API is used to delete a TDMQ for RabbitMQ user.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQVipInstance(
            self,
            request: models.DeleteRabbitMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQVipInstanceResponse:
        """
        This API is used to delete a RabbitMQ managed instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRabbitMQVirtualHost(
            self,
            request: models.DeleteRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.DeleteRabbitMQVirtualHostResponse:
        """
        This API is used to delete a TDMQ for RabbitMQ vhost.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQCluster(
            self,
            request: models.DeleteRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQClusterResponse:
        """
        This API is used to delete a RocketMQ cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQEnvironmentRoles(
            self,
            request: models.DeleteRocketMQEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQEnvironmentRolesResponse:
        """
        Deletes environment role authorization
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQGroup(
            self,
            request: models.DeleteRocketMQGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQGroupResponse:
        """
        This API is used to delete a RocketMQ consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQNamespace(
            self,
            request: models.DeleteRocketMQNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQNamespaceResponse:
        """
        This API is used to delete a RocketMQ namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQRoles(
            self,
            request: models.DeleteRocketMQRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQRolesResponse:
        """
        Deletes roles. Batch deletion is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQTopic(
            self,
            request: models.DeleteRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQTopicResponse:
        """
        This API is used to delete a RocketMQ topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRocketMQVipInstance(
            self,
            request: models.DeleteRocketMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteRocketMQVipInstanceResponse:
        """
        This API is used to delete a RocketMQ Exclusive Edition instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRocketMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRocketMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoles(
            self,
            request: models.DeleteRolesRequest,
            opts: Dict = None,
    ) -> models.DeleteRolesResponse:
        """
        This API is used to delete one or multiple roles.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubscriptions(
            self,
            request: models.DeleteSubscriptionsRequest,
            opts: Dict = None,
    ) -> models.DeleteSubscriptionsResponse:
        """
        This API is used to delete a subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubscriptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubscriptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopics(
            self,
            request: models.DeleteTopicsRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicsResponse:
        """
        This API is used to batch delete topics.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindClusters(
            self,
            request: models.DescribeBindClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeBindClustersResponse:
        """
        This API is used to get the list of dedicated clusters bound to a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindVpcs(
            self,
            request: models.DescribeBindVpcsRequest,
            opts: Dict = None,
    ) -> models.DescribeBindVpcsResponse:
        """
        This API is used to get the tenant-VPC binding relationship.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterDetail(
            self,
            request: models.DescribeClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDetailResponse:
        """
        This API is used to get the details of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        This API is used to get the list of clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqQueueDetail(
            self,
            request: models.DescribeCmqQueueDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqQueueDetailResponse:
        """
        This API is used to query the details of a CMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqQueueDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqQueueDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqQueues(
            self,
            request: models.DescribeCmqQueuesRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqQueuesResponse:
        """
        This API is used to query all CMQ queues.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqQueues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqQueuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqSubscriptionDetail(
            self,
            request: models.DescribeCmqSubscriptionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqSubscriptionDetailResponse:
        """
        This API is used to query the CMQ subscription details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqSubscriptionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqSubscriptionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqTopicDetail(
            self,
            request: models.DescribeCmqTopicDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqTopicDetailResponse:
        """
        This API is used to query the details of a CMQ topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqTopicDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqTopicDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCmqTopics(
            self,
            request: models.DescribeCmqTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqTopicsResponse:
        """
        This API is used to enumerate all CMQ topics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironmentAttributes(
            self,
            request: models.DescribeEnvironmentAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentAttributesResponse:
        """
        This API is used to get the attributes of the specified namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironmentAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironmentRoles(
            self,
            request: models.DescribeEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentRolesResponse:
        """
        This API is used to get the list of namespace roles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        This API is used to get the list of namespaces under a tenant.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMqMsgTrace(
            self,
            request: models.DescribeMqMsgTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeMqMsgTraceResponse:
        """
        Queries message trajectory
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMqMsgTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMqMsgTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMsg(
            self,
            request: models.DescribeMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeMsgResponse:
        """
        This API is used to get message details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMsgTrace(
            self,
            request: models.DescribeMsgTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeMsgTraceResponse:
        """
        Queries message trajectory
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMsgTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMsgTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublisherSummary(
            self,
            request: models.DescribePublisherSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribePublisherSummaryResponse:
        """
        This API is used to obtain message production overview information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublisherSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublisherSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublishers(
            self,
            request: models.DescribePublishersRequest,
            opts: Dict = None,
    ) -> models.DescribePublishersResponse:
        """
        This API is used to obtain the list of producer information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublishers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublishersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePulsarProInstanceDetail(
            self,
            request: models.DescribePulsarProInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePulsarProInstanceDetailResponse:
        """
        This API is used to obtain the information of a TDMQ for Pulsar pro cluster instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePulsarProInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePulsarProInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePulsarProInstances(
            self,
            request: models.DescribePulsarProInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePulsarProInstancesResponse:
        """
        This API is used to query the list of the purchased TDMQ for Pulsar pro instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePulsarProInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePulsarProInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQBindings(
            self,
            request: models.DescribeRabbitMQBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQBindingsResponse:
        """
        This API is used to query the list of RabbitMQ route relations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQExchanges(
            self,
            request: models.DescribeRabbitMQExchangesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQExchangesResponse:
        """
        This API is used to query the list of TDMQ for RabbitMQ exchanges.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQExchanges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQExchangesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQNodeList(
            self,
            request: models.DescribeRabbitMQNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQNodeListResponse:
        """
        This API is used to query the RabbitMQ managed node list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQNodeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQPermission(
            self,
            request: models.DescribeRabbitMQPermissionRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQPermissionResponse:
        """
        This API is used to query the list of TDMQ for RabbitMQ permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQQueueDetail(
            self,
            request: models.DescribeRabbitMQQueueDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQQueueDetailResponse:
        """
        This API is used to query the details of RabbitMQ queues.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQQueueDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQQueueDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQQueues(
            self,
            request: models.DescribeRabbitMQQueuesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQQueuesResponse:
        """
        This API is used to query the list of TDMQ for RabbitMQ queues.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQQueues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQQueuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQUser(
            self,
            request: models.DescribeRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQUserResponse:
        """
        This API is used to query the list of TDMQ for RabbitMQ users.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQVipInstance(
            self,
            request: models.DescribeRabbitMQVipInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVipInstanceResponse:
        """
        This API is used to obtain information about one RabbitMQ managed instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQVipInstances(
            self,
            request: models.DescribeRabbitMQVipInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVipInstancesResponse:
        """
        This API is used to query the RabbitMQ managed instance list of user purchases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQVipInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQVipInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRabbitMQVirtualHost(
            self,
            request: models.DescribeRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVirtualHostResponse:
        """
        This API is used to query the list of TDMQ for RabbitMQ vhosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQCluster(
            self,
            request: models.DescribeRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQClusterResponse:
        """
        This API is used to get the information of a specific RocketMQ cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQClusters(
            self,
            request: models.DescribeRocketMQClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQClustersResponse:
        """
        This API is used to get the list of RocketMQ clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQEnvironmentRoles(
            self,
            request: models.DescribeRocketMQEnvironmentRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQEnvironmentRolesResponse:
        """
        Obtains the namespace role list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQEnvironmentRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQEnvironmentRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQGroups(
            self,
            request: models.DescribeRocketMQGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQGroupsResponse:
        """
        This API is used to get the list of RocketMQ consumer groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQMsg(
            self,
            request: models.DescribeRocketMQMsgRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQMsgResponse:
        """
        This API is used to query the TDMQ for RocketMQ message details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQMsgTrace(
            self,
            request: models.DescribeRocketMQMsgTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQMsgTraceResponse:
        """
        Queries message trajectory
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQMsgTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQMsgTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQNamespaces(
            self,
            request: models.DescribeRocketMQNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQNamespacesResponse:
        """
        This API is used to get the list of RocketMQ namespaces.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQProducers(
            self,
            request: models.DescribeRocketMQProducersRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQProducersResponse:
        """
        This API is used to query the producer client list under a specified topic in RocketMQ.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQProducers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQProducersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQPublicAccessMonitorData(
            self,
            request: models.DescribeRocketMQPublicAccessMonitorDataRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQPublicAccessMonitorDataResponse:
        """
        This API is used to pull public network metric monitoring data from TCOP. Currently, only inbound bandwidth and outbound bandwidth metrics from client to LB are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQPublicAccessMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQPublicAccessMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQPublicAccessPoint(
            self,
            request: models.DescribeRocketMQPublicAccessPointRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQPublicAccessPointResponse:
        """
        This API is used to query the public network access information of RocketMQ instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQPublicAccessPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQPublicAccessPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQRoles(
            self,
            request: models.DescribeRocketMQRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQRolesResponse:
        """
        Obtains the list of roles
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopUsages(
            self,
            request: models.DescribeRocketMQTopUsagesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopUsagesResponse:
        """
        Used to obtain the RocketMQ metric sorting list, such as sorting topics under a cluster instance by the most occupied storage space.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopUsages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopUsagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopic(
            self,
            request: models.DescribeRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicResponse:
        """
        This API is used to obtain RocketMQ topic details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopicMsgs(
            self,
            request: models.DescribeRocketMQTopicMsgsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicMsgsResponse:
        """
        Query RocketMQ messages.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopicMsgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicMsgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopicStats(
            self,
            request: models.DescribeRocketMQTopicStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicStatsResponse:
        """
        This API is used to obtain the topic production details list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopicStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopics(
            self,
            request: models.DescribeRocketMQTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicsResponse:
        """
        This API is used to get the list of RocketMQ topics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQTopicsByGroup(
            self,
            request: models.DescribeRocketMQTopicsByGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQTopicsByGroupResponse:
        """
        Obtains the list of topics subscribed under a specified consumer group
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQTopicsByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQTopicsByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQVipInstanceDetail(
            self,
            request: models.DescribeRocketMQVipInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQVipInstanceDetailResponse:
        """
        This API is used to get the information of a specific TDMQ for RocketMQ exclusive cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQVipInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQVipInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRocketMQVipInstances(
            self,
            request: models.DescribeRocketMQVipInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeRocketMQVipInstancesResponse:
        """
        This API is used to query the list of the purchased TDMQ for RocketMQ exclusive instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRocketMQVipInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRocketMQVipInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoles(
            self,
            request: models.DescribeRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeRolesResponse:
        """
        This API is used to get the list of roles.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubscriptions(
            self,
            request: models.DescribeSubscriptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubscriptionsResponse:
        """
        This API is used to query the list of subscribers under the specified environment and topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubscriptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubscriptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicMsgs(
            self,
            request: models.DescribeTopicMsgsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicMsgsResponse:
        """
        This API is used to query messages.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicMsgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicMsgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopics(
            self,
            request: models.DescribeTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicsResponse:
        """
        This API is used to get the list of topics under an environment.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportRocketMQMessageDetail(
            self,
            request: models.ExportRocketMQMessageDetailRequest,
            opts: Dict = None,
    ) -> models.ExportRocketMQMessageDetailResponse:
        """
        Export the RocketMQ message details.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportRocketMQMessageDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportRocketMQMessageDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCluster(
            self,
            request: models.ModifyClusterRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterResponse:
        """
        This API is used to update a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCmqQueueAttribute(
            self,
            request: models.ModifyCmqQueueAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCmqQueueAttributeResponse:
        """
        This API is used to modify the attributes of a CMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCmqQueueAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCmqQueueAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCmqSubscriptionAttribute(
            self,
            request: models.ModifyCmqSubscriptionAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCmqSubscriptionAttributeResponse:
        """
        This API is used to modify the attributes of a CMQ subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCmqSubscriptionAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCmqSubscriptionAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCmqTopicAttribute(
            self,
            request: models.ModifyCmqTopicAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCmqTopicAttributeResponse:
        """
        This API is used to modify the attributes of a CMQ topic.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCmqTopicAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCmqTopicAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnvironmentAttributes(
            self,
            request: models.ModifyEnvironmentAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvironmentAttributesResponse:
        """
        This API is used to modify the attributes of the specified namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnvironmentAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvironmentAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEnvironmentRole(
            self,
            request: models.ModifyEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyEnvironmentRoleResponse:
        """
        This API is used to modify an environment role.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublicNetworkSecurityPolicy(
            self,
            request: models.ModifyPublicNetworkSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyPublicNetworkSecurityPolicyResponse:
        """
        This API is used to modify the public network security policy for pulsar Pro Edition.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublicNetworkSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublicNetworkSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQPermission(
            self,
            request: models.ModifyRabbitMQPermissionRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQPermissionResponse:
        """
        This API is used to modify RabbitMQ permissions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQPermission"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQPermissionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQUser(
            self,
            request: models.ModifyRabbitMQUserRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQUserResponse:
        """
        This API is used to modify a TDMQ for RabbitMQ user.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRabbitMQVirtualHost(
            self,
            request: models.ModifyRabbitMQVirtualHostRequest,
            opts: Dict = None,
    ) -> models.ModifyRabbitMQVirtualHostResponse:
        """
        This API is used to modify a TDMQ for RabbitMQ vhost.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRabbitMQVirtualHost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRabbitMQVirtualHostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQCluster(
            self,
            request: models.ModifyRocketMQClusterRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQClusterResponse:
        """
        This API is used to update a RocketMQ cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQEnvironmentRole(
            self,
            request: models.ModifyRocketMQEnvironmentRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQEnvironmentRoleResponse:
        """
        Modifies environment role authorization
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQEnvironmentRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQEnvironmentRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQGroup(
            self,
            request: models.ModifyRocketMQGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQGroupResponse:
        """
        This API is used to update a RocketMQ consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQInstance(
            self,
            request: models.ModifyRocketMQInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQInstanceResponse:
        """
        Modify the RocketMQ dedicated instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQInstanceSpec(
            self,
            request: models.ModifyRocketMQInstanceSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQInstanceSpecResponse:
        """
        This API is used to modify the configurations of a TDMQ for RocketMQ exclusive instance, including the upgrade of the instance specification, node count, and storage, and the downgrade of the instance specification. After you call this API to place the order and make payments, the configuration modification will be in progress. You can query whether the modification has been completed through the `DescribeRocketMQVipInstances` API`.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQInstanceSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQInstanceSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQNamespace(
            self,
            request: models.ModifyRocketMQNamespaceRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQNamespaceResponse:
        """
        This API is used to update a RocketMQ namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQRole(
            self,
            request: models.ModifyRocketMQRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQRoleResponse:
        """
        Modifies roles
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRocketMQTopic(
            self,
            request: models.ModifyRocketMQTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyRocketMQTopicResponse:
        """
        This API is used to update a RocketMQ topic.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRocketMQTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRocketMQTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRole(
            self,
            request: models.ModifyRoleRequest,
            opts: Dict = None,
    ) -> models.ModifyRoleResponse:
        """
        This API is used to modify a role.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopic(
            self,
            request: models.ModifyTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicResponse:
        """
        This API is used to modify the topic remarks and number of partitions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PublishCmqMsg(
            self,
            request: models.PublishCmqMsgRequest,
            opts: Dict = None,
    ) -> models.PublishCmqMsgResponse:
        """
        This API is used to send a CMQ topic message.
        """
        
        kwargs = {}
        kwargs["action"] = "PublishCmqMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PublishCmqMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReceiveMessage(
            self,
            request: models.ReceiveMessageRequest,
            opts: Dict = None,
    ) -> models.ReceiveMessageResponse:
        """
        This API is used to receive messages sent to a specified Partitioned Topic. It supports only Partitioned Topic type. When there are no messages in the Partitioned Topic but the API is still called, it throws a ReceiveTimeout exception.

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
        """
        
        kwargs = {}
        kwargs["action"] = "ReceiveMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReceiveMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetMsgSubOffsetByTimestamp(
            self,
            request: models.ResetMsgSubOffsetByTimestampRequest,
            opts: Dict = None,
    ) -> models.ResetMsgSubOffsetByTimestampResponse:
        """
        This API is used to rewind a message by timestamp, accurate down to the millisecond.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetMsgSubOffsetByTimestamp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetMsgSubOffsetByTimestampResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRocketMQConsumerOffSet(
            self,
            request: models.ResetRocketMQConsumerOffSetRequest,
            opts: Dict = None,
    ) -> models.ResetRocketMQConsumerOffSetResponse:
        """
        This API is used to reset the consumption offset of a specified consumer group to a specified timestamp.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRocketMQConsumerOffSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRocketMQConsumerOffSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryRocketMQDlqMessage(
            self,
            request: models.RetryRocketMQDlqMessageRequest,
            opts: Dict = None,
    ) -> models.RetryRocketMQDlqMessageResponse:
        """
        Resend the RocketMQ dead letter messages.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryRocketMQDlqMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryRocketMQDlqMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RewindCmqQueue(
            self,
            request: models.RewindCmqQueueRequest,
            opts: Dict = None,
    ) -> models.RewindCmqQueueResponse:
        """
        This API is used to rewind a CMQ queue.
        """
        
        kwargs = {}
        kwargs["action"] = "RewindCmqQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RewindCmqQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendBatchMessages(
            self,
            request: models.SendBatchMessagesRequest,
            opts: Dict = None,
    ) -> models.SendBatchMessagesResponse:
        """
        This API is used to batch send messages.

        Note: the batch message sending API in TDMQ is to package messages into a batch on the service side of TDMQ-HTTP and then send the batch as a TCP request inside the service. Therefore, when using this API, you should still follow the logic of sending a single message: each message is an independent HTTP request, and multiple HTTP requests are aggregated into one batch inside the TDMQ-HTTP service and then sent to the server; that is, batch sending messages is the same as sending a single message in terms of usage, and batch aggregation is completed inside the TDMQ-HTTP service.
        """
        
        kwargs = {}
        kwargs["action"] = "SendBatchMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendBatchMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendCmqMsg(
            self,
            request: models.SendCmqMsgRequest,
            opts: Dict = None,
    ) -> models.SendCmqMsgResponse:
        """
        This API is used to send a CMQ message.
        """
        
        kwargs = {}
        kwargs["action"] = "SendCmqMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendCmqMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendMessages(
            self,
            request: models.SendMessagesRequest,
            opts: Dict = None,
    ) -> models.SendMessagesResponse:
        """
        This API is used to send a single message.
        The message cannot be sent to a persistent topic.
        """
        
        kwargs = {}
        kwargs["action"] = "SendMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendMsg(
            self,
            request: models.SendMsgRequest,
            opts: Dict = None,
    ) -> models.SendMsgResponse:
        """
        This API is used to test message sending. It cannot be used in the production environment.
        """
        
        kwargs = {}
        kwargs["action"] = "SendMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendRocketMQMessage(
            self,
            request: models.SendRocketMQMessageRequest,
            opts: Dict = None,
    ) -> models.SendRocketMQMessageResponse:
        """
        This API is used to send messages through RocketMQ. It is only used for sending a small number of test messages from the console and does not provide SLA. Cloud API is subject to traffic throttling. In real business scenarios, use the RocketMQ SDK to send messages.
        """
        
        kwargs = {}
        kwargs["action"] = "SendRocketMQMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendRocketMQMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetRocketMQPublicAccessPoint(
            self,
            request: models.SetRocketMQPublicAccessPointRequest,
            opts: Dict = None,
    ) -> models.SetRocketMQPublicAccessPointResponse:
        """
        This API is used to enable/disable public network access, and set the security access policy.
        """
        
        kwargs = {}
        kwargs["action"] = "SetRocketMQPublicAccessPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetRocketMQPublicAccessPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindCmqDeadLetter(
            self,
            request: models.UnbindCmqDeadLetterRequest,
            opts: Dict = None,
    ) -> models.UnbindCmqDeadLetterResponse:
        """
        This API is used to unbind a CMQ dead letter queue.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindCmqDeadLetter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindCmqDeadLetterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)