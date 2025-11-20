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
from tencentcloud.gse.v20191112 import models
from typing import Dict


class GseClient(AbstractClient):
    _apiVersion = '2019-11-12'
    _endpoint = 'gse.intl.tencentcloudapi.com'
    _service = 'gse'

    async def CopyFleet(
            self,
            request: models.CopyFleetRequest,
            opts: Dict = None,
    ) -> models.CopyFleetResponse:
        """
        This API is used to replicate server fleet.
        """
        
        kwargs = {}
        kwargs["action"] = "CopyFleet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyFleetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGameServerSession(
            self,
            request: models.CreateGameServerSessionRequest,
            opts: Dict = None,
    ) -> models.CreateGameServerSessionResponse:
        """
        This API is used to create a game server session.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGameServerSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGameServerSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTimerScalingPolicy(
            self,
            request: models.DeleteTimerScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteTimerScalingPolicyResponse:
        """
        This API (DeleteTimerScalingPolicy) is used to delete a scheduled scaling policy of a fleet.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTimerScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTimerScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGameServerSessionDetails(
            self,
            request: models.DescribeGameServerSessionDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeGameServerSessionDetailsResponse:
        """
        This API is used to query the list of game server session details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGameServerSessionDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGameServerSessionDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGameServerSessionPlacement(
            self,
            request: models.DescribeGameServerSessionPlacementRequest,
            opts: Dict = None,
    ) -> models.DescribeGameServerSessionPlacementResponse:
        """
        This API is used to query the placement of a game server session.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGameServerSessionPlacement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGameServerSessionPlacementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGameServerSessions(
            self,
            request: models.DescribeGameServerSessionsRequest,
            opts: Dict = None,
    ) -> models.DescribeGameServerSessionsResponse:
        """
        This API is used to query the list of game server sessions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGameServerSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGameServerSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTypes(
            self,
            request: models.DescribeInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTypesResponse:
        """
        This API is used to obtain the list of CVM types in the specified region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlayerSessions(
            self,
            request: models.DescribePlayerSessionsRequest,
            opts: Dict = None,
    ) -> models.DescribePlayerSessionsResponse:
        """
        This API is used to get the list of player sessions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlayerSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlayerSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimerScalingPolicies(
            self,
            request: models.DescribeTimerScalingPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeTimerScalingPoliciesResponse:
        """
        This API (DescribeTimerScalingPolicies) is used to query the scheduled scaling policies of a fleet. You can query the policies by `fleetID` or the fleet name. The returned results are paged.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimerScalingPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimerScalingPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EndGameServerSessionAndProcess(
            self,
            request: models.EndGameServerSessionAndProcessRequest,
            opts: Dict = None,
    ) -> models.EndGameServerSessionAndProcessResponse:
        """
        This API is used to terminate the game server session and the corresponding process, which is applicable to time-limited protection and no protection.
        """
        
        kwargs = {}
        kwargs["action"] = "EndGameServerSessionAndProcess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EndGameServerSessionAndProcessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGameServerSessionLogUrl(
            self,
            request: models.GetGameServerSessionLogUrlRequest,
            opts: Dict = None,
    ) -> models.GetGameServerSessionLogUrlResponse:
        """
        This API is used to get the log URL of a game server session.
        """
        
        kwargs = {}
        kwargs["action"] = "GetGameServerSessionLogUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGameServerSessionLogUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetInstanceAccess(
            self,
            request: models.GetInstanceAccessRequest,
            opts: Dict = None,
    ) -> models.GetInstanceAccessResponse:
        """
        This API is used to get the credentials required for instance login.
        """
        
        kwargs = {}
        kwargs["action"] = "GetInstanceAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetInstanceAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def JoinGameServerSession(
            self,
            request: models.JoinGameServerSessionRequest,
            opts: Dict = None,
    ) -> models.JoinGameServerSessionResponse:
        """
        This API is used to join a game server session.
        """
        
        kwargs = {}
        kwargs["action"] = "JoinGameServerSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.JoinGameServerSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def JoinGameServerSessionBatch(
            self,
            request: models.JoinGameServerSessionBatchRequest,
            opts: Dict = None,
    ) -> models.JoinGameServerSessionBatchResponse:
        """
        This API is used to join game server sessions in batch.
        """
        
        kwargs = {}
        kwargs["action"] = "JoinGameServerSessionBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.JoinGameServerSessionBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutTimerScalingPolicy(
            self,
            request: models.PutTimerScalingPolicyRequest,
            opts: Dict = None,
    ) -> models.PutTimerScalingPolicyResponse:
        """
        This API (PutTimerScalingPolicy) is used to create or update a scheduled scaling policy for a fleet.

        If the field `timerID` is filled in, the specified policy will be updated, and if `timerID` is left empty, a new policy will be created.
        """
        
        kwargs = {}
        kwargs["action"] = "PutTimerScalingPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutTimerScalingPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchGameServerSessions(
            self,
            request: models.SearchGameServerSessionsRequest,
            opts: Dict = None,
    ) -> models.SearchGameServerSessionsResponse:
        """
        This API is used to search in the list of game server sessions.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchGameServerSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchGameServerSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetServerReserved(
            self,
            request: models.SetServerReservedRequest,
            opts: Dict = None,
    ) -> models.SetServerReservedResponse:
        """
        This API (SetServerReserved) is used to mark the exceptional instances as retained for troubleshooting.

        `ReserveValue`: specifies whether to retain the instance. Valid values: `0` (do not retain), `1` (retain). Default value: `0`.
        """
        
        kwargs = {}
        kwargs["action"] = "SetServerReserved"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetServerReservedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartGameServerSessionPlacement(
            self,
            request: models.StartGameServerSessionPlacementRequest,
            opts: Dict = None,
    ) -> models.StartGameServerSessionPlacementResponse:
        """
        This API is used to start placing a game server session.
        """
        
        kwargs = {}
        kwargs["action"] = "StartGameServerSessionPlacement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartGameServerSessionPlacementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopGameServerSessionPlacement(
            self,
            request: models.StopGameServerSessionPlacementRequest,
            opts: Dict = None,
    ) -> models.StopGameServerSessionPlacementResponse:
        """
        This API is used to stop placing a game server session.
        """
        
        kwargs = {}
        kwargs["action"] = "StopGameServerSessionPlacement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopGameServerSessionPlacementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateBucketAccelerateOpt(
            self,
            request: models.UpdateBucketAccelerateOptRequest,
            opts: Dict = None,
    ) -> models.UpdateBucketAccelerateOptResponse:
        """
        This API (UpdateBucketAccelerateOpt) is used to enable COS global acceleration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateBucketAccelerateOpt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateBucketAccelerateOptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateBucketCORSOpt(
            self,
            request: models.UpdateBucketCORSOptRequest,
            opts: Dict = None,
    ) -> models.UpdateBucketCORSOptResponse:
        """
        This API (UpdateBucketCORSOpt) is used to configure CORS for COS.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateBucketCORSOpt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateBucketCORSOptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGameServerSession(
            self,
            request: models.UpdateGameServerSessionRequest,
            opts: Dict = None,
    ) -> models.UpdateGameServerSessionResponse:
        """
        This API is used to update a game server session.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGameServerSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGameServerSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)