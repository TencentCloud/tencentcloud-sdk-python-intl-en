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
        This API is used to create a TDMQ for RabbitMQ exclusive instance.
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
        This API is used to delete a TDMQ for RabbitMQ exclusive instance.
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
        
    async def DescribeCmqDeadLetterSourceQueues(
            self,
            request: models.DescribeCmqDeadLetterSourceQueuesRequest,
            opts: Dict = None,
    ) -> models.DescribeCmqDeadLetterSourceQueuesResponse:
        """
        This API is used to enumerate the source queues of a CMQ dead letter queue.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCmqDeadLetterSourceQueues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCmqDeadLetterSourceQueuesResponse
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
        
    async def DescribeRabbitMQNodeList(
            self,
            request: models.DescribeRabbitMQNodeListRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQNodeListResponse:
        """
        This API is used to query the list of TDMQ for RabbitMQ exclusive cluster nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQNodeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQNodeListResponse
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
        
    async def DescribeRabbitMQVipInstances(
            self,
            request: models.DescribeRabbitMQVipInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVipInstancesResponse:
        """
        This API is used to query the list of the purchased TDMQ for RabbitMQ exclusive instances.
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
        
    async def DescribeRabbitMQVirtualHostList(
            self,
            request: models.DescribeRabbitMQVirtualHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeRabbitMQVirtualHostListResponse:
        """
        This API is used to query the list of TDMQ for RabbitMQ exclusive vhosts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRabbitMQVirtualHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRabbitMQVirtualHostListResponse
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
        Currently, the `ReceiveMessage` API only supports partitioned topics. It is used to receive messages sent to a specified partitioned topic. If it is called when there are no messages in the partitioned topic, the `ReceiveTimeout` exception will be reported.

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
        This document is used to send a TDMQ for RocketMQ message.
        """
        
        kwargs = {}
        kwargs["action"] = "SendRocketMQMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendRocketMQMessageResponse
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