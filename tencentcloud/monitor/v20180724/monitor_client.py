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
from tencentcloud.monitor.v20180724 import models


class MonitorClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'


    def BindPrometheusManagedGrafana(self, request):
        """This API is used to bind a Grafana instance.

        :param request: Request instance for BindPrometheusManagedGrafana.
        :type request: :class:`tencentcloud.monitor.v20180724.models.BindPrometheusManagedGrafanaRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.BindPrometheusManagedGrafanaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindPrometheusManagedGrafana", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindPrometheusManagedGrafanaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindingPolicyObject(self, request):
        """This API is used to bind an alarm policy to a specific object.

        :param request: Request instance for BindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindingPolicyObject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindingPolicyObjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CleanGrafanaInstance(self, request):
        """This API is used to forcibly terminate a Grafana instance.

        :param request: Request instance for CleanGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CleanGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CleanGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CleanGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CleanGrafanaInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlarmNotice(self, request):
        """This API is used to create a notification template.

        :param request: Request instance for CreateAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarmNotice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAlarmNoticeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlarmPolicy(self, request):
        """This API is used to create a Cloud Monitor alarm policy.

        :param request: Request instance for CreateAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAlarmPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAlertRule(self, request):
        """This API is used to create a Prometheus alerting rule.

        Note that alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively. For more information, see [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/).

        :param request: Request instance for CreateAlertRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateAlertRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlertRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAlertRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateExporterIntegration(self, request):
        """This API is used to create an exporter integration.

        :param request: Request instance for CreateExporterIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateExporterIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateExporterIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExporterIntegration", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateExporterIntegrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGrafanaInstance(self, request):
        """This API is used to create a Grafana instance.

        :param request: Request instance for CreateGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGrafanaInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGrafanaIntegration(self, request):
        """This API is used to create a Grafana integration configuration.

        :param request: Request instance for CreateGrafanaIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGrafanaIntegration", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGrafanaIntegrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateGrafanaNotificationChannel(self, request):
        """This API is used to create a Grafana notification channel.

        :param request: Request instance for CreateGrafanaNotificationChannel.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaNotificationChannelRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateGrafanaNotificationChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGrafanaNotificationChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGrafanaNotificationChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePolicyGroup(self, request):
        """This API is used to add a policy group.

        :param request: Request instance for CreatePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePolicyGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusAgent(self, request):
        """This API is used to create a Prometheus CVM agent.

        :param request: Request instance for CreatePrometheusAgent.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusAgentRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusAgent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusAgentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusMultiTenantInstancePostPayMode(self, request):
        """This API is used to create a pay-as-you-go Prometheus instance.

        :param request: Request instance for CreatePrometheusMultiTenantInstancePostPayMode.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusMultiTenantInstancePostPayModeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusMultiTenantInstancePostPayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusMultiTenantInstancePostPayMode", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusMultiTenantInstancePostPayModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePrometheusScrapeJob(self, request):
        """This API is used to create a Prometheus scrape task.

        :param request: Request instance for CreatePrometheusScrapeJob.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusScrapeJobRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePrometheusScrapeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusScrapeJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePrometheusScrapeJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRecordingRule(self, request):
        """This API is used to create a Prometheus recording rule.

        :param request: Request instance for CreateRecordingRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateRecordingRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateRecordingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecordingRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRecordingRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSSOAccount(self, request):
        """This API is used to authorize a Grafana instance to another Tencent Cloud user.

        :param request: Request instance for CreateSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSSOAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSSOAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceDiscovery(self, request):
        """This API is used to create a Prometheus scrape configuration in TKE.
        <p>Note: The prerequisite is that the corresponding TKE service has been integrated through the Prometheus console. For more information, see
        <a href="https://intl.cloud.tencent.com/document/product/248/48859?from_cn_redirect=1" target="_blank">Agent Management</a>.</p>

        :param request: Request instance for CreateServiceDiscovery.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreateServiceDiscoveryRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreateServiceDiscoveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceDiscovery", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceDiscoveryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlarmNotices(self, request):
        """This API is used to delete alarm notification templates.

        :param request: Request instance for DeleteAlarmNotices.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmNoticesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmNotices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAlarmNoticesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlarmPolicy(self, request):
        """This API is used to delete an alarm policy.

        :param request: Request instance for DeleteAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAlarmPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAlertRules(self, request):
        """This API is used to batch delete Prometheus alerting rules.

        :param request: Request instance for DeleteAlertRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteAlertRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteAlertRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlertRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAlertRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteExporterIntegration(self, request):
        """This API is used to delete an exporter integration.

        :param request: Request instance for DeleteExporterIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteExporterIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteExporterIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExporterIntegration", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteExporterIntegrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGrafanaInstance(self, request):
        """This API is used to delete a Grafana instance.

        :param request: Request instance for DeleteGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGrafanaInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGrafanaIntegration(self, request):
        """This API is used to delete a Grafana integration configuration.

        :param request: Request instance for DeleteGrafanaIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGrafanaIntegration", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGrafanaIntegrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGrafanaNotificationChannel(self, request):
        """This API is used to delete a Grafana notification channel.

        :param request: Request instance for DeleteGrafanaNotificationChannel.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaNotificationChannelRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteGrafanaNotificationChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGrafanaNotificationChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGrafanaNotificationChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePolicyGroup(self, request):
        """This API is used to delete an alarm policy group.

        :param request: Request instance for DeletePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePolicyGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePrometheusScrapeJobs(self, request):
        """This API is used to delete a Prometheus scrape task.

        :param request: Request instance for DeletePrometheusScrapeJobs.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusScrapeJobsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePrometheusScrapeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusScrapeJobs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrometheusScrapeJobsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRecordingRules(self, request):
        """This API is used to batch delete Prometheus recording rules.

        :param request: Request instance for DeleteRecordingRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteRecordingRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteRecordingRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRecordingRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRecordingRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSSOAccount(self, request):
        """This API is used to delete an authorized TCMG user.

        :param request: Request instance for DeleteSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeleteSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeleteSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSSOAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSSOAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccidentEventList(self, request):
        """This API is used to get the platform event list.

        :param request: Request instance for DescribeAccidentEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccidentEventList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccidentEventListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmEvents(self, request):
        """This API is used to query the list of alarm events.

        :param request: Request instance for DescribeAlarmEvents.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmEventsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmHistories(self, request):
        """This API is used to query the alarm records.

        Note: **If you use a sub-account, you can only query the alarm records of authorized projects** or uncategorized products.

        :param request: Request instance for DescribeAlarmHistories.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmHistoriesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmHistoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmHistories", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmHistoriesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmMetrics(self, request):
        """This API is used to query the list of alarm metrics.

        :param request: Request instance for DescribeAlarmMetrics.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmMetricsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmMetrics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmMetricsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmNotice(self, request):
        """This API is used to query the details of a single notification template.

        :param request: Request instance for DescribeAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNotice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmNoticeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmNoticeCallbacks(self, request):
        """This API is used to get all the callback URLs of an alarm notification template.

        :param request: Request instance for DescribeAlarmNoticeCallbacks.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeCallbacksRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticeCallbacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNoticeCallbacks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmNoticeCallbacksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmNotices(self, request):
        """This API is used to query the list of notification templates.

        :param request: Request instance for DescribeAlarmNotices.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmNoticesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmNotices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmNoticesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmPolicies(self, request):
        """This API is used to query the list of alarm policies.

        :param request: Request instance for DescribeAlarmPolicies.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPoliciesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmPolicies", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmPolicy(self, request):
        """This API is used to get the details of a single alarm policy.

        :param request: Request instance for DescribeAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlertRules(self, request):
        """This API is used to query a Prometheus alerting rule.

        :param request: Request instance for DescribeAlertRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAlertRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAlertRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlertRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlertRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAllNamespaces(self, request):
        """This API is used to query all namespaces.

        :param request: Request instance for DescribeAllNamespaces.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAllNamespacesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAllNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllNamespaces", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllNamespacesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBaseMetrics(self, request):
        """This API is used to get the attributes of basic metrics.

        :param request: Request instance for DescribeBaseMetrics.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaseMetrics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBaseMetricsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBasicAlarmList(self, request):
        """This API is used to get the basic alarm list.

        :param request: Request instance for DescribeBasicAlarmList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBasicAlarmList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicAlarmListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBindingPolicyObjectList(self, request):
        """This API is used to get the bound object list.

        :param request: Request instance for DescribeBindingPolicyObjectList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindingPolicyObjectList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindingPolicyObjectListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConditionsTemplateList(self, request):
        """This API is used to get the trigger condition template.

        :param request: Request instance for DescribeConditionsTemplateList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeConditionsTemplateListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeConditionsTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConditionsTemplateList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConditionsTemplateListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDNSConfig(self, request):
        """This API is used to list Grafana DNS configurations.

        :param request: Request instance for DescribeDNSConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeDNSConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeDNSConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDNSConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDNSConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExporterIntegrations(self, request):
        """This API is used to query the list of exporter integrations.

        :param request: Request instance for DescribeExporterIntegrations.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeExporterIntegrationsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeExporterIntegrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExporterIntegrations", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExporterIntegrationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaChannels(self, request):
        """This API is used to list all Grafana alert channels.

        :param request: Request instance for DescribeGrafanaChannels.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaChannelsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaChannels", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGrafanaChannelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaConfig(self, request):
        """This API is used to list Grafana settings, i.e., the `grafana.ini` file content.

        :param request: Request instance for DescribeGrafanaConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGrafanaConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaEnvironments(self, request):
        """This API is used to list Grafana environment variables.

        :param request: Request instance for DescribeGrafanaEnvironments.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaEnvironmentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaEnvironments", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGrafanaEnvironmentsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaInstances(self, request):
        """This API is used to list all Grafana instances under a user account.

        :param request: Request instance for DescribeGrafanaInstances.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGrafanaInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaIntegrations(self, request):
        """This API is used to list installed Grafana integrations.

        :param request: Request instance for DescribeGrafanaIntegrations.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaIntegrationsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaIntegrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaIntegrations", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGrafanaIntegrationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaNotificationChannels(self, request):
        """This API is used to list Grafana notification channels.

        :param request: Request instance for DescribeGrafanaNotificationChannels.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaNotificationChannelsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaNotificationChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaNotificationChannels", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGrafanaNotificationChannelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGrafanaWhiteList(self, request):
        """This API is used to list the Grafana allowlist.

        :param request: Request instance for DescribeGrafanaWhiteList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaWhiteListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeGrafanaWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGrafanaWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGrafanaWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstalledPlugins(self, request):
        """This API is used to list the plugins installed in an instance.

        :param request: Request instance for DescribeInstalledPlugins.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeInstalledPluginsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeInstalledPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstalledPlugins", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstalledPluginsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMonitorTypes(self, request):
        """This API is used to list all the monitor types supported by CM.

        :param request: Request instance for DescribeMonitorTypes.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeMonitorTypesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeMonitorTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorTypes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMonitorTypesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePolicyConditionList(self, request):
        """This API is used to get basic alarm policy conditions.

        :param request: Request instance for DescribePolicyConditionList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyConditionList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyConditionListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePolicyGroupInfo(self, request):
        """This API is used to get details of a basic policy group.

        :param request: Request instance for DescribePolicyGroupInfo.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyGroupInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyGroupInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePolicyGroupList(self, request):
        """This API is used to get the list of basic policy alarm groups.

        :param request: Request instance for DescribePolicyGroupList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePolicyGroupList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyGroupListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProductEventList(self, request):
        """This API is used to get the list of product events by page.

        :param request: Request instance for DescribeProductEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductEventList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductEventListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusAgents(self, request):
        """This API is used to list Prometheus CVM agents.

        :param request: Request instance for DescribePrometheusAgents.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAgentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusAgentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusAgents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusAgentsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusInstances(self, request):
        """This API is used to query the details of one or multiple instances.
        <ul>
        <li>You can query the details of an instance by its ID, name, or status.</li>
        <li>If this parameter is empty, the information of a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.</li>
        </ul>

        :param request: Request instance for DescribePrometheusInstances.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePrometheusScrapeJobs(self, request):
        """This API is used to list Prometheus scrape tasks.

        :param request: Request instance for DescribePrometheusScrapeJobs.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusScrapeJobsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePrometheusScrapeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusScrapeJobs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrometheusScrapeJobsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecordingRules(self, request):
        """This API is used to query Prometheus recording rules by filter.

        :param request: Request instance for DescribeRecordingRules.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeRecordingRulesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeRecordingRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordingRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSSOAccount(self, request):
        """This API is used to list all authorized accounts of the current Grafana instance.

        :param request: Request instance for DescribeSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSSOAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSSOAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceDiscovery(self, request):
        """This API is used to list Prometheus scrape configurations in TKE.
        <p>Note: The prerequisite is that the corresponding TKE service has been integrated through the Prometheus console. For more information, see
        <a href="https://intl.cloud.tencent.com/document/product/248/48859?from_cn_redirect=1" target="_blank">Agent Management</a>.</p>

        :param request: Request instance for DescribeServiceDiscovery.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeServiceDiscoveryRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeServiceDiscoveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceDiscovery", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceDiscoveryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStatisticData(self, request):
        """This API is used to query monitoring data by dimension conditions.

        :param request: Request instance for DescribeStatisticData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeStatisticDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeStatisticDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStatisticData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStatisticDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyPrometheusInstance(self, request):
        """This API is used to delete the data of a Prometheus instance. The specified instance must be terminated first.

        :param request: Request instance for DestroyPrometheusInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DestroyPrometheusInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DestroyPrometheusInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPrometheusInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyPrometheusInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableGrafanaInternet(self, request):
        """This API is used to set the Grafana public network access.

        :param request: Request instance for EnableGrafanaInternet.
        :type request: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaInternetRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaInternetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableGrafanaInternet", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableGrafanaInternetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableGrafanaSSO(self, request):
        """This API is used to set the Grafana SSO through a Tencent Cloud account.

        :param request: Request instance for EnableGrafanaSSO.
        :type request: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaSSORequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.EnableGrafanaSSOResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableGrafanaSSO", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableGrafanaSSOResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableSSOCamCheck(self, request):
        """This API is used to set whether to enable CAM authentication during SSO.

        :param request: Request instance for EnableSSOCamCheck.
        :type request: :class:`tencentcloud.monitor.v20180724.models.EnableSSOCamCheckRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.EnableSSOCamCheckResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableSSOCamCheck", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableSSOCamCheckResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetMonitorData(self, request):
        """This API is used to get the monitoring data of Tencent Cloud services except TKE. To pull TKE’s monitoring data, use the [DescribeStatisticData](https://www.tencentcloud.com/document/product/248/39481) API.
        You can get the monitoring data of a Tencent Cloud service by passing in its namespace, object dimension description, and monitoring metrics.
        API call rate limit: 20 calls/second (1,200 calls/minute). A single request can get the data of up to 10 instances for up to 1,440 data points.
        If you need to call a large number of APIs to pull metrics or objects at a time, some APIs may fail to be called due to the rate limit. We suggest you evenly arrange API calls at a time granularity.

        :param request: Request instance for GetMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetMonitorData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetMonitorDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetPrometheusAgentManagementCommand(self, request):
        """This API is used to get the command line for Prometheus agent management.

        :param request: Request instance for GetPrometheusAgentManagementCommand.
        :type request: :class:`tencentcloud.monitor.v20180724.models.GetPrometheusAgentManagementCommandRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.GetPrometheusAgentManagementCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPrometheusAgentManagementCommand", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPrometheusAgentManagementCommandResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InstallPlugins(self, request):
        """This API is used to install a Grafana plugin.

        :param request: Request instance for InstallPlugins.
        :type request: :class:`tencentcloud.monitor.v20180724.models.InstallPluginsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.InstallPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallPlugins", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InstallPluginsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmNotice(self, request):
        """This API is used to edit an alarm notification template.

        :param request: Request instance for ModifyAlarmNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmNotice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmNoticeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyCondition(self, request):
        """This API is used to modify the trigger condition of an alarm policy.

        :param request: Request instance for ModifyAlarmPolicyCondition.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyConditionRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyConditionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyCondition", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyConditionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyInfo(self, request):
        """This API is used to edit the basic information of a v2.0 alarm policy, including policy name and remarks.

        :param request: Request instance for ModifyAlarmPolicyInfo.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyInfoRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyNotice(self, request):
        """This API is used to modify the alarm notification template bound to an alarm policy.

        :param request: Request instance for ModifyAlarmPolicyNotice.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyNoticeRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyNoticeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyNotice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyNoticeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyStatus(self, request):
        """This API is used to enable/disable an alarm policy.

        :param request: Request instance for ModifyAlarmPolicyStatus.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyStatusRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmPolicyTasks(self, request):
        """This API is used to modify the task triggered by an alarm policy. The `TriggerTasks` field contains the list of triggered tasks. If an empty array is passed in for `TriggerTasks`, it indicates to unbind all the triggered tasks from this policy.

        :param request: Request instance for ModifyAlarmPolicyTasks.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyTasksRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmPolicyTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmPolicyTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmPolicyTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAlarmReceivers(self, request):
        """This API is used to modify alarm recipients.

        :param request: Request instance for ModifyAlarmReceivers.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmReceivers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmReceiversResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGrafanaInstance(self, request):
        """This API is used to modify the attributes of a Grafana instance.

        :param request: Request instance for ModifyGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGrafanaInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPolicyGroup(self, request):
        """This API is used to update policy group.

        :param request: Request instance for ModifyPolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPolicyGroup", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPolicyGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrometheusInstanceAttributes(self, request):
        """This API is used to modify the attributes of a Prometheus instance.

        :param request: Request instance for ModifyPrometheusInstanceAttributes.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPrometheusInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusInstanceAttributes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrometheusInstanceAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PutMonitorData(self, request):
        """The default API request rate limit is 50 requests/sec.
        The default upper limit on metrics of a single tenant is 100.
        A maximum of 30 metric/value pairs can be reported at a time. When an error is returned for a request, no metrics/values in the request will be saved.

        The reporting timestamp is the timestamp when you want to save the data. We recommend that you construct a timestamp at integer minutes.
        The time range of a timestamp is from 300 seconds before the current time to the current time.
        The data of the same IP metric/value pair must be reported by minute in chronological order.

        :param request: Request instance for PutMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutMonitorData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutMonitorDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeGrafanaInstance(self, request):
        """This API is used to restore a Grafana instance.

        :param request: Request instance for ResumeGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ResumeGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ResumeGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeGrafanaInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendCustomAlarmMsg(self, request):
        """This API is used to send a custom alarm notification.

        :param request: Request instance for SendCustomAlarmMsg.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendCustomAlarmMsg", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendCustomAlarmMsgResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetDefaultAlarmPolicy(self, request):
        """This API is used to set an alarm policy as the default policy in the current policy type under the current project.
        Alarm policies in the same type under the project will be set as non-default.

        :param request: Request instance for SetDefaultAlarmPolicy.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SetDefaultAlarmPolicyRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SetDefaultAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDefaultAlarmPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetDefaultAlarmPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminatePrometheusInstances(self, request):
        """This API is used to terminate a pay-as-you-go Prometheus instance.

        :param request: Request instance for TerminatePrometheusInstances.
        :type request: :class:`tencentcloud.monitor.v20180724.models.TerminatePrometheusInstancesRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.TerminatePrometheusInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminatePrometheusInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminatePrometheusInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindingAllPolicyObject(self, request):
        """This API is used to delete all bound objects.

        :param request: Request instance for UnBindingAllPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindingAllPolicyObject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindingAllPolicyObjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindingPolicyObject(self, request):
        """This API is used to delete an object that is bound to a policy.

        :param request: Request instance for UnBindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindingPolicyObject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindingPolicyObjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindPrometheusManagedGrafana(self, request):
        """This API is used to unbind a Grafana instance from an instance.

        :param request: Request instance for UnbindPrometheusManagedGrafana.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnbindPrometheusManagedGrafanaRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnbindPrometheusManagedGrafanaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindPrometheusManagedGrafana", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindPrometheusManagedGrafanaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UninstallGrafanaDashboard(self, request):
        """This API is used to delete a Grafana dashboard.

        :param request: Request instance for UninstallGrafanaDashboard.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaDashboardRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallGrafanaDashboard", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UninstallGrafanaDashboardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UninstallGrafanaPlugins(self, request):
        """This API is used to delete installed plugins.

        :param request: Request instance for UninstallGrafanaPlugins.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaPluginsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UninstallGrafanaPluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallGrafanaPlugins", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UninstallGrafanaPluginsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAlertRule(self, request):
        """This API is used to update a Prometheus alerting rule.

        Note that alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively. For more information, see [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/).

        :param request: Request instance for UpdateAlertRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlertRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAlertRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAlertRuleState(self, request):
        """This API is used to update the status of a Prometheus alerting rule.

        :param request: Request instance for UpdateAlertRuleState.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleStateRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateAlertRuleStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlertRuleState", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAlertRuleStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDNSConfig(self, request):
        """This API is used to update the Grafana DNS configuration.

        :param request: Request instance for UpdateDNSConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateDNSConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateDNSConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDNSConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDNSConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateExporterIntegration(self, request):
        """This API is used to update the exporter integration configuration.

        :param request: Request instance for UpdateExporterIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateExporterIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateExporterIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateExporterIntegration", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateExporterIntegrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaConfig(self, request):
        """This API is used to update the Grafana configuration.

        :param request: Request instance for UpdateGrafanaConfig.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaConfigRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGrafanaConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaEnvironments(self, request):
        """This API is used to update Grafana environment variables.

        :param request: Request instance for UpdateGrafanaEnvironments.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaEnvironmentsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaEnvironments", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGrafanaEnvironmentsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaIntegration(self, request):
        """This API is used to update the Grafana integration configuration.

        :param request: Request instance for UpdateGrafanaIntegration.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaIntegrationRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaIntegrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaIntegration", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGrafanaIntegrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaNotificationChannel(self, request):
        """This API is used to update the Grafana notification channel.

        :param request: Request instance for UpdateGrafanaNotificationChannel.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaNotificationChannelRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaNotificationChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaNotificationChannel", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGrafanaNotificationChannelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateGrafanaWhiteList(self, request):
        """This API is used to update the Grafana allowlist.

        :param request: Request instance for UpdateGrafanaWhiteList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaWhiteListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateGrafanaWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGrafanaWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGrafanaWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdatePrometheusAgentStatus(self, request):
        """This API is used to update the status of a Prometheus CVM agent.

        :param request: Request instance for UpdatePrometheusAgentStatus.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusAgentStatusRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusAgentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePrometheusAgentStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePrometheusAgentStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdatePrometheusScrapeJob(self, request):
        """This API is used to update a Prometheus scrape task.

        :param request: Request instance for UpdatePrometheusScrapeJob.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusScrapeJobRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdatePrometheusScrapeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePrometheusScrapeJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePrometheusScrapeJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRecordingRule(self, request):
        """This API is used to update a Prometheus recording rule.

        :param request: Request instance for UpdateRecordingRule.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateRecordingRuleRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateRecordingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRecordingRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRecordingRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateSSOAccount(self, request):
        """This API is used to update the remarks and permission information of an authorized account in an overwriting manner.

        :param request: Request instance for UpdateSSOAccount.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpdateSSOAccountRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpdateSSOAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSSOAccount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSSOAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeGrafanaDashboard(self, request):
        """This API is used to update a Grafana dashboard.

        :param request: Request instance for UpgradeGrafanaDashboard.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaDashboardRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeGrafanaDashboard", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeGrafanaDashboardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeGrafanaInstance(self, request):
        """This API is used to upgrade a Grafana instance.

        :param request: Request instance for UpgradeGrafanaInstance.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaInstanceRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UpgradeGrafanaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeGrafanaInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeGrafanaInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)