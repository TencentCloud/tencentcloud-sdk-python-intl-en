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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.eb.v20210416 import models


class EbClient(AbstractClient):
    _apiVersion = '2021-04-16'
    _endpoint = 'eb.intl.tencentcloudapi.com'
    _service = 'eb'


    def CheckRule(self, request):
        """This API is used to check a rule.

        :param request: Request instance for CheckRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.CheckRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CheckRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRule", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTransformation(self, request):
        """This API is used to test rules and data on the ETL configuration page.

        :param request: Request instance for CheckTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CheckTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CheckTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConnection(self, request):
        """This API is used to create an event connector.

        :param request: Request instance for CreateConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEventBus(self, request):
        """This API is used to create an event bus.

        :param request: Request instance for CreateEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """This API is used to create an event rule.

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateRuleResponse`

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


    def CreateTarget(self, request):
        """This API is used to create a delivery target.

        :param request: Request instance for CreateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTarget", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTransformation(self, request):
        """This API is used to create a transformer.

        :param request: Request instance for CreateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.CreateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.CreateTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConnection(self, request):
        """This API is used to delete an event connector.

        :param request: Request instance for DeleteConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEventBus(self, request):
        """This API is used to delete an event bus.

        :param request: Request instance for DeleteEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """This API is used to delete an event rule.

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteRuleResponse`

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


    def DeleteTarget(self, request):
        """This API is used to delete a delivery target.

        :param request: Request instance for DeleteTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTarget", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTransformation(self, request):
        """This API is used to delete a transformer.

        :param request: Request instance for DeleteTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DeleteTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogTagValue(self, request):
        """This API is used to query log searching metric values.

        :param request: Request instance for DescribeLogTagValue.
        :type request: :class:`tencentcloud.eb.v20210416.models.DescribeLogTagValueRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.DescribeLogTagValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogTagValue", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogTagValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEventBus(self, request):
        """This API is used to get the details of an event bus.

        :param request: Request instance for GetEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.GetEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRule(self, request):
        """This API is used to get the details of an event rule.

        :param request: Request instance for GetRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRule", params, headers=headers)
            response = json.loads(body)
            model = models.GetRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTransformation(self, request):
        """This API is used to get the details of a transformer.

        :param request: Request instance for GetTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.GetTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.GetTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.GetTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListConnections(self, request):
        """This API is used to get the list of event connectors.

        :param request: Request instance for ListConnections.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListConnectionsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListConnections", params, headers=headers)
            response = json.loads(body)
            model = models.ListConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEventBuses(self, request):
        """This API is used to get the list of event buses.

        :param request: Request instance for ListEventBuses.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListEventBusesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListEventBusesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEventBuses", params, headers=headers)
            response = json.loads(body)
            model = models.ListEventBusesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRules(self, request):
        """This API is used to get the list of event rules.

        :param request: Request instance for ListRules.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListRulesRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRules", params, headers=headers)
            response = json.loads(body)
            model = models.ListRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTargets(self, request):
        """This API is used to get the list delivery targets.

        :param request: Request instance for ListTargets.
        :type request: :class:`tencentcloud.eb.v20210416.models.ListTargetsRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.ListTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTargets", params, headers=headers)
            response = json.loads(body)
            model = models.ListTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchLog(self, request):
        """This API is used to query logs.

        :param request: Request instance for SearchLog.
        :type request: :class:`tencentcloud.eb.v20210416.models.SearchLogRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.SearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateConnection(self, request):
        """This API is used to update an event connector.

        :param request: Request instance for UpdateConnection.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateConnection", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEventBus(self, request):
        """This API is used to update an event bus.

        :param request: Request instance for UpdateEventBus.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateEventBusRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateEventBusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEventBus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEventBusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRule(self, request):
        """This API is used to update an event rule.

        :param request: Request instance for UpdateRule.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateRuleRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTarget(self, request):
        """This API is used to update a delivery target.

        :param request: Request instance for UpdateTarget.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTargetRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTarget", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTransformation(self, request):
        """This API is used to update a transformer.

        :param request: Request instance for UpdateTransformation.
        :type request: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationRequest`
        :rtype: :class:`tencentcloud.eb.v20210416.models.UpdateTransformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTransformation", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTransformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))