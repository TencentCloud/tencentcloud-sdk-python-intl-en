# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.gse.v20191112 import models


class GseClient(AbstractClient):
    _apiVersion = '2019-11-12'
    _endpoint = 'gse.intl.tencentcloudapi.com'
    _service = 'gse'


    def CopyFleet(self, request):
        """This API is used to replicate server fleet.

        :param request: Request instance for CopyFleet.
        :type request: :class:`tencentcloud.gse.v20191112.models.CopyFleetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CopyFleetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyFleet", params, headers=headers)
            response = json.loads(body)
            model = models.CopyFleetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGameServerSession(self, request):
        """This API is used to create a game server session.

        :param request: Request instance for CreateGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGameServerSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGameServerSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTimerScalingPolicy(self, request):
        """This API (DeleteTimerScalingPolicy) is used to delete a scheduled scaling policy of a fleet.

        :param request: Request instance for DeleteTimerScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteTimerScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteTimerScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTimerScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTimerScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGameServerSessionDetails(self, request):
        """This API is used to query the list of game server session details.

        :param request: Request instance for DescribeGameServerSessionDetails.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionDetailsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGameServerSessionDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGameServerSessionDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGameServerSessionPlacement(self, request):
        """This API is used to query the placement of a game server session.

        :param request: Request instance for DescribeGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGameServerSessionPlacement", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGameServerSessionPlacementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGameServerSessions(self, request):
        """This API is used to query the list of game server sessions.

        :param request: Request instance for DescribeGameServerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGameServerSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGameServerSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTypes(self, request):
        """This API is used to obtain the list of CVM types in the specified region.

        :param request: Request instance for DescribeInstanceTypes.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceTypesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlayerSessions(self, request):
        """This API is used to get the list of player sessions.

        :param request: Request instance for DescribePlayerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribePlayerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribePlayerSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlayerSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlayerSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimerScalingPolicies(self, request):
        """This API (DescribeTimerScalingPolicies) is used to query the scheduled scaling policies of a fleet. You can query the policies by `fleetID` or the fleet name. The returned results are paged.

        :param request: Request instance for DescribeTimerScalingPolicies.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeTimerScalingPoliciesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeTimerScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimerScalingPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimerScalingPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EndGameServerSessionAndProcess(self, request):
        """This API is used to terminate the game server session and the corresponding process, which is applicable to time-limited protection and no protection.

        :param request: Request instance for EndGameServerSessionAndProcess.
        :type request: :class:`tencentcloud.gse.v20191112.models.EndGameServerSessionAndProcessRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.EndGameServerSessionAndProcessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EndGameServerSessionAndProcess", params, headers=headers)
            response = json.loads(body)
            model = models.EndGameServerSessionAndProcessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGameServerSessionLogUrl(self, request):
        """This API is used to get the log URL of a game server session.

        :param request: Request instance for GetGameServerSessionLogUrl.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetGameServerSessionLogUrlRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetGameServerSessionLogUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGameServerSessionLogUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GetGameServerSessionLogUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetInstanceAccess(self, request):
        """This API is used to get the credentials required for instance login.

        :param request: Request instance for GetInstanceAccess.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetInstanceAccessRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetInstanceAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInstanceAccess", params, headers=headers)
            response = json.loads(body)
            model = models.GetInstanceAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def JoinGameServerSession(self, request):
        """This API is used to join a game server session.

        :param request: Request instance for JoinGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("JoinGameServerSession", params, headers=headers)
            response = json.loads(body)
            model = models.JoinGameServerSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def JoinGameServerSessionBatch(self, request):
        """This API is used to join game server sessions in batch.

        :param request: Request instance for JoinGameServerSessionBatch.
        :type request: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionBatchRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("JoinGameServerSessionBatch", params, headers=headers)
            response = json.loads(body)
            model = models.JoinGameServerSessionBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutTimerScalingPolicy(self, request):
        """This API (PutTimerScalingPolicy) is used to create or update a scheduled scaling policy for a fleet.

        If the field `timerID` is filled in, the specified policy will be updated, and if `timerID` is left empty, a new policy will be created.

        :param request: Request instance for PutTimerScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.PutTimerScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.PutTimerScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutTimerScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.PutTimerScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchGameServerSessions(self, request):
        """This API is used to search in the list of game server sessions.

        :param request: Request instance for SearchGameServerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.SearchGameServerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.SearchGameServerSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchGameServerSessions", params, headers=headers)
            response = json.loads(body)
            model = models.SearchGameServerSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetServerReserved(self, request):
        """This API (SetServerReserved) is used to mark the exceptional instances as retained for troubleshooting.

        `ReserveValue`: specifies whether to retain the instance. Valid values: `0` (do not retain), `1` (retain). Default value: `0`.

        :param request: Request instance for SetServerReserved.
        :type request: :class:`tencentcloud.gse.v20191112.models.SetServerReservedRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.SetServerReservedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetServerReserved", params, headers=headers)
            response = json.loads(body)
            model = models.SetServerReservedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartGameServerSessionPlacement(self, request):
        """This API is used to start placing a game server session.

        :param request: Request instance for StartGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.StartGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StartGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartGameServerSessionPlacement", params, headers=headers)
            response = json.loads(body)
            model = models.StartGameServerSessionPlacementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopGameServerSessionPlacement(self, request):
        """This API is used to stop placing a game server session.

        :param request: Request instance for StopGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.StopGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StopGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopGameServerSessionPlacement", params, headers=headers)
            response = json.loads(body)
            model = models.StopGameServerSessionPlacementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBucketAccelerateOpt(self, request):
        """This API (UpdateBucketAccelerateOpt) is used to enable COS global acceleration.

        :param request: Request instance for UpdateBucketAccelerateOpt.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateBucketAccelerateOptRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateBucketAccelerateOptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBucketAccelerateOpt", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBucketAccelerateOptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBucketCORSOpt(self, request):
        """This API (UpdateBucketCORSOpt) is used to configure CORS for COS.

        :param request: Request instance for UpdateBucketCORSOpt.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateBucketCORSOptRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateBucketCORSOptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBucketCORSOpt", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBucketCORSOptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGameServerSession(self, request):
        """This API is used to update a game server session.

        :param request: Request instance for UpdateGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGameServerSession", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGameServerSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))