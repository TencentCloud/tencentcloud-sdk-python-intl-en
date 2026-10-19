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
from tencentcloud.config.v20220802 import models
from typing import Dict


class ConfigClient(AbstractClient):
    _apiVersion = '2022-08-02'
    _endpoint = 'config.intl.tencentcloudapi.com'
    _service = 'config'

    async def AddAggregateCompliancePack(
            self,
            request: models.AddAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.AddAggregateCompliancePackResponse:
        """
        This API is used to create compliance packages for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAggregateConfigRule(
            self,
            request: models.AddAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.AddAggregateConfigRuleResponse:
        """
        This API is used to create rules for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddAlarmPolicy(
            self,
            request: models.AddAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.AddAlarmPolicyResponse:
        """
        This API is used to add alarm monitoring rules.
        """
        
        kwargs = {}
        kwargs["action"] = "AddAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCompliancePack(
            self,
            request: models.AddCompliancePackRequest,
            opts: Dict = None,
    ) -> models.AddCompliancePackResponse:
        """
        This API is used to create a compliance package.
        """
        
        kwargs = {}
        kwargs["action"] = "AddCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddConfigRule(
            self,
            request: models.AddConfigRuleRequest,
            opts: Dict = None,
    ) -> models.AddConfigRuleResponse:
        """
        This API is used to create rules.
        """
        
        kwargs = {}
        kwargs["action"] = "AddConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseAggregateConfigRule(
            self,
            request: models.CloseAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.CloseAggregateConfigRuleResponse:
        """
        This API is used to close rules for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseConfigRecorder(
            self,
            request: models.CloseConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.CloseConfigRecorderResponse:
        """
        This API is used to manage resource monitoring - disabling monitoring.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseConfigRule(
            self,
            request: models.CloseConfigRuleRequest,
            opts: Dict = None,
    ) -> models.CloseConfigRuleResponse:
        """
        Close rules
        """
        
        kwargs = {}
        kwargs["action"] = "CloseConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAggregator(
            self,
            request: models.CreateAggregatorRequest,
            opts: Dict = None,
    ) -> models.CreateAggregatorResponse:
        """
        This API is used to create account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAggregator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAggregatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRemediation(
            self,
            request: models.CreateRemediationRequest,
            opts: Dict = None,
    ) -> models.CreateRemediationResponse:
        """
        This API is used to add rule remediation settings.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRemediation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRemediationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAggregateCompliancePack(
            self,
            request: models.DeleteAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DeleteAggregateCompliancePackResponse:
        """
        This API is used to delete compliance packages for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAggregateConfigRule(
            self,
            request: models.DeleteAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAggregateConfigRuleResponse:
        """
        This API is used to delete rules for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAggregators(
            self,
            request: models.DeleteAggregatorsRequest,
            opts: Dict = None,
    ) -> models.DeleteAggregatorsResponse:
        """
        This API is used to delete account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAggregators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAggregatorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmPolicy(
            self,
            request: models.DeleteAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmPolicyResponse:
        """
        Deletes alarm rules
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCompliancePack(
            self,
            request: models.DeleteCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DeleteCompliancePackResponse:
        """
        This API is used to delete compliance packages.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigRule(
            self,
            request: models.DeleteConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigRuleResponse:
        """
        Delete a rule
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRemediations(
            self,
            request: models.DeleteRemediationsRequest,
            opts: Dict = None,
    ) -> models.DeleteRemediationsResponse:
        """
        This API is used to delete rule remediation settings.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRemediations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRemediationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateCompliancePack(
            self,
            request: models.DescribeAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateCompliancePackResponse:
        """
        This API is used to query compliance package details for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateConfigDeliver(
            self,
            request: models.DescribeAggregateConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateConfigDeliverResponse:
        """
        This API is used to query delivery setting details for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateConfigRule(
            self,
            request: models.DescribeAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateConfigRuleResponse:
        """
        This API is used to query rule details for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregateDiscoveredResource(
            self,
            request: models.DescribeAggregateDiscoveredResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregateDiscoveredResourceResponse:
        """
        This API is used to query resource details for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregateDiscoveredResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregateDiscoveredResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAggregator(
            self,
            request: models.DescribeAggregatorRequest,
            opts: Dict = None,
    ) -> models.DescribeAggregatorResponse:
        """
        This example shows you how to query account group details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAggregator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAggregatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompliancePack(
            self,
            request: models.DescribeCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DescribeCompliancePackResponse:
        """
        This API is used to query compliance package details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigDeliver(
            self,
            request: models.DescribeConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigDeliverResponse:
        """
        This API is used to query delivery setting details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigRecorder(
            self,
            request: models.DescribeConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigRecorderResponse:
        """
        This API is used to query monitoring details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigRule(
            self,
            request: models.DescribeConfigRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigRuleResponse:
        """
        This example shows you how to query rule details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDiscoveredResource(
            self,
            request: models.DescribeDiscoveredResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDiscoveredResourceResponse:
        """
        Resource details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDiscoveredResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDiscoveredResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemCompliancePack(
            self,
            request: models.DescribeSystemCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemCompliancePackResponse:
        """
        This API is used to query the system compliance package details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemRule(
            self,
            request: models.DescribeSystemRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemRuleResponse:
        """
        This API is used to preset rule details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachAggregateConfigRuleToCompliancePack(
            self,
            request: models.DetachAggregateConfigRuleToCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DetachAggregateConfigRuleToCompliancePackResponse:
        """
        This API is used to remove rules from compliance packages for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachAggregateConfigRuleToCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachAggregateConfigRuleToCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachConfigRuleToCompliancePack(
            self,
            request: models.DetachConfigRuleToCompliancePackRequest,
            opts: Dict = None,
    ) -> models.DetachConfigRuleToCompliancePackResponse:
        """
        This API is used to remove rules for a compliance package.
        """
        
        kwargs = {}
        kwargs["action"] = "DetachConfigRuleToCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachConfigRuleToCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateCompliancePacks(
            self,
            request: models.ListAggregateCompliancePacksRequest,
            opts: Dict = None,
    ) -> models.ListAggregateCompliancePacksResponse:
        """
        This API is used to query the list of compliance packages for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateCompliancePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateCompliancePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateConfigRuleEvaluationResults(
            self,
            request: models.ListAggregateConfigRuleEvaluationResultsRequest,
            opts: Dict = None,
    ) -> models.ListAggregateConfigRuleEvaluationResultsResponse:
        """
        This API is used to query evaluation results from the rule dimension for account groups (the list of evaluation results for resources under a specific rule).
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateConfigRuleEvaluationResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateConfigRuleEvaluationResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateConfigRuleResourceEvaluationResults(
            self,
            request: models.ListAggregateConfigRuleResourceEvaluationResultsRequest,
            opts: Dict = None,
    ) -> models.ListAggregateConfigRuleResourceEvaluationResultsResponse:
        """
        This API is used to list resource evaluation results of compliance rules in account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateConfigRuleResourceEvaluationResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateConfigRuleResourceEvaluationResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateConfigRules(
            self,
            request: models.ListAggregateConfigRulesRequest,
            opts: Dict = None,
    ) -> models.ListAggregateConfigRulesResponse:
        """
        This API is used to query the list of rules for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateConfigRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateConfigRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregateDiscoveredResources(
            self,
            request: models.ListAggregateDiscoveredResourcesRequest,
            opts: Dict = None,
    ) -> models.ListAggregateDiscoveredResourcesResponse:
        """
        This API is used to query the list of resources for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregateDiscoveredResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregateDiscoveredResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAggregators(
            self,
            request: models.ListAggregatorsRequest,
            opts: Dict = None,
    ) -> models.ListAggregatorsResponse:
        """
        Account group list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAggregators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAggregatorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAlarmPolicy(
            self,
            request: models.ListAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.ListAlarmPolicyResponse:
        """
        Alarm rule list
        """
        
        kwargs = {}
        kwargs["action"] = "ListAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCompliancePacks(
            self,
            request: models.ListCompliancePacksRequest,
            opts: Dict = None,
    ) -> models.ListCompliancePacksResponse:
        """
        This API is used to query the list of compliance packages.
        """
        
        kwargs = {}
        kwargs["action"] = "ListCompliancePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCompliancePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConfigRuleEvaluationResults(
            self,
            request: models.ListConfigRuleEvaluationResultsRequest,
            opts: Dict = None,
    ) -> models.ListConfigRuleEvaluationResultsResponse:
        """
        This API is used to obtain evaluation results from the rule dimension (the list of evaluation results for resources under a specific rule).
        """
        
        kwargs = {}
        kwargs["action"] = "ListConfigRuleEvaluationResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConfigRuleEvaluationResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConfigRuleResourceEvaluationResults(
            self,
            request: models.ListConfigRuleResourceEvaluationResultsRequest,
            opts: Dict = None,
    ) -> models.ListConfigRuleResourceEvaluationResultsResponse:
        """
        This API is used to query the list of resource evaluation results under configuration rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConfigRuleResourceEvaluationResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConfigRuleResourceEvaluationResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListConfigRules(
            self,
            request: models.ListConfigRulesRequest,
            opts: Dict = None,
    ) -> models.ListConfigRulesResponse:
        """
        This example shows you how to query the rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListConfigRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListConfigRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDiscoveredResources(
            self,
            request: models.ListDiscoveredResourcesRequest,
            opts: Dict = None,
    ) -> models.ListDiscoveredResourcesResponse:
        """
        Obtaining the Resource List
        """
        
        kwargs = {}
        kwargs["action"] = "ListDiscoveredResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDiscoveredResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRemediationExecutions(
            self,
            request: models.ListRemediationExecutionsRequest,
            opts: Dict = None,
    ) -> models.ListRemediationExecutionsResponse:
        """
        Correction records.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRemediationExecutions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRemediationExecutionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRemediations(
            self,
            request: models.ListRemediationsRequest,
            opts: Dict = None,
    ) -> models.ListRemediationsResponse:
        """
        This API is used to list remediation settings.
        """
        
        kwargs = {}
        kwargs["action"] = "ListRemediations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRemediationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListResourceTypes(
            self,
            request: models.ListResourceTypesRequest,
            opts: Dict = None,
    ) -> models.ListResourceTypesResponse:
        """
        This API is used to query the resource type list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSystemCompliancePacks(
            self,
            request: models.ListSystemCompliancePacksRequest,
            opts: Dict = None,
    ) -> models.ListSystemCompliancePacksResponse:
        """
        This API is used to query the list of system compliance packages.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSystemCompliancePacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSystemCompliancePacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSystemRules(
            self,
            request: models.ListSystemRulesRequest,
            opts: Dict = None,
    ) -> models.ListSystemRulesResponse:
        """
        This API is used to query the preset rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSystemRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSystemRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenAggregateConfigRule(
            self,
            request: models.OpenAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.OpenAggregateConfigRuleResponse:
        """
        This API is used to enable a rule for an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenConfigRecorder(
            self,
            request: models.OpenConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.OpenConfigRecorderResponse:
        """
        This API is used to manage resource monitoring - enabling monitoring.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenConfigRule(
            self,
            request: models.OpenConfigRuleRequest,
            opts: Dict = None,
    ) -> models.OpenConfigRuleResponse:
        """
        Enable rules
        """
        
        kwargs = {}
        kwargs["action"] = "OpenConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutEvaluations(
            self,
            request: models.PutEvaluationsRequest,
            opts: Dict = None,
    ) -> models.PutEvaluationsResponse:
        """
        Reporting Evaluation Results Under Custom Rules
        """
        
        kwargs = {}
        kwargs["action"] = "PutEvaluations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutEvaluationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAggregateConfigRuleEvaluation(
            self,
            request: models.StartAggregateConfigRuleEvaluationRequest,
            opts: Dict = None,
    ) -> models.StartAggregateConfigRuleEvaluationResponse:
        """
        This API is used to trigger evaluation for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "StartAggregateConfigRuleEvaluation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAggregateConfigRuleEvaluationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartConfigRuleEvaluation(
            self,
            request: models.StartConfigRuleEvaluationRequest,
            opts: Dict = None,
    ) -> models.StartConfigRuleEvaluationResponse:
        """
        This API is used to trigger evaluations.
        """
        
        kwargs = {}
        kwargs["action"] = "StartConfigRuleEvaluation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartConfigRuleEvaluationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartRemediation(
            self,
            request: models.StartRemediationRequest,
            opts: Dict = None,
    ) -> models.StartRemediationResponse:
        """
        This API is used to manually execute rule repairs.
        """
        
        kwargs = {}
        kwargs["action"] = "StartRemediation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartRemediationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateCompliancePack(
            self,
            request: models.UpdateAggregateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateCompliancePackResponse:
        """
        This API is used to edit conformance packages for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateCompliancePackStatus(
            self,
            request: models.UpdateAggregateCompliancePackStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateCompliancePackStatusResponse:
        """
        This API is used to enable or disable compliance packages for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateCompliancePackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateCompliancePackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateConfigDeliver(
            self,
            request: models.UpdateAggregateConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateConfigDeliverResponse:
        """
        This API is used to edit delivery settings for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregateConfigRule(
            self,
            request: models.UpdateAggregateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregateConfigRuleResponse:
        """
        This API is used to edit rules for account groups.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAggregator(
            self,
            request: models.UpdateAggregatorRequest,
            opts: Dict = None,
    ) -> models.UpdateAggregatorResponse:
        """
        Edit an account group.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAggregator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAggregatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlarmPolicy(
            self,
            request: models.UpdateAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateAlarmPolicyResponse:
        """
        Updating an Alarm Rule
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCompliancePack(
            self,
            request: models.UpdateCompliancePackRequest,
            opts: Dict = None,
    ) -> models.UpdateCompliancePackResponse:
        """
        This API is used to edit a conformance pack.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCompliancePack"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCompliancePackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCompliancePackStatus(
            self,
            request: models.UpdateCompliancePackStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateCompliancePackStatusResponse:
        """
        This API is used to enable or disable compliance packages.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCompliancePackStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCompliancePackStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConfigDeliver(
            self,
            request: models.UpdateConfigDeliverRequest,
            opts: Dict = None,
    ) -> models.UpdateConfigDeliverResponse:
        """
        This API is used to edit shipping settings.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConfigDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConfigDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConfigRecorder(
            self,
            request: models.UpdateConfigRecorderRequest,
            opts: Dict = None,
    ) -> models.UpdateConfigRecorderResponse:
        """
        Edit the monitoring scope.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConfigRecorder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConfigRecorderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateConfigRule(
            self,
            request: models.UpdateConfigRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateConfigRuleResponse:
        """
        This API is used to edit a rule.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateConfigRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateConfigRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRemediation(
            self,
            request: models.UpdateRemediationRequest,
            opts: Dict = None,
    ) -> models.UpdateRemediationResponse:
        """
        This API is used to add alarm monitoring rules.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRemediation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRemediationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)