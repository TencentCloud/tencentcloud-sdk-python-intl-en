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
from tencentcloud.apm.v20210622 import models


class ApmClient(AbstractClient):
    _apiVersion = '2021-06-22'
    _endpoint = 'apm.intl.tencentcloudapi.com'
    _service = 'apm'


    def CreateApmInstance(self, request):
        r"""This API is used to create a business purchase in the APM business system.

        :param request: Request instance for CreateApmInstance.
        :type request: :class:`tencentcloud.apm.v20210622.models.CreateApmInstanceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.CreateApmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApmPrometheusRule(self, request):
        r"""This API is used to create metric match rules between apm Business System and Prometheus Instance.

        :param request: Request instance for CreateApmPrometheusRule.
        :type request: :class:`tencentcloud.apm.v20210622.models.CreateApmPrometheusRuleRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.CreateApmPrometheusRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApmPrometheusRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApmPrometheusRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApmSampleConfig(self, request):
        r"""Create sampling configurations

        :param request: Request instance for CreateApmSampleConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.CreateApmSampleConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.CreateApmSampleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApmSampleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApmSampleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProfileTask(self, request):
        r"""This API is used to create an event task.

        :param request: Request instance for CreateProfileTask.
        :type request: :class:`tencentcloud.apm.v20210622.models.CreateProfileTaskRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.CreateProfileTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProfileTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProfileTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApmSampleConfig(self, request):
        r"""Delete sampling configurations

        :param request: Request instance for DeleteApmSampleConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.DeleteApmSampleConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DeleteApmSampleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApmSampleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApmSampleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmAgent(self, request):
        r"""Obtaining APM Access Point.

        :param request: Request instance for DescribeApmAgent.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmAgentRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmAllVulCount(self, request):
        r"""Query all vulnerability information of the user

        :param request: Request instance for DescribeApmAllVulCount.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmAllVulCountRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmAllVulCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmAllVulCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmAllVulCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmApplicationConfig(self, request):
        r"""This API is used to query application configuration.

        :param request: Request instance for DescribeApmApplicationConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmApplicationConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmAssociation(self, request):
        r"""This API is used to query the relationship between apm Business System and other product.

        :param request: Request instance for DescribeApmAssociation.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmAssociationRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmAssociationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmAssociation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmAssociationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmInstances(self, request):
        r"""This API is used to obtain the list of APM business systems.

        :param request: Request instance for DescribeApmInstances.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmInstancesRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmPrometheusRule(self, request):
        r"""This API is used to query the match rule for metrics between apm Business System and Prometheus Instance.

        :param request: Request instance for DescribeApmPrometheusRule.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmPrometheusRuleRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmPrometheusRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmPrometheusRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmPrometheusRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmSQLInjectionDetail(self, request):
        r"""Query SQL injection details

        :param request: Request instance for DescribeApmSQLInjectionDetail.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmSQLInjectionDetailRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmSQLInjectionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmSQLInjectionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmSQLInjectionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmSampleConfig(self, request):
        r"""Query sampling configuration

        :param request: Request instance for DescribeApmSampleConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmSampleConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmSampleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmSampleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmSampleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmServiceMetric(self, request):
        r"""This API is used to obtain the list of APM application metrics.

        :param request: Request instance for DescribeApmServiceMetric.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmServiceMetricRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmServiceMetricResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmServiceMetric", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmServiceMetricResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmVulnerabilityCount(self, request):
        r"""Query vulnerability metrics

        :param request: Request instance for DescribeApmVulnerabilityCount.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmVulnerabilityCountRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmVulnerabilityCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmVulnerabilityCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmVulnerabilityCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApmVulnerabilityDetail(self, request):
        r"""Query vulnerability details.

        :param request: Request instance for DescribeApmVulnerabilityDetail.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeApmVulnerabilityDetailRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeApmVulnerabilityDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApmVulnerabilityDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApmVulnerabilityDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralApmApplicationConfig(self, request):
        r"""This API is used to query the application configuration information.

        :param request: Request instance for DescribeGeneralApmApplicationConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralApmApplicationConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralApmApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralApmApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralApmApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralMetricData(self, request):
        r"""General interface to obtain metric data. Submit request parameters as needed and receive the corresponding metric data.
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

        :param request: Request instance for DescribeGeneralMetricData.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralMetricDataRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralMetricDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralMetricData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralMetricDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralOTSpanList(self, request):
        r"""General Query OpenTelemetry Call Chain List.

        :param request: Request instance for DescribeGeneralOTSpanList.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralOTSpanListRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralOTSpanListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralOTSpanList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralOTSpanListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralSpanList(self, request):
        r"""General Query Call Chain List.

        :param request: Request instance for DescribeGeneralSpanList.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralSpanListRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeGeneralSpanListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralSpanList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralSpanListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMetricRecords(self, request):
        r"""This API is used to query metric list. To query metrics, it is recommended to use the DescribeGeneralMetricData API.

        :param request: Request instance for DescribeMetricRecords.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeMetricRecordsRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeMetricRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMetricRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMetricRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOPRAllVulCount(self, request):
        r"""Query all vulnerability information of the user

        :param request: Request instance for DescribeOPRAllVulCount.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeOPRAllVulCountRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeOPRAllVulCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOPRAllVulCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOPRAllVulCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceOverview(self, request):
        r"""This API is used to pull application overview data.

        :param request: Request instance for DescribeServiceOverview.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeServiceOverviewRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeServiceOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagValues(self, request):
        r"""This API is used to query dimensional data by dimension name and filter condition.

        :param request: Request instance for DescribeTagValues.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeTagValuesRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeTagValuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagValues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagValuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopologyNew(self, request):
        r"""This API is used to query the service topology diagram according to the application name.

        :param request: Request instance for DescribeTopologyNew.
        :type request: :class:`tencentcloud.apm.v20210622.models.DescribeTopologyNewRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.DescribeTopologyNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopologyNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopologyNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApmApplicationConfig(self, request):
        r"""Modify application configurations

        :param request: Request instance for ModifyApmApplicationConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyApmApplicationConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyApmApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApmApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApmApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApmAssociation(self, request):
        r"""This API is used to modify the relationship between the apm Business System and other products, including deletion.

        :param request: Request instance for ModifyApmAssociation.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyApmAssociationRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyApmAssociationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApmAssociation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApmAssociationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApmInstance(self, request):
        r"""This API is used to modify the APM business system.

        :param request: Request instance for ModifyApmInstance.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyApmInstanceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyApmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApmPrometheusRule(self, request):
        r"""This API is used to modify metric match rules between apm Business System and Prometheus Instance.

        :param request: Request instance for ModifyApmPrometheusRule.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyApmPrometheusRuleRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyApmPrometheusRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApmPrometheusRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApmPrometheusRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApmSampleConfig(self, request):
        r"""Modify sampling configurations

        :param request: Request instance for ModifyApmSampleConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyApmSampleConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyApmSampleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApmSampleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApmSampleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApmService(self, request):
        r"""This API is used to edit information about applications of APM.

        :param request: Request instance for ModifyApmService.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyApmServiceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyApmServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApmService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApmServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGeneralApmApplicationConfig(self, request):
        r"""OpenAPI available for external use. Customers can flexibly specify the fields to be modified, and then add the list of services to be modified.

        :param request: Request instance for ModifyGeneralApmApplicationConfig.
        :type request: :class:`tencentcloud.apm.v20210622.models.ModifyGeneralApmApplicationConfigRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.ModifyGeneralApmApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGeneralApmApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGeneralApmApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateApmInstance(self, request):
        r"""Termination of APM business system.

        :param request: Request instance for TerminateApmInstance.
        :type request: :class:`tencentcloud.apm.v20210622.models.TerminateApmInstanceRequest`
        :rtype: :class:`tencentcloud.apm.v20210622.models.TerminateApmInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateApmInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateApmInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))