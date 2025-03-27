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
from tencentcloud.cdc.v20201214 import models


class CdcClient(AbstractClient):
    _apiVersion = '2020-12-14'
    _endpoint = 'cdc.intl.tencentcloudapi.com'
    _service = 'cdc'


    def CreateDedicatedCluster(self, request):
        """This API is used to create a CDC.

        :param request: Request instance for CreateDedicatedCluster.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDedicatedClusterOrder(self, request):
        """This API is used to create a CDC order.

        :param request: Request instance for CreateDedicatedClusterOrder.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterOrderRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedClusterOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSite(self, request):
        """This API is used to create a site.

        :param request: Request instance for CreateSite.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateSiteRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateSiteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSite", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSiteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDedicatedClusters(self, request):
        """This API is used to delete a CDC.

        :param request: Request instance for DeleteDedicatedClusters.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClustersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDedicatedClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDedicatedClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSites(self, request):
        """This API is used to delete a site.

        :param request: Request instance for DeleteSites.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DeleteSitesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DeleteSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSites", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSitesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterCosCapacity(self, request):
        """This API is used to query the Cloud Object Storage (COS) capacity of the CDC.

        :param request: Request instance for DescribeDedicatedClusterCosCapacity.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCosCapacityRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCosCapacityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterCosCapacity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterCosCapacityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterHostStatistics(self, request):
        """This API is used to query the statistic information of the host in the CDC.

        :param request: Request instance for DescribeDedicatedClusterHostStatistics.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostStatisticsRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterHostStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterHostStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterHosts(self, request):
        """This API is used to query host information of the CDC

        :param request: Request instance for DescribeDedicatedClusterHosts.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostsRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterHosts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterInstanceTypes(self, request):
        """This API is used to query instance types supported by the CDC.

        :param request: Request instance for DescribeDedicatedClusterInstanceTypes.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterInstanceTypesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterOrders(self, request):
        """This API is used to query the list of CDC orders.

        :param request: Request instance for DescribeDedicatedClusterOrders.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOrdersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterOrders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterOrdersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterOverview(self, request):
        """This API is used to query the overview of the CDC

        :param request: Request instance for DescribeDedicatedClusterOverview.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOverviewRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusterTypes(self, request):
        """This API is used to query the configuration list of the CDC.

        :param request: Request instance for DescribeDedicatedClusterTypes.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterTypesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClusterTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedClusters(self, request):
        """This API is used to query the CDC list.

        :param request: Request instance for DescribeDedicatedClusters.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClustersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDedicatedSupportedZones(self, request):
        """This API is used to query the list of AZs supported by the CDC.

        :param request: Request instance for DescribeDedicatedSupportedZones.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedSupportedZonesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedSupportedZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedSupportedZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedSupportedZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSites(self, request):
        """This API is used to query the site list.

        :param request: Request instance for DescribeSites.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSites", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSitesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSitesDetail(self, request):
        """This API is used to query site details.

        :param request: Request instance for DescribeSitesDetail.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesDetailRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSitesDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSitesDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDedicatedClusterInfo(self, request):
        """This API is used to modify the CDC information.

        :param request: Request instance for ModifyDedicatedClusterInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifyDedicatedClusterInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifyDedicatedClusterInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDedicatedClusterInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDedicatedClusterInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOrderStatus(self, request):
        """This API is used to modify the status of large and small orders.

        :param request: Request instance for ModifyOrderStatus.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifyOrderStatusRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifyOrderStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrderStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOrderStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySiteDeviceInfo(self, request):
        """This API is used to modify the information about devices in the equipment room.

        :param request: Request instance for ModifySiteDeviceInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifySiteDeviceInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifySiteDeviceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySiteDeviceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySiteDeviceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySiteInfo(self, request):
        """This API is used to modify the equipment room information.

        :param request: Request instance for ModifySiteInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifySiteInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifySiteInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySiteInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySiteInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))