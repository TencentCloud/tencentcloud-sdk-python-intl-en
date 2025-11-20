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
from tencentcloud.dc.v20180410 import models
from typing import Dict


class DcClient(AbstractClient):
    _apiVersion = '2018-04-10'
    _endpoint = 'dc.intl.tencentcloudapi.com'
    _service = 'dc'

    async def AcceptDirectConnectTunnel(
            self,
            request: models.AcceptDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.AcceptDirectConnectTunnelResponse:
        """
        This API is used to accept an application for a dedicated tunnel.
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ApplyInternetAddress(
            self,
            request: models.ApplyInternetAddressRequest,
            opts: Dict = None,
    ) -> models.ApplyInternetAddressResponse:
        """
        This API is used to apply for an internet tunnel’s CIDR block.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnect(
            self,
            request: models.CreateDirectConnectRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectResponse:
        """
        This API is used to apply for a connection.
        When calling this API, please note that:
        You need to complete identity verification for your account; otherwise, you cannot apply for a connection;
        If there is any connection in arrears under your account, you cannot apply for more connections.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnectTunnel(
            self,
            request: models.CreateDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectTunnelResponse:
        """
        This API is used to create a dedicated tunnel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnect(
            self,
            request: models.DeleteDirectConnectRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectResponse:
        """
        This API is used to delete a connection.
        Only connected connections can be deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnectTunnel(
            self,
            request: models.DeleteDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectTunnelResponse:
        """
        This API is used to delete a dedicated tunnel.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessPoints(
            self,
            request: models.DescribeAccessPointsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessPointsResponse:
        """
        This API is used to query connection access points.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessPoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessPointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectTunnels(
            self,
            request: models.DescribeDirectConnectTunnelsRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectTunnelsResponse:
        """
        This API is used to query the list of dedicated tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectTunnels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectTunnelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnects(
            self,
            request: models.DescribeDirectConnectsRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectsResponse:
        """
        This API is used to query the list of connections.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternetAddress(
            self,
            request: models.DescribeInternetAddressRequest,
            opts: Dict = None,
    ) -> models.DescribeInternetAddressResponse:
        """
        This API is used to obtain the public IP address of an internet tunnel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternetAddressQuota(
            self,
            request: models.DescribeInternetAddressQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeInternetAddressQuotaResponse:
        """
        This API is used to obtain the public IP quota of internet tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternetAddressQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternetAddressQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInternetAddressStatistics(
            self,
            request: models.DescribeInternetAddressStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeInternetAddressStatisticsResponse:
        """
        This API is used to obtain the public IP address assignment statistics of internet tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInternetAddressStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInternetAddressStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableInternetAddress(
            self,
            request: models.DisableInternetAddressRequest,
            opts: Dict = None,
    ) -> models.DisableInternetAddressResponse:
        """
        This API is used to disable a public IP address of internet tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableInternetAddress(
            self,
            request: models.EnableInternetAddressRequest,
            opts: Dict = None,
    ) -> models.EnableInternetAddressResponse:
        """
        This API is used to enable a public IP address for internet tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDirectConnectAttribute(
            self,
            request: models.ModifyDirectConnectAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDirectConnectAttributeResponse:
        """
        This API is used to modify connection attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDirectConnectAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDirectConnectAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDirectConnectTunnelAttribute(
            self,
            request: models.ModifyDirectConnectTunnelAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDirectConnectTunnelAttributeResponse:
        """
        This API is used to modify the dedicated tunnel attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDirectConnectTunnelAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDirectConnectTunnelAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectDirectConnectTunnel(
            self,
            request: models.RejectDirectConnectTunnelRequest,
            opts: Dict = None,
    ) -> models.RejectDirectConnectTunnelResponse:
        """
        This API is used to reject an application for a dedicated tunnel.
        """
        
        kwargs = {}
        kwargs["action"] = "RejectDirectConnectTunnel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectDirectConnectTunnelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseInternetAddress(
            self,
            request: models.ReleaseInternetAddressRequest,
            opts: Dict = None,
    ) -> models.ReleaseInternetAddressResponse:
        """
        This API is used to release an IP address of internet tunnels.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseInternetAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseInternetAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)