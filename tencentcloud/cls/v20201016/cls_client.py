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
from tencentcloud.cls.v20201016 import models


class ClsClient(AbstractClient):
    _apiVersion = '2020-10-16'
    _endpoint = 'cls.intl.tencentcloudapi.com'
    _service = 'cls'


    def AddMachineGroupInfo(self, request):
        r"""This API is used to add machine group information.

        :param request: Request instance for AddMachineGroupInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.AddMachineGroupInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.AddMachineGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddMachineGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddMachineGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplyConfigToMachineGroup(self, request):
        r"""This API is used to apply the collection configuration to a specified machine group.

        :param request: Request instance for ApplyConfigToMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.ApplyConfigToMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ApplyConfigToMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyConfigToMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyConfigToMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelRebuildIndexTask(self, request):
        r"""This API is used to cancel creating a reindexing task.

        :param request: Request instance for CancelRebuildIndexTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.CancelRebuildIndexTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CancelRebuildIndexTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelRebuildIndexTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelRebuildIndexTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChatCompletions(self, request):
        r"""Call the API to initiate a dialogue request.
        This API supports AI-powered logging features such as intelligently generating retrieval analysis statements.
        Note: When calling this API via SSE streaming, ensure the request domain name is set to cls.ai.tencentcloudapi.com (configurable as cls.ai.internal.tencentcloudapi.com in a private network environment).

        :param request: Request instance for ChatCompletions.
        :type request: :class:`tencentcloud.cls.v20201016.models.ChatCompletionsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ChatCompletionsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ChatCompletions", params, models.ChatCompletionsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckFunction(self, request):
        r"""This API is used to verify the syntax of data processing DSL functions.

        :param request: Request instance for CheckFunction.
        :type request: :class:`tencentcloud.cls.v20201016.models.CheckFunctionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CheckFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CheckFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckRechargeKafkaServer(self, request):
        r"""This API is used to check whether the Kafka service cluster is accessible.

        :param request: Request instance for CheckRechargeKafkaServer.
        :type request: :class:`tencentcloud.cls.v20201016.models.CheckRechargeKafkaServerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CheckRechargeKafkaServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRechargeKafkaServer", params, headers=headers)
            response = json.loads(body)
            model = models.CheckRechargeKafkaServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseKafkaConsumer(self, request):
        r"""This API is used to disable Kafka consumption.

        :param request: Request instance for CloseKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.CloseKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CloseKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.CloseKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitConsumerOffsets(self, request):
        r"""This API is used to submit a consumption offset.

        :param request: Request instance for CommitConsumerOffsets.
        :type request: :class:`tencentcloud.cls.v20201016.models.CommitConsumerOffsetsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CommitConsumerOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitConsumerOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.CommitConsumerOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlarm(self, request):
        r"""This API is used to create an alarm policy.

        :param request: Request instance for CreateAlarm.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateAlarmRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlarmNotice(self, request):
        r"""This API is used to create a notification channel group with two configuration modes to choose from.
        1. Easy mode provides the most basic notification channel function. The following parameters are required:
        - Type
        - NoticeReceivers
        - WebCallbacks

        2. Advanced mode: On the basis of easy mode, it supports setting rules, setting notification channels for different types of alarms, and escalating alarms. The following parameters are required:
        - NoticeRules

        :param request: Request instance for CreateAlarmNotice.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarmNotice", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlarmShield(self, request):
        r"""This API is used to create an alarm blocking rule.

        :param request: Request instance for CreateAlarmShield.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateAlarmShieldRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateAlarmShieldResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarmShield", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmShieldResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudProductLogCollection(self, request):
        r"""Cloud product integration uses internal APIs

        :param request: Request instance for CreateCloudProductLogCollection.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateCloudProductLogCollectionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateCloudProductLogCollectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudProductLogCollection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudProductLogCollectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConfig(self, request):
        r"""This API is used to create collection rule configuration.

        :param request: Request instance for CreateConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsole(self, request):
        r"""This API is used to create the DataSight Console

        :param request: Request instance for CreateConsole.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConsoleRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConsoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumer(self, request):
        r"""This API is used to create a CKafka delivery task.

        :param request: Request instance for CreateConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumerGroup(self, request):
        r"""This API is used to check the heartbeat of a consumer group.

        :param request: Request instance for CreateConsumerGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateConsumerGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCosRecharge(self, request):
        r"""This API is used to create a COS import task.

        :param request: Request instance for CreateCosRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateCosRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateCosRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCosRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDashboard(self, request):
        r"""This API is used to create a dashboard.

        :param request: Request instance for CreateDashboard.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDashboardRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDashboardSubscribe(self, request):
        r"""This API is used to create a dashboard subscription.

        :param request: Request instance for CreateDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDataTransform(self, request):
        r"""This API is used to create a data processing task.

        :param request: Request instance for CreateDataTransform.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDataTransformRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDataTransformResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataTransform", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataTransformResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeliverCloudFunction(self, request):
        r"""This API is used to create a delivery SCF task.

        :param request: Request instance for CreateDeliverCloudFunction.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDeliverCloudFunctionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDeliverCloudFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeliverCloudFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeliverCloudFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDlcDeliver(self, request):
        r"""Create a DLC delivery task

        :param request: Request instance for CreateDlcDeliver.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateDlcDeliverRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateDlcDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDlcDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDlcDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEsRecharge(self, request):
        r"""This API is used to create an es import configuration

        :param request: Request instance for CreateEsRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateEsRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateEsRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEsRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEsRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExport(self, request):
        r"""This API only creates download tasks. The download address returned by the task can be obtained by user invocation of [DescribeExports](https://www.tencentcloud.com/document/product/614/56449?from_cn_redirect=1) to view task list, which includes the CosPath parameter for the download address.

        :param request: Request instance for CreateExport.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateExportRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostMetricConfig(self, request):
        r"""This API is used to create host metric collection configurations.

        :param request: Request instance for CreateHostMetricConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateHostMetricConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateHostMetricConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostMetricConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostMetricConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIndex(self, request):
        r"""This API is used to create an index.

        :param request: Request instance for CreateIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIndex", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKafkaRecharge(self, request):
        r"""This API is used to create a Kafka data subscription task.

        :param request: Request instance for CreateKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLogset(self, request):
        r"""This API is used to create a logset. The ID of the created logset is returned.

        :param request: Request instance for CreateLogset.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateLogsetRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMachineGroup(self, request):
        r"""This API is used to create a machine group.

        :param request: Request instance for CreateMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMetricConfig(self, request):
        r"""This API is used to create metric collection configurations.

        :param request: Request instance for CreateMetricConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateMetricConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateMetricConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMetricConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMetricConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMetricSubscribe(self, request):
        r"""This API is used to create metric subscription configurations.

        :param request: Request instance for CreateMetricSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateMetricSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateMetricSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMetricSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMetricSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkApplication(self, request):
        r"""This API is used to create a network application.

        :param request: Request instance for CreateNetworkApplication.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateNetworkApplicationRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateNetworkApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNoticeContent(self, request):
        r"""This API is used to create notification content.

        :param request: Request instance for CreateNoticeContent.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateNoticeContentRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateNoticeContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNoticeContent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNoticeContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRebuildIndexTask(self, request):
        r"""This API is used to creates rebuild index tasks.
        Note:
        -A single log topic allows only one index reconstruction task at a time and can have up to 10 rebuild index task records. Delete task records that are no longer needed before creating an index task.
        -Logs within the same time range only allow rebuilding indexes once. Delete previous task records before rebuilding again.
        -Deleting a rebuild index task record restores the index data before rebuilding an index.
        -The log write traffic of the selected time range cannot exceed 5TB.
        -The index rebuilding time range is subject to the log time. When the log uploading time has a deviation exceeding one hour from the index rebuilding time range (for example, reporting a new log at 16:00 for 02:00 to CLS and rebuilding the log index for 00:00–12:00), the logs will not be rebuilt and cannot be retrieved subsequently. When reporting a new log to the reconstructed log time range, it will not be rebuilt and cannot be retrieved subsequently.

        :param request: Request instance for CreateRebuildIndexTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateRebuildIndexTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateRebuildIndexTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRebuildIndexTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRebuildIndexTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordingRuleTask(self, request):
        r"""Creating a Metric Pre-Aggregation Task

        :param request: Request instance for CreateRecordingRuleTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateRecordingRuleTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateRecordingRuleTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordingRuleTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordingRuleTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecordingRuleYamlTask(self, request):
        r"""Creating a Metric Pre-Aggregation Task Through a YAML File

        :param request: Request instance for CreateRecordingRuleYamlTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateRecordingRuleYamlTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateRecordingRuleYamlTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordingRuleYamlTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecordingRuleYamlTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScheduledSql(self, request):
        r"""This API is used to create a scheduled SQL analysis task.

        :param request: Request instance for CreateScheduledSql.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateScheduledSqlRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateScheduledSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScheduledSql", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScheduledSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchView(self, request):
        r"""Create a query view

        :param request: Request instance for CreateSearchView.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateSearchViewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateSearchViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchView", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSearchViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateShipper(self, request):
        r"""This API is used to create a task to ship to COS. Note: To use this API, you need to check whether you have configured the role and permission for shipping to COS. If not, see **Viewing and Configuring Shipping Authorization** at https://intl.cloud.tencent.com/document/product/614/71623.?from_cn_redirect=1

        :param request: Request instance for CreateShipper.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateShipperRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateShipperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateShipper", params, headers=headers)
            response = json.loads(body)
            model = models.CreateShipperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSplunkDeliver(self, request):
        r"""Create a Splunk delivery task

        :param request: Request instance for CreateSplunkDeliver.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateSplunkDeliverRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateSplunkDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSplunkDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSplunkDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        r"""This API is used to create logs or metric topics.

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWebCallback(self, request):
        r"""This API is used to create alarm channel callback configurations.

        :param request: Request instance for CreateWebCallback.
        :type request: :class:`tencentcloud.cls.v20201016.models.CreateWebCallbackRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.CreateWebCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebCallback", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWebCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlarm(self, request):
        r"""This API is used to delete an alarm policy.

        :param request: Request instance for DeleteAlarm.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlarmNotice(self, request):
        r"""This API is used to delete a notification group.

        :param request: Request instance for DeleteAlarmNotice.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmNotice", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlarmShield(self, request):
        r"""This API is used to delete an alarm blocking rule. When the alarm blocking rule is active or invalid, it cannot be deleted.

        :param request: Request instance for DeleteAlarmShield.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmShieldRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteAlarmShieldResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmShield", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmShieldResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudProductLogCollection(self, request):
        r"""Cloud product integration uses internal APIs

        :param request: Request instance for DeleteCloudProductLogCollection.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteCloudProductLogCollectionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteCloudProductLogCollectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudProductLogCollection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudProductLogCollectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfig(self, request):
        r"""This API is used to delete collection rule configuration.

        :param request: Request instance for DeleteConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConfigFromMachineGroup(self, request):
        r"""This API is used to delete the collection configuration applied to a machine group.

        :param request: Request instance for DeleteConfigFromMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConfigFromMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConfigFromMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConfigFromMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConfigFromMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsole(self, request):
        r"""This API is used to delete the DataSight Console

        :param request: Request instance for DeleteConsole.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConsoleRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConsoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsole", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsumer(self, request):
        r"""Deleting a CKafka Delivery Task

        :param request: Request instance for DeleteConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConsumerGroup(self, request):
        r"""Delete consumer groups.

        :param request: Request instance for DeleteConsumerGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteConsumerGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCosRecharge(self, request):
        r"""This API is used to delete a cos Import Task.

        :param request: Request instance for DeleteCosRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteCosRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteCosRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCosRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCosRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDashboard(self, request):
        r"""This API is used to delete dashboards.

        :param request: Request instance for DeleteDashboard.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteDashboardRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDashboardSubscribe(self, request):
        r"""This API is used to delete dashboard subscriptions.

        :param request: Request instance for DeleteDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataTransform(self, request):
        r"""This API is used to delete a data processing task.

        :param request: Request instance for DeleteDataTransform.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteDataTransformRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteDataTransformResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataTransform", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataTransformResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDlcDeliver(self, request):
        r"""Delete a DLC delivery task

        :param request: Request instance for DeleteDlcDeliver.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteDlcDeliverRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteDlcDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDlcDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDlcDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEsRecharge(self, request):
        r"""Delete es import configuration

        :param request: Request instance for DeleteEsRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteEsRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteEsRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEsRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEsRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteExport(self, request):
        r"""This API is used to delete a log download task.

        :param request: Request instance for DeleteExport.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteExportRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExport", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHostMetricConfig(self, request):
        r"""Delete host metric collection configuration

        :param request: Request instance for DeleteHostMetricConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteHostMetricConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteHostMetricConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHostMetricConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHostMetricConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIndex(self, request):
        r"""This API is used to delete the index configuration of a log topic. After deleting, you cannot retrieve or query the collected logs.

        :param request: Request instance for DeleteIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKafkaRecharge(self, request):
        r"""This API is used to delete a Kafka data subscription task.

        :param request: Request instance for DeleteKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogset(self, request):
        r"""This API is used to delete a logset.

        :param request: Request instance for DeleteLogset.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteLogsetRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogset", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineGroup(self, request):
        r"""This API is used to delete a machine group.

        :param request: Request instance for DeleteMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineGroupInfo(self, request):
        r"""This API is used to delete machine group information.

        :param request: Request instance for DeleteMachineGroupInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteMachineGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMetricConfig(self, request):
        r"""This API is used to delete metric collection configurations.

        :param request: Request instance for DeleteMetricConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteMetricConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteMetricConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMetricConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMetricConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMetricSubscribe(self, request):
        r"""This API is used to delete metric subscription configurations.

        :param request: Request instance for DeleteMetricSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteMetricSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteMetricSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMetricSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMetricSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkApplication(self, request):
        r"""Delete a web application

        :param request: Request instance for DeleteNetworkApplication.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteNetworkApplicationRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteNetworkApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkApplication", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNoticeContent(self, request):
        r"""This API is used to delete notification content configuration.

        :param request: Request instance for DeleteNoticeContent.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteNoticeContentRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteNoticeContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNoticeContent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNoticeContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordingRuleTask(self, request):
        r"""This API is used to delete a pre-aggregation analysis task.

        :param request: Request instance for DeleteRecordingRuleTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteRecordingRuleTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteRecordingRuleTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordingRuleTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordingRuleTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRecordingRuleYamlTask(self, request):
        r"""This API is used to delete the pre-aggregation task in yaml.

        :param request: Request instance for DeleteRecordingRuleYamlTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteRecordingRuleYamlTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteRecordingRuleYamlTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordingRuleYamlTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRecordingRuleYamlTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScheduledSql(self, request):
        r"""This API is used to delete a scheduled SQL analysis task.

        :param request: Request instance for DeleteScheduledSql.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteScheduledSqlRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteScheduledSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScheduledSql", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScheduledSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSearchView(self, request):
        r"""This API is used to delete a query view.

        :param request: Request instance for DeleteSearchView.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteSearchViewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteSearchViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSearchView", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSearchViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteShipper(self, request):
        r"""This API is used to delete a COS shipping task.

        :param request: Request instance for DeleteShipper.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteShipperRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteShipperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteShipper", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteShipperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSplunkDeliver(self, request):
        r"""Delete a Splunk delivery task

        :param request: Request instance for DeleteSplunkDeliver.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteSplunkDeliverRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteSplunkDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSplunkDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSplunkDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        r"""This API is used to delete logs or metric topics.

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebCallback(self, request):
        r"""This API is used to delete alarm channel callback configurations.

        :param request: Request instance for DeleteWebCallback.
        :type request: :class:`tencentcloud.cls.v20201016.models.DeleteWebCallbackRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DeleteWebCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmNotices(self, request):
        r"""This API is used to get the notification group list.

        :param request: Request instance for DescribeAlarmNotices.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmNoticesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNotices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmNoticesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmShields(self, request):
        r"""This API is used to access alarm blocking configuration rules.

        :param request: Request instance for DescribeAlarmShields.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmShieldsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmShieldsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmShields", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmShieldsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarms(self, request):
        r"""This API is used to get the alarm policy list.

        :param request: Request instance for DescribeAlarms.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlarmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlertRecordHistory(self, request):
        r"""This API is used to get alarm records, such as today's uncleared alarms.

        :param request: Request instance for DescribeAlertRecordHistory.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeAlertRecordHistoryRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeAlertRecordHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertRecordHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlertRecordHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudProductLogTasks(self, request):
        r"""Cloud product integration uses relevant APIs

        :param request: Request instance for DescribeCloudProductLogTasks.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeCloudProductLogTasksRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeCloudProductLogTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudProductLogTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudProductLogTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterBaseMetricConfigs(self, request):
        r"""This API is used to obtain metric subscription configurations.

        :param request: Request instance for DescribeClusterBaseMetricConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeClusterBaseMetricConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeClusterBaseMetricConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterBaseMetricConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterBaseMetricConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterMetricConfigs(self, request):
        r"""This API is used to obtain metric subscription configurations.

        :param request: Request instance for DescribeClusterMetricConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeClusterMetricConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeClusterMetricConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterMetricConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterMetricConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigMachineGroups(self, request):
        r"""This API is used to get the machine group bound to collection rule configuration.

        :param request: Request instance for DescribeConfigMachineGroups.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConfigMachineGroupsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConfigMachineGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigMachineGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigMachineGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigs(self, request):
        r"""This API is used to get collection rule configuration.

        :param request: Request instance for DescribeConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsoles(self, request):
        r"""Query the DataSight console instance list

        :param request: Request instance for DescribeConsoles.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsolesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumer(self, request):
        r"""This API is used to query a shipping task.

        :param request: Request instance for DescribeConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerGroups(self, request):
        r"""This API is used to obtain the consumer group list.

        :param request: Request instance for DescribeConsumerGroups.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerGroupsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerOffsets(self, request):
        r"""Obtaining the Consumer Group Point Information

        :param request: Request instance for DescribeConsumerOffsets.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerOffsetsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerPreview(self, request):
        r"""This API is used to preview Kafka shipping data.

        :param request: Request instance for DescribeConsumerPreview.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerPreviewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsumerPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumers(self, request):
        r"""This API is used to obtain the shipping rule information list.

        :param request: Request instance for DescribeConsumers.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeConsumersRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeConsumersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCosRecharges(self, request):
        r"""This API is used to get COS import configuration.

        :param request: Request instance for DescribeCosRecharges.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeCosRechargesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeCosRechargesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCosRecharges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCosRechargesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDashboardSubscribes(self, request):
        r"""This API is used to obtain the dashboard subscription list, and supports paging.

        :param request: Request instance for DescribeDashboardSubscribes.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeDashboardSubscribesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeDashboardSubscribesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDashboardSubscribes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDashboardSubscribesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataTransformInfo(self, request):
        r"""This API is used to get the basic information of data processing tasks.

        :param request: Request instance for DescribeDataTransformInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeDataTransformInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeDataTransformInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataTransformInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataTransformInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDlcDelivers(self, request):
        r"""This API is used to search alarm channel callback configuration lists.

        :param request: Request instance for DescribeDlcDelivers.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeDlcDeliversRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeDlcDeliversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDlcDelivers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDlcDeliversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEsRechargePreview(self, request):
        r"""Import Preview

        :param request: Request instance for DescribeEsRechargePreview.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeEsRechargePreviewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeEsRechargePreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEsRechargePreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEsRechargePreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEsRecharges(self, request):
        r"""Retrieve the es import configuration

        :param request: Request instance for DescribeEsRecharges.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeEsRechargesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeEsRechargesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEsRecharges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEsRechargesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExports(self, request):
        r"""This API is used to get the list of log download tasks.

        :param request: Request instance for DescribeExports.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeExportsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeExportsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExports", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostMetricConfigs(self, request):
        r"""This API is used to obtain metric subscription configurations.

        :param request: Request instance for DescribeHostMetricConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeHostMetricConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeHostMetricConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostMetricConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostMetricConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndex(self, request):
        r"""This API is used to get the index configuration information.

        :param request: Request instance for DescribeIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaConsumer(self, request):
        r"""This API is used to access Kafka protocol consumption information.

        :param request: Request instance for DescribeKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaConsumerGroupDetail(self, request):
        r"""Retrieve Kafka protocol consumption group details

        :param request: Request instance for DescribeKafkaConsumerGroupDetail.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerGroupDetailRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerGroupDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaConsumerGroupDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaConsumerGroupDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaConsumerGroupList(self, request):
        r"""Retrieve the information list of Kafka protocol consumption groups

        :param request: Request instance for DescribeKafkaConsumerGroupList.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerGroupListRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaConsumerGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaConsumerGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaConsumerPreview(self, request):
        r"""This API is used to preview the Kafka consumption.

        :param request: Request instance for DescribeKafkaConsumerPreview.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerPreviewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaConsumerPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaConsumerPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaConsumerTopics(self, request):
        r"""This API is used to obtain the topic information list of Kafka consumption.

        :param request: Request instance for DescribeKafkaConsumerTopics.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerTopicsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaConsumerTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaConsumerTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaConsumerTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKafkaRecharges(self, request):
        r"""This API is used to get the list of Kafka data subscription tasks.

        :param request: Request instance for DescribeKafkaRecharges.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaRechargesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeKafkaRechargesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaRecharges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaRechargesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogContext(self, request):
        r"""This API is used to search for content near the log context. For more details, see [Context Search](https://intl.cloud.tencent.com/document/product/614/53248?from_cn_redirect=1).The maximum value of API's return data packet is 49MB. It is recommended to enable gzip compression (HTTP Request Header Accept-Encoding: gzip).

        :param request: Request instance for DescribeLogContext.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeLogContextRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeLogContextResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogContext", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogContextResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogHistogram(self, request):
        r"""This API is used to get a log count histogram.

        :param request: Request instance for DescribeLogHistogram.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeLogHistogramRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeLogHistogramResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogHistogram", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogHistogramResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogsets(self, request):
        r"""This API is used to get the list of logsets.

        :param request: Request instance for DescribeLogsets.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeLogsetsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeLogsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineGroupConfigs(self, request):
        r"""This API is used to get the collection rule configuration bound to a machine group.

        :param request: Request instance for DescribeMachineGroupConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineGroupConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineGroupConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineGroups(self, request):
        r"""This API is used to get the list of machine groups.

        :param request: Request instance for DescribeMachineGroups.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMachineGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachines(self, request):
        r"""This API is used to get the status of a machine under the specified machine group.

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMetricCorrectDimension(self, request):
        r"""This API is used to obtain metric subscription configurations.

        :param request: Request instance for DescribeMetricCorrectDimension.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMetricCorrectDimensionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMetricCorrectDimensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMetricCorrectDimension", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMetricCorrectDimensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMetricSubscribePreview(self, request):
        r"""This API is used to create metric subscription configurations.

        :param request: Request instance for DescribeMetricSubscribePreview.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMetricSubscribePreviewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMetricSubscribePreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMetricSubscribePreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMetricSubscribePreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMetricSubscribes(self, request):
        r"""This API is used to obtain metric subscription configurations.

        :param request: Request instance for DescribeMetricSubscribes.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeMetricSubscribesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeMetricSubscribesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMetricSubscribes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMetricSubscribesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkApplicationDetail(self, request):
        r"""Retrieve web application details

        :param request: Request instance for DescribeNetworkApplicationDetail.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeNetworkApplicationDetailRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeNetworkApplicationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkApplicationDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkApplicationDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkApplications(self, request):
        r"""Retrieve the network application list

        :param request: Request instance for DescribeNetworkApplications.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeNetworkApplicationsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeNetworkApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNoticeContents(self, request):
        r"""This API is used to obtain the notification content list.

        :param request: Request instance for DescribeNoticeContents.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeNoticeContentsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeNoticeContentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNoticeContents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNoticeContentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePartitions(self, request):
        r"""This API is deprecated. If needed, please use the DescribeTopics API to get the number of partitions.

        :param request: Request instance for DescribePartitions.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribePartitionsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribePartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePartitions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRebuildIndexTasks(self, request):
        r"""This API is used to obtain the list of rebuild index tasks.

        :param request: Request instance for DescribeRebuildIndexTasks.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeRebuildIndexTasksRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeRebuildIndexTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRebuildIndexTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRebuildIndexTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordingRuleTask(self, request):
        r"""This API is used to retrieve the pre-aggregation task list.

        :param request: Request instance for DescribeRecordingRuleTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeRecordingRuleTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeRecordingRuleTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingRuleTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordingRuleTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordingRuleYamlTask(self, request):
        r"""This API is used to retrieve the pre-aggregation task list in yaml.

        :param request: Request instance for DescribeRecordingRuleYamlTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeRecordingRuleYamlTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeRecordingRuleYamlTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingRuleYamlTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordingRuleYamlTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScheduledSqlInfo(self, request):
        r"""This API is used to access the scheduled SQL analysis task list.

        :param request: Request instance for DescribeScheduledSqlInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeScheduledSqlInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeScheduledSqlInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScheduledSqlInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScheduledSqlInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchViews(self, request):
        r"""Query view list

        :param request: Request instance for DescribeSearchViews.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeSearchViewsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeSearchViewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchViews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchViewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShipperTasks(self, request):
        r"""This API is used to get the list of shipping tasks.

        :param request: Request instance for DescribeShipperTasks.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeShipperTasksRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeShipperTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShipperTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShipperTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShippers(self, request):
        r"""This API is used to get the configuration of the task shipped to COS.

        :param request: Request instance for DescribeShippers.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeShippersRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeShippersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShippers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShippersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSplunkDelivers(self, request):
        r"""Retrieve the Splunk delivery task list

        :param request: Request instance for DescribeSplunkDelivers.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeSplunkDeliversRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeSplunkDeliversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSplunkDelivers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSplunkDeliversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSplunkPreview(self, request):
        r"""splunk delivery task preview

        :param request: Request instance for DescribeSplunkPreview.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeSplunkPreviewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeSplunkPreviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSplunkPreview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSplunkPreviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicBaseMetricConfigs(self, request):
        r"""This API is used to obtain metric subscription configurations.

        :param request: Request instance for DescribeTopicBaseMetricConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeTopicBaseMetricConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeTopicBaseMetricConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicBaseMetricConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicBaseMetricConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicMetricConfigs(self, request):
        r"""This API is used to obtain metric subscription configurations.

        :param request: Request instance for DescribeTopicMetricConfigs.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeTopicMetricConfigsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeTopicMetricConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicMetricConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicMetricConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopics(self, request):
        r"""This API is used to obtain logs or metric topic lists and supports pagination.

        :param request: Request instance for DescribeTopics.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeTopicsRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebCallbacks(self, request):
        r"""This API is used to search alarm channel callback configuration lists.

        :param request: Request instance for DescribeWebCallbacks.
        :type request: :class:`tencentcloud.cls.v20201016.models.DescribeWebCallbacksRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.DescribeWebCallbacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebCallbacks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebCallbacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EstimateRebuildIndexTask(self, request):
        r"""This API is used to estimate rebuild index tasks.

        :param request: Request instance for EstimateRebuildIndexTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.EstimateRebuildIndexTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.EstimateRebuildIndexTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EstimateRebuildIndexTask", params, headers=headers)
            response = json.loads(body)
            model = models.EstimateRebuildIndexTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAlarmLog(self, request):
        r"""This API is used to access alarm policy execution details.

        :param request: Request instance for GetAlarmLog.
        :type request: :class:`tencentcloud.cls.v20201016.models.GetAlarmLogRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.GetAlarmLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAlarmLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetAlarmLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetClsService(self, request):
        r"""This API is used to check whether CLS is enabled.
        This API is used to fill in any region for Region, recommend using Guangzhou (ap-guangzhou).

        :param request: Request instance for GetClsService.
        :type request: :class:`tencentcloud.cls.v20201016.models.GetClsServiceRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.GetClsServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetClsService", params, headers=headers)
            response = json.loads(body)
            model = models.GetClsServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetMetricLabelValues(self, request):
        r"""This API is used to obtain the list of time series label values.

        :param request: Request instance for GetMetricLabelValues.
        :type request: :class:`tencentcloud.cls.v20201016.models.GetMetricLabelValuesRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.GetMetricLabelValuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMetricLabelValues", params, headers=headers)
            response = json.loads(body)
            model = models.GetMetricLabelValuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MergePartition(self, request):
        r"""This API is deprecated. If needed, please use the ModifyTopic API to change the number of partitions.

        :param request: Request instance for MergePartition.
        :type request: :class:`tencentcloud.cls.v20201016.models.MergePartitionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.MergePartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MergePartition", params, headers=headers)
            response = json.loads(body)
            model = models.MergePartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarm(self, request):
        r"""This API is used to modify an alarm policy. At least one valid configuration item needs to be modified.

        :param request: Request instance for ModifyAlarm.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarmNotice(self, request):
        r"""This API is used to modify a notification group.

        :param request: Request instance for ModifyAlarmNotice.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmNotice", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmNoticeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarmShield(self, request):
        r"""This API is used to modify alarm blocking rules. When the alarm blocking rule is invalid, it cannot be modified.

        :param request: Request instance for ModifyAlarmShield.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmShieldRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyAlarmShieldResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmShield", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmShieldResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudProductLogCollection(self, request):
        r"""Cloud product integration uses internal APIs

        :param request: Request instance for ModifyCloudProductLogCollection.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyCloudProductLogCollectionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyCloudProductLogCollectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudProductLogCollection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudProductLogCollectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConfig(self, request):
        r"""This API is used to modify collection rule configuration.

        :param request: Request instance for ModifyConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsole(self, request):
        r"""This API is used to edit the DataSight Console

        :param request: Request instance for ModifyConsole.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConsoleRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConsoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsole", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsumer(self, request):
        r"""This API is used to modify a CKafka delivery task.

        :param request: Request instance for ModifyConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsumerGroup(self, request):
        r"""This API is used to update the consumer group information.

        :param request: Request instance for ModifyConsumerGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyConsumerGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCosRecharge(self, request):
        r"""This API is used to modify a COS import task.

        :param request: Request instance for ModifyCosRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyCosRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyCosRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCosRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCosRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDashboard(self, request):
        r"""This API is used to modify the dashboard.

        :param request: Request instance for ModifyDashboard.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyDashboardRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDashboardSubscribe(self, request):
        r"""This API is used to modify dashboard subscriptions.

        :param request: Request instance for ModifyDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataTransform(self, request):
        r"""This API is used to modify a data processing task.

        :param request: Request instance for ModifyDataTransform.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyDataTransformRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyDataTransformResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataTransform", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataTransformResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDlcDeliver(self, request):
        r"""Modify a DLC delivery task

        :param request: Request instance for ModifyDlcDeliver.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyDlcDeliverRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyDlcDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDlcDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDlcDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEsRecharge(self, request):
        r"""Modify es import configuration

        :param request: Request instance for ModifyEsRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyEsRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyEsRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEsRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEsRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHostMetricConfig(self, request):
        r"""Modify host metric collection configuration

        :param request: Request instance for ModifyHostMetricConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyHostMetricConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyHostMetricConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHostMetricConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHostMetricConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIndex(self, request):
        r"""This API is used to modify the index configuration. It is subject to the default request frequency limit, and the number of concurrent requests to the same log topic cannot exceed 1, i.e., the index configuration of only one log topic can be modified at a time.

        :param request: Request instance for ModifyIndex.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyIndexRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIndex", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKafkaConsumer(self, request):
        r"""This API is used to modify Kafka protocol consumption information.

        :param request: Request instance for ModifyKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKafkaConsumerGroupOffset(self, request):
        r"""This API is used to modify Kafka protocol consumption group offsets.

        :param request: Request instance for ModifyKafkaConsumerGroupOffset.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaConsumerGroupOffsetRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaConsumerGroupOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKafkaConsumerGroupOffset", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKafkaConsumerGroupOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyKafkaRecharge(self, request):
        r"""This API is used to modify a Kafka data subscription task.

        :param request: Request instance for ModifyKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogset(self, request):
        r"""This API is used to modify a logset.

        :param request: Request instance for ModifyLogset.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyLogsetRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyLogsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogset", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineGroup(self, request):
        r"""Modify machine group.
        Note: Modifying the interface will directly overwrite historical data and change it to valid input parameters this time. Please be cautious when calling this API.

        :param request: Request instance for ModifyMachineGroup.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyMachineGroupRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyMachineGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMetricConfig(self, request):
        r"""This API is used to create metric collection configurations.

        :param request: Request instance for ModifyMetricConfig.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyMetricConfigRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyMetricConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMetricConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMetricConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMetricSubscribe(self, request):
        r"""This API is used to modify metric subscription configurations.

        :param request: Request instance for ModifyMetricSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyMetricSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyMetricSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMetricSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMetricSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkApplication(self, request):
        r"""Modify a web application

        :param request: Request instance for ModifyNetworkApplication.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyNetworkApplicationRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyNetworkApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNoticeContent(self, request):
        r"""This API is used to modify notification content configuration.

        :param request: Request instance for ModifyNoticeContent.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyNoticeContentRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyNoticeContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNoticeContent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNoticeContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordingRuleTask(self, request):
        r"""This API is used to modify a scheduled pre-aggregation task.

        :param request: Request instance for ModifyRecordingRuleTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyRecordingRuleTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyRecordingRuleTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordingRuleTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordingRuleTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordingRuleYamlTask(self, request):
        r"""Modifying a Metric Pre-Aggregation Task Through a YAML File

        :param request: Request instance for ModifyRecordingRuleYamlTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyRecordingRuleYamlTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyRecordingRuleYamlTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordingRuleYamlTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordingRuleYamlTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyScheduledSql(self, request):
        r"""This API is used to modify a scheduled SQL analysis task.

        :param request: Request instance for ModifyScheduledSql.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyScheduledSqlRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyScheduledSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyScheduledSql", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyScheduledSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySearchView(self, request):
        r"""This API is used to modify a query view.

        :param request: Request instance for ModifySearchView.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifySearchViewRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifySearchViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySearchView", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySearchViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyShipper(self, request):
        r"""This API is used to modify an existing shipping rule. To use this API, you need to grant CLS the write permission of the specified bucket.

        :param request: Request instance for ModifyShipper.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyShipperRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyShipperResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyShipper", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyShipperResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySplunkDeliver(self, request):
        r"""Modify information related to splunk delivery task

        :param request: Request instance for ModifySplunkDeliver.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifySplunkDeliverRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifySplunkDeliverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySplunkDeliver", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySplunkDeliverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopic(self, request):
        r"""This API is used to modify logs or metric topics.

        :param request: Request instance for ModifyTopic.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyTopicRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebCallback(self, request):
        r"""This API is used to modify alarm channel callback configurations.

        :param request: Request instance for ModifyWebCallback.
        :type request: :class:`tencentcloud.cls.v20201016.models.ModifyWebCallbackRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.ModifyWebCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebCallback", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenClawService(self, request):
        r"""This API is used to create resources and indexes dependent on OpenClaw.

        :param request: Request instance for OpenClawService.
        :type request: :class:`tencentcloud.cls.v20201016.models.OpenClawServiceRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.OpenClawServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenClawService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenClawServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenClsService(self, request):
        r"""Enable logging
        This API is used to enable CLS in all regions by filling any region for Region, recommend using Guangzhou (ap-guangzhou).

        :param request: Request instance for OpenClsService.
        :type request: :class:`tencentcloud.cls.v20201016.models.OpenClsServiceRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.OpenClsServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenClsService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenClsServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenKafkaConsumer(self, request):
        r"""This API is used to enable the Kafka consumption feature.

        :param request: Request instance for OpenKafkaConsumer.
        :type request: :class:`tencentcloud.cls.v20201016.models.OpenKafkaConsumerRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.OpenKafkaConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenKafkaConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.OpenKafkaConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PreviewKafkaRecharge(self, request):
        r"""This API is used to preview the logs of Kafka data subscription tasks.

        :param request: Request instance for PreviewKafkaRecharge.
        :type request: :class:`tencentcloud.cls.v20201016.models.PreviewKafkaRechargeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.PreviewKafkaRechargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PreviewKafkaRecharge", params, headers=headers)
            response = json.loads(body)
            model = models.PreviewKafkaRechargeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryMetric(self, request):
        r"""Query the latest metric value at a specified time.
        If there is no metric data in the 5 minutes before that moment, there will be no query result.

        :param request: Request instance for QueryMetric.
        :type request: :class:`tencentcloud.cls.v20201016.models.QueryMetricRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.QueryMetricResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMetric", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMetricResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryRangeMetric(self, request):
        r"""This API is used to query the trend of metrics within a specified time range.

        :param request: Request instance for QueryRangeMetric.
        :type request: :class:`tencentcloud.cls.v20201016.models.QueryRangeMetricRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.QueryRangeMetricResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryRangeMetric", params, headers=headers)
            response = json.loads(body)
            model = models.QueryRangeMetricResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetryShipperTask(self, request):
        r"""This API is used to retry a failed shipping task.

        :param request: Request instance for RetryShipperTask.
        :type request: :class:`tencentcloud.cls.v20201016.models.RetryShipperTaskRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.RetryShipperTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetryShipperTask", params, headers=headers)
            response = json.loads(body)
            model = models.RetryShipperTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchCosRechargeInfo(self, request):
        r"""This API is used to preview COS import information.

        :param request: Request instance for SearchCosRechargeInfo.
        :type request: :class:`tencentcloud.cls.v20201016.models.SearchCosRechargeInfoRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SearchCosRechargeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchCosRechargeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.SearchCosRechargeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchDashboardSubscribe(self, request):
        r"""This API is used to preview the dashboard subscription.

        :param request: Request instance for SearchDashboardSubscribe.
        :type request: :class:`tencentcloud.cls.v20201016.models.SearchDashboardSubscribeRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SearchDashboardSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchDashboardSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.SearchDashboardSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchLog(self, request):
        r"""This API is used to retrieve and analyze logs. Please note the following matters when using this API.
        1. Besides being subject to the default API request rate limit, for a single log topic, the number of concurrent queries cannot exceed 15.
        2. The API's return data packet maximum is 49MB. It is recommended to enable gzip compression (HTTP Request Header Accept-Encoding: gzip).

        :param request: Request instance for SearchLog.
        :type request: :class:`tencentcloud.cls.v20201016.models.SearchLogRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SearchLogResponse`

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


    def SendConsumerHeartbeat(self, request):
        r"""This API is used to check the heartbeat of a consumer group.

        :param request: Request instance for SendConsumerHeartbeat.
        :type request: :class:`tencentcloud.cls.v20201016.models.SendConsumerHeartbeatRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SendConsumerHeartbeatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendConsumerHeartbeat", params, headers=headers)
            response = json.loads(body)
            model = models.SendConsumerHeartbeatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SplitPartition(self, request):
        r"""This API is deprecated. If needed, please use the ModifyTopic API to change the number of partitions.

        :param request: Request instance for SplitPartition.
        :type request: :class:`tencentcloud.cls.v20201016.models.SplitPartitionRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.SplitPartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SplitPartition", params, headers=headers)
            response = json.loads(body)
            model = models.SplitPartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadLog(self, request, body):
        r"""## Notification
        To ensure the reliability of your log data and use the log service more efficiently, we recommend that you use the CLS-optimized API to upload structured logs (https://www.tencentcloud.com/document/product/614/16873?from_cn_redirect=1).

        Meanwhile, we have specially optimized and customized SDKs in multiple languages for this API for you to choose from. The SDK provides unified async sending, resource control, automatic retry, graceful shutdown, perception reporting, and other features to improve the log reporting function. For details, refer to [SDK Collection](https://www.tencentcloud.com/document/product/614/67157?from_cn_redirect=1).

        Meanwhile, the log upload API also supports synchronous log data upload. If you select to continue using this API, refer to the following text.

        ## Feature Description

        This API is used to write logs to the designated log topic.

        #### Input parameter (pb binary stream, located in body)

        | Field name | Data type | Location | Must | Description |
        | ------------ | ------- | ---- | ---- | ------------------------------------------------------------ |
        | logGroupList | message | pb   | Yes | logGroup list, encapsulated content of the log group list. It is advisable not to exceed 5 logGroups. |

        Group description:

        | Field name | Required or optional | Description |
        | ----------- | -------- | ------------------------------------------------------------ |
        | logs        | is       | a log array, which means a set of multiple logs. One Log represents one log, and the number of logs in one LogGroup cannot exceed 10000 |
        | contextFlow | No | The unique ID of LogGroup, which must be imported when using context features. Format: "{context ID}-{LogGroupID}".<br>Context ID: A unique identifier for a context (a series of consecutively scrolled log files or a sequence of logs requiring order preservation), a 64-bit integer string in base 16.<br>LogGroupID: A consecutively incremental integer string in base 16. Example: "102700A66102516A-59F59".
        | filename    | No       | Log file name |
        | source      | No       | Log source, using machine IP as a label in general use       |
        | logTags     | No       | Log tag list                                               |

        Log description:

        | field name | Required or optional | Description |
        | -------- | -------- | ------------------------------------------------------------ |
        | time     | is       | log time (Unix timestamp), supports second, millisecond, microsecond, milliseconds is recommended |
        | contents | No | Key-value formatted log content, representing multiple key-value composites in a log |

        Content description:

        | Field name | Required or optional | Description |
        | ------ | -------- | ------------------------------------------------------------ |
        | key    | Yes       | The key value of a field group in a single-line log. It cannot start with `_` |
        | value  | Yes       | The value of a field group in a single-line log. The value of a single-line log must not exceed 1MB, and the sum of ALL values in a LogGroup cannot exceed 5MB. |

        LogTag description:

        | Field name | Required or optional | Description |
        | ------ | -------- | -------------------------------- |
        | key    | Yes      | Custom tag key                 |
        | value  | is       | value corresponding to the custom tag key |

        ## PB Compilation Example

        This example shows how to use the official protoc compiler to compile and generate a C++ language adjustable log upload API from a description file.

        Currently protoc officially supports compilation for languages such as Java, C++, and Python. For details, see [protoc](https://github.com/protocolbuffers/protobuf).

        #### 1. Protocol Buffer installation

        Download [Protocol Buffer](https://main.qcloudimg.com/raw/d7810aaf8b3073fbbc9d4049c21532aa/protobuf-2.6.1.tar.gz), unzip and install. The example version is protobuf 2.6.1, and the environment is Centos 7.3 system. Decompress the `protobuf-2.6.1.tar.gz` compressed package to the `/usr/local` directory and enter the directory. Execute the command as follows:

        ```
        tar -zxvf protobuf-2.6.1.tar.gz -C /usr/local/ && cd /usr/local/protobuf-2.6.1
        ```

        Start compilation and installation, configure environment variables, execute the command as follows:

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# ./configure
        [root@VM_0_8_centos protobuf-2.6.1]# make && make install
        [root@VM_0_8_centos protobuf-2.6.1]# export PATH=$PATH:/usr/local/protobuf-2.6.1/bin
        ```

        After successful compilation, view the version using the following command:

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# protoc --version
        liprotoc 2.6.1
        ```

        #### 2. Create PB description file

        The PB description file is the data interchange format agreed by the communication parties. When uploading logs, compile the specified protocol format into the calling interface of the corresponding language version, then add to engineering code. For details, see [protoc](https://github.com/protocolbuffers/protobuf).

        Create a local PB message description file cls.proto based on the PB data format specified by the log service.

        !PB description file content immutable, and the file name must end with `.proto`.

        The content of cls.proto (PB description file) is as follows:

        ```
        package cls;

        message Log
        {
            message Content
            {
        required string key = 1; // key for each group of fields
        required string value = 2; // The value of the group field
            }
        required int64   time     = 1; // A timestamp in UNIX time format
        repeated Content contents = 2; // multiple kv combinations in a log
        }

        message LogTag
        {
            required string key       = 1;
            required string value     = 2;
        }

        message LogGroup
        {
        repeated Log    logs        = 1; // log array composed of multiple logs
        optional string contextFlow = 2; // Currently no utility
        optional string filename = 3; // log file name
        optional string source      = 4; // log source, general use machine IP
            repeated LogTag logTags     = 5;
        }

        message LogGroupList
        {
        repeated LogGroup logGroupList = 1; // log group list
        }
        ```

        #### 3. Compile and generate

        In this example, use the proto compiler to generate C++ language files under the same directory as the cls.proto file and execute the following compilation command:

        ```
        protoc --cpp_out=./ ./cls.proto
        ```

        `--cpp_out=./` means compile to cpp format and output in the current directory. `./cls.proto` refers to the cls.proto description file located in the current directory.

        After successful compilation, it will output the code file in the corresponding language. This routine generates the cls.pb.h header file and the cls.pb.cc code implementation file, as shown below:

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# protoc --cpp_out=./ ./cls.proto
        [root@VM_0_8_centos protobuf-2.6.1]# ls
        cls.pb.cc cls.pb.h cls.proto
        ```

        #### 4. Call

        Import the generated cls.pb.h header file into the code and call the interface to encapsulate the data format.

        :param request: Request instance for UploadLog.
        :type request: :class:`tencentcloud.cls.v20201016.models.UploadLogRequest`
        :rtype: :class:`tencentcloud.cls.v20201016.models.UploadLogResponse`

        """
        try:
            params = request._serialize()
            params = {"X-CLS-"+key: value for key, value in params.items()}
            response = self.call_octet_stream("UploadLog", params, body)
            model = models.UploadLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))