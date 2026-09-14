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
from tencentcloud.ga2.v20250115 import models
from typing import Dict


class Ga2Client(AbstractClient):
    _apiVersion = '2025-01-15'
    _endpoint = 'ga2.intl.tencentcloudapi.com'
    _service = 'ga2'

    async def CreateAccelerateAreas(
            self,
            request: models.CreateAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.CreateAccelerateAreasResponse:
        """
        This API is used to create an acceleration region.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEndpointGroup(
            self,
            request: models.CreateEndpointGroupRequest,
            opts: Dict = None,
    ) -> models.CreateEndpointGroupResponse:
        """
        This API is used to create a terminal node group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEndpointGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEndpointGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateForwardingPolicy(
            self,
            request: models.CreateForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateForwardingPolicyResponse:
        """
        Create a layer-7 forwarding policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateForwardingRule(
            self,
            request: models.CreateForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.CreateForwardingRuleResponse:
        """
        Create a Layer 7 forwarding rule
        """
        
        kwargs = {}
        kwargs["action"] = "CreateForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAccelerator(
            self,
            request: models.CreateGlobalAcceleratorRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorResponse:
        """
        This API is used to create a global acceleration instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAccelerator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAcceleratorAccessLog(
            self,
            request: models.CreateGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorAccessLogResponse:
        """
        Create a GA access log
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAcceleratorAclPolicy(
            self,
            request: models.CreateGlobalAcceleratorAclPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorAclPolicyResponse:
        """
        Create access control policy
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAcceleratorAclPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorAclPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalAcceleratorAclRule(
            self,
            request: models.CreateGlobalAcceleratorAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalAcceleratorAclRuleResponse:
        """
        Create an ACL rule
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalAcceleratorAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalAcceleratorAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListener(
            self,
            request: models.CreateListenerRequest,
            opts: Dict = None,
    ) -> models.CreateListenerResponse:
        """
        This API is used to create a listener.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListenerAdditionalCert(
            self,
            request: models.CreateListenerAdditionalCertRequest,
            opts: Dict = None,
    ) -> models.CreateListenerAdditionalCertResponse:
        """
        Add an extension certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListenerAdditionalCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerAdditionalCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccelerateAreas(
            self,
            request: models.DeleteAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.DeleteAccelerateAreasResponse:
        """
        Delete an acceleration region
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEndpointGroups(
            self,
            request: models.DeleteEndpointGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteEndpointGroupsResponse:
        """
        Delete a terminal node group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEndpointGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEndpointGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteForwardingPolicy(
            self,
            request: models.DeleteForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteForwardingPolicyResponse:
        """
        Delete a layer-7 forwarding policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteForwardingRule(
            self,
            request: models.DeleteForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteForwardingRuleResponse:
        """
        Delete a Layer 7 forwarding rule
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAccelerator(
            self,
            request: models.DeleteGlobalAcceleratorRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorResponse:
        """
        Deletes a global acceleration instance
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAccelerator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAcceleratorAccessLog(
            self,
            request: models.DeleteGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorAccessLogResponse:
        """
        This API is used to delete a GA log task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAcceleratorAclPolicy(
            self,
            request: models.DeleteGlobalAcceleratorAclPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorAclPolicyResponse:
        """
        Delete access control policy
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAcceleratorAclPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorAclPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalAcceleratorAclRule(
            self,
            request: models.DeleteGlobalAcceleratorAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalAcceleratorAclRuleResponse:
        """
        Delete ACL rule
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalAcceleratorAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalAcceleratorAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListener(
            self,
            request: models.DeleteListenerRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerResponse:
        """
        This API is used to delete a listener.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListenerAdditionalCert(
            self,
            request: models.DeleteListenerAdditionalCertRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerAdditionalCertResponse:
        """
        Delete the extension certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListenerAdditionalCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerAdditionalCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccelerateAreas(
            self,
            request: models.DescribeAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.DescribeAccelerateAreasResponse:
        """
        Queries acceleration regions
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccelerateRegions(
            self,
            request: models.DescribeAccelerateRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccelerateRegionsResponse:
        """
        Queries selectable acceleration regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccelerateRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccelerateRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessLogParam(
            self,
            request: models.DescribeAccessLogParamRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessLogParamResponse:
        """
        View access log reporting parameters
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessLogParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessLogParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBorderSettlement(
            self,
            request: models.DescribeCrossBorderSettlementRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderSettlementResponse:
        """
        Querying Cross-Border Bills
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderSettlement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderSettlementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEndpointGroups(
            self,
            request: models.DescribeEndpointGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeEndpointGroupsResponse:
        """
        Query a terminal node group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndpointGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndpointGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardingPolicy(
            self,
            request: models.DescribeForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardingPolicyResponse:
        """
        View a layer-7 forwarding policy
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardingRule(
            self,
            request: models.DescribeForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardingRuleResponse:
        """
        View a Layer 7 forwarding rule
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAcceleratorAccessLog(
            self,
            request: models.DescribeGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorAccessLogResponse:
        """
        Query log tasks
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAcceleratorAclPolicies(
            self,
            request: models.DescribeGlobalAcceleratorAclPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorAclPoliciesResponse:
        """
        View the access control policy
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAcceleratorAclPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorAclPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAcceleratorAclRules(
            self,
            request: models.DescribeGlobalAcceleratorAclRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorAclRulesResponse:
        """
        View ACL rules
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAcceleratorAclRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorAclRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalAccelerators(
            self,
            request: models.DescribeGlobalAcceleratorsRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalAcceleratorsResponse:
        """
        Modify a global acceleration instance
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalAccelerators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalAcceleratorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListeners(
            self,
            request: models.DescribeListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenersResponse:
        """
        This API is used to query listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        Query asynchronous task result
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccelerateAreas(
            self,
            request: models.ModifyAccelerateAreasRequest,
            opts: Dict = None,
    ) -> models.ModifyAccelerateAreasResponse:
        """
        Modify acceleration region
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccelerateAreas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccelerateAreasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccessLogStatus(
            self,
            request: models.ModifyAccessLogStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAccessLogStatusResponse:
        """
        Modify the status of a log task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccessLogStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccessLogStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEndpointGroup(
            self,
            request: models.ModifyEndpointGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyEndpointGroupResponse:
        """
        This API is used to modify a terminal node group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEndpointGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEndpointGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyForwardingPolicy(
            self,
            request: models.ModifyForwardingPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyForwardingPolicyResponse:
        """
        Modify a layer-7 forwarding policy
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyForwardingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyForwardingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyForwardingRule(
            self,
            request: models.ModifyForwardingRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyForwardingRuleResponse:
        """
        This API is used to modify a Layer 7 forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyForwardingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyForwardingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAccelerator(
            self,
            request: models.ModifyGlobalAcceleratorRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorResponse:
        """
        Modify a global acceleration instance
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAccelerator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAcceleratorAccessLog(
            self,
            request: models.ModifyGlobalAcceleratorAccessLogRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorAccessLogResponse:
        """
        Modify GA access logs
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAcceleratorAccessLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorAccessLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAcceleratorAclPolicy(
            self,
            request: models.ModifyGlobalAcceleratorAclPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorAclPolicyResponse:
        """
        Modify the status of an access control policy
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAcceleratorAclPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorAclPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalAcceleratorAclRule(
            self,
            request: models.ModifyGlobalAcceleratorAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalAcceleratorAclRuleResponse:
        """
        Modify ACL rules
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalAcceleratorAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalAcceleratorAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyListener(
            self,
            request: models.ModifyListenerRequest,
            opts: Dict = None,
    ) -> models.ModifyListenerResponse:
        """
        Modify a listener
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceListenerAdditionalCert(
            self,
            request: models.ReplaceListenerAdditionalCertRequest,
            opts: Dict = None,
    ) -> models.ReplaceListenerAdditionalCertResponse:
        """
        Replace the extension certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceListenerAdditionalCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceListenerAdditionalCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)