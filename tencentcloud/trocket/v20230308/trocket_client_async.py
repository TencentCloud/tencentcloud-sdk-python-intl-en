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
from tencentcloud.trocket.v20230308 import models
from typing import Dict


class TrocketClient(AbstractClient):
    _apiVersion = '2023-03-08'
    _endpoint = 'trocket.intl.tencentcloudapi.com'
    _service = 'trocket'

    async def ChangeMigratingTopicToNextStage(
            self,
            request: models.ChangeMigratingTopicToNextStageRequest,
            opts: Dict = None,
    ) -> models.ChangeMigratingTopicToNextStageResponse:
        """
        This API is used to modify the Topic status during migration and go to next step.
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeMigratingTopicToNextStage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeMigratingTopicToNextStageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumerGroup(
            self,
            request: models.CreateConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerGroupResponse:
        """
        Create consumer groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        This API is used to create a RocketMQ 5.x cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRole(
            self,
            request: models.CreateRoleRequest,
            opts: Dict = None,
    ) -> models.CreateRoleResponse:
        """
        This API is used to add a role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumerGroup(
            self,
            request: models.DeleteConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerGroupResponse:
        """
        This API is used to delete a consumer group. After a consumer group is deleted, all configurations and related data of the consumer group are cleared and cannot be restored. After deletion, online consumer clients report errors. It is recommended to take clients offline in advance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        This API is used to delete a TDMQ RocketMQ 5.x cluster. Topics, consumer groups, and roles in use should be deleted first.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRole(
            self,
            request: models.DeleteRoleRequest,
            opts: Dict = None,
    ) -> models.DeleteRoleResponse:
        """
        This API is used to delete a role. Make sure that the related information on this role is not used in the current code. After the role is deleted, the keys (AccessKey and SecretKey) used to produce or consume messages with this role become invalid immediately.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmoothMigrationTask(
            self,
            request: models.DeleteSmoothMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteSmoothMigrationTaskResponse:
        """
        This API is used to delete a smooth migration task. Only canceled tasks can be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmoothMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmoothMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        This API is used to delete a topic. After deletion, all configurations and related data of the topic will be cleared and cannot be restored.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerClient(
            self,
            request: models.DescribeConsumerClientRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerClientResponse:
        """
        Query consumer client details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerClientList(
            self,
            request: models.DescribeConsumerClientListRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerClientListResponse:
        """
        This API is used to query the client connection list of a consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerClientList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerClientListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroup(
            self,
            request: models.DescribeConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupResponse:
        """
        Query consumer group details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerLag(
            self,
            request: models.DescribeConsumerLagRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerLagResponse:
        """
        This API is used to query the number of heaped messages in a specified consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerLag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerLagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFusionInstanceList(
            self,
            request: models.DescribeFusionInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeFusionInstanceListResponse:
        """
        This API is used to describe clusters, supporting both 4.x and 5.x clusters. Among them, parameter usage of Filters is as follows:.

        -InstanceName, the cluster name, supports fuzzy query and can be obtained from the API return value or console.
        -InstanceId Cluster ID, exact query, obtain from the current API or console.
        - InstanceType cluster type, see [InstanceItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#InstanceItem) data structure, supports multiple selections.
        - Version: cluster edition, enumeration values as follows:.
        -4 RocketMQ 4.x clusters.
        -Deploy a RocketMQ 5.x cluster.

        This API is used to demonstrate Filters.
         [{ "Name": "InstanceId", "Values": ["rmq-72mo3a9o"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFusionInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFusionInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        This API is used to query RocketMQ 5.x cluster information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceList(
            self,
            request: models.DescribeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceListResponse:
        """
        This API is used to describe clusters. It only supports 5.x clusters. Description of the Filters parameter use is as follows:.

        -InstanceName Cluster name, supports fuzzy search.
        - InstanceId The Tencent Cloud RocketMQ instance ID, obtained from the [DescribeFusionInstanceList](https://www.tencentcloud.comom/document/api/1493/106745?from_cn_redirect=1) API or console.
        - InstanceType cluster type, see [InstanceItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#InstanceItem) data structure, supports multiple selections.
        -InstanceStatus cluster status, see [InstanceItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#InstanceItem) data structure, supports multiple selections.

        This API is used to demonstrate Filters.
        [{
            "Name": "InstanceId",
            "Values": ["rmq-72mo3a9o"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessage(
            self,
            request: models.DescribeMessageRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageResponse:
        """
        Query message details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageList(
            self,
            request: models.DescribeMessageListRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageListResponse:
        """
        Query the message list. If querying dead letter messages, set the ConsumerGroup parameter.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageTrace(
            self,
            request: models.DescribeMessageTraceRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageTraceResponse:
        """
        This API is used to query message trace by message ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageTrace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageTraceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigratingGroupStats(
            self,
            request: models.DescribeMigratingGroupStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigratingGroupStatsResponse:
        """
        This API is used to view real-time information of migration consumption groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigratingGroupStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigratingGroupStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigratingTopicList(
            self,
            request: models.DescribeMigratingTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeMigratingTopicListResponse:
        """
        This API is used to query the Topic migration status list.

        The Filters field is a query filter that supports the following conditions:.
        This API is used to get topic names with fuzzy query support.
        This api is used to query the migration status. See the data structure in MigratingTopic (https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#MigratingTopic).
        This API is used to manage namespaces, valid only for 4.x clusters.

        This API is used to demonstrate Filters.
        [{
            "Name": "TopicName",
            "Values": ["topic-a"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigratingTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigratingTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigratingTopicStats(
            self,
            request: models.DescribeMigratingTopicStatsRequest,
            opts: Dict = None,
    ) -> models.DescribeMigratingTopicStatsResponse:
        """
        This API is used to query real-time data of migration topics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigratingTopicStats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigratingTopicStatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationTaskList(
            self,
            request: models.DescribeMigrationTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationTaskListResponse:
        """
        This API is used to search the data migration task list. Filter parameter usage instructions are as follows:.

        This API is used to search precisely according to task ID.
        InstanceId. This API is used to precisely search based on instance ID.
        This API is used to search by task Type.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProducerList(
            self,
            request: models.DescribeProducerListRequest,
            opts: Dict = None,
    ) -> models.DescribeProducerListResponse:
        """
        This API is used to query producer list information associated with a topic. Filters support the following criteria:.
        -client IP.
        -client ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProducerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProducerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductSKUs(
            self,
            request: models.DescribeProductSKUsRequest,
            opts: Dict = None,
    ) -> models.DescribeProductSKUsResponse:
        """
        This API is used to query product sales specifications against RocketMQ 5.x clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductSKUs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductSKUsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        This API is used to query the list of roles. Filter parameter usage instructions are as follows:.

        -Role name supports fuzzy search and can be obtained from the API return value or console.
        -AccessKey, support fuzzy search, obtain from API return value or console.

        This API is used to demonstrate Filters.
        [{ "Name": "RoleName", "Values": ["test_role"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmoothMigrationTaskList(
            self,
            request: models.DescribeSmoothMigrationTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeSmoothMigrationTaskListResponse:
        """
        This API is used to query the migration task list smoothly.

        This API is used to query the supported fields of the query parameter Filters as follows:.
        Task status, supports multiple selections.
        ConnectionType, network connection type, supports multiple selections. See the description of SmoothMigrationTaskItem (https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#SmoothMigrationTaskItem).
        This API is used to search for an instance by instance ID with precise matching.
        This API is used to query task names with fuzzy search support.

        This API is used to demonstrate Filters.
        [{
            "Name": "InstanceId",
            "Values": ["rmq-1gzecldfg"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmoothMigrationTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmoothMigrationTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSourceClusterGroupList(
            self,
            request: models.DescribeSourceClusterGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeSourceClusterGroupListResponse:
        """
        This API is used to obtain the group list of the source cluster during the smooth migration process.

        The Filters field is a query filter that supports the following fields:.
        This API is used to query consumer group names with fuzzy search support.
        This API is used to check whether the data is Imported.
        This api is used to check the import status. See SourceClusterGroupConfig (https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#SourceClusterGroupConfig) for details.
        This API is used to manage namespaces, valid only for 4.x clusters.

        This API is used to demonstrate Filters.
        [{
            "Name": "GroupName",
            "Values": ["group-a"]
        }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSourceClusterGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSourceClusterGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopic(
            self,
            request: models.DescribeTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicResponse:
        """
        This API is used to query topic details. The Offset and Limit parameters are pagination parameters for consumer groups subscribing to this topic. The Filter parameter usage instructions are as follows:.

        -The ConsumerGroup name can be obtained from the [ConsumeGroupItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#ConsumeGroupItem) in the API response of [DescribeConsumerGroupList](https://www.tencentcloud.comom/document/api/1493/101535?from_cn_redirect=1) or from the console.

        This API is used to demonstrate Filters.
        [{ "Name": "ConsumerGroup", "Values": ["test_group"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicList(
            self,
            request: models.DescribeTopicListRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicListResponse:
        """
        This API is used to search the topic list. Filter parameter usage instructions are as follows:.

        -TopicName supports fuzzy search. Obtain it from the [TopicItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#TopicItem) in the [DescribeTopicList](https://www.tencentcloud.comom/document/api/1493/96030?from_cn_redirect=1) API response or the console.
        -Search by TopicType, support multiple selections. See the TopicType field in the [DescribeTopic](https://www.tencentcloud.comom/document/api/1493/97945?from_cn_redirect=1) API.

        This API is used to demonstrate Filters.
         [{ "Name": "TopicName", "Values": ["test_topic"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicListByGroup(
            self,
            request: models.DescribeTopicListByGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicListByGroupResponse:
        """
        This API is used to get topic list by consumer group. Filter parameter usage instructions are as follows:.

        -TopicName. It can be obtained from [TopicItem](https://www.tencentcloud.comom/document/api/1493/96031?from_cn_redirect=1#TopicItem) returned by the API [DescribeTopicList](https://www.tencentcloud.comom/document/api/1493/96030?from_cn_redirect=1) or from the console.

        This API is used to demonstrate Filters.
        [{ "Name": "TopicName", "Values": ["test_topic"] }]
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicListByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicListByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DoHealthCheckOnMigratingTopic(
            self,
            request: models.DoHealthCheckOnMigratingTopicRequest,
            opts: Dict = None,
    ) -> models.DoHealthCheckOnMigratingTopicResponse:
        """
        This API is used to check whether the topics being migrated are in normal status. Only topics in normal status can enter the next migration stage.
        """
        
        kwargs = {}
        kwargs["action"] = "DoHealthCheckOnMigratingTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DoHealthCheckOnMigratingTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroup(
            self,
            request: models.ModifyConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupResponse:
        """
        Modify consumer group attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        This API is used to modify attributes of a TDMQ RocketMQ 5.x cluster. Only running clusters support this operation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceEndpoint(
            self,
            request: models.ModifyInstanceEndpointRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceEndpointResponse:
        """
        This API is used to modify access points of a TDMQ RocketMQ 5.x cluster. Make sure that the access points exist before the operation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceEndpointResponse
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
        Modify topic attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveMigratingTopic(
            self,
            request: models.RemoveMigratingTopicRequest,
            opts: Dict = None,
    ) -> models.RemoveMigratingTopicResponse:
        """
        This API is used to remove a topic from the migration list. It is valid only when the topic is in the initial state.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMigratingTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMigratingTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResendDeadLetterMessage(
            self,
            request: models.ResendDeadLetterMessageRequest,
            opts: Dict = None,
    ) -> models.ResendDeadLetterMessageResponse:
        """
        This API is used to resend dead letter messages.
        """
        
        kwargs = {}
        kwargs["action"] = "ResendDeadLetterMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResendDeadLetterMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetConsumerGroupOffset(
            self,
            request: models.ResetConsumerGroupOffsetRequest,
            opts: Dict = None,
    ) -> models.ResetConsumerGroupOffsetResponse:
        """
        Reset the consumption position.
        """
        
        kwargs = {}
        kwargs["action"] = "ResetConsumerGroupOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetConsumerGroupOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackMigratingTopicStage(
            self,
            request: models.RollbackMigratingTopicStageRequest,
            opts: Dict = None,
    ) -> models.RollbackMigratingTopicStageResponse:
        """
        This API is used to roll back the topic that is undergoing migration to the previous stage.
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackMigratingTopicStage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackMigratingTopicStageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)