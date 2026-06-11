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
from tencentcloud.cls.v20201016 import models
from typing import Dict


class ClsClient(AbstractClient):
    _apiVersion = '2020-10-16'
    _endpoint = 'cls.intl.tencentcloudapi.com'
    _service = 'cls'

    async def AddMachineGroupInfo(
            self,
            request: models.AddMachineGroupInfoRequest,
            opts: Dict = None,
    ) -> models.AddMachineGroupInfoResponse:
        """
        This API is used to add machine group information.
        """
        
        kwargs = {}
        kwargs["action"] = "AddMachineGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddMachineGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyConfigToMachineGroup(
            self,
            request: models.ApplyConfigToMachineGroupRequest,
            opts: Dict = None,
    ) -> models.ApplyConfigToMachineGroupResponse:
        """
        This API is used to apply the collection configuration to a specified machine group.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyConfigToMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyConfigToMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelRebuildIndexTask(
            self,
            request: models.CancelRebuildIndexTaskRequest,
            opts: Dict = None,
    ) -> models.CancelRebuildIndexTaskResponse:
        """
        This API is used to cancel creating a reindexing task.
        """
        
        kwargs = {}
        kwargs["action"] = "CancelRebuildIndexTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelRebuildIndexTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChatCompletions(
            self,
            request: models.ChatCompletionsRequest,
            opts: Dict = None,
    ) -> models.ChatCompletionsResponse:
        """
        Call the API to initiate a dialogue request.
        This API supports AI-powered logging features such as intelligently generating retrieval analysis statements.
        Note: When calling this API via SSE streaming, ensure the request domain name is set to cls.ai.tencentcloudapi.com (configurable as cls.ai.internal.tencentcloudapi.com in a private network environment).
        """
        
        kwargs = {}
        kwargs["action"] = "ChatCompletions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatCompletionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFunction(
            self,
            request: models.CheckFunctionRequest,
            opts: Dict = None,
    ) -> models.CheckFunctionResponse:
        """
        This API is used to verify the syntax of data processing DSL functions.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckRechargeKafkaServer(
            self,
            request: models.CheckRechargeKafkaServerRequest,
            opts: Dict = None,
    ) -> models.CheckRechargeKafkaServerResponse:
        """
        This API is used to check whether the Kafka service cluster is accessible.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRechargeKafkaServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRechargeKafkaServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseKafkaConsumer(
            self,
            request: models.CloseKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.CloseKafkaConsumerResponse:
        """
        This API is used to disable Kafka consumption.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitConsumerOffsets(
            self,
            request: models.CommitConsumerOffsetsRequest,
            opts: Dict = None,
    ) -> models.CommitConsumerOffsetsResponse:
        """
        This API is used to submit a consumption offset.
        """
        
        kwargs = {}
        kwargs["action"] = "CommitConsumerOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitConsumerOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarm(
            self,
            request: models.CreateAlarmRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmResponse:
        """
        This API is used to create an alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmNotice(
            self,
            request: models.CreateAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmNoticeResponse:
        """
        This API is used to create a notification channel group with two configuration modes to choose from.
        1. Easy mode provides the most basic notification channel function. The following parameters are required:
        - Type
        - NoticeReceivers
        - WebCallbacks

        2. Advanced mode: On the basis of easy mode, it supports setting rules, setting notification channels for different types of alarms, and escalating alarms. The following parameters are required:
        - NoticeRules
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmShield(
            self,
            request: models.CreateAlarmShieldRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmShieldResponse:
        """
        This API is used to create an alarm blocking rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmShieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudProductLogCollection(
            self,
            request: models.CreateCloudProductLogCollectionRequest,
            opts: Dict = None,
    ) -> models.CreateCloudProductLogCollectionResponse:
        """
        Cloud product integration uses internal APIs
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudProductLogCollection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudProductLogCollectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfig(
            self,
            request: models.CreateConfigRequest,
            opts: Dict = None,
    ) -> models.CreateConfigResponse:
        """
        This API is used to create collection rule configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsole(
            self,
            request: models.CreateConsoleRequest,
            opts: Dict = None,
    ) -> models.CreateConsoleResponse:
        """
        This API is used to create the DataSight Console
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumer(
            self,
            request: models.CreateConsumerRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerResponse:
        """
        This API is used to create a CKafka delivery task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConsumerGroup(
            self,
            request: models.CreateConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateConsumerGroupResponse:
        """
        This API is used to check the heartbeat of a consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCosRecharge(
            self,
            request: models.CreateCosRechargeRequest,
            opts: Dict = None,
    ) -> models.CreateCosRechargeResponse:
        """
        This API is used to create a COS import task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCosRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCosRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDashboard(
            self,
            request: models.CreateDashboardRequest,
            opts: Dict = None,
    ) -> models.CreateDashboardResponse:
        """
        This API is used to create a dashboard.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDashboardSubscribe(
            self,
            request: models.CreateDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateDashboardSubscribeResponse:
        """
        This API is used to create a dashboard subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataTransform(
            self,
            request: models.CreateDataTransformRequest,
            opts: Dict = None,
    ) -> models.CreateDataTransformResponse:
        """
        This API is used to create a data processing task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataTransform"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataTransformResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDeliverCloudFunction(
            self,
            request: models.CreateDeliverCloudFunctionRequest,
            opts: Dict = None,
    ) -> models.CreateDeliverCloudFunctionResponse:
        """
        This API is used to create a delivery SCF task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDeliverCloudFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDeliverCloudFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDlcDeliver(
            self,
            request: models.CreateDlcDeliverRequest,
            opts: Dict = None,
    ) -> models.CreateDlcDeliverResponse:
        """
        Create a DLC delivery task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDlcDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDlcDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEsRecharge(
            self,
            request: models.CreateEsRechargeRequest,
            opts: Dict = None,
    ) -> models.CreateEsRechargeResponse:
        """
        This API is used to create an es import configuration
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEsRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEsRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExport(
            self,
            request: models.CreateExportRequest,
            opts: Dict = None,
    ) -> models.CreateExportResponse:
        """
        This API only creates download tasks. The download address returned by the task can be obtained by user invocation of [DescribeExports](https://www.tencentcloud.com/document/product/614/56449?from_cn_redirect=1) to view task list, which includes the CosPath parameter for the download address.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostMetricConfig(
            self,
            request: models.CreateHostMetricConfigRequest,
            opts: Dict = None,
    ) -> models.CreateHostMetricConfigResponse:
        """
        This API is used to create host metric collection configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIndex(
            self,
            request: models.CreateIndexRequest,
            opts: Dict = None,
    ) -> models.CreateIndexResponse:
        """
        This API is used to create an index.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKafkaRecharge(
            self,
            request: models.CreateKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.CreateKafkaRechargeResponse:
        """
        This API is used to create a Kafka data subscription task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogset(
            self,
            request: models.CreateLogsetRequest,
            opts: Dict = None,
    ) -> models.CreateLogsetResponse:
        """
        This API is used to create a logset. The ID of the created logset is returned.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMachineGroup(
            self,
            request: models.CreateMachineGroupRequest,
            opts: Dict = None,
    ) -> models.CreateMachineGroupResponse:
        """
        This API is used to create a machine group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMetricConfig(
            self,
            request: models.CreateMetricConfigRequest,
            opts: Dict = None,
    ) -> models.CreateMetricConfigResponse:
        """
        This API is used to create metric collection configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMetricSubscribe(
            self,
            request: models.CreateMetricSubscribeRequest,
            opts: Dict = None,
    ) -> models.CreateMetricSubscribeResponse:
        """
        This API is used to create metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMetricSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMetricSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkApplication(
            self,
            request: models.CreateNetworkApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkApplicationResponse:
        """
        This API is used to create a network application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNoticeContent(
            self,
            request: models.CreateNoticeContentRequest,
            opts: Dict = None,
    ) -> models.CreateNoticeContentResponse:
        """
        This API is used to create notification content.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNoticeContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNoticeContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRebuildIndexTask(
            self,
            request: models.CreateRebuildIndexTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRebuildIndexTaskResponse:
        """
        This API is used to creates rebuild index tasks.
        Note:
        -A single log topic allows only one index reconstruction task at a time and can have up to 10 rebuild index task records. Delete task records that are no longer needed before creating an index task.
        -Logs within the same time range only allow rebuilding indexes once. Delete previous task records before rebuilding again.
        -Deleting a rebuild index task record restores the index data before rebuilding an index.
        -The log write traffic of the selected time range cannot exceed 5TB.
        -The index rebuilding time range is subject to the log time. When the log uploading time has a deviation exceeding one hour from the index rebuilding time range (for example, reporting a new log at 16:00 for 02:00 to CLS and rebuilding the log index for 00:00–12:00), the logs will not be rebuilt and cannot be retrieved subsequently. When reporting a new log to the reconstructed log time range, it will not be rebuilt and cannot be retrieved subsequently.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRebuildIndexTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRebuildIndexTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordingRuleTask(
            self,
            request: models.CreateRecordingRuleTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRecordingRuleTaskResponse:
        """
        Creating a Metric Pre-Aggregation Task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordingRuleTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordingRuleTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordingRuleYamlTask(
            self,
            request: models.CreateRecordingRuleYamlTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRecordingRuleYamlTaskResponse:
        """
        Creating a Metric Pre-Aggregation Task Through a YAML File
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordingRuleYamlTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordingRuleYamlTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScheduledSql(
            self,
            request: models.CreateScheduledSqlRequest,
            opts: Dict = None,
    ) -> models.CreateScheduledSqlResponse:
        """
        This API is used to create a scheduled SQL analysis task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScheduledSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScheduledSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSearchView(
            self,
            request: models.CreateSearchViewRequest,
            opts: Dict = None,
    ) -> models.CreateSearchViewResponse:
        """
        Create a query view
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSearchView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSearchViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateShipper(
            self,
            request: models.CreateShipperRequest,
            opts: Dict = None,
    ) -> models.CreateShipperResponse:
        """
        This API is used to create a task to ship to COS. Note: To use this API, you need to check whether you have configured the role and permission for shipping to COS. If not, see **Viewing and Configuring Shipping Authorization** at https://intl.cloud.tencent.com/document/product/614/71623.?from_cn_redirect=1
        """
        
        kwargs = {}
        kwargs["action"] = "CreateShipper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateShipperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSplunkDeliver(
            self,
            request: models.CreateSplunkDeliverRequest,
            opts: Dict = None,
    ) -> models.CreateSplunkDeliverResponse:
        """
        Create a Splunk delivery task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSplunkDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSplunkDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        This API is used to create logs or metric topics.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebCallback(
            self,
            request: models.CreateWebCallbackRequest,
            opts: Dict = None,
    ) -> models.CreateWebCallbackResponse:
        """
        This API is used to create alarm channel callback configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarm(
            self,
            request: models.DeleteAlarmRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmResponse:
        """
        This API is used to delete an alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmNotice(
            self,
            request: models.DeleteAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmNoticeResponse:
        """
        This API is used to delete a notification group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmShield(
            self,
            request: models.DeleteAlarmShieldRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmShieldResponse:
        """
        This API is used to delete an alarm blocking rule. When the alarm blocking rule is active or invalid, it cannot be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmShieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudProductLogCollection(
            self,
            request: models.DeleteCloudProductLogCollectionRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudProductLogCollectionResponse:
        """
        Cloud product integration uses internal APIs
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudProductLogCollection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudProductLogCollectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfig(
            self,
            request: models.DeleteConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigResponse:
        """
        This API is used to delete collection rule configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConfigFromMachineGroup(
            self,
            request: models.DeleteConfigFromMachineGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConfigFromMachineGroupResponse:
        """
        This API is used to delete the collection configuration applied to a machine group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConfigFromMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConfigFromMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsole(
            self,
            request: models.DeleteConsoleRequest,
            opts: Dict = None,
    ) -> models.DeleteConsoleResponse:
        """
        This API is used to delete the DataSight Console
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumer(
            self,
            request: models.DeleteConsumerRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerResponse:
        """
        Deleting a CKafka Delivery Task
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteConsumerGroup(
            self,
            request: models.DeleteConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerGroupResponse:
        """
        Delete consumer groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCosRecharge(
            self,
            request: models.DeleteCosRechargeRequest,
            opts: Dict = None,
    ) -> models.DeleteCosRechargeResponse:
        """
        This API is used to delete a cos Import Task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCosRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCosRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDashboard(
            self,
            request: models.DeleteDashboardRequest,
            opts: Dict = None,
    ) -> models.DeleteDashboardResponse:
        """
        This API is used to delete dashboards.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDashboardSubscribe(
            self,
            request: models.DeleteDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeleteDashboardSubscribeResponse:
        """
        This API is used to delete dashboard subscriptions.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataTransform(
            self,
            request: models.DeleteDataTransformRequest,
            opts: Dict = None,
    ) -> models.DeleteDataTransformResponse:
        """
        This API is used to delete a data processing task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataTransform"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataTransformResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDlcDeliver(
            self,
            request: models.DeleteDlcDeliverRequest,
            opts: Dict = None,
    ) -> models.DeleteDlcDeliverResponse:
        """
        Delete a DLC delivery task
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDlcDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDlcDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEsRecharge(
            self,
            request: models.DeleteEsRechargeRequest,
            opts: Dict = None,
    ) -> models.DeleteEsRechargeResponse:
        """
        Delete es import configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEsRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEsRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExport(
            self,
            request: models.DeleteExportRequest,
            opts: Dict = None,
    ) -> models.DeleteExportResponse:
        """
        This API is used to delete a log download task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHostMetricConfig(
            self,
            request: models.DeleteHostMetricConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteHostMetricConfigResponse:
        """
        Delete host metric collection configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHostMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHostMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIndex(
            self,
            request: models.DeleteIndexRequest,
            opts: Dict = None,
    ) -> models.DeleteIndexResponse:
        """
        This API is used to delete the index configuration of a log topic. After deleting, you cannot retrieve or query the collected logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteKafkaRecharge(
            self,
            request: models.DeleteKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.DeleteKafkaRechargeResponse:
        """
        This API is used to delete a Kafka data subscription task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogset(
            self,
            request: models.DeleteLogsetRequest,
            opts: Dict = None,
    ) -> models.DeleteLogsetResponse:
        """
        This API is used to delete a logset.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineGroup(
            self,
            request: models.DeleteMachineGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineGroupResponse:
        """
        This API is used to delete a machine group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMachineGroupInfo(
            self,
            request: models.DeleteMachineGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteMachineGroupInfoResponse:
        """
        This API is used to delete machine group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMachineGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMachineGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMetricConfig(
            self,
            request: models.DeleteMetricConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteMetricConfigResponse:
        """
        This API is used to delete metric collection configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMetricSubscribe(
            self,
            request: models.DeleteMetricSubscribeRequest,
            opts: Dict = None,
    ) -> models.DeleteMetricSubscribeResponse:
        """
        This API is used to delete metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMetricSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMetricSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkApplication(
            self,
            request: models.DeleteNetworkApplicationRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkApplicationResponse:
        """
        Delete a web application
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNoticeContent(
            self,
            request: models.DeleteNoticeContentRequest,
            opts: Dict = None,
    ) -> models.DeleteNoticeContentResponse:
        """
        This API is used to delete notification content configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNoticeContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNoticeContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordingRuleTask(
            self,
            request: models.DeleteRecordingRuleTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordingRuleTaskResponse:
        """
        This API is used to delete a pre-aggregation analysis task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordingRuleTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordingRuleTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordingRuleYamlTask(
            self,
            request: models.DeleteRecordingRuleYamlTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordingRuleYamlTaskResponse:
        """
        This API is used to delete the pre-aggregation task in yaml.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordingRuleYamlTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordingRuleYamlTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScheduledSql(
            self,
            request: models.DeleteScheduledSqlRequest,
            opts: Dict = None,
    ) -> models.DeleteScheduledSqlResponse:
        """
        This API is used to delete a scheduled SQL analysis task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScheduledSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScheduledSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSearchView(
            self,
            request: models.DeleteSearchViewRequest,
            opts: Dict = None,
    ) -> models.DeleteSearchViewResponse:
        """
        This API is used to delete a query view.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSearchView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSearchViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShipper(
            self,
            request: models.DeleteShipperRequest,
            opts: Dict = None,
    ) -> models.DeleteShipperResponse:
        """
        This API is used to delete a COS shipping task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShipper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShipperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSplunkDeliver(
            self,
            request: models.DeleteSplunkDeliverRequest,
            opts: Dict = None,
    ) -> models.DeleteSplunkDeliverResponse:
        """
        Delete a Splunk delivery task
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSplunkDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSplunkDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        This API is used to delete logs or metric topics.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebCallback(
            self,
            request: models.DeleteWebCallbackRequest,
            opts: Dict = None,
    ) -> models.DeleteWebCallbackResponse:
        """
        This API is used to delete alarm channel callback configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotices(
            self,
            request: models.DescribeAlarmNoticesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticesResponse:
        """
        This API is used to get the notification group list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmShields(
            self,
            request: models.DescribeAlarmShieldsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmShieldsResponse:
        """
        This API is used to access alarm blocking configuration rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmShields"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmShieldsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarms(
            self,
            request: models.DescribeAlarmsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmsResponse:
        """
        This API is used to get the alarm policy list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertRecordHistory(
            self,
            request: models.DescribeAlertRecordHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertRecordHistoryResponse:
        """
        This API is used to get alarm records, such as today's uncleared alarms.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertRecordHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertRecordHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudProductLogTasks(
            self,
            request: models.DescribeCloudProductLogTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudProductLogTasksResponse:
        """
        Cloud product integration uses relevant APIs
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudProductLogTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudProductLogTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterBaseMetricConfigs(
            self,
            request: models.DescribeClusterBaseMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterBaseMetricConfigsResponse:
        """
        This API is used to obtain metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterBaseMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterBaseMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterMetricConfigs(
            self,
            request: models.DescribeClusterMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterMetricConfigsResponse:
        """
        This API is used to obtain metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigMachineGroups(
            self,
            request: models.DescribeConfigMachineGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigMachineGroupsResponse:
        """
        This API is used to get the machine group bound to collection rule configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigMachineGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigMachineGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigs(
            self,
            request: models.DescribeConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigsResponse:
        """
        This API is used to get collection rule configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsoles(
            self,
            request: models.DescribeConsolesRequest,
            opts: Dict = None,
    ) -> models.DescribeConsolesResponse:
        """
        Query the DataSight console instance list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumer(
            self,
            request: models.DescribeConsumerRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerResponse:
        """
        This API is used to query a shipping task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerGroups(
            self,
            request: models.DescribeConsumerGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerGroupsResponse:
        """
        This API is used to obtain the consumer group list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerOffsets(
            self,
            request: models.DescribeConsumerOffsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerOffsetsResponse:
        """
        Obtaining the Consumer Group Point Information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerOffsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerOffsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumerPreview(
            self,
            request: models.DescribeConsumerPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumerPreviewResponse:
        """
        This API is used to preview Kafka shipping data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumerPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumerPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConsumers(
            self,
            request: models.DescribeConsumersRequest,
            opts: Dict = None,
    ) -> models.DescribeConsumersResponse:
        """
        This API is used to obtain the shipping rule information list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConsumers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConsumersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCosRecharges(
            self,
            request: models.DescribeCosRechargesRequest,
            opts: Dict = None,
    ) -> models.DescribeCosRechargesResponse:
        """
        This API is used to get COS import configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCosRecharges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCosRechargesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDashboardSubscribes(
            self,
            request: models.DescribeDashboardSubscribesRequest,
            opts: Dict = None,
    ) -> models.DescribeDashboardSubscribesResponse:
        """
        This API is used to obtain the dashboard subscription list, and supports paging.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDashboardSubscribes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDashboardSubscribesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataTransformInfo(
            self,
            request: models.DescribeDataTransformInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDataTransformInfoResponse:
        """
        This API is used to get the basic information of data processing tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataTransformInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataTransformInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDlcDelivers(
            self,
            request: models.DescribeDlcDeliversRequest,
            opts: Dict = None,
    ) -> models.DescribeDlcDeliversResponse:
        """
        This API is used to search alarm channel callback configuration lists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDlcDelivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDlcDeliversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEsRechargePreview(
            self,
            request: models.DescribeEsRechargePreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeEsRechargePreviewResponse:
        """
        Import Preview
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEsRechargePreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEsRechargePreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEsRecharges(
            self,
            request: models.DescribeEsRechargesRequest,
            opts: Dict = None,
    ) -> models.DescribeEsRechargesResponse:
        """
        Retrieve the es import configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEsRecharges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEsRechargesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExports(
            self,
            request: models.DescribeExportsRequest,
            opts: Dict = None,
    ) -> models.DescribeExportsResponse:
        """
        This API is used to get the list of log download tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExports"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExportsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostMetricConfigs(
            self,
            request: models.DescribeHostMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeHostMetricConfigsResponse:
        """
        This API is used to obtain metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIndex(
            self,
            request: models.DescribeIndexRequest,
            opts: Dict = None,
    ) -> models.DescribeIndexResponse:
        """
        This API is used to get the index configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumer(
            self,
            request: models.DescribeKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerResponse:
        """
        This API is used to access Kafka protocol consumption information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerGroupDetail(
            self,
            request: models.DescribeKafkaConsumerGroupDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerGroupDetailResponse:
        """
        Retrieve Kafka protocol consumption group details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerGroupDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerGroupDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerGroupList(
            self,
            request: models.DescribeKafkaConsumerGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerGroupListResponse:
        """
        Retrieve the information list of Kafka protocol consumption groups
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerPreview(
            self,
            request: models.DescribeKafkaConsumerPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerPreviewResponse:
        """
        This API is used to preview the Kafka consumption.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaConsumerTopics(
            self,
            request: models.DescribeKafkaConsumerTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaConsumerTopicsResponse:
        """
        This API is used to obtain the topic information list of Kafka consumption.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaConsumerTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaConsumerTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKafkaRecharges(
            self,
            request: models.DescribeKafkaRechargesRequest,
            opts: Dict = None,
    ) -> models.DescribeKafkaRechargesResponse:
        """
        This API is used to get the list of Kafka data subscription tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKafkaRecharges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKafkaRechargesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogContext(
            self,
            request: models.DescribeLogContextRequest,
            opts: Dict = None,
    ) -> models.DescribeLogContextResponse:
        """
        This API is used to search for content near the log context. For more details, see [Context Search](https://intl.cloud.tencent.com/document/product/614/53248?from_cn_redirect=1).The maximum value of API's return data packet is 49MB. It is recommended to enable gzip compression (HTTP Request Header Accept-Encoding: gzip).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogContext"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogContextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogHistogram(
            self,
            request: models.DescribeLogHistogramRequest,
            opts: Dict = None,
    ) -> models.DescribeLogHistogramResponse:
        """
        This API is used to get a log count histogram.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogHistogram"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogHistogramResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogsets(
            self,
            request: models.DescribeLogsetsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogsetsResponse:
        """
        This API is used to get the list of logsets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogsets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogsetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineGroupConfigs(
            self,
            request: models.DescribeMachineGroupConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineGroupConfigsResponse:
        """
        This API is used to get the collection rule configuration bound to a machine group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineGroupConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineGroupConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachineGroups(
            self,
            request: models.DescribeMachineGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineGroupsResponse:
        """
        This API is used to get the list of machine groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachineGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachines(
            self,
            request: models.DescribeMachinesRequest,
            opts: Dict = None,
    ) -> models.DescribeMachinesResponse:
        """
        This API is used to get the status of a machine under the specified machine group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricCorrectDimension(
            self,
            request: models.DescribeMetricCorrectDimensionRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricCorrectDimensionResponse:
        """
        This API is used to obtain metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricCorrectDimension"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricCorrectDimensionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricSubscribePreview(
            self,
            request: models.DescribeMetricSubscribePreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricSubscribePreviewResponse:
        """
        This API is used to create metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricSubscribePreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricSubscribePreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricSubscribes(
            self,
            request: models.DescribeMetricSubscribesRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricSubscribesResponse:
        """
        This API is used to obtain metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricSubscribes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricSubscribesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkApplicationDetail(
            self,
            request: models.DescribeNetworkApplicationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkApplicationDetailResponse:
        """
        Retrieve web application details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkApplicationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkApplicationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkApplications(
            self,
            request: models.DescribeNetworkApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkApplicationsResponse:
        """
        Retrieve the network application list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNoticeContents(
            self,
            request: models.DescribeNoticeContentsRequest,
            opts: Dict = None,
    ) -> models.DescribeNoticeContentsResponse:
        """
        This API is used to obtain the notification content list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNoticeContents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNoticeContentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePartitions(
            self,
            request: models.DescribePartitionsRequest,
            opts: Dict = None,
    ) -> models.DescribePartitionsResponse:
        """
        This API is deprecated. If needed, please use the DescribeTopics API to get the number of partitions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePartitionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRebuildIndexTasks(
            self,
            request: models.DescribeRebuildIndexTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeRebuildIndexTasksResponse:
        """
        This API is used to obtain the list of rebuild index tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRebuildIndexTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRebuildIndexTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordingRuleTask(
            self,
            request: models.DescribeRecordingRuleTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordingRuleTaskResponse:
        """
        This API is used to retrieve the pre-aggregation task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordingRuleTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordingRuleTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordingRuleYamlTask(
            self,
            request: models.DescribeRecordingRuleYamlTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordingRuleYamlTaskResponse:
        """
        This API is used to retrieve the pre-aggregation task list in yaml.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordingRuleYamlTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordingRuleYamlTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScheduledSqlInfo(
            self,
            request: models.DescribeScheduledSqlInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeScheduledSqlInfoResponse:
        """
        This API is used to access the scheduled SQL analysis task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScheduledSqlInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScheduledSqlInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSearchViews(
            self,
            request: models.DescribeSearchViewsRequest,
            opts: Dict = None,
    ) -> models.DescribeSearchViewsResponse:
        """
        Query view list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSearchViews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSearchViewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShipperTasks(
            self,
            request: models.DescribeShipperTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeShipperTasksResponse:
        """
        This API is used to get the list of shipping tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShipperTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShipperTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeShippers(
            self,
            request: models.DescribeShippersRequest,
            opts: Dict = None,
    ) -> models.DescribeShippersResponse:
        """
        This API is used to get the configuration of the task shipped to COS.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeShippers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeShippersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSplunkDelivers(
            self,
            request: models.DescribeSplunkDeliversRequest,
            opts: Dict = None,
    ) -> models.DescribeSplunkDeliversResponse:
        """
        Retrieve the Splunk delivery task list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSplunkDelivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSplunkDeliversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSplunkPreview(
            self,
            request: models.DescribeSplunkPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeSplunkPreviewResponse:
        """
        splunk delivery task preview
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSplunkPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSplunkPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicBaseMetricConfigs(
            self,
            request: models.DescribeTopicBaseMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicBaseMetricConfigsResponse:
        """
        This API is used to obtain metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicBaseMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicBaseMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopicMetricConfigs(
            self,
            request: models.DescribeTopicMetricConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicMetricConfigsResponse:
        """
        This API is used to obtain metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopicMetricConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicMetricConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopics(
            self,
            request: models.DescribeTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicsResponse:
        """
        This API is used to obtain logs or metric topic lists and supports pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebCallbacks(
            self,
            request: models.DescribeWebCallbacksRequest,
            opts: Dict = None,
    ) -> models.DescribeWebCallbacksResponse:
        """
        This API is used to search alarm channel callback configuration lists.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebCallbacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebCallbacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EstimateRebuildIndexTask(
            self,
            request: models.EstimateRebuildIndexTaskRequest,
            opts: Dict = None,
    ) -> models.EstimateRebuildIndexTaskResponse:
        """
        This API is used to estimate rebuild index tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "EstimateRebuildIndexTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EstimateRebuildIndexTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAlarmLog(
            self,
            request: models.GetAlarmLogRequest,
            opts: Dict = None,
    ) -> models.GetAlarmLogResponse:
        """
        This API is used to access alarm policy execution details.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAlarmLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAlarmLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetClsService(
            self,
            request: models.GetClsServiceRequest,
            opts: Dict = None,
    ) -> models.GetClsServiceResponse:
        """
        This API is used to check whether CLS is enabled.
        This API is used to fill in any region for Region, recommend using Guangzhou (ap-guangzhou).
        """
        
        kwargs = {}
        kwargs["action"] = "GetClsService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetClsServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMetricLabelValues(
            self,
            request: models.GetMetricLabelValuesRequest,
            opts: Dict = None,
    ) -> models.GetMetricLabelValuesResponse:
        """
        This API is used to obtain the list of time series label values.
        """
        
        kwargs = {}
        kwargs["action"] = "GetMetricLabelValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMetricLabelValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MergePartition(
            self,
            request: models.MergePartitionRequest,
            opts: Dict = None,
    ) -> models.MergePartitionResponse:
        """
        This API is deprecated. If needed, please use the ModifyTopic API to change the number of partitions.
        """
        
        kwargs = {}
        kwargs["action"] = "MergePartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MergePartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarm(
            self,
            request: models.ModifyAlarmRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmResponse:
        """
        This API is used to modify an alarm policy. At least one valid configuration item needs to be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmNotice(
            self,
            request: models.ModifyAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmNoticeResponse:
        """
        This API is used to modify a notification group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmShield(
            self,
            request: models.ModifyAlarmShieldRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmShieldResponse:
        """
        This API is used to modify alarm blocking rules. When the alarm blocking rule is invalid, it cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmShieldResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudProductLogCollection(
            self,
            request: models.ModifyCloudProductLogCollectionRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudProductLogCollectionResponse:
        """
        Cloud product integration uses internal APIs
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudProductLogCollection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudProductLogCollectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConfig(
            self,
            request: models.ModifyConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyConfigResponse:
        """
        This API is used to modify collection rule configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsole(
            self,
            request: models.ModifyConsoleRequest,
            opts: Dict = None,
    ) -> models.ModifyConsoleResponse:
        """
        This API is used to edit the DataSight Console
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumer(
            self,
            request: models.ModifyConsumerRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerResponse:
        """
        This API is used to modify a CKafka delivery task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsumerGroup(
            self,
            request: models.ModifyConsumerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyConsumerGroupResponse:
        """
        This API is used to update the consumer group information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsumerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsumerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCosRecharge(
            self,
            request: models.ModifyCosRechargeRequest,
            opts: Dict = None,
    ) -> models.ModifyCosRechargeResponse:
        """
        This API is used to modify a COS import task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCosRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCosRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDashboard(
            self,
            request: models.ModifyDashboardRequest,
            opts: Dict = None,
    ) -> models.ModifyDashboardResponse:
        """
        This API is used to modify the dashboard.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDashboardSubscribe(
            self,
            request: models.ModifyDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.ModifyDashboardSubscribeResponse:
        """
        This API is used to modify dashboard subscriptions.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataTransform(
            self,
            request: models.ModifyDataTransformRequest,
            opts: Dict = None,
    ) -> models.ModifyDataTransformResponse:
        """
        This API is used to modify a data processing task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataTransform"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataTransformResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDlcDeliver(
            self,
            request: models.ModifyDlcDeliverRequest,
            opts: Dict = None,
    ) -> models.ModifyDlcDeliverResponse:
        """
        Modify a DLC delivery task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDlcDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDlcDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEsRecharge(
            self,
            request: models.ModifyEsRechargeRequest,
            opts: Dict = None,
    ) -> models.ModifyEsRechargeResponse:
        """
        Modify es import configuration
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEsRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEsRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostMetricConfig(
            self,
            request: models.ModifyHostMetricConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyHostMetricConfigResponse:
        """
        Modify host metric collection configuration
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIndex(
            self,
            request: models.ModifyIndexRequest,
            opts: Dict = None,
    ) -> models.ModifyIndexResponse:
        """
        This API is used to modify the index configuration. It is subject to the default request frequency limit, and the number of concurrent requests to the same log topic cannot exceed 1, i.e., the index configuration of only one log topic can be modified at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKafkaConsumer(
            self,
            request: models.ModifyKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.ModifyKafkaConsumerResponse:
        """
        This API is used to modify Kafka protocol consumption information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKafkaConsumerGroupOffset(
            self,
            request: models.ModifyKafkaConsumerGroupOffsetRequest,
            opts: Dict = None,
    ) -> models.ModifyKafkaConsumerGroupOffsetResponse:
        """
        This API is used to modify Kafka protocol consumption group offsets.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKafkaConsumerGroupOffset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKafkaConsumerGroupOffsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyKafkaRecharge(
            self,
            request: models.ModifyKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.ModifyKafkaRechargeResponse:
        """
        This API is used to modify a Kafka data subscription task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLogset(
            self,
            request: models.ModifyLogsetRequest,
            opts: Dict = None,
    ) -> models.ModifyLogsetResponse:
        """
        This API is used to modify a logset.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLogset"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLogsetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMachineGroup(
            self,
            request: models.ModifyMachineGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyMachineGroupResponse:
        """
        Modify machine group.
        Note: Modifying the interface will directly overwrite historical data and change it to valid input parameters this time. Please be cautious when calling this API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMetricConfig(
            self,
            request: models.ModifyMetricConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyMetricConfigResponse:
        """
        This API is used to create metric collection configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMetricConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMetricConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMetricSubscribe(
            self,
            request: models.ModifyMetricSubscribeRequest,
            opts: Dict = None,
    ) -> models.ModifyMetricSubscribeResponse:
        """
        This API is used to modify metric subscription configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMetricSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMetricSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkApplication(
            self,
            request: models.ModifyNetworkApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkApplicationResponse:
        """
        Modify a web application
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNoticeContent(
            self,
            request: models.ModifyNoticeContentRequest,
            opts: Dict = None,
    ) -> models.ModifyNoticeContentResponse:
        """
        This API is used to modify notification content configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNoticeContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNoticeContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordingRuleTask(
            self,
            request: models.ModifyRecordingRuleTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordingRuleTaskResponse:
        """
        This API is used to modify a scheduled pre-aggregation task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordingRuleTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordingRuleTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordingRuleYamlTask(
            self,
            request: models.ModifyRecordingRuleYamlTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordingRuleYamlTaskResponse:
        """
        Modifying a Metric Pre-Aggregation Task Through a YAML File
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordingRuleYamlTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordingRuleYamlTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScheduledSql(
            self,
            request: models.ModifyScheduledSqlRequest,
            opts: Dict = None,
    ) -> models.ModifyScheduledSqlResponse:
        """
        This API is used to modify a scheduled SQL analysis task.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScheduledSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScheduledSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySearchView(
            self,
            request: models.ModifySearchViewRequest,
            opts: Dict = None,
    ) -> models.ModifySearchViewResponse:
        """
        This API is used to modify a query view.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySearchView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySearchViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyShipper(
            self,
            request: models.ModifyShipperRequest,
            opts: Dict = None,
    ) -> models.ModifyShipperResponse:
        """
        This API is used to modify an existing shipping rule. To use this API, you need to grant CLS the write permission of the specified bucket.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyShipper"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyShipperResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySplunkDeliver(
            self,
            request: models.ModifySplunkDeliverRequest,
            opts: Dict = None,
    ) -> models.ModifySplunkDeliverResponse:
        """
        Modify information related to splunk delivery task
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySplunkDeliver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySplunkDeliverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTopic(
            self,
            request: models.ModifyTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicResponse:
        """
        This API is used to modify logs or metric topics.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebCallback(
            self,
            request: models.ModifyWebCallbackRequest,
            opts: Dict = None,
    ) -> models.ModifyWebCallbackResponse:
        """
        This API is used to modify alarm channel callback configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClawService(
            self,
            request: models.OpenClawServiceRequest,
            opts: Dict = None,
    ) -> models.OpenClawServiceResponse:
        """
        This API is used to create resources and indexes dependent on OpenClaw.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClawService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClawServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenClsService(
            self,
            request: models.OpenClsServiceRequest,
            opts: Dict = None,
    ) -> models.OpenClsServiceResponse:
        """
        Enable logging
        This API is used to enable CLS in all regions by filling any region for Region, recommend using Guangzhou (ap-guangzhou).
        """
        
        kwargs = {}
        kwargs["action"] = "OpenClsService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenClsServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenKafkaConsumer(
            self,
            request: models.OpenKafkaConsumerRequest,
            opts: Dict = None,
    ) -> models.OpenKafkaConsumerResponse:
        """
        This API is used to enable the Kafka consumption feature.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenKafkaConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenKafkaConsumerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PreviewKafkaRecharge(
            self,
            request: models.PreviewKafkaRechargeRequest,
            opts: Dict = None,
    ) -> models.PreviewKafkaRechargeResponse:
        """
        This API is used to preview the logs of Kafka data subscription tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "PreviewKafkaRecharge"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PreviewKafkaRechargeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMetric(
            self,
            request: models.QueryMetricRequest,
            opts: Dict = None,
    ) -> models.QueryMetricResponse:
        """
        Query the latest metric value at a specified time.
        If there is no metric data in the 5 minutes before that moment, there will be no query result.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryRangeMetric(
            self,
            request: models.QueryRangeMetricRequest,
            opts: Dict = None,
    ) -> models.QueryRangeMetricResponse:
        """
        This API is used to query the trend of metrics within a specified time range.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryRangeMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryRangeMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RetryShipperTask(
            self,
            request: models.RetryShipperTaskRequest,
            opts: Dict = None,
    ) -> models.RetryShipperTaskResponse:
        """
        This API is used to retry a failed shipping task.
        """
        
        kwargs = {}
        kwargs["action"] = "RetryShipperTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RetryShipperTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchCosRechargeInfo(
            self,
            request: models.SearchCosRechargeInfoRequest,
            opts: Dict = None,
    ) -> models.SearchCosRechargeInfoResponse:
        """
        This API is used to preview COS import information.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchCosRechargeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchCosRechargeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchDashboardSubscribe(
            self,
            request: models.SearchDashboardSubscribeRequest,
            opts: Dict = None,
    ) -> models.SearchDashboardSubscribeResponse:
        """
        This API is used to preview the dashboard subscription.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchDashboardSubscribe"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchDashboardSubscribeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        This API is used to retrieve and analyze logs. Please note the following matters when using this API.
        1. Besides being subject to the default API request rate limit, for a single log topic, the number of concurrent queries cannot exceed 15.
        2. The API's return data packet maximum is 49MB. It is recommended to enable gzip compression (HTTP Request Header Accept-Encoding: gzip).
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendConsumerHeartbeat(
            self,
            request: models.SendConsumerHeartbeatRequest,
            opts: Dict = None,
    ) -> models.SendConsumerHeartbeatResponse:
        """
        This API is used to check the heartbeat of a consumer group.
        """
        
        kwargs = {}
        kwargs["action"] = "SendConsumerHeartbeat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendConsumerHeartbeatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SplitPartition(
            self,
            request: models.SplitPartitionRequest,
            opts: Dict = None,
    ) -> models.SplitPartitionResponse:
        """
        This API is deprecated. If needed, please use the ModifyTopic API to change the number of partitions.
        """
        
        kwargs = {}
        kwargs["action"] = "SplitPartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SplitPartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadLog(
            self,
            request: models.UploadLogRequest,
            body: bytes,
            opts: Dict = None,
    ) -> models.UploadLogResponse:
        """
        ## Notification
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
        """
        
        kwargs = {}
        kwargs["action"] = "UploadLog"
        kwargs["params"] = body
        kwargs["resp_cls"] = models.UploadLogResponse
        kwargs["headers"] = request.headers or {}
        kwargs["headers"].update({"X-CLS-" + k : v for k, v in request._serialize().items()})
        kwargs["opts"] = opts or {}
        kwargs["opts"]["IsOctetStream"] = True
        
        return await self.call_and_deserialize(**kwargs)