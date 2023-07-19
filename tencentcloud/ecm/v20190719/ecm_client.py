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
from tencentcloud.ecm.v20190719 import models


class EcmClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'ecm.tencentcloudapi.com'
    _service = 'ecm'


    def AllocateAddresses(self, request):
        """This API is used to apply for one or multiple EIPs.

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignIpv6Addresses(self, request):
        """This API is used to apply for an IPv6 address for an ENI.

        :param request: Request instance for AssignIpv6Addresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.AssignIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignPrivateIpAddresses(self, request):
        """This API is used to apply for a private IP for an ENI.

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignPrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.AssignPrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateAddress(self, request):
        """This API is used to bind an EIP to an instance or the specified private IP of an ENI.
        Binding an EIP to an instance (ECM) is essentially to bind it to the primary private IP of the primary ENI of the instance.
        When you bind an EIP to the private IP of the specified ENI, if the private IP is already bound to an EIP or public IP, a failure will be reported, and you must unbind it first before you can bind it to a new EIP.
        Only EIPs in `UNBIND` status can be bound to a private IP.

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """This API is used to bind a security group.

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachNetworkInterface(self, request):
        """This API is used to bind an ENI to a CVM instance.

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.AttachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeregisterTargets(self, request):
        """This API is used to batch unbind real servers.

        :param request: Request instance for BatchDeregisterTargets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.BatchDeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.BatchDeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeregisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeregisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyTargetWeight(self, request):
        """This API is used to batch modify the forwarding weights of the real servers bound to a listener.

        :param request: Request instance for BatchModifyTargetWeight.
        :type request: :class:`tencentcloud.ecm.v20190719.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.BatchModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRegisterTargets(self, request):
        """This API is used to batch bind backend targets.

        :param request: Request instance for BatchRegisterTargets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.BatchRegisterTargetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.BatchRegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRegisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRegisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHaVip(self, request):
        """This API is used to create an HAVIP.

        :param request: Request instance for CreateHaVip.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateHaVipRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateHaVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHaVip", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHaVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateImage(self, request):
        """This API is used to create an image with the system disk of an instance. The image can be used to create instances.

        :param request: Request instance for CreateImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKeyPair(self, request):
        """This API is used to create an `OpenSSH RSA` key pair, which can be used to log in to a Linux instance.

        :param request: Request instance for CreateKeyPair.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateKeyPairRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateKeyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateListener(self, request):
        """This API is used to create a CLB listener.

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancer(self, request):
        """This API is used to purchase a CLB instance.

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModule(self, request):
        """This API is used to create a module.

        :param request: Request instance for CreateModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateModuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkInterface(self, request):
        """This API is used to create an ENI.

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRouteTable(self, request):
        """After a VPC is created, the system will create a default route table, with which all new subnets will be associated. By default, you can use the default route table to manage your routing policies. If you have multiple routing policies, you can call the API for route table creation to create more route tables to manage your routing policies.

        :param request: Request instance for CreateRouteTable.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateRouteTableRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoutes(self, request):
        """This API is used to create a routing policy.

        :param request: Request instance for CreateRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroup(self, request):
        """This API is used to create a security group.

        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupPolicies(self, request):
        """<p>This API is used to create a security group policy.</p>
        <p>In the `SecurityGroupPolicySet` parameter:</p>
        <ul>
        <li>`Version`: the version number of a security group policy, which automatically increases by one each time you update the security policy, to prevent expiration of the updated routing policies. If it is left empty, any conflicts will be ignored.</li>
        <li>When creating the `Egress` and `Ingress` polices,<ul>
        <li><code>Protocol</code>: <code>TCP</code>, <code>UDP</code>, <code>ICMP</code>, <code>GRE</code>, or <code>ALL</code>.</li>
        <li>`CidrBlock`: a CIDR block in the correct format. In a classic network, if a `CidrBlock` contains private IPs on Tencent Cloud for devices under your account other than CVMs, it does not mean this policy allows you to access these devices. The network isolation policies between tenants take priority over the private network policies in security groups.</li>
        <li>`SecurityGroupId`: ID of the security group. It can be the ID of security group to be modified, or the ID of other security group in the same project. All private IPs of all CVMs under the security group will be covered. If this field is used, the policy will automatically change according to the CVM associated with the group ID while being used to match network messages. You don’t need to change it manually.</li>
        <li>`Port`: a single port number such as 80, or a port range in the format of “8000-8010”. You may use this field only if the `Protocol` field takes the value `TCP` or `UDP`. Otherwise `Protocol` and `Port` are mutually exclusive.</li>
        <li>`Action`: only allows `ACCEPT` or `DROP`.</li>
        <li>`CidrBlock`, `SecurityGroupId`, and `AddressTemplate` are mutually exclusive. `Protocol` + `Port` and `ServiceTemplate` are mutually exclusive.</li>
        <li>You can only create policies in one direction in each request. To specify the `PolicyIndex` parameter, use the same index number in policies.</li>
        </ul></li></ul>
        <p>Default API request rate limit: 20 requests/sec.</p>

        :param request: Request instance for CreateSecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubnet(self, request):
        """This API is used to create a subnet. After the subnet is created successfully, it will become the default subnet for the AZ.

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpc(self, request):
        """This API is used to create a VPC.

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpc", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHaVip(self, request):
        """This API is used to delete an HAVIP.

        :param request: Request instance for DeleteHaVip.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteHaVipRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteHaVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHaVip", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHaVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteImage(self, request):
        """This API is used to delete an image.

        :param request: Request instance for DeleteImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteImage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListener(self, request):
        """This API is used to delete a CLB listener.

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListener", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancer(self, request):
        """This API is used to delete a CLB instance.

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancerListeners(self, request):
        """This API is used to delete multiple CLB listeners.

        :param request: Request instance for DeleteLoadBalancerListeners.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerListenersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancerListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModule(self, request):
        """This API is used to delete a business module.

        :param request: Request instance for DeleteModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteModuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkInterface(self, request):
        """This API is used to delete an ENI.

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRouteTable(self, request):
        """This API is used to delete a route table.

        :param request: Request instance for DeleteRouteTable.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteRouteTableRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoutes(self, request):
        """This API is used to batch delete routing policies from a route table.

        :param request: Request instance for DeleteRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroup(self, request):
        """Only security groups under the current account can be deleted.
        A security group cannot be deleted directly if its instance ID is used in the policy of another security group. In this case, you need to modify the policy first before deleting the security group.
        Deleted security groups cannot be recovered. Therefore, call this API with caution.

        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroupPolicies(self, request):
        """`SecurityGroupPolicySet.Version` is used to specify the version of the security group to be manipulated. If the `Version` value passed in differs from the current latest version of the security group, a failure will be returned. If `Version` is not passed in, the policy of the specified `PolicyIndex` will be deleted directly.

        :param request: Request instance for DeleteSecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshots(self, request):
        """This API is used to delete a snapshot.

        * Only snapshots in the `NORMAL` state can be deleted. To query the state of a snapshot, you can call the [DescribeSnapshots](https://intl.cloud.tencent.com/document/product/362/15647?from_cn_redirect=1) API and check the `SnapshotState` field in the response.
        * Batch operations are supported. If there is any snapshot that cannot be deleted, the operation will not be performed and a specific error code will be returned.

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubnet(self, request):
        """This API is used to delete a subnet. If the subnet is the current default subnet in the AZ, after it is deleted, the default subnet automatically created by the system rather than the last subnet created by you will be used as the new default subnet. If the new default subnet does not meet your needs, you can call the API for setting the default subnet to configure it.

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpc(self, request):
        """This API is used to delete a VPC.

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressQuota(self, request):
        """This API is used to query the quota information of the EIP under your account in the current region.

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddresses(self, request):
        """This API is used to query the list of EIPs.

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaseOverview(self, request):
        """This API is used to get the basic data displayed on the overview page.

        :param request: Request instance for DescribeBaseOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeBaseOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeBaseOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaseOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaseOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfig(self, request):
        """This API is used to get the limits of data such as bandwidth and disk.

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomImageTask(self, request):
        """This API is used to query an image import task.

        :param request: Request instance for DescribeCustomImageTask.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeCustomImageTaskRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeCustomImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultSubnet(self, request):
        """This API is used to query the default subnet in an AZ.

        :param request: Request instance for DescribeDefaultSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHaVips(self, request):
        """This API is used to query the list of HAVIPs.

        :param request: Request instance for DescribeHaVips.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeHaVipsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeHaVipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHaVips", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHaVipsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImage(self, request):
        """This API is used to display the list of images.

        :param request: Request instance for DescribeImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImportImageOs(self, request):
        """This API is used to query the list of operating systems supported by an image imported from an external resource.

        :param request: Request instance for DescribeImportImageOs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeImportImageOsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeImportImageOsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImportImageOs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImportImageOsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTypeConfig(self, request):
        """This API is used to get the list of model configurations.

        :param request: Request instance for DescribeInstanceTypeConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceTypeConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceTypeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTypeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTypeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceVncUrl(self, request):
        """This API is used to query the VNC URL of an instance.

        :param request: Request instance for DescribeInstanceVncUrl.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceVncUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceVncUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceVncUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """This API is used to get the information of an instance.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesResponse`

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


    def DescribeInstancesDeniedActions(self, request):
        """This API is used to get the information of prohibited operations by instance ID.

        :param request: Request instance for DescribeInstancesDeniedActions.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesDeniedActionsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListeners(self, request):
        """This API is used to query the list of CLB listeners.

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalanceTaskStatus(self, request):
        """This API is used to query the task status of a CLB instance.

        :param request: Request instance for DescribeLoadBalanceTaskStatus.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalanceTaskStatusRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalanceTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalanceTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalanceTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancers(self, request):
        """This API is used to query the list of CLB instances.

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModule(self, request):
        """This API is used to get the list of modules.

        :param request: Request instance for DescribeModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModuleDetail(self, request):
        """This API is used to display the details of a module.

        :param request: Request instance for DescribeModuleDetail.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleDetailRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonthPeakNetwork(self, request):
        """This API is used to get the monthly peak and billable inbound/outbound bandwidth values of your node.

        :param request: Request instance for DescribeMonthPeakNetwork.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeMonthPeakNetworkRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeMonthPeakNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonthPeakNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonthPeakNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkInterfaces(self, request):
        """This API is used to query the list of ENIs.

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkInterfacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNode(self, request):
        """This API is used to get the list of nodes.

        :param request: Request instance for DescribeNode.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeNodeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePackingQuotaGroup(self, request):
        """This API is used to get the packing quota of a model in a region (when a virtual model is used, a set of correlated packing quotas will be returned).

        :param request: Request instance for DescribePackingQuotaGroup.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePackingQuotaGroupRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePackingQuotaGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackingQuotaGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackingQuotaGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePeakBaseOverview(self, request):
        """This API is used to get the peak data of basic information such as CPU, memory, and disk.

        :param request: Request instance for DescribePeakBaseOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePeakBaseOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePeakBaseOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePeakBaseOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePeakBaseOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePeakNetworkOverview(self, request):
        """This API is used to get the peak network data.

        :param request: Request instance for DescribePeakNetworkOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePeakNetworkOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePeakNetworkOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePeakNetworkOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePeakNetworkOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePriceRunInstance(self, request):
        """This API is used to query the price of an instance.

        :param request: Request instance for DescribePriceRunInstance.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePriceRunInstanceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePriceRunInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePriceRunInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePriceRunInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteConflicts(self, request):
        """This API is used to query the list of conflicts between a custom routing policy and a CCN routing policy.

        :param request: Request instance for DescribeRouteConflicts.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteConflictsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteConflictsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteConflicts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteConflictsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteTables(self, request):
        """This API is used to query the list of the objects in a route table.

        :param request: Request instance for DescribeRouteTables.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteTablesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupAssociationStatistics(self, request):
        """This API is used to query statistics on the instances associated with a security group.

        :param request: Request instance for DescribeSecurityGroupAssociationStatistics.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupAssociationStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupAssociationStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupAssociationStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupLimits(self, request):
        """This API is used to query the security group quota.

        :param request: Request instance for DescribeSecurityGroupLimits.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupLimitsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupPolicies(self, request):
        """This API is used to query a security group rule.

        :param request: Request instance for DescribeSecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroups(self, request):
        """This API is used to view a security group.

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshots(self, request):
        """This API is used to query the list of snapshots.

        * You can filter results by snapshot ID and the ID and type of the cloud disk for which the snapshot is created. The relationship between different filters is `AND`. For more information on filters, see `Filter`.
        * If no parameter is defined, the status of a certain number of snapshots under the current account will be returned. The number is specified by `Limit` and is 20 by default.

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnets(self, request):
        """This API is used to query the list of subnets.

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetHealth(self, request):
        """This API is used to get the health check status of a CLB real server.

        :param request: Request instance for DescribeTargetHealth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetHealthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetHealthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetHealth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetHealthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargets(self, request):
        """This API is used to query the list of the real servers bound to a CLB instance.

        :param request: Request instance for DescribeTargets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskResult(self, request):
        """This API is used to query the execution result of an EIP async task.

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """This API is used to get the status of an async task.

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcs(self, request):
        """This API is used to query the list of VPCs.

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachNetworkInterface(self, request):
        """This API is used to unbind an ENI from a CVM instance.

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.DetachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableRoutes(self, request):
        """This API is used to disable a subnet route.

        :param request: Request instance for DisableRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisableRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisableRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DisableRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateAddress(self, request):
        """This API is used to unbind an EIP.
        Only EIPs in `BIND` or `BIND_ENI` status can be unbound.
        Blocked EIPs cannot be unbound.

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisassociateAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateInstancesKeyPairs(self, request):
        """This API is used to unbind a key pair from an instance.

        :param request: Request instance for DisassociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisassociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisassociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """This API is used to unbind a security group.

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableRoutes(self, request):
        """This API is used to enable a disabled subnet route.
        This API verifies whether a CCN route will conflict with an existing route after it is enabled, and if so, you cannot enable it before you disable the conflicting route first.

        :param request: Request instance for EnableRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.EnableRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.EnableRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.EnableRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportImage(self, request):
        """This API is used to import an image from a CVM instance to an ECM instance.

        :param request: Request instance for ImportImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ImportImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImportImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportImage", params, headers=headers)
            response = json.loads(body)
            model = models.ImportImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigrateNetworkInterface(self, request):
        """This API is used to migrate an ENI.

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigratePrivateIpAddress(self, request):
        """This API is used to migrate a private IP from an ENI.
        It migrates a private IP from one ENI to another. Primary IPs cannot be migrated.
        The source and destination ENIs must be in the same subnet.

        :param request: Request instance for MigratePrivateIpAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.MigratePrivateIpAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigratePrivateIpAddress", params, headers=headers)
            response = json.loads(body)
            model = models.MigratePrivateIpAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressAttribute(self, request):
        """This API is used to modify EIP attributes.

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressesBandwidth(self, request):
        """This API is used to modify the EIP bandwidth.

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDefaultSubnet(self, request):
        """This API is used to modify the default subnet used when you create an instance in an AZ (if you don't specify the VPC parameter when creating the instance, `sunbetId` will be used).

        :param request: Request instance for ModifyDefaultSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDefaultSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHaVipAttribute(self, request):
        """This API is used to modify the attributes of an HAVIP.

        :param request: Request instance for ModifyHaVipAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyHaVipAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHaVipAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHaVipAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyImageAttribute(self, request):
        """This API is used to modify the attributes of an image.

        :param request: Request instance for ModifyImageAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyImageAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyImageAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesAttribute(self, request):
        """This API is used to modify the attributes of an instance.

        :param request: Request instance for ModifyInstancesAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIpv6AddressesAttribute(self, request):
        """This API is used to modify the IPv6 address attributes of an ENI.

        :param request: Request instance for ModifyIpv6AddressesAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyIpv6AddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIpv6AddressesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIpv6AddressesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyListener(self, request):
        """This API is used to modify the attributes of a CLB listener.

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyListener", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerAttributes(self, request):
        """This API is used to modify the attributes of a CLB instance.

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyLoadBalancerAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleConfig(self, request):
        """This API is used to modify the configuration of a module. You cannot modify the configuration of the module if it is associated with an instance.

        :param request: Request instance for ModifyModuleConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleDisableWanIp(self, request):
        """This API is used to specify whether to prohibit public IP assignment for a module.

        :param request: Request instance for ModifyModuleDisableWanIp.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleDisableWanIpRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleDisableWanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleDisableWanIp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleDisableWanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleImage(self, request):
        """This API is used to modify the default image of a module.

        :param request: Request instance for ModifyModuleImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleImage", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleIpDirect(self, request):
        """This API is used to modify the IP direct access of a module.

        :param request: Request instance for ModifyModuleIpDirect.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleIpDirectRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleIpDirectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleIpDirect", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleIpDirectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleName(self, request):
        """This API is used to rename a module.

        :param request: Request instance for ModifyModuleName.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNameRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleNetwork(self, request):
        """This API is used to modify the default bandwidth cap of a module.

        :param request: Request instance for ModifyModuleNetwork.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNetworkRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyModuleSecurityGroups(self, request):
        """This API is used to modify the default security group of a module.

        :param request: Request instance for ModifyModuleSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateIpAddressesAttribute(self, request):
        """This API is used to modify the private IP attributes of an ENI.

        :param request: Request instance for ModifyPrivateIpAddressesAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyPrivateIpAddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateIpAddressesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateIpAddressesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRouteTableAttribute(self, request):
        """This API is used to modify the attributes of a route table.

        :param request: Request instance for ModifyRouteTableAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyRouteTableAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRouteTableAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRouteTableAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupAttribute(self, request):
        """This API is used to modify the attributes of a security group.

        :param request: Request instance for ModifySecurityGroupAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupPolicies(self, request):
        """This API is used to modify the outbound and inbound rules of a security group.

        :param request: Request instance for ModifySecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubnetAttribute(self, request):
        """This API is used to modify the attributes of a subnet.

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubnetAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubnetAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetPort(self, request):
        """This API is used to modify the port of a real server bound to a listener.

        :param request: Request instance for ModifyTargetPort.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetPortRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetWeight(self, request):
        """This API is used to modify the forwarding weight of a real server bound to a listener.

        :param request: Request instance for ModifyTargetWeight.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcAttribute(self, request):
        """This API is used to modify the attributes of a VPC.

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootInstances(self, request):
        """This API is used to restart an instance. Only instances in `RUNNING` status can be restarted. The instance status will become `REBOOTING` when the API is called successfully and will become `RUNNING` when the instance is restarted successfully. Forced restart is supported. Just like powering off a physical PC and restarting it, a forced restart may cause data loss or file system corruption. Make sure that you use this API only when the server cannot be restarted normally.

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RebootInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseAddresses(self, request):
        """This API is used to release one or multiple EIPs.
        This operation is irreversible. Once you release an EIP, the IP address associated with it will no longer belong to you.
        Only EIPs in `UNBIND` status can be released.

        :param request: Request instance for ReleaseAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReleaseAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReleaseAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseIpv6Addresses(self, request):
        """This API is used to release the IPv6 addresses of an ENI.

        :param request: Request instance for ReleaseIpv6Addresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReleaseIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReleaseIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemovePrivateIpAddresses(self, request):
        """This API is used to return the private IPs of an ENI.
        To return the secondary private IPs of an ENI, the API will automatically unbind them from the ENI. The primary private IP of the ENI cannot be returned.

        :param request: Request instance for RemovePrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemovePrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.RemovePrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceRouteTableAssociation(self, request):
        """This API is used to modify the route table associated with a subnet. A subnet can be associated with only one route table.

        :param request: Request instance for ReplaceRouteTableAssociation.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReplaceRouteTableAssociationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceRouteTableAssociation", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceRouteTableAssociationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceRoutes(self, request):
        """This API is used to replace a routing policy.

        :param request: Request instance for ReplaceRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReplaceRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReplaceRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceSecurityGroupPolicy(self, request):
        """This API is used to replace a single routing rule of a security group. You can replace only one rule in a single direction in one request and must specify the index (PolicyIndex).

        :param request: Request instance for ReplaceSecurityGroupPolicy.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReplaceSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceSecurityGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceSecurityGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstances(self, request):
        """This API is used to reinstall an instance. If you specify the `ImageId` parameter, the specified image will be used; otherwise, the image used by the current instance will be used. If you don't specify the password, a password will be sent later in Message Center.

        :param request: Request instance for ResetInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstancesMaxBandwidth(self, request):
        """This API is used to reset the bandwidth cap of an instance.

        :param request: Request instance for ResetInstancesMaxBandwidth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstancesMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstancesPassword(self, request):
        """This API is used to reset the password for a running status. You need to explicitly specify the `ForceStop` parameter; otherwise, you can reset the password only for instances that have been shut down.

        :param request: Request instance for ResetInstancesPassword.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstancesPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetRoutes(self, request):
        """This API is used to reset a route table name and all routing policies.

        :param request: Request instance for ResetRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ResetRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunInstances(self, request):
        """This API is used to create an ECM instance.

        :param request: Request instance for RunInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerSecurityGroups(self, request):
        """This API is used to configure security groups for a CLB instance.

        :param request: Request instance for SetLoadBalancerSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SetLoadBalancerSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetSecurityGroupForLoadbalancers(self, request):
        """This API is used to bind or unbind a security group to or from multiple CLB instances.

        :param request: Request instance for SetSecurityGroupForLoadbalancers.
        :type request: :class:`tencentcloud.ecm.v20190719.models.SetSecurityGroupForLoadbalancersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SetSecurityGroupForLoadbalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetSecurityGroupForLoadbalancers", params, headers=headers)
            response = json.loads(body)
            model = models.SetSecurityGroupForLoadbalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartInstances(self, request):
        """This API is used to start an instance. Only instances in `STOPPED` status can be started. The instance status will become `STARTING` when this API is called successfully and will become `RUNNING` when the instance is started successfully.

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInstances(self, request):
        """Only instances in `RUNNING` status can be shut down.
        The instance status will become `STOPPING` when the API is called successfully and will become `STOPPED` when the instance is shut down successfully.
        Forced shutdown is supported. Just like powering off a physical PC, a forced shutdown may cause data loss or file system corruption. Make sure that you use this API only when the server cannot be shut down normally.

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstances(self, request):
        """This API is used to terminate an instance.

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.TerminateInstancesResponse`

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