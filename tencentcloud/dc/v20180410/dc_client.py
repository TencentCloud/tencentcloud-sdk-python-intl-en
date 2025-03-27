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
from tencentcloud.dc.v20180410 import models


class DcClient(AbstractClient):
    _apiVersion = '2018-04-10'
    _endpoint = 'dc.intl.tencentcloudapi.com'
    _service = 'dc'


    def AcceptDirectConnectTunnel(self, request):
        """This API is used to accept an application for a dedicated tunnel.

        :param request: Request instance for AcceptDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.AcceptDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.AcceptDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptDirectConnectTunnel", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptDirectConnectTunnelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplyInternetAddress(self, request):
        """This API is used to apply for an internet tunnel’s CIDR block.

        :param request: Request instance for ApplyInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.ApplyInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ApplyInternetAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyInternetAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyInternetAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDirectConnect(self, request):
        """This API is used to apply for a connection.
        When calling this API, please note that:
        You need to complete identity verification for your account; otherwise, you cannot apply for a connection;
        If there is any connection in arrears under your account, you cannot apply for more connections.

        :param request: Request instance for CreateDirectConnect.
        :type request: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDirectConnect", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDirectConnectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDirectConnectTunnel(self, request):
        """This API is used to create a dedicated tunnel.

        :param request: Request instance for CreateDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.CreateDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDirectConnectTunnel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDirectConnectTunnelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDirectConnect(self, request):
        """This API is used to delete a connection.
        Only connected connections can be deleted.

        :param request: Request instance for DeleteDirectConnect.
        :type request: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDirectConnect", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDirectConnectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDirectConnectTunnel(self, request):
        """This API is used to delete a dedicated tunnel.

        :param request: Request instance for DeleteDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DeleteDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDirectConnectTunnel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDirectConnectTunnelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessPoints(self, request):
        """This API is used to query connection access points.

        :param request: Request instance for DescribeAccessPoints.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeAccessPointsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeAccessPointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessPoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessPointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnectTunnels(self, request):
        """This API is used to query the list of dedicated tunnels.

        :param request: Request instance for DescribeDirectConnectTunnels.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectTunnelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnectTunnels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectTunnelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnects(self, request):
        """This API is used to query the list of connections.

        :param request: Request instance for DescribeDirectConnects.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeDirectConnectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInternetAddress(self, request):
        """This API is used to obtain the public IP address of an internet tunnel.

        :param request: Request instance for DescribeInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInternetAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInternetAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInternetAddressQuota(self, request):
        """This API is used to obtain the public IP quota of internet tunnels.

        :param request: Request instance for DescribeInternetAddressQuota.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressQuotaRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInternetAddressQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInternetAddressQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInternetAddressStatistics(self, request):
        """This API is used to obtain the public IP address assignment statistics of internet tunnels.

        :param request: Request instance for DescribeInternetAddressStatistics.
        :type request: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressStatisticsRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DescribeInternetAddressStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInternetAddressStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInternetAddressStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableInternetAddress(self, request):
        """This API is used to disable a public IP address of internet tunnels.

        :param request: Request instance for DisableInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.DisableInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.DisableInternetAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableInternetAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DisableInternetAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableInternetAddress(self, request):
        """This API is used to enable a public IP address for internet tunnels.

        :param request: Request instance for EnableInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.EnableInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.EnableInternetAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableInternetAddress", params, headers=headers)
            response = json.loads(body)
            model = models.EnableInternetAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDirectConnectAttribute(self, request):
        """This API is used to modify connection attributes.

        :param request: Request instance for ModifyDirectConnectAttribute.
        :type request: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectAttributeRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDirectConnectAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDirectConnectAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDirectConnectTunnelAttribute(self, request):
        """This API is used to modify the dedicated tunnel attributes.

        :param request: Request instance for ModifyDirectConnectTunnelAttribute.
        :type request: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelAttributeRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ModifyDirectConnectTunnelAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDirectConnectTunnelAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDirectConnectTunnelAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectDirectConnectTunnel(self, request):
        """This API is used to reject an application for a dedicated tunnel.

        :param request: Request instance for RejectDirectConnectTunnel.
        :type request: :class:`tencentcloud.dc.v20180410.models.RejectDirectConnectTunnelRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.RejectDirectConnectTunnelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectDirectConnectTunnel", params, headers=headers)
            response = json.loads(body)
            model = models.RejectDirectConnectTunnelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseInternetAddress(self, request):
        """This API is used to release an IP address of internet tunnels.

        :param request: Request instance for ReleaseInternetAddress.
        :type request: :class:`tencentcloud.dc.v20180410.models.ReleaseInternetAddressRequest`
        :rtype: :class:`tencentcloud.dc.v20180410.models.ReleaseInternetAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseInternetAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseInternetAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))