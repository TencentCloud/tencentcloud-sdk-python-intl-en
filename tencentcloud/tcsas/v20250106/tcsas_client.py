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
from tencentcloud.tcsas.v20250106 import models


class TcsasClient(AbstractClient):
    _apiVersion = '2025-01-06'
    _endpoint = 'tcsas.intl.tencentcloudapi.com'
    _service = 'tcsas'


    def DescribeMNGMAUDataDetail(self, request):
        r"""This API is used to retrieve the detailed mini game monthly active user data.

        :param request: Request instance for DescribeMNGMAUDataDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUDataDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUDataDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGMAUDataDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGMAUDataDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGMAULineChart(self, request):
        r"""This API is used to retrieve mini game monthly active user data in a line chart format.

        :param request: Request instance for DescribeMNGMAULineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAULineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAULineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGMAULineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGMAULineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNGMAUMonthlyComparisonMetricCard(self, request):
        r"""This API is used to retrieve MAU comparison data for a mini game between two months.

        :param request: Request instance for DescribeMNGMAUMonthlyComparisonMetricCard.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUMonthlyComparisonMetricCardRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNGMAUMonthlyComparisonMetricCardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNGMAUMonthlyComparisonMetricCard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNGMAUMonthlyComparisonMetricCardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPMAUDataDetail(self, request):
        r"""This API is used to retrieve the detailed mini program monthly active user data.

        :param request: Request instance for DescribeMNPMAUDataDetail.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUDataDetailRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUDataDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPMAUDataDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPMAUDataDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPMAULineChart(self, request):
        r"""This API is used to retrieve mini program monthly active user data in a line chart format.

        :param request: Request instance for DescribeMNPMAULineChart.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAULineChartRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAULineChartResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPMAULineChart", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPMAULineChartResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMNPMAUMetricCard(self, request):
        r"""This API is used to retrieve MAU comparison data for a mini program between two months.

        :param request: Request instance for DescribeMNPMAUMetricCard.
        :type request: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUMetricCardRequest`
        :rtype: :class:`tencentcloud.tcsas.v20250106.models.DescribeMNPMAUMetricCardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMNPMAUMetricCard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMNPMAUMetricCardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))