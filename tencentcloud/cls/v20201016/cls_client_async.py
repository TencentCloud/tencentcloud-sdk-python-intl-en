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
        This API is used to create a notification group.
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
        
    async def CreateExport(
            self,
            request: models.CreateExportRequest,
            opts: Dict = None,
    ) -> models.CreateExportResponse:
        """
        This API is used to create a download task. To get the returned download address, call DescribeExports to view the task list. The CosPath parameter is also included for download address. For more information, visit https://intl.cloud.tencent.com/document/product/614/56449.?from_cn_redirect=1
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportResponse
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
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        This API is used to create a log topic.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
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
        This API is used to delete an alarm blocking rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmShieldResponse
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
        
    async def DeleteConsumer(
            self,
            request: models.DeleteConsumerRequest,
            opts: Dict = None,
    ) -> models.DeleteConsumerResponse:
        """
        This API is used to delete a shipping task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteConsumer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteConsumerResponse
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
        
    async def DeleteTopic(
            self,
            request: models.DeleteTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteTopicResponse:
        """
        This API is used to delete a log topic.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTopicResponse
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
        
    async def DescribePartitions(
            self,
            request: models.DescribePartitionsRequest,
            opts: Dict = None,
    ) -> models.DescribePartitionsResponse:
        """
        This API is used to get the list of topic partitions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePartitionsResponse
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
        
    async def DescribeTopics(
            self,
            request: models.DescribeTopicsRequest,
            opts: Dict = None,
    ) -> models.DescribeTopicsResponse:
        """
        This API is used to get the list of log topics and supports pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopicsResponse
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
        
    async def MergePartition(
            self,
            request: models.MergePartitionRequest,
            opts: Dict = None,
    ) -> models.MergePartitionResponse:
        """
        This API is used to merge a topic partition in read/write state. During merge, a topic partition ID can be specified, and CLS will automatically merge the partition adjacent to the right of the range.
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
        This API is used to modify alarm blocking rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmShield"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmShieldResponse
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
        This API is used to modify a machine group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMachineGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMachineGroupResponse
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
        
    async def ModifyTopic(
            self,
            request: models.ModifyTopicRequest,
            opts: Dict = None,
    ) -> models.ModifyTopicResponse:
        """
        This API is used to modify a log topic.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTopicResponse
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
        This API is used to query the latest metric value at a specified time.
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
        
    async def SearchLog(
            self,
            request: models.SearchLogRequest,
            opts: Dict = None,
    ) -> models.SearchLogResponse:
        """
        This API is used to search and analyze logs. When using this API, please note the following:1. Besides being subject to the default API request frequency limit by this API, for a single log topic, the concurrency number cannot exceed 15. 2. For search syntax, it's recommended to use the CQL syntax rule. Please use the SyntaxRule parameter and set its value to 1.
        3. The maximum value of API's response data packet is 49MB. It is recommended to enable gzip compression (HTTP Request Header Accept-Encoding: gzip).
        """
        
        kwargs = {}
        kwargs["action"] = "SearchLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SplitPartition(
            self,
            request: models.SplitPartitionRequest,
            opts: Dict = None,
    ) -> models.SplitPartitionResponse:
        """
        This API is used to split a topic partition.
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
        ## Note
        To ensure log data reliability and help you use CLS more efficiently, we recommend you use the optimized API to upload logs. For more information about the API, see [Uploading Log via API](https://intl.cloud.tencent.com/document/product/614/16873?from_cn_redirect=1).

        For the optimized API, we have developed an SDK (available in multiple languages) that provides features including async sending, resource control, automatic retry, graceful shutdown, and detection-based reporting. For details, see [Uploading Log via SDK](https://intl.cloud.tencent.com/document/product/614/67157?from_cn_redirect=1).

        `UploadLog` allows you to synchronously upload log data. If you still want to continue to use this API instead of the optimized one, read this document.

        ## Feature Description

        This API is used to write logs to a specified log topic.

        CLS provides the following two modes:

        #### Load balancing mode

        In this mode, logs will be automatically written to a target partition among all readable/writable partitions under the current log topic based on the load balancing principle. This mode is suitable for scenarios where sequential consumption is not needed.

        #### Hash routing mode

        In this mode, data will be written to a target partition that meets the range requirements based on the carried hash value (`X-CLS-HashKey`). For example, a log source can be bound to a topic partition through `HashKey`, strictly guaranteeing the sequence of the data written to and consumed in this partition.



        #### Input parameters (pb binary streams in `body`)

        | Parameter       | Type    | Location | Required | Description                                                         |
        | ------------ | ------- | ---- | ---- | ------------------------------------------------------------ |
        | logGroupList | message | pb   | Yes   | The `logGroup` list, which describes the encapsulated log groups. We recommend you enter up to five `logGroup` values. |

        `LogGroup` description:

        | Parameter      | Required | Description                                                         |
        | ----------- | -------- | ------------------------------------------------------------ |
        | logs        | Yes       | Log array consisting of multiple `Log` values. The `Log` indicates a log, and a `LogGroup` can contain up to 10,000 `Log` values. |
        | contextFlow | No       | Unique `LogGroup` ID, which should be passed in if the context feature needs to be used. Format: "{Context ID}-{LogGroupID}". <br>Context ID: Uniquely identifies the context (a series of log files that are continuously scrolling or a series of logs that need to be sequenced), which is a 64-bit integer hex string. <br>LogGroupID: A 64-bit integer hex string that continuously increases, such as `102700A66102516A-59F59`.                        |
        | filename    | No       | Log filename                                                   |
        | source      | No       | Log source, which is generally the machine IP                           |
        | logTags     | No       | List of log tags                                               |

        `Log` description:

        | Parameter   | Required | Description                                                         |
        | -------- | -------- | ------------------------------------------------------------ |
        | time     | Yes       | Unix timestamp of log time in seconds or milliseconds (recommended)      |
        | contents | No       | Log content in key-value format. A log can contain multiple key-value pairs. |

        `Content` description:

        | Parameter | Required | Description                                                         |
        | ------ | -------- | ------------------------------------------------------------ |
        | key    | Yes       | Key of a field group in one log, which cannot start with `_`.                 |
        | value  | Yes       | Value of a field group. The `value` of one log cannot exceed 1 MB and the total `value` in `LogGroup` cannot exceed 5 MB. |

        `LogTag` description:

        | Parameter | Required | Description                             |
        | ------ | -------- | -------------------------------- |
        | key    | Yes       | Key of a custom tag                 |
        | value  | Yes       | Value corresponding to the custom tag key |

        ## pb Compilation Example

        This example shows you how to use the protoc compiler to compile a pb description file into a log upload API in C++.

        > ?Currently, protoc supports compilation in multiple programming languages such as Java, C++, and Python. For more information, see [protoc](https://github.com/protocolbuffers/protobuf).

        #### 1. Install protocol buffers

        Download [Protocol Buffers](https://main.qcloudimg.com/raw/d7810aaf8b3073fbbc9d4049c21532aa/protobuf-2.6.1.tar.gz), decompress the package, and install the tool. The version used in the example is protobuf 2.6.1 running on CentOS 7.3. Run the following command to decompress the `protobuf-2.6.1.tar.gz` package to the `/usr/local` directory and go to the directory:

        ```
        tar -zxvf protobuf-2.6.1.tar.gz -C /usr/local/ && cd /usr/local/protobuf-2.6.1
        ```

        Run the following commands to start compilation and installation and configure the environment variables:

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# ./configure
        [root@VM_0_8_centos protobuf-2.6.1]# make && make install
        [root@VM_0_8_centos protobuf-2.6.1]# export PATH=$PATH:/usr/local/protobuf-2.6.1/bin
        ```

        After the compilation succeeds, run the following command to check the version:

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# protoc --version
        liprotoc 2.6.1
        ```

        #### 2. Create a pb description file

        A pb description file is an agreed-on data interchange format for communication. To upload logs, compile the specified protocol format to an API in the target programming language and add the API to the project code. For more information, see [protoc](https://github.com/protocolbuffers/protobuf).

        Create a pb message description file `cls.proto` based on the pb data format content specified by CLS.

        > !The pb description file content cannot be modified, and the filename must end with `.proto`.

        The content of `cls.proto` (pb description file) is as follows:

        ```
        package cls;

        message Log
        {
            message Content
            {
                required string key   = 1; // Key of each field group
                required string value = 2; // Value of each field group
            }
            required int64   time     = 1; // Unix timestamp
            repeated Content contents = 2; // Multiple key-value pairs in one log
        }

        message LogTag
        {
            required string key       = 1;
            required string value     = 2;
        }

        message LogGroup
        {
            repeated Log    logs        = 1; // Log array consisting of multiple logs
            optional string contextFlow = 2; // This parameter does not take effect currently
            optional string filename    = 3; // Log filename
            optional string source      = 4; // Log source, which is generally the machine IP
            repeated LogTag logTags     = 5;
        }

        message LogGroupList
        {
            repeated LogGroup logGroupList = 1; // Log group list
        }
        ```

        #### 3. Compile and generate the API

        This example uses the proto compiler to generate a C++ file in the same directory as the `cls.proto` file. Run the following compilation command:

        ```
        protoc --cpp_out=./ ./cls.proto
        ```

        > ?`--cpp_out=./` indicates that the file will be compiled in cpp format and output to the current directory. `./cls.proto` indicates the `cls.proto` description file in the current directory.

        After the compilation succeeds, the code file in the corresponding programming language will be generated. This example generates the `cls.pb.h` header file and [cls.pb.cc](http://cls.pb.cc) code implementation file as shown below:

        ```
        [root@VM_0_8_centos protobuf-2.6.1]# protoc --cpp_out=./ ./cls.proto
        [root@VM_0_8_centos protobuf-2.6.1]# ls
        cls.pb.cc cls.pb.h cls.proto
        ```

        #### 4. Call the API

        Import the generated `cls.pb.h` header file into the code and call the API for data encapsulation.
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