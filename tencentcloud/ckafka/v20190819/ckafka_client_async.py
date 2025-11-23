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
from tencentcloud.ckafka.v20190819 import models
from typing import Dict


class CkafkaClient(AbstractClient):
    _apiVersion = '2019-08-19'
    _endpoint = 'ckafka.intl.tencentcloudapi.com'
    _service = 'ckafka'

    async def BatchCreateAcl(
            self,
            request: models.BatchCreateAclRequest,
            opts: Dict = None,
    ) -> models.BatchCreateAclResponse:
        """
        This API is used to create ACL policies in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyGroupOffsets(
            self,
            request: models.BatchModifyGroupOffsetsRequest,
            opts: Dict = None,
    ) -> models.BatchModifyGroupOffsetsResponse:
        """
        This API is used to batch modify consumer group offsets.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyGroupOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyGroupOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyTopicAttributes(
            self,
            request: models.BatchModifyTopicAttributesRequest,
            opts: Dict = None,
    ) -> models.BatchModifyTopicAttributesResponse:
        """
        This API is used to batch set topic attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyTopicAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyTopicAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAcl(
            self,
            request: models.CreateAclRequest,
            opts: Dict = None,
    ) -> models.CreateAclResponse:
        """
        This API is used to add an ACL policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAclRule(
            self,
            request: models.CreateAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAclRuleResponse:
        """
        This API shows you how to create an ACL rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumer(
            self,
            request: models.CreateConsumerRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerResponse:
        """
        This API is used to create a consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatahubTopic(
            self,
            request: models.CreateDatahubTopicRequest,
            opts: Dict = None,
    ) -> models.CreateDatahubTopicResponse:
        """
        This API is used to create a DIP topic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatahubTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatahubTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstancePre(
            self,
            request: models.CreateInstancePreRequest,
            opts: Dict = None,
    ) -> models.CreateInstancePreResponse:
        """
        This API is used to create prepaid annual and monthly instances. It only supports creating Pro Edition instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstancePre"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancePreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePartition(
            self,
            request: models.CreatePartitionRequest,
            opts: Dict = None,
    ) -> models.CreatePartitionResponse:
        """
        This API is used to add a partition in a topic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePostPaidInstance(
            self,
            request: models.CreatePostPaidInstanceRequest,
            opts: Dict = None,
    ) -> models.CreatePostPaidInstanceResponse:
        """
        This API is used to replace `CreateInstancePost`  to create a pay-as-you-go instance.  You can call this API via SDK or the TencentCloud API console to create a pay-as-you-go CKafka instance,  which is an alternate option for making a purchase in the console.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePostPaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePostPaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoute(
            self,
            request: models.CreateRouteRequest,
            opts: Dict = None,
    ) -> models.CreateRouteResponse:
        """
        This API is used to add instance routes.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        This API is used to create a CKafka topic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopicIpWhiteList(
            self,
            request: models.CreateTopicIpWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateTopicIpWhiteListResponse:
        """
        This API is used to create a topic IP allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopicIpWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicIpWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        This API is used to add a user.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAcl(
            self,
            request: models.DeleteAclRequest,
            opts: Dict = None,
    ) -> models.DeleteAclResponse:
        """
        This API is used to delete an ACL.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAclRule(
            self,
            request: models.DeleteAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAclRuleResponse:
        """
        This API is used to delete an ACL rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        Delete consumer groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstancePost(
            self,
            request: models.DeleteInstancePostRequest,
            opts: Dict = None,
    ) -> models.DeleteInstancePostResponse:
        """
        This API is used to delete post-payment instances. It directly performs instance termination by calling API deletion without associating connectors and tasks in pre-check.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstancePost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstancePostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstancePre(
            self,
            request: models.DeleteInstancePreRequest,
            opts: Dict = None,
    ) -> models.DeleteInstancePreResponse:
        """
        This API is used to delete prepaid instances. It performs isolation and deletion actions on the instance. After successful execution, the instance will be directly deleted and terminated. By calling API deletion, it directly performs instance termination without associating connectors and tasks in pre-check.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstancePre"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstancePreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoute(
            self,
            request: models.DeleteRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteRouteResponse:
        """
        This API is used to delete a route.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRouteTriggerTime(
            self,
            request: models.DeleteRouteTriggerTimeRequest,
            opts: Dict = None,
    ) -> models.DeleteRouteTriggerTimeResponse:
        """
        This API is used to modify the delayed trigger time of route deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRouteTriggerTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRouteTriggerTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        This API is used to delete a CKafka topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopicIpWhiteList(
            self,
            request: models.DeleteTopicIpWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicIpWhiteListResponse:
        """
        This API is used to delete a topic IP allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopicIpWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicIpWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        This API is used to delete a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeACL(
            self,
            request: models.DescribeACLRequest,
            opts: Dict = None,
    ) -> models.DescribeACLResponse:
        """
        This API is used to enumerate ACLs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAclRule(
            self,
            request: models.DescribeAclRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeAclRuleResponse:
        """
        This API is used to query the ACL rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCkafkaVersion(
            self,
            request: models.DescribeCkafkaVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeCkafkaVersionResponse:
        """
        This API is used to query instance version information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCkafkaVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCkafkaVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCkafkaZone(
            self,
            request: models.DescribeCkafkaZoneRequest,
            opts: Dict = None,
    ) -> models.DescribeCkafkaZoneResponse:
        """
        This API is used to view the AZ list of Ckafka.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCkafkaZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCkafkaZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroup(
            self,
            request: models.DescribeConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupResponse:
        """
        This API is used to query consumer group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCvmInfo(
            self,
            request: models.DescribeCvmInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCvmInfoResponse:
        """
        This API is used to get instance information corresponding to backend CVM, including cvmId and ip. It is for Pro Edition, while Standard Edition returns empty data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCvmInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCvmInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatahubTopic(
            self,
            request: models.DescribeDatahubTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeDatahubTopicResponse:
        """
        This API is used to retrieve DIP topic attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatahubTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatahubTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatahubTopics(
            self,
            request: models.DescribeDatahubTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatahubTopicsResponse:
        """
        This API is used to query the DataHub topic list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatahubTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatahubTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroup(
            self,
            request: models.DescribeGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupResponse:
        """
        This API is used to enumerate consumer groups (simplified).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupInfo(
            self,
            request: models.DescribeGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupInfoResponse:
        """
        This API is used to get consumer group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupOffsets(
            self,
            request: models.DescribeGroupOffsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupOffsetsResponse:
        """
        This API is used to get the consumer group offset.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceAttributes(
            self,
            request: models.DescribeInstanceAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceAttributesResponse:
        """
        This API is used to obtain instance attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to search for a list of TDMQ CKafka instances under a user account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDetail(
            self,
            request: models.DescribeInstancesDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDetailResponse:
        """
        This API is used to get instance list details under a user account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegion(
            self,
            request: models.DescribeRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionResponse:
        """
        This API is used to enumerate regions, and can be called only in Guangzhou.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoute(
            self,
            request: models.DescribeRouteRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteResponse:
        """
        This API is used to view route information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupRoutes(
            self,
            request: models.DescribeSecurityGroupRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupRoutesResponse:
        """
        This API is used to retrieve the security group route information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        This API is used to query the task status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopic(
            self,
            request: models.DescribeTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicResponse:
        """
        API domain name: https://ckafka.tencentcloudapi.com
        This API is used to get the list of topics in a CKafka instance of a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicAttributes(
            self,
            request: models.DescribeTopicAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicAttributesResponse:
        """
        This API is used to retrieve topic attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicDetail(
            self,
            request: models.DescribeTopicDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicDetailResponse:
        """
        This API is used to get topic list details (only for call in the console).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicProduceConnection(
            self,
            request: models.DescribeTopicProduceConnectionRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicProduceConnectionResponse:
        """
        This API is used to query the connection information of the topic producer.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicProduceConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicProduceConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicSubscribeGroup(
            self,
            request: models.DescribeTopicSubscribeGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicSubscribeGroupResponse:
        """
        This API is used to search and subscribe the message group information of a topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicSubscribeGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicSubscribeGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicSyncReplica(
            self,
            request: models.DescribeTopicSyncReplicaRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicSyncReplicaResponse:
        """
        This API is used to get the details of a synced topic replica.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicSyncReplica"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicSyncReplicaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTypeInstances(
            self,
            request: models.DescribeTypeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeTypeInstancesResponse:
        """
        This API is used to search for a list of TDMQ CKafka instances of the specified type under a user account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTypeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTypeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUser(
            self,
            request: models.DescribeUserRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResponse:
        """
        This API is used to query user information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchMessageByOffset(
            self,
            request: models.FetchMessageByOffsetRequest,
            opts: Dict = None,
    ) -> models.FetchMessageByOffsetResponse:
        """
        This API is used to query messages based on a specified offset position.
        """
        
        kwargs = {}
        kwargs["action"] = "FetchMessageByOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchMessageByOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchMessageListByOffset(
            self,
            request: models.FetchMessageListByOffsetRequest,
            opts: Dict = None,
    ) -> models.FetchMessageListByOffsetResponse:
        """
        This API is used to query the message list based on an offset.
        """
        
        kwargs = {}
        kwargs["action"] = "FetchMessageListByOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchMessageListByOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchMessageListByTimestamp(
            self,
            request: models.FetchMessageListByTimestampRequest,
            opts: Dict = None,
    ) -> models.FetchMessageListByTimestampResponse:
        """
        This API is used to query a message list by timestamp.
        """
        
        kwargs = {}
        kwargs["action"] = "FetchMessageListByTimestamp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchMessageListByTimestampResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquireCkafkaPrice(
            self,
            request: models.InquireCkafkaPriceRequest,
            opts: Dict = None,
    ) -> models.InquireCkafkaPriceResponse:
        """
        This API is used to purchase a CKafka instance or query the instance renewal price.
        """
        
        kwargs = {}
        kwargs["action"] = "InquireCkafkaPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquireCkafkaPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstanceScalingDown(
            self,
            request: models.InstanceScalingDownRequest,
            opts: Dict = None,
    ) -> models.InstanceScalingDownResponse:
        """
        This API is used to perform downsizing on a pay-as-you-go instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InstanceScalingDown"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstanceScalingDownResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAclRule(
            self,
            request: models.ModifyAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAclRuleResponse:
        """
        This API is used to modify ACL policy, currently only support whether to apply preset rules to newly-added topics.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDatahubTopic(
            self,
            request: models.ModifyDatahubTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyDatahubTopicResponse:
        """
        This API is used to modify DIP topic attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDatahubTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDatahubTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroupOffsets(
            self,
            request: models.ModifyGroupOffsetsRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupOffsetsResponse:
        """
        This API is used to set the consumer group (Groups) offset.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroupOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAttributes(
            self,
            request: models.ModifyInstanceAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAttributesResponse:
        """
        This API is used to set instance attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancePre(
            self,
            request: models.ModifyInstancePreRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancePreResponse:
        """
        This API is used to change the configuration of prepaid instances, adjust disks, modify bandwidth, and manage partitions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancePre"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancePreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPassword(
            self,
            request: models.ModifyPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyPasswordResponse:
        """
        This API is used to change the password.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoutineMaintenanceTask(
            self,
            request: models.ModifyRoutineMaintenanceTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRoutineMaintenanceTaskResponse:
        """
        This API is used to set automated ops attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoutineMaintenanceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoutineMaintenanceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopicAttributes(
            self,
            request: models.ModifyTopicAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicAttributesResponse:
        """
        This API is used to modify topic attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopicAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendMessage(
            self,
            request: models.SendMessageRequest,
            opts: Dict = None,
    ) -> models.SendMessageResponse:
        """
        This API is used to send messages through the HTTP access layer.
        """
        
        kwargs = {}
        kwargs["action"] = "SendMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeBrokerVersion(
            self,
            request: models.UpgradeBrokerVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeBrokerVersionResponse:
        """
        This API is used to upgrade the broker version.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeBrokerVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeBrokerVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)