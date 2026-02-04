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
        This API is a general API used to obtain metric data. Users submit request parameters as needed and receive the corresponding metric data.
        The API call frequency is limited to 20 requests per second and 1200 requests per minute. The number of data points per request is limited to 1440.
        **Usage of the General Interface for Fetching Metric Data**
        DescribeGeneralMetricData is a general interface for querying metric data, supporting flexible data retrieval. The query method of this interface is similar to using the following SQL statement:
        SELECT {Metrics} FROM {ViewName} WHERE {Filters} GROUP BY {GroupBy}.
        1. View (ViewName)
        Determines the data domain you want to query.
        Examples: service_metric (Service Monitoring View), db_metric (Database View), etc. For views supported by APM, please refer to [Metric Views](https://www.tencentcloud.com/document/product/248/68462?has_map=1&lang=en&pg=)
        2. Metrics (Metrics)
        Used to specify one or more metric items to be included in the returned results.
        Examples: request_count (Total Requests), duration_avg (Average Latency), error_rate (Error Rate). For metrics supported by APM, please refer to the [APM Metric Protocol Standard](https://www.tencentcloud.com/document/product/248/68462?has_map=1&lang=en&pg=).
        3. Filters (Filters)
        Supports one or more filtering conditions in the form of Key-Value pairs.
        Example: Querying only a specific service: service.name = "order-service". Common dimensions and specific dimensions supported by each ViewName can be used as keys in filtering conditions. For more details, please refer to the [APM Metric Protocol Standard](https://www.tencentcloud.com/document/product/248/68462?has_map=1&lang=en&pg=).
        4. Aggregation (GroupBy)
        Supports one or more aggregation dimensions, equivalent to the GROUP BY clause in SQL.
        Example: Grouping by the interface name operation to view the performance of each interface. Common dimensions and specific dimensions supported by each ViewName can be used as aggregation dimensions. For more details, please refer to the [APM Metric Protocol Standard](https://www.tencentcloud.com/document/product/248/68462?has_map=1&lang=en&pg=).
        5. Granularity (Period)
        This parameter determines whether the data needs to be aggregated by time slices.
            - Period = 1 (Time Series Mode): The returned results are aggregated by time slices. The multiple values contained in the TimeSerial and DataSerial correspond one-to-one, representing the aggregation results for specific time slices. Time Series Mode is primarily used for displaying time trend charts.
            - Period = 0 (Summary Statistics Mode): In the returned results, the DataSerial contains only a single value, representing the summarized data for the entire time range.
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