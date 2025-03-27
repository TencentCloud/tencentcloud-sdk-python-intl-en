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
from tencentcloud.gpm.v20200820 import models


class GpmClient(AbstractClient):
    _apiVersion = '2020-08-20'
    _endpoint = 'gpm.intl.tencentcloudapi.com'
    _service = 'gpm'


    def CancelMatching(self, request):
        """This API is used to cancel matching.

        :param request: Request instance for CancelMatching.
        :type request: :class:`tencentcloud.gpm.v20200820.models.CancelMatchingRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.CancelMatchingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelMatching", params, headers=headers)
            response = json.loads(body)
            model = models.CancelMatchingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMatch(self, request):
        """This API is used to create a match.

        :param request: Request instance for CreateMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.CreateMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.CreateMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMatch", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """This API is used to create a rule.

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMatch(self, request):
        """This API is used to delete a match.

        :param request: Request instance for DeleteMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DeleteMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DeleteMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMatch", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """This API is used to delete a rule.

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeData(self, request):
        """This API is used to view statistics.

        :param request: Request instance for DescribeData.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeDataRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMatch(self, request):
        """This API is used to query the matchmaking details.

        :param request: Request instance for DescribeMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMatchCodes(self, request):
        """This API is used to query the created MatchCodes and paginate the query result.

        :param request: Request instance for DescribeMatchCodes.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchCodesRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatchCodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMatchCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMatches(self, request):
        """This API is used to query the matchmaking list and paginate the query result.

        :param request: Request instance for DescribeMatches.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchesRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatches", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMatchesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMatchingProgress(self, request):
        """This API is used to query the matching progress.

        :param request: Request instance for DescribeMatchingProgress.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchingProgressRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeMatchingProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMatchingProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMatchingProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRule(self, request):
        """This API is used to query the rule details.

        :param request: Request instance for DescribeRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRules(self, request):
        """This API is used to query the rule set list and paginate the query result.

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeToken(self, request):
        """This API is used to query the token of a Matchcode, which is used for verified the pushed message.

        :param request: Request instance for DescribeToken.
        :type request: :class:`tencentcloud.gpm.v20200820.models.DescribeTokenRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.DescribeTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMatch(self, request):
        """This API is used to modify a match.

        :param request: Request instance for ModifyMatch.
        :type request: :class:`tencentcloud.gpm.v20200820.models.ModifyMatchRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ModifyMatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        """This API is used to modify a rule (including description and tag).

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.gpm.v20200820.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyToken(self, request):
        """This API is used to modify the token of a Matchcode.

        :param request: Request instance for ModifyToken.
        :type request: :class:`tencentcloud.gpm.v20200820.models.ModifyTokenRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.ModifyTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyToken", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMatching(self, request):
        """This API is used to pass in one player or multiple players to initiate match. Players within the same request will be assigned to the same game session.

        :param request: Request instance for StartMatching.
        :type request: :class:`tencentcloud.gpm.v20200820.models.StartMatchingRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.StartMatchingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMatching", params, headers=headers)
            response = json.loads(body)
            model = models.StartMatchingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMatchingBackfill(self, request):
        """This API is used to send a match backfill request, for which a MatchTicket will be searched to start a new match.

        :param request: Request instance for StartMatchingBackfill.
        :type request: :class:`tencentcloud.gpm.v20200820.models.StartMatchingBackfillRequest`
        :rtype: :class:`tencentcloud.gpm.v20200820.models.StartMatchingBackfillResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMatchingBackfill", params, headers=headers)
            response = json.loads(body)
            model = models.StartMatchingBackfillResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))