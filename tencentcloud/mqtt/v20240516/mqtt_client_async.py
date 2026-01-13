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
from tencentcloud.mqtt.v20240516 import models
from typing import Dict


class MqttClient(AbstractClient):
    _apiVersion = '2024-05-16'
    _endpoint = 'mqtt.intl.tencentcloudapi.com'
    _service = 'mqtt'

    async def AddClientSubscription(
            self,
            request: models.AddClientSubscriptionRequest,
            opts: Dict = None,
    ) -> models.AddClientSubscriptionResponse:
        """
        This API is used to add a subscription for an MQTT client.
        """
        
        kwargs = {}
        kwargs["action"] = "AddClientSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddClientSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAuthorizationPolicy(
            self,
            request: models.CreateAuthorizationPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAuthorizationPolicyResponse:
        """
        This API is used to create a performance test task for an MQTT instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAuthorizationPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAuthorizationPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        This API is used to purchase a new MQTT instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMessageEnrichmentRule(
            self,
            request: models.CreateMessageEnrichmentRuleRequest,
            opts: Dict = None,
    ) -> models.CreateMessageEnrichmentRuleResponse:
        """
        This API is used to create a message enrichment rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMessageEnrichmentRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMessageEnrichmentRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        This API is used to add an MQTT role.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAuthorizationPolicy(
            self,
            request: models.DeleteAuthorizationPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAuthorizationPolicyResponse:
        """
        This API is used to delete policy rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAuthorizationPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAuthorizationPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClientSubscription(
            self,
            request: models.DeleteClientSubscriptionRequest,
            opts: Dict = None,
    ) -> models.DeleteClientSubscriptionResponse:
        """
        This API is used to delete a subscription of an MQTT client.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClientSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClientSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInstance(
            self,
            request: models.DeleteInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteInstanceResponse:
        """
        This API is used to delete an MQTT instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMessageEnrichmentRule(
            self,
            request: models.DeleteMessageEnrichmentRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteMessageEnrichmentRuleResponse:
        """
        This API is used to delete the message enrichment rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMessageEnrichmentRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMessageEnrichmentRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        This API is used to delete an MQTT topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        This API is used to delete an MQTT user.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthorizationPolicies(
            self,
            request: models.DescribeAuthorizationPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthorizationPoliciesResponse:
        """
        This API is used to query authorization rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthorizationPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthorizationPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientList(
            self,
            request: models.DescribeClientListRequest,
            opts: Dict = None,
    ) -> models.DescribeClientListResponse:
        """
        This API is used to query the MQTT client details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        This API is used to query instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageByTopic(
            self,
            request: models.DescribeMessageByTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageByTopicResponse:
        """
        This API is used to query messages based on subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageByTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageByTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageDetails(
            self,
            request: models.DescribeMessageDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageDetailsResponse:
        """
        This API is used to query the MQTT message details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMessageEnrichmentRules(
            self,
            request: models.DescribeMessageEnrichmentRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeMessageEnrichmentRulesResponse:
        """
        This API is used to query message enrichment rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMessageEnrichmentRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMessageEnrichmentRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopic(
            self,
            request: models.DescribeTopicRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicResponse:
        """
        This API is used to query the MQTT topic details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserList(
            self,
            request: models.DescribeUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserListResponse:
        """
        This API is used to query the user list. Filter parameter usage instructions are as follows:.

        This API is used to perform Username fuzzy search.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KickOutClient(
            self,
            request: models.KickOutClientRequest,
            opts: Dict = None,
    ) -> models.KickOutClientResponse:
        """
        This API is used to kick out a client.
        """
        
        kwargs = {}
        kwargs["action"] = "KickOutClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KickOutClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAuthorizationPolicy(
            self,
            request: models.ModifyAuthorizationPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyAuthorizationPolicyResponse:
        """
        This API is used to modify policy rules. See the data plane authorization policy description (https://www.tencentcloud.com/document/product/1778/109715?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAuthorizationPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAuthorizationPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        This API is used to modify instance attributes. Only running clusters can call this API to perform configuration change.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMessageEnrichmentRule(
            self,
            request: models.ModifyMessageEnrichmentRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyMessageEnrichmentRuleResponse:
        """
        This API is used to modify message enrichment rules.
        Note: All attributes of the current rule must be submitted, even if specific fields are not modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMessageEnrichmentRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMessageEnrichmentRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        This API is used to modify an MQTT role.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAuthorizationPolicyPriority(
            self,
            request: models.UpdateAuthorizationPolicyPriorityRequest,
            opts: Dict = None,
    ) -> models.UpdateAuthorizationPolicyPriorityResponse:
        """
        This API is used to modify policy rule priority.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAuthorizationPolicyPriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAuthorizationPolicyPriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateMessageEnrichmentRulePriority(
            self,
            request: models.UpdateMessageEnrichmentRulePriorityRequest,
            opts: Dict = None,
    ) -> models.UpdateMessageEnrichmentRulePriorityResponse:
        """
        This API is used to modify the priority for message enrichment rule.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateMessageEnrichmentRulePriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateMessageEnrichmentRulePriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)