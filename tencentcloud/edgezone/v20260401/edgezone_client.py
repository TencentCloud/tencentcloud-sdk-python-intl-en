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
from tencentcloud.edgezone.v20260401 import models


class EdgezoneClient(AbstractClient):
    _apiVersion = '2026-04-01'
    _endpoint = 'edgezone.intl.tencentcloudapi.com'
    _service = 'edgezone'


    def ApplyPublicIps(self, request):
        r"""This API is used to submit a request for multiple IP addresses from the static IP pool to specify a public network instance (random allocation). Need to check user quota before applying.
        This API is applicable only to public network instances with `RouteMode=static`. Calling this API for BGP/OSPF instances will return an error.

        :param request: Request instance for ApplyPublicIps.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ApplyPublicIpsRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ApplyPublicIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyPublicIps", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyPublicIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstances(self, request):
        r"""This API is used to create a physical machine instance. The system automatically allocates physical machine resources and completes installation. If the user is not in the current availability zone, the system automatically enables billing. It supports concurrent allocation of physical machine resources and async execution of network assignment and installation tasks.

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateNetworkInstance(self, request):
        r"""Create a private network instance. A user can only create one private network instance in an availability zone. The subnet range is collectively determined by both parameters: Network (network number) and Mask (bit number of the mask). Network must be a valid network address from one of the three RFC 1918 private address ranges: 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16, and all host bits must be 0 (meaning the combination of Network and Mask cannot have any host bits set, such as 10.0.0.1/24 is illegal, use 10.0.0.0/24 instead). The maximum Mask is unified as 28, and the minimum is determined by the address range it belongs to: 10.x.x.x allows 8–28, 172.16.x.x allows 12–28, and 192.168.x.x allows 16–28.

        :param request: Request instance for CreatePrivateNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.CreatePrivateNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.CreatePrivateNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublicNetworkInstance(self, request):
        r"""The user inputs the availability zone ID, public network instance name, network line, and routing mode to create a public network instance. A user can only create one public network instance in an availability zone.
        Public network instances in **static** routing mode require users to proactively apply for and release public IP addresses.
        Public network instances with routing mode set to **OSPF, BGP** automatically allocate public IP ranges when creating and auto release public IP ranges upon termination.

        :param request: Request instance for CreatePublicNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.CreatePublicNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.CreatePublicNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublicNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublicNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateNetworkInstance(self, request):
        r"""Delete a private network instance

        :param request: Request instance for DeletePrivateNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DeletePrivateNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DeletePrivateNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePublicNetworkInstance(self, request):
        r"""Modify public network instance info

        :param request: Request instance for DeletePublicNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DeletePublicNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DeletePublicNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePublicNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePublicNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTypes(self, request):
        r"""This API is used to query the model quota list under the account by availability zone dimensionality based on AppId. If a Zone is input, it returns the model quota under the designated availability zone. If not, it returns the model quota of all AZs under the account.

        :param request: Request instance for DescribeInstanceTypes.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstanceTypesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        r"""This API is used to query physical machine instance list, support by instance ID, instance name, availability zone, instance status with conditional filtering, and support paging query.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNetworkInstances(self, request):
        r"""Query private network instances, support through parameters such as private network instance ID, instance name, and availability zone id.

        :param request: Request instance for DescribePrivateNetworkInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribePrivateNetworkInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribePrivateNetworkInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNetworkInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNetworkInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicIps(self, request):
        r"""Query the public network Ip information of the user. For public network instances with routing mode set to Static, return all applied public network Ip information. For public network instances with routing mode set to Ospf and Bgp, return Ip range information directly.

        :param request: Request instance for DescribePublicIps.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicIpsRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicIps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicNetworkInstances(self, request):
        r"""Query public network instance list, support conditional filtering by instance ID, instance name, availability zone, and support paging query.

        :param request: Request instance for DescribePublicNetworkInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicNetworkInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribePublicNetworkInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicNetworkInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicNetworkInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZoneData(self, request):
        r"""Query statistics by metric name. Data is aggregated at 1-minute intervals.

        :param request: Request instance for DescribeZoneData.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeZoneDataRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeZoneDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZoneData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZoneDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        r"""Cross-regional aggregate query returns the AZ list for the specified AppId in ALL configured regions. The local region directly performs a database query, while remote regions send HTTP requests to each region's DescribeAppZones API and merge the results.

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceAttribute(self, request):
        r"""This API is used to modify the attributes of a physical machine instance, supporting modification of the instance name and update of the public IP address (IPv4/IPv6). At least one of InstanceName and NewPublicIp must be input.

        :param request: Request instance for ModifyInstanceAttribute.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ModifyInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ModifyInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateNetworkInstance(self, request):
        r"""Modify private network instance info

        :param request: Request instance for ModifyPrivateNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ModifyPrivateNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ModifyPrivateNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublicNetworkInstance(self, request):
        r"""Modify public network instance info

        :param request: Request instance for ModifyPublicNetworkInstance.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ModifyPublicNetworkInstanceRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ModifyPublicNetworkInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublicNetworkInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublicNetworkInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleasePublicIp(self, request):
        r"""Batch release IPv4 addresses assigned to STATIC public network instances but not bound to physical servers
        This API is applicable only to STATIC mode instances. The CIDR of BGP/OSPF instances is automatically returned during deletion with no need to manually release single IP addresses.

        :param request: Request instance for ReleasePublicIp.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.ReleasePublicIpRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.ReleasePublicIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleasePublicIp", params, headers=headers)
            response = json.loads(body)
            model = models.ReleasePublicIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstances(self, request):
        r"""This API is used to terminate a physical machine instance and free up resources. It synchronously releases network resources (IP recycling) and updates status to terminating, while performing disk cleanup asynchronously in the background. It supports partially successful operations.

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.edgezone.v20260401.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.edgezone.v20260401.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))