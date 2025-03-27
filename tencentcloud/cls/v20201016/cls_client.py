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
from tencentcloud.cls.v20201016 import models


class ClsClient(AbstractClient):
    _apiVersion = '2020-10-16'
    _endpoint = 'cls.intl.tencentcloudapi.com'
    _service = 'cls'


    def AddMachineGroupInfo(self, request):
        """This API is used to add machine group information.

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
        """This API is used to apply the collection configuration to a specified machine group.

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


    def CheckFunction(self, request):
        """This API is used to verify the syntax of data processing DSL functions.

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
        """This API is used to check whether the Kafka service cluster is accessible.

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
        """This API is used to disable Kafka consumption.

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


    def CreateAlarm(self, request):
        """This API is used to create an alarm policy.

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
        """This API is used to create a notification group.

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
        """This API is used to create an alarm blocking rule.

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


    def CreateConfig(self, request):
        """This API is used to create collection rule configuration.

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


    def CreateConsumer(self, request):
        """This API is used to create a CKafka delivery task.

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


    def CreateCosRecharge(self, request):
        """This API is used to create a COS import task.

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


    def CreateDataTransform(self, request):
        """This API is used to create a data processing task.

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
        """This API is used to create a delivery SCF task.

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


    def CreateExport(self, request):
        """This API is used to create a download task. To get the returned download address, call DescribeExports to view the task list. The CosPath parameter is also included for download address. For more information, visit https://intl.cloud.tencent.com/document/product/614/56449.?from_cn_redirect=1

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


    def CreateIndex(self, request):
        """This API is used to create an index.

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
        """This API is used to create a Kafka data subscription task.

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
        """This API is used to create a logset. The ID of the created logset is returned.

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
        """This API is used to create a machine group.

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


    def CreateScheduledSql(self, request):
        """This API is used to create a scheduled SQL analysis task.

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


    def CreateShipper(self, request):
        """This API is used to create a task to ship to COS. Note: To use this API, you need to check whether you have configured the role and permission for shipping to COS. If not, see **Viewing and Configuring Shipping Authorization** at https://intl.cloud.tencent.com/document/product/614/71623.?from_cn_redirect=1

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


    def CreateTopic(self, request):
        """This API is used to create a log topic.

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


    def DeleteAlarm(self, request):
        """This API is used to delete an alarm policy.

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
        """This API is used to delete a notification group.

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
        """This API is used to delete an alarm blocking rule.

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


    def DeleteConfig(self, request):
        """This API is used to delete collection rule configuration.

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
        """This API is used to delete the collection configuration applied to a machine group.

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


    def DeleteConsumer(self, request):
        """This API is used to delete a shipping task.

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


    def DeleteDataTransform(self, request):
        """This API is used to delete a data processing task.

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


    def DeleteExport(self, request):
        """This API is used to delete a log download task.

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


    def DeleteIndex(self, request):
        """This API is used to delete the index configuration of a log topic. After deleting, you cannot retrieve or query the collected logs.

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
        """This API is used to delete a Kafka data subscription task.

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
        """This API is used to delete a logset.

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
        """This API is used to delete a machine group.

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
        """This API is used to delete machine group information.

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


    def DeleteScheduledSql(self, request):
        """This API is used to delete a scheduled SQL analysis task.

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


    def DeleteShipper(self, request):
        """This API is used to delete a COS shipping task.

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


    def DeleteTopic(self, request):
        """This API is used to delete a log topic.

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


    def DescribeAlarmNotices(self, request):
        """This API is used to get the notification group list.

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
        """This API is used to access alarm blocking configuration rules.

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
        """This API is used to get the alarm policy list.

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
        """This API is used to get alarm records, such as today's uncleared alarms.

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


    def DescribeConfigMachineGroups(self, request):
        """This API is used to get the machine group bound to collection rule configuration.

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
        """This API is used to get collection rule configuration.

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


    def DescribeConsumer(self, request):
        """This API is used to query a shipping task.

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


    def DescribeCosRecharges(self, request):
        """This API is used to get COS import configuration.

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


    def DescribeDataTransformInfo(self, request):
        """This API is used to get the basic information of data processing tasks.

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


    def DescribeExports(self, request):
        """This API is used to get the list of log download tasks.

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


    def DescribeIndex(self, request):
        """This API is used to get the index configuration information.

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
        """This API is used to access Kafka protocol consumption information.

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


    def DescribeKafkaRecharges(self, request):
        """This API is used to get the list of Kafka data subscription tasks.

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
        """This API is used to search for content near the log context. For more details, see [Context Search](https://intl.cloud.tencent.com/document/product/614/53248?from_cn_redirect=1).The maximum value of API's return data packet is 49MB. It is recommended to enable gzip compression (HTTP Request Header Accept-Encoding: gzip).

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
        """This API is used to get a log count histogram.

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
        """This API is used to get the list of logsets.

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
        """This API is used to get the collection rule configuration bound to a machine group.

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
        """This API is used to get the list of machine groups.

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
        """This API is used to get the status of a machine under the specified machine group.

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


    def DescribePartitions(self, request):
        """This API is used to get the list of topic partitions.

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


    def DescribeScheduledSqlInfo(self, request):
        """This API is used to access the scheduled SQL analysis task list.

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


    def DescribeShipperTasks(self, request):
        """This API is used to get the list of shipping tasks.

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
        """This API is used to get the configuration of the task shipped to COS.

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


    def DescribeTopics(self, request):
        """This API is used to get the list of log topics and supports pagination.

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


    def GetAlarmLog(self, request):
        """This API is used to access alarm policy execution details.

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


    def MergePartition(self, request):
        """This API is used to merge a topic partition in read/write state. During merge, a topic partition ID can be specified, and CLS will automatically merge the partition adjacent to the right of the range.

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
        """This API is used to modify an alarm policy. At least one valid configuration item needs to be modified.

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
        """This API is used to modify a notification group.

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
        """This API is used to modify alarm blocking rules.

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


    def ModifyConfig(self, request):
        """This API is used to modify collection rule configuration.

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


    def ModifyConsumer(self, request):
        """This API is used to modify a CKafka delivery task.

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


    def ModifyCosRecharge(self, request):
        """This API is used to modify a COS import task.

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


    def ModifyDataTransform(self, request):
        """This API is used to modify a data processing task.

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


    def ModifyIndex(self, request):
        """This API is used to modify the index configuration. It is subject to the default request frequency limit, and the number of concurrent requests to the same log topic cannot exceed 1, i.e., the index configuration of only one log topic can be modified at a time.

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
        """This API is used to modify Kafka protocol consumption information.

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


    def ModifyKafkaRecharge(self, request):
        """This API is used to modify a Kafka data subscription task.

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
        """This API is used to modify a logset.

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
        """This API is used to modify a machine group.

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


    def ModifyScheduledSql(self, request):
        """This API is used to modify a scheduled SQL analysis task.

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


    def ModifyShipper(self, request):
        """This API is used to modify an existing shipping rule. To use this API, you need to grant CLS the write permission of the specified bucket.

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


    def ModifyTopic(self, request):
        """This API is used to modify a log topic.

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


    def OpenKafkaConsumer(self, request):
        """This API is used to enable the Kafka consumption feature.

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
        """This API is used to preview the logs of Kafka data subscription tasks.

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
        """This API is used to query the latest metric value at a specified time.

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
        """This API is used to query the trend of metrics within a specified time range.

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
        """This API is used to retry a failed shipping task.

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
        """This API is used to preview COS import information.

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


    def SearchLog(self, request):
        """This API is used to search and analyze logs. When using this API, please note the following:1. Besides being subject to the default API request frequency limit by this API, for a single log topic, the concurrency number cannot exceed 15. 2. For search syntax, it's recommended to use the CQL syntax rule. Please use the SyntaxRule parameter and set its value to 1.
        3. The maximum value of API's response data packet is 49MB. It is recommended to enable gzip compression (HTTP Request Header Accept-Encoding: gzip).

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


    def SplitPartition(self, request):
        """This API is used to split a topic partition.

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
        """## Note
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