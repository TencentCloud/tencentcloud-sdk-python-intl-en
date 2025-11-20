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
from tencentcloud.monitor.v20180724 import models
from typing import Dict


class MonitorClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'monitor.intl.tencentcloudapi.com'
    _service = 'monitor'

    async def BindPrometheusManagedGrafana(
            self,
            request: models.BindPrometheusManagedGrafanaRequest,
            opts: Dict = None,
    ) -> models.BindPrometheusManagedGrafanaResponse:
        """
        This API is used to bind a Grafana instance.
        """
        
        kwargs = {}
        kwargs["action"] = "BindPrometheusManagedGrafana"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindPrometheusManagedGrafanaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindingPolicyObject(
            self,
            request: models.BindingPolicyObjectRequest,
            opts: Dict = None,
    ) -> models.BindingPolicyObjectResponse:
        """
        This API is used to bind an alarm policy to a specific object.
        """
        
        kwargs = {}
        kwargs["action"] = "BindingPolicyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindingPolicyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIsPrometheusNewUser(
            self,
            request: models.CheckIsPrometheusNewUserRequest,
            opts: Dict = None,
    ) -> models.CheckIsPrometheusNewUserResponse:
        """
        This API is used to determine whether the user is new to TMP, that is, whether the user has never created a TMP instance in any region.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIsPrometheusNewUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIsPrometheusNewUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CleanGrafanaInstance(
            self,
            request: models.CleanGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.CleanGrafanaInstanceResponse:
        """
        This API is used to forcibly terminate a Grafana instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CleanGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CleanGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmNotice(
            self,
            request: models.CreateAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmNoticeResponse:
        """
        This API is used to create a notification template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlarmPolicy(
            self,
            request: models.CreateAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAlarmPolicyResponse:
        """
        This API is used to create an alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAlertRule(
            self,
            request: models.CreateAlertRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAlertRuleResponse:
        """
        This API is used to create a Prometheus alerting rule.

        Note that alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively. For more information, see [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExporterIntegration(
            self,
            request: models.CreateExporterIntegrationRequest,
            opts: Dict = None,
    ) -> models.CreateExporterIntegrationResponse:
        """
        Create an exporter integration in the integration center. Due to the considerable number of integrations, it is advisable to create through the console.  **Prerequisite:** Authorized to create a managed EKS cluster.  **Verification method:** 1. Confirm on the console interface. If no authorization notification appears, it indicates authorization is granted. 2. Query the cluster status via the `DescribePrometheusInstanceInitStatus` API. If the managed cluster does not exist, create it using the `RunPrometheusInstance` API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExporterIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExporterIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGrafanaInstance(
            self,
            request: models.CreateGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateGrafanaInstanceResponse:
        """
        This API is used to create a monthly subscribed TCMG instance of the Basic Edition, with auto-renewal enabled and vouchers not allowed by default.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGrafanaIntegration(
            self,
            request: models.CreateGrafanaIntegrationRequest,
            opts: Dict = None,
    ) -> models.CreateGrafanaIntegrationResponse:
        """
        This API is used to create a Grafana integration configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGrafanaIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGrafanaIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGrafanaNotificationChannel(
            self,
            request: models.CreateGrafanaNotificationChannelRequest,
            opts: Dict = None,
    ) -> models.CreateGrafanaNotificationChannelResponse:
        """
        This API is used to create a Grafana notification channel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGrafanaNotificationChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGrafanaNotificationChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePolicyGroup(
            self,
            request: models.CreatePolicyGroupRequest,
            opts: Dict = None,
    ) -> models.CreatePolicyGroupResponse:
        """
        This API is used to add a policy group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePolicyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePolicyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAgent(
            self,
            request: models.CreatePrometheusAgentRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAgentResponse:
        """
        This API is used to create a Prometheus CVM agent.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAlertGroup(
            self,
            request: models.CreatePrometheusAlertGroupRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAlertGroupResponse:
        """
        This API is used to create a Prometheus alert rule groups.

        This API is used to group alert rules, which can include multiple alert rules. Alert messages within the group are sent via the alert group's notification template.
        This API is used to enable individually creating enabled/disabled alert rules under an alert group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAlertGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAlertGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAlertPolicy(
            self,
            request: models.CreatePrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAlertPolicyResponse:
        """
        This API is used to create an alerting rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusClusterAgent(
            self,
            request: models.CreatePrometheusClusterAgentRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusClusterAgentResponse:
        """
        This API is used to associate a cluster with a Cloud Monitor (CM)-integrated Tencent Managed Service for Prometheus (TMP) 2.0 instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusConfig(
            self,
            request: models.CreatePrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusConfigResponse:
        """
        This API is used to create Prometheus configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusGlobalNotification(
            self,
            request: models.CreatePrometheusGlobalNotificationRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusGlobalNotificationResponse:
        """
        This API is used to create a global alert notification channel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusGlobalNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusGlobalNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusMultiTenantInstancePostPayMode(
            self,
            request: models.CreatePrometheusMultiTenantInstancePostPayModeRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusMultiTenantInstancePostPayModeResponse:
        """
        This API is used to create a pay-as-you-go Prometheus instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusMultiTenantInstancePostPayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusMultiTenantInstancePostPayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusRecordRuleYaml(
            self,
            request: models.CreatePrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusRecordRuleYamlResponse:
        """
        This API is used to create a recording rule in the YAML way.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusScrapeJob(
            self,
            request: models.CreatePrometheusScrapeJobRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusScrapeJobResponse:
        """
        This API is used to create a Prometheus scrape task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusScrapeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusScrapeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusTemp(
            self,
            request: models.CreatePrometheusTempRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusTempResponse:
        """
        This API is used to create a TMP template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordingRule(
            self,
            request: models.CreateRecordingRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRecordingRuleResponse:
        """
        This API is used to create a Prometheus recording rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSSOAccount(
            self,
            request: models.CreateSSOAccountRequest,
            opts: Dict = None,
    ) -> models.CreateSSOAccountResponse:
        """
        This API is used to authorize a Grafana instance to another Tencent Cloud user.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceDiscovery(
            self,
            request: models.CreateServiceDiscoveryRequest,
            opts: Dict = None,
    ) -> models.CreateServiceDiscoveryResponse:
        """
        This API is used to create a Prometheus scrape configuration in TKE.
        <p>Note: The prerequisite is that the corresponding TKE service has been integrated through the Prometheus console. For more information, see
        <a href="https://intl.cloud.tencent.com/document/product/248/48859?from_cn_redirect=1" target="_blank">Agent Management</a>.</p>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceDiscovery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceDiscoveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmNotices(
            self,
            request: models.DeleteAlarmNoticesRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmNoticesResponse:
        """
        This API is used to delete an alarm notification template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmNotices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmNoticesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlarmPolicy(
            self,
            request: models.DeleteAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAlarmPolicyResponse:
        """
        This API is used to delete an alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAlertRules(
            self,
            request: models.DeleteAlertRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteAlertRulesResponse:
        """
        This API is used to batch delete Prometheus alerting rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAlertRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAlertRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteExporterIntegration(
            self,
            request: models.DeleteExporterIntegrationRequest,
            opts: Dict = None,
    ) -> models.DeleteExporterIntegrationResponse:
        """
        This API is used to delete an exporter integration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteExporterIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteExporterIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGrafanaInstance(
            self,
            request: models.DeleteGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteGrafanaInstanceResponse:
        """
        This API is used to refund a monthly subscribed TCMG instance. Once it is called, the instance cannot be used and will be automatically terminated seven days later.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGrafanaIntegration(
            self,
            request: models.DeleteGrafanaIntegrationRequest,
            opts: Dict = None,
    ) -> models.DeleteGrafanaIntegrationResponse:
        """
        This API is used to delete a Grafana integration configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGrafanaIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGrafanaIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGrafanaNotificationChannel(
            self,
            request: models.DeleteGrafanaNotificationChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteGrafanaNotificationChannelResponse:
        """
        This API is used to delete a Grafana notification channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGrafanaNotificationChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGrafanaNotificationChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePolicyGroup(
            self,
            request: models.DeletePolicyGroupRequest,
            opts: Dict = None,
    ) -> models.DeletePolicyGroupResponse:
        """
        This API is used to delete an alarm policy group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePolicyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePolicyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusAlertGroups(
            self,
            request: models.DeletePrometheusAlertGroupsRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusAlertGroupsResponse:
        """
        This API is used to delete Prometheus alert rule groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusAlertGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusAlertGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusAlertPolicy(
            self,
            request: models.DeletePrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusAlertPolicyResponse:
        """
        This API is used to delete a TMP 2.0 instance alerting rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusClusterAgent(
            self,
            request: models.DeletePrometheusClusterAgentRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusClusterAgentResponse:
        """
        This API is used to disassociate a TMP instance from a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusClusterAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusClusterAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusConfig(
            self,
            request: models.DeletePrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusConfigResponse:
        """
        This API is used to delete Prometheus configurations. If the target cluster does not exist, a result indicating success will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusRecordRuleYaml(
            self,
            request: models.DeletePrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusRecordRuleYamlResponse:
        """
        This API is used to delete a recording instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusScrapeJobs(
            self,
            request: models.DeletePrometheusScrapeJobsRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusScrapeJobsResponse:
        """
        This API is used to delete a Prometheus scrape task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusScrapeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusScrapeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusTemp(
            self,
            request: models.DeletePrometheusTempRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusTempResponse:
        """
        This API is used to delete a TMP template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusTempSync(
            self,
            request: models.DeletePrometheusTempSyncRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusTempSyncResponse:
        """
        This API is used to unsync a template, which will delete the configuration generated by the template in the target. It takes effect for v2 instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusTempSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusTempSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordingRules(
            self,
            request: models.DeleteRecordingRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordingRulesResponse:
        """
        This API is used to batch delete Prometheus recording rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordingRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordingRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSSOAccount(
            self,
            request: models.DeleteSSOAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteSSOAccountResponse:
        """
        This API is used to delete an authorized TCMG user.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccidentEventList(
            self,
            request: models.DescribeAccidentEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccidentEventListResponse:
        """
        This API is used to get the platform event list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccidentEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccidentEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmEvents(
            self,
            request: models.DescribeAlarmEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmEventsResponse:
        """
        This API is used to query the list of alarm events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmHistories(
            self,
            request: models.DescribeAlarmHistoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmHistoriesResponse:
        """
        This API is used to query the alarm records.

        Note: **If you use a sub-account, you can only query the alarm records of authorized projects** or uncategorized products.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmHistories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmHistoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmMetrics(
            self,
            request: models.DescribeAlarmMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmMetricsResponse:
        """
        This API is used to query the list of alarm metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotice(
            self,
            request: models.DescribeAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticeResponse:
        """
        This API is used to query the details of a single notification template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNoticeCallbacks(
            self,
            request: models.DescribeAlarmNoticeCallbacksRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticeCallbacksResponse:
        """
        This API is used to obtain all the callback URLs of an alarm notification template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNoticeCallbacks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticeCallbacksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotices(
            self,
            request: models.DescribeAlarmNoticesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNoticesResponse:
        """
        This API is used to query the list of notification templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNoticesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmPolicies(
            self,
            request: models.DescribeAlarmPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmPoliciesResponse:
        """
        This API is used to query the list of alarm policies.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmPolicy(
            self,
            request: models.DescribeAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmPolicyResponse:
        """
        This API is used to get the details of a single alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlertRules(
            self,
            request: models.DescribeAlertRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlertRulesResponse:
        """
        This API is used to query a Prometheus alerting rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlertRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlertRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllNamespaces(
            self,
            request: models.DescribeAllNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeAllNamespacesResponse:
        """
        This API is used to query all namespaces.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaseMetrics(
            self,
            request: models.DescribeBaseMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeBaseMetricsResponse:
        """
        This API is used to get the attributes of basic metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaseMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaseMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBasicAlarmList(
            self,
            request: models.DescribeBasicAlarmListRequest,
            opts: Dict = None,
    ) -> models.DescribeBasicAlarmListResponse:
        """
        This API is used to get the basic alarm list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBasicAlarmList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBasicAlarmListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBindingPolicyObjectList(
            self,
            request: models.DescribeBindingPolicyObjectListRequest,
            opts: Dict = None,
    ) -> models.DescribeBindingPolicyObjectListResponse:
        """
        This API is used to get the bound object list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBindingPolicyObjectList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBindingPolicyObjectListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAgentCreatingProgress(
            self,
            request: models.DescribeClusterAgentCreatingProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAgentCreatingProgressResponse:
        """
        This API is used to obtain the binding status between the TencentCloud Managed Service for Prometheus instance and the TKE cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAgentCreatingProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAgentCreatingProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConditionsTemplateList(
            self,
            request: models.DescribeConditionsTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeConditionsTemplateListResponse:
        """
        This API is used to get the trigger condition template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConditionsTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConditionsTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDNSConfig(
            self,
            request: models.DescribeDNSConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDNSConfigResponse:
        """
        This API is used to list Grafana DNS configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDNSConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDNSConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExporterIntegrations(
            self,
            request: models.DescribeExporterIntegrationsRequest,
            opts: Dict = None,
    ) -> models.DescribeExporterIntegrationsResponse:
        """
        This API is used to query the list of exporter integrations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExporterIntegrations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExporterIntegrationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaChannels(
            self,
            request: models.DescribeGrafanaChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaChannelsResponse:
        """
        This API is used to list all Grafana alert channels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaConfig(
            self,
            request: models.DescribeGrafanaConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaConfigResponse:
        """
        This API is used to list Grafana settings, i.e., the `grafana.ini` file content.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaEnvironments(
            self,
            request: models.DescribeGrafanaEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaEnvironmentsResponse:
        """
        This API is used to list Grafana environment variables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaInstances(
            self,
            request: models.DescribeGrafanaInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaInstancesResponse:
        """
        This API is used to list all Grafana instances under a user account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaIntegrations(
            self,
            request: models.DescribeGrafanaIntegrationsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaIntegrationsResponse:
        """
        This API is used to list installed Grafana integrations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaIntegrations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaIntegrationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaNotificationChannels(
            self,
            request: models.DescribeGrafanaNotificationChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaNotificationChannelsResponse:
        """
        This API is used to list Grafana notification channels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaNotificationChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaNotificationChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGrafanaWhiteList(
            self,
            request: models.DescribeGrafanaWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeGrafanaWhiteListResponse:
        """
        This API is used to list the Grafana allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGrafanaWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGrafanaWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstalledPlugins(
            self,
            request: models.DescribeInstalledPluginsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstalledPluginsResponse:
        """
        This API is used to list the plugins installed in an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstalledPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstalledPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonitorTypes(
            self,
            request: models.DescribeMonitorTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeMonitorTypesResponse:
        """
        This API is used to list all the monitoring types supported by CM.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonitorTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonitorTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyConditionList(
            self,
            request: models.DescribePolicyConditionListRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyConditionListResponse:
        """
        This API is used to get basic alarm policy conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyConditionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyConditionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyGroupInfo(
            self,
            request: models.DescribePolicyGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyGroupInfoResponse:
        """
        This API is used to get details of a basic policy group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePolicyGroupList(
            self,
            request: models.DescribePolicyGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribePolicyGroupListResponse:
        """
        This API is used to get the list of basic policy alarm groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePolicyGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePolicyGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductEventList(
            self,
            request: models.DescribeProductEventListRequest,
            opts: Dict = None,
    ) -> models.DescribeProductEventListResponse:
        """
        This API is used to get the list of product events by page.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductEventList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductEventListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAgentInstances(
            self,
            request: models.DescribePrometheusAgentInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAgentInstancesResponse:
        """
        This API is used to get the list of instances associated with the target cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAgentInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAgentInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAgents(
            self,
            request: models.DescribePrometheusAgentsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAgentsResponse:
        """
        This API is used to list Prometheus CVM agents.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAlertGroups(
            self,
            request: models.DescribePrometheusAlertGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAlertGroupsResponse:
        """
        This API is used to query alarm groups under a given prometheus.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAlertGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAlertGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusAlertPolicy(
            self,
            request: models.DescribePrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusAlertPolicyResponse:
        """
        This API is used to get the list of v2.0 instance alerting rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusClusterAgents(
            self,
            request: models.DescribePrometheusClusterAgentsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusClusterAgentsResponse:
        """
        This API is used to get the list of clusters associated with the TMP instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusClusterAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusClusterAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusConfig(
            self,
            request: models.DescribePrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusConfigResponse:
        """
        This API is used to get the Prometheus configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusGlobalConfig(
            self,
            request: models.DescribePrometheusGlobalConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusGlobalConfigResponse:
        """
        This API is used to get the instance-level scrape configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusGlobalConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusGlobalConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusGlobalNotification(
            self,
            request: models.DescribePrometheusGlobalNotificationRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusGlobalNotificationResponse:
        """
        This API is used to query the global alert notification channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusGlobalNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusGlobalNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstanceDetail(
            self,
            request: models.DescribePrometheusInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceDetailResponse:
        """
        This API is used to get the details of a TMP instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstanceInitStatus(
            self,
            request: models.DescribePrometheusInstanceInitStatusRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceInitStatusResponse:
        """
        This API is used to get the initialization task status of a v2.0 instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstanceInitStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceInitStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstanceUsage(
            self,
            request: models.DescribePrometheusInstanceUsageRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceUsageResponse:
        """
        This API is used to query the usage of a pay-as-you-go Tencent Managed Service for Prometheus (TMP) instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstanceUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstances(
            self,
            request: models.DescribePrometheusInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstancesResponse:
        """
        This API is used to query the details of one or multiple instances.
        <ul>
        <li>You can query the details of an instance by its ID, name, or status.</li>
        <li>If this parameter is empty, the information of a certain number of instances under the current account will be returned. The number is specified by `Limit` and is 20 by default.</li>
        </ul>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstancesOverview(
            self,
            request: models.DescribePrometheusInstancesOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstancesOverviewResponse:
        """
        This API is used to obtain the list of Tencent Managed Service for Prometheus (TMP) instances and the clusters associated with them.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstancesOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstancesOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusRecordRuleYaml(
            self,
            request: models.DescribePrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusRecordRuleYamlResponse:
        """
        This API is used to get the YAML list of Prometheus recording rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusRecordRules(
            self,
            request: models.DescribePrometheusRecordRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusRecordRulesResponse:
        """
        This API is used to get the list of recording rules, including those created by CRD resources in the associated cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusRecordRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusRecordRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusScrapeJobs(
            self,
            request: models.DescribePrometheusScrapeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusScrapeJobsResponse:
        """
        This API is used to list Prometheus scrape tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusScrapeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusScrapeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTargetsTMP(
            self,
            request: models.DescribePrometheusTargetsTMPRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTargetsTMPResponse:
        """
        This API is used to get the targets information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTargetsTMP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTargetsTMPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTemp(
            self,
            request: models.DescribePrometheusTempRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTempResponse:
        """
        This API is used to get the list of templates, where the default template is always on top.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusTempSync(
            self,
            request: models.DescribePrometheusTempSyncRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusTempSyncResponse:
        """
        This API is used to get the information of instances associated with a template. It takes effect for v2 instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusTempSync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusTempSyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusZones(
            self,
            request: models.DescribePrometheusZonesRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusZonesResponse:
        """
        This API is used to list the AZs of Tencent Managed Service for Prometheus (TMP).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordingRules(
            self,
            request: models.DescribeRecordingRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordingRulesResponse:
        """
        This API is used to query Prometheus recording rules by filter.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordingRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordingRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSSOAccount(
            self,
            request: models.DescribeSSOAccountRequest,
            opts: Dict = None,
    ) -> models.DescribeSSOAccountResponse:
        """
        This API is used to list all authorized accounts of the current Grafana instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceDiscovery(
            self,
            request: models.DescribeServiceDiscoveryRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceDiscoveryResponse:
        """
        This API is used to list Prometheus scrape configurations in TKE.
        <p>Note: The prerequisite is that the corresponding TKE service has been integrated through the Prometheus console. For more information, see
        <a href="https://intl.cloud.tencent.com/document/product/248/48859?from_cn_redirect=1" target="_blank">Agent Management</a>.</p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceDiscovery"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceDiscoveryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStatisticData(
            self,
            request: models.DescribeStatisticDataRequest,
            opts: Dict = None,
    ) -> models.DescribeStatisticDataResponse:
        """
        This API is used to query monitoring data by dimension conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatisticData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatisticDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPrometheusInstance(
            self,
            request: models.DestroyPrometheusInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPrometheusInstanceResponse:
        """
        This API is used to delete the data of a Prometheus instance. The specified instance must be terminated first.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPrometheusInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPrometheusInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableGrafanaInternet(
            self,
            request: models.EnableGrafanaInternetRequest,
            opts: Dict = None,
    ) -> models.EnableGrafanaInternetResponse:
        """
        This API is used to set the Grafana public network access.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableGrafanaInternet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableGrafanaInternetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableGrafanaSSO(
            self,
            request: models.EnableGrafanaSSORequest,
            opts: Dict = None,
    ) -> models.EnableGrafanaSSOResponse:
        """
        This API is used to set the Grafana SSO through a Tencent Cloud account.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableGrafanaSSO"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableGrafanaSSOResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSSOCamCheck(
            self,
            request: models.EnableSSOCamCheckRequest,
            opts: Dict = None,
    ) -> models.EnableSSOCamCheckResponse:
        """
        This API is used to set whether to enable CAM authentication during SSO.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSSOCamCheck"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableSSOCamCheckResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMonitorData(
            self,
            request: models.GetMonitorDataRequest,
            opts: Dict = None,
    ) -> models.GetMonitorDataResponse:
        """
        This API is used to get the monitoring data of Tencent Cloud services except TKE. To pull TKE’s monitoring data, use the [DescribeStatisticData](https://www.tencentcloud.com/document/product/248/39481) API.
        You can get the monitoring data of a Tencent Cloud service by passing in its namespace, object dimension description, and monitoring metrics.
        API call rate limit: 20 calls/second (1,200 calls/minute). A single request can get the data of up to 10 instances for up to 1,440 data points.
        If you need to call a large number of APIs to pull metrics or objects at a time, some APIs may fail to be called due to the rate limit. We suggest you evenly arrange API calls at a time granularity.
        """
        
        kwargs = {}
        kwargs["action"] = "GetMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPrometheusAgentManagementCommand(
            self,
            request: models.GetPrometheusAgentManagementCommandRequest,
            opts: Dict = None,
    ) -> models.GetPrometheusAgentManagementCommandResponse:
        """
        This API is used to get the command line for Prometheus agent management.
        """
        
        kwargs = {}
        kwargs["action"] = "GetPrometheusAgentManagementCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPrometheusAgentManagementCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallPlugins(
            self,
            request: models.InstallPluginsRequest,
            opts: Dict = None,
    ) -> models.InstallPluginsResponse:
        """
        This API is used to install a Grafana plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "InstallPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmNotice(
            self,
            request: models.ModifyAlarmNoticeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmNoticeResponse:
        """
        This API is used to edit an alarm notification template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyCondition(
            self,
            request: models.ModifyAlarmPolicyConditionRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyConditionResponse:
        """
        This API is used to modify the trigger condition of an alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyCondition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyConditionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyInfo(
            self,
            request: models.ModifyAlarmPolicyInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyInfoResponse:
        """
        This API is used to edit the basic information of a v2.0 alarm policy, including policy name and remarks.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyNotice(
            self,
            request: models.ModifyAlarmPolicyNoticeRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyNoticeResponse:
        """
        This API is used to modify the alarm notification template bound to an alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyNotice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyNoticeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyStatus(
            self,
            request: models.ModifyAlarmPolicyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyStatusResponse:
        """
        This API is used to enable/disable an alarm policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmPolicyTasks(
            self,
            request: models.ModifyAlarmPolicyTasksRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmPolicyTasksResponse:
        """
        This API is used to modify the tasks triggered by alarm policy, which are listed by the value of the `TriggerTasks` field. If an empty array is passed in for `TriggerTasks`, it means unbinding all the trigger tasks from the policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmPolicyTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmPolicyTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAlarmReceivers(
            self,
            request: models.ModifyAlarmReceiversRequest,
            opts: Dict = None,
    ) -> models.ModifyAlarmReceiversResponse:
        """
        This API is used to modify alarm recipients.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAlarmReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAlarmReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGrafanaInstance(
            self,
            request: models.ModifyGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyGrafanaInstanceResponse:
        """
        This API is used to modify the attributes of a Grafana instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPolicyGroup(
            self,
            request: models.ModifyPolicyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyPolicyGroupResponse:
        """
        This API is used to update policy group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPolicyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPolicyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusAgentExternalLabels(
            self,
            request: models.ModifyPrometheusAgentExternalLabelsRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusAgentExternalLabelsResponse:
        """
        This API is used to modify the external labels of the associated cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusAgentExternalLabels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusAgentExternalLabelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusAlertPolicy(
            self,
            request: models.ModifyPrometheusAlertPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusAlertPolicyResponse:
        """
        This API is used to modify a TMP 2.0 instance alerting rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusAlertPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusAlertPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusConfig(
            self,
            request: models.ModifyPrometheusConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusConfigResponse:
        """
        This API is used to modify the Prometheus configuration. If there are no configuration items, one will be added.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusGlobalNotification(
            self,
            request: models.ModifyPrometheusGlobalNotificationRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusGlobalNotificationResponse:
        """
        This API is used to modify the global alert notification channel.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusGlobalNotification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusGlobalNotificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusInstanceAttributes(
            self,
            request: models.ModifyPrometheusInstanceAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusInstanceAttributesResponse:
        """
        This API is used to modify the attributes of a Prometheus instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusInstanceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusInstanceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusRecordRuleYaml(
            self,
            request: models.ModifyPrometheusRecordRuleYamlRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusRecordRuleYamlResponse:
        """
        This API is used to modify a Prometheus recording instance through YAML.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusRecordRuleYaml"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusRecordRuleYamlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusTemp(
            self,
            request: models.ModifyPrometheusTempRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusTempResponse:
        """
        This API is used to modify a template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeGrafanaInstance(
            self,
            request: models.ResumeGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeGrafanaInstanceResponse:
        """
        This API is used to renew a monthly subscribed TCMG instance for a month without changing the instance edition. It doesn't apply to running instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunPrometheusInstance(
            self,
            request: models.RunPrometheusInstanceRequest,
            opts: Dict = None,
    ) -> models.RunPrometheusInstanceResponse:
        """
        This API is used to initialize a TMP instance, which is called when the integration center is enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "RunPrometheusInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunPrometheusInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendCustomAlarmMsg(
            self,
            request: models.SendCustomAlarmMsgRequest,
            opts: Dict = None,
    ) -> models.SendCustomAlarmMsgResponse:
        """
        This API is used to send a custom alarm notification.
        """
        
        kwargs = {}
        kwargs["action"] = "SendCustomAlarmMsg"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendCustomAlarmMsgResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetDefaultAlarmPolicy(
            self,
            request: models.SetDefaultAlarmPolicyRequest,
            opts: Dict = None,
    ) -> models.SetDefaultAlarmPolicyResponse:
        """
        This API is used to set an alarm policy as the default policy in the current policy type under the current project.
        Alarm policies in the same type under the project will be set as non-default.
        """
        
        kwargs = {}
        kwargs["action"] = "SetDefaultAlarmPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetDefaultAlarmPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncPrometheusTemp(
            self,
            request: models.SyncPrometheusTempRequest,
            opts: Dict = None,
    ) -> models.SyncPrometheusTempResponse:
        """
        This API is used to sync a template to an instance or cluster. It takes effect for v2 instances.
        """
        
        kwargs = {}
        kwargs["action"] = "SyncPrometheusTemp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncPrometheusTempResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminatePrometheusInstances(
            self,
            request: models.TerminatePrometheusInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminatePrometheusInstancesResponse:
        """
        This API is used to terminate a pay-as-you-go Prometheus instance.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminatePrometheusInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminatePrometheusInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindingAllPolicyObject(
            self,
            request: models.UnBindingAllPolicyObjectRequest,
            opts: Dict = None,
    ) -> models.UnBindingAllPolicyObjectResponse:
        """
        This API is used to delete all bound objects.
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindingAllPolicyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindingAllPolicyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnBindingPolicyObject(
            self,
            request: models.UnBindingPolicyObjectRequest,
            opts: Dict = None,
    ) -> models.UnBindingPolicyObjectResponse:
        """
        This API is used to delete an object that is bound to a policy.
        """
        
        kwargs = {}
        kwargs["action"] = "UnBindingPolicyObject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnBindingPolicyObjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindPrometheusManagedGrafana(
            self,
            request: models.UnbindPrometheusManagedGrafanaRequest,
            opts: Dict = None,
    ) -> models.UnbindPrometheusManagedGrafanaResponse:
        """
        This API is used to unbind a Grafana instance from an instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindPrometheusManagedGrafana"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindPrometheusManagedGrafanaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallGrafanaDashboard(
            self,
            request: models.UninstallGrafanaDashboardRequest,
            opts: Dict = None,
    ) -> models.UninstallGrafanaDashboardResponse:
        """
        This API is used to delete a Grafana dashboard.
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallGrafanaDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallGrafanaDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallGrafanaPlugins(
            self,
            request: models.UninstallGrafanaPluginsRequest,
            opts: Dict = None,
    ) -> models.UninstallGrafanaPluginsResponse:
        """
        This API is used to delete installed plugins.
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallGrafanaPlugins"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallGrafanaPluginsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlertRule(
            self,
            request: models.UpdateAlertRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateAlertRuleResponse:
        """
        This API is used to update a Prometheus alerting rule.

        Note that alert object and alert message are special fields of Prometheus Rule Annotations, which need to be passed in through `annotations` and correspond to `summary` and `description` keys respectively. For more information, see [Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/).
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlertRuleState(
            self,
            request: models.UpdateAlertRuleStateRequest,
            opts: Dict = None,
    ) -> models.UpdateAlertRuleStateResponse:
        """
        This API is used to update the status of a Prometheus alerting rule.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlertRuleState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAlertRuleStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDNSConfig(
            self,
            request: models.UpdateDNSConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateDNSConfigResponse:
        """
        This API is used to update the Grafana DNS configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDNSConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDNSConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateExporterIntegration(
            self,
            request: models.UpdateExporterIntegrationRequest,
            opts: Dict = None,
    ) -> models.UpdateExporterIntegrationResponse:
        """
        This API is used to update the exporter integration configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateExporterIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateExporterIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaConfig(
            self,
            request: models.UpdateGrafanaConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaConfigResponse:
        """
        This API is used to update the Grafana configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaEnvironments(
            self,
            request: models.UpdateGrafanaEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaEnvironmentsResponse:
        """
        This API is used to update Grafana environment variables.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaIntegration(
            self,
            request: models.UpdateGrafanaIntegrationRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaIntegrationResponse:
        """
        This API is used to update the Grafana integration configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaIntegration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaIntegrationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaNotificationChannel(
            self,
            request: models.UpdateGrafanaNotificationChannelRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaNotificationChannelResponse:
        """
        This API is used to update the Grafana notification channel.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaNotificationChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaNotificationChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateGrafanaWhiteList(
            self,
            request: models.UpdateGrafanaWhiteListRequest,
            opts: Dict = None,
    ) -> models.UpdateGrafanaWhiteListResponse:
        """
        This API is used to update the Grafana allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateGrafanaWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateGrafanaWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusAgentStatus(
            self,
            request: models.UpdatePrometheusAgentStatusRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusAgentStatusResponse:
        """
        This API is used to update the status of a Prometheus CVM agent.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusAgentStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusAgentStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusAlertGroup(
            self,
            request: models.UpdatePrometheusAlertGroupRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusAlertGroupResponse:
        """
        This API is used to update Prometheus alert rule groups.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusAlertGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusAlertGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusAlertGroupState(
            self,
            request: models.UpdatePrometheusAlertGroupStateRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusAlertGroupStateResponse:
        """
        This API is used to batch update the status of alarm groups and set all rules grouped in them to the target status.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusAlertGroupState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusAlertGroupStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePrometheusScrapeJob(
            self,
            request: models.UpdatePrometheusScrapeJobRequest,
            opts: Dict = None,
    ) -> models.UpdatePrometheusScrapeJobResponse:
        """
        This API is used to update a Prometheus scrape task.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePrometheusScrapeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePrometheusScrapeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRecordingRule(
            self,
            request: models.UpdateRecordingRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateRecordingRuleResponse:
        """
        This API is used to update a Prometheus recording rule.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRecordingRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRecordingRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSSOAccount(
            self,
            request: models.UpdateSSOAccountRequest,
            opts: Dict = None,
    ) -> models.UpdateSSOAccountResponse:
        """
        This API is used to update the remarks and permission information of an authorized account in an overwriting manner.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSSOAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSSOAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeGrafanaDashboard(
            self,
            request: models.UpgradeGrafanaDashboardRequest,
            opts: Dict = None,
    ) -> models.UpgradeGrafanaDashboardResponse:
        """
        This API is used to update a Grafana dashboard.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeGrafanaDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeGrafanaDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeGrafanaInstance(
            self,
            request: models.UpgradeGrafanaInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeGrafanaInstanceResponse:
        """
        This API is used to upgrade a Grafana instance.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeGrafanaInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeGrafanaInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)