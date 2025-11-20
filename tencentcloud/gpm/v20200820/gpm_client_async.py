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
from tencentcloud.gpm.v20200820 import models
from typing import Dict


class GpmClient(AbstractClient):
    _apiVersion = '2020-08-20'
    _endpoint = 'gpm.intl.tencentcloudapi.com'
    _service = 'gpm'

    async def CancelMatching(
            self,
            request: models.CancelMatchingRequest,
            opts: Dict = None,
    ) -> models.CancelMatchingResponse:
        """
        This API is used to cancel matching.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelMatching"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelMatchingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMatch(
            self,
            request: models.CreateMatchRequest,
            opts: Dict = None,
    ) -> models.CreateMatchResponse:
        """
        This API is used to create a match.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        This API is used to create a rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMatch(
            self,
            request: models.DeleteMatchRequest,
            opts: Dict = None,
    ) -> models.DeleteMatchResponse:
        """
        This API is used to delete a match.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        This API is used to delete a rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeData(
            self,
            request: models.DescribeDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDataResponse:
        """
        This API is used to view statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMatch(
            self,
            request: models.DescribeMatchRequest,
            opts: Dict = None,
    ) -> models.DescribeMatchResponse:
        """
        This API is used to query the matchmaking details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMatchCodes(
            self,
            request: models.DescribeMatchCodesRequest,
            opts: Dict = None,
    ) -> models.DescribeMatchCodesResponse:
        """
        This API is used to query the created MatchCodes and paginate the query result.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMatchCodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMatchCodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMatches(
            self,
            request: models.DescribeMatchesRequest,
            opts: Dict = None,
    ) -> models.DescribeMatchesResponse:
        """
        This API is used to query the matchmaking list and paginate the query result.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMatches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMatchesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMatchingProgress(
            self,
            request: models.DescribeMatchingProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeMatchingProgressResponse:
        """
        This API is used to query the matching progress.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMatchingProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMatchingProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRule(
            self,
            request: models.DescribeRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleResponse:
        """
        This API is used to query the rule details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        This API is used to query the rule set list and paginate the query result.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeToken(
            self,
            request: models.DescribeTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeTokenResponse:
        """
        This API is used to query the token of a Matchcode, which is used for verified the pushed message.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMatch(
            self,
            request: models.ModifyMatchRequest,
            opts: Dict = None,
    ) -> models.ModifyMatchResponse:
        """
        This API is used to modify a match.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRule(
            self,
            request: models.ModifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleResponse:
        """
        This API is used to modify a rule (including description and tag).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyToken(
            self,
            request: models.ModifyTokenRequest,
            opts: Dict = None,
    ) -> models.ModifyTokenResponse:
        """
        This API is used to modify the token of a Matchcode.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMatching(
            self,
            request: models.StartMatchingRequest,
            opts: Dict = None,
    ) -> models.StartMatchingResponse:
        """
        This API is used to pass in one player or multiple players to initiate match. Players within the same request will be assigned to the same game session.
        """
        
        kwargs = {}
        kwargs["action"] = "StartMatching"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMatchingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartMatchingBackfill(
            self,
            request: models.StartMatchingBackfillRequest,
            opts: Dict = None,
    ) -> models.StartMatchingBackfillResponse:
        """
        This API is used to send a match backfill request, for which a MatchTicket will be searched to start a new match.
        """
        
        kwargs = {}
        kwargs["action"] = "StartMatchingBackfill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartMatchingBackfillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)