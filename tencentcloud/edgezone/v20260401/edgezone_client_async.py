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
from tencentcloud.edgezone.v20260401 import models
from typing import Dict


class EdgezoneClient(AbstractClient):
    _apiVersion = '2026-04-01'
    _endpoint = 'edgezone.intl.tencentcloudapi.com'
    _service = 'edgezone'

    async def ApplyPublicIps(
            self,
            request: models.ApplyPublicIpsRequest,
            opts: Dict = None,
    ) -> models.ApplyPublicIpsResponse:
        """
        This API is used to submit a request for multiple IP addresses from the static IP pool to specify a public network instance (random allocation). Need to check user quota before applying.
        This API is applicable only to public network instances with `RouteMode=static`. Calling this API for BGP/OSPF instances will return an error.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyPublicIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyPublicIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        This API is used to create a physical machine instance. The system automatically allocates physical machine resources and completes installation. If the user is not in the current availability zone, the system automatically enables billing. It supports concurrent allocation of physical machine resources and async execution of network assignment and installation tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateNetworkInstance(
            self,
            request: models.CreatePrivateNetworkInstanceRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateNetworkInstanceResponse:
        """
        Create a private network instance. A user can only create one private network instance in an availability zone. The subnet range is collectively determined by both parameters: Network (network number) and Mask (bit number of the mask). Network must be a valid network address from one of the three RFC 1918 private address ranges: 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16, and all host bits must be 0 (meaning the combination of Network and Mask cannot have any host bits set, such as 10.0.0.1/24 is illegal, use 10.0.0.0/24 instead). The maximum Mask is unified as 28, and the minimum is determined by the address range it belongs to: 10.x.x.x allows 8–28, 172.16.x.x allows 12–28, and 192.168.x.x allows 16–28.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateNetworkInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateNetworkInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePublicNetworkInstance(
            self,
            request: models.CreatePublicNetworkInstanceRequest,
            opts: Dict = None,
    ) -> models.CreatePublicNetworkInstanceResponse:
        """
        The user inputs the availability zone ID, public network instance name, network line, and routing mode to create a public network instance. A user can only create one public network instance in an availability zone.
        Public network instances in **static** routing mode require users to proactively apply for and release public IP addresses.
        Public network instances with routing mode set to **OSPF, BGP** automatically allocate public IP ranges when creating and auto release public IP ranges upon termination.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePublicNetworkInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePublicNetworkInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateNetworkInstance(
            self,
            request: models.DeletePrivateNetworkInstanceRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateNetworkInstanceResponse:
        """
        Delete a private network instance
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateNetworkInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateNetworkInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePublicNetworkInstance(
            self,
            request: models.DeletePublicNetworkInstanceRequest,
            opts: Dict = None,
    ) -> models.DeletePublicNetworkInstanceResponse:
        """
        Modify public network instance info
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePublicNetworkInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePublicNetworkInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTypes(
            self,
            request: models.DescribeInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTypesResponse:
        """
        This API is used to query the model quota list under the account by availability zone dimensionality based on AppId. If a Zone is input, it returns the model quota under the designated availability zone. If not, it returns the model quota of all AZs under the account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        This API is used to query physical machine instance list, support by instance ID, instance name, availability zone, instance status with conditional filtering, and support paging query.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateNetworkInstances(
            self,
            request: models.DescribePrivateNetworkInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateNetworkInstancesResponse:
        """
        Query private network instances, support through parameters such as private network instance ID, instance name, and availability zone id.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateNetworkInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateNetworkInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicIps(
            self,
            request: models.DescribePublicIpsRequest,
            opts: Dict = None,
    ) -> models.DescribePublicIpsResponse:
        """
        Query the public network Ip information of the user. For public network instances with routing mode set to Static, return all applied public network Ip information. For public network instances with routing mode set to Ospf and Bgp, return Ip range information directly.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicNetworkInstances(
            self,
            request: models.DescribePublicNetworkInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribePublicNetworkInstancesResponse:
        """
        Query public network instance list, support conditional filtering by instance ID, instance name, availability zone, and support paging query.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicNetworkInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicNetworkInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneData(
            self,
            request: models.DescribeZoneDataRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneDataResponse:
        """
        Query statistics by metric name. Data is aggregated at 1-minute intervals.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        Cross-regional aggregate query returns the AZ list for the specified AppId in ALL configured regions. The local region directly performs a database query, while remote regions send HTTP requests to each region's DescribeAppZones API and merge the results.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceAttribute(
            self,
            request: models.ModifyInstanceAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceAttributeResponse:
        """
        This API is used to modify the attributes of a physical machine instance, supporting modification of the instance name and update of the public IP address (IPv4/IPv6). At least one of InstanceName and NewPublicIp must be input.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateNetworkInstance(
            self,
            request: models.ModifyPrivateNetworkInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateNetworkInstanceResponse:
        """
        Modify private network instance info
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateNetworkInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateNetworkInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPublicNetworkInstance(
            self,
            request: models.ModifyPublicNetworkInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyPublicNetworkInstanceResponse:
        """
        Modify public network instance info
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPublicNetworkInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPublicNetworkInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleasePublicIp(
            self,
            request: models.ReleasePublicIpRequest,
            opts: Dict = None,
    ) -> models.ReleasePublicIpResponse:
        """
        Batch release IPv4 addresses assigned to STATIC public network instances but not bound to physical servers
        This API is applicable only to STATIC mode instances. The CIDR of BGP/OSPF instances is automatically returned during deletion with no need to manually release single IP addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "ReleasePublicIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleasePublicIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstances(
            self,
            request: models.TerminateInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateInstancesResponse:
        """
        This API is used to terminate a physical machine instance and free up resources. It synchronously releases network resources (IP recycling) and updates status to terminating, while performing disk cleanup asynchronously in the background. It supports partially successful operations.
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)