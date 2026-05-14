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
from tencentcloud.apm.v20210622 import models
from typing import Dict


class ApmClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'apm.intl.tencentcloudapi.com'
    _service = 'apm'

    async def CreateApmInstance(
            self,
            request: models.CreateApmInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateApmInstanceResponse:
        """
        This API is used to create a business purchase in the APM business system.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApmInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApmInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApmPrometheusRule(
            self,
            request: models.CreateApmPrometheusRuleRequest,
            opts: Dict = None,
    ) -> models.CreateApmPrometheusRuleResponse:
        """
        This API is used to create metric match rules between apm Business System and Prometheus Instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApmPrometheusRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApmPrometheusRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApmSampleConfig(
            self,
            request: models.CreateApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.CreateApmSampleConfigResponse:
        """
        Create sampling configurations
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProfileTask(
            self,
            request: models.CreateProfileTaskRequest,
            opts: Dict = None,
    ) -> models.CreateProfileTaskResponse:
        """
        This API is used to create an event task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProfileTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProfileTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApmSampleConfig(
            self,
            request: models.DeleteApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteApmSampleConfigResponse:
        """
        Delete sampling configurations
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmAgent(
            self,
            request: models.DescribeApmAgentRequest,
            opts: Dict = None,
    ) -> models.DescribeApmAgentResponse:
        """
        Obtaining APM Access Point.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmAllVulCount(
            self,
            request: models.DescribeApmAllVulCountRequest,
            opts: Dict = None,
    ) -> models.DescribeApmAllVulCountResponse:
        """
        Query all vulnerability information of the user
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmAllVulCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmAllVulCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmApplicationConfig(
            self,
            request: models.DescribeApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeApmApplicationConfigResponse:
        """
        This API is used to query application configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmAssociation(
            self,
            request: models.DescribeApmAssociationRequest,
            opts: Dict = None,
    ) -> models.DescribeApmAssociationResponse:
        """
        This API is used to query the relationship between apm Business System and other product.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmAssociation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmAssociationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmInstances(
            self,
            request: models.DescribeApmInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeApmInstancesResponse:
        """
        This API is used to obtain the list of APM business systems.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmPrometheusRule(
            self,
            request: models.DescribeApmPrometheusRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeApmPrometheusRuleResponse:
        """
        This API is used to query the match rule for metrics between apm Business System and Prometheus Instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmPrometheusRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmPrometheusRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmSQLInjectionDetail(
            self,
            request: models.DescribeApmSQLInjectionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeApmSQLInjectionDetailResponse:
        """
        Query SQL injection details
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmSQLInjectionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmSQLInjectionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmSampleConfig(
            self,
            request: models.DescribeApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeApmSampleConfigResponse:
        """
        Query sampling configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmServiceMetric(
            self,
            request: models.DescribeApmServiceMetricRequest,
            opts: Dict = None,
    ) -> models.DescribeApmServiceMetricResponse:
        """
        This API is used to obtain the list of APM application metrics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmServiceMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmServiceMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmVulnerabilityCount(
            self,
            request: models.DescribeApmVulnerabilityCountRequest,
            opts: Dict = None,
    ) -> models.DescribeApmVulnerabilityCountResponse:
        """
        Query vulnerability metrics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmVulnerabilityCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmVulnerabilityCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApmVulnerabilityDetail(
            self,
            request: models.DescribeApmVulnerabilityDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeApmVulnerabilityDetailResponse:
        """
        Query vulnerability details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApmVulnerabilityDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApmVulnerabilityDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralApmApplicationConfig(
            self,
            request: models.DescribeGeneralApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralApmApplicationConfigResponse:
        """
        This API is used to query the application configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralMetricData(
            self,
            request: models.DescribeGeneralMetricDataRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralMetricDataResponse:
        """
        General interface to obtain metric data. Submit request parameters as needed and receive the corresponding metric data.
        API call frequency limit: 20 requests/second, 1,200 requests/minute. Data point limit per single request: up to 1,440 data points.

        General interface to obtain metric data usage: This API is used to query metric data flexibly. The query method of this API is similar to using the following SQL statement: SELECT {Metrics} FROM {ViewName} WHERE {Filters} GROUP BY {GroupBy}. Before initiating request, please confirm the following key parameters:
        1. View (ViewName)
        Determine the domain of the queried data.
        For example: service_metric (service monitoring view), db_metric (database view). For views supported by APM, see metrics view (https://www.tencentcloud.com/document/product/248/101681?from_cn_redirect=1#069b06a9-2593-49db-b694-dea4200f3b19).

        2. Metrics
        Used to specify one or more metric items in the returned result.
        For example: request_count (request count), duration_avg (avg duration), error_rate (error rate). For supported metrics about APM, see [APM Protocol Standards](https://www.tencentcloud.com/document/product/248/101681?from_cn_redirect=1). Each view (ViewName) supports an exclusive metric set.
        3. Filters
        Support filter criteria in the form of one or multiple Key-Value pairs.
        For example: Only query a certain specific service with service.name = "order-service". Common dimensional and each view (ViewName) support exclusive dimensions, which can be used as keys in filter conditions. For details, refer to the APM metrics protocol standard (https://www.tencentcloud.com/document/product/248/101681?from_cn_redirect=1).

        4. GroupBy (aggregation)
        Support one or more aggregate dimensions, equivalent to SQL GROUP BY.
        For example: Group by API name operation to view the performance of each API. Common dimensional and each view (ViewName) support exclusive dimensional, which can be used as aggregation dimension. For details, see [APM protocol standards](https://www.tencentcloud.com/document/product/248/101681?from_cn_redirect=1).
        5. Granularity (Period)
        This parameter determines whether time slice aggregation is required.
        -Period = 1: Time series mode: In the returned result, aggregation is performed by time slice. The time series (TimeSerial) and data sequence (DataSerial) have a one-to-one correspondence, representing aggregation results for specific time slices. Time series mode is mainly used to show time trend charts.
        -Period = 0: Summarize mode. In the returned result, the data sequence (DataSerial) only contains a unique value, representing the aggregated data for the entire time interval.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralMetricData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralMetricDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralOTSpanList(
            self,
            request: models.DescribeGeneralOTSpanListRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralOTSpanListResponse:
        """
        General Query OpenTelemetry Call Chain List.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralOTSpanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralOTSpanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGeneralSpanList(
            self,
            request: models.DescribeGeneralSpanListRequest,
            opts: Dict = None,
    ) -> models.DescribeGeneralSpanListResponse:
        """
        General Query Call Chain List.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGeneralSpanList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGeneralSpanListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMetricRecords(
            self,
            request: models.DescribeMetricRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeMetricRecordsResponse:
        """
        This API is used to query metric list. To query metrics, it is recommended to use the DescribeGeneralMetricData API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMetricRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMetricRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOPRAllVulCount(
            self,
            request: models.DescribeOPRAllVulCountRequest,
            opts: Dict = None,
    ) -> models.DescribeOPRAllVulCountResponse:
        """
        Query all vulnerability information of the user
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOPRAllVulCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOPRAllVulCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceOverview(
            self,
            request: models.DescribeServiceOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceOverviewResponse:
        """
        This API is used to pull application overview data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagValues(
            self,
            request: models.DescribeTagValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagValuesResponse:
        """
        This API is used to query dimensional data by dimension name and filter condition.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopologyNew(
            self,
            request: models.DescribeTopologyNewRequest,
            opts: Dict = None,
    ) -> models.DescribeTopologyNewResponse:
        """
        This API is used to query the service topology diagram according to the application name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopologyNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopologyNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmApplicationConfig(
            self,
            request: models.ModifyApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyApmApplicationConfigResponse:
        """
        Modify application configurations
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmAssociation(
            self,
            request: models.ModifyApmAssociationRequest,
            opts: Dict = None,
    ) -> models.ModifyApmAssociationResponse:
        """
        This API is used to modify the relationship between the apm Business System and other products, including deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmAssociation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmAssociationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmInstance(
            self,
            request: models.ModifyApmInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyApmInstanceResponse:
        """
        This API is used to modify the APM business system.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmPrometheusRule(
            self,
            request: models.ModifyApmPrometheusRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyApmPrometheusRuleResponse:
        """
        This API is used to modify metric match rules between apm Business System and Prometheus Instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmPrometheusRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmPrometheusRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmSampleConfig(
            self,
            request: models.ModifyApmSampleConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyApmSampleConfigResponse:
        """
        Modify sampling configurations
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmSampleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmSampleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApmService(
            self,
            request: models.ModifyApmServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyApmServiceResponse:
        """
        This API is used to edit information about applications of APM.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApmService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApmServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGeneralApmApplicationConfig(
            self,
            request: models.ModifyGeneralApmApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyGeneralApmApplicationConfigResponse:
        """
        OpenAPI available for external use. Customers can flexibly specify the fields to be modified, and then add the list of services to be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGeneralApmApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGeneralApmApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateApmInstance(
            self,
            request: models.TerminateApmInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateApmInstanceResponse:
        """
        Termination of APM business system.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateApmInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateApmInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)